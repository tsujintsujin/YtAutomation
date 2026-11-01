"""One day's analytics reading -> rows for the sheet's "Daily analytics" tab (tab-separated, no header).

Usage: python sheet_rows.py <date YYYY-MM-DD> [channel ...]     (default: every channel with a raw file that day)

Reads channels/<key>/analytics/raw/<date>.json. Story, part and posting hour come from the videos' posted.json
(its "parts" list for a Short posted in parts) or pulled.json. Paste the output under the tab's last row.
"""
import glob, json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
NAMES = {"found-rich": "LuckySticks", "what-happens-now": "OldSticksNewSticks", "chaotic-lives": "TangledSticks"}
HEAD = ["Date read", "Channel", "Story", "Part", "Video ID", "Title", "Published", "Post hour", "Length (s)", "Views",
        "Engaged views", "Stayed %", "Avg view (s)", "Avg % viewed", "Likes", "Comments", "Shares", "Subs", "Source"]


def known(ch):
    """video_id -> (story, part, publish_at) from posted.json / pulled.json."""
    out = {}
    for f in glob.glob(os.path.join(HERE, "channels", ch, "videos", "*", "posted.json")) + \
             glob.glob(os.path.join(HERE, "channels", ch, "videos", "*", "pulled.json")):
        d = json.load(open(f, encoding="utf-8"))
        slug = os.path.basename(os.path.dirname(f))
        for p in d.get("parts") or []:
            out[p["video_id"]] = (slug, p["n"], p.get("publish_at", ""))
        out.setdefault(d.get("video_id"), (slug, "whole", d.get("publish_at", "")))
    return out


def rows(date, channels):
    out = []
    for ch in channels:
        f = os.path.join(HERE, "channels", ch, "analytics", "raw", date + ".json")
        if not os.path.exists(f):
            continue
        ids, d = known(ch), json.load(open(f, encoding="utf-8"))
        for s in d["shorts"]:
            slug, part, pa = ids.get(s["video_id"], (s.get("slug") or "", "whole", ""))
            v = lambda k: "" if s.get(k) is None else s[k]
            out.append([d["date"], NAMES.get(ch, ch), slug, part, s["video_id"], s["title"], s.get("published", ""),
                        pa[11:13] if len(pa) > 12 else "", v("length_s"), v("views"), v("engaged_views"),
                        v("stayed_pct"), v("avg_view_duration_s"), v("avg_pct_viewed"), v("likes"), v("comments"),
                        v("shares"), v("subs_net"), v("source")])
    return out


if __name__ == "__main__":
    date, chs = sys.argv[1], sys.argv[2:] or list(NAMES)
    sys.stdout.reconfigure(encoding="utf-8")
    print("\n".join("\t".join(str(c).replace("\t", " ") for c in r) for r in rows(date, chs)))
