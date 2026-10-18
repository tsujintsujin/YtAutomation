"""Find this week's source videos for a short channel: the most-viewed on-topic videos not used before.

usage: python find_sources.py found-rich [--out file.json] [--mark-used] [--count N]
       python find_sources.py --selftest
Reads channels/<key>/sources.json (where to look, topic words, min views, count).
Looks in two places with yt-dlp (no API key, no Claude): the Shorts tab of known format channels, and YouTube
searches (these return mostly long videos, which is fine: long "lucky finds" videos are sources too).
Keeps a video only if its title is on topic, it has >= min_views, it is <= max_seconds, and its id is not in
channels/<key>/used-sources.json. Takes the top `count` by views. Fewer found = prints "only N found", no retry.
--mark-used adds the picked ids to used-sources.json (n8n does this once the rows are in the sheet).
"""
import argparse
import json
import re
import subprocess
import sys
from datetime import date
from pathlib import Path

HERE = Path(__file__).parent
FIELDS = ["id", "view_count", "duration", "channel", "title"]


def ytdlp_list(url):
    """Flat list of a channel tab or search: [{id, view_count, duration, channel, title}]. A failed source gives []."""
    fmt = "\t".join(f"%({f})s" for f in FIELDS)
    r = subprocess.run([sys.executable, "-m", "yt_dlp", "--flat-playlist", "--ignore-errors", "--print", fmt, url],
                       capture_output=True, text=True, encoding="utf-8", errors="replace")
    out = []
    for line in r.stdout.splitlines():
        v = dict(zip(FIELDS, line.split("\t")))
        if len(v) == len(FIELDS) and v["id"] != "NA":
            out.append(v)
    if not out:
        print(f"  nothing from {url} ({r.stderr.strip().splitlines()[-1:] or 'no output'})", file=sys.stderr)
    return out


def num(s):
    try:
        return int(float(s))
    except (TypeError, ValueError):
        return None


def on_topic(title, cfg, kind="short"):
    """kind "short" = from a known format channel's Shorts tab. Anything from search ("long", "search_short") must
    also be about people finding things (compilations), which drops vlogs, deals, dramas and songs."""
    t = title.lower()
    ok = re.search(cfg["topic"], t) and re.search(cfg["money"], t) and not re.search(cfg["exclude"], t)
    return bool(ok and (kind == "short" or re.search(cfg["long_people"], t)))


def pick(videos, cfg, used):
    """videos: dicts from ytdlp_list (with 'kind'). Returns the top cfg['count'] by views, deduped by id."""
    best = {}
    for v in videos:
        views, secs = num(v["view_count"]), num(v["duration"])
        if (views is None or views < cfg["min_views"] or v["id"] in used or not on_topic(v["title"], cfg, v["kind"])
                or (secs is not None and secs > cfg["max_seconds"])):
            continue
        if v["id"] not in best or v["kind"] != "long":
            best[v["id"]] = {"id": v["id"], "views": views, "seconds": secs, "channel": v["channel"],
                             "title": v["title"], "kind": v["kind"],
                             "url": f"https://www.youtube.com/{'watch?v=' if v['kind'] == 'long' else 'shorts/'}{v['id']}"}
    return sorted(best.values(), key=lambda x: -x["views"])[:cfg["count"]]


