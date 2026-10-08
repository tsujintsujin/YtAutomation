"""Prints the slug of the next unfinished video, or nothing. n8n's hourly check runs this.

Unfinished = output/<slug>/ has script.json but no <slug>.mp4 yet. Folders starting with "_" are tests.
A video another n8n run is already working on is turned away by that run's claim on the bridge
(POST /claim), not here.
"""
import json
from pathlib import Path

OUT = Path(__file__).parent / "output"

for d in sorted(OUT.iterdir(), key=lambda d: d.stat().st_mtime):
    if d.is_dir() and not d.name.startswith("_") and (d / "script.json").exists() and not (d / f"{d.name}.mp4").exists():
        # slug and the voice the script asks for, tab-separated (n8n's hourly check passes both on)
        print(d.name + "	" + json.loads((d / "script.json").read_text(encoding="utf-8")).get("voice", "am_liam"))
        break
