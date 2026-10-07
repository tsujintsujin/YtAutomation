"""Voice: script.json -> audio/NNN.wav, voice.wav, timings.json. Needs no images.
--images-only: the separate image prep for the edit (img/NNN.* -> img_clean/NNN.jpg, border-trimmed, 1920x1080).
--if-needed: skip the voice when voice.wav and timings.json exist and were made from the same narration text, voice
and speed (recorded in voice-settings.json), even if script.json was rebuilt with new image prompts.

usage: tts/.venv/Scripts/python voice.py output/<slug> [--voice am_santa] [--speed 1.0]

Each segment is split after every punctuation mark; one TTS call per piece, a punctuation-sized
pause after each (mid-segment too), cumulative timing. Segment N owns [start, end) where end includes its trailing pause, so
the images tile the whole voice track with no gaps.
"""
import argparse
import hashlib
import json
import re
import sys
import time
from pathlib import Path

import numpy as np
import soundfile as sf
from kokoro_onnx import Kokoro
from PIL import Image, ImageChops, ImageOps

HERE = Path(__file__).parent
PAUSE = {",": 0.22, ";": 0.22, ":": 0.22, ".": 0.45, "!": 0.45, "?": 0.5}  # silence after each piece, by its last mark
NO_MARK = 0.2  # segment cut mid-sentence (no punctuation at its end)


def pieces(text):
    """Split a segment after every punctuation mark (so a period mid-segment gets its own pause).
    A mark only counts when followed by a space or the end: "3.5" stays whole, "..." is one mark."""
    return re.findall(r'\S.*?(?:[,;:.!?]+["”’)]*(?=\s|$)|$)', text)


def pause_after(piece):
    return PAUSE.get(piece.rstrip('"”’)')[-1:], NO_MARK)


def trim_border(src, dst, size=(1920, 1080)):
    """Cut off any flat margin/frame an image model added (compares against the corner colour),
    then cover-crop to exactly 1920x1080 so OpenCut never letterboxes and its canvas (which takes
    the first imported image's size) is always 1080p with even dimensions."""
    im = Image.open(src).convert("RGB")
    bg = Image.new("RGB", im.size, im.getpixel((0, 0)))
    box = ImageChops.difference(im, bg).convert("L").point(lambda v: 255 if v > 24 else 0).getbbox()
    if box and box != (0, 0, *im.size) and (box[2] - box[0]) * (box[3] - box[1]) > 0.6 * im.width * im.height:
        l, t, r, b = box
        im = im.crop((l + 6, t + 6, r - 6, b - 6))  # 6px more eats the frame's inner outline
    ImageOps.fit(im, size, Image.LANCZOS).save(dst, quality=95)


def main():
    p = argparse.ArgumentParser()
    p.add_argument("folder")
    p.add_argument("--voice", default=None, help="default: script.json voice, else am_santa")
    p.add_argument("--speed", type=float, default=1.0)
    p.add_argument("--images-only", action="store_true", help="only prepare img_clean/ for the edit")
    p.add_argument("--if-needed", action="store_true", help="skip the voice if it is already up to date")
    a = p.parse_args()

    t0 = time.time()
    out = Path(a.folder).resolve()
    script = json.loads((out / "script.json").read_text(encoding="utf-8"))
    segs = script["segments"]
    voice = a.voice or script.get("voice") or "am_santa"

    if a.images_only:                       # image prep for the edit: every image must exist
        imgs = {s["id"]: next(iter(sorted((out / "img").glob(f"{s['id']:03d}.*"))), None) for s in segs}
        missing = [i for i, f in imgs.items() if f is None]
        if not missing:
            (out / "img_clean").mkdir(exist_ok=True)
            for i, f in imgs.items():
                trim_border(f, out / "img_clean" / f"{i:03d}.jpg")
        print(json.dumps({"ok": not missing, "images": len(imgs) - len(missing), "images_missing": missing}))
        return

    done = [out / "voice.wav", out / "timings.json"]
    # The voice depends only on the narration, the voice and the speed, so a script.json rebuilt with new image
    # prompts must not redo it. Older voice-settings.json had no "texts": then fall back to the file dates once.
    texts = hashlib.sha1(json.dumps([s["text"] for s in segs]).encode("utf-8")).hexdigest()
    settings = {"voice": voice, "speed": a.speed, "texts": texts}
    made_with = json.loads((out / "voice-settings.json").read_text(encoding="utf-8")) if (out / "voice-settings.json").exists() else None
    if made_with and "texts" not in made_with and made_with == {"voice": voice, "speed": a.speed} and \
            all(f.exists() and f.stat().st_mtime > (out / "script.json").stat().st_mtime for f in done):
        made_with = settings
        (out / "voice-settings.json").write_text(json.dumps(settings), encoding="utf-8")
    if a.if_needed and made_with == settings and all(f.exists() for f in done):
        timings = json.loads((out / "timings.json").read_text(encoding="utf-8"))
        print(json.dumps({"ok": True, "folder": str(out), "voice": voice, "segments": len(timings),
                          "seconds": timings[-1]["end"], "took": 0, "skipped": "already up to date", "over_6s": []}))
        return

    (out / "audio").mkdir(exist_ok=True)
    kokoro = Kokoro(str(HERE / "tts/models/kokoro-v1.0.onnx"), str(HERE / "tts/models/voices-v1.0.bin"))
    full, timings, t, sr = [], [], 0.0, 24000
    for s in segs:
        parts = []
        for p in pieces(s["text"].strip()):
            samples, sr = kokoro.create(p, voice=voice, speed=a.speed, lang="en-us")
            parts += [samples, np.zeros(int(sr * pause_after(p)), dtype=samples.dtype)]
        piece = np.concatenate(parts)
        sf.write(out / "audio" / f"{s['id']:03d}.wav", piece, sr)
        full.append(piece)
        dur = len(piece) / sr  # sample-exact, so cumulative timing cannot drift from voice.wav
        timings.append({"id": s["id"], "start": round(t, 4), "end": round(t + dur, 4)})
        t += dur

    # 6 s per image is Justin's hard max. Length here includes the trailing pause (= how long the image shows).
    long = [x for x in timings if x["end"] - x["start"] > 6.0]
    for x in long:
        print(f"OVER 6s: segment {x['id']} is {x['end'] - x['start']:.2f}s", file=sys.stderr)

    sf.write(out / "voice.wav", np.concatenate(full), sr)
    (out / "timings.json").write_text(json.dumps(timings, indent=1), encoding="utf-8")
    (out / "voice-settings.json").write_text(json.dumps(settings), encoding="utf-8")
    print(json.dumps({"ok": True, "folder": str(out), "voice": voice, "segments": len(segs),
                      "seconds": round(t, 2), "took": round(time.time() - t0, 1),
                      "over_6s": [{"id": x["id"], "seconds": round(x["end"] - x["start"], 2)} for x in long]}))


if __name__ == "__main__":
    main()
