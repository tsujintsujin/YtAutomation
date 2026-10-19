"""Image prompts for comic-coins-magnolias, written as one story (channels/SHORTS_RULES.md "How image prompts are
written"; worked example: ../nail-sandwich-nugget-declaration/scenes.py). Checks every line against script.md; once the
script is approved (right away: no approval step, this file approves it) writes scene + full prompt for every line into script.json.
usage: python channels/found-rich/videos/comic-coins-magnolias/scenes.py"""
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent                 # videos/<slug>
ROOT = HERE.parents[3]                                 # YtAutomation
sys.path.insert(0, str(ROOT))
from dashboard import approve, short_lines, short_prompt       # the script's lines, and the fixed frame around every prompt

STYLE = json.loads((HERE.parents[1] / "settings.json").read_text(encoding="utf-8"))["image_style"]
TOTAL = 33

# ---- the same words every time a person, object or place appears ----
HEADE_MAN = "a stick-figure man with a buzz cut and a plain work shirt with the sleeves rolled up"
HEADE_HOME = ("his plain living room in Indiana: a sofa, a low coffee table, a small TV, a window with flat farm "
              "fields outside, and a bare plaster wall")
MAGNOLIAS = ("an old painting in a plain wide wooden frame, about as wide as a pillow and a little wider than tall, "
             "showing three big open magnolia flowers with large rounded petals and a few glossy leaves lying on a "
             "soft draped cloth; black ink lines only, no colour")
HOLE = "a ragged hole in the plaster wall about the size of a dinner plate, with cracked edges and crumbs of plaster"
GAME = ("a board game laid out on the coffee table: a square board with a path of squares, little playing pieces, and "
        "a fan of cards, each card showing a tiny framed painting (no letters)")
EXPERT = "a stick-figure art expert in a tweed jacket and round glasses, holding a big magnifying glass"
MUSEUM = ("a big museum gallery in Houston: white walls, a polished floor, a long bench, a tall window with tall city "
          "towers outside")
BUILDER = ("a stick-figure man with a hard hat, safety goggles pushed up on his forehead, a work shirt and a tool belt "
           "round his waist")
OLDHOUSE = ("an old run-down wooden house in a small Minnesota town in winter: a sagging porch, a broken window, "
            "peeling boards, snow on the ground and the roof, bare trees")
INSIDE = ("inside the old house: the walls stripped down to their wooden boards and beams, broken plaster on the "
          "floor, a ladder, a work lamp on a stand, a frosty window")
PAPERS = ("a thick wad of old crumpled newspapers packed between the wall boards, covered in rows of tiny wavy lines "
          "for text (no readable letters); black ink lines only, no yellow, no brown")
COMIC = ("an old thin comic book a little bigger than a hand, its front cover showing only bold simple shapes and a "
         "thick band across the top (no characters, no figures, no faces, no letters), with worn soft corners")
COUPLE = ("a stick-figure couple in work overalls: a man with a bald head and glasses, and a woman with a short grey "
          "bob")
KITCHEN = ("their old kitchen in a Yorkshire house in England: the cupboards pushed to one side, the floor dug up "
           "into a square hole in broken concrete with old wooden floorboards pulled up beside it, a pickaxe, a "
           "bucket, a kitchen table, a window with green hills and a stone wall outside")
POT = "a small round clay pot about the size of a coffee mug, with a narrow neck and a chipped rim"
COINS = ("small round gold coins, each with a tiny outline of a king's head in profile (no letters); black ink lines "
         "only, no yellow, no gold colour, no colour")
AUCTION = ("an auction room: a wooden podium at the front with an auctioneer stick figure in a suit holding a gavel, a "
           "small display stand beside the podium, rows of chairs with stick-figure bidders holding up round paddles")
CAPTIONS = ("The place fills the whole frame; keep the very top and very bottom of the frame calm (sky, wall or floor) "
            "for captions. Never write any name, label or caption under or beside anyone or anything.")


