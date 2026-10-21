"""Image prompts for icecream-lake-then-now, written as one story (channels/SHORTS_RULES.md "How image prompts are
written"; worked example: ../tooth-key-then-now/scenes.py). Checks every line against script.md; this file approves the
script (no approval step) and writes scene + full prompt for every line into script.json.
usage: python channels/what-happens-now/videos/icecream-lake-then-now/scenes.py"""
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
# back then (the eighteen hundreds)
WORKERS = ("two ice cutters from the eighteen hundreds (two stick-figure men in heavy knee-length wool coats, knitted "
           "caps, thick mittens and tall boots)")
SAW = ("a long ice saw (a long straight saw blade taller than a man's waist, with big jagged teeth along one edge and a "
       "crosswise wooden handle at the top held with both hands)")
BLOCK = "a big square block of ice (drawn as a plain outlined cube with a few short shine lines on its faces)"
BLOCKS = "big square blocks of ice (each drawn as a plain outlined cube with a few short shine lines on its faces)"
HORSE_SLED = ("a big work horse with a thick mane pulling a low flat wooden sled on two long wooden runners")
LAKE = ("a wide frozen lake in winter: flat smooth ice with a few long cracks drawn on it, snow on the shore, a row of "
        "snowy pine trees along the far side, and a small wooden farmhouse with a smoking chimney far off; a grey "
        "winter sky")
FARM_ROAD = ("a snowy country road from the lake to a farm: deep snow on both sides, a wooden fence, bare trees, and "
             "a wooden farmhouse and barn ahead")
ICEHOUSE_OUT = ("the outside of a farm ice house in the eighteen hundreds: a small windowless wooden shed with thick "
                "plank walls, a steep pointed roof and one heavy wooden door, beside a farmhouse")
ICEHOUSE_IN = ("the inside of a farm ice house in the eighteen hundreds: thick wooden plank walls with no windows, a "
               "heavy wooden door standing open with daylight coming in, and a deep floor of loose sawdust")
SAWDUST = "loose sawdust (a soft heap of tiny dots and short flecks)"
COOK = ("a stick-figure woman from the eighteen hundreds (hair in a round bun, a long plain dress to her ankles and "
        "an apron over it)")
PORCH = ("the back porch of a farmhouse in the eighteen hundreds on a hot summer day: wooden porch boards, a wooden "
         "railing, a small wooden table, and behind the porch a green field, a few leafy trees and a blazing sun")
PICK = "an ice pick (a short wooden handle with one long thin pointed metal spike)"
JUG = "a tall pottery jug of cream"
CAN = "a tall round metal can with a lid (as tall as a forearm)"
FREEZER = ("a hand-crank ice cream freezer (a round wooden bucket held together with metal hoops; standing in its "
           "middle a tall round metal can; across the top an iron frame with a crank handle that sticks out sideways)")
PADDLE = "a wooden paddle with flat wooden slats (it turns inside the metal can when the crank turns)"
SALT = "a small open cloth sack of coarse salt"
BOWL = "a plain round bowl"
# now
FACTORY_OUT = ("a big modern ice cream factory: a long flat building with big metal walls, loading doors, short "
               "chimneys and pipes on the roof, a car park in front")
FACTORY_IN = ("the inside of a modern ice cream factory: a clean shiny floor, a row of giant round steel tanks with "
              "pipes and valves between them, a metal walkway, bright ceiling lights")
WORKER = ("a factory worker (a stick-figure man in a white coat, a white hair net, white boots and gloves)")
TANKS = "giant round steel tanks taller than a person, joined by pipes and valves"
HEATER = "a boxy steel heating machine with pipes going in and out and a small round dial on the front"
COOLTANK = "a giant round steel tank with frost lines on it"
FREEZE_PIPE = ("an ice cream freezing machine: a long thick round steel pipe lying on its side on a steel stand, with a "
               "small motor at one end and a nozzle at the other end")
TUBS = "plain round ice cream tubs with lids (no letters or pictures on them)"
TUNNEL = "a long boxy steel tunnel with frost on its walls and a moving belt running through it"
TRUCK = ("a freezer delivery truck (a box truck with a big plain white box on the back and a small cooling unit on the "
         "front of the box)")
STORE = ("the front of a big modern supermarket: glass sliding doors, a wide car park, a row of shopping trolleys")
YOU = "a stick-figure young man (short spiky hair, plain T-shirt and jeans)"
KITCHEN = ("a modern home kitchen: a tall fridge-freezer with two doors, counters, a sink under a window, cupboards "
           "above")
