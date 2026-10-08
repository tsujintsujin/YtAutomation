"""Puts the opening question in front of the story in script.json, and marks the channel intro after it in
intro.json (Justin, 2026-10-07: every video starts with the question, then the intro clip, then the story).

The three segments get new ids (309-311) so every existing segment keeps its id and its image.
Run after build_script.py (which rebuilds script.json without them). Safe to run twice.
"""
import json
import sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE.parents[1]))
from prompt_kit import build  # noqa: E402
from scenes import PLACES  # noqa: E402

OPENING = [
    ("Why does your cat knead you like a lump of dough?",
     (1, 1, "room_evening", "The silver tabby cat stands on the Geek's lap as he sits on the brown sofa, kneading his "
      "stomach with both white front paws like dough, eyes half closed, while he looks down at it with a flat, "
      "puzzled expression, arms held up out of the way.")),
    ("Left paw, right paw, purring, eyes half shut.",
     (1, 1, "room_close_evening", "Close-up of the silver tabby cat's two white front paws pressing in turn into the "
      "Geek's charcoal-grey jeans as he sits on the brown sofa, one paw down, one lifted; above them the cat's face, "
      "eyes half shut and blissful. Only his jeans and the hem of his green hoodie show.")),
    ("Why would a grown predator do that at all?",
     (0, 1, "garden", "The silver tabby cat crouches low in the tall grass in a stalking pose, body flat, eyes "
      "locked forward, ears pricked, every muscle tense like a small hunter.")),
]
FIRST_ID = 309
LAST_OPENING = FIRST_ID + len(OPENING) - 1

script = json.loads((HERE / "script.json").read_text(encoding="utf-8"))
story = [s for s in script["segments"] if s["id"] < FIRST_ID]
assert max(s["id"] for s in story) == FIRST_ID - 1, "story ids changed: pick a new FIRST_ID"
opening = [{"id": FIRST_ID + n, "text": t, "geek": g, "cat": c, "scene": sc, "prompt": pr}
           for n, ((t, _), (g, c, sc, pr)) in enumerate(zip(OPENING, build([s for _, s in OPENING], PLACES)))]
script["segments"] = opening + story
(HERE / "script.json").write_text(json.dumps(script, indent=2, ensure_ascii=False), encoding="utf-8")

intro = json.loads((HERE / "intro.json").read_text(encoding="utf-8"))
intro["after_segment"] = LAST_OPENING
(HERE / "intro.json").write_text(json.dumps(intro, indent=2) + "\n", encoding="utf-8")
print(f"{len(opening)} opening segments ({FIRST_ID}-{LAST_OPENING}) + {len(story)} story segments; "
      f"intro after segment {LAST_OPENING}")
