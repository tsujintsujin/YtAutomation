"""Image prompts for doorstop-computer-hammer, written as one story (channels/SHORTS_RULES.md "How image prompts are
written"; worked example: ../nail-sandwich-nugget-declaration/scenes.py). Checks every line against script.md; once the
script is approved (right away: no approval step, this file approves it) writes scene + full prompt for every line into script.json.
usage: python channels/found-rich/videos/doorstop-computer-hammer/scenes.py"""
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent                 # videos/<slug>
ROOT = HERE.parents[3]                                 # YtAutomation
sys.path.insert(0, str(ROOT))
from dashboard import approve, short_lines, short_prompt       # the script's lines, and the fixed frame around every prompt

STYLE = json.loads((HERE.parents[1] / "settings.json").read_text(encoding="utf-8"))["image_style"]
TOTAL = 35

# ---- the same words every time a person, object or place appears ----
FARMER = "a stick-figure farmer with a flat cap, a waxed jacket and tall rubber boots"
FRIEND = ("a stick-figure older man with a white moustache and a woolly hat, with headphones round his neck and a metal "
          "detector (a long pole with a handle at the top and a round flat disc at the bottom)")
HAMMER = "a plain old claw hammer with a wooden handle"
FIELD = ("a wide ploughed field in Suffolk, England: long rows of dark furrows, a hedge along the edge, a wooden gate, a "
         "few tall trees, a small church tower far off, a grey cloudy sky")
COINS = ("small round old Roman coins, each with a tiny outline of an emperor's head wearing a leaf crown (no letters); "
         "black ink lines only, no colour")
TREASURE = (f"a heap of treasure: long thin silver spoons, gold chains and bracelets, and thousands of {COINS}; black "
            "ink lines only, no yellow, no gold colour")
MAZ = "a stick-figure man with a grey beard, a baseball cap and a checked flannel shirt"
ROCK = ("a heavy lumpy rock about the size of a loaf of bread, its surface covered in small smooth dents like thumb "
        "prints, drawn with simple outline lines and small dots, no shading, no colour")
BARN = ("his old wooden barn in Michigan: big double wooden doors, a small hayloft window above, a tractor tyre "
        "leaning on the wall, flat farm fields and a few trees around")
OLD_FARMER = "a stick-figure old farmer with a straw hat and bib overalls"
LAB = ("a university geology lab: long lab benches, trays of rock samples, a microscope, a tall window looking out on "
       "a campus lawn and a brick building")
GEOLOGIST = "a stick-figure woman geologist with glasses, a white lab coat and her hair in a long braid"
WOMAN = "a stick-figure older woman with short white hair, a cardigan, and reading glasses on a chain round her neck"
GARAGE = ("her garage in California: shelves of dusty cardboard boxes, an old bicycle, a workbench, the big garage door "
          "open onto a sunny driveway with a palm tree")
RECYCLE = ("an electronics recycling center: a big warehouse with stacks of old TVs, computer screens and keyboards, "
           "cardboard boxes on wooden pallets, a forklift, a drop-off counter at the front")
WORKER = "a stick-figure recycling worker in a safety vest with reflective stripes and thick work gloves"
APPLE1 = ("a very old home computer from the 1970s: a bare flat circuit board with rows of small rectangular chips, "
          "set inside a plain wooden box, with a separate old typewriter-style keyboard beside it; no logo, no fruit "
          "symbol, no letters")
CAPTIONS = ("The place fills the whole frame; keep the very top and very bottom of the frame calm (sky, wall or floor) "
            "for captions. Never write any name, label or caption under or beside anyone or anything.")


def shot(n, text, what, place, must, never=""):
    return n, text, " ".join(x for x in (
        f"This is picture {n} of {TOTAL} in one continuous picture story; draw exactly this moment.",
        what, f"Place: {place}.", f"It MUST show: {must}.", f"NEVER: {never}." if never else "", CAPTIONS) if x)