def shot(n, text, what, place, must, never=""):
    return n, text, " ".join(x for x in (
        f"This is picture {n} of {TOTAL} in one continuous picture story; draw exactly this moment.",
        what, f"Place: {place}.", f"It MUST show: {must}.", f"NEVER: {never}." if never else "", CAPTIONS) if x)


S = [
 shot(1, "A man hung a painting",
      f"{HEADE_MAN} stands on tiptoe and hangs {MAGNOLIAS} on the bare wall, holding it level with both hands.",
      HEADE_HOME,
      "the man hanging the flower painting on his living-room wall",
      "any money, any museum"),
 shot(2, "over a hole in his wall.",
      f"{HEADE_MAN} tilts {MAGNOLIAS} away from the wall with one hand, and behind it we see {HOLE}. He winks at "
      "the viewer.",
      HEADE_HOME,
      "the hole in the wall, half hidden behind the same flower painting",
      "any money"),
 shot(3, "It was worth one point two five million dollars.",
      f"{MAGNOLIAS} hangs on the living-room wall; beside it stands a tower of banknotes with \"$\" symbols that "
      "reaches the ceiling. Small sparkle marks around the painting.",
      HEADE_HOME,
      "the same flower painting on the wall and the huge cash tower beside it",
      "any person, any museum"),
 shot(4, "But first, two other fortunes",
      f"Two groups stand side by side, each holding their find out to the viewer, a big question mark above each. "
      f"Left: {BUILDER}, holding up {COMIC}. Right: {COUPLE}, holding up {POT} between them.",
      "a plain town pavement with a low brick wall behind the people and a lamp post at one side",
      "the builder with the old comic and the couple with the small clay pot, with question marks",
      "any money yet, the painting, any comic character"),
 shot(5, "that were hiding inside people's homes.",
      f"A two-storey house drawn cut open like a doll's house, so we see inside every room. Inside one wall, between "
      f"the boards, {COMIC} glows with small sparkle marks. Under the kitchen floor, {POT} glows with small "
      "sparkle marks. Nobody is in the house.",
      "the cut-open house standing on a lawn with a tree beside it and a plain sky",
      "the comic hidden inside a wall and the pot hidden under a floor of the same cut-open house",
      "any person, any money, any comic character"),
 shot(6, "In Minnesota, a man bought an old house",
      f"{BUILDER} stands in the snow in front of the house with his hands on his hips, smiling up at it.",
      OLDHOUSE,
      "the builder in front of the run-down wooden house in the snow",
      "any letters"),
 shot(7, "for about ten thousand dollars,",
      f"{BUILDER} hands a stack of banknotes to a seller stick figure in a winter coat and woolly hat, on the porch. "
      "A small paper sign hanging on the porch rail shows \"$10,000\".",
      OLDHOUSE,
      "the builder paying for the house and $10,000 on the porch sign",
      "any other letters"),
 shot(8, "to fix it up.",
      f"{BUILDER} walks up to the porch carrying a toolbox in one hand and a ladder over his shoulder, ready to work.",
      OLDHOUSE,
      "the builder with a toolbox and a ladder heading into the old house",
      "any letters"),
 shot(9, "When he tore open a wall,",
      f"{BUILDER} pulls a wooden board off the wall with a crowbar; dust and bits of plaster fly with motion lines.",
      INSIDE,
      "the builder tearing a board off the wall with a crowbar",
      "the comic yet, any letters"),
 shot(10, "he found old newspapers stuffed inside to keep the heat in.",
      f"Behind the removed board: {PAPERS}. {BUILDER} peers at them, surprised, the crowbar in one hand.",
      INSIDE,
      "the thick wad of old newspapers packed inside the wall",
      "readable letters, the comic yet"),
 shot(11, "In the middle of them",
      f"{BUILDER} pulls the old newspapers out of the wall and apart with both hands; crumpled pages fall to the floor.",
      INSIDE,
      "the builder pulling the old newspapers apart",
      "readable letters"),
 shot(12, "was a comic book from nineteen thirty-eight.",
      f"{BUILDER} holds up {COMIC}, found among the newspapers; one crumpled newspaper at his feet shows a small "
      "date \"1938\" at its top. His eyes are wide.",
      INSIDE,
      "the builder holding up the old comic book, and 1938 on the old newspaper",
      "any comic character or figure on the cover, any other letters"),
 shot(13, "It was the very first Superman comic.",
      f"{COMIC}, drawn big in the middle of the frame, floating, with bright sparkle marks and light rays around it.",
      f"{INSIDE}; blurred behind it",
      "the old comic book, shining like a treasure",
      "Superman or any superhero, any character, any figure, any cape, any letters or logo"),
 shot(14, "The back cover got torn soon after,",
      f"Close view: the back of {COMIC}, with a long jagged rip across its back cover and a torn flap hanging down.",
      "a kitchen table with a few old newspapers on it",
      "the comic's back cover with a big jagged rip",
      "any character, any letters"),
 shot(15, "and that cost him a lot.",
      f"{BUILDER} holds the torn comic and clutches his hard hat with the other hand, groaning; a few banknotes with "
      "\"$\" fly away out of the frosty window with motion lines.",
      INSIDE,
      "the builder upset holding the torn comic, money flying away",
      "any character, any letters"),
 shot(16, "It still sold for a hundred seventy-five thousand dollars.",
      f"{BUILDER} cheers with both arms up next to a laptop on a sawhorse table; the screen shows an auction page with "
      f"a photo of {COMIC}, a small gavel icon and \"$175,000\" big. A stack of banknotes stands beside the laptop.",
      INSIDE,
      "the same builder celebrating, $175,000 on the laptop, the cash",
      "any character, any letters or logos"),
 shot(17, "Then a couple in England were fixing their kitchen floor.",
      f"{COUPLE}: the man swings a pickaxe into the broken concrete floor; the woman lifts old floorboards aside.",
      KITCHEN,
      "the couple in overalls digging up their kitchen floor",
      "the pot yet, any letters"),
 shot(18, "Under the concrete, they found a small pot.",
      f"The woman of {COUPLE} kneels at the hole and lifts {POT} out of the dirt with both hands; the man leans in, "
      "eyebrows high.",
      KITCHEN,
      "the small clay pot coming up out of the hole under the floor",
      "any coins showing yet, any letters"),
 shot(19, "It was full of gold coins,",
      f"The pot tips over on the kitchen floor and {COINS} spill out in a shining stream, with sparkle marks. "
      f"{COUPLE} gasp, hands on cheeks.",
      KITCHEN,
      "gold coins spilling out of the small pot, and the couple's shock",
      "any colour, any letters"),
 shot(20, "more than two hundred sixty of them,",
      f"The kitchen table covered with many neat rows and little stacks of {COINS}; {COUPLE} sort them, counting on "
      "their fingers.",
      KITCHEN,
      "lots and lots of coins laid out in rows on the table",
      "any colour, any letters or numbers"),
 shot(21, "hidden about three hundred years ago.",
      f"Long ago, by candlelight, in the same room when it was new: a man in a three-cornered hat and a long coat kneels "
      f"and lowers {POT} full of coins into a hole under the wooden floorboards, glancing over his shoulder.",
      "the same kitchen three hundred years ago: plain stone walls, a big open fireplace with a cooking pot, a "
      "wooden table, a candle",
      "the man from long ago hiding the pot under the floor",
      "any modern thing, any letters"),
 shot(22, "In twenty twenty-two",
      f"{AUCTION}. On the small display stand sits a wooden tray full of {COINS}. The auctioneer raises his gavel. A "
      "small sign on the front of the podium shows \"2022\".",
      "the auction room, filling the frame",
      "the tray of coins on the stand, the raised gavel, 2022 on the podium sign",
      "any other letters"),
 shot(23, "they sold at auction for seven hundred fifty-four thousand pounds.",
      f"{AUCTION}. The gavel slams down with impact lines. Beside the tray of coins stands a tall stack of banknotes "
      f"with a \"£\" symbol on top. In the front row, {COUPLE} hug each other, cheering.",
      "the same auction room, filling the frame",
      "the gavel coming down, the coins, the tall stack of cash with £, the same couple cheering",
      "any letters"),
 shot(24, "Now, the painting.",
      f"{MAGNOLIAS}, alone on a plain wall in the middle of the frame, with a spotlight cone shining on it.",
      f"{HEADE_HOME}; only the wall and a bit of the sofa show",
      "the same flower painting under a spotlight",
      "any person, any money"),
 shot(25, "A man in Indiana had an old painting of flowers.",
      f"{HEADE_MAN} stands beside {MAGNOLIAS}, which leans against the sofa; he shrugs, not impressed.",
      HEADE_HOME,
      "the man in his Indiana living room with the old flower painting",
      "any money"),
 shot(26, "He'd hung it on his wall just to hide a hole.",
      f"{HEADE_MAN} hangs {MAGNOLIAS} right over {HOLE}; half of the hole still shows at the painting's edge as it "
      "goes up.",
      HEADE_HOME,
      "the painting going up over the hole in the wall",
      "any money"),
 shot(27, "One day he was playing a board game called Masterpiece.",
      f"{HEADE_MAN} and two friends sit around the coffee table playing {GAME}. The flower painting hangs on the wall "
      "behind them.",
      HEADE_HOME,
      "the friends playing the board game with painting cards, the painting on the wall behind",
      "any letters or logo on the game"),
 shot(28, "One of the game's paintings looked a lot like his.",
      f"{HEADE_MAN} holds up one game card toward the viewer; the card shows a tiny painting of big magnolia flowers on "
      f"a draped cloth. He looks back over his shoulder at {MAGNOLIAS} on his wall: the two match in style. His jaw "
      "drops.",
      HEADE_HOME,
      "the game card's flower painting and the painting on his wall looking alike",
      "any letters"),
 shot(29, "It turned out his was by the same artist,",
      f"{EXPERT} studies {MAGNOLIAS} up close through the magnifying glass; {HEADE_MAN} waits beside him, biting his "
      "nails.",
      HEADE_HOME,
      "the expert checking the same flower painting with a magnifying glass",
      "any letters"),
 shot(30, "Martin Johnson Heade.",
      "Long ago: a painter stick figure with a long beard, a waistcoat and a painter's palette stands at a wooden "
      "easel, painting big magnolia flowers on a draped cloth; real magnolia flowers lie on a table in front of him.",
      "a painter's studio long ago: a tall window with soft light, canvases leaning against the wall, a jar of brushes",
      "the painter from long ago painting the magnolias",
      "any real person's face or likeness, any letters"),
 shot(31, "A museum in Houston bought it",
      f"{MAGNOLIAS} hangs on a white museum wall with a small spotlight above it; two visitors admire it.",
      MUSEUM,
      "the same flower painting hanging in the big museum, the city towers outside",
      "any letters or signs"),
 shot(32, "for one point two five million dollars.",
      f"Beside {MAGNOLIAS} on the museum wall stands a tower of banknotes with \"$\" symbols up to the ceiling; "
      f"{HEADE_MAN}'s jaw drops.",
      MUSEUM,
      "the painting, the huge cash tower and the same man in shock",
      "any letters"),
 shot(33, "What's hiding in your walls?",
      "A friendly stick figure faces the viewer and knocks on a plain living-room wall with one fist, ear pressed "
      "close, a curious grin; a big question mark floats above.",
      "a cosy living room: a plain wall, a picture frame, a lamp, a sofa",
      "the stick figure knocking on the wall, and the question mark",
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