def selftest():
    cfg = json.loads((HERE / "channels/found-rich/sources.json").read_text(encoding="utf-8"))
    yes = ["Items People Found That Made Them Rich", "Free Items People Sold For Millions!",
           "10 Thrift Store Finds That Made People Rich", "Found a year's salary in the trash"]
    no = ["What Rich People Do Differently", "Married Into a Wealthy Family by Mistake #drama",
          "$2 million worth of meth found in home", "3 Expensive Things Rich People Avoid Buying",
          "Finding $10,000 In Your Bank Account", "Is Searching A Millionaire's Trash Illegal?",
          "I Collected Rich People's Trash"]
    assert not on_topic("You Think I Ain't Worth A Dollar | From The Basement", cfg, "search_short")
    assert all(on_topic(t, cfg) for t in yes), [t for t in yes if not on_topic(t, cfg)]
    assert not any(on_topic(t, cfg) for t in no), [t for t in no if on_topic(t, cfg)]
    long_yes = ["10 Thrift Store Finds That Made People Rich", "Lucky Discoveries that Made Normal People Millionaires"]
    long_no = ["TOP 5 GOLD & SILVER DEALS | Pawn Stars", "I Bought a Storage Unit & Found This.. **JACKPOT**",
               "Son FINDS OUT His DAD Is A MILLIONAIRE", "$50,000 Crystal Treasure Hunt"]
    assert all(on_topic(t, cfg, "long") for t in long_yes), [t for t in long_yes if not on_topic(t, cfg, "long")]
    assert not any(on_topic(t, cfg, "long") for t in long_no), [t for t in long_no if on_topic(t, cfg, "long")]
    v = lambda i, views, kind="short", secs="NA": {"id": i, "view_count": str(views), "duration": secs, "channel": "c",
                                                    "title": "Items People Found That Made Them Rich", "kind": kind}
    got = pick([v("a", 5e6), v("b", 2e6), v("c", 999_999), v("d", 9e6), v("e", 3e6, "long", "4000"), v("a", 5e6, "long", "60")],
               dict(cfg, count=2), used={"d"})
    assert [g["id"] for g in got] == ["a", "b"] and got[0]["kind"] == "short", got
    print("selftest ok")


def main():
    p = argparse.ArgumentParser()
    p.add_argument("channel", nargs="?")
    p.add_argument("--out")
    p.add_argument("--mark-used", action="store_true")
    p.add_argument("--count", type=int)
    p.add_argument("--selftest", action="store_true")
    p.add_argument("--cache", help="raw listing file: read it if it exists, else fetch and save it (for testing filters)")
    a = p.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")
    if a.selftest:
        return selftest()
    cdir = HERE / "channels" / a.channel
    cfg = json.loads((cdir / "sources.json").read_text(encoding="utf-8"))
    if a.count:
        cfg["count"] = a.count
    used_file = cdir / "used-sources.json"
    used = set(json.loads(used_file.read_text(encoding="utf-8"))) if used_file.exists() else set()

    if a.cache and Path(a.cache).exists():
        videos = json.loads(Path(a.cache).read_text(encoding="utf-8"))
    else:
        videos = []
        for ch in cfg["shorts_channels"]:
            print(f"listing {ch} Shorts", file=sys.stderr)
            # the Shorts tab gives no channel name: use the handle
            videos += [dict(v, kind="short", channel=ch if v["channel"] == "NA" else v["channel"])
                       for v in ytdlp_list(f"https://www.youtube.com/{ch}/shorts")]
        for q in cfg["searches"]:
            print(f"searching: {q}", file=sys.stderr)
            videos += [dict(v, kind="search_short" if (num(v["duration"]) or 999) <= 180 else "long")
                       for v in ytdlp_list(f"ytsearch{cfg['search_results_per_query']}:{q}")]
        if a.cache:
            Path(a.cache).write_text(json.dumps(videos, ensure_ascii=False), encoding="utf-8")

    picked = pick(videos, cfg, used)
    if len(picked) < cfg["count"]:
        print(f"only {len(picked)} found (wanted {cfg['count']})", file=sys.stderr)
    result = {"channel": a.channel, "week": date.today().isoformat(), "checked": len(videos), "videos": picked}
    if a.out:
        Path(a.out).parent.mkdir(parents=True, exist_ok=True)
        Path(a.out).write_text(json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8")
    if a.mark_used:
        used_file.write_text(json.dumps(sorted(used | {v["id"] for v in picked}), indent=1), encoding="utf-8")
    for i, v in enumerate(picked, 1):
        print(f"{i:2}. {v['views'] / 1e6:6.1f}M  {v['kind']:5}  {v['channel'][:22]:22}  {v['title'][:70]}  {v['url']}")


if __name__ == "__main__":
    main()
