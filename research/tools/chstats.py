"""Per channel: subscribers, and for /videos and /shorts: count, total views, median of newest 20, best 3 (title, views, length).
usage: python chstats.py OUT.json @handle [@handle ...]"""
import json, subprocess, sys, time, statistics

def tab(handle, t):
    r = subprocess.run(["yt-dlp", "-J", "--flat-playlist", f"https://www.youtube.com/{handle}/{t}"],
                       capture_output=True, text=True, encoding="utf-8")
    if r.returncode or not r.stdout.strip():
        return None, r.stderr.strip().splitlines()[-1:] 
    return json.loads(r.stdout), None

out = {}
for h in sys.argv[2:]:
    row = {}
    for t in ("videos", "shorts"):
        d, err = tab(h, t)
        if not d:
            row[t] = {"error": err}; continue
        es = [e for e in d.get("entries", []) if e]
        v = [e.get("view_count") or 0 for e in es]
        row["subs"] = d.get("channel_follower_count") or row.get("subs")
        row["channel"] = d.get("channel") or d.get("uploader")
        best = sorted(es, key=lambda e: -(e.get("view_count") or 0))[:3]
        row[t] = {"count": len(es), "total_views": sum(v),
                  "median_newest20": statistics.median(v[:20]) if v else 0,
                  "best": [(e.get("title"), e.get("view_count"), e.get("duration")) for e in best],
                  "newest": [(e.get("title"), e.get("view_count"), e.get("duration")) for e in es[:5]]}
        time.sleep(2)
    out[h] = row
    print(h, row.get("subs"), {t: (row[t].get("count"), row[t].get("median_newest20")) for t in ("videos", "shorts") if "count" in row[t]}, flush=True)
json.dump(out, open(sys.argv[1], "w", encoding="utf-8"), ensure_ascii=False, indent=1)
