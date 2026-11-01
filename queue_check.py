"""Where every video of a Shorts run queue stands, for n8n "Shorts: run queue" (n8n/build_shorts_queue.py), which runs
this every 30 s and decides in n8n which part to start next. Reads only: the video folders and the bridge's claims.

    python queue_check.py <channel> <slug,slug,...>
prints one JSON line:
    {"ok": true, "retryAt": unix seconds Continue pictures was last pressed (0: never),
     "videos": [{"slug", "mp4", "total", "missing", "voiceDone",
                             "parts": {"voice": {"state", "outcome", "reason", "at"}, "pictures": {...}, "finish": {...}}}]}
    {"ok": false, "error": "..."}                    (the bridge is not answering, a folder or script.json is missing)
state:     queued / running  the bridge holds that part's claim (the queue started it / its run has it)
           ended             no claim, and parts.json says how it last ended (outcome done / limit / robot / failed /
                             stopped; a claim gone while parts.json still says queued or running = the bridge was
                             restarted under it: failed)
           none              never run
voiceDone: the voice part ended "done" after script.json last changed (a changed script needs its voice again).
"""
import json
import re
import sys
import urllib.request
from pathlib import Path

HERE = Path(__file__).parent
BRIDGE = "http://127.0.0.1:8766"
PARTS = ("voice", "pictures", "finish")
IMG = re.compile(r"^(\d{3})\.(jpg|jpeg|png|webp)$", re.I)


def video(channel, slug, states):
    d = HERE / "channels" / channel / "videos" / slug
    s = json.loads((d / "script.json").read_text(encoding="utf-8-sig"))
    have = {int(m[1]) for p in (d / "img").glob("*") if (m := IMG.match(p.name))} if (d / "img").is_dir() else set()
    try:
        made = json.loads((d / "parts.json").read_text(encoding="utf-8")) if (d / "parts.json").exists() else {}
    except ValueError:
        made = {}
    parts = {}
    for part in PARTS:
        m = made.get(part) or {}
        claim = states.get(f"{slug}:{part}")
        if claim:
            parts[part] = {"state": claim, "outcome": m.get("outcome", ""), "reason": m.get("reason", ""), "at": m.get("at", 0)}
        elif m.get("outcome") in ("queued", "running"):
            parts[part] = {"state": "ended", "outcome": "failed", "at": m.get("at", 0),
                           "reason": "its claim is gone (the bridge was restarted while it ran)"}
        elif m:
            parts[part] = {"state": "ended", "outcome": m["outcome"], "reason": m.get("reason", ""), "at": m.get("at", 0)}
        else:
            parts[part] = {"state": "none", "outcome": "", "reason": "", "at": 0}
    v = parts["voice"]
    return {"slug": slug, "mp4": (d / f"{slug}.mp4").exists(), "total": len(s["segments"]),
            "missing": sum(1 for x in s["segments"] if x["id"] not in have),
            "voiceDone": v["state"] == "ended" and v["outcome"] == "done" and v["at"] > (d / "script.json").stat().st_mtime,
            "parts": parts}


def long_run(states):
    """A "YouTube Render" run (a long video in output/<slug>: its claim has no part) holds the Gemini windows while
    it makes pictures, and OpenCut after that: {"slug", "phase": "pictures" | "finish"}, or None."""
    for key, state in states.items():
        d = HERE / "output" / key
        if ":" in key or state != "running" or not (d / "script.json").exists():
            continue
        s = json.loads((d / "script.json").read_text(encoding="utf-8-sig"))
        have = {int(m[1]) for p in (d / "img").glob("*") if (m := IMG.match(p.name))} if (d / "img").is_dir() else set()
        return {"slug": key, "phase": "pictures" if any(x["id"] not in have for x in s["segments"]) else "finish"}
    return None


def check(channel, slugs):
    try:
        with urllib.request.urlopen(BRIDGE + "/status", timeout=5) as r:
            states = json.loads(r.read()).get("states", {})
    except Exception as e:
        return {"ok": False, "error": f"the bridge is not answering ({type(e).__name__}: {e})"}
    # Continue pictures (dashboard button, Justin 2026-10-21): the last time it was pressed for this channel
    retry = HERE / "channels" / channel / "pictures-retry.json"
    try:
        retry_at = json.loads(retry.read_text(encoding="utf-8")).get("at", 0) if retry.exists() else 0
    except ValueError:
        retry_at = 0
    try:
        return {"ok": True, "retryAt": retry_at, "longRun": long_run(states),
                "videos": [video(channel, s, states) for s in slugs]}
    except Exception as e:
        return {"ok": False, "error": f"{type(e).__name__}: {e}"}


if __name__ == "__main__":
    ch, names = sys.argv[1], [s for s in sys.argv[2].split(",") if s]
    ok = re.compile(r"^[a-z0-9][a-z0-9_-]*$")
    if not ok.match(ch) or not names or not all(ok.match(s) for s in names):
        print(json.dumps({"ok": False, "error": "bad channel or video name"}))
    else:
        print(json.dumps(check(ch, names)))
