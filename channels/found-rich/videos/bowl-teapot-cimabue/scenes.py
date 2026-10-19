"""Image prompts for bowl-teapot-cimabue, written as one story (channels/SHORTS_RULES.md "How image prompts are
written"; worked example: ../nail-sandwich-nugget-declaration/scenes.py). Checks every line against script.md; once the
script is approved (right away: no approval step, this file approves it) writes scene + full prompt for every line into script.json.
usage: python channels/found-rich/videos/bowl-teapot-cimabue/scenes.py"""
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
GRANNY = "a stick-figure old woman with white hair in a bun, round glasses and a flowery apron"
KITCHEN = ("her old kitchen in a French house: a small two-ring hot plate on a counter, a kettle, a wooden table "
           "with a checked cloth, a window with shutters and a church spire outside")
PAINTING = ("a tiny old painting on a wooden panel, about the size of a paperback book, with a pointed-arch top edge "
            "and a plain gold-leaf background (drawn plain, no colour), showing a calm man with long hair and a beard "
            "in a long robe, standing with a small crowd of figures around him")
EXPERT_FR = "a stick-figure woman expert with a sleek short haircut, a blazer and a clipboard"
HOUSE_FR = ("the outside of an old stone house in a French town: wooden window shutters, a wooden front door, "
            "a small garden with a gate, a church spire behind")
MEDIEVAL = ("a painter's workshop in Italy about seven hundred years ago: wooden panels leaning on the walls, pots of "
            "paint, a work table, a tall window with a medieval town and a tall stone bell tower outside")
PAINTER_OLD = "a stick-figure painter long ago in a long simple tunic and a soft cap, holding a thin brush"
MING_MAN = "a stick-figure man with a baseball cap, a short beard and a fleece jacket"
YARDSALE = ("a yard sale on the front lawn of a white wooden house in Connecticut: folding tables on the grass with old "
            "plates, bowls, books and a lamp, big leafy trees, a car parked at the curb")
YARD_SELLER = "a stick-figure old man in a cardigan and slippers sitting on a lawn chair behind the table"
BOWL = ("a small round bowl about as wide as a hand, with gently curved sides, painted inside and out with a ring of "
        "simple flowers and leaves in thin brush lines; black ink lines only, no blue, no colour")
MING_HOME = "his kitchen: a counter, a window over the sink, a table with a laptop and a phone"
CHINA_OLD = ("a Chinese palace room about six hundred years ago: tall wooden columns, a curved tiled roof edge seen "
             "through the open doors, a low carved table, paper lanterns")
TEA_MAN = "a stick-figure man with a flat cap, a waistcoat and a big grey moustache"
TEAPOT = ("a small round teapot about the size of a grapefruit, with a curved spout, a loop handle and a little lid "
          "with a knob, painted with a few simple leaves; a chip missing from the end of its spout and a crack line "
          "down its side; black ink lines only, no colour")
TEA_HOME = ("his front room in England: a wooden table with a laptop, a dresser with old plates, a window with rainy "
            "rooftops")
COLONY = ("a small colonial American town in the 1760s by a river: wooden houses, a small brick pottery with a kiln "
          "chimney, a horse and cart, tall trees")
POTTER = "a stick-figure potter long ago in a three-cornered hat, a leather apron and rolled-up sleeves"
MUSEUM_NY = ("a big museum gallery in New York: tall glass cases, a polished floor, a tall window with skyscrapers "
             "outside")
AUCTION = ("an auction room: a wooden podium at the front with an auctioneer stick figure in a suit holding a gavel, a "
           "small display stand beside the podium, rows of chairs with stick-figure bidders holding up round paddles")
CAPTIONS = ("The place fills the whole frame; keep the very top and very bottom of the frame calm (sky, wall or floor) "
            "for captions. Never write any name, label or caption under or beside anyone or anything.")


