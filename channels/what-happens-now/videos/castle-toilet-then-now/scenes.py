"""Image prompts for castle-toilet-then-now, written as one story (channels/SHORTS_RULES.md "How image prompts are
written"; worked example: ../tooth-key-then-now/scenes.py). Checks every line against script.md; this file approves the
script (no approval step) and writes scene + full prompt for every line into script.json.
usage: python channels/what-happens-now/videos/castle-toilet-then-now/scenes.py"""
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
# back then (the Middle Ages)
CASTLE = ("a medieval stone castle: tall stone walls with square battlements along the top, two round towers, a "
          "wooden drawbridge, and a wide moat of water all around it, green hills behind")
GARDEROBE = ("a garderobe (a small square stone box room that sticks out from high up on the outside of the castle "
             "wall, held up by a row of stone brackets underneath, with one tiny window slit)")
GARDEROBE_IN = ("the inside of a garderobe: a tiny stone room, a smooth stone bench along the back wall with one round "
                "hole in the middle of it, one narrow window slit letting in light, a small wooden door")
KNIGHT = ("a castle lord (a stick-figure man in a long belted tunic down to his knees, hose, pointed shoes and a small "
          "round cap), fully dressed")
SHAFT = "a long narrow stone shaft running down inside the castle wall"
HALL = ("the great hall of the castle: a long wooden table with benches, a big stone fireplace, banners on the walls "
        "(no letters or symbols on them), torches")
TOWN = ("a medieval town at night: narrow crooked timber-framed houses leaning over a muddy lane, a stone church "
        "tower with a big round clock, and a dark sky with stars")
YARD = ("the small muddy backyard of a medieval town house: a wooden fence, a woodpile, and a privy (a small narrow "
        "wooden shed with a plank seat inside)")
PIT = "a deep square pit lined with stones, dug under the privy"
MUCK = "dark muck (drawn only as a thick dark muddy scribble, nothing recognisable in it)"
GONG = ("the gong farmer (a stick-figure man in a rough patched tunic, tall leather boots, a cloth tied over his nose "
        "and mouth, and a wide-brimmed floppy hat)")
BOYS = "two boys (small stick figures in rough tunics and caps)"
BUCKET = "a wooden bucket on a rope"
LANTERN = "an iron lantern with a candle inside"
CART = "a horse-drawn cart loaded with closed wooden barrels"
GATE = "a stone town gate with a pointed arch and a raised iron gate"
FIELD = ("a farm field outside a medieval town at dawn: ploughed rows of earth, a wooden fence, the town walls far "
         "behind, a rising sun")
FARMER = "a medieval farmer (a stick-figure man in a plain tunic and a straw hat) with a wooden shovel"
# now
YOU = "a stick-figure young man (short spiky hair, plain T-shirt and jeans)"
TOILET = ("a modern white toilet (a bowl with a seat and lid, and a tank on the back with a flush handle on its side)")
BATHROOM = ("a modern bathroom: tiled walls, a white toilet, a sink with a mirror, a towel on a rail")
CUTAWAY = ("a cut-away side view of a modern white toilet, as if sliced in half: the tank on the back full of water, "
           "the bowl, and the bent pipe under the bowl curving up and then down into the floor")
STREET_NOW = ("a cut-away view of a modern street: a house above ground on one side, the road and pavement, and below "
              "the ground the soil cut away to show pipes")
SEWER = "a big round concrete sewer pipe running under the street"
PLANT = ("a wastewater treatment plant: big round open concrete tanks, walkways with railings, pipes, a small control "
         "building, green grass around, and a river running past")
