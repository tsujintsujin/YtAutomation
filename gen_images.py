"""Generate one image per script segment through local ComfyUI (Qwen-Image 2.1).

usage: python gen_images.py scripts/pig-milk.json [--steps 25] [--size 1280x720] [--only 8,9]
Needs ComfyUI running on 127.0.0.1:8188 (D:/ComfyUI/ComfyUI-Start.bat).
Skips segments that already have an image in output/<slug>/img/, so it can be re-run after a stop.
"""
import argparse
import json
import time
from pathlib import Path

import requests

COMFY = "http://127.0.0.1:8188"
HERE = Path(__file__).parent

p = argparse.ArgumentParser()
p.add_argument("script")
p.add_argument("--steps", type=int, default=25)
p.add_argument("--size", default="1280x720")
p.add_argument("--seed", type=int, default=7)
p.add_argument("--only", default="", help="comma-separated segment ids")
a = p.parse_args()

script = json.loads(Path(a.script).read_text(encoding="utf-8"))
img_dir = HERE / "output" / Path(a.script).stem / "img"
img_dir.mkdir(parents=True, exist_ok=True)
w, h = map(int, a.size.split("x"))
only = {int(x) for x in a.only.split(",") if x}


def graph(prompt):
    return {
        "1": {"class_type": "UNETLoader", "inputs": {"unet_name": "qwen_image_2.1_int8_convrot.safetensors", "weight_dtype": "default"}},
        "2": {"class_type": "CLIPLoader", "inputs": {"clip_name": "qwen3vl_8b_w4a8_heretic.safetensors", "type": "qwen_image", "device": "default"}},
        "3": {"class_type": "VAELoader", "inputs": {"vae_name": "qwen_image_2.1_vae_bf16.safetensors"}},
        "4": {"class_type": "TextEncodeQwenImage21", "inputs": {"clip": ["2", 0], "prompt": prompt, "negative_prompt": script["negative"], "resolution": 1024}},
        "5": {"class_type": "EmptyLatentImage", "inputs": {"width": w, "height": h, "batch_size": 1}},
        "6": {"class_type": "KSampler", "inputs": {"model": ["1", 0], "positive": ["4", 0], "negative": ["4", 1], "latent_image": ["5", 0],
                                                  "seed": a.seed, "steps": a.steps, "cfg": 1, "sampler_name": "euler", "scheduler": "simple", "denoise": 1}},
        "7": {"class_type": "VAEDecode", "inputs": {"samples": ["6", 0], "vae": ["3", 0]}},
        "8": {"class_type": "SaveImage", "inputs": {"images": ["7", 0], "filename_prefix": "ytauto"}},
    }


for seg in script["segments"]:
    if (only and seg["id"] not in only) or (not only and any(img_dir.glob(f"{seg['id']:02d}.*"))):
        continue
    # cfg=1 turbo models ignore negative_prompt, so the negatives also ride in the positive text
    prompt = f"{script['style']}. " + (f"{script['character']}. " if seg["character"] else "") + seg["prompt"] + f". {script['negative']}."
    t0 = time.time()
    r = requests.post(f"{COMFY}/prompt", json={"prompt": graph(prompt)})
    r.raise_for_status()
    pid = r.json()["prompt_id"]
    while not (hist := requests.get(f"{COMFY}/history/{pid}").json()).get(pid):
        time.sleep(2)
    entry = hist[pid]
    if entry["status"].get("status_str") != "success":
        raise SystemExit(f"segment {seg['id']} failed: {entry['status']}")
    f = entry["outputs"]["8"]["images"][0]
    png = requests.get(f"{COMFY}/view", params={"filename": f["filename"], "subfolder": f["subfolder"], "type": f["type"]}).content
    for old in img_dir.glob(f"{seg['id']:02d}.*"):
        old.unlink()
    (img_dir / f"{seg['id']:02d}.png").write_bytes(png)
    print(f"{seg['id']:02d}  {time.time() - t0:5.1f}s  {seg['prompt'][:60]}", flush=True)
