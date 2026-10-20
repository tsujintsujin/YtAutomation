"""Image prompts for picasso-cup-hoard, written as one story (channels/SHORTS_RULES.md "How image prompts are written";
worked example: ../nail-sandwich-nugget-declaration/scenes.py). Checks every line against script.md; once the script
is approved (right away: no approval step, this file approves it) writes scene + full prompt for every line into script.json.
usage: python channels/found-rich/videos/picasso-cup-hoard/scenes.py"""
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent                 # videos/<slug>
ROOT = HERE.parents[3]                                 # YtAutomation
sys.path.insert(0, str(ROOT))
from dashboard import approve, short_lines, short_prompt       # the script's lines, and the fixed frame around every prompt

STYLE = json.loads((HERE.parents[1] / "settings.json").read_text(encoding="utf-8"))["image_style"]
TOTAL = 42

# ---- the same words every time a person, object or place appears ----
TERRY = ("a stick-figure man with round glasses, a baseball cap, big headphones over the cap and a padded work vest")
DETECTOR = ("a metal detector: a long pole with an armrest, a small control box near the handle and a flat round coil "
            "at the bottom")
FIELD = ("a big ploughed farm field in the English Midlands: long straight rows of turned-over soil, a hedge along the "
         "edge, a red-brick farmhouse at one side, and far off on the horizon a cathedral with three tall pointed "
         "spires")
FARMER = "a stick-figure farmer with a flat cap, a waxed jacket and tall rubber boots"
GOLD = ("Anglo-Saxon gold pieces from long ago: small curved sword-handle fittings and little plates covered in fine "
        "swirling knotwork patterns and tiny inset squares, some bent; black ink lines only, no yellow, no colour")
SWORD = ("an old sword from long ago with a straight blade and a handle decorated with gold fittings covered in fine "
         "swirling knotwork; black ink lines only, no colour")
ZACH = "a stick-figure young man with a knitted beanie hat, a hoodie and a short beard"
POSTER = ("an old framed poster, taller than it is wide, showing a few simple bold shapes of a jug and a round sun, "
          "with a small scribbled signature in one bottom corner; black ink lines only except where the scene says")
THRIFT = ("a thrift store in Ohio: racks of used clothes, shelves of old dishes and toys, a stack of old framed pictures "
          "leaning against a wall, and a till counter by the door")
EXPERT = "a stick-figure art expert with a neat grey bob haircut, glasses on a chain and a dark blazer"
CLIFF = "a stick-figure older man with a white beard, a flat cap and a waxed jacket"
KENT = ("farmland in Kent, England: green fields divided by hedges, a ploughed field, a round brick oast house with a "
        "pointed white cowl on top, a small farmhouse")
CUP = ("a small gold cup about as tall as a hand, with ridged ring-like bands around its sides, a rounded bottom and one "
       "small flat handle riveted on; black ink lines only, no yellow, no colour")
CRUSHED = (f"the same small cup, but crushed and squashed inwards, its ridged sides buckled and dented; black ink lines "
           "only, no yellow, no colour")
FARM_COUPLE = "a stick-figure farm couple: a tall man in a checked shirt and a woman with short grey hair and a fleece"
BRIT_MUSEUM = ("a grand museum hall in London with tall stone columns, a glass ceiling, and a glass display case on a "
               "stand in the middle")
CAPTIONS = ("The place fills the whole frame; keep the very top and very bottom of the frame calm (sky, wall or floor) "
            "for captions. Never write any name, label or caption under or beside anyone or anything.")


def shot(n, text, what, place, must, never=""):
    return n, text, " ".join(x for x in (
        f"This is picture {n} of {TOTAL} in one continuous picture story; draw exactly this moment.",
        what, f"Place: {place}.", f"It MUST show: {must}.", f"NEVER: {never}." if never else "", CAPTIONS) if x)


