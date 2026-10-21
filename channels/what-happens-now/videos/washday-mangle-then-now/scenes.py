"""Image prompts for washday-mangle-then-now, written as one story (channels/SHORTS_RULES.md "How image prompts are
written"; worked example: ../tooth-key-then-now/scenes.py). Checks every line against script.md; this file approves the
script (no approval step) and writes scene + full prompt for every line into script.json.
usage: python channels/what-happens-now/videos/washday-mangle-then-now/scenes.py"""
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
# back then (around nineteen hundred)
WOMAN = ("a stick-figure woman from around nineteen hundred (hair pinned up in a bun, a long plain skirt to her "
         "ankles, a blouse with the sleeves rolled up to the elbows, and a long apron)")
SCULLERY = ("a scullery around nineteen hundred: brick walls, a stone floor, a deep stone sink with one single cold "
            "tap, a small window, and in the corner the copper (a big round metal pot set into a waist-high brick "
            "stand with a small iron fire door at the bottom)")
COPPER = ("the copper (a big round metal pot set into a waist-high brick stand, with a small iron fire door at the "
          "bottom and a wooden lid)")
TUB = "a round wooden tub held together with metal hoops"
WASHBOARD = "a washboard (a wooden frame holding a sheet of wavy ribbed metal)"
PLUNGER = "a wooden plunger (a long wooden handle with a round wooden head with short legs at the bottom)"
MANGLE = ("the mangle (a big iron stand as tall as a woman's waist with two thick wooden rollers lying one above the "
          "other, and a big iron wheel with a handle on one side to turn them)")
BATH = "a long tin bath of cold water"
YARD = ("the small backyard of a brick terraced house around nineteen hundred: a brick wall, a stone-flagged ground, "
        "a washing line strung between two posts with a long wooden prop holding it up, the back door of the house")
STREET = ("a row of brick terraced houses around nineteen hundred seen from their backyards: washing lines in every "
          "yard, chimneys smoking, an early morning sky")
# now
YOU = "a stick-figure young man (short spiky hair, plain T-shirt and jeans)"
MACHINE = ("a front-loading washing machine (a white box with a round glass door on the front, a small soap drawer at "
           "the top left, a round dial and one round button)")
CUT = ("a cut-away view of a front-loading washing machine, as if its side were see-through: the round metal drum "
       "inside, covered in tiny holes, with three small paddles on its inside, a motor below, a water pipe at the top, "
       "and a small pump and drain hose at the bottom")
LAUNDRY_NEW = ("a modern laundry corner: the washing machine under a counter, a shelf above with a bottle of "
               "detergent, a laundry basket on the tiled floor")
