"""Voice with Chatterbox: script.json -> audio/NNN.wav, voice.wav, timings.json, voice-settings.json.
The same files voice.py (Kokoro) makes, so images, subtitles and OpenCut need no change.

usage: chatterbox/.venv/Scripts/python voice_cb.py output/<slug> [--if-needed] [--preview N | --only 133,134]

The channel voice is Mark (tts/samples/voices/29_mark.mp3, Justin 2026-10-09), Chatterbox Standard with its default
settings, or the channel's voice exaggeration/cfg from channels/<channel>/settings.json. Like voice.py, whole sentences are spoken in one take, so the voice keeps its flow. A sentence usually spans
several 2-4 s segments; Chatterbox gives no word times, so Whisper (small.en, CPU) listens to each take and the image
cut between two segments goes in the middle of the gap between their words. Commas need no rules: Chatterbox pauses.

Nothing in here stops the step (Justin 2026-10-09: "this needs to be 'it wont fail'"; run 473 died at sentence 102
of 180 on "thirty" vs Whisper's "30" and lost 26 minutes of narration):
- Whisper only picks the best take. A take is good when at most 1 word differs or 90% match (numbers count the same
  however they are written); otherwise up to 3 takes are made and the best is kept. Kept takes that were not good
  are listed in voice-check.json and the last line, to listen to; they never stop the run.
- Every finished take is saved in voice-parts/ at once; a rerun reuses the ones whose text is unchanged, so a stop
  (PC or n8n restart, Stop button) never redoes finished narration. Deleted once voice.wav is written.
- A group of segments longer than MAX_WORDS is spoken in parts split at a segment boundary: Chatterbox stops at
  1000 speech tokens (~40 s), so a very long take would be cut off.
- Models load from the disk cache only (HF_HUB_OFFLINE): no internet needed.
- The Chatterbox page (:7861) is closed first if open: the 6 GB card holds one Chatterbox model.

--preview N / --only IDS: only the first N sentences / the sentences holding those segments, into
output/<slug>/voice-preview/ (the real voice files are not touched).
"""
import argparse
import difflib
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import time
import urllib.request
from pathlib import Path

os.environ["TQDM_DISABLE"] = "1"         # Chatterbox draws a progress bar per sentence: ~1 MB of noise in n8n's output
os.environ["HF_HUB_OFFLINE"] = "1"       # both models are on disk; never wait on (or fail for) the internet

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
GOOD = 0.90                             # a take is good at this share of words, or with at most 1 word different
MAX_WORDS = 45                          # ~15 s of speech; Chatterbox cuts off at ~40 s
NUMBER = set("""zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen
seventeen eighteen nineteen twenty thirty forty fifty sixty seventy eighty ninety hundred thousand million billion
""".split())


def sentences(segs):
    """Consecutive segments, grouped so each group ends where a sentence ends (as voice.py)."""
    groups, cur = [], []
    for s in segs:
        cur.append(s)
        if SENTENCE_END.search(s["text"].strip()):
            groups.append(cur)
            cur = []
    return groups + ([cur] if cur else [])


def parts(group):
    """A group too long for one take, halved at segment boundaries until each part fits."""
    if len(group) == 1 or sum(len(x["text"].split()) for x in group) <= MAX_WORDS:
        return [group]
    h = len(group) // 2
    return parts(group[:h]) + parts(group[h:])


def words(text):
    """Lower-case words for comparing the script with what Whisper heard. A run of number words or digits becomes
    one '#': Whisper writes "thirty six" as "36" and "twenty fourteen" as "2014"."""
    out = []
    for w in re.sub(r"[^a-z0-9' ]+", " ", text.lower().replace("’", "'")).split():
        if not w.strip("'"):
            continue
        if w in NUMBER or re.fullmatch(r"\d+(st|nd|rd|th|s)?", w):
            if not out or out[-1] != "#":
                out.append("#")
        else:
            out.append(w)
    return out


