"""Script JSON + one image per segment -> narrated MP4.

usage: tts/.venv/Scripts/python make_video.py scripts/pig-milk.json [--voice am_liam] [--speed 1.1]

Expects images at output/<slug>/img/01.png, 02.png ... (one per segment id).
Voices each segment with Kokoro, so every image lasts exactly as long as its line.
"""
import argparse
import json
import subprocess
from pathlib import Path

import imageio_ffmpeg
import numpy as np
import soundfile as sf
from kokoro_onnx import Kokoro
from PIL import Image, ImageChops

HERE = Path(__file__).parent
FFMPEG = imageio_ffmpeg.get_ffmpeg_exe()
FPS, W, H = 30, 1280, 720
PAUSE = {",": 0.12, ".": 0.35, "?": 0.4, "!": 0.35}  # silence after each piece, by its last char

p = argparse.ArgumentParser()
p.add_argument("script")
p.add_argument("--voice", default="am_liam")
p.add_argument("--speed", type=float, default=1.0)
a = p.parse_args()

script = json.loads(Path(a.script).read_text(encoding="utf-8"))
out = HERE / "output" / Path(a.script).stem
clips = out / "clips"
clips.mkdir(parents=True, exist_ok=True)

# 1. Voice: one Kokoro call per segment, glued with punctuation-sized pauses.
# ponytail: per-piece TTS loses cross-comma intonation; switch to per-sentence + forced alignment if it sounds choppy.
kokoro = Kokoro(str(HERE / "tts/models/kokoro-v1.0.onnx"), str(HERE / "tts/models/voices-v1.0.bin"))
audio, bounds, sr = [], [0.0], 24000
for seg in script["segments"]:
    samples, sr = kokoro.create(seg["text"], voice=a.voice, speed=a.speed, lang="en-us")
    audio += [samples, np.zeros(int(sr * PAUSE.get(seg["text"][-1], 0.2)), dtype=samples.dtype)]
    bounds.append(bounds[-1] + (len(samples) / sr) + PAUSE.get(seg["text"][-1], 0.2))
sf.write(out / "voice.wav", np.concatenate(audio), sr)

def trim_border(src, dst):
    """Cut off any flat margin/frame an image model added (compares against the corner colour)."""
    im = Image.open(src).convert("RGB")
    bg = Image.new("RGB", im.size, im.getpixel((0, 0)))
    box = ImageChops.difference(im, bg).convert("L").point(lambda v: 255 if v > 24 else 0).getbbox()
    if box and box != (0, 0, *im.size) and (box[2] - box[0]) * (box[3] - box[1]) > 0.6 * im.width * im.height:
        l, t, r, b = box
        im = im.crop((l + 6, t + 6, r - 6, b - 6))  # 6px more eats the frame's inner outline
    im.save(dst)


# 2. Video: each image gets a slow zoom for exactly its segment's frames (cumulative rounding keeps sync).
listing = []
for i, seg in enumerate(script["segments"]):
    img = clips / f"{seg['id']:02d}.png"
    trim_border(next((out / "img").glob(f"{seg['id']:02d}.*")), img)
    frames = round(bounds[i + 1] * FPS) - round(bounds[i] * FPS)
    z = f"1+0.08*on/{frames}" if i % 2 == 0 else f"1.08-0.08*on/{frames}"  # alternate zoom in / out
    clip = clips / f"{seg['id']:02d}.mp4"
    subprocess.run([FFMPEG, "-y", "-loglevel", "error", "-i", str(img), "-vf",
                    f"scale={W*2}:{H*2}:force_original_aspect_ratio=increase,crop={W*2}:{H*2},zoompan=z='{z}':d={frames}:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s={W}x{H}:fps={FPS}",
                    "-frames:v", str(frames), "-c:v", "libx264", "-pix_fmt", "yuv420p", str(clip)], check=True)
    listing.append(f"file '{clip.as_posix()}'")

(out / "clips.txt").write_text("\n".join(listing), encoding="utf-8")
final = out / f"{Path(a.script).stem}.mp4"
subprocess.run([FFMPEG, "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", str(out / "clips.txt"),
                "-i", str(out / "voice.wav"), "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", "-shortest", str(final)], check=True)
print(f"{final}: {bounds[-1]:.1f}s, {len(script['segments'])} images")
