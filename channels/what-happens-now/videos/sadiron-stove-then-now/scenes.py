"""Image prompts for sadiron-stove-then-now, written as one story (channels/SHORTS_RULES.md "How image prompts are
written"; worked example: ../tooth-key-then-now/scenes.py). Checks every line against script.md; this file approves the
script (no approval step) and writes scene + full prompt for every line into script.json.
usage: python channels/what-happens-now/videos/sadiron-stove-then-now/scenes.py"""
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent                 # videos/<slug>
ROOT = HERE.parents[3]                                 # YtAutomation
sys.path.insert(0, str(ROOT))
from dashboard import approve, short_lines, short_prompt       # the script's lines, and the fixed frame around every prompt

SETTINGS = json.loads((HERE.parents[1] / "settings.json").read_text(encoding="utf-8"))
STYLE = SETTINGS["image_style"]

# ---- the same words every time a person, object or place appears ----
# the eighteen hundreds
KITCHEN = ("a kitchen in the eighteen hundreds: a big black iron cooking stove with a flat stovetop and a stovepipe "
           "going up into the wall, a wooden table, a window with plain curtains, wooden floorboards, a shelf with jugs")
SAD_IRON = ("a sad iron (a heavy solid lump of black iron with a flat bottom, pointed at the front like a boat, with a "
            "curved metal handle on top made in one piece with the body)")
SAD_IRONS = ("sad irons (heavy solid lumps of black iron with flat bottoms, pointed at the front like boats, each with "
             "a curved metal handle on top made in one piece with the body)")
WOMAN = ("a stick-figure woman from the eighteen hundreds (hair in a bun, a long plain dress, an apron and her sleeves "
         "rolled up)")
CLOTH = "a folded thick cloth pad"
BOARD = "a long wooden ironing board laid across the backs of two chairs, with a white cotton shirt spread on it"
POTTS = ("an inventor from eighteen seventy-one (a stick-figure woman in a long dress with a high collar and her hair "
         "pinned up neatly)")
POTTS_IRON = ("a Mrs Potts iron (a heavy iron body pointed at both ends, with no handle of its own; one curved wooden "
              "handle on a metal clip clips onto its top)")
POTTS_BODIES = "three handle-less iron bodies, each pointed at both ends"
HANDLE = "one curved wooden handle on a metal clip"
# now
YOU = "a stick-figure young man (short spiky hair, plain T-shirt and jeans)"
ROOM_NOW = ("a modern living room: an ironing board with a white shirt on it, a wall socket near the floor, a sofa, a "
            "window")
IRON = ("an electric steam iron (a smooth plastic body with a handle, a small round dial on top, a clear water tank at "
        "the front, a flat metal bottom plate with little steam holes, and a power cord)")
IRON_CUT = ("a cut-away side view of an electric steam iron, as if sliced in half: the clear water tank at the front, "
            "a zigzag heating wire inside the flat metal bottom plate, and a tiny switch made of a thin metal strip "
            "above the plate")
# ---- the one coloured thing per picture (settings.json "colour_subject") ----
C_STOVE = "the stove's fire, seen through its little door: flat orange and yellow"
C_IRON = "the sad iron: flat dark iron grey"
C_HOT = "the sad iron on the stove: flat glowing orange-red"
C_IRONS = "the row of sad irons: flat dark iron grey"
C_SOLID = "the solid metal inside the cut-away iron: flat dark iron grey"
C_THREE = "the three sad irons: flat glowing orange-red"
C_CLOTH = "the thick cloth pad: flat blue and white check"
C_BURN = "the hot metal handle's heat lines: flat bright red"
C_SHIRT = "the shirt: flat light blue"
C_COOL = "the cooled iron: flat dark iron grey"
C_NEXT = "the next hot iron: flat glowing orange-red"
C_POTTS = "the inventor's dress: flat dark green"
C_HANDLE = "the wooden handle: flat warm brown"
C_CLICK = "the wooden handle flat warm brown, and the hot iron body flat glowing orange-red"
C_HAPPY = "the wooden handle: flat warm brown"
C_PLUG = "the iron's plug and cord: flat black, with a small flat yellow spark at the socket"
C_WIRE = "the heating wire: flat glowing orange-red"
C_DIAL = "the little dial: flat bright red"
C_SWITCH = "the tiny metal switch strip: flat copper orange"
C_WATER = "the water: flat bright blue"
C_STEAM = "the steam: flat pale blue-white puffs"
C_SMOOTH = "the shirt: flat light blue"
C_ALL = "all the sad irons: flat glowing orange-red"
C_DONE = "the smooth shirt: flat light blue"
CAPTIONS = ("The place fills the whole frame; keep the very top and very bottom of the frame calm (sky, wall or floor) "
            "for captions. Never write any name, label or caption under or beside anyone or anything.")

M = 26


