"""Cut a finished Short into 20-30 s parts, each with "Part N" drawn on it.

Usage: python parts.py <video folder>      (e.g. channels/what-happens-now/videos/candle-tallow-then-now)
       python parts.py --selftest

Justin, 2026-11-01: Shorts are posted as 20-30 s parts; a Short under 1 minute stays whole (no parts, no label).
Reads <slug>.mp4, timings.json (one start/end per line) and script.json (the line texts). Cuts only where a line
ends: first where a sentence ends, else at any line end (a picture change), never inside a line. The voice,
pictures and music are the MP4's own; nothing is made again.
Writes parts/part-N.mp4 and cuts.json {"whole": bool, "parts": [{"n", "of", "start", "end", "file", "first_line"}]}.
"""
import json, math, os, re, subprocess, sys

MIN, MAX, WHOLE_UNDER = 20.0, 30.0, 60.0
FONT = "C\\:/Windows/Fonts/arialbd.ttf"
# Centred, at 73% of the height: above the strip where YouTube draws the title and channel on a phone.
LABEL = ("drawtext=fontfile='" + FONT + "':text='Part {n}':fontsize=78:fontcolor=black:"
         "box=1:boxcolor=white@0.92:boxborderw=26:x=(w-text_w)/2:y=h*0.73")


def plan(total, cuts):
    """Part boundaries [0, ..., total] using only times in `cuts`, every part MIN-MAX s, fewest parts, most even."""
    for n in range(math.ceil(total / MAX), int(total // MIN) + 1):
        goal, best = total / n, {0.0: (0.0, [0.0])}  # end time -> (cost, boundaries)
        for _ in range(n - 1):
            nxt = {}
            for t, (cost, path) in best.items():
                for c in cuts:
                    if MIN <= c - t <= MAX:
                        cand = (cost + (c - t - goal) ** 2, path + [c])
                        if c not in nxt or cand[0] < nxt[c][0]:
                            nxt[c] = cand
            best = nxt
        done = [(cost + (total - t - goal) ** 2, path + [total]) for t, (cost, path) in best.items()
                if MIN <= total - t <= MAX]
        if done:
            return min(done)[1]
    return None


def duration(mp4):
    out = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", mp4],
                         capture_output=True, text=True, check=True).stdout
    return float(out)


def main(folder):
    folder = os.path.abspath(folder)
    slug = os.path.basename(folder)
    mp4 = os.path.join(folder, slug + ".mp4")
    total = duration(mp4)
    out_dir = os.path.join(folder, "parts")
    if os.path.isdir(out_dir):  # parts of an earlier MP4 of this video
        for f in os.listdir(out_dir):
            os.remove(os.path.join(out_dir, f))
    if total < WHOLE_UNDER:
        json.dump({"whole": True, "length": round(total, 2), "parts": []}, open(os.path.join(folder, "cuts.json"), "w"), indent=1)
        print(f"{slug}: {total:.1f} s, under a minute: stays whole")
        print(json.dumps({"ok": True, "whole": True, "parts": 0}))  # last line: read by n8n's "Parse split"
        return
    timings = json.load(open(os.path.join(folder, "timings.json"), encoding="utf-8"))
    text = {s["id"]: s["text"] for s in json.load(open(os.path.join(folder, "script.json"), encoding="utf-8"))["segments"]}
    ends = [(t["end"], text[t["id"]]) for t in timings[:-1]]
    sentence = [e for e, tx in ends if re.search(r"[.!?][\"')\]]*\s*$", tx)]
    bounds = plan(total, sentence) or plan(total, [e for e, _ in ends])
    if not bounds:
        sys.exit(f"{slug}: no way to cut {total:.1f} s into {MIN:.0f}-{MAX:.0f} s parts at line ends")
    os.makedirs(out_dir, exist_ok=True)
    parts, of = [], len(bounds) - 1
    for i in range(of):
        a, b = bounds[i], bounds[i + 1]
        name = f"part-{i + 1}.mp4"
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", f"{a:.3f}", "-i", mp4, "-t", f"{b - a:.3f}",
                        "-vf", LABEL.format(n=i + 1), "-c:v", "libx264", "-preset", "medium", "-crf", "18",
                        "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart",
                        os.path.join(out_dir, name)], check=True)
        first = next((text[t["id"]] for t in timings if t["start"] >= a - 0.01), "")
        parts.append({"n": i + 1, "of": of, "start": round(a, 3), "end": round(b, 3), "file": "parts/" + name,
                      "first_line": first})
    json.dump({"whole": False, "length": round(total, 2), "parts": parts}, open(os.path.join(folder, "cuts.json"), "w"), indent=1)
    print(f"{slug}: {total:.1f} s -> " + ", ".join(f"part {p['n']} {p['end'] - p['start']:.1f} s" for p in parts))
    print(json.dumps({"ok": True, "whole": False, "parts": of}))


def selftest():
    b = plan(74.0, [5.0, 12.0, 23.0, 26.0, 40.0, 49.0, 52.0, 66.0])
    assert b == [0.0, 23.0, 49.0, 74.0], b
    assert plan(74.0, [5.0, 70.0]) is None                       # no cut lands in range
    for total in (60.0, 61.0, 90.0, 95.0, 108.0):                # a cut every 0.5 s: always splittable
        b = plan(total, [x / 2 for x in range(1, int(total * 2))])
        assert all(MIN <= y - x <= MAX for x, y in zip(b, b[1:])), (total, b)
    print("selftest ok")


if __name__ == "__main__":
    selftest() if sys.argv[1:] == ["--selftest"] else main(sys.argv[1])
