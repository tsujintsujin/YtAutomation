"""Image prompts for toiletpaper-sponge-then-now, written as one story (channels/SHORTS_RULES.md "How image prompts are
written"; worked example: ../tooth-key-then-now/scenes.py). Checks every line against script.md; this file approves the
script (no approval step) and writes scene + full prompt for every line into script.json.
usage: python channels/what-happens-now/videos/toiletpaper-sponge-then-now/scenes.py"""
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
# ancient Rome
SPONGE = ("a sponge on a stick (a long thin wooden stick with a round puffy sea sponge tied to one end)")
ROMAN = ("a Roman man (a stick figure in a plain knee-length tunic with a belt and simple sandals, short curly hair)")
ROMANS = ("a row of Roman men (stick figures in plain knee-length tunics with belts and simple sandals) sitting side "
          "by side, fully clothed, their tunics covering their laps")
LATRINE = ("an ancient Roman public toilet room: a long smooth stone bench running along the wall with round holes "
           "in it, stone columns, a small open water channel running along the floor in front of the bench, and an "
           "arched doorway")
BUCKET = "a wooden bucket of vinegar"
ROME_STREET = ("an ancient Roman street: stone paving, tall stone columns, a temple with a triangular roof, and a "
               "stone building with an arched doorway")
# later
VILLAGE = ("a small village in the Middle Ages: thatched-roof cottages, a muddy path, a few trees, and a small wooden "
           "outhouse (a tall narrow wooden shed with a door with a small crescent moon cut into it)")
VILLAGER = ("a villager from the Middle Ages (a stick-figure man in a plain belted tunic, hose and a hood)")
FARM = ("an American farm in the eighteen hundreds: a plain wooden barn, a split-rail fence, a field of tall "
        "corn plants, and a small wooden outhouse (a tall narrow wooden shed with a door with a small crescent moon "
        "cut into it)")
FARMER = ("a farmer from the eighteen hundreds (a stick-figure man in a wide-brimmed straw hat, a checked shirt and "
          "overalls)")
COB = "a dried corncob (a long bumpy cob with all its kernels gone, rough and dry)"
PRESS = ("an old printing press from the seventeen hundreds (a big wooden frame with a large screw and a long lever "
         "handle on top, a flat bed with a sheet of paper on it)")
PRINT_SHOP = ("an old print shop in the seventeen hundreds: wooden floor, stacks of printed paper on tables, sheets "
              "hanging up to dry on strings, a small window")
READER = ("a stick-figure man from the seventeen hundreds (a three-cornered hat, a long coat and knee breeches)")
NEWSPAPER = "an old folded newspaper (printed columns drawn as rows of small squiggly lines, no readable letters)"
SHOP_1850 = ("a small general store in the eighteen fifties: a long wooden counter, shelves of jars and boxes behind it, "
             "a big shop window, a wooden floor")
STREET_1850 = ("a city street in the eighteen fifties: brick shop fronts with big windows and awnings, a dirt road, a "
               "horse and carriage, gas street lamps")
SELLER = ("a shopkeeper from the eighteen fifties (a stick-figure man with neat side-whiskers, a waistcoat, a bow tie "
          "and an apron)")
CUSTOMER = ("a customer from the eighteen fifties (a stick-figure woman in a long full skirt, a shawl and a bonnet)")
PACK = ("a pack of flat sheets of paper (a neat stack of flat square sheets, tied with a paper band, no letters)")
OLD_ROLL = "a roll of toilet paper on a simple wooden wall holder in a plain old washroom"
# now
FOREST = "a pine forest: tall straight trees, stumps, a dirt logging track"
LUMBERJACK = "a forest worker (a stick-figure man in a hard hat, a hi-vis vest and work boots)"
MILL = ("the inside of a big modern paper mill: huge steel machines, long rollers, pipes, a high ceiling with bright "
        "lights, a clean concrete floor")
MILL_WORKER = "a mill worker (a stick-figure man in a hard hat, safety glasses, ear muffs and overalls)"
CHIPPER = "a big steel wood chipper with a wide mouth at the front and a chute at the side"
DIGESTER = "a giant round steel cooking tank (taller than a house) with a big open hatch on top"
SCREEN = "a long fast-moving mesh belt (a fine net like a long conveyor belt)"
DRUM = "a giant round steel drum, as tall as two people, glowing hot"
BIG_ROLL = "a giant roll of thin soft paper, taller than a person"
LOGS = "long paper logs (long thin rolls of toilet paper, many times longer than a normal roll, each on a cardboard tube)"
SAW = "a big round spinning saw blade"
BATHROOM = ("a modern bathroom: tiled walls, a white toilet, a sink with a mirror, and a toilet roll holder on the "
            "wall")
