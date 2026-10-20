"""Image prompts for nugget-hand-cans, written as one story (channels/SHORTS_RULES.md "How image prompts are written";
worked example: ../nail-sandwich-nugget-declaration/scenes.py). Checks every line against script.md; once the script
is approved (right away: no approval step, this file approves it) writes scene + full prompt for every line into script.json.
usage: python channels/found-rich/videos/nugget-hand-cans/scenes.py"""
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent                 # videos/<slug>
ROOT = HERE.parents[3]                                 # YtAutomation
sys.path.insert(0, str(ROOT))
from dashboard import approve, short_lines, short_prompt       # the script's lines, and the fixed frame around every prompt

STYLE = json.loads((HERE.parents[1] / "settings.json").read_text(encoding="utf-8"))["image_style"]
TOTAL = 47

# ---- the same words every time a person, object or place appears ----
COUPLE = ("a stick-figure couple: a man with a bushy grey beard and a checked flannel shirt, and a woman with a wide "
          "sun hat and a long braid down her back")
DOG = "a medium-sized scruffy dog with floppy ears and a waggy tail"
CAN = ("an old round metal can, about as tall as a hand, with a tight lid, dented, its surface covered in small dots "
       "of flaky rust; black ink lines only, no brown, no orange, no colour")
COIN = ("round old gold coins, each with a thin raised rim and a tiny simple outline of an eagle with spread wings in "
        "the middle, no letters or numbers; black ink lines only, no yellow, no gold colour")
LAND = ("hilly rural land in Northern California: rolling grassy hills, big old oak trees with twisting branches, a "
        "dirt path winding uphill, a wooden fence, an odd rock shaped like a horse's saddle beside the path")
BAL_MAN = ("a stick-figure man in a wide-brimmed bush hat, a long-sleeved shirt and big headphones over the hat")
DETECTOR = ("a modern metal detector: a long pole with an armrest, a small control box near the handle and a flat "
            "round coil at the bottom")
BAL_HILLS = ("rolling hills near Ballarat in Australia: tall gum trees with peeling bark and thin drooping leaves, dry "
             "grass, scattered rocks, a pickup truck parked on a dirt track")
NUGGET = ("a big lumpy gold nugget about the size of two fists, with a rough knobbly surface full of little bumps and "
          "dents; black ink lines only, no yellow, no gold colour")
HILLIER = ("a stick-figure man with a big bushy moustache, a baseball cap, a short-sleeved work shirt and shorts")
OLD_DETECTOR = ("an old nineteen-eighties metal detector: a long straight pole, a boxy control case with two round "
                "dials, a round coil at the bottom and a curly cable to a pair of chunky headphones")
KINGOWER = ("dry Australian bush near a small country town: scrubby low trees, bare dirt ground, scattered rocks and "
            "fallen branches, and far off a few small tin-roofed houses and a little church with a pointed roof")
HAND = ("a huge flat gold nugget about as long as a forearm, wide and flat like a slab, with knobbly lumps all along "
        "its edges and a rough bumpy surface; black ink lines only, no yellow, no gold colour")
VEGAS = ("a Las Vegas street at night: tall hotel towers covered in lights drawn as small star bursts, palm trees, "
         "glowing signs made only of shapes and stars with no letters")
CASINO = ("inside a big casino lobby: a patterned carpet, crystal chandeliers, rows of slot machines in the background, "
          "and in the middle a tall glass display case on a pedestal")
CAPTIONS = ("The place fills the whole frame; keep the very top and very bottom of the frame calm (sky, wall or floor) "
            "for captions. Never write any name, label or caption under or beside anyone or anything.")


def shot(n, text, what, place, must, never=""):
    return n, text, " ".join(x for x in (
        f"This is picture {n} of {TOTAL} in one continuous picture story; draw exactly this moment.",
        what, f"Place: {place}.", f"It MUST show: {must}.", f"NEVER: {never}." if never else "", CAPTIONS) if x)


