"""Builds script.json (segments + full self-contained Gemini prompts) from script.md.

Every segment's text must appear in script.md in order; the check at the bottom fails otherwise.
Each `full_prompt` carries the whole style block, character blocks and negatives, never "same as before".
"""
import json
import re
from pathlib import Path

HERE = Path(__file__).parent

STYLE = ("Generate one image. 16:9 landscape, full-bleed: the artwork fills the entire canvas edge to edge, like a single "
         "full-screen frame from an animated documentary on YouTube. Look: digital 2D animation background art, clean confident "
         "outlines of varying weight, cel shading with two tones of shadow, muted earthy natural palette, natural proportions, "
         "calm informative documentary mood, the scene continues past every edge of the frame. Match the art style of the attached "
         "finished example frame exactly: the same line weight, the same flat two-tone cel shading, the same muted earthy palette "
         "and the same level of background detail. Every person and every animal is drawn in this same 2D illustrated style, never "
         "photographic, never 3D rendered.")

GEEK = ("The Geek appears in this shot and must match the attached Geek character sheet exactly: a skinny young man with messy "
        "short dark-brown hair, large round thin black-framed glasses over simple black dot eyes, a few freckles across his cheeks, "
        "peach skin, an oversized forest-green hoodie with two dangling drawstrings and a front pouch pocket over a grey t-shirt, "
        "charcoal-grey jeans, black-and-white canvas sneakers. He is drawn in flat 2D comic style with thick black outlines and flat "
        "color, so he stands out against the detailed, textured environment. His humor comes from deadpan posture, not exaggerated "
        "faces. He carries no backpack, bag or anything on his back.")

CAT = ("A silver tabby cat appears in this shot and must match the attached cat character sheet exactly: a medium-sized adult "
       "domestic short-haired cat with a pale silver-white coat covered in bold black swirling marbled tabby markings, a black "
       "bullseye swirl on each side of the body, black stripes down the spine, thin black lines on the forehead and cheeks, a black "
       "and silver ringed tail with a black tip, a clean white chest bib, a white muzzle and chin, four white paws, a pink nose, "
       "pale greenish-yellow eyes with vertical pupils, and medium triangular ears with pink insides. Natural cat anatomy and "
       "proportions, drawn in flat 2D comic style with thick black outlines and flat color like the attached sheet. It shows "
       "feeling only through ears, tail, eyes and posture, never a human-like smile or cartoon face. It is the only silver tabby "
       "cat in the image.")

NEGATIVE = ("Do not include: any border, margin, frame, panel outline, comic panel border, rounded corners, vignette, paper texture, "
            "text, letters, numbers, labels, captions, signs with writing, speech bubbles, watermarks, human-like faces on animals, "
            "chibi proportions, blush cheeks, photographic or 3D-rendered elements.")

from scenes import SCENES


def full_prompt(geek, cat, scene):
    parts = [STYLE]
    refs = ["The first attached image is a finished example frame; match its art style."]
    if geek:
        parts.append(GEEK)
        refs.append("The attached Geek character sheet shows The Geek; match him to it exactly.")
    if cat:
        parts.append(CAT)
        refs.append("The attached cat character sheet shows the cat; match it exactly.")
    if not geek:
        parts.append("No young man with round glasses and a green hoodie appears in this image.")
    if not cat:
        parts.append("No silver tabby cat with black swirling markings appears in this image; the only animals are the ones described in the scene.")
    return " ".join(parts + refs + ["Scene: " + scene, NEGATIVE])


BANNED = re.compile(r"every (image|shot|frame)|same (as|kind|room|cat|test|village)|\bagain\b|earlier|previous|as before|from before|other images|last (image|shot)", re.I)


def check_standalone(prompt):
    hit = BANNED.search(prompt)
    assert not hit, f"prompt points outside itself: '{hit.group(0)}'"
    return prompt


texts = json.loads((HERE / "segments.json").read_text(encoding="utf-8"))
assert len(texts) == len(SCENES), f"{len(texts)} segments but {len(SCENES)} scenes"
segments = [{"id": i, "text": t, "geek": bool(g), "cat": bool(c), "scene": sc, "prompt": check_standalone(full_prompt(g, c, sc))}
            for i, (t, (g, c, sc)) in enumerate(zip(texts, SCENES), 1)]

# Check: segment texts, joined, are exactly the narration in script.md (whitespace-normalised).
norm = lambda s: re.sub(r"\s+", " ", s).strip()
assert norm(" ".join(s["text"] for s in segments)) == norm((HERE / "script.md").read_text(encoding="utf-8")), "segments drifted from script.md"

(HERE / "script.json").write_text(json.dumps({
    "title": "Why Do Cats Follow Their Owners Everywhere?",
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
