"""Image prompts for knockerup-alarm-then-now, written as one story (channels/SHORTS_RULES.md "How image prompts are
written"; worked example: ../tooth-key-then-now/scenes.py). Checks every line against script.md; this file approves the
script (no approval step) and writes scene + full prompt for every line into script.json.
usage: python channels/what-happens-now/videos/knockerup-alarm-then-now/scenes.py"""
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
KNOCKER = ("a knocker-upper (a stick-figure man in a long dark overcoat, a flat cap and a scarf, carrying a very long "
           "thin bamboo pole that reaches above his head to upstairs windows)")
POLE = "a very long thin bamboo pole"
SLEEPER = ("a factory worker (a stick-figure man with messy hair in a plain long nightshirt)")
WORKER_DAY = ("a factory worker (a stick-figure man in a flat cap, a work jacket and trousers)")
WOMAN = ("a woman knocker-upper (a stick-figure woman in a long skirt, a shawl over her shoulders and a cloth cap, "
         "holding a long thin tube to her mouth)")
MINER = "a coal miner (a stick-figure man in a work jacket and a cloth cap, with a lamp on his cap)"
SLATE = "a small black slate board hung on the brick wall beside a front door"
LANTERN = "a small oil lantern"
STREET = ("a street of brick terraced houses around nineteen hundred: a long row of narrow two-storey houses with front "
          "doors on the pavement and small upstairs bedroom windows, cobblestones, gas street lamps, and tall factory "
          "chimneys behind the roofs")
BEDROOM_OLD = ("a small upstairs bedroom around nineteen hundred: a plain iron bed with a blanket, a small window, a "
               "wooden chair, bare floorboards")
MILL = ("the gate of a big brick cotton mill around nineteen hundred: tall iron gates, a brick wall, and a big round "
        "clock on the wall above the gate")
SHOP = "the front window of a small clock shop around nineteen hundred, with clocks on a shelf behind the glass"
MINING_STREET = ("a street of small stone miners' cottages in a mining town around nineteen hundred, with the tall "
                 "wheel of a coal mine shaft behind the roofs")
# now
YOU = "a stick-figure young man (short spiky hair)"
BEDROOM_NEW = ("a modern bedroom: a bed with a duvet and pillows, a small bedside table with a lamp, a window with "
               "curtains")
PHONE = "a smartphone (a flat rectangle with a plain screen)"
PHONE_CUT = ("a cut-away view of a smartphone, as if its back were see-through: a green circuit board with tiny chips, "
             "a battery, and one tiny crystal (a little silver oval can)")