S = [
 shot(1, "A farmer lost his hammer in a field.",
      f"{FARMER} stands in the field patting his empty jacket pockets with a puzzled face. Behind him, half hidden in a "
      f"furrow, lies {HAMMER}; he hasn't seen it.",
      FIELD,
      "the farmer searching his empty pockets, and the hammer hidden in the furrow behind him",
      "any treasure, any money, any metal detector"),
 shot(2, "Looking for it made two friends rich.",
      f"{FARMER} and {FRIEND} stand side by side in the field, grinning, as banknotes with \"£\" symbols rain down on "
      "them; each catches a fan of cash.",
      FIELD,
      "the two friends in the field getting rich, cash raining down",
      "any treasure or coins showing, any letters"),
 shot(3, "But first, two other ordinary things",
      f"Two plain things side by side, each with a big question mark above it. Left: {ROCK}, propping open a wooden "
      f"barn door. Right: a dusty cardboard box of old electronics with tangled cables and an old keyboard sticking "
      "out. Nobody is in the picture.",
      "left half: the doorway of an old wooden barn; right half: a concrete garage floor",
      "the plain rock holding a door open and the dusty box of old electronics, with question marks",
      "any person, any money, any glow"),
 shot(4, "that weren't ordinary at all.",
      f"The same two things in the same places, now shining: {ROCK} by the barn door and the cardboard box of old "
      "electronics both give off bright light rays and sparkle marks, with small \"$\" symbols floating up from them.",
      "left half: the doorway of an old wooden barn; right half: a concrete garage floor",
      "the same rock and box, now glowing like treasure",
      "any person"),
 shot(5, "A man in Michigan used a heavy rock",
      f"{MAZ} lifts {ROCK} with both hands, straining a little, with sweat drops; shown from head to feet.",
      BARN,
      "the bearded man in a cap lifting the heavy lumpy rock",
      "any glow, any money"),
 shot(6, "to hold a door open.",
      f"{ROCK} sits on the ground propping open one of the big barn doors; {MAZ} walks through the doorway carrying a "
      "bucket.",
      BARN,
      "the rock used as a doorstop for the barn door",
      "any glow, any money"),
 shot(7, "He'd had it for about thirty years.",
      f"{ROCK} still propping open the barn door, with a few weeds grown up around it and cobwebs in the door corner. "
      "On the barn wall hangs a calendar with many of its pages flying off through the air.",
      BARN,
      "the same rock by the door and the calendar pages flying: many years passing",
      "any person, any money"),
 shot(8, "The farmer who sold him the land said",
      f"{OLD_FARMER} stands beside {MAZ} in front of the barn, pointing up at the sky with one hand and at {ROCK} with "
      "the other, telling a story.",
      BARN,
      "the old farmer telling the man about the rock, pointing at the sky",
      "any letters"),
 shot(9, "it fell from the sky back in the nineteen thirties.",
      f"Long ago, at night: {ROCK}, glowing hot with a long fiery tail of streak lines, falls out of the starry sky "
      "toward the same farm fields. An old farmhouse with a lit window below.",
      "the same Michigan farm fields long ago at night: a dark starry sky, an old farmhouse, a wooden fence",
      "the rock falling from the night sky with a fiery tail toward the farm",
      "any modern thing, any letters"),
 shot(10, "In twenty eighteen,",
      f"{MAZ} carries {ROCK} toward his old pickup truck; on the barn wall hangs a calendar showing \"2018\".",
      BARN,
      "the man carrying the rock to his truck, and 2018 on the calendar",
      "any other letters"),
 shot(11, "he finally took it to a university.",
      f"{MAZ} sets {ROCK} down on a lab bench in front of {GEOLOGIST}, who leans over it with interest.",
      LAB,
      "the man handing the rock over to the geologist on the lab bench",
      "any letters"),
 shot(12, "It was a real meteorite,",
      f"{GEOLOGIST} studies {ROCK} through a big magnifying glass, eyebrows high, mouth an O. {MAZ} leans in beside her.",
      LAB,
      "the geologist amazed, examining the same rock",
      "any letters"),
 shot(13, "a rock from space.",
      f"{ROCK} floating in dark space among many stars, with a big round planet Earth (outline of continents, no "
      "colour) behind it and a small moon at one side.",
      "outer space: black sky full of stars, the planet Earth, a small moon",
      "the same lumpy rock floating in space with Earth behind it",
      "any person, any letters"),
 shot(14, "It was valued at about a hundred thousand dollars.",
      f"{ROCK} on the lab bench next to a stack of banknotes with a \"$\" on top, as tall as the rock is wide many "
      f"times over. {MAZ}'s jaw drops; {GEOLOGIST} smiles.",
      LAB,
      "the rock, the stack of cash and the man's shock",
      "any auction, any letters"),
 shot(15, "Then a woman in California cleared out her garage",
      f"{WOMAN} carries a cardboard box out of the garage toward the driveway; more boxes are stacked by the door.",
      GARAGE,
      "the older woman carrying boxes out of her garage, the palm tree outside",
      "any letters"),
 shot(16, "and dropped some old electronics at a recycling center.",
      f"{WOMAN} sets a cardboard box of old electronics (tangled cables, an old keyboard poking out) on the drop-off "
      f"counter; {WORKER} reaches for it.",
      RECYCLE,
      "the woman handing the box of old electronics to the worker at the counter",
      "any logo or letters"),
 shot(17, "She didn't leave her name.",
      f"{WOMAN} walks away out of the big warehouse door with a little wave. At the counter, {WORKER} holds up a "
      "blank paper form with an empty line on it and a pen, looking after her.",
      RECYCLE,
      "the woman leaving and the worker holding a blank form",
      "any readable letters"),
 shot(18, "Inside one box was an Apple One,",
      f"{WORKER} opens the cardboard box on a workbench and lifts out {APPLE1}; his eyes go wide.",
      RECYCLE,
      "the worker finding the old computer inside the box",
      "any logo, any fruit symbol, any letters"),
 shot(19, "one of the very first Apple computers.",
      f"{APPLE1}, drawn big in the middle of the frame on a workbench, with sparkle marks and light rays around it.",
      f"{RECYCLE}; only the workbench and stacks of old screens show behind",
      "the very old computer board in its wooden box with its keyboard, like a treasure",
      "any logo, any fruit symbol, any letters, a modern computer"),
 shot(20, "Only about fifty are left.",
      f"A long glass museum case, mostly empty, with only three copies of {APPLE1} far apart inside it, each under a "
      "small spotlight.",
      "a quiet museum hall: a long glass case, a plain wall, a polished floor",
      "the long, mostly empty case with only a few of the old computers: they are rare",
      "any person, any logo or letters"),
 shot(21, "The recycling company sold it for two hundred thousand dollars,",
      f"{WORKER} cheers with both arms up beside a laptop on the counter that shows \"$200,000\" big and a photo of "
      f"{APPLE1}. A tall stack of banknotes with \"$\" stands beside it.",
      RECYCLE,
      "the same worker cheering, $200,000 on the laptop, the cash",
      "any logo or letters"),
 shot(22, "and they wanted to give her half.",
      f"{WORKER} stands at the warehouse door holding out half of the stack of banknotes, looking left and right down "
      "the empty street for the woman.",
      f"{RECYCLE}; the open warehouse door and an empty sunny street with palm trees outside",
      "the worker holding out half the money, looking for the woman who is not there",
      "the woman, any letters"),
 shot(23, "Now, the hammer.",
      f"{HAMMER}, lying alone in a ploughed furrow in the middle of the frame, with a spotlight cone shining on it.",
      f"{FIELD}; only the furrows close by and the hedge behind",
      "the same plain hammer lying in the field under a spotlight",
      "any person, any treasure"),
 shot(24, "In nineteen ninety-two,",
      "Wide view of the ploughed field; a small calendar hangs on the wooden gate post showing \"1992\".",
      FIELD,
      "the field and 1992 on the calendar on the gate post",
      "any other letters, any treasure"),
 shot(25, "a farmer in England lost his hammer in a field.",
      f"{FARMER} walks slowly along the furrows, bent over, searching the ground and scratching his head.",
      FIELD,
      "the same farmer searching the field for his hammer",
      "the hammer in his hand, any treasure"),
 shot(26, "He asked his friend to find it with a metal detector.",
      f"{FRIEND} arrives at the gate and puts on his headphones, holding his metal detector; {FARMER} points out over "
      "the field.",
      FIELD,
      "the friend with the metal detector and the farmer pointing at the field",
      "any treasure yet"),
 shot(27, "First, his friend found silver spoons",
      f"{FRIEND} sweeps the metal detector over a furrow; beep lines come out of it. He kneels and lifts a few long "
      "thin silver spoons out of the dirt.",
      FIELD,
      "the friend digging up silver spoons with the detector beeping",
      "any coins yet, any colour"),
 shot(28, "and gold jewellery.",
      f"{FRIEND} holds up gold chains and bracelets dangling from his fingers, with sparkle marks; black ink lines only, "
      f"no yellow. {FARMER} runs over.",
      FIELD,
      "the gold chains and bracelets held up out of the dirt",
      "any colour"),
 shot(29, "Then thousands of Roman coins.",
      f"A big spill of {COINS} pours out of the dark dirt in the furrow, piling up; {FRIEND} and {FARMER} kneel beside "
      "it with mouths open.",
      FIELD,
      "thousands of old coins spilling out of the ground",
      "any colour, any letters"),
 shot(30, "It was the biggest pile of Roman gold and silver",
      f"Inside a white tent at the edge of the field, long tables are covered with {TREASURE}; experts in white gloves "
      "lay it out in rows.",
      f"{FIELD}; a white tent with its side open, standing at the edge of the field",
      "the huge amount of treasure laid out on tables",
      "any colour, any letters"),
 shot(31, "ever found in Britain.",
      "A big outline map of Britain (England, Scotland and Wales) drawn on old paper, with one big star on the east "
      "side of England where the field is, and a small pile of treasure drawn next to the star.",
      "a wooden table with the old paper map spread out on it",
      "the map of Britain with the star on the find spot",
      "any letters, any other countries"),
 shot(32, "The finder got one point seven five million pounds,",
      f"{FRIEND} stands in the field beside a tall stack of banknotes with a \"£\" symbol on top, taller than he is, "
      "grinning.",
      FIELD,
      "the same friend with the huge stack of cash with £",
      "any letters"),
 shot(33, "and he shared it with the farmer.",
      f"{FRIEND} splits the stack of banknotes into two equal piles and pushes one toward {FARMER}; they shake hands.",
      FIELD,
      "the cash split into two equal piles, the two friends shaking hands",
      "any letters"),
 shot(34, "And yes, they found the hammer too.",
      f"{FARMER} holds {HAMMER} high above his head, laughing; {FRIEND} laughs beside him, the metal detector over his "
      "shoulder.",
      FIELD,
      "the farmer holding up the found hammer, both laughing",
      "any treasure in the picture, any letters"),
 shot(35, "What's the luckiest thing you've ever lost?",
      "A friendly stick figure faces the viewer at the edge of a field, holding out empty hands in a shrug with a "
      "curious grin; a big question mark floats above.",
      FIELD,
      "the stick figure shrugging with empty hands, and the question mark",
      "any letters"),
]

lines = short_lines((HERE / "script.md").read_text(encoding="utf-8"))
assert len(S) == TOTAL and [(i, t) for i, t, _, _ in lines] == [(n, t) for n, t, _ in S], "scenes.py and script.md differ"
p = HERE / "script.json"
if not p.exists():
    print(approve(HERE.name)["message"])            # no approval step (Justin, 2026-10-19)
data = json.load(open(p, encoding="utf-8"))
segs = data["segments"]
assert len(segs) == TOTAL
for seg, (n, text, scene) in zip(segs, S):
    assert seg["id"] == n and seg["text"] == text, (n, seg["text"], text)
    seg["scene"] = scene
    seg["prompt"] = short_prompt(scene, STYLE)
json.dump(data, open(p, "w", encoding="utf-8"), indent=1, ensure_ascii=False)
print("written", len(segs), "longest", max(len(s["prompt"]) for s in segs), "shortest", min(len(s["prompt"]) for s in segs))
