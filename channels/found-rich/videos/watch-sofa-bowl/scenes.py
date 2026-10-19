"""Image prompts for watch-sofa-bowl, written as one story (channels/SHORTS_RULES.md "How image prompts are written";
worked example: ../nail-sandwich-nugget-declaration/scenes.py). Checks every line against script.md; once the script
is approved (right away: no approval step, this file approves it) writes scene + full prompt for every line into script.json.
usage: python channels/found-rich/videos/watch-sofa-bowl/scenes.py"""
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
FAMILY = ("a stick-figure family of three: a dad with glasses and a sweater vest, a mom with her hair in a bun, and a "
          "small girl with two pigtails")
BOWL = ("a small round bowl, about as wide as a hand, with gently sloping sides, a thin smooth rim and a small round "
        "foot underneath; completely plain, no pattern, no picture on it; black ink outline only on the white paper, "
        "no colour")
YARDSALE = ("a yard sale on the front lawn of a two-storey wooden house in New York state, with a porch behind; folding "
            "tables on the grass covered with old things (plates, vases, books, a lamp, a toy truck), a few trees")
YARD_SELLER = "a stick-figure old woman with short white curly hair and a cardigan, sitting on a lawn chair behind the table"
LIVING = ("the family's living room: a brick fireplace with a wooden mantel shelf above it, a framed landscape picture "
          "on the wall above the mantel, a sofa, a window with curtains")
EXPERT = "a stick-figure expert in a neat suit and round glasses, wearing white cotton gloves"
EXPERT_ROOM = ("an expert's viewing room: a table covered with a soft cloth, a desk lamp, shelves of old vases and "
               "bowls behind glass, a tall window with city buildings")
POTTER = ("a stick-figure potter long ago, in a simple long robe with wide sleeves and his hair tied in a small top "
          "knot")
KILN = ("an old pottery workshop in China a thousand years ago: a wooden potter's wheel, rows of drying bowls on "
        "wooden racks, a brick kiln with a chimney, a building with a curved tiled roof, misty mountains behind")
MUSEUM = ("a big quiet museum gallery in London: tall glass cases on stands, a polished floor, a tall window through "
          "which a tall clock tower with a pointed top can be seen")
AUCTION = ("an auction room: a wooden podium at the front with an auctioneer stick figure in a suit holding a gavel, a "
           "small display stand beside the podium, rows of chairs with stick-figure bidders holding up round paddles")
ZACH = "a stick-figure man with short spiky hair, a small goatee and a plain T-shirt"
STORE = ("a Goodwill thrift store in Arizona: racks of used clothes, shelves of old things (cups, toys, books, a golf "
         "bag), a glass display case at the counter, and a big front window showing a tall cactus and bright desert sun")
DIVE_WATCH = ("an old diving wristwatch: a round face with a wide outer ring with tick marks, two hands and a third "
              "thin pointer, two winding knobs on its right side, no numbers and no letters, on a plain strap")
STUDENT = "a stick-figure student with short bobbed hair, a long striped scarf and a backpack"
SOFABED = ("an old plain sofa bed with square cushions, rounded arms and short wooden legs, a little worn")
FLEA = ("an outdoor flea market in Berlin: rows of stalls with old furniture and boxes of junk under simple awnings, "
        "and on the skyline a very tall thin TV tower with a big ball near its top")
FLAT = ("the student's small flat: a bookshelf, a desk with a lamp and a pile of textbooks, a window with a city view "
        "and the same tall thin TV tower with a ball near its top in the distance")
PAINTING = ("a small old oil painting about the size of a sheet of paper, in a plain thin wooden frame, showing a "
            "simple tiny scene of a woman holding a baby and a man loading bags onto a donkey (simple lines)")
CAPTIONS = ("The place fills the whole frame; keep the very top and very bottom of the frame calm (sky, wall or floor) "
            "for captions. Never write any name, label or caption under or beside anyone or anything.")


def shot(n, text, what, place, must, never=""):
    return n, text, " ".join(x for x in (
        f"This is picture {n} of {TOTAL} in one continuous picture story; draw exactly this moment.",
        what, f"Place: {place}.", f"It MUST show: {must}.", f"NEVER: {never}." if never else "", CAPTIONS) if x)


