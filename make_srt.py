"""Writes output/<video>/<video>.srt: one subtitle per segment, its text from script.json, its start and end from
timings.json (the same times OpenCut uses to show each segment's image). Upload it to YouTube with the MP4.

usage: python make_srt.py output/<video>
Last line: {"ok": true, "srt": "...", "subtitles": N}
"""
import json
import sys
from pathlib import Path

folder = Path(sys.argv[1]).resolve()
text = {s["id"]: s["text"] for s in json.loads((folder / "script.json").read_text(encoding="utf-8"))["segments"]}
times = json.loads((folder / "timings.json").read_text(encoding="utf-8"))


def stamp(sec):
    ms = round(sec * 1000)
    return f"{ms // 3600000:02d}:{ms // 60000 % 60:02d}:{ms // 1000 % 60:02d},{ms % 1000:03d}"


assert sorted(t["id"] for t in times) == sorted(text), "timings.json and script.json have different segments"
blocks = [f"{n}\n{stamp(t['start'])} --> {stamp(t['end'])}\n{text[t['id']]}\n"
          for n, t in enumerate(sorted(times, key=lambda t: t["start"]), 1)]
out = folder / f"{folder.name}.srt"
out.write_text("\n".join(blocks), encoding="utf-8")
print(json.dumps({"ok": True, "srt": str(out), "subtitles": len(blocks)}))
