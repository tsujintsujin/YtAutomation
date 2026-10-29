"""script.md -> segments.json: one picture per ~4-7 s (MONETIZATION.md R4: ~5 s; voice ~2.9 words/s).
A sentence is one segment; a sentence over 20 words is cut at the comma nearest its middle; a sentence of 4 words
or fewer... (7 or fewer, if the two stay within 20 words) joins the one before it in the same paragraph (one moment, one picture). Chapter headings are not spoken."""
import json, re
from pathlib import Path
HERE = Path(__file__).parent

def narration():
    """[(chapter, paragraph text)] from script.md; '## End' counts as a chapter with no YouTube chapter title."""
    out, chap = [], None
    for line in (HERE / "script.md").read_text(encoding="utf-8").splitlines():
        if line.startswith("## "):
            chap = line[3:].strip()
        elif chap and line.strip():
            out.append((chap, line.strip()))
    return out

def split(par):
    sents = re.split(r'(?<=[.?!])["”]?\s+', par)
    segs = []
    for s in sents:
        w = s.split()
        if len(w) > 20 and "," in s:
            cuts = [m.end() for m in re.finditer(r",\s", s)]
            mid = len(s) / 2
            c = min(cuts, key=lambda x: abs(x - mid))
            segs += [s[:c].strip(), s[c:].strip()]
        elif len(w) <= 7 and segs and len((segs[-1] + " " + s).split()) <= 20:
            segs[-1] += " " + s
        else:
            segs.append(s)
    return segs

segs = []
for chap, par in narration():
    for t in split(par):
        segs.append({"chapter": chap, "text": t})
(HERE / "segments.json").write_text(json.dumps(segs, indent=1, ensure_ascii=False), encoding="utf-8")
if __name__ == "__main__":
    for i, s in enumerate(segs, 1):
        print(i, s["chapter"][:6], len(s["text"].split()), s["text"])
    print(len(segs), "segments", sum(len(s["text"].split()) for s in segs), "words")