SCREEN = "a tall metal screen of upright bars set across a concrete channel of flowing water"
TANK = "a big round open concrete tank of water"
RIVER = "a clear river with grassy banks, reeds and a few trees"
# ---- the one coloured thing per picture (settings.json "colour_subject") ----
C_MOAT = "the moat's water: flat blue"
C_GARDEROBE = "the garderobe's stone box: flat warm sandy beige"
C_DROP = "the water of the moat far below: flat blue"
C_SEAT = "the stone seat: flat warm sandy beige"
C_ARROW = "the long arrow down the shaft: flat bright red"
C_SPLASH = "the moat water and the splash: flat blue"
C_PIT_STONE = "the stone pit: flat warm sandy beige"
C_SMELL = "the smell lines: flat pale green"
C_PRIVY = "the privy shed: flat warm brown wood"
C_MUCK = "the dark muck: flat dark brown"
C_GONG = "the gong farmer's tunic: flat dull green"
C_LANTERN = "the lantern's light: flat warm yellow glow"
C_CLOCKS = "the two clock faces: flat pale yellow, with flat black hands"
C_LADDER = "the wooden ladder: flat warm brown"
C_BUCKET = "the wooden bucket: flat warm brown"
C_CART = "the cart's barrels: flat warm brown"
C_SUN = "the rising sun: flat orange, and the ploughed field flat dark brown"
C_HANDLE = "the flush handle: flat shiny silver grey"
C_WATER = "the rushing water: flat bright blue"
C_PIPE = "the bent pipe: flat light grey"
C_SEAL = "the water sitting in the bend of the pipe: flat bright blue"
C_SEWER = "the big sewer pipe: flat grey"
C_PLANT = "the round treatment tanks: flat light blue water"
C_TRASH = "the caught trash on the screen: flat pink and flat yellow scraps"
C_SLUDGE = "the sludge settling at the bottom of the tank: flat dark brown"
C_BACTERIA = "the little bacteria: flat bright green"
C_RIVER = "the clean water and the river: flat bright blue"
C_SPLIT = "on the left the garderobe's stone box flat warm sandy beige, and on the right the bucket flat warm brown"
C_YOU = "the young man's clothes: his T-shirt flat green, his jeans flat blue"
CAPTIONS = ("The place fills the whole frame; keep the very top and very bottom of the frame calm (sky, wall or floor) "
            "for captions. Never write any name, label or caption under or beside anyone or anything.")
POLITE = "any bare skin, any recognisable waste, anyone undressed"

M = 33


def shot(n, text, what, place, must, never="", colour=""):
    what = re.sub(r"(^|\. )([a-z])", lambda m: m[1] + m[2].upper(), what)   # blocks start lowercase
    return n, text, " ".join(x for x in (
        f"This is picture {n} of {M} in one continuous picture story; draw exactly this moment.",
        what, f"Place: {place}.",
        f"The one coloured thing in this picture is {colour}; every other person, object and the whole place are black "
        "ink lines only, no colour.",
        f"It MUST show: {must}.", f"NEVER: {never}." if never else "", CAPTIONS) if x)


