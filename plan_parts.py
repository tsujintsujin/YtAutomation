"""Give split Shorts their posting days and times; prints the rows for the sheet's Schedule tab (tab-separated).

Usage: python plan_parts.py <first day YYYY-MM-DD> <channel>:<slug>,<slug>,... [<channel>:...]
       python plan_parts.py --selftest

Justin, 2026-11-01: each channel posts one story a day; all parts of that story go out the same day, in order, at
random times (to learn which hours do best), so a sequence is always complete. A Short under 1 minute stays whole
and is that channel's post for its day. Slugs are posted in the order given, one day each, from the first day.
Times: random minutes between 7:00 AM and 11:00 PM Philippines time, at least 2 hours apart.
Reads each video's cuts.json (parts.py) and script.json (title).
"""
import datetime as dt, json, os, random, sys

HERE = os.path.dirname(os.path.abspath(__file__))
NAMES = {"found-rich": "LuckySticks", "what-happens-now": "OldSticksNewSticks", "chaotic-lives": "TangledSticks"}
FIRST, LAST, GAP = 7 * 60, 23 * 60, 120  # minutes of the day


def times(n, rng):
    """n random minutes in [FIRST, LAST], sorted, each GAP apart."""
    while True:
        t = sorted(rng.randint(FIRST, LAST) for _ in range(n))
        if all(b - a >= GAP for a, b in zip(t, t[1:])):
            return t


def rows(first_day, plan, rng):
    out = []
    for ch, slugs in plan:
        for k, slug in enumerate(slugs):
            day = first_day + dt.timedelta(days=k)
            folder = os.path.join(HERE, "channels", ch, "videos", slug)
            cuts = json.load(open(os.path.join(folder, "cuts.json"), encoding="utf-8"))
            title = json.load(open(os.path.join(folder, "script.json"), encoding="utf-8"))["title"]
            parts = cuts["parts"] or [{"n": "whole", "of": "", "start": 0, "end": cuts["length"]}]
            for p, m in zip(parts, times(len(parts), rng)):
                yt_title = title if p["n"] == "whole" else f"{title} | Part {p['n']}"
                out.append([NAMES[ch], slug, p["n"], p["of"], yt_title, round(p["end"] - p["start"], 1),
                            day.isoformat(), f"{m // 60:02d}:{m % 60:02d}", day.strftime("%a"), m // 60,
                            "to upload", "", "", ""])
    return sorted(out, key=lambda r: (r[6], r[7]))


HEAD = ["Channel", "Story", "Part", "Of", "Title on YouTube", "Length (s)", "Post date", "Post time (PHT)", "Weekday",
        "Hour", "Status", "Video ID", "Link", "Notes"]


def selftest():
    rng = random.Random(1)
    for n in (1, 2, 3, 4, 5):
        t = times(n, rng)
        assert len(t) == n and all(FIRST <= x <= LAST for x in t) and all(b - a >= GAP for a, b in zip(t, t[1:]))
    print("selftest ok")


if __name__ == "__main__":
    if sys.argv[1:] == ["--selftest"]:
        selftest()
    else:
        first = dt.date.fromisoformat(sys.argv[1])
        plan = [(a.split(":")[0], a.split(":")[1].split(",")) for a in sys.argv[2:]]
        sys.stdout.reconfigure(encoding="utf-8")  # titles have £ and €
        print("\n".join("\t".join(str(c) for c in r) for r in [HEAD] + rows(first, plan, random.Random())))
