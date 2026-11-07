"""Compare niches: last-30-day long videos (4+ min) from YouTube search sorted by views, per niche.
Per niche: videos found, distinct channels, median views, how many over 10K / 100K, the top 12 with channel subscribers.
Reads YouTube's public search pages (no API key). Search helpers copied from channels/book-stories/niche_scan.py.
Edit NICHES before a run.
usage: python research/tools/nichescan.py OUT.json"""
import json
import re
import statistics
import sys
import time

import requests

NICHES = {
 "money-history-explained": ["explained like you're 5 money", "how the great depression happened explained", "rise and fall of company explained",
                             "how rockefeller got rich explained", "financial crisis explained animated", "how billionaire built empire explained"],
 "pov-money-stories": ["POV you money story", "POV your boss money", "POV millionaire nobody knows", "POV your family money"],
 "what-if-stories": ["what if you had 500 iq", "what if animated story", "what if you could stop time", "what if your reaction time"],
 "luck-survival-worst": ["luckiest people who survived", "most avoidable deaths ever", "worst ways people got trapped", "people who cheated death"],
 "psychology-explained": ["psychology explained animated", "why your brain does this", "dark psychology explained animation", "why people stay broke psychology"],
 "history-daily-life": ["what life was like in medieval times", "worst jobs in history", "how people lived before electricity", "history of everyday things"],
 "found-fortunes": ["people who found treasure worth millions", "thrift store finds worth millions", "found in attic worth millions", "luckiest finds ever"],
 "personal-finance-explained": ["why you are broke explained", "how inflation works explained", "how the rich avoid taxes explained", "how money works animated"],
}
LAST_MONTH_BY_VIEWS = "CAMSBAgEEAE%3D"  # search filter: uploaded this month, sorted by view count
H = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36",
     "Accept-Language": "en-US,en;q=0.9"}


def initial_data(url, **params):
    r = requests.get(url, params=params, headers=H, cookies={"CONSENT": "YES+1"}, timeout=20)
    m = re.search(r"var ytInitialData = (\{.*?\});</script>", r.text, re.S)
    return json.loads(m.group(1)) if m else {}


def find(o, key):
    if isinstance(o, dict):
        if key in o:
            yield o[key]
        for v in o.values():
            yield from find(v, key)
    elif isinstance(o, list):
        for v in o:
            yield from find(v, key)


def number(text):
    """'1,197,020 views' -> 1197020, '3.76K subscribers' -> 3760."""
    m = re.search(r"([\d.,]+)\s*([KMB]?)", text or "")
    if not m:
        return 0
    return int(float(m.group(1).replace(",", "")) * {"": 1, "K": 1e3, "M": 1e6, "B": 1e9}[m.group(2)])


def days(text):
    """'14h ago' -> 0.6, '9d ago' -> 9, '3w ago' -> 21, '1mo ago' -> 30."""
    # "mo" must come before "m": YouTube writes "11mo ago", which would otherwise read as 11 minutes
    m = re.search(r"(\d+)\s*(second|minute|hour|day|week|month|year|mo|s|m|h|d|w|y)", text or "")
    if not m:
        return 30
    n, u = int(m.group(1)), m.group(2)
    return n * {"second": 1 / 86400, "s": 1 / 86400, "minute": 1 / 1440, "m": 1 / 1440, "hour": 1 / 24, "h": 1 / 24,
                "day": 1, "d": 1, "week": 7, "w": 7, "month": 30, "mo": 30, "year": 365, "y": 365}[u] if n else 1


def videos(query):
    out = []
    for v in find(initial_data("https://www.youtube.com/results", search_query=query, sp=LAST_MONTH_BY_VIEWS), "videoRenderer"):
        owner = (v.get("ownerText") or {}).get("runs", [{}])[0]
        out.append({"id": v.get("videoId"), "title": v["title"]["runs"][0]["text"],
                    "views": number((v.get("viewCountText") or {}).get("simpleText")),
                    "days": days((v.get("publishedTimeText") or {}).get("simpleText")),
                    "length": (v.get("lengthText") or {}).get("simpleText", ""),
                    "channel": owner.get("text", ""),
                    "url": owner.get("navigationEndpoint", {}).get("browseEndpoint", {}).get("canonicalBaseUrl", "")})
    return out


def subscribers(url, cache={}):
    if url not in cache:
        s = json.dumps(initial_data("https://www.youtube.com" + url))
        m = re.search(r'"([\d.,]+[KMB]?) subscribers"', s)
        cache[url] = number(m.group(1)) if m else 0
        time.sleep(0.5)
    return cache[url]


def mins(length):
    p = [int(x) for x in length.split(":")] if length else [0]
    return p[0] * 60 + p[1] + p[2] / 60 if len(p) == 3 else (p[0] + p[1] / 60 if len(p) == 2 else 0)


def main(out_path):
    res = {}
    for niche, qs in NICHES.items():
        seen = {}
        for q in qs:
            try:
                for v in videos(q):
                    if v["id"] and mins(v["length"]) >= 4:
                        seen.setdefault(v["id"], v)
            except Exception as e:  # one failed search shouldn't lose the niche
                print("search failed:", q, e, flush=True)
            time.sleep(1.5)
        rows = sorted(seen.values(), key=lambda v: -v["views"])
        views = [v["views"] for v in rows]
        for v in rows[:12]:
            v["subs"] = subscribers(v["url"]) if v["url"] else 0
            v["min"] = round(mins(v["length"]), 1)
        res[niche] = {"videos": len(rows), "channels": len({v["channel"] for v in rows}),
                      "median": statistics.median(views) if views else 0,
                      "over_10k": sum(x >= 10_000 for x in views), "over_100k": sum(x >= 100_000 for x in views),
                      "small_channel_hits": sum(1 for v in rows[:12] if v.get("subs", 10**9) < 20_000 and v["views"] >= 50_000),
                      "top": [{k: v.get(k) for k in ("views", "days", "subs", "min", "channel", "title")} for v in rows[:12]]}
        r = res[niche]
        print(niche, r["videos"], "videos,", r["channels"], "channels, median", r["median"], ">10K", r["over_10k"],
              ">100K", r["over_100k"], "small-channel hits", r["small_channel_hits"], flush=True)
    json.dump(res, open(out_path, "w", encoding="utf-8"), ensure_ascii=False, indent=1)


if __name__ == "__main__":
    assert mins("14:47") == 14 + 47 / 60 and mins("1:02:00") == 62 and number("3.76K subscribers") == 3760
    assert days("11mo ago") == 330 and days("1 month ago") == 30 and days("6y ago") == 2190 and days("9d ago") == 9
    main(sys.argv[1])
