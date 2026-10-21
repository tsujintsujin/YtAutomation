"""Image prompts for candle-tallow-then-now, written as one story (channels/SHORTS_RULES.md "How image prompts are
written"; worked example: ../tooth-key-then-now/scenes.py). Checks every line against script.md; this file approves the
script (no approval step) and writes scene + full prompt for every line into script.json.
usage: python channels/what-happens-now/videos/candle-tallow-then-now/scenes.py"""
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
# the seventeen hundreds
FARMHOUSE = ("a wooden farmhouse in the seventeen hundreds at night: a steep roof, a stone chimney, small square "
             "windows, a dark sky with stars, bare trees around it")
KITCHEN = ("a farmhouse kitchen in the seventeen hundreds: a big open stone hearth with a fire, a heavy iron hook "
           "holding a pot over it, a long wooden table, wooden beams, plank floor, a small window")
MAKER = ("a stick-figure woman from the seventeen hundreds (a long plain dress, an apron, a white cloth cap, her "
         "sleeves rolled up)")
POT = "a big black iron pot hanging over the fire"
TALLOW = "tallow (a lump of hard, waxy white animal fat)"
ROD = "a long wooden candle rod"
WICKS = "six cotton string wicks hanging down in a row from the rod"
RACK = "a simple wooden drying rack (two upright posts with crossbars) where rods of candles hang to cool"
SNUFFERS = ("snuffers (small metal scissors with a little box on one blade to catch the cut wick)")
TIN_BOX = "a tin candle box (a long round tin tube with a lid, hung on the wall)"
MAN1700 = ("a stick-figure man from the seventeen hundreds (a loose shirt, a waistcoat and knee breeches)")
SHOP = ("a candle maker's workshop in the seventeen hundreds: big pots of melted tallow on a fire, long wooden racks "
        "hung with rows and rows of candles, a stone floor")
# now
YOU = "a stick-figure young man (short spiky hair, plain T-shirt and jeans)"
ROOM_NOW = ("a modern living room: a sofa, a rug, a bookshelf, a window, a light switch on the wall by the door and a "
            "ceiling light with one bulb")
PLANT = ("a power plant: big buildings with two tall chimneys, and tall metal power towers carrying wires away across "
         "the fields")
BULB = ("a modern light bulb (a round bulb shape on a screw base), drawn as a cut-away so you can see inside: a tiny "
        "square chip on a small board in the middle")
SWITCH_CUT = ("a cut-away view of a light switch on a wall, as if see-through: two wires coming in, and a small metal "
              "bridge piece inside that the switch presses down")
# ---- the one coloured thing per picture (settings.json "colour_subject") ----
C_WINDOW = "the dim candle glow in the window: flat warm yellow"
C_TALLOW = "the melted tallow: flat creamy yellow"
C_LUMP = "the lump of tallow: flat creamy yellow-white"
C_FIRE = "the hearth fire: flat orange and yellow flames"
C_WICKS = "the string wicks: flat bright white"
C_COOL = "the coated candles: flat creamy yellow"
C_ARROWS = "the circular arrows: flat bright red"
C_LAYERS = "the thin layers in the candle: alternating flat creamy yellow and flat pale yellow"
C_CANDLES = "the fat finished candles: flat creamy yellow"
C_RACKS = "the rows of candles: flat creamy yellow"
C_SMELL = "the smell lines: flat greenish grey"
C_WICK = "the black curled wick flat black, and the flame flat orange"
C_SNUFFERS = "the snuffers: flat dark iron grey"
C_TIN = "the tin candle box: flat shiny silver grey"
C_MOUSE = "the mouse: flat grey with a flat pink nose and ears"
C_SWITCH = "the light switch: flat white with a flat yellow spark"
C_PLANT = "the power towers and wires: flat dark grey"
C_WIRES = "the wires inside the walls: flat copper orange"
C_GAP = "the small metal bridge piece closing the gap: flat copper orange"
C_POWER = "the arrow of power along the wire: flat bright yellow"
C_CHIP = "the tiny chip: flat dark blue"
C_BLUE = "the chip's glow: flat bright blue"
C_COATING = "the blue light flat bright blue, the coating flat yellow, and the white light coming out filled flat bright white"
C_HEAT = "the candle's flame and heat waves: flat orange; the bulb's soft glow flat pale yellow"
C_CALENDAR = "the flying calendar pages: flat cream with flat red tops"
C_SMOKE = "the smoky haze in the kitchen: flat grey"
C_BRIGHT = "the bright light from the ceiling bulb: flat warm yellow glow filling the room"
CAPTIONS = ("The place fills the whole frame; keep the very top and very bottom of the frame calm (sky, wall or floor) "
            "for captions. Never write any name, label or caption under or beside anyone or anything.")

