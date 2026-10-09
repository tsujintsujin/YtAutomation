"""Voice with Chatterbox: script.json -> audio/NNN.wav, voice.wav, timings.json, voice-settings.json.
The same files voice.py (Kokoro) makes, so images, subtitles and OpenCut need no change.

usage: chatterbox/.venv/Scripts/python voice_cb.py output/<slug> [--if-needed] [--preview N]

The channel voice is Mark (tts/samples/voices/29_mark.mp3, Justin 2026-10-09), Chatterbox Standard with its default
settings. Like voice.py, whole sentences are spoken in one take, so the voice keeps its flow. A sentence usually spans
several 2-4 s segments; Chatterbox gives no word times, so Whisper (small.en, CPU) listens to each take and the image
cut between two segments goes in the middle of the gap between their words. Whisper also catches a take where
Chatterbox dropped or repeated words: that sentence is made again (3 tries), then the step fails with the segment.
Commas need no rules here: Chatterbox pauses at them.

--preview N: only the first N sentences, into output/<slug>/voice-preview/ (the real voice files are not touched).
The Chatterbox page (:7861) is closed first if it is open: the 6 GB card holds one Chatterbox model.
"""
import argparse
import difflib
import hashlib
import json
import os
import re
import subprocess
import sys
import time
import urllib.request
from pathlib import Path

os.environ["TQDM_DISABLE"] = "1"         # Chatterbox draws a progress bar per sentence: ~1 MB of noise in n8n's output

import numpy as np
import soundfile as sf
import torch

HERE = Path(__file__).parent
REF = HERE / "tts" / "samples" / "voices" / "29_mark.mp3"
PAUSE = {".": 0.45, "!": 0.45, "?": 0.5}  # silence after a sentence, by its last mark (same as voice.py)
NO_MARK = 0.2
SENTENCE_END = re.compile(r'[.!?]+["”’)]*$')
METHOD = "chatterbox-standard+whisper"  # recorded in voice-settings.json, so a Kokoro voice is redone
TRIES = 3
MATCH = 0.85                            # share of words Whisper must hear as written (spelling of numbers etc. varies)


def sentences(segs):
    """Consecutive segments, grouped so each group ends where a sentence ends (as voice.py)."""
    groups, cur = [], []
    for s in segs:
        cur.append(s)
        if SENTENCE_END.search(s["text"].strip()):
            groups.append(cur)
            cur = []
    return groups + ([cur] if cur else [])


def words(text):
    return [w for w in re.sub(r"[^a-z0-9' ]+", " ", text.lower().replace("’", "'")).split() if w.strip("'")]


def close_page():
    """The Chatterbox page keeps its model on the GPU; two will not fit on 6 GB."""
    try:
        urllib.request.urlopen("http://127.0.0.1:7861/", timeout=2)
    except Exception:
        return False
    subprocess.run(["powershell", "-NoProfile", "-Command",
                    "Get-CimInstance Win32_Process | ? { $_.Name -eq 'cmd.exe' -and $_.CommandLine -match "
                    "'title Chatterbox :7861' } | % { taskkill /F /T /PID $_.ProcessId | Out-Null }"],
                   capture_output=True, timeout=60)
    time.sleep(3)
    return True


def trim(wav, sr):
    """Drop the silence Chatterbox leaves before and after the speech (-40 dB, 30 ms kept)."""
    loud = np.flatnonzero(np.abs(wav) > 0.01 * np.abs(wav).max())
    if not len(loud):
        return wav
    return wav[max(0, loud[0] - int(0.03 * sr)):loud[-1] + int(0.03 * sr)]


def hear(whisper, wav, sr):
    """Whisper's words with their start/end seconds."""
    x = np.interp(np.arange(0, len(wav), sr / 16000), np.arange(len(wav)), wav).astype(np.float32)
    segs, _ = whisper.transcribe(x, language="en", word_timestamps=True, beam_size=5)
    return [(w, ww.start, ww.end) for s in segs for ww in (s.words or []) for w in words(ww.word)]


def cuts(group, heard, length):
    """Second (inside the take) where each segment of the group starts: the middle of the gap between the last
    word of the segment before and the first word of this one, found by lining Whisper's words up with the script's."""
    script = [words(x["text"]) for x in group]
    flat = [w for ws in script for w in ws]
    pos = {}                                                  # script word index -> heard word index
    for a, b, n in difflib.SequenceMatcher(None, flat, [h[0] for h in heard], autojunk=False).get_matching_blocks():
        for k in range(n):
            pos[a + k] = b + k
    starts, i = [0.0], 0
    for ws in script[:-1]:
        i += len(ws)                                          # first script word of the next segment
        left = [heard[pos[j]][2] for j in range(i - 1, -1, -1) if j in pos][:1]
        right = [heard[pos[j]][1] for j in range(i, len(flat)) if j in pos][:1]
        if left and right and right[0] >= left[0]:
            starts.append((left[0] + right[0]) / 2)
        else:                                                 # no matched word on one side: share by word count
            starts.append(length * i / max(1, len(flat)))
    return starts


