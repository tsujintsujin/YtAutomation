"""Image prompts for icebox-iceman-then-now, written as one story (channels/SHORTS_RULES.md "How image prompts are
written"; worked example: ../tooth-key-then-now/scenes.py). Checks every line against script.md; this file approves the
script (no approval step) and writes scene + full prompt for every line into script.json.
usage: python channels/what-happens-now/videos/icebox-iceman-then-now/scenes.py"""
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
# back then (nineteen ten)
ICEBOX = ("an icebox (a waist-high wooden cabinet on short legs, made of dark wood with panelled doors: one small "
          "door at the top for the ice and two doors below for the food, each with a shiny metal latch)")
ICEMAN = ("the iceman (a strong stick-figure man in a flat cap, a heavy work shirt with rolled sleeves, braces, and a "
          "thick leather pad over one shoulder)")
WOMAN = ("a stick-figure woman from nineteen ten (hair pinned up in a bun, a long plain skirt to her ankles, a blouse "
         "with puffed sleeves and an apron)")
BLOCK = "a big square block of ice (drawn as a plain outlined cube with a few short shine lines on its faces)"
TONGS = "big iron ice tongs (like giant scissors with two curved, pointed hooks at the ends)"
PICK = "an ice pick (a short wooden handle with one long thin pointed metal spike)"
CARD = ("a square cardboard ice card in the window with the number 50 printed big in the middle and nothing else on it")
WAGON = ("a horse-drawn ice wagon (a big work horse pulling a boxy wooden wagon with a closed top, a back door, and a "
         "driver's bench)")
PAN = "a flat round metal drip pan"
STREET = ("a city street in nineteen ten: a row of tall narrow brick houses with front steps and big front windows, a "
          "cobblestone road, an old gas street lamp, a few people in long coats and hats")
STAIRS = ("the narrow wooden stairs inside an old brick house in nineteen ten: a wooden banister, striped wallpaper, "
          "a small window on the landing")
KITCHEN_OLD = ("a kitchen in nineteen ten: a black iron cooking stove, a deep stone sink with a single tap, wooden "
               "shelves of jars, a small wooden table, a window with lace curtains, wooden floorboards")
FOOD_OLD = "a glass bottle of milk, a wrapped piece of meat and a dish of butter"
# now
FRIDGE = ("a modern fridge (a tall smooth white upright fridge with one long door and a plain handle)")
KITCHEN_NEW = ("a modern kitchen: smooth counters, a sink under a window, cupboards above, a tiled floor, and a wall "
               "socket near the floor")
PIPES = "thin pipes that wind back and forth through the walls of the fridge"
COMPRESSOR = "a compressor (a small round black metal pump, like a fat can, at the bottom back of the fridge)"
COILS = "a grid of thin zigzag pipes (the coils) on the back of the fridge"
YOU = "a stick-figure young man (short spiky hair, plain T-shirt and jeans)"
FOOD_NEW = "a carton of milk, a tray of eggs, a bowl of fruit and a plate of leftovers"
# ---- the one coloured thing per picture (settings.json "colour_subject") ----
C_WAGON = "the ice wagon: flat bright yellow, with flat red wheels"
C_ICEBOX = "the icebox: flat warm brown wood, with flat gold latches"
C_ICE = "the ice: flat pale icy blue"
C_WALL = "the hollow gap inside the icebox wall: flat light tan"
C_CORK = "the cork chips and sawdust packed in the wall: flat light tan"
C_LINING = "the metal lining inside the icebox: flat shiny silver grey"
C_COLD = "the cold air arrows: flat pale icy blue"
C_DRIPS = "the ice and its falling drips: flat pale icy blue"
C_CARD = "the ice card: flat bright red with the number 50 in flat white"
C_SCALES = "the ice card flat bright red with the number 50 in flat white, and the ice block flat pale icy blue"
C_PICK = "the ice pick: its spike flat steel grey, its handle flat warm brown"
C_TONGS = "the ice tongs: flat dark iron grey"
C_PAD = "the iceman's leather shoulder pad: flat brown"
C_PAN = "the drip pan: flat shiny silver grey, and the water in it flat light blue"
C_WOMAN = "the full drip pan's water: flat light blue"
C_FRIDGE = "the modern fridge: flat light grey"
C_PIPES = "the hidden pipes: flat copper orange"
C_LIQUID = "the special liquid in the pipe: flat light green"
C_GAS = "the bubbles of gas in the pipe: flat light green"
C_HEAT = "the wavy heat lines leaving the food: flat orange"
C_COMPRESSOR = "the compressor pump: flat dark blue"
C_COILS = "the heat lines coming off the coils: flat orange"
C_LOOP = "the loop of arrows through the pipes: flat light green"
C_MOON = "the moon in the window flat pale yellow, and the fridge's small light flat soft blue"
C_PLUG = "the plug and its cord: flat black, with a small flat yellow spark of power at the socket"
C_SHOULDER = "the ice block on his shoulder: flat pale icy blue"
CAPTIONS = ("The place fills the whole frame; keep the very top and very bottom of the frame calm (sky, wall or floor) "
            "for captions. Never write any name, label or caption under or beside anyone or anything.")