def shot(n, text, what, place, must, never=""):
    return n, text, " ".join(x for x in (
        f"This is picture {n} of {TOTAL} in one continuous picture story; draw exactly this moment.",
        what, f"Place: {place}.", f"It MUST show: {must}.", f"NEVER: {never}." if never else "", CAPTIONS) if x)


S = [
 shot(1, "An old woman kept a small painting in her kitchen,",
      f"{GRANNY} stirs a small pot on the hot plate. On the wall above the hot plate hangs {PAINTING}, small among the "
      "kitchen things.",
      KITCHEN,
      "the old woman cooking and the tiny painting hanging on her kitchen wall",
      "any money, any expert"),
 shot(2, "right above the stove.",
      f"Close view: {PAINTING} hanging on the wall just above the hot plate; wavy steam lines rise from a pot past the "
      "painting.",
      f"{KITCHEN}; only the wall, the hot plate and the pot show",
      "the tiny painting right above the hot plate, steam rising past it",
      "any money"),
 shot(3, "It sold for twenty-four million euros.",
      f"{PAINTING} on the kitchen wall, now beside a tower of banknotes with \"€\" symbols reaching the ceiling; small "
      "sparkle marks around the painting.",
      KITCHEN,
      "the tiny painting and the huge cash tower beside it",
      "any person, any letters"),
 shot(4, "But first, two other kitchen things",
      f"On a plain kitchen counter, side by side, each with a big question mark above it: {BOWL} and {TEAPOT}.",
      "a plain kitchen counter against a tiled wall with a window",
      "the small flower bowl and the small chipped teapot, with question marks",
      "any person, any money, any colour"),
 shot(5, "that were worth a fortune.",
      f"The same counter: {BOWL} and {TEAPOT} now glow with light rays and sparkle marks, and stacks of banknotes with "
      "\"$\" and \"£\" pile up behind them against the tiles.",
      "a plain kitchen counter against a tiled wall with a window",
      "the same bowl and teapot glowing, with piles of cash behind them",
      "any person, any colour"),
 shot(6, "In twenty twenty,",
      f"Wide view of the yard sale on the lawn; {YARD_SELLER} sits behind a table. A small calendar hangs on the porch "
      "post showing \"2020\".",
      YARDSALE,
      "the yard sale and 2020 on the calendar",
      "any other letters or numbers"),
 shot(7, "a man in Connecticut stopped at a yard sale.",
      f"{MING_MAN} steps out of his car at the curb and walks up the lawn toward the yard-sale tables, curious.",
      YARDSALE,
      "the man in a baseball cap arriving at the yard sale",
      "any letters"),
 shot(8, "He paid thirty-five dollars",
      f"{MING_MAN} hands banknotes to {YARD_SELLER}; a small paper price tag on the table shows \"$35\".",
      YARDSALE,
      "the man paying and the $35 tag",
      "any other letters"),
 shot(9, "for a small white bowl with blue flowers.",
      f"{MING_MAN} holds up {BOWL} in both hands, turning it to look at the painted flowers.",
      YARDSALE,
      "the small bowl with its painted flowers held up by the same man",
      "any colour, any letters"),
 shot(10, "He had a feeling it was special,",
      f"{MING_MAN} sits at his kitchen table studying {BOWL} closely, chin in hand; a small light bulb drawn above his "
      "head.",
      MING_HOME,
      "the man studying the bowl at home with a light bulb above his head",
      "any money, any letters"),
 shot(11, "so he sent photos to Sotheby's.",
      f"{MING_MAN} photographs {BOWL} on the table with his phone; the open laptop beside it shows an email with small "
      "photos of the bowl and a send arrow.",
      MING_HOME,
      "the man photographing the bowl and emailing the photos",
      "any readable letters or logo"),
 shot(12, "It was made in China about six hundred years ago,",
      f"Long ago: a stick-figure painter in a long robe with his hair in a top knot paints the flowers onto the same "
      f"small bowl with a fine brush, sitting at a low table; finished bowls stand in a row.",
      CHINA_OLD,
      "the painter long ago painting the flowers onto the same bowl",
      "any modern thing, any letters"),
 shot(13, "in the Ming dynasty.",
      f"Wide view of the old Chinese palace room: {BOWL} sits on the low carved table; a stick-figure emperor in a long "
      "robe and a round hat looks at it.",
      CHINA_OLD,
      "the bowl in the old Chinese palace long ago",
      "any real person's face, any letters"),
 shot(14, "Only six others like it are known.",
      f"Seven identical copies of {BOWL} in a long row, each inside its own small glass case on a stand, each under a "
      "small spotlight.",
      "a long quiet museum hall with a plain wall and a polished floor",
      "exactly seven matching bowls in a row: they are rare",
      "any person, any letters or numbers"),
 shot(15, "In twenty twenty-one,",
      f"{AUCTION}. On the small display stand sits {BOWL}. The auctioneer raises his gavel. A small sign on the front of "
      "the podium shows \"2021\".",
      "the auction room, filling the frame",
      "the bowl on its stand, the raised gavel, 2021 on the podium sign",
      "any other letters"),
 shot(16, "it sold for over seven hundred twenty thousand dollars.",
      f"{AUCTION}. The gavel slams down with impact lines. Beside {BOWL} stands a tall stack of banknotes with a \"$\" "
      f"on top. In the front row, {MING_MAN} cheers.",
      "the same auction room, filling the frame",
      "the gavel coming down, the bowl, the tall stack of cash, the same man cheering",
      "any letters"),
 shot(17, "Then a man in England bought a small broken teapot",
      f"{TEA_MAN} sits at his table holding {TEAPOT} up to the light, frowning at the chipped spout and the crack.",
      TEA_HOME,
      "the man with the grey moustache holding the small chipped, cracked teapot",
      "a whole perfect teapot, any colour"),
 shot(18, "for fifteen pounds.",
      f"Close view: {TEAPOT} on the table with a small paper price tag on a string showing \"£15\"; the man's hand "
      "puts down a few coins and a note beside it.",
      TEA_HOME,
      "the chipped teapot with its £15 tag",
      "any other letters"),
 shot(19, "It turned out to be one of the first pieces of porcelain,",
      f"{TEAPOT}, drawn big in the middle of the frame on the table, with sparkle marks and light rays around it; "
      "it looks delicate and fine, so thin the light shines through its edge.",
      TEA_HOME,
      "the same chipped teapot, shining like a treasure",
      "a different teapot, any colour"),
 shot(20, "that's fine china,",
      f"A wooden dresser shelf with a neat row of delicate fine-china cups, saucers and plates, and in the middle {TEAPOT}.",
      TEA_HOME,
      "the teapot among fine china cups and plates on a shelf",
      "any colour, any letters"),
 shot(21, "ever made in America,",
      f"Wide view long ago: {COLONY}; smoke curls from the pottery's kiln chimney.",
      COLONY,
      "the small colonial American town with its little pottery",
      "any modern thing, any letters or flags"),
 shot(22, "from the seventeen sixties.",
      f"Inside the small pottery long ago: {POTTER} shapes the same small teapot on a wheel; a small wooden plaque on "
      "the wall shows \"1760s\".",
      f"inside the brick pottery in {COLONY}: shelves of drying pots, the kiln glowing at the back",
      "the potter long ago making the teapot, and 1760s on the plaque",
      "any other letters"),
 shot(23, "It sold for five hundred seventy-five thousand pounds,",
      f"{AUCTION}. The gavel slams down with impact lines. Beside {TEAPOT} on its stand stands a tall stack of banknotes "
      f"with a \"£\" symbol on top. In the front row, {TEA_MAN} cheers.",
      "the auction room, filling the frame",
      "the gavel coming down, the chipped teapot, the tall stack of cash with £, the same man cheering",
      "any letters"),
 shot(24, "and a museum in New York ended up with it.",
      f"{TEAPOT} sits inside a tall glass case in the museum, under a small spotlight; two visitors admire it.",
      MUSEUM_NY,
      "the same chipped teapot on show in the New York museum, skyscrapers outside",
      "any letters or signs"),
 shot(25, "Now, the painting.",
      f"{PAINTING}, alone on a plain wall in the middle of the frame, with a spotlight cone shining on it.",
      f"{KITCHEN}; only the wall and the hot plate below show",
      "the same tiny painting under a spotlight",
      "any person, any money"),
 shot(26, "In twenty nineteen,",
      f"The outside of the house; a small calendar hangs by the front door showing \"2019\".",
      HOUSE_FR,
      "the old French house and 2019 on the calendar",
      "any other letters or numbers"),
 shot(27, "an expert was clearing out an old woman's house in France.",
      f"{EXPERT_FR} walks through the old woman's house writing on her clipboard, looking at furniture with stickers on "
      f"it; {GRANNY} shows her around.",
      "inside the old French house: old furniture with small round stickers on it, boxes, paintings stacked by the wall",
      "the expert going through the house with the old woman",
      "any readable letters"),
 shot(28, "In the kitchen, above the hot plate,",
      f"{EXPERT_FR} steps into the kitchen doorway and looks toward the hot plate; {GRANNY} behind her.",
      KITCHEN,
      "the expert entering the kitchen, looking at the wall above the hot plate",
      "any money"),
 shot(29, "hung a tiny painting of Jesus.",
      f"Close view: {PAINTING}, drawn big in the middle of the frame on the kitchen wall above the hot plate; the "
      f"face of {EXPERT_FR} leans in from the side, eyes wide.",
      f"{KITCHEN}; only the wall and the hot plate show",
      "the tiny painting of Jesus with the crowd around him, and the amazed expert",
      "a smiley face, any letters"),
 shot(30, "The woman thought it was just an old religious picture.",
      f"{GRANNY} shrugs at {PAINTING} with a little wave of her hand, not impressed; the expert stares at it.",
      KITCHEN,
      "the old woman shrugging at the painting, the expert amazed",
      "any money"),
 shot(31, "It was painted around twelve eighty",
      f"Long ago: {PAINTER_OLD} paints the same small scene of the calm man in a robe and the crowd onto a small wooden "
      "panel on his work table.",
      MEDIEVAL,
      "the painter long ago painting the same small panel",
      "any modern thing, any letters"),
 shot(32, "by Cimabue,",
      f"{PAINTER_OLD} presses thin flat sheets of gold leaf onto the background of the panel with a soft brush "
      "(drawn plain, no colour), concentrating.",
      MEDIEVAL,
      "the same painter adding gold leaf to the background of the panel",
      "any real person's face or likeness, any colour, any letters"),
 shot(33, "one of the first great Italian painters.",
      f"Wide view long ago: a medieval Italian town on a hill with a tall stone bell tower and a big church dome; "
      f"{PAINTER_OLD} stands in the square holding the finished panel while townspeople gather round in awe.",
      "a medieval Italian hill town: stone houses, the tall bell tower, a church dome, cypress trees",
      "the painter admired in his town long ago",
      "any modern thing, any letters"),
 shot(34, "It sold for twenty-four million euros.",
      f"{AUCTION}. The gavel slams down with impact lines. Beside {PAINTING} on its stand stands a tower of banknotes "
      f"with \"€\" symbols reaching the ceiling. In the front row, {GRANNY}'s jaw drops.",
      "the auction room, filling the frame",
      "the gavel coming down, the tiny painting, the giant cash tower, the old woman's shock",
      "any letters"),
 shot(35, "What's hanging in your kitchen?",
      "A friendly stick figure faces the viewer and points at a small framed picture on a kitchen wall with a curious "
      "grin; a big question mark floats above.",
      "a cosy kitchen: a stove, a kettle, a window, the small picture on the wall",
      "the stick figure pointing at the picture on the kitchen wall, and the question mark",
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