# ---- the one coloured thing per picture (settings.json "colour_subject") ----
C_ICE = "the ice: flat pale icy blue"
C_BOWL_ICE = "the bowl of ice cream: the bowl flat pale blue and the scoops of ice cream flat creamy white-yellow"
C_WORKERS = "the two ice cutters' coats: flat dark red"
C_SAW = "the ice saws: their blades flat steel grey, their handles flat warm brown"
C_HORSE = "the horse: flat warm brown, with a darker brown mane"
C_ICEHOUSE = "the ice house: flat warm brown wood"
C_SAWDUST = "the sawdust: flat light tan"
C_SUN = "the blazing sun: flat bright yellow, with flat orange heat arrows"
C_PICK = "the ice pick: its spike flat steel grey, its handle flat warm brown"
C_MALLET = "the wooden mallet: flat warm brown"
C_CREAM = "the cream pouring from the jug: flat creamy white-yellow"
C_CAN = "the metal can: flat shiny silver grey"
C_BUCKET = "the wooden bucket: flat warm brown, with flat dark grey metal hoops"
C_SALT = "the salt: the sack flat light brown and the falling salt grains flat light grey"
C_THERMO = "the thermometer: its glass tube outline black, its liquid flat bright red"
C_CRANK = "the crank handle and its iron frame: flat dark iron grey"
C_PADDLE = "the wooden paddle: flat warm brown"
C_COOK = "the woman's dress: flat blue, with a flat white apron"
C_ICECREAM = "the ice cream: flat creamy white-yellow"
C_FACTORY = "the factory building: flat light blue metal walls"
C_SUGAR = "the sugar pouring into the tank: flat white grains on a flat light grey sack"
C_TANKS = "the steel tanks: flat shiny silver grey"
C_GERMS = "the little germ blobs: flat green, each crossed out with a flat red X"
C_CLOCK = "the wall clock: its face flat white with a flat red rim"
C_PIPE = "the freezing machine's long steel pipe: flat shiny silver grey"
C_SOFT = "the soft ice cream coming out of the nozzle: flat creamy white-yellow"
C_BITS = "the chocolate chunks flat dark brown and the strawberries flat red"
C_TUBS = "the ice cream tubs: flat pink"
C_TUNNEL = "the cold air lines blowing in the tunnel: flat pale icy blue"
C_TRUCK = "the freezer truck: flat bright blue cab, with a flat white box"
C_SPLIT = ("on the left the lake ice blocks flat pale icy blue, and on the right the woman's dress flat blue with a "
           "flat white apron")
C_FREEZER_DOOR = "the home fridge-freezer: flat light grey"
CAPTIONS = ("The place fills the whole frame; keep the very top and very bottom of the frame calm (sky, wall or floor) "
            "for captions. Never write any name, label or caption under or beside anyone or anything.")

