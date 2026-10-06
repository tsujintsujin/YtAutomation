"""Script -> segments: one image per phrase, 2-4 s each (Justin, 2026-10-05: 4 s max).

Split at every punctuation mark; a one-word piece joins its neighbour; a phrase over 4 s is cut at
the connecting word nearest its middle; then neighbours merge, preferring cuts after a full stop,
never past 4 s, avoiding segments under 2 s.
Length estimate = words / 3.1 (am_liam's slow end at speed 1.0, measured on the first video: p10 2.82 w/s
at 0.9) + voice.py's own pauses after every punctuation mark. The voice step re-times it for real.
Run with tts/.venv python (imports voice.py for the pauses).
"""
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE.parent.parent))
from voice import pause_after, pieces  # noqa: E402

WPS = 3.1
MAX_S, MIN_S = 4.0, 2.0
CUT = {"and", "but", "so", "that", "when", "which", "while", "because", "than", "to", "until", "with",
       "like", "before", "after", "where", "who", "or", "for", "in", "on", "at", "from", "into", "around"}


def est(text):
    return len(text.split()) / WPS + sum(pause_after(p) for p in pieces(text))


def cut(p):
    w = p.split()
    if est(p) <= MAX_S or len(w) < 6:
        return [p]
    mid = len(w) // 2
    # never cut right after "a", "the", "now", or another connecting word ("in / which", "now / and then")
    ok = [i for i in range(2, len(w) - 1) if w[i - 1].lower() not in CUT | {"a", "an", "the", "now", "its", "your", "of"}
          and w[i].lower() != "of" and w[i + 1].lower() not in {"which", "whom"}]
    best = min((i for i in ok if w[i].lower() in CUT), key=lambda i: abs(i - mid),
               default=min(ok, key=lambda i: abs(i - mid), default=mid))
    return cut(" ".join(w[:best])) + cut(" ".join(w[best:]))


def segment(text):
    t = re.sub(r"\s+", " ", text).strip()
    ph, hold = [], ""
    for p in pieces(t):
        p = (hold + " " + p).strip()
        hold = ""
        if len(p.split()) == 1:
            if p.rstrip('"')[-1] in ".?!" and ph:
                ph[-1] += " " + p
            else:
                hold = p
        else:
            ph.append(p)
    if hold:
        ph[-1] += " " + hold
    ph = [x for p in ph for x in cut(p)]

    # best[i] = cheapest way to cover phrases[:i]. A cut after a full stop is free, after a comma costs a
    # little, inside a phrase costs more; segments under 2 s cost extra, over 4 s are not allowed.
    def end_cost(p):
        c = p.rstrip('"')[-1]
        return 0 if c in ".?!" else 4 if c in ",;:" else 9
    n, INF = len(ph), float("inf")
    best, back = [0] + [INF] * n, [0] * (n + 1)
    for i in range(1, n + 1):
        for j in range(i - 1, -1, -1):
            s = est(" ".join(ph[j:i]))
            if s > MAX_S and j < i - 1:
                break
            cost = best[j] + end_cost(ph[i - 1]) + (12 * (MIN_S - s) ** 2 if s < MIN_S else 0) + 1
            if cost < best[i]:
                best[i], back[i] = cost, j
    segs, i = [], n
    while i:
        segs.append(" ".join(ph[back[i]:i]))
        i = back[i]
    segs.reverse()
    assert re.sub(r"\s", "", "".join(segs)) == re.sub(r"\s", "", t), "segments lost text"
    assert all(len(s.split()) > 1 for s in segs), "one-word segment"
    return segs


if __name__ == "__main__":
    segs = segment((HERE / "script.md").read_text(encoding="utf-8"))
    sec = [est(s) for s in segs]
    print(f"{len(segs)} segments | est. total {sum(sec)/60:.1f} min | avg {sum(sec)/len(sec):.1f}s, "
          f"min {min(sec):.1f}s, max {max(sec):.1f}s | under 2 s: {sum(x < 2 for x in sec)} | over 4 s: {sum(x > 4 for x in sec)}")
    (HERE / "segments.json").write_text(json.dumps(segs, indent=1, ensure_ascii=False), encoding="utf-8")