def main():
    p = argparse.ArgumentParser()
    p.add_argument("folder")
    p.add_argument("--if-needed", action="store_true", help="skip if the voice is already made this way")
    p.add_argument("--preview", type=int, default=0, help="only the first N sentences, into voice-preview/")
    a = p.parse_args()

    t0 = time.time()
    out = Path(a.folder).resolve()
    segs = json.loads((out / "script.json").read_text(encoding="utf-8"))["segments"]
    texts = hashlib.sha1(json.dumps([s["text"] for s in segs]).encode("utf-8")).hexdigest()
    settings = {"engine": "chatterbox", "ref": REF.name, "texts": texts, "method": METHOD}
    done = [out / "voice.wav", out / "timings.json"]
    made_with = json.loads((out / "voice-settings.json").read_text(encoding="utf-8")) if (out / "voice-settings.json").exists() else None
    if a.if_needed and not a.preview and made_with == settings and all(f.exists() for f in done):
        timings = json.loads((out / "timings.json").read_text(encoding="utf-8"))
        print(json.dumps({"ok": True, "folder": str(out), "voice": "chatterbox:" + REF.stem, "segments": len(timings),
                          "seconds": timings[-1]["end"], "took": 0, "skipped": "already up to date", "over_6s": []}))
        return

    groups = sentences(segs)[:a.preview] if a.preview else sentences(segs)
    dest = out / "voice-preview" if a.preview else out
    closed = close_page()
    from chatterbox.tts import ChatterboxTTS                  # after the page is closed: loading needs the GPU
    from faster_whisper import WhisperModel
    model = ChatterboxTTS.from_pretrained(device="cuda" if torch.cuda.is_available() else "cpu")
    model.prepare_conditionals(str(REF))                      # Mark, read once; default exaggeration 0.5
    whisper = WhisperModel("small.en", device="cpu", compute_type="int8")
    sr = model.sr
    print(f"loaded in {time.time() - t0:.0f}s{' (closed the Chatterbox page)' if closed else ''}; "
          f"{len(groups)} sentences", file=sys.stderr, flush=True)

    full, starts, t, retried = [], {}, 0.0, []
    for n, g in enumerate(groups, 1):
        text = " ".join(x["text"].strip() for x in g)
        want = words(text)
        for k in range(TRIES):
            torch.manual_seed(1000 * n + k)                   # same take again on a rerun; a retry gets a new one
            wav = trim(model.generate(text).squeeze().cpu().numpy(), sr)   # Standard, default settings
            heard = hear(whisper, wav, sr)
            score = difflib.SequenceMatcher(None, want, [h[0] for h in heard], autojunk=False).ratio()
            if score >= MATCH:
                break
            print(f"  segments {g[0]['id']}-{g[-1]['id']}: heard {score:.0%} of the words, trying again",
                  file=sys.stderr, flush=True)
        else:
            raise SystemExit(f"segments {g[0]['id']}-{g[-1]['id']}: after {TRIES} takes Whisper still heard only "
                             f"{score:.0%} of the words.\n  script: {text}\n  heard:  {' '.join(h[0] for h in heard)}")
        if k:
            retried.append(g[0]["id"])
        end = SENTENCE_END.search(g[-1]["text"].strip())
        pause = np.zeros(int(sr * (PAUSE[end.group()[0]] if end else NO_MARK)), dtype=wav.dtype)
        for x, st in zip(g, cuts(g, heard, len(wav) / sr)):
            starts[x["id"]] = t + st
        full += [wav, pause]
        t += (len(wav) + len(pause)) / sr                     # sample-exact, so timing cannot drift from voice.wav
        print(f"  {n}/{len(groups)} segments {g[0]['id']}-{g[-1]['id']}: {len(wav) / sr:.1f}s, "
              f"{time.time() - t0:.0f}s so far", file=sys.stderr, flush=True)

    dest.mkdir(exist_ok=True)
    (dest / "audio").mkdir(exist_ok=True)
    wav = np.concatenate(full)
    sf.write(dest / "voice.wav", wav, sr)
    order = [x["id"] for g in groups for x in g]
    timings = [{"id": i, "start": round(starts[i], 4), "end": round(starts[order[k + 1]] if k + 1 < len(order) else t, 4)}
               for k, i in enumerate(order)]
    for x in timings:                                         # per-segment slices, as voice.py (not used by the edit)
        sf.write(dest / "audio" / f"{x['id']:03d}.wav", wav[int(x["start"] * sr):int(x["end"] * sr)], sr)
    long = [x for x in timings if x["end"] - x["start"] > 6.0]   # 6 s per image is Justin's hard max
    for x in long:
        print(f"OVER 6s: segment {x['id']} is {x['end'] - x['start']:.2f}s", file=sys.stderr)
    (dest / "timings.json").write_text(json.dumps(timings, indent=1), encoding="utf-8")
    if not a.preview:
        (dest / "voice-settings.json").write_text(json.dumps(settings), encoding="utf-8")
    print(json.dumps({"ok": True, "folder": str(dest), "voice": "chatterbox:" + REF.stem, "segments": len(timings),
                      "seconds": round(t, 2), "took": round(time.time() - t0, 1), "sentences": len(groups),
                      "retried": retried, "over_6s": [{"id": x["id"], "seconds": round(x["end"] - x["start"], 2)} for x in long]}))


if __name__ == "__main__":
    main()