S = [
 shot(1, "A couple saw a rusty can",
      f"{COUPLE} walk along the path with {DOG} on a lead; they stop and both look down at the ground at their feet, "
      "the woman pointing.",
      LAND,
      "the couple and their dog stopping on the path, looking down at something on the ground",
      "any coins or money, any letters"),
 shot(2, "sticking out of the dirt.",
      f"Close view of the dirt path: the top of {CAN} pokes out of the earth at an angle, half buried, a few blades of "
      "grass around it. The dog's nose sniffs at it from the edge of the frame.",
      f"{LAND}; only the dirt path, grass and an oak root show",
      "the rusty can half buried in the dirt",
      "any coins showing, any letters"),
 shot(3, "It led to gold coins",
      f"{CAN} lies tipped on its side on the dirt with its lid off; {COIN} spill out of it in a little stream, sparkle "
      "marks around them.",
      f"{LAND}; only the dirt path, grass and an oak root show",
      "gold coins pouring out of the old rusty can",
      "any colour on the coins, any letters"),
 shot(4, "worth about ten million dollars.",
      f"Big piles of {COIN} on the grass beside a tower of banknotes with \"$\" symbols that reaches the top of the "
      "frame; the rusty can sits in front.",
      LAND,
      "the piles of coins beside a huge tower of cash",
      "any person, any letters"),
 shot(5, "But first, two lumps of gold",
      f"Two gold nuggets side by side on a plain wooden table, a big question mark above each: left, {NUGGET}; right, "
      f"{HAND}, much bigger.",
      "a plain room with a wooden table and a plain wall behind",
      "two gold nuggets, one big and one huge",
      "any coins, any person, any colour, any letters"),
 shot(6, "that were hiding just under the ground.",
      f"A cut-away view of the ground like a slice of cake: grass and a gum tree on top, and in the soil "
      f"layers just below (black ink lines only, no brown), {NUGGET} lying on the left and {HAND} standing upright on its end on the right.",
      "dry Australian bush: gum trees and scattered rocks on the ground above the cut-away",
      "the two nuggets hidden in the soil just under the grass",
      "any person, any colour, any letters"),
 shot(7, "In twenty thirteen, a man was out with a metal detector",
      f"{BAL_MAN} sweeps {DETECTOR} slowly over the dry grass. On the dashboard of the parked pickup truck behind him "
      "sits a small calendar showing \"2013\".",
      BAL_HILLS,
      "the man in the bush hat sweeping his metal detector, 2013 on the calendar",
      "any letters other than 2013"),
 shot(8, "near Ballarat, in Australia.",
      f"Wide view of the hills: {BAL_MAN} small in the middle with {DETECTOR}, gum trees all around, and a kangaroo "
      "standing on its back legs in the distance.",
      BAL_HILLS,
      "the wide Australian gum-tree hills with the small figure detecting and a kangaroo far off",
      "any town signs, any letters"),
 shot(9, "That town had a big gold rush",
      "Long ago: crowds of stick-figure miners with bushy beards and wide floppy hats crouch along a creek swirling "
      "gold pans; others swing picks and push wheelbarrows.",
      "a creek in hilly gum-tree country long ago, with rows of white canvas tents on the banks",
      "a busy gold rush with many miners panning in a creek",
      "any modern thing, any letters"),
 shot(10, "more than a hundred and fifty years ago.",
      "Long ago: a rough gold rush town of canvas tents and wooden huts with tin chimneys, a horse and cart on a muddy "
      "track, miners walking with picks on their shoulders.",
      "a gold rush town in the eighteen fifties among gum-tree hills",
      "an old-time gold rush town from long ago",
      "any modern thing, any letters or dates"),
 shot(11, "People have searched those hills for ages.",
      f"The same gum-tree hills full of people: many stick figures with metal detectors and shovels spread all over "
      "the slopes, digging little holes everywhere.",
      BAL_HILLS,
      "lots of people searching the same hills with detectors and shovels",
      "any gold found, any letters"),
 shot(12, "Then his detector beeped.",
      f"{BAL_MAN} freezes mid-step; the coil of {DETECTOR} sends up curved sound-wave lines and a small \"!\" from the "
      "ground; his eyes go wide.",
      BAL_HILLS,
      "the detector beeping with sound waves and the man freezing",
      "any gold visible yet, any letters"),
 shot(13, "About sixty centimetres down,",
      f"{BAL_MAN} digs with a shovel; the hole is already deep, up to his knees; a pile of dirt beside it; {DETECTOR} "
      "lies on the grass.",
      BAL_HILLS,
      "the man digging a deep hole with a shovel",
      "any gold visible yet, any letters"),
 shot(14, "he dug up a gold nugget.",
      f"{BAL_MAN} kneels by the hole and lifts {NUGGET} out of the dirt with both hands, sparkle marks around it, his "
      "mouth wide open.",
      BAL_HILLS,
      "the man pulling the big lumpy gold nugget out of the hole",
      "any colour, any letters"),
 shot(15, "It weighed five and a half kilos.",
      f"{NUGGET} sits on an old round kitchen scale on a table; the scale's pointer has swung far over and the "
      f"table bends a little; {BAL_MAN} stares at it.",
      "a small farmhouse kitchen: a wooden table, a window with gum trees outside, a kettle on a stove",
      "the heavy nugget on a kitchen scale with the pointer swung far over",
      "any numbers on the scale, any letters, any colour"),
 shot(16, "Experts said it was worth",
      f"A stick-figure gold dealer with a neat beard and a magnifying eyepiece in one eye studies {NUGGET} on the "
      f"counter; {BAL_MAN} waits nervously across the counter.",
      "a small gold shop: a glass counter with small nuggets in it, a set of brass scales, old mining photos on the wall",
      "the gold dealer examining the nugget closely",
      "any money yet, any letters"),
 shot(17, "over three hundred thousand Australian dollars.",
      f"{NUGGET} on the shop counter beside a tall stack of banknotes with \"$\" symbols; {BAL_MAN} throws both arms "
      "up and cheers.",
      "a small gold shop: a glass counter with small nuggets in it, a set of brass scales, old mining photos on the wall",
      "the nugget, the tall stack of cash and the man cheering",
      "any letters"),
 shot(18, "Way back in nineteen eighty,",
      "An old wall calendar showing \"1980\" hangs above a wooden shelf with a big old box-shaped radio and a "
      "chunky dial telephone.",
      "a plain old room with patterned wallpaper",
      "the 1980 calendar and old-fashioned things from that time",
      "any person, any letters other than 1980"),
 shot(19, "another man in Australia was out with his metal detector too.",
      f"{HILLIER} sweeps {OLD_DETECTOR} over the ground, wearing the chunky headphones.",
      KINGOWER,
      "the moustached man in a cap with his old metal detector in the dry bush",
      "any letters"),
 shot(20, "Near a small town called Kingower,",
      f"Wide view: the dry bush with the little town far off; {HILLIER} is small in the middle, detecting.",
      KINGOWER,
      "the dry bush, the small far-off town with its little church, and the man detecting",
      "any signs or letters"),
 shot(21, "it beeped.",
      f"Close view of {OLD_DETECTOR}: the coil on the ground sends up curved sound-wave lines and a small \"!\"; "
      f"{HILLIER}'s hand grips the handle.",
      KINGOWER,
      "the old detector beeping with sound waves",
      "any gold visible yet, any letters"),
 shot(22, "Just thirty centimetres down,",
      f"{HILLIER} kneels and scrapes the dirt away with a small hand trowel; the hole is shallow, only as deep as his "
      "hand.",
      KINGOWER,
      "the man scraping out a shallow hole with a trowel",
      "any gold visible yet, any letters"),
 shot(23, "a huge nugget was standing on its end.",
      f"In the shallow hole, {HAND} sticks straight up on its end out of the dirt, sparkle marks around it; {HILLIER} "
      "falls back on his bottom in shock.",
      KINGOWER,
      "the huge flat nugget standing upright on its end in the hole",
      "the nugget lying flat, any colour, any letters"),
 shot(24, "It weighed about twenty-seven kilos.",
      f"{HILLIER} hugs {HAND} against his chest with both arms, knees bent, straining, sweat drops flying.",
      KINGOWER,
      "the man straining to lift the very heavy nugget",
      "any colour, any letters"),
 shot(25, "It's still the biggest nugget",
      f"{HAND} stands on a plain table, towering over a neat row of small ordinary gold nuggets lined up beside it, "
      "like a giant among pebbles.",
      "a plain room with a wooden table and a plain wall behind",
      "the huge nugget towering over a row of small nuggets",
      "any person, any colour, any letters"),
 shot(26, "ever found with a metal detector.",
      f"{HAND} lies on the table next to {OLD_DETECTOR}; small star shapes burst around the nugget.",
      "a plain room with a wooden table and a plain wall behind",
      "the giant nugget next to the old metal detector that found it",
      "any person, any colour, any letters"),
 shot(27, "A casino in Las Vegas bought it",
      f"Two casino workers in smart waistcoats carry {HAND} on a velvet cushion through the doors of a big casino "
      "hotel, people stopping to stare.",
      VEGAS,
      "the giant nugget being carried into a Las Vegas casino",
      "any person who looks like the finder, any letters or casino names"),
 shot(28, "for over a million dollars.",
      f"{HAND} on its velvet cushion beside a tower of banknotes with \"$\" symbols reaching the top of the frame; "
      "sparkle marks.",
      VEGAS,
      "the giant nugget beside a huge tower of cash",
      "any letters"),
 shot(29, "It's called the Hand of Faith,",
      f"{HAND}, alone in the middle of the frame, with a spotlight cone shining down on it and small sparkle marks.",
      f"{CASINO}; dim behind the spotlight",
      "the huge flat nugget alone under a spotlight",
      "any person, any colour, any letters"),
 shot(30, "and it's still on show there.",
      f"{HAND} stands inside the tall glass display case in the middle of the casino lobby; a few stick-figure "
      "visitors lean in to look at it, one taking a photo with a phone.",
      CASINO,
      "the nugget on show in a glass case in the casino, people looking at it",
      "any letters or signs"),
 shot(31, "Now, the cans.",
      f"{CAN}, alone in the middle of the frame, with a spotlight cone shining down on it.",
      f"{LAND}; dim behind the spotlight",
      "the rusty old can under a spotlight",
      "any coins showing, any person, any letters"),
 shot(32, "In twenty thirteen, a couple in California",
      f"{COUPLE} stand by the wooden fence of their land, the dog sitting at their feet; a mailbox on a post by the "
      "gate shows \"2013\" painted on its side.",
      LAND,
      "the couple on their hilly land with oak trees, and 2013 on the mailbox",
      "any letters other than 2013"),
 shot(33, "were walking their dog on their land.",
      f"{COUPLE} walk up the winding dirt path; {DOG} trots ahead on a lead, past the saddle-shaped rock.",
      LAND,
      "the same couple walking their dog uphill on their land",
      "any can or coins yet, any letters"),
 shot(34, "They spotted an old rusty can",
      f"{DOG} stops and sniffs the ground; the woman from {COUPLE} points down at something, the man leans in.",
      LAND,
      "the dog sniffing and the couple noticing something on the ground",
      "any coins, any letters"),
 shot(35, "poking out of the ground.",
      f"Close view: the top of {CAN} sticking up out of the dirt beside an oak root, half buried.",
      f"{LAND}; only the dirt, grass and the oak root show",
      "the rusty can poking out of the ground",
      "any coins showing, any letters"),
 shot(36, "They pried it loose with a stick.",
      f"The man from {COUPLE} levers {CAN} up out of the dirt with a short stick; clods of dirt fly up; the woman "
      "watches.",
      LAND,
      "the man prying the can out of the ground with a stick",
      "a shovel, any letters"),
 shot(37, "It was heavy.",
      f"The man holds {CAN} with both hands, his arms pulled down by its weight, a surprised face, a few sweat drops.",
      LAND,
      "the small can clearly much heavier than it looks",
      "any coins visible yet, any letters"),
 shot(38, "Inside were gold coins.",
      f"The lid of {CAN} pulled off: inside it is packed with {COIN}; sparkle marks; both faces of {COUPLE} lean over "
      "it, mouths open.",
      LAND,
      "the open can full of gold coins and the couple's amazed faces",
      "any colour, any letters"),
 shot(39, "They went back with tools",
      f"{COUPLE} walk back up the path carrying shovels and {DETECTOR}; {DOG} runs ahead.",
      LAND,
      "the couple coming back with shovels and a metal detector",
      "any letters"),
 shot(40, "and found eight cans in all.",
      f"Eight copies of {CAN} stand in a neat row on the grass beside a freshly dug patch of dirt; the couple kneel "
      "behind them.",
      LAND,
      "exactly eight rusty cans in a row",
      "more or fewer than eight cans, any letters"),
 shot(41, "More than fourteen hundred gold coins,",
      f"A wooden kitchen table completely covered in piles and stacks of {COIN}; {COUPLE} stand at the end of the "
      "table staring.",
      "a farmhouse kitchen: a wooden table, a window with oak-covered hills outside",
      "a whole table covered in many gold coins",
      "any colour, any letters"),
 shot(42, "from the eighteen hundreds.",
      "Long ago: a dusty western town street with a stagecoach pulled by horses, wooden buildings with porches, a man "
      "in a long coat and a wide hat walking past.",
      "a California gold country town in the eighteen hundreds, with hills behind",
      "an old western town from the eighteen hundreds",
      "any modern thing, any letters"),
 shot(43, "Lots of them looked brand new.",
      f"Close view: a few of {COIN} held in fingers, crisp and perfect with sharp rims, sparkle marks all around them.",
      "a farmhouse kitchen: the wooden table and the window softly behind",
      "the coins looking shiny and brand new",
      "worn or scratched coins, any colour, any letters"),
 shot(44, "Nobody knows who buried them.",
      f"Long ago at night: a stick figure in a long coat and a wide hat, face hidden in shadow, digs a hole beside an "
      f"oak tree by the light of a lantern, a row of {CAN} beside him; a big question mark floats above him.",
      "the same oak-covered hills long ago at night, a crescent moon and stars",
      "a mystery person burying the cans at night, face hidden, with a question mark",
      "a visible face, any letters"),
 shot(45, "Experts said they could be worth",
      f"A stick-figure coin expert with round glasses and white cotton gloves studies one of {COIN} through a "
      f"magnifying glass at a desk; the couple watch from the other side.",
      "a coin dealer's office: a desk with a lamp, trays of coins, a safe in the corner",
      "the coin expert studying a coin through a magnifying glass",
      "any money piles yet, any letters"),
 shot(46, "about ten million dollars.",
      f"Piles of {COIN} beside a tower of banknotes with \"$\" symbols reaching the top of the frame; {COUPLE} and "
      f"{DOG} jump for joy.",
      "a coin dealer's office: a desk with a lamp, trays of coins, a safe in the corner",
      "the coins, the huge cash tower, the couple and the dog jumping",
      "any letters"),
 shot(47, "What's buried in your backyard?",
      "A friendly stick figure faces the viewer, leaning on a shovel in a backyard, with a curious grin; a big "
      "question mark floats above a patch of lawn.",
      "a backyard: a lawn, a wooden fence, a small tree, a garden shed",
      "the stick figure with a shovel in a backyard, and the question mark",
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
