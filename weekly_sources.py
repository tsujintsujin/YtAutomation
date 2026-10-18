"""One week's sources for a short channel: find the videos, transcribe them, hand the rows to n8n.

usage: chatterbox\\.venv\\Scripts\\python weekly_sources.py found-rich [--want 28] [--test]
Run by the n8n workflow "Shorts: weekly sources" (Monday 06:00, or by hand). No Claude, no API key.

1. Real run only: stop if channels/<key>/weeks/<monday>/sources.json already exists (one batch a week).
2. find_sources.py picks want+12 candidates (extra in case some have no narration), most viewed first.
3. Per candidate, in order: download the audio (yt-dlp), Whisper small.en on CPU (same as voice_cb.py), delete
   the audio. Under 25 words = "no narration" (music-only clips), skipped. A failed download = "failed", skipped.
4. Stops when `want` videos have a transcript, or the candidates run out (then "only N found").
5. Writes weeks/<monday>/sources.json (all checked videos, for Claude), and on a real run adds every checked id
   to used-sources.json (silent ones too, so they aren't checked again; failed ones are left to retry).
--test: week "test-<date>", nothing marked used, no once-a-week stop.
Last stdout line: JSON {"ok", "week", "rows": [...]} with only the transcribed videos (n8n puts them in the sheet).
"""
import argparse
import json
import shutil
import subprocess
import sys
import time
from datetime import date, timedelta
from pathlib import Path

HERE = Path(__file__).parent
MIN_WORDS = 25
MAX_FAILS_IN_A_ROW = 3   # something systematic (network, YouTube block, Whisper): stop instead of skipping everything
FFMPEG = shutil.which("ffmpeg") or str(next(Path.home().glob(
    "AppData/Local/Microsoft/WinGet/Packages/Gyan.FFmpeg*/ffmpeg-*/bin/ffmpeg.exe"), "ffmpeg"))


def log(msg):
    print(time.strftime("%H:%M:%S"), msg, file=sys.stderr, flush=True)


def download(video, folder):
    """Best audio-only stream as-is (no ffmpeg needed; faster-whisper decodes it). Returns the file or None."""
    for f in folder.glob(video["id"] + ".*"):
        f.unlink()
    r = subprocess.run([sys.executable, "-m", "yt_dlp", "-q", "--no-warnings", "-f", "bestaudio/best",
                        "-o", str(folder / "%(id)s.%(ext)s"), video["url"]], capture_output=True, text=True,
                       encoding="utf-8", errors="replace")
    files = list(folder.glob(video["id"] + ".*"))
    if r.returncode or not files:
        log(f"  download failed: {(r.stderr.strip().splitlines() or ['no file'])[-1]}")
        return None
    return files[0]


def samples(audio):
    """16 kHz mono float32 via ffmpeg. faster-whisper's own file decoder (PyAV) breaks on this venv's av version,
    and upgrading av could break Chatterbox; voice_cb.py also hands Whisper samples, never files."""
    import numpy as np
    r = subprocess.run([FFMPEG, "-nostdin", "-v", "error", "-i", str(audio), "-f", "f32le", "-ac", "1", "-ar", "16000", "-"],
                       capture_output=True)
    if r.returncode:
        raise RuntimeError("ffmpeg: " + r.stderr.decode(errors="replace").strip()[-200:])
    return np.frombuffer(r.stdout, dtype=np.float32)


def main():
    p = argparse.ArgumentParser()
    p.add_argument("channel")
    p.add_argument("--want", type=int, default=28)
    p.add_argument("--test", action="store_true")
    a = p.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")
    if not a.channel.replace("-", "").isalnum():
        sys.exit("bad channel name")

    cdir = HERE / "channels" / a.channel
    today = date.today()
    monday = (today - timedelta(days=today.weekday())).isoformat()
    week = f"test-{today.isoformat()}" if a.test else monday
    wdir = cdir / "weeks" / week
    out = wdir / "sources.json"
    if out.exists() and not a.test:
        print(json.dumps({"ok": False, "week": week, "reason": "this week is already done", "rows": []}))
        return
    wdir.mkdir(parents=True, exist_ok=True)

    cand_file = wdir / "candidates.json"   # kept: a rerun of the same week (after a stop) skips the 6-min search
    if not cand_file.exists():
        log(f"finding candidates for {a.channel} ({week})")
        r = subprocess.run([sys.executable, str(HERE / "find_sources.py"), a.channel, "--count", str(a.want + 12),
                            "--out", str(cand_file)], capture_output=True, text=True, encoding="utf-8", errors="replace")
        if r.returncode or not cand_file.exists():
            print(json.dumps({"ok": False, "week": week, "reason": "finder failed: " + r.stderr.strip()[-300:], "rows": []}))
            return
    candidates = json.loads(cand_file.read_text(encoding="utf-8"))["videos"]
    log(f"{len(candidates)} candidates")

    from faster_whisper import WhisperModel
    whisper = WhisperModel("small.en", device="cpu", compute_type="int8")
    audio_dir = wdir / "audio"
    audio_dir.mkdir(exist_ok=True)
    checked, good, fails, stopped = [], 0, 0, ""
    for v in candidates:
        if good >= a.want:
            break
        if fails >= MAX_FAILS_IN_A_ROW:
            stopped = f"stopped: {fails} failures in a row ({checked[-1].get('error', '')})"
            log(stopped)
            break
        log(f"[{good}/{a.want}] {v['title'][:60]} ({v['kind']}, {v['url']})")
        audio = download(v, audio_dir)
        if not audio:
            checked.append(dict(v, status="failed", transcript="", error="download"))
            fails += 1
            continue
        try:
            segs, _ = whisper.transcribe(samples(audio), language="en", beam_size=5, vad_filter=True)
            text = " ".join(s.text.strip() for s in segs).strip()
        except Exception as e:  # a broken file is one skipped video, not a stopped week
            log(f"  whisper failed: {e}")
            checked.append(dict(v, status="failed", transcript="", error=str(e)[:200]))
            fails += 1
            continue
        finally:
            audio.unlink(missing_ok=True)
        words = len(text.split())
        status = "ok" if words >= MIN_WORDS else "no narration"
        log(f"  {status}, {words} words")
        checked.append(dict(v, status=status, words=words, transcript=text))
        good += status == "ok"
        fails = 0
    audio_dir.rmdir()

    rows = [v for v in checked if v["status"] == "ok"]
    note = stopped or ("" if len(rows) >= a.want else f"only {len(rows)} found")
    out.write_text(json.dumps({"channel": a.channel, "week": week, "note": note, "videos": checked},
                              indent=2, ensure_ascii=False), encoding="utf-8")
    if not a.test:
        used_file = cdir / "used-sources.json"
        used = set(json.loads(used_file.read_text(encoding="utf-8"))) if used_file.exists() else set()
        used |= {v["id"] for v in checked if v["status"] != "failed"}
        used_file.write_text(json.dumps(sorted(used), indent=1), encoding="utf-8")
    log(f"done: {len(rows)} transcribed, {len(checked) - len(rows)} skipped {note}")
    print(json.dumps({"ok": not stopped, "week": week, "note": note, "rows": [
        {"Week": week, "Views": v["views"], "Type": v["kind"], "Channel": v["channel"], "Title": v["title"],
         "Link": v["url"], "Words": v["words"], "Transcript": v["transcript"]} for v in rows]}, ensure_ascii=False))


if __name__ == "__main__":
    main()