S = [
 shot(1, "A family paid three dollars",
      f"{FAMILY} stand at a yard-sale table; the dad hands three banknotes, each marked \"$1\", to {YARD_SELLER}. "
      f"On the table between them sits {BOWL}.",
      YARDSALE,
      "the family paying three $1 bills, and the small plain bowl on the table",
      "any big money, any shop, any letters"),
 shot(2, "for a little bowl at a yard sale.",
      f"Close view of the yard-sale table: {BOWL}, drawn big in the middle, among a few other old things (a chipped "
      "plate, a small lamp). A small paper price tag beside it shows \"$3\".",
      f"{YARDSALE}; only the table top, the grass and the house porch behind show",
      "the small plain bowl with its $3 tag, clearly the main thing",
      "any pattern or picture on the bowl, any colour"),
 shot(3, "Years later,",
      f"{BOWL} sits on the mantel above the fireplace. Beside the mantel hangs a wall calendar with many of its pages "
      "flying off through the air.",
      LIVING,
      "the bowl on the mantel and the calendar pages flying",
      "any person, any money"),
 shot(4, "it sold for over two million.",
      f"{BOWL} stands on a plain table next to a tower of banknotes with \"$\" symbols that reaches the top of the "
      "frame; small sparkle marks around the bowl.",
      f"{LIVING}; the fireplace and mantel behind the table",
      "the small plain bowl beside a huge tower of cash",
      "any auction room, any person"),
 shot(5, "But first, two other bargains",
      f"Two people stand side by side, each holding their find out toward the viewer, a big question mark above each. "
      f"Left: {ZACH}, holding up {DIVE_WATCH} with a small paper price tag showing \"$5.99\". Right: {STUDENT}, "
      f"holding up {PAINTING}, standing beside {SOFABED} that has a price tag showing \"$215\".",
      "a plain town pavement with a low brick wall behind the people and a lamp post at one side",
      "the man with the old diving watch and its $5.99 tag, the student with the small painting and the sofa bed",
      "any money piles yet, the bowl"),
 shot(6, "that paid off big.",
      f"The same two people in the same places, now rich: banknotes rain down, each stands on a pile of money, "
      f"cheering. Left: {ZACH}, holding {DIVE_WATCH} and a fan of cash. Right: {STUDENT}, holding {PAINTING} and a "
      "fan of cash, beside the sofa bed.",
      "a plain town pavement with a low brick wall behind the people and a lamp post at one side",
      "the same two people clearly getting rich, each still holding their find",
      "the bowl, any colour"),
 shot(7, "A man in Arizona went into a Goodwill store.",
      f"{ZACH} walks in through the front door of the thrift store, shown from head to feet, looking around.",
      STORE,
      "the man with spiky hair and goatee entering the thrift store, the cactus through the front window",
      "any shop sign letters or logo"),
 shot(8, "He was looking for something else,",
      f"{ZACH} walks along the shelves of old things, one hand on his chin, looking at a golf bag and other "
      "things, not at any watches.",
      STORE,
      "the same man browsing shelves, looking for something",
      "any watch close-up yet, any letters"),
 shot(9, "but a case of old watches caught his eye.",
      f"{ZACH} stops short at the glass display case by the counter and leans over it; inside lie many old wristwatches "
      "in a row. Small exclamation lines above his head.",
      STORE,
      "the same man stopping at the glass case full of old watches",
      "any letters"),
 shot(10, "One of them cost five dollars and ninety-nine cents.",
      f"{ZACH} holds up {DIVE_WATCH} by its strap; a small paper price tag on a string hangs from it showing \"$5.99\".",
      STORE,
      "the diving watch held up with its $5.99 tag",
      "any letters on the watch"),
 shot(11, "He knew the name on the dial.",
      f"Close view: {DIVE_WATCH} drawn big in the middle of the frame, in his fingers. At the edge of the frame "
      f"the face of {ZACH}, eyes wide, mouth open.",
      f"{STORE}; only the glass case and the counter show behind",
      "the watch face up close and the man's amazed face",
      "readable letters or a brand name"),
 shot(12, "It was a rare diving watch from the nineteen fifties,",
      f"Underwater: a stick-figure diver in an old-fashioned 1950s diving mask, two air tanks on his back and "
      f"flippers swims past a reef; on his wrist is {DIVE_WATCH}, drawn a little big so it shows. Bubbles rise.",
      "under the sea: a rocky reef with seaweed, a few simple fish, light rays from the surface above",
      "the old-fashioned diver wearing the same diving watch underwater",
      "any letters, any modern gear"),
 shot(13, "with a built-in alarm.",
      f"Close view of the diver's wrist with {DIVE_WATCH}: little sound-wave arcs and a small bell symbol come out of "
      "the watch, ringing. The diver looks at it.",
      "under the sea: seaweed and bubbles around the wrist, light rays from above",
      "the watch ringing with sound waves on the diver's wrist",
      "any letters or numbers"),
 shot(14, "He sold it for thirty-five thousand dollars.",
      f"{ZACH} at home jumps with both arms up, a huge grin. He holds a phone whose screen shows \"$35,000\" big. "
      "A stack of banknotes with \"$\" stands on the table beside the watch.",
      "his small living room: a sofa, a coffee table, a window with desert hills and a cactus outside",
      "the same man cheering, $35,000 on the phone, the cash and the watch",
      "any letters or logos"),
 shot(15, "Then a student in Berlin bought a used sofa bed",
      f"{STUDENT} stands beside {SOFABED} at a market stall, pressing a cushion to test it, smiling.",
      FLEA,
      "the student with the bobbed hair and long scarf at the old sofa bed",
      "any letters or signs"),
 shot(16, "at a flea market,",
      f"Wide view of the flea market: rows of stalls of old furniture; among them {STUDENT} beside {SOFABED}. The "
      "TV tower rises over the skyline.",
      FLEA,
      "the Berlin flea market with the tall TV tower, and the student by the sofa bed",
      "any letters"),
 shot(17, "for two hundred fifteen dollars.",
      f"{STUDENT} hands a small fan of banknotes to a seller stick figure with a big moustache; a paper price tag "
      f"on {SOFABED} shows \"$215\".",
      FLEA,
      "the student paying, and the $215 tag on the sofa bed",
      "any other letters"),
 shot(18, "When the student pulled it out to make the bed,",
      f"In the flat, {STUDENT} pulls the folded mattress part of {SOFABED} out toward the viewer with both hands, "
      "unfolding it into a bed, with motion lines.",
      FLAT,
      "the same student unfolding the same sofa bed at home",
      "the painting yet, any letters"),
 shot(19, "a small painting was tucked inside.",
      f"The sofa bed half unfolded: in the fold between the mattress and the frame lies {PAINTING}. {STUDENT} "
      "freezes, eyes wide, mouth open.",
      FLAT,
      "the small framed painting lying inside the fold of the sofa bed, and the student's shock",
      "any money, any letters"),
 shot(20, "It was about four hundred years old.",
      f"{PAINTING}, drawn big in the middle of the frame, held in the student's hands. A thought bubble above shows a "
      "painter long ago in a puffy-sleeved shirt and a feathered hat, painting at a wooden easel by candlelight.",
      FLAT,
      "the small old painting up close and the thought bubble of a painter from long ago",
      "any letters or dates"),
 shot(21, "It sold at an auction",
      f"{AUCTION}. On the small display stand sits {PAINTING}. The auctioneer raises his gavel; bidders lift their "
      "paddles.",
      "the auction room, filling the frame",
      "the same small painting on the stand and the raised gavel",
      "any letters"),
 shot(22, "for over twenty-seven thousand dollars.",
      f"{AUCTION}. The gavel slams down with impact lines. Beside {PAINTING} stands a stack of banknotes with a \"$\" "
      f"on top. In the front row, {STUDENT} cheers with both arms up.",
      "the same auction room, filling the frame",
      "the gavel coming down, the painting, the stack of cash, the student cheering",
      "any letters"),
 shot(23, "Now, the bowl.",
      f"{BOWL}, alone on a plain wooden table in the middle of the frame, with a spotlight cone shining down on it.",
      f"{LIVING}; the fireplace behind the table, dim",
      "the same small plain bowl under a spotlight",
      "any person, any money"),
 shot(24, "In two thousand seven,",
      f"Wide view of the yard sale: the tables on the lawn, {YARD_SELLER} in her lawn chair, and a small wall calendar "
      f"hanging on the porch post showing \"2007\". On one table sits {BOWL}.",
      YARDSALE,
      "the yard sale, the bowl on a table, and 2007 on the calendar",
      "any other letters or numbers"),
 shot(25, "a family in New York bought it at a yard sale.",
      f"{FAMILY} walk away from the yard-sale table smiling; the mom carries {BOWL} in both hands; the girl waves "
      "goodbye to the seller.",
      YARDSALE,
      "the same family carrying the bowl away from the yard sale",
      "any money piles, any letters"),
 shot(26, "It was small and plain, and creamy white.",
      f"Close view: {BOWL} resting in the mom's two cupped hands, drawn big in the middle of the frame.",
      f"{LIVING}; the sofa and window softly behind",
      "the plain bowl up close: small, simple, no pattern",
      "any pattern, flowers or pictures on the bowl, any colour"),
 shot(27, "They kept it on their mantel.",
      f"{BOWL} sits on the mantel shelf next to a small clock and a family photo frame. The dad reads a newspaper on "
      "the sofa below, not looking at it.",
      LIVING,
      "the bowl sitting as an everyday ornament on the mantel",
      "any money, any letters"),
 shot(28, "Then they asked experts at Sotheby's to look at it.",
      f"{EXPERT} holds {BOWL} up carefully in both gloved hands under the desk lamp, studying its foot. {FAMILY} watch "
      "from the other side of the table, nervous.",
      EXPERT_ROOM,
      "the expert with white gloves examining the bowl, the same family watching",
      "any logo or letters"),
 shot(29, "It was about a thousand years old,",
      f"Long ago: {POTTER} sits at the wooden potter's wheel shaping the same small plain bowl from clay with both "
      "hands.",
      KILN,
      "the potter long ago making the same bowl on a wheel",
      "any modern thing, any letters"),
 shot(30, "made in China.",
      f"Wide view: {POTTER} carries a wooden board with a row of small plain bowls toward the brick kiln.",
      KILN,
      "the old Chinese pottery workshop with the curved roof and misty mountains",
      "any letters or flags"),
 shot(31, "Only one other like it is known,",
      f"Two identical copies of {BOWL} side by side on a plain cloth, each with a small spotlight above it; empty "
      "space all around them, nothing else.",
      "a plain dark gallery wall behind a long low table with a soft cloth",
      "exactly two matching bowls and nothing else: they are rare",
      "a third bowl, any person, any letters"),
 shot(32, "and it's in a museum in London.",
      f"One copy of {BOWL} sits alone inside a tall glass case in the museum; a visitor stick figure looks at it. "
      "Through the tall window the clock tower is seen.",
      MUSEUM,
      "the other bowl in a glass case in the London museum, the clock tower through the window",
      "any letters or signs"),
 shot(33, "In twenty thirteen,",
      f"{AUCTION}. On the small display stand sits {BOWL}. The auctioneer raises his gavel. A small sign on the front "
      "of the podium shows \"2013\".",
      "the auction room, filling the frame",
      "the auction room, the bowl on its stand, the raised gavel, 2013 on the podium sign",
      "any letters other than 2013"),
 shot(34, "the bowl sold for two point two million dollars.",
      f"{AUCTION}. The gavel slams down with impact lines. Beside {BOWL} stands a tower of banknotes with \"$\" "
      f"symbols reaching the top of the frame. {FAMILY} jump for joy in the front row.",
      "the same auction room, filling the frame",
      "the gavel coming down, the bowl, the huge cash tower, the same family jumping",
      "any letters"),
 shot(35, "What's sitting on your shelf right now?",
      "A friendly stick figure faces the viewer and points at a shelf of plain old things (a vase, a small bowl, a "
      "teapot, a clock) with a curious grin; a big question mark floats above the shelf.",
      "a cosy living room: the wooden shelf on the wall, a sofa, a window",
      "the stick figure pointing at the shelf of old things, and the question mark",
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
