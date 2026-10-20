"""Image prompts for vikingcup-helmet-chew, written as one story (channels/SHORTS_RULES.md "How image prompts are written";
worked example: ../nail-sandwich-nugget-declaration/scenes.py). Checks every line against script.md; once the script
is approved (right away: no approval step, this file approves it) writes scene + full prompt for every line into script.json.
usage: python channels/found-rich/videos/vikingcup-helmet-chew/scenes.py"""
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent                 # videos/<slug>
ROOT = HERE.parents[3]                                 # YtAutomation
sys.path.insert(0, str(ROOT))
from dashboard import approve, short_lines, short_prompt       # the script's lines, and the fixed frame around every prompt

STYLE = json.loads((HERE.parents[1] / "settings.json").read_text(encoding="utf-8"))["image_style"]
TOTAL = 41

# ---- the same words every time a person, object or place appears ----
DETECTOR = ("a metal detector: a long pole with an armrest, a small control box near the handle and a flat round coil "
            "at the bottom")
LISA = "a stick-figure woman with a long plait down her back, a beanie hat and a padded winter coat"
ADAM = "a stick-figure man with a shaved head, a short beard and a hi-vis vest over a hoodie"
FIVE = ("five stick-figure friends in winter coats and woolly hats, each holding a brand-new metal detector: one tall, "
        "one short, one with glasses, one with a ponytail, one with a scarf")
BATH_FIELD = ("a muddy ploughed farm field in winter near Bath, England: bare hedges, a wooden field gate, a few bare "
              "trees, rolling hills with a little stone village and a church spire in the distance, a grey sky")
COINS = ("small thin silver pennies from long ago, each with a simple crowned head in side view and a tiny cross on "
         "the back, no letters; black ink lines only, no colour")
LANDOWNER = "a stick-figure farmer with a flat cap, a waxed jacket and rubber boots"
DAVID = "a stick-figure older man with white hair, glasses and a quilted jacket"
ANDREW = "his grown-up son, a stick-figure man with short dark hair, a fleece and a baseball cap"
YORKS = ("a grassy field in North Yorkshire near Harrogate: dry-stone walls, a few big trees, a farmhouse, and far off "
         "the rooftops and church towers of a town")
CUP = ("a round old silver cup, like a deep bowl with a small foot, its sides covered in a pattern of leaves and running "
       "animals; black ink lines only, no colour")
HOARD = ("silver coins, silver arm rings, small silver bars, chopped pieces of silver jewellery and one gold arm ring; "
         "black ink lines only, no yellow, no colour")
SON2 = "a stick-figure young man in his twenties with messy hair and a hoodie"
DAD2 = "his dad, a stick-figure man with a grey moustache, a flat cap and a wax jacket"
CUMBRIA = ("a hilly sheep farm in Cumbria: steep green fells, dry-stone walls running up the hills, grazing sheep, a "
           "small stone barn")
BITS = "dozens of crumpled, broken bits of old bronze metal, bent and dirty, some curved, some flat"
HELMET = ("a Roman rider's helmet: a rounded metal cap with curly hair shapes on top and a small griffin figure on the "
          "crest, joined to a full metal face mask of a calm young man's face with open eye holes and a closed mouth; "
          "black ink lines only, no bronze colour")
AUCTION = ("an auction room: a wooden podium at the front with an auctioneer stick figure in a suit holding a gavel, a "
           "small display stand beside the podium, rows of chairs with stick-figure bidders holding up round paddles")
CAPTIONS = ("The place fills the whole frame; keep the very top and very bottom of the frame calm (sky, wall or floor) "
            "for captions. Never write any name, label or caption under or beside anyone or anything.")


def shot(n, text, what, place, must, never=""):
    return n, text, " ".join(x for x in (
        f"This is picture {n} of {TOTAL} in one continuous picture story; draw exactly this moment.",
        what, f"Place: {place}.", f"It MUST show: {must}.", f"NEVER: {never}." if never else "", CAPTIONS) if x)


