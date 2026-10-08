"""Voice: script.json -> audio/NNN.wav, voice.wav, timings.json. Needs no images.
--images-only: the separate image prep for the edit (img/NNN.* -> img_clean/NNN.jpg, border-trimmed, 1920x1080).
--if-needed: skip the voice when voice.wav and timings.json exist and were made from the same narration text, voice
and speed (recorded in voice-settings.json), even if script.json was rebuilt with new image prompts.

usage: tts/.venv/Scripts/python voice.py output/<slug> [--voice am_santa] [--speed 1.0]

Whole sentences are spoken in one TTS call, so the voice keeps its flow and only falls at a real sentence end
(2026-10-07: the old one-call-per-comma-piece voice sounded choppy, every pause like a period, and short pieces were
mispronounced). A sentence usually spans several 2-4 s segments. Where each one starts inside the sentence comes
from the model itself: tts/models/kokoro-v1.0-timestamped.onnx is the same Kokoro v1.0 (identical audio, checked)
exported with a duration for every phoneme, so a cut sits in the middle of the word gap between two segments.
Commas get no pause from this voice (25 ms, tested 2026-10-08: punctuation swaps, misaki phonemes, longer
durations inside the model, cut-in silence and splitting all failed or sounded wrong), so the story is written
with at most one comma per sentence (HANDOFF "Rules for the story text"). Segment N owns [start, end) where end
includes any trailing pause, so the images tile the whole voice track with no gaps.
"""
import argparse
import hashlib
import json
import re
import sys
import time
from pathlib import Path

import numpy as np
import onnxruntime
import soundfile as sf
from kokoro_onnx import Kokoro
from PIL import Image, ImageChops, ImageOps

HERE = Path(__file__).parent
PAUSE = {".": 0.45, "!": 0.45, "?": 0.5}  # silence after a sentence, by its last mark
NO_MARK = 0.2  # the script ends without a sentence mark
SR = 24000
MAX_TOKENS = 510  # Kokoro's limit per call
SENTENCE_END = re.compile(r'[.!?]+["”’)]*$')
METHOD = "sentences+timestamped"  # recorded in voice-settings.json, so a voice made the old way is redone


def sentences(segs):
    """Consecutive segments, grouped so each group ends where a sentence ends."""
    groups, cur = [], []
    for s in segs:
        cur.append(s)
        if SENTENCE_END.search(s["text"].strip()):
            groups.append(cur)
            cur = []
    return groups + ([cur] if cur else [])


def speak(kokoro, model, group, voice, speed):
    """One sentence group -> (audio, [start second of each segment in it]). Each segment is phonemized on its own
    and the pieces joined with a space, so the token where each segment begins is known exactly; the model's
    per-token durations then give the time of the word gap before it."""
    phon = [kokoro.tokenizer.phonemize(x["text"].strip(), "en-us") for x in group]
    tokens = kokoro.tokenizer.tokenize(" ".join(phon))
    first = [len(kokoro.tokenizer.tokenize(" ".join(phon[:i]) + " ")) if i else 0 for i in range(len(group))]
    if len(tokens) > MAX_TOKENS:                   # too long for one call: speak it in two halves, split at a segment
        h = len(group) // 2
        if h == 0:
            raise ValueError(f"segment {group[0]['id']} alone is {len(tokens)} phoneme tokens (max {MAX_TOKENS})")
        a1, s1 = speak(kokoro, model, group[:h], voice, speed)
        a2, s2 = speak(kokoro, model, group[h:], voice, speed)
        return np.concatenate([a1, a2]), s1 + [len(a1) / SR + x for x in s2]
    style = kokoro.get_voice_style(voice)[len(tokens)].reshape(1, 256).astype(np.float32)
    wav, dur = model.run(None, {"input_ids": np.array([[0, *tokens, 0]], dtype=np.int64), "style": style,
                                "speed": np.array([speed], dtype=np.float32)})
    wav, dur = wav.ravel(), dur.ravel()
    edge = np.concatenate([[0], np.cumsum(dur)]) * len(wav) / dur.sum()   # edge[k] = sample where input k starts
    # input k = token k-1 (k=0 and the last are the model's padding). Keep speech only: from the first token to
    # the last spoken one, 50 ms either side. The silence the model gives the closing mark is dropped: the sentence
    # pause after the group (PAUSE) replaces it, otherwise every sentence end got two pauses.
    spoken = len(kokoro.tokenizer.tokenize(" ".join(phon).rstrip(' .,!?;:"”’)…—')))
    lo, hi = max(0, int(edge[1] - 0.05 * SR)), min(len(wav), int(edge[spoken + 1] + 0.05 * SR))
    loud = np.flatnonzero(np.abs(wav[lo:hi]) > 0.01 * np.abs(wav).max())   # then trim to the first/last sound (-40 dB)
    if len(loud):
        lo, hi = lo + max(0, loud[0] - int(0.03 * SR)), lo + min(hi - lo, loud[-1] + int(0.03 * SR))
    starts = [0.0] + [((edge[f] + edge[f + 1]) / 2 - lo) / SR for f in first[1:]]   # middle of the space token
    return wav[lo:hi], starts


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
    settings = {"voice": voice, "speed": a.speed, "texts": texts, "method": METHOD}
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
    kokoro = Kokoro(str(HERE / "tts/models/kokoro-v1.0.onnx"), str(HERE / "tts/models/voices-v1.0.bin"))  # phonemizer + voices
    model = onnxruntime.InferenceSession(str(HERE / "tts/models/kokoro-v1.0-timestamped.onnx"))
    groups = sentences(segs)
    full, starts, t, sr = [], {}, 0.0, SR
    for g in groups:
        samples, inner = speak(kokoro, model, g, voice, a.speed)
        end = SENTENCE_END.search(g[-1]["text"].strip())
        pause = np.zeros(int(sr * (PAUSE[end.group()[0]] if end else NO_MARK)), dtype=samples.dtype)
        full += [samples, pause]
        for x, st in zip(g, inner):
            starts[x["id"]] = t + st
        t += (len(samples) + len(pause)) / sr       # sample-exact, so timing cannot drift from voice.wav
    wav = np.concatenate(full)
    sf.write(out / "voice.wav", wav, sr)
    order = [x["id"] for x in segs]
    timings = [{"id": i, "start": round(starts[i], 4), "end": round(starts[order[k + 1]] if k + 1 < len(order) else t, 4)}
               for k, i in enumerate(order)]
    for x in timings:                             # per-segment slices, as before (not used by the edit)
        sf.write(out / "audio" / f"{x['id']:03d}.wav", wav[int(x["start"] * sr):int(x["end"] * sr)], sr)

    # 6 s per image is Justin's hard max. Length here includes the trailing pause (= how long the image shows).
    long = [x for x in timings if x["end"] - x["start"] > 6.0]
    for x in long:
        print(f"OVER 6s: segment {x['id']} is {x['end'] - x['start']:.2f}s", file=sys.stderr)

    (out / "timings.json").write_text(json.dumps(timings, indent=1), encoding="utf-8")
    (out / "voice-settings.json").write_text(json.dumps(settings), encoding="utf-8")
    print(json.dumps({"ok": True, "folder": str(out), "voice": voice, "segments": len(segs),
                      "seconds": round(t, 2), "took": round(time.time() - t0, 1), "sentences": len(groups),
                      "over_6s": [{"id": x["id"], "seconds": round(x["end"] - x["start"], 2)} for x in long]}))


if __name__ == "__main__":
    main()
