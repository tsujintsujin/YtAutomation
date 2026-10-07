"""Writes output/<video>/<video>.srt: one subtitle per segment, its text from script.json, its start and end from
timings.json (the same times OpenCut uses to show each segment's image). Upload it to YouTube with the MP4.

usage: python make_srt.py output/<video>
Last line: {"ok": true, "srt": "...", "subtitles": N}
"""
import json
import subprocess
import sys
from pathlib import Path

folder = Path(sys.argv[1]).resolve()
text = {s["id"]: s["text"] for s in json.loads((folder / "script.json").read_text(encoding="utf-8"))["segments"]}
times = json.loads((folder / "timings.json").read_text(encoding="utf-8"))


def stamp(sec):
    ms = round(sec * 1000)
    return f"{ms // 3600000:02d}:{ms // 60000 % 60:02d}:{ms // 1000 % 60:02d},{ms % 1000:03d}"


assert sorted(t["id"] for t in times) == sorted(text), "timings.json and script.json have different segments"
subs = [(t["start"], t["end"], text[t["id"]]) for t in sorted(times, key=lambda t: t["start"])]

# Channel intro (intro.json, same rules as opencut-controller/scripts/render-folder.mjs): segments after it move
# later by the intro's length, and the intro's voice line gets its own subtitle.
cfg = folder / "intro.json"
if cfg.exists():
    intro = json.loads(cfg.read_text(encoding="utf-8"))
    probe = lambda f: float(subprocess.run(  # noqa: E731  (paths are relative to the YtAutomation folder)
        ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(folder.parent.parent / f)],
        capture_output=True, text=True, check=True).stdout)
    at =next(t["end"] for t in times if t["id"] == intro["after_segment"])
    length = probe(intro["intro"])
    v0 = at + intro["intro_voice_at"]
    subs = [(a + length, b + length, x) if a >= at else (a, b, x) for a, b, x in subs]
    subs.append((v0, v0 + probe(intro["intro_voice"]), intro["intro_voice_text"]))
    subs.sort()
blocks = [f"{n}\n{stamp(a)} --> {stamp(b)}\n{x}\n" for n, (a, b, x) in enumerate(subs, 1)]
out = folder / f"{folder.name}.srt"
out.write_text("\n".join(blocks), encoding="utf-8")
print(json.dumps({"ok": True, "srt": str(out), "subtitles": len(blocks)}))
