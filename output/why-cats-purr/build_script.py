"""Builds script.json (segments + full self-contained Gemini prompts) from script.md.

Every segment's text must appear in script.md in order; the check at the bottom fails otherwise.
Prompts come from prompt_kit.py (YtAutomation root): style, place, characters and negatives in full in every prompt.
"""
import json
import re
from pathlib import Path

HERE = Path(__file__).parent

import sys
sys.path.insert(0, str(HERE.parents[1]))
from prompt_kit import build  # noqa: E402
from scenes import SCENES, PLACES  # noqa: E402

texts = json.loads((HERE / "segments.json").read_text(encoding="utf-8"))
assert len(texts) == len(SCENES), f"{len(texts)} segments but {len(SCENES)} scenes"
segments = [{"id": i, "text": t, "geek": g, "cat": c, "scene": sc, "prompt": pr}
            for i, (t, (g, c, sc, pr)) in enumerate(zip(texts, build(SCENES, PLACES)), 1)]

# Check: segment texts, joined, are exactly the narration in script.md (whitespace-normalised).
norm = lambda s: re.sub(r"\s+", " ", s).strip()
assert norm(" ".join(s["text"] for s in segments)) == norm((HERE / "script.md").read_text(encoding="utf-8")), "segments drifted from script.md"

(HERE / "script.json").write_text(json.dumps({
    "title": "Why Does Your Cat Purr?",
    "voice": "am_liam",
    "segments": segments,
}, indent=2, ensure_ascii=False), encoding="utf-8")

# Gemini batches: 4 prompts per message (8 made Gemini stop halfway and ask).
bdir = HERE / "batches"
bdir.mkdir(exist_ok=True)
for f in bdir.glob("*.txt"):
    f.unlink()
for b in range(0, len(segments), 4):
    group = segments[b:b + 4]
    body = [f"Generate {len(group)} separate images, one for each numbered prompt below. Each prompt is complete on its own."]
    for n, s in enumerate(group, 1):
        body.append(f"\n{n}. (image {s['id']:03d}) {s['prompt']}")
    (bdir / f"batch-{b // 4 + 1:02d}_img-{group[0]['id']:03d}-{group[-1]['id']:03d}.txt").write_text("\n".join(body), encoding="utf-8")
print(f"{len(segments)} segments, {sum(len(s['text'].split()) for s in segments)} words, {len(list(bdir.glob('*.txt')))} batches")