def shot(n, text, what, place, must, never="", colour=""):
    what = re.sub(r"(^|\. )([a-z])", lambda m: m[1] + m[2].upper(), what)   # blocks start lowercase
    return n, text, " ".join(x for x in (
        f"This is picture {n} of {M} in one continuous picture story; draw exactly this moment.",
        what, f"Place: {place}.",
        f"The one coloured thing in this picture is {colour}; every other person, object and the whole place are black "
        "ink lines only, no colour.",
        f"It MUST show: {must}.", f"NEVER: {never}." if never else "", CAPTIONS) if x)


S = [
 shot(1, "In the eighteen hundreds,",
      "Wide view of the kitchen; the big black iron stove stands against the wall with a fire glowing through its "
      "little door.",
      KITCHEN,
      "the old kitchen with its iron cooking stove",
      "any electric thing",
      colour=C_STOVE),
 shot(2, "your iron was a solid lump of metal.",
      f"{SAD_IRON} drawn big, sitting on the wooden table.",
      KITCHEN,
      "the heavy solid lump of an iron",
      "an electric iron, any cord",
      colour=C_IRON),
 shot(3, "And you heated it on the stove.",
      f"{SAD_IRON} sits on the hot stovetop, wavy heat lines rising around it.",
      KITCHEN,
      "the iron heating on the stovetop",
      "any cord or plug",
      colour=C_HOT),
 shot(4, "It was called a sad iron.",
      f"A row of {SAD_IRONS} stands on a wooden shelf by the stove, from big to small.",
      KITCHEN,
      "the row of sad irons on the shelf",
      "any letters or labels",
      colour=C_IRONS),
 shot(5, "\"Sad\" was an old word for solid.",
      f"Cut-away view of {SAD_IRON}, as if sliced in half: solid metal all the way through, with no hollow space, "
      "shaded with even hatch lines.",
      "a plain wooden table top in an old kitchen; the cut-away iron fills most of the frame",
      "the iron being solid metal all the way through",
      "any letters",
      colour=C_SOLID),
 shot(6, "You set a few of them on the hot stove at once.",
      f"Three {SAD_IRONS} sit side by side on the hot stovetop, heat lines rising from all of them.",
      KITCHEN,
      "three irons heating on the stove at the same time",
      "any cord or plug",
      colour=C_THREE),
 shot(7, "When one was hot, you grabbed it with a thick cloth.",
      f"{WOMAN} lifts one hot sad iron off the stove, gripping its metal handle through {CLOTH}.",
      KITCHEN,
      "the woman grabbing a hot iron with a thick cloth",
      "bare hands on the handle",
      colour=C_CLOTH),
 shot(8, "Its handle was metal too, and it could burn you.",
      "Close view: the curved metal handle of a hot sad iron with heat lines rising off it; a bare stick-figure hand "
      "jerks back from it, small ouch lines around the fingers.",
      KITCHEN + "; the close view fills most of the frame",
      "the hot metal handle burning a bare hand",
      "any blood, any wound",
      colour=C_BURN),
 shot(9, "You pressed it over your shirt, back and forth.",
      f"{WOMAN} presses a hot sad iron over the shirt on {BOARD}, pushing it back and forth, a double arrow showing "
      "the motion.",
      KITCHEN,
      "the woman ironing the shirt back and forth",
      "an electric iron, any cord",
      colour=C_SHIRT),
 shot(10, "Soon, it cooled down.",
      f"The sad iron sits on the shirt on {BOARD}; only one faint heat line is left above it, and {WOMAN} touches "
      "it, frowning.",
      KITCHEN,
      "the iron going cold in the middle of ironing",
      "any cord",
      colour=C_COOL),
 shot(11, "So you put it back,",
      f"{WOMAN} sets the cooled sad iron back down on the stovetop next to the other irons.",
      KITCHEN,
      "the woman putting the cold iron back on the stove",
      "any cord",
      colour=C_COOL),
 shot(12, "and grabbed the next hot one.",
      f"{WOMAN} picks up the next hot sad iron from the stovetop with {CLOTH}, heat lines rising from it.",
      KITCHEN,
      "the woman picking up the next hot iron",
      "bare hands on the handle",
      colour=C_NEXT),
 shot(13, "In eighteen seventy-one, a woman named Mary Potts made it easier.",
      f"{POTTS} stands at a workbench and proudly holds up {POTTS_IRON}.",
      "a small workshop in eighteen seventy-one: a wooden workbench with tools, a window, a stove in the corner",
      "the inventor proudly holding up her new iron",
      "any name written anywhere, any likeness of a real person",
      colour=C_POTTS),
 shot(14, "Her irons shared one wooden handle that clipped on and off.",
      f"On the workbench sit {POTTS_BODIES}; {POTTS} lifts {HANDLE} off one of them, showing that it comes off.",
      "a small workshop in eighteen seventy-one: a wooden workbench with tools, a window, a stove in the corner",
      "the one wooden handle lifting off the iron body",
      "any letters",
      colour=C_HANDLE),
 shot(15, "You clipped it onto whichever iron was hot.",
      f"{WOMAN} clips {HANDLE} onto one of {POTTS_BODIES} heating on the hot stovetop, a small click mark at the "
      "clip.",
      KITCHEN,
      "the wooden handle clicking onto a hot iron body on the stove",
      "any cord",
      colour=C_CLICK),
 shot(16, "No more burned hands.",
      f"{WOMAN} irons the shirt on {BOARD} happily, holding the iron by its cool curved wooden handle with her bare "
      "hand, smiling.",
      KITCHEN,
      "the woman ironing comfortably by the cool wooden handle",
      "any cloth pad, any burn",
      colour=C_HAPPY),
 shot(17, "Today, you plug in an electric iron.",
      f"{YOU} pushes the plug of {IRON} into the wall socket.",
      ROOM_NOW,
      "the young man plugging in the electric iron",
      "any stove, any letters or logos",
      colour=C_PLUG),
 shot(18, "A wire inside its flat bottom heats up.",
      f"{IRON_CUT}; the zigzag heating wire in the bottom plate glows, with heat lines.",
      "a plain flat white background with a simple table line",
      "the heating wire inside the bottom plate glowing hot",
      "any letters",
      colour=C_WIRE),
 shot(19, "A little dial sets how hot.",
      f"Close view of the young man's fingers turning the small round dial on top of {IRON}; a curved arrow around the dial.",
      ROOM_NOW + "; the close view of the iron fills most of the frame",
      "fingers turning the little dial on the iron",
      "any numbers or letters on the dial",
      colour=C_DIAL),
 shot(20, "A tiny switch inside turns the heat off when it's hot enough,",
      f"{IRON_CUT}; the thin metal strip of the tiny switch has bent up and opened a small gap, and the heating wire "
      "below has stopped glowing.",
      "a plain flat white background with a simple table line",
      "the tiny switch opening and the heat turning off",
      "any letters",
      colour=C_SWITCH),
 shot(21, "and back on when it cools.",
      f"{IRON_CUT}; the thin metal strip of the tiny switch has bent back down and closed the gap, and the heating "
      "wire below is glowing again.",
      "a plain flat white background with a simple table line",
      "the tiny switch closing again and the heat coming back on",
      "any letters",
      colour=C_SWITCH),
 shot(22, "You pour water into a tank.",
      f"{YOU} pours water from a cup into the clear water tank at the front of {IRON}.",
      ROOM_NOW,
      "water being poured into the iron's tank",
      "any letters or logos",
      colour=C_WATER),
 shot(23, "It drips onto the hot plate, and turns to steam.",
      f"{IRON_CUT}; drops of water drip down from the tank onto the hot bottom plate and burst into puffs of steam.",
      "a plain flat white background with a simple table line",
      "the water drops turning into steam on the hot plate",
      "any letters",
      colour=C_STEAM),
 shot(24, "The steam puffs out of little holes, and softens the creases.",
      f"{YOU} slides {IRON} over the shirt on the ironing board; puffs of steam come out of the little holes under "
      "it; behind the iron the shirt is smooth, ahead of it still creased.",
      ROOM_NOW,
      "steam puffing out under the iron and the creases going smooth",
      "any letters or logos",
      colour=C_STEAM),
 shot(25, "Back then, a stove full of hot iron lumps.",
      f"The whole stovetop is covered with {SAD_IRONS}, all heating, heat lines everywhere; {WOMAN} wipes her "
      "forehead beside it.",
      KITCHEN,
      "the stove crowded with hot sad irons",
      "any modern thing",
      colour=C_ALL),
 shot(26, "Now? One plug.",
      f"{YOU} holds up a perfectly smooth shirt on a hanger with one hand, giving a thumbs up with the other; the "
      "iron stands on the board, its plug in the wall socket.",
      ROOM_NOW,
      "the smooth shirt and the iron plugged into one socket",
      "any letters or logos, any stove",
      colour=C_DONE),
]

lines = short_lines((HERE / "script.md").read_text(encoding="utf-8"))
assert len(S) == M and [(i, t) for i, t, _, _ in lines] == [(n, t) for n, t, _ in S], "scenes.py and script.md differ"
p = HERE / "script.json"
if not p.exists():
    print(approve(HERE.name)["message"])            # no approval step (Justin, 2026-10-19)
data = json.load(open(p, encoding="utf-8"))
segs = data["segments"]
assert len(segs) == M
for seg, (n, text, scene) in zip(segs, S):
    assert seg["id"] == n and seg["text"] == text, (n, seg["text"], text)
    seg["scene"] = scene
    seg["prompt"] = short_prompt(scene, STYLE, SETTINGS["colour_subject"], "paper_ref" in SETTINGS)
json.dump(data, open(p, "w", encoding="utf-8"), indent=1, ensure_ascii=False)
print("written", len(segs), "longest", max(len(s["prompt"]) for s in segs), "shortest", min(len(s["prompt"]) for s in segs))
