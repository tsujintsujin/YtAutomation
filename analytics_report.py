"""Turns one day's YouTube Studio reading into that day's analytics file (Justin, 2026-10-25).

    python analytics_report.py found-rich 2026-10-25

Reads   channels/<key>/analytics/raw/<date>.json   (written by the daily Studio read, channels/ANALYTICS.md)
Writes  channels/<key>/analytics/<date>.md         one row per public Short + the change since the last reading
The numbers come from Studio as they are; this only lays them out and works out the day-over-day change.
"""
import json
import sys
from pathlib import Path

HERE = Path(__file__).parent
COLS = [("views", "Views"), ("engaged_views", "Engaged"), ("stayed_pct", "Stayed %"),
        ("avg_view_duration_s", "Avg watched"), ("avg_pct_viewed", "Avg %"), ("likes", "Likes"),
        ("comments", "Comments"), ("shares", "Shares"), ("subs_net", "Subs")]
GROWS = {"views", "engaged_views", "likes", "comments", "shares", "subs_net"}  # totals: show "+N since last"


def fmt(key, v):
    if v is None:
        return "-"
    if key == "avg_view_duration_s":
        return f"{int(v) // 60}:{int(v) % 60:02d}"
    if key in ("stayed_pct", "avg_pct_viewed"):
        return f"{v:.1f}%"
    return f"{v:,}"


def previous(folder, date):
    older = sorted(p for p in (folder / "raw").glob("*.json") if p.stem < date)
    return json.loads(older[-1].read_text(encoding="utf-8")) if older else None


def report(key, date):
    folder = HERE / "channels" / key / "analytics"
    day = json.loads((folder / "raw" / f"{date}.json").read_text(encoding="utf-8"))
    prev = previous(folder, date)
    before = {s["video_id"]: s for s in prev["shorts"]} if prev else {}

    lines = [f"# {day['channel_name']} ({key}): Shorts analytics, {date}", "",
             f"Read from YouTube Studio at {day['read_at']}. "
             f"Studio's full table is complete to **{day.get('table_complete_to') or 'not yet'}**; "
             "Shorts newer than that are read live from their own pages (source `live`)."
             + (f" Change is since the reading of {prev['date']}." if prev else " First reading, no change yet."), "",
             "| Short | Published | Length | Source | " + " | ".join(c[1] for c in COLS) + " | Top traffic |",
             "|" + "---|" * (len(COLS) + 5)]
    for s in sorted(day["shorts"], key=lambda s: s["published"]):
        b = before.get(s["video_id"], {})
        cells = []
        for k, _ in COLS:
            cell = fmt(k, s.get(k))
            if k in GROWS and s.get(k) is not None and b.get(k) is not None:
                cell += f" (+{s[k] - b[k]:,})" if s[k] >= b[k] else f" ({s[k] - b[k]:,})"
            cells.append(cell)
        traffic = ", ".join(f"{n} {p:.1f}%" for n, p in list((s.get("traffic") or {}).items())[:2]) or "-"
        length = f"{s['length_s'] // 60}:{s['length_s'] % 60:02d}" if s.get("length_s") else "-"
        lines.append(f"| {s['title']} (`{s.get('slug') or s['video_id']}`) | {s['published']} | {length} | "
                     f"{s['source']} | " + " | ".join(cells) + f" | {traffic} |")
    notes = [f"- **{s['title']}**: {s['note']}" for s in day["shorts"] if s.get("note")]
    if notes:
        lines += ["", "Notes from Studio:", *notes]
    total = sum(s.get("views") or 0 for s in day["shorts"])
    lines += ["", f"**Channel:** {len(day['shorts'])} public Short{'s' if len(day['shorts']) != 1 else ''}, {total:,} views in total.", ""]
    out = folder / f"{date}.md"
    out.write_text("\n".join(lines), encoding="utf-8")
    return out


if __name__ == "__main__":
    assert fmt("avg_view_duration_s", 47) == "0:47" and fmt("stayed_pct", 30.2) == "30.2%" and fmt("views", 1234) == "1,234"
    print(report(sys.argv[1], sys.argv[2]))