M = 34


def shot(n, text, what, place, must, never="", colour=""):
    what = re.sub(r"(^|\. )([a-z])", lambda m: m[1] + m[2].upper(), what)   # blocks start lowercase
    return n, text, " ".join(x for x in (
        f"This is picture {n} of {M} in one continuous picture story; draw exactly this moment.",
        what, f"Place: {place}.",
        f"The one coloured thing in this picture is {colour}; every other person, object and the whole place are black "
        "ink lines only, no colour.",
        f"It MUST show: {must}.", f"NEVER: {never}." if never else "", CAPTIONS) if x)


S = [
 shot(1, "In nineteen ten,",
      f"Wide view of the street: {WAGON} rolls along the cobblestones past the row of brick houses.",
      STREET,
      "the old city street of nineteen ten with the horse-drawn ice wagon",
      "cars, any modern thing, any letters on the wagon",
      colour=C_WAGON),
 shot(2, "your fridge was a wooden box.",
      f"{ICEBOX} stands against the kitchen wall, its doors shut.",
      KITCHEN_OLD,
      "the wooden icebox standing in the old kitchen where a fridge would be",
      "a modern fridge, any electric cord",
      colour=C_ICEBOX),
 shot(3, "And a man carried ice up your stairs to fill it.",
      f"{ICEMAN} climbs the narrow stairs with {BLOCK} balanced on the leather pad on his shoulder, gripping it with "
      f"{TONGS}, water drips falling from the ice.",
      STAIRS,
      "the iceman carrying a block of ice up the stairs on his shoulder",
      "a lift, a trolley, any letters",
      colour=C_SHOULDER),
 shot(4, "It was called an icebox.",
      f"Close view of {ICEBOX}, standing on the wooden floorboards, a small shine on each metal latch.",
      KITCHEN_OLD,
      "the wooden icebox with its small top door and two lower doors",
      "any letters or labels, an electric cord",
      colour=C_ICEBOX),
 shot(5, "Its walls were hollow,",
      f"Cut-away view of {ICEBOX}, as if one corner of it were sliced off: its wooden wall is made of an outer wooden "
      "panel and an inner panel with an empty hollow gap between them, a small arrow pointing into the gap.",
      KITCHEN_OLD,
      "the hollow gap inside the icebox's wall",
      "any people, any letters",
      colour=C_WALL),
 shot(6, "and stuffed with cork or sawdust.",
      "The same kind of cut-away view of the icebox's wall: the hollow gap between the outer and inner wooden "
      "panels is now packed full of little lumpy cork chips and fine sawdust flecks.",
      KITCHEN_OLD,
      "the cork and sawdust packed inside the icebox wall",
      "any people, any letters",
      colour=C_CORK),
 shot(7, "Inside, they were lined with metal.",
      f"{ICEBOX} with all its doors open: every inside wall of it is lined with smooth shiny metal sheets, with small "
      "shine marks.",
      KITCHEN_OLD,
      "the shiny metal lining inside the open icebox",
      "any food yet, any letters",
      colour=C_LINING),
 shot(8, "A big block of ice sat in the top.",
      f"{ICEBOX} with its small top door open: {BLOCK} sits on a metal rack in the top compartment; the lower doors "
      "are shut.",
      KITCHEN_OLD,
      "the block of ice sitting in the top of the icebox",
      "ice cubes, an ice tray",
      colour=C_ICE),
 shot(9, "Cold air sank down over the food below.",
      f"Cut-away view of {ICEBOX} with its front off: {BLOCK} in the top compartment, and below it on the shelves "
      f"{FOOD_OLD}; wavy downward arrows of cold air flow from the ice down over the food.",
      KITCHEN_OLD,
      "cold air sinking from the ice down onto the food",
      "any letters or labels on the food",
      colour=C_COLD),
 shot(10, "But the ice melted every day.",
      f"Close view of the top compartment of {ICEBOX}: the block of ice has shrunk to a small rounded lump, with drops "
      "of water dripping off it; a faint dotted outline shows how big it was before.",
      KITCHEN_OLD,
      "the ice block shrinking and dripping as it melts",
      "any people",
      colour=C_DRIPS),
 shot(11, "So you put a card in your window.",
      f"{WOMAN} props {CARD} up against the inside of her big front window, facing out to the street.",
      "inside the front room of a brick house in nineteen ten: a big window looking out onto a cobblestone street, "
      "lace curtains, a small table",
      "the woman putting the ice card in her window",
      "any other letters or words on the card",
      colour=C_CARD),
 shot(12, "The number on it told the iceman",
      f"Seen from the street: {ICEMAN} stands on the pavement looking up at the house's front window, where {CARD} "
      "faces out; he nods.",
      STREET,
      "the iceman reading the ice card in the window from the street",
      "any other letters or words",
      colour=C_CARD),
 shot(13, "how many pounds you wanted.",
      f"Close view: on the left, {CARD}; on the right, {BLOCK} sitting on a simple hanging scale with a hook and a "
      "flat tray, its pointer at the middle.",
      "the back of an ice wagon in nineteen ten: wooden boards, sawdust on the floor; the close view fills the frame",
      "the number on the card matched to a block of ice on the scale",
      "any other numbers or letters",
      colour=C_SCALES),
 shot(14, "His horse and wagon stopped outside.",
      f"{WAGON} stands still at the kerb in front of the brick house; the horse rests, and {ICEMAN} hops down from "
      "the driver's bench.",
      STREET,
      "the ice wagon stopped outside the house",
      "a truck, a car, any letters on the wagon",
      colour=C_WAGON),
 shot(15, "He chipped a block to size with his pick.",
      f"{ICEMAN} stands at the open back door of the wagon and chips {BLOCK} with {PICK}, small chips of ice flying.",
      STREET,
      "the iceman chipping a block of ice with the ice pick",
      "a saw, a machine",
      colour=C_PICK),
 shot(16, "He grabbed it with big iron tongs",
      f"{ICEMAN} grips {BLOCK} with {TONGS}, the two hooks biting into its sides, and lifts it out of the back of "
      "the wagon.",
      STREET,
      "the iron tongs gripping the ice block",
      "bare hands holding the ice, a forklift",
      colour=C_TONGS),
 shot(17, "and swung it up onto his shoulder.",
      f"{ICEMAN} swings {BLOCK} up with {TONGS} and sets it down on the thick leather pad over his shoulder, bending "
      "his knees, a curved swing arrow.",
      STREET,
      "the block of ice landing on the leather pad on his shoulder",
      "a trolley, a box",
      colour=C_PAD),
 shot(18, "He carried it up to your kitchen",
      f"{ICEMAN} climbs the narrow stairs with {BLOCK} on the leather pad on his shoulder, water drips falling on the "
      "steps behind him.",
      STAIRS,
      "the iceman climbing the stairs with the ice on his shoulder",
      "a lift, a trolley",
      colour=C_SHOULDER),
 shot(19, "and dropped it into the icebox.",
      f"In the kitchen, {ICEMAN} lowers {BLOCK} with {TONGS} into the open top compartment of {ICEBOX}.",
      KITCHEN_OLD,
      "the iceman putting the block into the top of the icebox",
      "a modern fridge",
      colour=C_ICE),
 shot(20, "Under the box sat a pan.",
      f"Low close view of the bottom of {ICEBOX} on its short legs: {PAN} sits on the floorboards underneath it, and "
      "a small pipe from the icebox's bottom ends just above the pan.",
      KITCHEN_OLD,
      "the drip pan sitting under the icebox",
      "any people",
      colour=C_PAN),
 shot(21, "It slowly filled with melted ice.",
      f"Low close view under {ICEBOX}: water drops fall from the small pipe into {PAN}, which is now nearly full, the "
      "water almost at the rim with small ripples.",
      KITCHEN_OLD,
      "the drip pan filling up with melted ice water",
      "any people",
      colour=C_PAN),
 shot(22, "And you had to empty it every single day.",
      f"{WOMAN} carries {PAN}, full to the brim with water, carefully across the kitchen to the deep stone sink, "
      "a little water sloshing over the edge, her face tired.",
      KITCHEN_OLD,
      "the woman carrying the full drip pan to the sink to empty it",
      "any modern thing",
      colour=C_WOMAN),
 shot(23, "Today, your fridge makes its own cold.",
      f"{FRIDGE} stands in the modern kitchen, a few short cold lines around it.",
      KITCHEN_NEW,
      "the modern fridge in the modern kitchen",
      "any ice block, any letters or logo on the fridge",
      colour=C_FRIDGE),
 shot(24, "Hidden pipes run through its walls,",
      f"Cut-away view of {FRIDGE}, as if its side were see-through: {PIPES}, all through the back and the side walls.",
      KITCHEN_NEW,
      "the hidden pipes winding through the fridge's walls",
      "any ice block, any letters",
      colour=C_PIPES),
 shot(25, "filled with a special liquid.",
      "Close cut-away view of one of the thin pipes inside the fridge wall: a special liquid flows along inside it, "
      "with small arrows showing the flow.",
      "inside the wall of a modern fridge; the close view of the pipe fills the frame",
      "the special liquid flowing inside the pipe",
      "any letters or labels",
      colour=C_LIQUID),
 shot(26, "Inside, the liquid turns into a gas",
      f"Cut-away view of the open {FRIDGE} with {FOOD_NEW} on its shelves: in the thin pipes behind the back wall, the "
      "liquid bubbles up into round gas bubbles.",
      KITCHEN_NEW,
      "the liquid in the pipe inside the fridge turning into bubbles of gas",
      "any ice, any letters",
      colour=C_GAS),
 shot(27, "and soaks up the heat from your food.",
      f"Cut-away view of the open {FRIDGE}: wavy heat lines rise off {FOOD_NEW} and flow into the thin pipes at the "
      "back wall, while the food gets small frost marks.",
      KITCHEN_NEW,
      "the heat leaving the food and going into the pipes",
      "any letters",
      colour=C_HEAT),
 shot(28, "A pump at the bottom, called a compressor,",
      f"Cut-away view of the bottom back corner of {FRIDGE}: {COMPRESSOR}, with the thin pipes going into and out "
      "of it.",
      KITCHEN_NEW,
      "the compressor pump at the bottom back of the fridge",
      "any letters or labels",
      colour=C_COMPRESSOR),
 shot(29, "squeezes that gas.",
      f"Close cut-away view of {COMPRESSOR}: inside it, a round piston pushes and squeezes a cloud of gas bubbles "
      "into a tight bunch, with squeeze lines around the pump.",
      "inside the bottom of a modern fridge; the close view fills the frame",
      "the compressor squeezing the gas",
      "any letters",
      colour=C_COMPRESSOR),
 shot(30, "Coils on the back let the heat out into your kitchen.",
      f"The back of {FRIDGE}, pulled out a little from the kitchen wall: {COILS}, with wavy heat lines rising off "
      "them into the kitchen air.",
      KITCHEN_NEW,
      "the coils on the back of the fridge giving off heat",
      "any letters",
      colour=C_COILS),
 shot(31, "Then it goes round again,",
      f"Cut-away view of the whole {FRIDGE}: the thin pipes run from the compressor at the bottom, up the coils on the "
      "back, into the walls and back down, with arrows all along them in one big loop.",
      KITCHEN_NEW,
      "the loop of pipes with arrows going round and round",
      "any letters",
      colour=C_LOOP),
 shot(32, "all day and all night.",
      f"{FRIDGE} stands in the dark modern kitchen at night, a crescent moon and stars in the window, a small soft "
      "hum line beside the fridge.",
      KITCHEN_NEW + ", at night",
      "the fridge still working in the kitchen at night",
      "any people",
      colour=C_MOON),
 shot(33, "Back then, a block of ice and a man on your stairs.",
      f"{ICEMAN} climbs the narrow stairs with {BLOCK} on the leather pad on his shoulder, gripping it with {TONGS}, "
      "sweat drops on his face and water dripping from the ice.",
      STAIRS,
      "the iceman hauling a block of ice up the stairs",
      "any modern thing",
      colour=C_SHOULDER),
 shot(34, "Now? You just plug it in.",
      f"{YOU} kneels beside {FRIDGE} and pushes its plug into the wall socket, a big easy smile.",
      KITCHEN_NEW,
      "the young man plugging the fridge into the wall",
      "any ice, any iceman",
      colour=C_PLUG),
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
