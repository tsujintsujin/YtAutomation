# -*- coding: utf-8 -*-
"""
Cover for a Short: one frame of the finished MP4, saved as cover.jpg next to it (Justin, 2026-10-19:
"just a frame from the video should do").

    python cover.py channels/found-rich/videos/<slug>

Which frame: cover.json {"segment": N} (written by Claude with the scenes), else segment 1. The frame is the
middle of that segment's time in timings.json, so it is exactly the picture the viewer sees there.
Last line is JSON: {"ok": true, "cover": ..., "segment": N, "at": seconds} or {"ok": false, "error": ...}.
"""
import json, shutil, subprocess, sys
from pathlib import Path

FFMPEG = shutil.which("ffmpeg") or str(next(Path.home().glob(
    "AppData/Local/Microsoft/WinGet/Packages/Gyan.FFmpeg*/ffmpeg-*/bin/ffmpeg.exe"), "ffmpeg"))


def main(folder):
    d = Path(folder)
    mp4 = d / (d.name + ".mp4")
    if not mp4.exists():
        return {"ok": False, "error": "no MP4: " + str(mp4)}
    seg = 1
    if (d / "cover.json").exists():
        seg = int(json.loads((d / "cover.json").read_text(encoding="utf-8"))["segment"])
    t = next((t for t in json.loads((d / "timings.json").read_text(encoding="utf-8")) if t["id"] == seg), None)
    if t is None:
        return {"ok": False, "error": "segment %d not in timings.json" % seg}
    at = round((t["start"] + t["end"]) / 2, 3)
    out = d / "cover.jpg"
    r = subprocess.run([FFMPEG, "-v", "error", "-y", "-ss", str(at), "-i", str(mp4), "-frames:v", "1",
                        "-q:v", "2", str(out)], capture_output=True)
    if r.returncode or not out.exists():
        return {"ok": False, "error": "ffmpeg: " + r.stderr.decode(errors="replace").strip()[-200:]}
    return {"ok": True, "cover": str(out), "segment": seg, "at": at}


if __name__ == "__main__":
    res = main(sys.argv[1])
    print(json.dumps(res))
    sys.exit(0 if res["ok"] else 1)