S = [
 shot(1, "A couple took five friends out",
      f"{LISA} and {ADAM} lead {FIVE} through the wooden field gate, all carrying metal detectors.",
      BATH_FIELD,
      "a couple leading five friends with new metal detectors into a field: seven people in all",
      "any coins yet, any letters"),
 shot(2, "to teach them metal detecting.",
      f"{LISA} shows the five friends how to sweep {DETECTOR} low over the soil; they copy her, some clumsily.",
      BATH_FIELD,
      "the woman teaching the friends how to use their detectors",
      "any coins yet, any letters"),
 shot(3, "That day, they found coins",
      f"Close view of the muddy soil: {COINS} lie scattered everywhere among the clods, sparkle marks on each.",
      f"{BATH_FIELD}; only the muddy soil and a few boots show",
      "lots of small silver coins scattered in the mud",
      "gold coins, any colour, any letters"),
 shot(4, "worth over four million pounds.",
      f"Piles of {COINS} on the soil beside a tower of banknotes with \"£\" symbols reaching the top of the frame.",
      BATH_FIELD,
      "piles of the coins beside a huge tower of pound cash",
      "any person, any letters"),
 shot(5, "But first, two dads and their sons",
      f"Two pairs side by side, a big question mark above each. Left: {DAVID} and {ANDREW}. Right: {DAD2} and {SON2}. "
      "Each person holds a metal detector.",
      "a plain town pavement with a low brick wall behind the people and a lamp post at one side",
      "two dad-and-son pairs, each with metal detectors",
      "any treasure yet, any letters"),
 shot(6, "who went detecting together.",
      "The same two dad-and-son pairs sweep their metal detectors side by side over a grassy field, smiling at each "
      "other.",
      "a grassy field with a stone wall and a few trees",
      "both pairs detecting together happily",
      "any treasure yet, any letters"),
 shot(7, "In two thousand seven, a father and son",
      f"{DAVID} and {ANDREW} stand at a field gate holding detectors; a small paper calendar pinned to the gatepost "
      "shows \"2007\".",
      YORKS,
      "the white-haired father and his son, 2007 on the calendar",
      "any letters other than 2007"),
 shot(8, "were metal detecting in a field",
      f"{DAVID} and {ANDREW} sweep {DETECTOR} side by side across the grass.",
      YORKS,
      "the father and son detecting together in the field",
      "any treasure yet, any letters"),
 shot(9, "near Harrogate, in England.",
      f"Wide view of the Yorkshire field with stone walls; the father and son small in the middle; the town's rooftops "
      "and church towers far off.",
      YORKS,
      "the wide Yorkshire countryside with the town in the distance",
      "any signs or letters"),
 shot(10, "They dug up an old silver cup.",
      f"{ANDREW} kneels by a hole and lifts {CUP} out of the soil with both hands, clods falling off; {DAVID} leans in.",
      YORKS,
      "the son lifting the old patterned silver cup out of the ground",
      "any colour, any letters"),
 shot(11, "Packed inside were more than six hundred silver coins,",
      f"{CUP} tipped on its side on a cloth; a stream of many small silver coins pours out of it into a big heap.",
      f"{YORKS}; only the cloth on the grass shows",
      "lots of silver coins pouring out of the cup",
      "gold coins, any colour, any letters"),
 shot(12, "plus silver jewellery and a gold arm ring.",
      f"Laid out on the cloth beside the coins: {HOARD}; the gold arm ring in the middle with extra sparkle marks.",
      f"{YORKS}; only the cloth on the grass shows",
      "silver jewellery pieces and one special gold arm ring",
      "any colour, any letters"),
 shot(13, "It had been hidden in Viking times,",
      f"Long ago at dusk: a stick figure in a hooded cloak with a long beard lowers {CUP}, filled with treasure, into "
      "a pit in the ground, looking over his shoulder.",
      "a lonely field long ago at dusk, a wooden longhouse with a turf roof far off, a few trees",
      "a cloaked person from long ago hiding the cup in the ground",
      "horned helmets, any modern thing, any letters"),
 shot(14, "over a thousand years ago.",
      "The same patch of ground, now covered with grass; above it, many calendar pages fly through the air in a long "
      "swirl, and the sky changes from old to new.",
      "a quiet field with stone walls, a big tree",
      "a very long time passing over the buried spot",
      "any person, any letters or numbers"),
 shot(15, "Two museums bought it for over one million pounds.",
      f"Two different museum buildings side by side, a grand one with columns and an old stone one; between them "
      f"{CUP} on a stand beside a tall tower of banknotes with \"£\" symbols.",
      "a city square with trees in front of the two museums",
      "two museums and the cup beside a tall tower of pound cash",
      "any names or letters on the buildings"),
 shot(16, "Then in twenty ten, a young man and his dad",
      f"{SON2} and {DAD2} stand by a stone wall with their detectors; a small paper calendar on the wall shows "
      "\"2010\".",
      CUMBRIA,
      "the young man and his dad with detectors, 2010 on the calendar",
      "any letters other than 2010"),
 shot(17, "were searching a farm in Cumbria.",
      f"Wide view of the steep green fells and stone walls; {SON2} and {DAD2} small in a field among sheep, sweeping "
      "detectors.",
      CUMBRIA,
      "the wide hilly sheep farm with the two detecting",
      "any signs or letters"),
 shot(18, "He dug up dozens of broken bits of bronze.",
      f"{SON2} kneels by a hole and lifts two handfuls of {BITS}; more lie in the hole; his dad stares.",
      CUMBRIA,
      "the young man pulling many broken metal bits out of the ground",
      "a whole helmet yet, any colour, any letters"),
 shot(19, "Put back together,",
      f"In a workshop, a restorer stick figure with magnifying glasses fits {BITS} together like a jigsaw on a stand; "
      "a tube of glue and small tools lie on the bench.",
      "a restorer's workshop: a workbench with a bright lamp, tiny tools, shelves of old pots",
      "the restorer piecing the broken bits back together",
      "any letters"),
 shot(20, "they made a Roman rider's helmet,",
      f"{HELMET}, whole again, standing on a stand in the middle of the frame, drawn big.",
      "a restorer's workshop: a workbench with a bright lamp, tiny tools, shelves of old pots",
      "the finished Roman helmet with its face mask",
      "any colour, any letters"),
 shot(21, "with a full face mask.",
      f"Close view: the calm metal face mask of {HELMET}, filling most of the frame, eye holes open.",
      "only the dark workshop wall behind",
      "the metal face mask up close",
      "a real person's face, any colour, any letters"),
 shot(22, "It was about eighteen hundred years old.",
      f"Long ago: a Roman rider stick figure on a galloping horse, wearing {HELMET} and a short cloak, holding a small "
      "round shield.",
      "a field long ago beside a stone Roman fort with a wooden gate, hills behind",
      "a Roman rider from long ago wearing the face-mask helmet",
      "any modern thing, any letters"),
 shot(23, "Experts guessed it might sell",
      f"An auction expert stick figure in a bow tie studies {HELMET} on a stand, one finger on his chin, thinking.",
      "an auction house viewing room: a velvet-covered stand, a spotlight, paintings on the walls",
      "an expert thinking about what the helmet will sell for",
      "any money yet, any letters"),
 shot(24, "for three hundred thousand pounds.",
      f"Beside {HELMET} on its stand sits a small, short stack of banknotes with a \"£\" on top; the expert points at "
      "it.",
      "an auction house viewing room: a velvet-covered stand, a spotlight, paintings on the walls",
      "the helmet with a small stack of cash: the guess",
      "a big pile of money, any letters"),
 shot(25, "At the auction, it sold for two point three million.",
      f"{AUCTION}. The gavel slams down with impact lines. Beside {HELMET} the small stack of cash is dwarfed by a huge "
      "tower of banknotes with \"£\" symbols reaching the top of the frame; bidders' jaws drop.",
      "the auction room, filling the frame",
      "the gavel and a huge cash tower much bigger than the small guessed stack",
      "any letters"),
 shot(26, "Now, the lesson.",
      f"{DETECTOR}, leaning alone against the field gate, under a spotlight cone.",
      f"{BATH_FIELD}; dim behind the spotlight",
      "a metal detector alone under a spotlight",
      "any person, any coins, any letters"),
 shot(27, "In twenty nineteen, Lisa Grace and Adam Staples",
      f"{LISA} and {ADAM} stand side by side with their detectors at the field gate; a small paper calendar on the "
      "gatepost shows \"2019\".",
      BATH_FIELD,
      "the woman with the plait and the man with the shaved head, 2019 on the calendar",
      "any letters other than 2019, any likeness of a real person"),
 shot(28, "took five friends to a farm field near Bath.",
      f"{LISA} and {ADAM} open the gate and wave {FIVE} into the muddy field.",
      BATH_FIELD,
      "the couple bringing five friends into the winter field",
      "any coins yet, any letters"),
 shot(29, "They were showing them how to use metal detectors.",
      f"{ADAM} stands behind one of the friends, guiding his arms to hold {DETECTOR} correctly; the others watch.",
      BATH_FIELD,
      "the man showing a friend how to hold a metal detector",
      "any coins yet, any letters"),
 shot(30, "Then the beeping started.",
      "All seven people stand spread across the field; curved sound-wave lines rise from every one of their detectors "
      "at once; they look at each other, surprised.",
      BATH_FIELD,
      "all seven detectors beeping at the same time",
      "any coins visible yet, any letters"),
 shot(31, "Silver coins were all over the place.",
      f"All seven kneel in the mud picking up {COINS}, which lie scattered everywhere around them; sparkle marks.",
      BATH_FIELD,
      "everyone picking up coins scattered all over the field",
      "gold coins, any colour, any letters"),
 shot(32, "More than two thousand five hundred of them,",
      f"A long table covered in heaps and neat rows of {COINS}; the seven friends stand around it staring.",
      "a farmhouse kitchen with a long wooden table, a window onto the winter field",
      "a whole table covered in thousands of small silver coins",
      "gold coins, any colour, any letters"),
 shot(33, "from right after the year ten sixty-six,",
      "Long ago: a battle on a green hill, knights on horseback charging at a wall of soldiers with round and kite-"
      "shaped shields; a cloth banner on a pole shows \"1066\".",
      "a hillside long ago with a few trees, a cloudy sky",
      "a famous old battle from 1066",
      "any blood, any letters other than 1066"),
 shot(34, "when England got a new king.",
      "A new king stick figure with a big crown and a long robe sits on a tall wooden throne, holding a sword, as "
      "people bow in front of him.",
      "a stone castle hall long ago with tall narrow windows and banners with simple shapes",
      "a new king on his throne",
      "any likeness of a real person, any letters"),
 shot(35, "Lots of them showed King Harold.",
      "Close view: one small silver penny drawn big, showing a simple side-view head of a bearded king with a "
      "crown; a few more coins like it around it. Black ink lines only, no colour.",
      "a plain dark cloth behind the coins",
      "a coin with a crowned king's head on it",
      "any letters or names, any colour"),
 shot(36, "Lots showed King William, the man who beat him.",
      "Close view: another small silver penny drawn big, showing a different king's head facing forward with a "
      "different crown; behind it, faintly, a knight on horseback raising a sword in victory. Black ink lines only.",
      "a plain dark cloth behind the coin",
      "a second coin with a different king, and the winner of the battle behind it",
      "any letters or names, any colour"),
 shot(37, "A museum trust bought them",
      f"{COINS} laid out in neat rows inside a glass case in a museum; a few visitors look at them.",
      "a museum gallery: glass display cases, a polished floor, soft spotlights",
      "the coins on show in a museum case",
      "any letters or signs"),
 shot(38, "for four point three million pounds.",
      "The glass case of coins beside a tower of banknotes with \"£\" symbols reaching the top of the frame; sparkle "
      "marks.",
      "a museum gallery: glass display cases, a polished floor, soft spotlights",
      "the coins beside a giant tower of pound cash",
      "any person, any letters"),
 shot(39, "Half went to the landowner.",
      f"A big pile of cash split exactly in two: {LANDOWNER} at his field gate happily holds one whole half.",
      BATH_FIELD,
      "the landowner getting half of the money",
      "any letters"),
 shot(40, "The other half was split between all seven friends.",
      f"{LISA}, {ADAM} and {FIVE} stand in a row in the field, each holding an equal small stack of banknotes with "
      "\"£\", cheering.",
      BATH_FIELD,
      "seven friends each with an equal share of the cash",
      "more or fewer than seven people, any letters"),
 shot(41, "Who would you take treasure hunting?",
      "A friendly stick figure faces the viewer, holding a metal detector in one hand and holding out a second "
      "metal detector toward the viewer with the other, with a big grin; a question mark floats above.",
      "a grassy field with a stone wall and a few trees",
      "the stick figure offering the viewer a metal detector, and the question mark",
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