# ---- the one coloured thing per picture (settings.json "colour_subject") ----
C_ROME = "the Roman temple and columns: flat warm sandy beige"
C_SPONGE = "the sponge: flat yellow, on a flat warm brown stick"
C_ROMANS = "the Romans' tunics: each one flat plain colour (red, blue, green or yellow)"
C_VINEGAR = "the vinegar in the bucket: flat dark purple-red"
C_OUTHOUSE = "the outhouse: flat warm brown wood"
C_NATURE = "the leaves flat green, the moss flat dark green, the hay flat golden yellow, and the snow flat pale blue"
C_COB = "the dried corncob: flat pale tan"
C_PAPER = "the stacks of printed paper: flat creamy white"
C_NEWSPAPER = "the newspaper page: flat creamy grey-white"
C_STORE = "the shop's awning: flat red and white stripes"
C_SELLER = "the shopkeeper's waistcoat: flat dark green"
C_PACK = "the pack of paper: flat soft pink paper band, flat white sheets"
C_ROLL = "the roll of toilet paper: flat bright white, on a flat warm brown holder"
C_TREE = "the tall trees: flat green needles and flat brown trunks"
C_CHIPS = "the wood chips: flat light tan"
C_PULP = "the mushy pulp: flat muddy brown"
C_WHITE = "the pulp: flat muddy brown on the left turning to flat bright white on the right"
C_SPRAY = "the white pulp spraying onto the mesh: flat bright white, and the mesh flat light blue"
C_WATER = "the water draining through the mesh: flat bright blue drops"
C_DRUM = "the hot drum: flat orange-red glow"
C_BLADE = "the scraping blade: flat silver grey"
C_BIG_ROLL = "the giant roll of paper: flat bright white, beside a small car drawn flat red"
C_LOGS = "the cardboard tubes: flat light brown"
C_SAW = "the spinning saw blade: flat silver grey"
C_SPLIT = "on the left the sponge flat yellow, and on the right the corncob flat pale tan"
C_ROLL_NOW = "the fresh roll of toilet paper: flat bright white, on a flat shiny silver holder"
CAPTIONS = ("The place fills the whole frame; keep the very top and very bottom of the frame calm (sky, wall or floor) "
            "for captions. Never write any name, label or caption under or beside anyone or anything.")
POLITE = "nobody shown wiping, any bare bottoms, any mess"

M = 30


def shot(n, text, what, place, must, never="", colour=""):
    what = re.sub(r"(^|\. )([a-z])", lambda m: m[1] + m[2].upper(), what)   # blocks start lowercase
    return n, text, " ".join(x for x in (
        f"This is picture {n} of {M} in one continuous picture story; draw exactly this moment.",
        what, f"Place: {place}.",
        f"The one coloured thing in this picture is {colour}; every other person, object and the whole place are black "
        "ink lines only, no colour.",
        f"It MUST show: {must}.", f"NEVER: {never}." if never else "", CAPTIONS) if x)