def score(want, got):
    """(good?, ratio) for the script's words against Whisper's."""
    sm = difflib.SequenceMatcher(None, want, got, autojunk=False)
    same = sum(b.size for b in sm.get_matching_blocks())
    return (sm.ratio() >= GOOD or (len(want) - same <= 1 and len(got) - same <= 1)), sm.ratio()


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
    p.add_argument("--only", default="", help="only the sentences holding these segment ids (1,5,9), into voice-preview/")
    a = p.parse_args()

    t0 = time.time()
    out = Path(a.folder).resolve()
    segs = json.loads((out / "script.json").read_text(encoding="utf-8"))["segments"]
    texts = hashlib.sha1(json.dumps([s["text"] for s in segs]).encode("utf-8")).hexdigest()
    # channels/<channel>/videos/<slug>: the channel's energy (found-rich: 1.0 / 0.3, Justin 2026-10-18); else defaults
    ch = out.parent.parent / "settings.json"
    voice = json.loads(ch.read_text(encoding="utf-8")).get("voice", {}) if ch.exists() else {}
    ex, cfg = voice.get("exaggeration", 0.5), voice.get("cfg", 0.5)
    method = METHOD if (ex, cfg) == (0.5, 0.5) else f"{METHOD}+ex{ex}+cfg{cfg}"   # default videos stay up to date
    settings = {"engine": "chatterbox", "ref": REF.name, "texts": texts, "method": method}
    test = bool(a.preview or a.only)
    done = [out / "voice.wav", out / "timings.json"]
    made_with = json.loads((out / "voice-settings.json").read_text(encoding="utf-8")) if (out / "voice-settings.json").exists() else None
    if a.if_needed and not test and made_with == settings and all(f.exists() for f in done):
        timings = json.loads((out / "timings.json").read_text(encoding="utf-8"))
        print(json.dumps({"ok": True, "folder": str(out), "voice": "chatterbox:" + REF.stem, "segments": len(timings),
                          "seconds": timings[-1]["end"], "took": 0, "skipped": "already up to date", "over_6s": [],
                          "check": []}))
        return

    groups = sentences(segs)
    if a.preview:
        groups = groups[:a.preview]
    if a.only:
        ids = {int(x) for x in a.only.split(",")}
        groups = [g for g in groups if ids & {x["id"] for x in g}]
    dest = out / "voice-preview" if test else out
    cache = dest / "voice-parts"
    cache.mkdir(parents=True, exist_ok=True)
    takes = [(part, k == len(ps) - 1) for g in groups for ps in [parts(g)] for k, part in enumerate(ps)]

    model = whisper = None
    full, starts, t, check, reused, retried = [], {}, 0.0, [], 0, []
    for n, (g, last) in enumerate(takes, 1):
        text = " ".join(x["text"].strip() for x in g)
        name = f"{g[0]['id']:03d}-{g[-1]['id']:03d}"
        meta = cache / f"{name}.json"
        saved = json.loads(meta.read_text(encoding="utf-8")) if meta.exists() else None
        if saved and saved["text"] == text and saved["method"] == method and (cache / f"{name}.wav").exists():
            wav, sr = sf.read(cache / f"{name}.wav", dtype="float32")
            heard, ratio, good = [tuple(h) for h in saved["heard"]], saved["ratio"], saved["good"]
            reused += 1
        else:
            if model is None:                                 # loaded only when a take is actually needed
                closed = close_page()
                from chatterbox.tts import ChatterboxTTS
                from faster_whisper import WhisperModel
                model = ChatterboxTTS.from_pretrained(device="cuda" if torch.cuda.is_available() else "cpu")
                model.prepare_conditionals(str(REF), exaggeration=ex)   # Mark, read once
                whisper = WhisperModel("small.en", device="cpu", compute_type="int8")
                print(f"loaded in {time.time() - t0:.0f}s{' (closed the Chatterbox page)' if closed else ''}; "
                      f"{len(takes)} takes, {reused} reused", file=sys.stderr, flush=True)
            sr, want, best = model.sr, words(text), None
            for k in range(TRIES):
                torch.manual_seed(1000 * g[0]["id"] + k)      # same take again on a rerun; a retry gets a new one
                take = trim(model.generate(text, exaggeration=ex, cfg_weight=cfg).squeeze().cpu().numpy(), sr)
                h = hear(whisper, take, sr)
                good, ratio = score(want, [x[0] for x in h])
                if best is None or ratio > best[2]:
                    best = (take, h, ratio, good)
                if good:
                    break
                print(f"  segments {name}: heard {ratio:.0%} of the words, another take", file=sys.stderr, flush=True)
            wav, heard, ratio, good = best
            if k:
                retried.append(name)
            sf.write(cache / f"{name}.wav", wav, sr)
            meta.write_text(json.dumps({"text": text, "method": method, "heard": heard, "ratio": ratio, "good": good}),
                            encoding="utf-8")
        if not good:
            check.append({"segments": name, "match": round(ratio, 2), "script": text,
                          "heard": " ".join(h[0] for h in heard)})
        end = SENTENCE_END.search(g[-1]["text"].strip())
        gap = (PAUSE[end.group()[0]] if end else NO_MARK) if last else 0.0   # no pause inside a split sentence
        for x, st in zip(g, cuts(g, heard, len(wav) / sr)):
            starts[x["id"]] = t + st
        full += [wav, np.zeros(int(sr * gap), dtype=np.float32)]
        t += (len(wav) + int(sr * gap)) / sr                  # sample-exact, so timing cannot drift from voice.wav
        print(f"  {n}/{len(takes)} segments {name}: {len(wav) / sr:.1f}s, {time.time() - t0:.0f}s so far",
              file=sys.stderr, flush=True)

    (dest / "audio").mkdir(exist_ok=True)
    wav = np.concatenate(full)
    sf.write(dest / "voice.wav", wav, sr)
    order = [x["id"] for g, _ in takes for x in g]
    timings = [{"id": i, "start": round(starts[i], 4), "end": round(starts[order[k + 1]] if k + 1 < len(order) else t, 4)}
               for k, i in enumerate(order)]
    for x in timings:                                         # per-segment slices, as voice.py (not used by the edit)
        sf.write(dest / "audio" / f"{x['id']:03d}.wav", wav[int(x["start"] * sr):int(x["end"] * sr)], sr)
    long = [x for x in timings if x["end"] - x["start"] > 6.0]   # 6 s per image is Justin's hard max
    for x in long:
        print(f"OVER 6s: segment {x['id']} is {x['end'] - x['start']:.2f}s", file=sys.stderr)
    (dest / "timings.json").write_text(json.dumps(timings, indent=1), encoding="utf-8")
    (dest / "voice-check.json").write_text(json.dumps(check, indent=1), encoding="utf-8")
    if not test:
        (dest / "voice-settings.json").write_text(json.dumps(settings), encoding="utf-8")
        shutil.rmtree(cache, ignore_errors=True)              # voice.wav holds it all now
    print(json.dumps({"ok": True, "folder": str(dest), "voice": "chatterbox:" + REF.stem, "segments": len(timings),
                      "seconds": round(t, 2), "took": round(time.time() - t0, 1), "takes": len(takes),
                      "reused": reused, "retried": retried, "check": check,
                      "over_6s": [{"id": x["id"], "seconds": round(x["end"] - x["start"], 2)} for x in long]}))


if __name__ == "__main__":
    main()