S = [
 shot(1, "Eight people had already searched a farm field",
      f"Eight different stick figures (caps, beanies, a bobble hat, a sun hat) spread across the field, each sweeping "
      f"{DETECTOR} over the soil.",
      FIELD,
      "exactly eight people with metal detectors searching the same ploughed field",
      "any gold, any letters"),
 shot(2, "and found nothing.",
      "The same eight stick figures walk off the field towards the hedge, shoulders slumped, shrugging, holding their "
      "metal detectors and empty hands up.",
      FIELD,
      "eight people leaving the field empty-handed and disappointed",
      "any gold, any letters"),
 shot(3, "Then one more man tried,",
      f"{TERRY} steps through a gap in the hedge into the empty field, holding {DETECTOR}, smiling hopefully.",
      FIELD,
      "one man arriving alone in the empty field with his metal detector",
      "any gold yet, any letters"),
 shot(4, "and found gold worth over three million pounds.",
      f"{TERRY} stands in the field holding up two handfuls of {GOLD}, sparkle marks around them; beside him rises a "
      "tower of banknotes with \"£\" symbols reaching the top of the frame.",
      FIELD,
      "the man holding up old gold pieces beside a huge tower of pound cash",
      "coins, any letters"),
 shot(5, "But first, two finds",
      f"Two people side by side, a big question mark above each. Left: {ZACH}, holding up {POSTER}. Right: {CLIFF}, "
      f"holding up {CRUSHED}.",
      "a plain town pavement with a low brick wall behind the people and a lamp post at one side",
      "the young man with the framed poster and the older man with the crushed little cup",
      "any money, any letters"),
 shot(6, "that didn't look like much at all.",
      f"The same two people in the same places shrug, unimpressed, looking at their things: {ZACH} with {POSTER}, "
      f"{CLIFF} with {CRUSHED}. A little \"meh\" squiggle line above each head.",
      "a plain town pavement with a low brick wall behind the people and a lamp post at one side",
      "both people unimpressed by their plain-looking finds",
      "any money, any letters"),
 shot(7, "In Ohio, a man bought an old poster",
      f"{ZACH} flips through the stack of old framed pictures leaning against the wall and lifts out {POSTER}.",
      THRIFT,
      "the young man in a beanie pulling the framed poster out of a stack",
      "any shop sign letters"),
 shot(8, "at a thrift store",
      f"Wide view of the thrift store: racks of clothes, shelves of old things, and {ZACH} in the middle holding "
      f"{POSTER} under his arm.",
      THRIFT,
      "the thrift store full of old things and the young man with the poster",
      "any shop name or letters"),
 shot(9, "for fourteen dollars and fourteen cents.",
      f"At the till counter, {ZACH} hands over a few banknotes and coins to a cashier stick figure with curly hair; "
      f"{POSTER} leans on the counter; the till's little screen shows \"$14.14\".",
      THRIFT,
      "the young man paying at the till, $14.14 on the till screen",
      "any other numbers or letters"),
 shot(10, "He thought it was a cheap copy.",
      f"{ZACH} holds {POSTER} out at arm's length with a shrug and a bored face; a thought bubble above him shows a "
      "simple office photocopier pushing out a sheet of paper.",
      "his small apartment: a sofa, a bare wall with a nail in it, a window",
      "the young man thinking the poster is just a cheap printed copy",
      "any letters"),
 shot(11, "It was an ad for a Picasso show",
      f"{POSTER}, drawn big and filling most of the frame, hanging on the apartment wall.",
      "his small apartment: a sofa below the poster, a window at the side",
      "the old poster up close with its simple bold jug and sun shapes",
      "any readable words or names, any famous painting, any colour"),
 shot(12, "from nineteen fifty-eight.",
      f"Close view of the bottom corner of {POSTER}: the edge of the jug shape and, printed small, \"1958\".",
      "his small apartment wall around the frame",
      "the poster's corner with 1958 on it",
      "any letters or names, any number other than 1958"),
 shot(13, "Then he spotted a signature in red.",
      f"Close view: {ZACH}'s finger points at the small scribbled signature in the bottom corner of {POSTER}; the "
      "scribble is the only thing drawn in red; his eye is wide at the edge of the frame.",
      "his small apartment wall around the frame",
      "his finger on the red scribbled signature",
      "any readable name or letters, any other colour"),
 shot(14, "Experts looked at it.",
      f"{EXPERT} bends over {POSTER} laid flat on a table, studying the corner through a big magnifying glass; "
      f"{ZACH} watches nervously.",
      "an art expert's office: a big table with a desk lamp, framed pictures on the walls, tall bookshelves",
      "the expert studying the poster through a magnifying glass",
      "any letters"),
 shot(15, "It wasn't a copy.",
      f"{EXPERT} shakes her head with a smile, holding up a plain sheet of copy paper with a big X crossed through it "
      f"in one hand and pointing at {POSTER} with the other; {ZACH}'s jaw drops.",
      "an art expert's office: a big table with a desk lamp, framed pictures on the walls, tall bookshelves",
      "the expert saying no, it's not a copy",
      "any letters"),
 shot(16, "It was a real print, made by Picasso himself.",
      "Long ago: an old bald artist in a work apron presses a carved flat block onto a sheet of paper on a wooden "
      "press, and lifts the paper to show the same jug and sun shapes printed on it.",
      "a sunny artist's workshop in the south of France long ago: a wooden printing press, carving tools, pots and "
      "jugs on shelves, a window with palm trees",
      "the artist long ago printing the poster by hand from a carved block",
      "any likeness of a real person, any letters"),
 shot(17, "He sold it for seven thousand dollars.",
      f"{ZACH} cheers with both arms up next to {POSTER} on the table and a stack of banknotes with a \"$\" on top.",
      "his small apartment: a sofa, a table, a window",
      "the young man cheering beside the poster and the stack of cash",
      "any letters"),
 shot(18, "Then in England, a man with a metal detector",
      f"{CLIFF} stands at the edge of a field holding {DETECTOR}, headphones round his neck.",
      KENT,
      "the older man with the white beard and flat cap holding his metal detector",
      "any letters"),
 shot(19, "was searching a farm in Kent.",
      f"Wide view of the farmland with the oast house; {CLIFF} small in the middle of a ploughed field, sweeping "
      f"{DETECTOR}.",
      KENT,
      "the Kent farmland with the oast house and the man detecting",
      "any signs or letters"),
 shot(20, "He dug up a small gold cup.",
      f"{CLIFF} kneels by a small hole and lifts {CRUSHED} out of the soil, sparkle marks around it, his eyebrows "
      "up.",
      KENT,
      "the man lifting the crushed little gold cup out of the soil",
      "a whole undamaged cup, any colour, any letters"),
 shot(21, "A plough had crushed it.",
      f"Cut-away view: a tractor pulls a plough across the field; under the soil surface, the plough's blade has "
      f"squashed {CRUSHED}; little impact lines around it.",
      KENT,
      "a plough passing over the field and the cup being crushed under the soil",
      "any person, any letters"),
 shot(22, "Still, it was about three and a half thousand years old.",
      f"Long ago: a Bronze Age stick figure in a fur cloak with long hair holds up {CUP}, whole and perfect, with "
      "both hands.",
      "a Bronze Age settlement long ago: round huts with cone-shaped thatched roofs, a wooden fence, a smoking fire, "
      "gentle hills",
      "a person from long ago holding the same cup, whole and new",
      "any modern thing, any letters"),
 shot(23, "Only a handful of cups like it",
      f"A small row of five copies of {CUP}, each slightly different in shape, standing on a plain cloth, each under a "
      "small spotlight, with empty space all around.",
      "a plain dark gallery wall behind a long low table with a soft cloth",
      "just a few rare gold cups in a row and nothing else",
      "a big crowd of cups, any person, any letters"),
 shot(24, "have ever been found in Europe.",
      f"A simple outline map of Europe (coastlines only) with five tiny drawings of {CUP} dotted on it far apart "
      "from each other.",
      "the map fills the frame on old paper, with a few simple sea waves drawn in the seas",
      "a map of Europe with only a few cups dotted on it",
      "any country names or letters"),
 shot(25, "The British Museum bought it",
      f"{CRUSHED} sits inside the glass display case in the grand museum hall; a museum curator stick figure in a suit "
      f"shakes hands with {CLIFF} beside it.",
      BRIT_MUSEUM,
      "the cup in a glass case in the grand museum, a handshake beside it",
      "any letters or signs"),
 shot(26, "for two hundred seventy thousand pounds.",
      f"{CRUSHED} on a small stand beside a tall stack of banknotes with \"£\" symbols; sparkle marks.",
      BRIT_MUSEUM,
      "the cup beside a tall stack of pound cash",
      "any letters"),
 shot(27, "The finder and the farm's owners split the money.",
      f"{CLIFF} and {FARM_COUPLE} stand in a row in the field, each holding an equal stack of banknotes with \"£\", "
      "smiling.",
      KENT,
      "the finder and the farm owners sharing the money",
      "any letters"),
 shot(28, "Now, the field.",
      "The ploughed field, empty of people, with a single spotlight cone shining down onto one patch of soil.",
      FIELD,
      "the empty ploughed field with a spotlight on one patch",
      "any person, any gold, any letters"),
 shot(29, "In two thousand nine, a man named Terry Herbert",
      f"{TERRY} stands at the field gate holding {DETECTOR}; a small paper calendar pinned to the gatepost shows "
      "\"2009\".",
      FIELD,
      "the man in glasses, cap and headphones at the field gate, 2009 on the calendar",
      "any letters other than 2009, any likeness of a real person"),
 shot(30, "took his metal detector to a farm near Lichfield.",
      f"Wide view: {TERRY} small in the middle of the ploughed field sweeping {DETECTOR}; the farmhouse at one side "
      "and the three-spired cathedral far off on the horizon.",
      FIELD,
      "the man detecting in the wide field, the three-spired cathedral far away",
      "any signs or letters"),
 shot(31, "Eight others had searched that field before him.",
      f"{TERRY} sweeps {DETECTOR} in the field; around him stand eight faint dotted-outline stick figures with metal "
      "detectors, like see-through ghosts of the people who searched there before.",
      FIELD,
      "the man and eight faint dotted ghost figures of earlier searchers",
      "any gold, any letters"),
 shot(32, "Then his detector beeped.",
      f"{TERRY} freezes mid-step; the coil of {DETECTOR} sends up curved sound-wave lines and a small \"!\" from the "
      "soil; his eyes wide behind his glasses.",
      FIELD,
      "the detector beeping and the man freezing",
      "any gold visible yet, any letters"),
 shot(33, "Gold came up out of the dirt.",
      f"{TERRY} kneels and lifts one of {GOLD} out of the dark soil with his fingers, sparkle marks around it.",
      FIELD,
      "the man pulling a patterned gold piece out of the soil",
      "coins, any colour, any letters"),
 shot(34, "He kept digging for five more days.",
      f"{TERRY} digs on his knees with a small trowel beside a growing row of finds; behind him on the gatepost hangs "
      "a paper calendar with five days crossed off with big X marks.",
      FIELD,
      "the man still digging, and five days crossed off on the calendar",
      "any numbers or letters"),
 shot(35, "He found more than fifteen hundred pieces",
      f"A long table covered end to end with trays full of {GOLD}, hundreds and hundreds of small pieces; {TERRY} "
      f"and {FARMER} stand at the end of the table staring.",
      "a farmhouse barn with a long table under bare light bulbs, wooden walls",
      "a whole long table covered in trays of many gold pieces",
      "coins, any letters"),
 shot(36, "of gold and silver.",
      f"Close view of one tray: {GOLD} sitting next to silver pieces of the same kind (drawn with a thinner, lighter "
      "outline), side by side.",
      "a farmhouse barn with a long table under bare light bulbs, only the table top shows",
      "gold and silver pieces side by side up close",
      "coins, any colour, any letters"),
 shot(37, "Lots of them came from old swords.",
      f"{SWORD}, drawn big across the frame, lying on a cloth; its gold handle fittings match the pieces in the trays.",
      "a farmhouse barn with a long table under bare light bulbs, only the table top shows",
      "an old sword with decorated gold handle fittings",
      "any colour, any letters"),
 shot(38, "They were about thirteen hundred years old.",
      f"Long ago: an Anglo-Saxon warrior stick figure in a round iron helmet and a long cloak, holding {SWORD} "
      "upright.",
      "a wooden great hall long ago with a fire pit, carved wooden pillars and round shields on the walls",
      "a warrior from long ago holding the decorated sword",
      "any modern thing, any letters"),
 shot(39, "Two museums paid",
      "Two different museum buildings side by side: one grand with columns and a dome, one smaller red-brick with "
      "tall arched windows; stick figures walking up their steps.",
      "a city square with trees and a paved plaza in front of the two museums",
      "two museums side by side",
      "any names or letters on the buildings"),
 shot(40, "over three point two million pounds for it all.",
      "The same two museum buildings, and between them a tower of banknotes with \"£\" symbols reaching the top of the "
      "frame; sparkle marks.",
      "a city square with trees and a paved plaza in front of the two museums",
      "a giant tower of pound cash between the two museums",
      "any names or letters"),
 shot(41, "Terry and the farmer split it down the middle.",
      f"In the field, {TERRY} and {FARMER} shake hands, each holding an equal tall stack of banknotes with \"£\" in "
      "his other arm, both grinning.",
      FIELD,
      "the finder and the farmer shaking hands, each with an equal half of the cash",
      "any letters"),
 shot(42, "What's under your feet right now?",
      "A friendly stick figure faces the viewer, standing on a garden lawn and looking down at their feet with a "
      "curious grin; a big question mark floats above.",
      "a back garden: a lawn, a flower bed, a wooden fence, a small shed",
      "the stick figure looking down at the ground under their feet, and the question mark",
      "any treasure shown, any letters"),
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