# ---- the one coloured thing per picture (settings.json "colour_subject") ----
C_LINES = "the washing hanging on the lines: flat white sheets and flat blue and red shirts"
C_HEAP = "the heap of laundry: flat dull grey-brown dirty clothes"
C_CAL = "the calendar page flat cream, with the sun flat yellow"
C_FIRE = "the fire in the copper's little fire door: flat orange and yellow flames"
C_COPPER = "the copper pot: flat shiny copper orange"
C_BUCKET = "the bucket of water: flat light blue water in a flat grey bucket"
C_TAP = "the cold tap and the water running from it: flat light blue"
C_WHITES = "the white sheets: filled flat bright white, with flat light grey steam"
C_SOAP = "the bar of soap flat pale yellow, and the soda crystals flat white"
C_COLOURED = "the coloured clothes in the tub: flat red, blue and green"
C_BOARD = "the washboard's ribbed metal: flat silver grey, with flat white soap suds"
C_PLUNGER = "the wooden plunger: flat warm brown"
C_MANGLE = "the mangle's iron frame and wheel: flat dark green"
C_ROLLERS = "the water pouring out of the shirt between the rollers: flat grey-blue"
C_BATH = "the cold water in the tin bath: flat light blue"
C_SHEETS = "the sheets on the line: filled flat bright white"
C_CLOUD = "the rain cloud: flat dark grey"
C_MACHINE = "the washing machine: flat light grey with a flat blue glass door"
C_SOAP_NOW = "the detergent: flat bright blue liquid"
C_WATER = "the water flowing into the drum: flat bright blue"
C_SUDS = "the clothes tumbling in the suds: flat red, blue and green clothes in flat white suds"
C_GREY = "the dirty water being pumped out: flat murky grey"
C_RINSE = "the clean rinse water: flat bright blue"
C_SPIN = "the spinning drum: flat silver grey with flat blue spin lines"
C_DROPS = "the water drops shooting out: flat bright blue"
C_CLEAN = "the clean clothes: flat red, blue and green"
C_HANDS = "the woman's sore hands: flat red"
C_BUTTON = "the round button: flat bright green, with a flat green tick"
CAPTIONS = ("The place fills the whole frame; keep the very top and very bottom of the frame calm (sky, wall or floor) "
            "for captions. Never write any name, label or caption under or beside anyone or anything.")

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
 shot(1, "Around nineteen hundred,",
      "Wide view over the backyards of a row of terraced houses on a Monday morning, washing hanging on every line.",
      STREET,
      "the row of terraced houses with washing lines in every yard",
      "any modern thing, any cars",
      colour=C_LINES),
 shot(2, "laundry wasn't a chore.",
      f"A huge heap of dirty laundry (sheets, shirts, socks, aprons) piled taller than {WOMAN}, who stands beside it "
      "with her hands on her hips, looking up at it.",
      SCULLERY,
      "the huge mountain of laundry next to the woman",
      "a washing machine",
      colour=C_HEAP),
 shot(3, "It was a whole day, every Monday.",
      "A simple wall calendar page on the scullery wall with one day box circled; beside it a curved arc shows a sun "
      "rising on the left and setting on the right, with a dotted path between them.",
      SCULLERY,
      "a whole day from sunrise to sunset spent on the laundry",
      "any letters or words on the calendar",
      colour=C_CAL),
 shot(4, "Before breakfast, you lit a fire",
      f"Early morning, still dark at the small window: {WOMAN} kneels and lights a fire in the small iron fire door "
      f"at the bottom of {COPPER}, holding a match.",
      SCULLERY + ", before dawn",
      "the woman lighting the fire under the copper",
      "a gas stove, any electric thing",
      colour=C_FIRE),
 shot(5, "under a big metal pot called a copper.",
      f"Close view of {COPPER}, its lid off, the fire glowing in its little iron door.",
      SCULLERY,
      "the big round metal pot of the copper in its brick stand",
      "any letters",
      colour=C_COPPER),
 shot(6, "You filled it bucket by bucket,",
      f"{WOMAN} lifts a heavy metal bucket of water and pours it into {COPPER}, leaning back from the weight; two "
      "more full buckets wait on the floor.",
      SCULLERY,
      "the woman pouring a bucket of water into the copper",
      "a hose, a tap over the copper",
      colour=C_BUCKET),
 shot(7, "from one cold tap.",
      f"{WOMAN} holds a metal bucket under the one single cold tap over the deep stone sink as it fills slowly.",
      SCULLERY,
      "the one cold tap filling the bucket",
      "hot and cold taps, a shower",
      colour=C_TAP),
 shot(8, "The whites went in to boil,",
      f"{WOMAN} pushes a pile of white sheets down into the steaming {COPPER[4:]} with a long wooden stick, steam "
      "curling up.",
      SCULLERY,
      "the white sheets going into the boiling copper",
      "coloured clothes in the copper",
      colour=C_WHITES),
 shot(9, "with hard soap and soda.",
      f"{WOMAN} drops a hard bar of soap and a scoop of soda crystals into the steaming {COPPER[4:]}.",
      SCULLERY,
      "the bar of soap and the soda crystals going into the copper",
      "any letters or labels, a modern detergent bottle",
      colour=C_SOAP),
 shot(10, "The colored clothes soaked in a wooden tub.",
      f"Coloured shirts, aprons and socks lie soaking in water in {TUB} on the stone floor.",
      SCULLERY,
      "the coloured clothes soaking in the wooden tub",
      "any people",
      colour=C_COLOURED),
 shot(11, "Then you scrubbed them up and down on a washboard.",
      f"{WOMAN} kneels by {TUB} with {WASHBOARD} standing in it and rubs a wet shirt hard up and down on the ribbed "
      "metal, soap suds and splash lines flying.",
      SCULLERY,
      "the woman scrubbing a shirt up and down on the washboard",
      "a machine",
      colour=C_BOARD),
 shot(12, "Or you pounded them with a wooden plunger.",
      f"{WOMAN} stands over {TUB} full of clothes and water and pounds them up and down with {PLUNGER}, big splash "
      "lines.",
      SCULLERY,
      "the woman pounding the clothes in the tub with the wooden plunger",
      "a machine",
      colour=C_PLUNGER),
 shot(13, "Next, every single piece went through the mangle.",
      f"{MANGLE} stands in the backyard beside a tall heap of wet dripping laundry in a basket.",
      YARD,
      "the big iron mangle next to the heap of wet laundry",
      "any electric thing",
      colour=C_MANGLE),
 shot(14, "You turned a big handle,",
      f"{WOMAN} turns the big iron wheel of {MANGLE} with both hands, leaning into it, a curved arrow around the "
      "wheel.",
      YARD,
      "the woman turning the mangle's big wheel handle",
      "any electric thing",
      colour=C_MANGLE),
 shot(15, "and two rollers squeezed the dirty water out.",
      "Close view of the two thick wooden rollers of the mangle: a wet shirt is squeezed flat between them, and dirty "
      "water pours out and splashes into a bucket below.",
      YARD + "; the close view of the rollers fills most of the frame",
      "the shirt squashed flat between the rollers with water pouring out",
      "any people's fingers in the rollers",
      colour=C_ROLLERS),
 shot(16, "Then you rinsed it all in cold water.",
      f"{WOMAN} dunks an armful of laundry into {BATH}, cold water splashing, her face wincing at the cold.",
      YARD,
      "the woman rinsing the laundry in the tin bath of cold water",
      "hot steam, a machine",
      colour=C_BATH),
 shot(17, "And put it through the mangle again.",
      f"{WOMAN} feeds a sheet into {MANGLE} again and turns the wheel, sweat drops on her forehead, a tired face.",
      YARD,
      "the woman tired, feeding the laundry through the mangle a second time",
      "any electric thing",
      colour=C_MANGLE),
 shot(18, "Finally, you pegged everything on the line,",
      f"{WOMAN} pegs a white sheet onto the washing line with wooden pegs; shirts and sheets already hang along "
      "the line.",
      YARD,
      "the woman pegging the sheets onto the washing line",
      "a tumble dryer",
      colour=C_SHEETS),
 shot(19, "and hoped it didn't rain.",
      f"{WOMAN} stands under the full washing line and looks up, worried, at a big dark rain cloud drifting toward "
      "the yard.",
      YARD,
      "the woman looking worriedly at a rain cloud over her washing",
      "rain already falling",
      colour=C_CLOUD),
 shot(20, "Today, you throw it all in a machine.",
      f"{YOU} stuffs an armful of clothes from the laundry basket through the open round door of {MACHINE}.",
      LAUNDRY_NEW,
      "the young man throwing his clothes into the washing machine",
      "any washboard, any mangle, any letters or logos",
      colour=C_MACHINE),
 shot(21, "Add soap, and press a button.",
      f"{YOU} pours a little detergent into the soap drawer of {MACHINE} with one hand and presses its round button "
      "with the other.",
      LAUNDRY_NEW,
      "the detergent going in and the button being pressed",
      "any letters or labels",
      colour=C_SOAP_NOW),
 shot(22, "Water pours in by itself.",
      f"{CUT}: water pours in from the pipe at the top and fills the bottom of the drum around the clothes.",
      LAUNDRY_NEW,
      "water filling the drum by itself",
      "any people, any letters",
      colour=C_WATER),
 shot(23, "The drum turns, lifting and dropping your clothes in soapy water.",
      f"{CUT}: the drum turns, the paddles lift the clothes up and they drop back down into soapy water, with round "
      "turning arrows and suds.",
      LAUNDRY_NEW,
      "the clothes being lifted and dropped in soapy water as the drum turns",
      "any people, any letters",
      colour=C_SUDS),
 shot(24, "The dirty water is pumped out,",
      f"{CUT}: the small pump at the bottom pushes dirty water out through the drain hose, with arrows.",
      LAUNDRY_NEW,
      "the dirty water being pumped out down the hose",
      "any people, any letters",
      colour=C_GREY),
 shot(25, "and clean water rinses them.",
      f"{CUT}: fresh clean water pours in from the top pipe over the clothes, washing the suds away.",
      LAUNDRY_NEW,
      "clean water rinsing the clothes",
      "any people, any letters",
      colour=C_RINSE),
 shot(26, "Then the drum spins up to fourteen hundred times a minute,",
      f"{MACHINE} shaking a little on the floor, its round glass door showing the drum blurred with very fast spin "
      "lines.",
      LAUNDRY_NEW,
      "the drum spinning very fast",
      "any numbers or letters",
      colour=C_SPIN),
 shot(27, "and flings the water out through tiny holes.",
      "Close view of the curved metal wall of the spinning drum covered in tiny holes: water drops shoot out through "
      "the holes in straight lines, flung outward.",
      "inside a washing machine; the close view of the drum wall fills the frame",
      "water drops flying out through the drum's tiny holes",
      "any letters",
      colour=C_DROPS),
 shot(28, "An hour or two later, it beeps. Done.",
      f"{MACHINE} gives a little beep (three small sound lines); {YOU} opens the round door and pulls out an armful of "
      "clean, fresh clothes, smiling.",
      LAUNDRY_NEW,
      "the machine beeping and the young man pulling out clean clothes",
      "any letters or numbers",
      colour=C_CLEAN),
 shot(29, "Back then, a whole Monday and sore hands.",
      f"{WOMAN} sits on an upturned bucket beside {MANGLE} at sunset, rubbing her sore red hands, exhausted; the "
      "full washing line hangs behind her.",
      YARD + ", at sunset",
      "the exhausted woman with sore hands after the whole wash day",
      "any modern thing",
      colour=C_HANDS),
 shot(30, "Now? One button.",
      f"Close view: one stick-figure finger presses the round button of {MACHINE}, with a big tick mark beside it.",
      LAUNDRY_NEW + "; the close view of the machine's front fills most of the frame",
      "one finger pressing the button",
      "any letters or numbers",
      colour=C_BUTTON),
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