S = [
 shot(1, "In ancient Rome,",
      f"Wide view of the Roman street; {ROMAN} walks toward the arched doorway of a stone building.",
      ROME_STREET,
      "the ancient Roman street with its columns and temple",
      "any modern thing, any letters on the buildings",
      colour=C_ROME),
 shot(2, "you probably wiped with a sponge on a stick.",
      f"{SPONGE} drawn big in the middle, standing upright, with a large question mark floating beside it.",
      LATRINE,
      "the sponge on a stick, with a question mark",
      POLITE + ", any letters",
      colour=C_SPONGE),
 shot(3, "And it was probably shared.",
      f"{ROMANS} on the long stone bench, chatting; one of them passes {SPONGE} to the man next to him, who looks at "
      "it unsure.",
      LATRINE,
      "the Romans sitting side by side and passing one sponge stick along",
      POLITE,
      colour=C_ROMANS),
 shot(4, "After you used it,",
      f"{ROMAN} stands up from the long stone bench, fully clothed, holding {SPONGE} with the sponge end pointing "
      "down.",
      LATRINE,
      "the Roman standing up holding the sponge stick",
      POLITE,
      colour=C_SPONGE),
 shot(5, "you rinsed it in a bucket of vinegar.",
      f"{ROMAN} dips the sponge end of {SPONGE} into {BUCKET} that stands by the stone bench, small splash lines.",
      LATRINE,
      "the sponge being dipped into the bucket of vinegar",
      POLITE,
      colour=C_VINEGAR),
 shot(6, "Then you left it for the next person.",
      f"{SPONGE} stands in {BUCKET}, its stick leaning on the rim; {ROMAN} walks away out of the arched doorway, "
      "while a second Roman man (a stick figure in a plain knee-length tunic) reaches for the stick, his face "
      "doubtful.",
      LATRINE,
      "the sponge stick left in the bucket and the next man reaching for it",
      POLITE,
      colour=C_SPONGE),
 shot(7, "Hundreds of years later,",
      "Wide view of the small village in the Middle Ages, smoke curling from cottage chimneys, the wooden outhouse "
      "at the edge.",
      VILLAGE,
      "the medieval village with its wooden outhouse",
      "any Roman thing, any modern thing",
      colour=C_OUTHOUSE),
 shot(8, "people grabbed whatever was around.",
      f"{VILLAGER} stands by the outhouse door looking around, scratching his head, three question marks above him.",
      VILLAGE,
      "the villager looking around for anything to use",
      POLITE,
      colour=C_OUTHOUSE),
 shot(9, "Leaves. Moss. Hay. Even snow.",
      "The picture is split into four equal boxes by a simple cross of lines: top left a handful of big soft leaves; "
      "top right a clump of soft moss; bottom left a bundle of hay; bottom right a small heap of snow.",
      "four simple boxes with a strip of ground under each thing",
      "the four things: leaves, moss, hay and snow",
      POLITE + ", any people, any letters",
      colour=C_NATURE),
 shot(10, "On farms, a dried corncob did the job.",
      f"{FARMER} stands by the outhouse holding up {COB}, shrugging; beside the outhouse door hangs a small basket "
      "full of dried corncobs.",
      FARM,
      "the farmer holding up a dried corncob by the outhouse",
      POLITE,
      colour=C_COB),
 shot(11, "Then printing made paper cheap.",
      f"{PRESS} in the print shop; a printer (a stick-figure man in a leather apron with rolled sleeves) pulls the "
      "long lever, and tall stacks of fresh paper pile up beside it.",
      PRINT_SHOP,
      "the printing press and the big stacks of paper it makes",
      "any readable letters",
      colour=C_PAPER),
 shot(12, "So people tore pages out of old newspapers and books.",
      f"{READER} stands by the wooden outhouse and tears a page out of {NEWSPAPER}; an old book with a few pages "
      "missing lies on a barrel beside him.",
      "the yard behind an old house in the seventeen hundreds: a wooden outhouse with a crescent moon on its door, a "
      "barrel, a fence",
      "the man tearing a page out of an old newspaper by the outhouse",
      POLITE + ", any readable letters",
      colour=C_NEWSPAPER),
 shot(13, "In eighteen fifty-seven,",
      "Wide view of the city street in the eighteen fifties, a horse and carriage passing a general store with a "
      "striped awning.",
      STREET_1850,
      "the city street of the eighteen fifties and the general store",
      "any modern thing, any letters on the shops",
      colour=C_STORE),
 shot(14, "an American named Joseph Gayetty",
      f"{SELLER} stands proudly behind the long wooden counter, hands on the counter.",
      SHOP_1850,
      "the shopkeeper of the eighteen fifties behind his counter",
      "any name written anywhere, any letters",
      colour=C_SELLER),
 shot(15, "sold the first paper made just for wiping.",
      f"{SELLER} holds up {PACK} across the counter to {CUSTOMER}, who hands him a coin.",
      SHOP_1850,
      "the shopkeeper selling a pack of paper sheets to a customer",
      "any roll of paper, any letters",
      colour=C_PACK),
 shot(16, "Flat sheets, in a pack.",
      f"Close view of {PACK} on the wooden counter, the top sheet lifted a little to show it is flat and loose.",
      SHOP_1850 + "; the close view of the counter fills most of the frame",
      "the flat sheets of paper in a pack",
      "any roll, any letters",
      colour=C_PACK),
 shot(17, "And in eighteen ninety, it came on a roll.",
      f"{OLD_ROLL}: plain painted wooden walls, a pull-chain toilet with a high wooden water tank; the end of the "
      "roll hangs down.",
      "a plain old washroom in the eighteen nineties: painted wooden walls, a pull-chain toilet with a high wooden "
      "water tank, a small window",
      "the roll of toilet paper on the old wall holder",
      POLITE + ", any letters",
      colour=C_ROLL),
 shot(18, "Today, toilet paper starts as a tree.",
      f"{LUMBERJACK} stands beside a tall straight pine tree and looks up at it.",
      FOREST,
      "a tall tree in the forest where toilet paper begins",
      "any toilet, any letters",
      colour=C_TREE),
 shot(19, "The logs are chopped into little chips.",
      f"Logs slide into the wide mouth of {CHIPPER}, and a stream of little wood chips shoots out of its side chute "
      f"onto a big heap; {MILL_WORKER} watches.",
      "a paper mill yard: big piles of logs, a heap of wood chips, conveyor belts, and the mill building behind",
      "the logs turning into little wood chips",
      "any letters",
      colour=C_CHIPS),
 shot(20, "The chips are cooked into a mushy soup of wood fibers.",
      f"Wood chips pour from a conveyor belt into the open hatch of {DIGESTER}; a cut-away window in its side shows "
      "a thick bubbling mushy soup inside, with steam curling up.",
      MILL,
      "the chips cooking into a mushy wood-fibre soup in the giant tank",
      "any letters",
      colour=C_PULP),
 shot(21, "It's washed and made white.",
      "A wide flat steel trough of pulp: at the left end the pulp is muddy brown, water sprays over it, and toward "
      "the right end it becomes clean and white; an arrow runs from left to right.",
      MILL,
      "the brown pulp being washed and turning white",
      "any letters",
      colour=C_WHITE),
 shot(22, "Then it's sprayed onto a fast-moving screen,",
      f"A long row of nozzles sprays watery white pulp evenly onto {SCREEN}, with speed lines along the belt.",
      MILL,
      "the white pulp being sprayed onto the moving mesh belt",
      "any letters",
      colour=C_SPRAY),
 shot(23, "and the water drains away.",
      f"Close view from the side of {SCREEN}: a thin white mat of pulp rides on top, and lots of water drops fall "
      "through the mesh into a tray below.",
      MILL + "; the close view fills most of the frame",
      "water draining down through the mesh, leaving a thin mat of pulp",
      "any letters",
      colour=C_WATER),
 shot(24, "A giant hot drum dries it into a super thin sheet.",
      f"{DRUM} turns, with a super thin white sheet of paper wrapped around it; wavy heat lines rise off it; "
      f"{MILL_WORKER} stands small beside it.",
      MILL,
      "the giant hot drum drying a super thin sheet of paper",
      "any letters",
      colour=C_DRUM),
 shot(25, "A blade scrapes it off and crinkles it soft.",
      "Close view where a long flat steel blade presses against the turning drum and scrapes the thin sheet off; "
      "the sheet comes away in soft crinkled wavy folds.",
      MILL + "; the close view fills most of the frame",
      "the blade scraping the sheet off the drum and crinkling it",
      "any letters",
      colour=C_BLADE),
 shot(26, "It's wound onto a roll heavier than a car.",
      f"{BIG_ROLL} sits on a steel stand; beside it, a small ordinary car looks tiny; {MILL_WORKER} looks up at the "
      "roll.",
      MILL,
      "the giant paper roll, far bigger than the car next to it",
      "any letters",
      colour=C_BIG_ROLL),
 shot(27, "Machines rewind it onto cardboard tubes, in long logs.",
      f"A machine unwinds the giant roll and rewinds the paper into {LOGS}, which roll out one after another onto a "
      "conveyor.",
      MILL,
      "the long paper logs wound on cardboard tubes",
      "any letters",
      colour=C_LOGS),
 shot(28, "A spinning saw slices the logs into rolls.",
      f"{SAW} slices down through one of the long paper logs; finished toilet rolls drop off the end in a row.",
      MILL,
      "the spinning saw slicing the long log into toilet rolls",
      "any people near the blade, any letters",
      colour=C_SAW),
 shot(29, "Back then, a shared sponge and a corncob.",
      f"The picture is split down the middle by a simple vertical line. Left half: {SPONGE} standing in {BUCKET}. "
      f"Right half: {COB} hanging on a nail by a wooden outhouse door.",
      f"left half: {LATRINE}; right half: {FARM}",
      "the sponge stick on the left and the dried corncob on the right",
      POLITE,
      colour=C_SPLIT),
 shot(30, "Now? A soft roll on the wall.",
      "A fresh soft roll of toilet paper on the wall holder, its end hanging down neatly; a stick-figure hand "
      "reaches for it, small sparkle lines around the roll.",
      BATHROOM,
      "the fresh soft roll of toilet paper on the bathroom wall",
      POLITE + ", any letters",
      colour=C_ROLL_NOW),
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