M = 38


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
      "Wide view of the frozen lake on a still winter morning, nobody on it yet, a few snowflakes falling.",
      LAKE,
      "the wide frozen lake in winter",
      "any people, any modern thing, any ice cream",
      colour=C_ICE),
 shot(2, "ice cream started on a frozen lake.",
      f"A big {BOWL} heaped with three round scoops of ice cream sits right on the flat ice in the middle of the frozen "
      "lake, like a surprise, with a few small sparkle lines around it.",
      LAKE,
      "a bowl of ice cream sitting on the frozen lake",
      "any people, any spoon held by anyone",
      colour=C_BOWL_ICE),
 shot(3, "In the middle of winter.",
      f"{WORKERS} walk out onto the frozen lake through falling snow, each carrying {SAW} over one shoulder, their "
      "breath showing as small puffs.",
      LAKE,
      "the two men in heavy winter coats walking onto the frozen lake in the snow",
      "any sled or horse yet, any ice blocks yet",
      colour=C_WORKERS),
 shot(4, "Men sawed the lake ice",
      f"{WORKERS} stand on the frozen lake, each pushing {SAW} straight down into the ice with both hands; a long "
      "straight cut line runs across the ice in front of them, with small chips of ice flying.",
      LAKE,
      "the two men sawing a straight line into the lake ice",
      "power tools, chainsaws, any modern machine",
      colour=C_SAW),
 shot(5, "into big square blocks.",
      f"Seen from above at an angle: a grid of straight cut lines on the frozen lake, and a row of {BLOCKS} floating "
      f"loose in a channel of dark open water; {WORKERS} push the blocks along with long wooden poles.",
      LAKE,
      "the neat square blocks of ice cut out of the lake",
      "round chunks, broken shards",
      colour=C_ICE),
 shot(6, "Horses pulled the blocks home on sleds.",
      f"{HORSE_SLED}, the sled stacked with {BLOCKS}; one of the ice cutters (a stick-figure man in a heavy "
      "knee-length wool coat, a knitted cap, thick mittens and tall boots) walks beside the horse holding the reins.",
      FARM_ROAD,
      "the horse pulling the sled full of ice blocks home through the snow",
      "a car, a truck, wheels on the sled",
      colour=C_HORSE),
 shot(7, "The blocks went into an ice house,",
      f"{WORKERS} carry {BLOCK} between them with big iron ice tongs (scissor-like tongs with two curved hooked "
      "points) toward the open wooden door of the ice house; the empty horse sled waits behind them.",
      ICEHOUSE_OUT,
      "the men carrying an ice block into the wooden ice house",
      "windows on the ice house, a modern fridge",
      colour=C_ICEHOUSE),
 shot(8, "buried deep in sawdust.",
      f"Inside the ice house: {BLOCKS} stacked in neat rows, each block with a gap around it, and {SAWDUST} heaped "
      f"over the top and packed into every gap, so only the tops of a few blocks peek out; one of the ice cutters (a "
      "stick-figure man in a heavy knee-length wool coat, a knitted cap and thick mittens) shovels more sawdust on "
      "with a wide wooden shovel.",
      ICEHOUSE_IN,
      "the ice blocks being buried in sawdust",
      "a fridge, any electric thing",
      colour=C_SAWDUST),
 shot(9, "Sawdust kept the heat out,",
      f"Cut-away view of the ice house, as if its front wall were sliced off: inside, {BLOCKS} buried in {SAWDUST}; "
      "outside, a big blazing sun in the sky sends wavy heat arrows toward the ice house, and the arrows bounce off "
      "the thick walls and the sawdust and never reach the ice.",
      "the outside of a farm ice house in the eighteen hundreds on a hot day: a small windowless wooden shed with "
      "thick plank walls and a steep pointed roof, green grass and leafy trees around it",
      "the heat arrows from the sun bouncing off before they reach the ice",
      "any people",
      colour=C_SUN),
 shot(10, "so the ice lasted into summer.",
      f"The heavy wooden door of the ice house stands open on a summer day: inside, {BLOCKS} still solid and sharp "
      f"in their bed of {SAWDUST}; outside, green leafy trees, flowers in the grass and a blazing sun.",
      ICEHOUSE_OUT + ", on a hot summer day with green trees, flowers and a blazing sun",
      "solid ice blocks still inside the ice house in the middle of summer",
      "melting puddles, snow, any people",
      colour=C_ICE),
 shot(11, "On a hot day, you chipped off a chunk",
      f"{COOK} stands at the open door of the ice house, wiping sweat off her forehead with one hand and holding "
      f"{PICK} in the other, chipping a chunk off {BLOCK} that sits in its bed of {SAWDUST}.",
      ICEHOUSE_OUT + ", on a hot summer day with green trees and a blazing sun",
      "the woman chipping a chunk of ice off a block with the ice pick",
      "a fridge, a freezer, any modern thing",
      colour=C_PICK),
 shot(12, "and smashed it into little pieces.",
      f"{COOK} kneels on the porch boards and pounds a plain cloth sack full of ice with a heavy wooden mallet; "
      "small bits of crushed ice spill out of the sack's open top, with small burst lines where the mallet hits.",
      PORCH,
      "the woman smashing the ice in a sack with a wooden mallet",
      "a blender, any machine",
      colour=C_MALLET),
 shot(13, "You poured cream, sugar and vanilla",
      f"{COOK} stands at the small wooden table and pours cream from {JUG}; on the table beside her sit a small bowl "
      "heaped with sugar and one long thin dark vanilla pod.",
      PORCH,
      "the woman pouring cream, with the sugar and the vanilla pod beside it",
      "any packaged food, any bottle with a label",
      colour=C_CREAM),
 shot(14, "into a metal can.",
      f"Close view on the table: cream pours from {JUG} into the open top of {CAN}, which is already half full.",
      PORCH,
      "the cream filling the tall metal can",
      "a glass, a bowl",
      colour=C_CAN),
 shot(15, "The can went into a wooden bucket.",
      f"{COOK} lowers {CAN}, now closed with its lid, down into the middle of a round wooden bucket held together "
      "with metal hoops, standing on the porch boards; there is an empty ring of space between the can and the "
      "bucket's wall.",
      PORCH,
      "the metal can going into the middle of the hooped wooden bucket",
      "any ice in the bucket yet",
      colour=C_BUCKET),
 shot(16, "You packed crushed ice all around it,",
      f"{COOK} scoops crushed ice out of the cloth sack with both hands and packs it into the ring of space between "
      "the tall metal can and the wall of the round wooden bucket with metal hoops; the can stands in the middle, "
      "the ice piling up around it.",
      PORCH,
      "the crushed ice packed in a ring all around the metal can",
      "ice inside the can",
      colour=C_ICE),
 shot(17, "with handfuls of salt.",
      f"{COOK} throws a handful of coarse salt from {SALT} onto the crushed ice that fills the ring around the tall "
      "metal can in the round wooden bucket with metal hoops; salt grains fly from her hand.",
      PORCH,
      "the woman throwing handfuls of salt onto the ice around the can",
      "salt going into the can, a salt shaker",
      colour=C_SALT),
 shot(18, "Salt makes the ice even colder.",
      "Close view of the top of the round wooden bucket with metal hoops: crushed ice sprinkled with salt grains "
      "packed around the tall metal can, and an old glass thermometer pushed into the salty ice; a big arrow "
      "beside the thermometer points down, its liquid line low, and a few frost lines around it.",
      PORCH,
      "the thermometer in the salty ice showing it getting colder",
      "any numbers or letters on the thermometer",
      colour=C_THERMO),
 shot(19, "Then you turned the crank.",
      f"{COOK} sits on the porch boards beside {FREEZER}, holding the bucket steady with one hand and turning the "
      "crank handle with the other; a curved arrow around the handle shows it turning.",
      PORCH,
      "the woman turning the crank handle of the ice cream freezer",
      "an electric motor, a plug or a cord",
      colour=C_CRANK),
 shot(20, "Inside, a paddle scraped the cream",
      f"Cut-away view of {FREEZER}, as if the front were sliced off: crushed ice packed around the tall metal can, "
      f"and inside the can, the cream with {PADDLE} standing in it; curved arrows show the paddle turning.",
      "inside the ice cream freezer on the farmhouse porch; the cut-away view fills the whole frame",
      "the paddle turning inside the can of cream, with ice all around the can",
      "any people, any motor",
      colour=C_PADDLE),
 shot(21, "off the cold metal walls.",
      "Close view inside the metal can: a thin layer of frozen cream clings to the cold metal wall, with frost lines "
      f"on the wall, and the edge of {PADDLE} scrapes it off in a curl, a small arrow showing the scrape.",
      "inside the metal can of the ice cream freezer; the close view fills the whole frame",
      "the paddle scraping frozen cream off the cold metal wall",
      "any people, any spoon",
      colour=C_PADDLE),
 shot(22, "You turned and turned",
      f"{COOK} keeps turning the crank of {FREEZER}, sweat drops flying off her face, round motion lines around the "
      "crank to show it going round and round.",
      PORCH,
      "the woman cranking hard, over and over",
      "an electric motor, a smile",
      colour=C_COOK),
 shot(23, "until your arm ached.",
      f"{COOK} sits back beside {FREEZER}, letting go of the crank and rubbing her tired arm with her other hand, "
      "small zigzag pain lines around the arm, her face tired.",
      PORCH,
      "the woman holding her aching arm after all the cranking",
      "any blood, any injury",
      colour=C_COOK),
 shot(24, "Slowly, the cream got thick.",
      f"{COOK} lifts {PADDLE} out of the open metal can of {FREEZER}; thick cream clings to the paddle's slats and "
      "drips slowly, and she peers at it hopefully.",
      PORCH,
      "the thick cream clinging to the paddle",
      "finished scoops yet",
      colour=C_ICECREAM),
 shot(25, "Then it froze.",
      f"{COOK} scoops firm frozen ice cream out of the open metal can into {BOWL} with a big spoon, smiling widely, "
      "small sparkle lines around the bowl.",
      PORCH,
      "the woman scooping the finished frozen ice cream into a bowl, happy",
      "a fridge, a store tub",
      colour=C_ICECREAM),
 shot(26, "Today, it's made in a factory.",
      "Wide view of the factory from the car park, a big flat roof with pipes, a few cars parked in front.",
      FACTORY_OUT,
      "the big modern ice cream factory building",
      "any letters or logo on the building",
      colour=C_FACTORY),
 shot(27, "Milk, cream and sugar are mixed",
      f"{WORKER} stands on the metal walkway and tips a big sack of sugar into the open hatch on top of one of the "
      f"{TANKS}; a pipe pours milk into the same hatch.",
      FACTORY_IN,
      "sugar and milk going into a big steel mixing tank",
      "any letters on the sack or tanks",
      colour=C_SUGAR),
 shot(28, "in giant steel tanks.",
      f"Wide view of the row of {TANKS}, each as tall as two people; {WORKER} stands small at the bottom looking up at "
      "them.",
      FACTORY_IN,
      "how giant the steel tanks are next to the worker",
      "any letters",
      colour=C_TANKS),
 shot(29, "The mix is heated to kill any germs,",
      f"Pale mix flows through a clear pipe into {HEATER}; wavy heat lines rise from the machine, and on the other "
      "side tiny round germ blobs with little faces drop out of the pipe, each crossed out.",
      FACTORY_IN,
      "the mix being heated and the germs being killed",
      "any letters",
      colour=C_GERMS),
 shot(30, "then cooled and left to rest for a few hours.",
      f"{COOLTANK} stands still with frost lines around it; on the wall above it hangs a round wall clock, and a "
      "curved arrow around the clock face shows time passing; the tank is closed and quiet.",
      FACTORY_IN,
      "the mix resting in a cold tank while hours pass",
      "any numbers on the clock, any letters",
      colour=C_CLOCK),
 shot(31, "A machine freezes it inside a cold steel pipe",
      f"{FREEZE_PIPE}, with frost lines on the outside of the pipe; a cut-away window in the pipe shows the mix "
      f"inside turning into ice cream; {WORKER} checks it.",
      FACTORY_IN,
      "the long cold steel pipe freezing the mix",
      "a hand crank, any letters",
      colour=C_PIPE),
 shot(32, "and whips in air, so it's soft.",
      "Close view of the nozzle at the end of the long steel freezing pipe: a thick ribbon of soft ice cream flows "
      "out of it, with small round air bubbles drawn in it and a small air hose joined to the pipe.",
      FACTORY_IN,
      "soft ice cream with air bubbles in it coming out of the machine",
      "any letters",
      colour=C_SOFT),
 shot(33, "Bits of chocolate or fruit are added.",
      "A small steel hopper above the stream of soft ice cream drops chocolate chunks and strawberry pieces into "
      "it as it flows past.",
      FACTORY_IN,
      "chocolate chunks and strawberries falling into the ice cream",
      "any letters",
      colour=C_BITS),
 shot(34, "Machines fill the tubs,",
      f"A long moving belt carries a line of {TUBS}; a steel nozzle above the belt fills each tub with soft ice "
      "cream as it passes; small arrows show the belt moving.",
      FACTORY_IN,
      "the machine filling a line of tubs",
      "any letters or pictures on the tubs, people's hands doing it",
      colour=C_TUBS),
 shot(35, "and a tunnel of freezing air makes them hard.",
      f"The line of filled {TUBS} rides on the belt into {TUNNEL}; inside, strong curly cold air lines blow over "
      "the tubs, and frost covers them as they come out the other end.",
      FACTORY_IN,
      "the tubs going through the frosty tunnel of freezing air",
      "any letters",
      colour=C_TUNNEL),
 shot(36, "A freezer truck takes them to the store.",
      f"{TRUCK} drives along a road toward a big supermarket, small cold frost lines on its box, speed lines "
      "behind it.",
      f"a wide road leading to {STORE}",
      "the freezer truck driving to the supermarket",
      "any letters or logo on the truck or the store",
      colour=C_TRUCK),
 shot(37, "Back then, a frozen lake and an aching arm.",
      f"The picture is split down the middle by a simple vertical line. Left half: on the frozen lake, {WORKERS} "
      f"saw {BLOCKS} out of the ice. Right half: on the farmhouse porch, {COOK} turns the crank of {FREEZER}, "
      "rubbing her tired arm with her other hand.",
      f"left half: {LAKE}; right half: {PORCH}",
      "the lake ice being cut on the left and the woman cranking with an aching arm on the right",
      "any modern thing",
      colour=C_SPLIT),
 shot(38, "Now? You just open the freezer.",
      f"{YOU} opens the freezer door of the tall fridge-freezer with one hand and takes out one of the {TUBS} with "
      "the other, a big easy smile; cold air curls out of the open freezer.",
      KITCHEN,
      "the young man opening his home freezer and taking out a tub of ice cream",
      "any letters on the tub, any ice saw, any crank",
      colour=C_FREEZER_DOOR),
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
