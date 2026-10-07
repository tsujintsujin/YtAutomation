"""Thumbnail prompts: output/<slug>/thumb-ideas.json -> output/<slug>/thumbnails.json.

thumb-ideas.json = {"thumbnails": [{"text": "WHY THE BISCUITS?", "scene": "..."}, ...]}   (5 ideas, written per video)
thumbnails.json  = {"thumbnails": [{"id": 1, "text": ..., "scene": ..., "prompt": <complete standalone prompt>}, ...]}

n8n's "3b. Thumbnails" group sends each prompt (with the 3 reference sheets) to its own Gemini window and saves the
answer as thumbs/thumb-N.jpg. Kept apart from script.json: a newer script.json makes voice.py redo the voice.

usage: python thumbnails.py output/<slug>
"""
import json
import sys
from pathlib import Path

TEMPLATE = (
    "Generate one image. 16:9 landscape YouTube thumbnail, 1280x720 framing, full-bleed: the artwork fills the entire "
    "canvas edge to edge. "
    "Art style: match the first attached finished example frame exactly: the same clean confident outlines of varying "
    "weight, the same flat cel shading with two tones of shadow, the same muted earthy natural palette and the same 2D "
    "illustrated look. Every person and every animal is drawn in this same 2D style, never photographic, never 3D "
    "rendered. Because this is a thumbnail, make the scene brightly lit with strong light-dark contrast and a simple, "
    "uncluttered background so it reads clearly at a small size, but keep the same palette and style. "
    "The Geek appears and must match the attached Geek character sheet exactly: a skinny young man with messy short "
    "dark-brown hair, large round thin black-framed glasses over simple black dot eyes, a few freckles across his "
    "cheeks, peach skin, an oversized forest-green hoodie with two dangling drawstrings and a front pouch pocket over a "
    "grey t-shirt, charcoal-grey jeans, black-and-white canvas sneakers. Flat 2D comic style with thick black outlines "
    "and flat color. His humor comes from deadpan posture and a flat, knowing expression, not an exaggerated face. He "
    "carries no backpack, bag or anything on his back. "
    "The silver tabby cat appears and must match the attached cat character sheet exactly: a medium-sized adult "
    "domestic short-haired cat with a pale silver-white coat covered in bold black swirling marbled tabby markings, a "
    "black bullseye swirl on each side of the body, black stripes down the spine, thin black lines on the forehead and "
    "cheeks, a black and silver ringed tail with a black tip, a clean white chest bib, a white muzzle and chin, four "
    "white paws, a pink nose, pale greenish-yellow eyes with vertical pupils, and medium triangular ears with pink "
    "insides. Natural cat anatomy, flat 2D comic style with thick black outlines. It shows feeling only through ears, "
    "tail, eyes and posture, never a human-like smile or cartoon face. It is the only silver tabby cat in the image. "
    "The first attached image is a finished example frame; match its art style. The attached Geek character sheet "
    "shows The Geek; match him to it exactly. The attached cat character sheet shows the cat; match it exactly. "
    "Composition: a close, medium shot. The Geek and the cat are large in the frame, together filling the right "
    "two-thirds of the image, faces clearly visible. Nothing important in the bottom-right corner. "
    "Text: in the left third of the image, the words \"{text}\" in huge, bold, hand-lettered comic capitals, bright "
    "white fill with a thick black outline and a slight drop shadow, stacked on two or three lines, very easy to read "
    "at a small size. Spell it exactly as written, letter for letter. This is the only text in the image. "
    "Scene: {scene} "
    "Do not include: any other text, letters, numbers, labels, logos, signs with writing, speech bubbles, arrows, "
    "emoji, watermarks, any border, margin, frame, panel outline, rounded corners, vignette, paper texture, "
    "human-like faces on animals, chibi proportions, blush cheeks, photographic or 3D-rendered elements."
)


def build(folder):
    ideas = json.loads((folder / "thumb-ideas.json").read_text(encoding="utf-8"))["thumbnails"]
    out = [{"id": i, "text": t["text"], "scene": t["scene"],
            "prompt": TEMPLATE.replace("{text}", t["text"]).replace("{scene}", t["scene"])}
           for i, t in enumerate(ideas, 1)]
    for t in out:
        assert "{" not in t["prompt"], f"thumbnail {t['id']}: placeholder left in the prompt"
    (folder / "thumbnails.json").write_text(json.dumps({"thumbnails": out}, indent=2, ensure_ascii=False) + "\n",
                                            encoding="utf-8")
    return out


if __name__ == "__main__":
    for t in build(Path(sys.argv[1])):
        print(t["id"], t["text"])