M = 28


def shot(n, text, what, place, must, never="", colour=""):
    what = re.sub(r"(^|\. )([a-z])", lambda m: m[1] + m[2].upper(), what)   # blocks start lowercase
    return n, text, " ".join(x for x in (
        f"This is picture {n} of {M} in one continuous picture story; draw exactly this moment.",
        what, f"Place: {place}.",
        f"The one coloured thing in this picture is {colour}; every other person, object and the whole place are black "
        "ink lines only, no colour.",
        f"It MUST show: {must}.", f"NEVER: {never}." if never else "", CAPTIONS) if x)


S = [
 shot(1, "In the seventeen hundreds,",
      "Wide view of the dark farmhouse at night; one small window shows the dim glow of a single candle.",
      FARMHOUSE,
      "the dark farmhouse with one dim candle glowing in a window",
      "electric lights, any modern thing",
      colour=C_WINDOW),
 shot(2, "light at night came from a pot of melted animal fat.",
      f"{POT} over the hearth fire, full of melted tallow, a little steam curling up.",
      KITCHEN,
      "the pot of melted animal fat over the fire",
      "any people, any electric thing",
      colour=C_TALLOW),
 shot(3, "It was called tallow.",
      f"Close view of {TALLOW} on a wooden board on the table beside the pot.",
      KITCHEN + "; the close view of the table fills most of the frame",
      "the lump of hard white animal fat",
      "any letters or labels",
      colour=C_LUMP),
 shot(4, "You melted it in a big pot over the fire.",
      f"{MAKER} drops chunks of tallow into {POT} and stirs with a long wooden spoon; the fire blazes under it.",
      KITCHEN,
      "the woman melting the tallow in the pot over the fire",
      "a modern stove",
      colour=C_FIRE),
 shot(5, "You hung string wicks from a stick, a few in a row.",
      f"{MAKER} holds up {ROD} with {WICKS}, straightening one with her fingers.",
      KITCHEN,
      "the row of string wicks hanging from the wooden rod",
      "any candles yet",
      colour=C_WICKS),
 shot(6, "You dipped them into the hot fat.",
      f"{MAKER} lowers {ROD} so {WICKS} dip down into the melted tallow in {POT}.",
      KITCHEN,
      "the wicks being dipped into the hot fat",
      "any modern thing",
      colour=C_TALLOW),
 shot(7, "Then you let them cool.",
      f"{ROD} hangs across {RACK}; the six thinly coated wicks hang straight down, a few drips falling, small cool "
      "air lines around them.",
      KITCHEN,
      "the thinly coated wicks hanging to cool",
      "flames on them",
      colour=C_COOL),
 shot(8, "Then you dipped them again. And again.",
      f"{MAKER} dips the rod of coated wicks into {POT} once more; two circular arrows around her show it happening "
      "over and over, and she looks tired.",
      KITCHEN,
      "the woman dipping the candles again and again",
      "any modern thing",
      colour=C_ARROWS),
 shot(9, "Each dip added one thin layer,",
      "Cut-away close view of one dipped candle, as if sliced across: rings of thin layers around the string wick in "
      "the middle, like the rings of a tree.",
      KITCHEN + "; the close view of the candle fills most of the frame",
      "the thin layers built up by each dip",
      "any letters",
      colour=C_LAYERS),
 shot(10, "until the candles were fat enough.",
      f"{ROD} hangs on {RACK} with six full, fat, smooth candles hanging from it; {MAKER} nods, pleased.",
      KITCHEN,
      "the row of finished fat candles",
      "any flames",
      colour=C_CANDLES),
 shot(11, "A good candle maker could dip about two hundred in a day.",
      f"A candle maker (a stick-figure man in a leather apron and a cap) stands proudly among racks and racks of "
      "candles hanging in rows.",
      SHOP,
      "a huge number of candles made in one day",
      "any numbers or letters",
      colour=C_RACKS),
 shot(12, "But tallow candles smelled bad, and burned unevenly.",
      f"A lit tallow candle on the table drips lopsidedly down one side, and wavy smell lines rise from it; "
      f"{MAN1700} sits beside it pinching his nose.",
      KITCHEN + ", at night",
      "the smelly lopsided candle and the man pinching his nose",
      "any electric light",
      colour=C_SMELL),
 shot(13, "The wick turned black and curled over,",
      "Close view of a burning tallow candle: its long wick has turned black and curls over to one side, and melted "
      "tallow runs down that side.",
      KITCHEN + ", at night; the close view of the candle fills most of the frame",
      "the black wick curling over on the candle",
      "any people",
      colour=C_WICK),
 shot(14, "so you snipped it with scissors called snuffers.",
      f"A stick-figure hand snips the black curled wick with {SNUFFERS}; the flame stands up straight again.",
      KITCHEN + ", at night; the close view of the candle fills most of the frame",
      "the snuffers snipping off the black wick",
      "ordinary scissors with no box",
      colour=C_SNUFFERS),
 shot(15, "And you kept your candles in a tin box,",
      f"{MAKER} slides candles into {TIN_BOX} on the kitchen wall.",
      KITCHEN,
      "the candles going into the tin box on the wall",
      "any letters",
      colour=C_TIN),
 shot(16, "safe from rats and mice.",
      f"At night, a small mouse sits on the shelf below {TIN_BOX}, sniffing up at it, its little face disappointed; "
      "the lid is shut tight.",
      KITCHEN + ", at night",
      "the mouse unable to get at the candles in the closed tin box",
      "any people, a mouse eating anything",
      colour=C_MOUSE),
 shot(17, "Today, you flick a switch.",
      f"{YOU} walks into the dark living room and flicks the light switch by the door.",
      ROOM_NOW + ", dark at night",
      "the young man flicking the light switch",
      "any candle",
      colour=C_SWITCH),
 shot(18, "Electricity comes from a power plant,",
      f"Wide view of the {PLANT[2:]}, with small zigzag arrows running along the wires away from it.",
      "open fields at dusk around a power plant",
      "the power plant sending electricity out along the wires",
      "any letters or signs",
      colour=C_PLANT),
 shot(19, "along wires, into your walls.",
      "The power wires reach a small house on a street; the house is drawn as a cut-away so you can see thin wires "
      "running inside its walls to the rooms.",
      "a quiet street at night with a few houses and power poles",
      "the wires coming into the house and running inside its walls",
      "any letters",
      colour=C_WIRES),
 shot(20, "The switch closes a gap,",
      f"{SWITCH_CUT}: the switch is pressed, and the small metal bridge piece closes the gap between the two wires.",
      ROOM_NOW + "; the close view of the switch fills most of the frame",
      "the metal piece closing the gap inside the switch",
      "any letters",
      colour=C_GAP),
 shot(21, "and the power reaches the bulb.",
      "A thin wire runs from the switch up the wall and across the ceiling to the ceiling light; a bright arrow of "
      "power travels along the wire and reaches the bulb.",
      ROOM_NOW + ", dark at night",
      "the power travelling along the wire to the bulb",
      "any letters",
      colour=C_POWER),
 shot(22, "Inside the bulb is a tiny chip.",
      f"{BULB} drawn big, with a magnifying circle around the tiny square chip.",
      "a plain flat white background with a simple table line",
      "the tiny chip inside the bulb",
      "any letters or logos",
      colour=C_CHIP),
 shot(23, "Electricity pushes through it, and it glows blue.",
      "Close view of the tiny square chip on its small board: small arrows of electricity flow into it, and it "
      "glows with short bright rays.",
      "inside a modern light bulb; the close view of the chip fills most of the frame",
      "the chip glowing blue as electricity flows through it",
      "any letters",
      colour=C_BLUE),
 shot(24, "A yellow coating turns that blue into white light.",
      "Close cut-away of the chip under a thin curved coating layer: blue rays come up from the chip into the "
      "coating, and bright white rays shine out of the top of the coating.",
      "inside a modern light bulb; the close view fills most of the frame",
      "blue light going into the yellow coating and white light coming out",
      "any letters",
      colour=C_COATING),
 shot(25, "It barely gets warm.",
      "Side by side: on the left, a stick-figure hand held calmly near a glowing modern light bulb, no heat lines; on the "
      "right, a candle flame with big wavy heat lines rising, and a hand pulling back from it.",
      "a plain flat white background with a simple table line",
      "the bulb staying cool next to the hot candle",
      "any letters",
      colour=C_HEAT),
 shot(26, "And one bulb can last for years.",
      "The ceiling bulb glows steadily while calendar pages fly off a wall calendar beside it, one after another.",
      ROOM_NOW,
      "the bulb shining on while lots of time passes",
      "any numbers or letters on the calendar",
      colour=C_CALENDAR),
 shot(27, "Back then, dip after dip of smelly fat.",
      f"{MAKER} dips {ROD} into {POT} again in the smoky kitchen, wiping her forehead, a haze of smoke and smell "
      "lines in the air.",
      KITCHEN,
      "the woman dipping candles in the smelly, smoky kitchen",
      "any modern thing",
      colour=C_SMOKE),
 shot(28, "Now? Flick. Light.",
      f"{YOU} stands by the switch in the living room, now bright with light from the ceiling bulb, giving a "
      "thumbs up.",
      ROOM_NOW,
      "the room bright with light at the flick of the switch",
      "any candle",
      colour=C_BRIGHT),
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
