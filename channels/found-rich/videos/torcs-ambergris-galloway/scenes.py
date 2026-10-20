"""Image prompts for torcs-ambergris-galloway, written as one story (channels/SHORTS_RULES.md "How image prompts are written";
worked example: ../nail-sandwich-nugget-declaration/scenes.py). Checks every line against script.md; once the script
is approved (right away: no approval step, this file approves it) writes scene + full prompt for every line into script.json.
usage: python channels/found-rich/videos/torcs-ambergris-galloway/scenes.py"""
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent                 # videos/<slug>
ROOT = HERE.parents[3]                                 # YtAutomation
sys.path.insert(0, str(ROOT))
from dashboard import approve, short_lines, short_prompt       # the script's lines, and the fixed frame around every prompt

STYLE = json.loads((HERE.parents[1] / "settings.json").read_text(encoding="utf-8"))["image_style"]
TOTAL = 43

# ---- the same words every time a person, object or place appears ----
DEREK = "a stick-figure man with a short dark beard, a woolly bobble hat, a waterproof jacket and walking boots"
MINISTERS = ("two stick-figure ministers wearing small white clerical collars under dark jumpers: one tall with grey "
             "hair and glasses, one short and bald")
DETECTOR = ("a metal detector: a long pole with an armrest, a small control box near the handle and a flat round coil "
            "at the bottom")
SCOT_FIELD = ("a rough grassy field in the Scottish countryside beside a small old stone church with a little bell "
              "tower, a dry-stone wall, rolling green hills, a loch in the distance, sheep grazing")
ARMBAND = ("a flat silver arm band, bent into a gentle curve, with small stamped patterns along it, dirty with soil; "
           "black ink lines only, no colour")
SPOON = "a plain soup spoon"
CROSS = ("a small silver cross with flared arm ends and simple patterns, on a short chain; black ink lines only, no "
         "colour")
HOARD = ("Viking-age treasure: flat silver arm bands, brooches, a small silver cross, glass beads, a little crystal "
         "jar, a gold pin shaped like a bird, and a round lidded silver pot; black ink lines only, no colour")
FRIENDS = ("two stick-figure friends: one tall with a ponytail and a flat cap, one short and round with a big beard and "
           "a camouflage jacket")
STAFFS = ("farmland in the Staffordshire Moorlands, England: green hills with dry-stone walls, grazing sheep, a stone "
          "farmhouse, a ploughed field edge")
FARMER = "a stick-figure farmer with a flat cap, a waxed jacket and rubber boots"
TORC = ("a twisted gold neck ring, a thick ring made of gold strands twisted like a rope, with a gap at the front "
        "and a round knob at each end; black ink lines only, no yellow, no colour")
BRACELET = ("a smaller twisted gold bracelet in the same rope-like twisted style with knob ends; black ink lines only, "
            "no yellow, no colour")
MUSEUM = ("a museum gallery: glass display cases on stands, a polished floor, plain walls, soft spotlights")
FISHERMEN = ("a crew of many stick-figure fishermen in simple wrap skirts, T-shirts and head cloths wrapped around "
             "their heads, some barefoot")
BOATS = ("a few small wooden fishing boats with outboard motors on a calm sea drawn with simple wavy lines, nets "
         "piled in them")
SEA = "the open sea in the Gulf of Aden: gentle waves, a hot sun, a dry rocky coastline far off"
WHALE = ("a huge dead sperm whale floating on its side: a big square-ended head, a long body, small flippers, a wide "
         "tail; black ink lines only, no grey shading")
BEACH = ("a sandy beach in Yemen: dry rocky hills behind, a small town of flat-roofed houses along the shore, wooden "
         "boats pulled up on the sand")
LUMP = ("a big lump of ambergris: a rough, waxy, rounded rock-like lump as big as a sack of rice, with a lumpy "
        "surface; black ink lines only, no colour")
CAPTIONS = ("The place fills the whole frame; keep the very top and very bottom of the frame calm (sky, wall or floor) "
            "for captions. Never write any name, label or caption under or beside anyone or anything.")


def shot(n, text, what, place, must, never=""):
    return n, text, " ".join(x for x in (
        f"This is picture {n} of {TOTAL} in one continuous picture story; draw exactly this moment.",
        what, f"Place: {place}.", f"It MUST show: {must}.", f"NEVER: {never}." if never else "", CAPTIONS) if x)


