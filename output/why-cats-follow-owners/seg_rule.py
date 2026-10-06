"""Script -> segments: one image per phrase, ~3-6 s each (never over 6 s).

Split at every punctuation mark; a one-word piece joins its neighbour; a phrase over 6 s is cut at
the connecting word nearest its middle; then short neighbours merge until ~3 s, never past 6 s.
Word-based estimate (Santa measured at 2.96 words/s, his slowest rate seen); the voice step re-times it for real.
"""
import json
import re
from pathlib import Path

WPS = 2.96
MAXW = int(6 * WPS)   # 17 words ~ 5.7 s
MINW = 9              # ~3 s
CUT = {"and", "but", "so", "that", "when", "which", "while", "because", "than", "to", "until", "with",
       "like", "before", "after", "where", "who", "or"}


def cut(p):
    w = p.split()
    if len(w) <= MAXW:
        return [p]
    mid = len(w) // 2
    best = min((i for i in range(3, len(w) - 3) if w[i].lower() in CUT), key=lambda i: abs(i - mid), default=mid)
    return cut(" ".join(w[:best])) + cut(" ".join(w[best:]))


def segment(text):
    t = re.sub(r"\s+", " ", text).strip()
    pieces = [m.strip() for m in re.findall(r'[^,.?!;:]+[,.?!;:]+"?', t)]
    ph, hold = [], ""
    for p in pieces:
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
        ph.append(hold)
    ph = [x for p in ph for x in cut(p)]
    # Choose where images change: best[i] = cheapest way to cover phrases[:i]. A cut after a full stop is
    # free, after a comma costs a little, inside a phrase costs more; segments under ~3 s cost extra,
    # over 6 s are not allowed.
    def end_cost(p):
        c = p.rstrip('"')[-1]
        return 0 if c in ".?!" else 4 if c in ",;:" else 9
    n, INF = len(ph), float("inf")
    best, back = [0] + [INF] * n, [0] * (n + 1)
    for i in range(1, n + 1):
        words = 0
        for j in range(i - 1, -1, -1):
            words += len(ph[j].split())
            if words > MAXW:
                break
            cost = best[j] + end_cost(ph[i - 1]) + (3 * (MINW - words) ** 2 if words < MINW else 0) + 1
            if cost < best[i]:
                best[i], back[i] = cost, j
    segs, i = [], n
    while i:
        segs.append(" ".join(ph[back[i]:i]))
        i = back[i]
    segs.reverse()
    assert re.sub(r"\s", "", "".join(segs)) == re.sub(r"\s", "", t), "segments lost text"
    return segs


if __name__ == "__main__":
    here = Path(__file__).parent
    segs = segment((here / "script.md").read_text(encoding="utf-8"))
    sec = [len(s.split()) / WPS for s in segs]
    print(f"{len(segs)} segments | est. avg {sum(sec)/len(sec):.1f}s, min {min(sec):.1f}s, max {max(sec):.1f}s | under 3 s: {sum(x < 3 for x in sec)}")
    (here / "segments.json").write_text(json.dumps(segs, indent=1, ensure_ascii=False), encoding="utf-8")