CRYSTAL = "the tiny crystal (a little silver oval can on the circuit board)"
CHIP = "a small square black chip with short legs on the circuit board"
TOWER = "a tall mobile phone tower with antennas at the top"
# ---- the one coloured thing per picture (settings.json "colour_subject") ----
C_DAWN = "the sky before dawn: flat deep blue, with the factory chimney smoke flat grey"
C_KNOCKER = "the knocker-upper's long coat: flat dark green"
C_POLE = "the bamboo pole: flat light yellow-green"
C_CLOCK = "the big mill clock: flat white face with a flat gold rim"
C_TAG = "the price tag: flat bright red, and the coins flat copper brown"
C_TWO_CLOCKS = "the two clocks: flat gold cases"
C_COINS = "the coins: flat copper brown"
C_LAMPS = "the gas lamps' glow: flat warm yellow"
C_WINDOW = "the upstairs window glass: flat pale blue"
C_TAP = "the tap lines where the pole hits the glass: flat bright yellow"
C_SLEEPER = "the sleepy man's nightshirt: flat pale blue"
C_WOMAN = "the woman's shawl: flat deep red"
C_PEAS = "the dried peas flying at the window: flat bright green"
C_SLATE = "the slate: flat dark charcoal grey, with the chalked time flat white"
C_LANTERN = "the lantern's light: flat warm yellow glow"
C_PHONE = "the phone: flat dark blue"
C_CRYSTAL = "the tiny crystal: flat bright silver, with a few flat yellow sparkle lines"
C_SHAKE = "the tiny crystal: flat bright silver, with flat yellow shake lines"
C_SPARK = "the little spark of electricity: flat bright yellow"
C_CHIP = "the tally marks: flat bright orange"
C_HANDS = "the clock face: flat white with flat red hands"
C_WAVES = "the signal waves: flat light blue"
C_MATCH = "the two clock faces showing the same time: flat white with flat red hands"
C_DARK = "the dark night outside the window: flat deep navy blue"
C_COUNTER = "the chip's counting tally marks: flat bright orange"
C_SCREEN = "the phone's lit-up screen: flat bright yellow glow"
C_RING = "the alarm sound lines: flat bright red"
C_SNOOZE = "the small curved clock arrow: flat light blue"
C_POCKET = "the tiny crystal glowing inside the phone in his pocket: flat bright silver with flat yellow glow lines"
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
 shot(1, "In nineteen hundred,",
      "Wide view of the street before dawn, every window dark, smoke drifting from the factory chimneys, a few stars.",
      STREET,
      "the row of terraced houses and factory chimneys before dawn",
      "any modern thing, any cars",
      colour=C_DAWN),
 shot(2, "your alarm clock was a person.",
      f"{SLEEPER} lies asleep in the iron bed; on the small wooden chair beside the bed, where an alarm clock would "
      f"stand, a tiny {KNOCKER[2:]} stands, no bigger than a clock, holding his pole.",
      BEDROOM_OLD,
      "a little knocker-upper standing beside the bed in place of an alarm clock",
      "an alarm clock, a phone",
      colour=C_KNOCKER),
 shot(3, "And they tapped on your bedroom window with a long stick.",
      f"{KNOCKER} stands on the pavement and reaches {POLE} up to tap on a small upstairs bedroom window of one of "
      "the houses.",
      STREET + ", before dawn",
      "the knocker-upper tapping an upstairs window with the long pole",
      "a ladder, any modern thing",
      colour=C_POLE),
 shot(4, "Factory workers had to be on time.",
      f"Several stick-figure factory workers in flat caps and work jackets hurry through the mill gates; above the "
      "gate the big round clock shows almost six o'clock.",
      MILL,
      "the workers rushing in under the big mill clock",
      "any numbers or letters on the clock",
      colour=C_CLOCK),
 shot(5, "But clocks were expensive,",
      f"{WORKER_DAY} looks into the clock shop window at a clock with a big price tag hanging from it, then down at "
      "two small coins in his open hand, sad.",
      SHOP + ", on a brick street",
      "the expensive clock and the worker with too few coins",
      "any numbers or letters on the tag",
      colour=C_TAG),
 shot(6, "and not always right.",
      "Two old mantel clocks stand side by side on a wooden shelf, their hands pointing to clearly different times; "
      "a big question mark floats between them.",
      BEDROOM_OLD,
      "two clocks disagreeing about the time",
      "any numbers or letters",
      colour=C_TWO_CLOCKS),
 shot(7, "So towns had knocker-uppers.",
      "Three knocker-uppers (stick-figure men in long dark overcoats, flat caps and scarves, each carrying a very "
      "long thin bamboo pole) set off in different directions down the dark street.",
      STREET + ", before dawn",
      "several knocker-uppers going out with their long poles",
      "any modern thing",
      colour=C_KNOCKER),
 shot(8, "You paid one a few pennies a week.",
      f"{WORKER_DAY} stands at his front door and drops a few coins into the open palm of {KNOCKER}.",
      STREET + ", in the evening",
      "the worker paying the knocker-upper a few coins",
      "banknotes, any letters",
      colour=C_COINS),
 shot(9, "They'd walk the dark streets before dawn.",
      f"{KNOCKER} walks alone down the dark street under the glowing gas lamps, his pole over his shoulder, stars "
      "and a thin moon above.",
      STREET + ", before dawn",
      "the knocker-upper walking the dark street alone",
      "any other people, any cars",
      colour=C_LAMPS),
 shot(10, "At your house, they lifted a long bamboo pole",
      f"{KNOCKER} stops in front of one house and lifts {POLE} upward with both hands.",
      STREET + ", before dawn",
      "the knocker-upper lifting the long pole at the house",
      "a ladder",
      colour=C_POLE),
 shot(11, "up to your window.",
      f"The tip of {POLE} reaches the small upstairs bedroom window, almost touching the glass; below, {KNOCKER} "
      "stretches up.",
      STREET + ", before dawn",
      "the tip of the pole reaching the upstairs window",
      "a broken window",
      colour=C_WINDOW),
 shot(12, "Tap, tap, tap.",
      "Close view of the upstairs window: the tip of a long thin bamboo pole taps the glass, with three small tap "
      "burst lines.",
      "the brick wall around a small upstairs window before dawn; the close view fills the frame",
      "the pole tapping the window glass",
      "broken glass, any letters",
      colour=C_TAP),
 shot(13, "Some wouldn't leave until they saw you at the window.",
      f"{SLEEPER} opens the upstairs window, yawning and waving sleepily; below, {KNOCKER} waves back and lowers his "
      "pole.",
      STREET + ", before dawn",
      "the sleepy worker at the window and the knocker-upper waving back",
      "any modern thing",
      colour=C_SLEEPER),
 shot(14, "In London, one woman didn't use a stick.",
      f"{WOMAN} stands on the pavement with no pole at all, holding her long thin tube, a small cloth bag at her hip.",
      STREET + ", before dawn",
      "the woman knocker-upper with no stick, holding a long tube",
      "a pole, any likeness of a real person",
      colour=C_WOMAN),
 shot(15, "She shot dried peas at the glass, through a long tube.",
      f"{WOMAN} blows through her long thin tube, aimed up at an upstairs window, and a few small dried peas fly up "
      "and hit the glass with small tap lines.",
      STREET + ", before dawn",
      "the woman shooting dried peas through the tube at the window",
      "a gun, a slingshot, broken glass",
      colour=C_PEAS),
 shot(16, "In one mining town, miners chalked their shift times",
      f"{MINER} stands at his front door and writes on {SLATE} with a piece of chalk.",
      MINING_STREET,
      "the miner chalking on the slate by his door",
      "any readable letters",
      colour=C_SLATE),
 shot(17, "on a slate on the wall,",
      f"Close view of {SLATE}: a simple chalk drawing of a small clock face with its hands at four o'clock.",
      MINING_STREET + "; the close view of the wall fills most of the frame",
      "the slate on the wall with a time chalked on it",
      "any letters or numbers",
      colour=C_SLATE),
 shot(18, "so the knocker-upper knew when to come.",
      f"At night, {KNOCKER} holds up {LANTERN} and reads the slate by the door, nodding.",
      MINING_STREET + ", at night",
      "the knocker-upper reading the slate by lantern light",
      "any letters",
      colour=C_LANTERN),
 shot(19, "Today, your alarm lives in your phone.",
      f"{YOU} sleeps in the bed under the duvet; {PHONE} lies on the bedside table beside him.",
      BEDROOM_NEW,
      "the phone on the bedside table next to the sleeping young man",
      "an old alarm clock, any letters on the screen",
      colour=C_PHONE),
 shot(20, "Inside is a tiny crystal.",
      f"{PHONE_CUT}; a big magnifying circle zooms in on {CRYSTAL}.",
      "a plain bedside table top; the cut-away phone fills most of the frame",
      "the tiny crystal inside the phone",
      "any letters or logos",
      colour=C_CRYSTAL),
 shot(21, "Electricity makes it shake,",
      f"Close view of {CRYSTAL}: a small zigzag spark of electricity runs into it from a thin wire, and small shake "
      "lines appear on both sides of it.",
      "inside a smartphone, a green circuit board; the close view fills the frame",
      "electricity going into the crystal and making it shake",
      "any letters",
      colour=C_SPARK),
 shot(22, "more than thirty-two thousand times a second.",
      f"Close view of {CRYSTAL}, drawn blurred with very many fast shake lines all around it, like it is buzzing.",
      "inside a smartphone, a green circuit board; the close view fills the frame",
      "the crystal shaking incredibly fast",
      "any numbers or letters",
      colour=C_SHAKE),
 shot(23, "A chip counts every shake.",
      f"{CHIP} sits next to {CRYSTAL}; above the chip, a growing pile of small tally marks in bundles of five.",
      "inside a smartphone, a green circuit board; the close view fills the frame",
      "the chip counting each shake with tally marks",
      "any numbers or letters",
      colour=C_CHIP),
 shot(24, "That adds up to seconds,",
      "Bundles of tally marks flow along an arrow into a round clock face, where the thin seconds hand ticks forward "
      "one step.",
      "inside a smartphone, a green circuit board; the clock face fills most of the frame",
      "the counted shakes becoming ticking seconds",
      "any numbers or letters",
      colour=C_HANDS),
 shot(25, "then minutes, then hours.",
      "A round clock face with all three hands, the seconds hand, the minute hand and the hour hand, each with a "
      "small curved arrow showing it moving.",
      "a plain flat white background with a simple table line",
      "the clock with seconds, minutes and hours all turning",
      "any numbers or letters",
      colour=C_HANDS),
 shot(26, "Your phone checks the time with the internet,",
      f"{PHONE} on the bedside table sends curved signal waves out of the window to {TOWER} in the distance.",
      BEDROOM_NEW,
      "the phone sending signal waves to the phone tower",
      "any letters",
      colour=C_WAVES),
 shot(27, "so it stays right.",
      f"{PHONE} with a clock face on its screen stands next to a big tower clock face, both with their hands at "
      "exactly the same time, and a big tick mark between them.",
      "a plain flat white background with a simple table line",
      "the phone's clock matching the big clock exactly",
      "any numbers or letters",
      colour=C_MATCH),
 shot(28, "While you sleep, the phone rests,",
      f"Night: {YOU} sleeps under the duvet, a few small z shapes above him; {PHONE} lies dark on the bedside table, "
      "the moon in the window.",
      BEDROOM_NEW + ", at night",
      "the young man asleep and the phone dark and resting",
      "any letters",
      colour=C_DARK),
 shot(29, "but that counter keeps going.",
      f"{PHONE_CUT}, its screen dark: the chip next to the crystal keeps adding small tally marks, glowing faintly in "
      "the dark.",
      "a dark bedside table at night; the cut-away phone fills most of the frame",
      "the chip still counting inside the sleeping phone",
      "any numbers or letters",
      colour=C_COUNTER),
 shot(30, "When it hits your time, it wakes the phone,",
      f"{PHONE} on the bedside table suddenly lights up, its screen glowing bright in the dark room.",
      BEDROOM_NEW + ", at night",
      "the phone's screen lighting up",
      "any numbers or letters on the screen",
      colour=C_SCREEN),
 shot(31, "and the alarm goes off.",
      f"{PHONE} rings and shakes on the bedside table, big sound lines bursting from it; {YOU} jolts awake, sitting "
      "up with wide eyes and messy hair.",
      BEDROOM_NEW + ", early morning",
      "the alarm ringing and the young man jolting awake",
      "an old alarm clock, any letters",
      colour=C_RING),
 shot(32, "And if you hit snooze, it tries again in a few minutes.",
      f"{YOU} taps the phone's screen with one finger without opening his eyes and flops back onto the pillow; a "
      "small curved clock arrow above the phone shows a few minutes going round.",
      BEDROOM_NEW + ", early morning",
      "the young man hitting snooze and falling back asleep",
      "any numbers or letters",
      colour=C_SNOOZE),
 shot(33, "Back then, a stranger tapping on your glass.",
      f"{KNOCKER} taps a small upstairs window with {POLE} in the dark before dawn.",
      STREET + ", before dawn",
      "the knocker-upper tapping on the window",
      "any modern thing",
      colour=C_POLE),
 shot(34, "Now? A crystal in your pocket.",
      f"{YOU}, now dressed in a plain T-shirt and jeans, walks out of his front door; the phone in his jeans pocket "
      "is drawn as if see-through, with the tiny crystal inside it glowing.",
      "the front door of a modern house: a small porch, a path, a tree, morning sun",
      "the young man heading out with the crystal glowing inside the phone in his pocket",
      "any knocker-upper, any letters",
      colour=C_POCKET),
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