S = [
 shot(1, "A man with a metal detector",
      f"{DEREK} sweeps {DETECTOR} over the grass, headphones on.",
      SCOT_FIELD,
      "the man in the bobble hat with his metal detector in the field",
      "any treasure yet, any letters"),
 shot(2, "dug up a spoon.",
      f"{DEREK} kneels by a small hole and holds up {ARMBAND}, squinting at it, puzzled.",
      SCOT_FIELD,
      "the man holding up a dirty curved silver thing, puzzled",
      "any other treasure, any letters"),
 shot(3, "At least, he thought it was a spoon.",
      f"{DEREK} holds {ARMBAND}; a thought bubble above his head shows {SPOON}.",
      SCOT_FIELD,
      "the man thinking the silver piece is just an old spoon",
      "any other treasure, any letters"),
 shot(4, "It led to a treasure",
      f"In the hole in the field, {HOARD} spill out of the soil in a heap, sparkle marks around them.",
      SCOT_FIELD,
      "a heap of old gold and silver treasure coming out of the ground",
      "coins, any colour, any letters"),
 shot(5, "worth almost two million pounds.",
      f"{HOARD} piled on the grass beside a tower of banknotes with \"£\" symbols reaching the top of the frame.",
      SCOT_FIELD,
      "the treasure beside a huge tower of pound cash",
      "any person, any letters"),
 shot(6, "But first, two more groups of friends",
      f"Two groups side by side, a big question mark above each. Left: {FRIENDS}, each holding a metal detector and "
      f"a spade. Right: {FISHERMEN} (five of them), standing together holding nets.",
      "a plain town pavement with a low brick wall behind the people and a lamp post at one side",
      "the two detecting friends and a group of fishermen",
      "any money yet, any letters"),
 shot(7, "who got very lucky.",
      "The same two groups in the same places, cheering with arms up as banknotes rain down on them.",
      "a plain town pavement with a low brick wall behind the people and a lamp post at one side",
      "both groups getting lucky, money raining down",
      "any letters"),
 shot(8, "In England, two friends went metal detecting",
      f"{FRIENDS} walk side by side through a field gate, each carrying {DETECTOR} and a small spade, chatting happily.",
      STAFFS,
      "the two friends setting off detecting together",
      "any letters"),
 shot(9, "on a farm in Staffordshire.",
      f"Wide view of the farmland: green hills, stone walls, sheep and the farmhouse; {FRIENDS} small in the middle of "
      "a field, sweeping their detectors.",
      STAFFS,
      "the wide green farm with the two friends detecting",
      "any signs or letters"),
 shot(10, "Just under the ground,",
      f"The detector of the tall friend beeps with sound-wave lines; the short bearded friend digs a small, shallow "
      "hole with his spade, only a hand deep.",
      STAFFS,
      "a beep and a shallow hole being dug",
      "any gold visible yet, any letters"),
 shot(11, "they found three gold rings,",
      f"In the shallow hole lie three copies of {TORC}, half in the soil, a little apart from each other; sparkle "
      "marks; both friends' faces lean over the hole, mouths open.",
      STAFFS,
      "three twisted gold neck rings lying in the soil",
      "more or fewer than three rings, coins, any colour, any letters"),
 shot(12, "big enough to wear around your neck.",
      f"The tall friend holds one {TORC} up around his own neck, grinning; the bearded friend laughs.",
      STAFFS,
      "the twisted gold ring held around a neck: it is a necklace-sized ring",
      "any colour, any letters"),
 shot(13, "Weeks later, they found a gold bracelet too.",
      f"Back in the field, with a little frost on the grass, the bearded friend lifts {BRACELET} out of the soil; a "
      "small calendar in the other friend's hand has pages flying off.",
      STAFFS,
      "the friend finding a smaller twisted gold bracelet weeks later",
      "any colour, any letters"),
 shot(14, "They were over two thousand years old,",
      f"Long ago: an Iron Age woman stick figure with long braided hair and a woven checked cloak, wearing {TORC} "
      "around her neck, standing proudly.",
      "an Iron Age village long ago: round huts with cone-shaped thatched roofs, a wooden fence, a smoking fire, "
      "green hills",
      "a woman from long ago wearing the twisted gold neck ring",
      "any modern thing, any letters"),
 shot(15, "the oldest gold jewellery of their kind",
      f"Three copies of {TORC} and one {BRACELET} laid side by side on a dark cloth under a spotlight cone, sparkle "
      "marks around them.",
      "a dark plain room, only the spotlight on the cloth",
      "the four twisted gold pieces shining together",
      "any person, any colour, any letters"),
 shot(16, "ever found in Britain.",
      "A simple outline map of the island of Great Britain (coastline only) on old paper, with one small star shape "
      f"in the middle of England and a tiny {TORC} drawn beside the star.",
      "the map fills the frame on old paper, with a few simple sea waves drawn around the island",
      "a map of Britain with one star marking where the gold was found",
      "any place names or letters"),
 shot(17, "A museum paid",
      f"Three copies of {TORC} and one {BRACELET} in a glass case in the museum; a few visitors look at them.",
      MUSEUM,
      "the four gold pieces on show in a museum case",
      "any letters or signs"),
 shot(18, "three hundred twenty-five thousand pounds for them.",
      f"The glass case with the gold rings beside a tall stack of banknotes with \"£\" symbols; sparkle marks.",
      MUSEUM,
      "the gold rings beside a tall stack of pound cash",
      "any person, any letters"),
 shot(19, "The friends and the farmer shared the money.",
      f"{FRIENDS} and {FARMER} stand in a row by the field gate, each holding a stack of banknotes with \"£\", "
      "smiling.",
      STAFFS,
      "the two friends and the farmer each with a share of the cash",
      "any letters"),
 shot(20, "Then in Yemen, thirty-five fishermen were out at sea.",
      f"{BOATS}, crowded with {FISHERMEN}, many of them, pulling in nets.",
      SEA,
      "a big crew of fishermen in small wooden boats at sea",
      "any letters or flags"),
 shot(21, "They spotted a dead whale floating.",
      f"{WHALE} floats in the water near the boats; the fishermen point at it from the boats.",
      SEA,
      "the huge dead whale floating and the fishermen pointing",
      "any blood, any letters"),
 shot(22, "It had a strong, nasty smell,",
      f"Wavy smell lines rise from {WHALE}; the fishermen in the nearest boat pinch their noses and lean away.",
      SEA,
      "the whale's strong smell and the men holding their noses",
      "any blood, any letters"),
 shot(23, "and they knew what that might mean.",
      "Three of the fishermen in the boat look at each other with big knowing grins, one raising his eyebrows, still "
      "pinching his nose.",
      f"{SEA}; the whale's tail just visible at the edge of the frame",
      "the men grinning knowingly at each other",
      "any money yet, any letters"),
 shot(24, "They brought it to the beach and cut it open.",
      f"{WHALE} lies on the sand; fishermen stand beside it with long knives, a cut opening in its side; others pull "
      "ropes from the boats.",
      BEACH,
      "the whale on the beach being cut open by the fishermen",
      "any blood or gore, any letters"),
 shot(25, "Inside was a big lump of ambergris.",
      f"Four fishermen lift {LUMP} out of the opening in the whale's side, amazed.",
      BEACH,
      "the men lifting the big waxy lump out of the whale",
      "any blood or gore, any letters"),
 shot(26, "It's a waxy stuff whales make in their gut,",
      f"A simple cut-away drawing of a living sperm whale swimming, its belly shown as a see-through window, with a "
      f"small rounded lump like {LUMP} sitting in its gut.",
      "under the sea: water drawn with a few wavy lines, light rays from above, a few small fish",
      "the lump forming inside a whale's gut",
      "any blood, any letters"),
 shot(27, "and it helps perfume last longer.",
      "A fancy glass perfume bottle with a round squeeze bulb sprays a cloud of scent lines; beside it a small clock, "
      "its hands spinning, shows the scent lasting a long time.",
      "a dressing table with a round mirror and a little vase of flowers",
      "a perfume bottle and a clock: the scent lasting longer",
      "any brand name or letters"),
 shot(28, "They sold it for one and a half million dollars.",
      f"On the beach, a buyer stick figure in a smart suit hands over two open briefcases full of banknotes with \"$\" "
      f"to the fishermen; {LUMP} sits on a cart beside them.",
      BEACH,
      "the lump being sold for briefcases full of cash",
      "any letters"),
 shot(29, "They split it equally,",
      "On a long cloth on the sand, the banknotes are laid out in many equal piles in a long row, one pile in front of "
      "each fisherman sitting along the cloth.",
      BEACH,
      "the money split into equal piles for every fisherman",
      "any letters"),
 shot(30, "and gave some to poor families in their town.",
      "Fishermen walk through the small town of flat-roofed houses handing banknotes to families standing at their "
      "doors; a mother and child smile.",
      "a small Yemeni fishing town: flat-roofed houses, narrow sandy lanes, a few palm trees, the sea at the end of "
      "the lane",
      "the fishermen sharing money with poor families",
      "any letters"),
 shot(31, "Now, the spoon.",
      f"{ARMBAND}, alone in the middle of the frame, under a spotlight cone.",
      "a dark plain room, only the spotlight",
      "the curved silver piece under a spotlight",
      "any person, any other treasure, any colour, any letters"),
 shot(32, "In two thousand fourteen, Derek McLennan",
      f"{DEREK} stands at a field gate holding {DETECTOR}; a small paper calendar pinned to the gatepost shows "
      "\"2014\".",
      SCOT_FIELD,
      "the man in the bobble hat with his detector, 2014 on the calendar",
      "any letters other than 2014, any likeness of a real person"),
 shot(33, "was detecting on church land in Scotland.",
      f"Wide view: {DEREK} small in the field sweeping his detector, the little stone church with its bell tower beside "
      "the field, hills and a loch behind.",
      SCOT_FIELD,
      "the man detecting in a field right beside a small stone church in the Scottish hills",
      "any letters or signs"),
 shot(34, "Two ministers were with him.",
      f"{MINISTERS} sweep their own metal detectors next to {DEREK}, all three chatting.",
      SCOT_FIELD,
      "two ministers in clerical collars detecting with the man",
      "any letters"),
 shot(35, "Then he dug up a piece of silver.",
      f"{DEREK} kneels at a small hole and lifts {ARMBAND} out of the soil; the two ministers lean in.",
      SCOT_FIELD,
      "the man lifting the dirty curved silver piece out of the ground",
      "any other treasure, any colour, any letters"),
 shot(36, "He thought it was a spoon.",
      f"{DEREK} turns {ARMBAND} over in his hands with a shrug; a thought bubble above him shows {SPOON}.",
      SCOT_FIELD,
      "the man thinking it is just a spoon",
      "any other treasure, any letters"),
 shot(37, "It was a silver arm band from Viking times.",
      f"Long ago: a stick-figure man from Viking times with a long braided beard, a round wooden shield and a fur "
      f"cloak, wearing {ARMBAND.replace(', dirty with soil', ', bright and new')} on his upper arm.",
      "a wooden longhouse long ago with a turf roof, a longship on a shore behind, misty hills",
      "a man from Viking times wearing the silver arm band",
      "horned helmets, any modern thing, any letters"),
 shot(38, "They found a silver cross,",
      f"{DEREK} holds up {CROSS} from the widening hole; the two ministers clasp their hands in delight.",
      SCOT_FIELD,
      "the man holding up a small silver cross, the ministers delighted",
      "any colour, any letters"),
 shot(39, "and over a hundred more pieces of gold, silver and glass.",
      f"A long table covered with trays full of {HOARD}, many pieces; {DEREK} and {MINISTERS} stand at the end of the "
      "table staring.",
      "a museum workroom: a long table under bright lamps, shelves with boxes",
      "a whole table covered in trays of many treasure pieces",
      "coins, any colour, any letters"),
 shot(40, "A museum in Edinburgh",
      "A grand old museum building with tall arched windows, and behind it on a high rocky hill a big castle; people "
      "walk on the street in front.",
      "a city street in Edinburgh with old stone buildings",
      "a grand museum with a castle on a rocky hill behind it",
      "any names or letters on the buildings"),
 shot(41, "paid almost two million pounds for it all.",
      f"{HOARD} on a display table beside a tower of banknotes with \"£\" symbols reaching the top of the frame.",
      "inside a grand museum hall with a glass roof and white iron balconies",
      "the treasure beside a giant tower of pound cash",
      "any person, any letters"),
 shot(42, "He agreed to share the money with the church.",
      f"Outside the little stone church, {DEREK} and {MINISTERS} stand together, each holding a stack of banknotes "
      "with \"£\", smiling and shaking hands.",
      SCOT_FIELD,
      "the man sharing the money with the church, outside the church",
      "any letters"),
 shot(43, "What's waiting to be found near you?",
      "A friendly stick figure faces the viewer holding a metal detector in a town park, with a curious grin; a big "
      "question mark floats above.",
      "a town park: a lawn, trees, a bench, a path, houses beyond",
      "the stick figure with a metal detector in a park, and the question mark",
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