S = [
 shot(1, "In a medieval castle,",
      "Wide view of the castle standing on its hill, its moat all around it.",
      CASTLE,
      "the medieval stone castle with its moat",
      "any modern thing, any flags with letters",
      colour=C_MOAT),
 shot(2, "the toilet was a little stone room sticking out of the wall.",
      f"Closer view of one high castle wall: {GARDEROBE}, jutting out over the moat far below.",
      CASTLE,
      "the little stone room sticking out from high up on the castle wall",
      POLITE + ", a balcony with people",
      colour=C_GARDEROBE),
 shot(3, "And under the seat? A long drop.",
      "View looking straight down through the round hole of a stone seat: a long narrow stone shaft drops away far "
      "below, and at its very bottom a small circle of moat water; a dizzy dotted line runs down the drop.",
      "looking down through the seat hole of a garderobe; the long drop fills the frame",
      "how long the drop is from the seat to the water far below",
      POLITE,
      colour=C_DROP),
 shot(4, "It was called a garderobe.",
      f"{GARDEROBE}, seen from outside and slightly below, high on the castle wall above the moat; birds fly past.",
      CASTLE,
      "the garderobe on its stone brackets high on the castle wall",
      POLITE + ", any letters",
      colour=C_GARDEROBE),
 shot(5, "You sat on a stone seat with a hole in it.",
      f"{KNIGHT} sits on the stone bench, his long tunic covering him, looking out of the narrow window slit, "
      "bored.",
      GARDEROBE_IN,
      "the lord sitting fully dressed on the stone seat with a hole in it",
      POLITE,
      colour=C_SEAT),
 shot(6, "Everything fell down a shaft in the wall.",
      f"Cut-away view of the castle wall, as if sliced open: the garderobe at the top, and {SHAFT} going all the way "
      "down from the seat hole; a long arrow points down the shaft.",
      CASTLE,
      "the shaft inside the wall leading down from the seat",
      POLITE,
      colour=C_ARROW),
 shot(7, "It landed in the moat,",
      "The bottom end of the shaft opens in the castle wall just above the moat; a splash rises from the water "
      "below it, and two ducks paddle quickly away, looking back in disgust.",
      CASTLE,
      "the splash in the moat at the bottom of the shaft",
      POLITE,
      colour=C_SPLASH),
 shot(8, "or in a pit at the bottom.",
      "A different castle wall with no moat: the shaft from the garderobe runs down the wall and ends in a deep "
      "square stone-lined pit dug into the ground at the foot of the wall.",
      "the foot of a medieval castle wall with no moat: grass, a few bushes, a stone path",
      "the shaft ending in a stone pit at the bottom of the wall",
      POLITE,
      colour=C_PIT_STONE),
 shot(9, "The room hung on the outside of the castle,",
      f"Cut-away view of the castle: on the inside, {HALL}; on the far outer wall, {GARDEROBE}, as far away from the "
      "hall as it can be; a long double arrow shows the distance between them.",
      CASTLE,
      "the garderobe hanging on the outside wall, far from the hall",
      POLITE,
      colour=C_GARDEROBE),
 shot(10, "to keep the smell away from everyone.",
      f"Wavy smell lines float out of the garderobe's window slit into the open air outside; inside the castle, "
      f"in {HALL}, stick-figure people eat at the long table smiling, not bothered.",
      CASTLE,
      "the smell drifting away outside while the people inside are fine",
      POLITE,
      colour=C_SMELL),
 shot(11, "In towns, people used a privy over a deep pit.",
      f"The privy shed in the backyard, drawn as a cut-away so you can see underneath it: {PIT}.",
      YARD + ", in daylight",
      "the privy shed with the deep pit dug under it",
      POLITE,
      colour=C_PRIVY),
 shot(12, "Every couple of years, that pit was full.",
      f"The same kind of cut-away view of the privy: {PIT}, now filled right up to the top with {MUCK}; flies buzz "
      "above it.",
      YARD + ", in daylight",
      "the pit under the privy filled to the top",
      POLITE,
      colour=C_MUCK),
 shot(13, "So a gong farmer came to dig it out.",
      f"{GONG} walks into the backyard carrying a long wooden shovel over his shoulder and two empty wooden buckets, "
      f"followed by {BOYS}.",
      YARD + ", at night",
      "the gong farmer arriving with his shovel and buckets",
      POLITE,
      colour=C_GONG),
 shot(14, "He could only work at night,",
      f"Wide view of the sleeping town at night, every window dark; in one backyard, {GONG} works by the light of "
      f"{LANTERN} hung on the fence.",
      TOWN,
      "the gong farmer working by lantern light while the town sleeps",
      POLITE,
      colour=C_LANTERN),
 shot(15, "between nine and five.",
      "Two big round clock faces side by side, with no numbers on them: the left clock's hands point to nine "
      "o'clock, with a crescent moon and stars above it; the right clock's hands point to five o'clock, with a "
      "small rising sun above it; a curved arrow goes from the left clock to the right clock.",
      "a plain dark night sky behind the left clock fading to a pale dawn sky behind the right clock",
      "the night hours from nine to five shown on two clocks",
      "any numbers or letters on the clocks",
      colour=C_CLOCKS),
 shot(16, "He climbed down into the pit,",
      f"Cut-away view of the privy pit: {GONG} climbs down a wooden ladder into {PIT}, holding {LANTERN}.",
      YARD + ", at night",
      "the gong farmer climbing down the ladder into the pit",
      POLITE,
      colour=C_LADDER),
 shot(17, "sometimes up to his waist.",
      f"Cut-away view of the privy pit: {GONG} stands inside {PIT} in {MUCK} up to his waist, shovelling, his eyes "
      "screwed up.",
      YARD + ", at night",
      "the gong farmer standing in the muck up to his waist",
      POLITE,
      colour=C_MUCK),
 shot(18, "Boys hauled up the full buckets.",
      f"At the top of the pit, {BOYS} pull hard on the rope of {BUCKET}, full to the brim, lifting it up out of the "
      "pit, leaning back.",
      YARD + ", at night",
      "the two boys hauling a full bucket up out of the pit",
      POLITE,
      colour=C_BUCKET),
 shot(19, "Then he carted it all out of town,",
      f"{GONG} leads {CART} out through {GATE} at night, under the stars.",
      TOWN,
      "the cart of barrels leaving through the town gate",
      POLITE,
      colour=C_CART),
 shot(20, "to be spread on the fields.",
      f"{FARMER} spreads dark muck from a barrel onto the ploughed rows with his wooden shovel; the empty cart stands "
      "nearby.",
      FIELD,
      "the farmer spreading it on the field as fertiliser",
      POLITE,
      colour=C_SUN),
 shot(21, "Today, you just push a handle.",
      f"{YOU} stands beside {TOILET} with its lid down, pressing the flush handle with one finger, relaxed.",
      BATHROOM,
      "the young man pushing the flush handle",
      POLITE,
      colour=C_HANDLE),
 shot(22, "Water from the tank rushes into the bowl.",
      f"{CUTAWAY}: water gushes down out of the tank and swirls into the bowl, with fast flow arrows.",
      BATHROOM,
      "the water rushing from the tank into the bowl",
      POLITE,
      colour=C_WATER),
 shot(23, "It pulls everything down a bent pipe.",
      f"{CUTAWAY}: the water swirls out of the bowl, over the bend and down into the floor pipe, with arrows "
      "following the bend.",
      BATHROOM,
      "the water being pulled down through the bent pipe",
      POLITE,
      colour=C_PIPE),
 shot(24, "Some water always stays in that bend,",
      f"{CUTAWAY}: after the flush, a small pool of clean water sits in the low part of the bend, filling it.",
      BATHROOM,
      "the water staying in the low part of the bend",
      POLITE,
      colour=C_SEAL),
 shot(25, "to block the smell.",
      f"{CUTAWAY}: wavy smell lines rise from the floor pipe below but stop at the water sitting in the bend, with a "
      "small stop bar drawn across them; the bathroom above is fresh.",
      BATHROOM,
      "the water in the bend blocking the smell from coming up",
      POLITE,
      colour=C_SEAL),
 shot(26, "The pipe joins a big sewer under the street.",
      f"A small pipe runs from the house under the pavement and joins {SEWER}, with an arrow showing the flow.",
      STREET_NOW,
      "the house pipe joining the big sewer under the street",
      POLITE + ", any letters",
      colour=C_SEWER),
 shot(27, "It flows to a treatment plant.",
      f"The big sewer pipe comes out of the ground and leads into the treatment plant; arrows show the water "
      "flowing in.",
      PLANT,
      "the sewer leading to the treatment plant with its round tanks",
      "any letters or signs",
      colour=C_PLANT),
 shot(28, "Screens catch the trash.",
      f"{SCREEN}: water flows through the bars, and scraps of trash (wipes, plastic bits, rags) are caught against "
      "them; a worker in a hard hat rakes them off.",
      PLANT,
      "the metal screen catching the trash",
      POLITE + ", any letters",
      colour=C_TRASH),
 shot(29, "The heavy stuff sinks to the bottom of big tanks.",
      f"Cut-away side view of {TANK}: dark sludge sinks slowly to the bottom in small falling specks, with downward "
      "arrows, while the water above clears.",
      PLANT,
      "the heavy sludge sinking to the bottom of the tank",
      POLITE,
      colour=C_SLUDGE),
 shot(30, "Tiny bacteria eat up the rest.",
      "A close view as if through a magnifying glass: little round bacteria with tiny smiling mouths munch on small "
      "specks floating in the water, with air bubbles rising around them.",
      "inside a treatment tank, seen through a big round magnifying lens; the lens fills the frame",
      "the tiny bacteria eating the specks in the water",
      "any scary monster faces, any letters",
      colour=C_BACTERIA),
 shot(31, "The clean water goes back into the river.",
      f"Clean water pours from a wide outlet pipe into the river; a fish jumps happily nearby.",
      RIVER + ", with the edge of the treatment plant behind",
      "clean water pouring back into the river",
      "any letters, any dirty water",
      colour=C_RIVER),
 shot(32, "Back then, a long drop and a man with a bucket.",
      f"The picture is split down the middle by a simple vertical line. Left half: {GARDEROBE}, high on the castle "
      f"wall over the moat. Right half: {GONG} by lantern light, holding up a full wooden bucket at the edge of the "
      "pit.",
      f"left half: {CASTLE}; right half: {YARD}, at night",
      "the castle garderobe on the left and the gong farmer with his bucket on the right",
      POLITE,
      colour=C_SPLIT),
 shot(33, "Now? One push, and it's gone.",
      f"{YOU} pushes the flush handle of {TOILET} with one finger and is already turning to walk away, giving a "
      "thumbs up, a small swirl line by the toilet.",
      BATHROOM,
      "the young man flushing with one push and walking away happy",
      POLITE,
      colour=C_YOU),
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
