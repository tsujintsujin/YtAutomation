"""Image prompts for game-chessman-vase, written as one story (channels/SHORTS_RULES.md "How image prompts are
written"; worked example: ../nail-sandwich-nugget-declaration/scenes.py). Checks every line against script.md; once the
script is approved (right away: no approval step, this file approves it) writes scene + full prompt for every line into script.json.
usage: python channels/found-rich/videos/game-chessman-vase/scenes.py"""
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent                 # videos/<slug>
ROOT = HERE.parents[3]                                 # YtAutomation
sys.path.insert(0, str(ROOT))
from dashboard import approve, short_lines, short_prompt       # the script's lines, and the fixed frame around every prompt

STYLE = json.loads((HERE.parents[1] / "settings.json").read_text(encoding="utf-8"))["image_style"]
TOTAL = 36

# ---- the same words every time a person, object or place appears ----
COUPLE = ("a stick-figure French couple: a man with a thin moustache and a beret, and a woman with a long braid and a "
          "striped top")
VASE = ("a tall round-bellied vase with a narrow neck and a flared lip, about as tall as a forearm, painted all over "
        "with a fine pattern of flowers, small birds and swirling clouds in simple ink lines; black ink lines only, no "
        "colour")
SHOEBOX = "a plain cardboard shoebox with its lid"
NEWSPAPER = "crumpled newspaper covered in tiny wavy lines for text (no readable letters)"
ATTIC = ("their dusty attic in France: sloping wooden roof beams, a small round window, old trunks, rolled-up rugs, a "
         "wooden rocking horse, stacked picture frames, cardboard boxes")
PARIS_HOUSE = ("the street outside a grand old auction house in Paris: stone steps up to tall wooden doors, iron "
               "balconies, and the top of the Eiffel Tower rising over the rooftops")
PARIS_ROOM = ("an elegant auction room in Paris: tall windows with the top of the Eiffel Tower seen outside, crystal "
              "chandeliers, a wooden podium with an auctioneer stick figure in a suit holding a gavel, a small display "
              "stand, rows of gilded chairs with stick-figure bidders holding up round paddles")
EMPEROR = ("a stick-figure Chinese emperor long ago in a long robe with a simple dragon pattern and a round hat with a "
           "tassel on top")
PALACE = ("a Chinese palace hall long ago: tall wooden columns, a curved tiled roof edge seen through the open doors, "
          "a low carved table, silk lanterns")
GAME = ("a small flat video game box about the size of a hardback book, still wrapped in shiny clear plastic (a few "
        "shine lines on it), its front showing only simple bold shapes and one big star shape (no characters, no "
        "faces, no letters, no logo)")
DAD80 = "a stick-figure dad with a big bushy moustache and a knitted sweater with a zig-zag stripe"
ROOM80 = ("a cosy 1980s living room: a Christmas tree with presents under it, a boxy old TV with rabbit-ear aerials, a "
          "sofa, a wooden desk with drawers, a window with snow outside")
DESK = "an old wooden desk with three drawers, a desk lamp and a pencil cup on top"
AUCTION = ("an auction room: a wooden podium at the front with an auctioneer stick figure in a suit holding a gavel, a "
           "small display stand beside the podium, rows of chairs with stick-figure bidders holding up round paddles")
DEALER = "a stick-figure older man with neat white hair, a tweed waistcoat and half-moon glasses"
SHOP = ("a cluttered antiques shop in Edinburgh: shelves of old clocks, china plates and silver, a wooden counter, a "
        "window showing a castle on a rocky hill")
PIECE = ("a small carved chess piece about the height of a thumb, carved from old ivory: a little standing warrior "
         "with a round helmet, wide staring eyes and a grumpy mouth, holding a tall shield in front of him and a sword "
         "upright; black ink lines only, no colour")
DRAWERS = "an old wooden chest of drawers with round knobs"
HOME = ("the family's living room in Edinburgh: the chest of drawers against the wall, a fireplace, a window with "
        "rooftops and chimney pots")
EXPERT = "a stick-figure expert in a neat suit and round glasses, wearing white cotton gloves, holding a magnifying glass"
FAMILY = "a stick-figure family: a middle-aged woman with a short bob and a cardigan, and her grown-up son with curly hair"
SET = ("a whole set of small carved chess pieces in the same style as the warrior: grumpy kings and queens on thrones, "
       "bishops, knights on little horses, warriors with shields, standing on an old wooden chessboard")
CAPTIONS = ("The place fills the whole frame; keep the very top and very bottom of the frame calm (sky, wall or floor) "
            "for captions. Never write any name, label or caption under or beside anyone or anything.")


def shot(n, text, what, place, must, never=""):
    return n, text, " ".join(x for x in (
        f"This is picture {n} of {TOTAL} in one continuous picture story; draw exactly this moment.",
        what, f"Place: {place}.", f"It MUST show: {must}.", f"NEVER: {never}." if never else "", CAPTIONS) if x)


S = [
 shot(1, "A family brought a vase to an auction house",
      f"{COUPLE} carry {SHOEBOX} carefully between them up the stone steps toward the tall doors.",
      PARIS_HOUSE,
      "the couple carrying a shoebox up the steps of the grand auction house, the Eiffel Tower behind",
      "the vase showing yet, any letters or signs"),
 shot(2, "in a shoebox.",
      f"Close view: {SHOEBOX} with its lid off, held in the couple's hands; inside, nested in {NEWSPAPER}, lies {VASE}, "
      "its neck poking out of the paper.",
      f"{PARIS_HOUSE}; only the stone steps and door show behind the box",
      "the vase wrapped in newspaper inside the shoebox",
      "readable letters, any colour"),
 shot(3, "It sold for sixteen million euros.",
      f"{VASE} stands on a small display stand next to a tower of banknotes with \"€\" symbols reaching the chandelier.",
      PARIS_ROOM,
      "the vase beside a huge tower of cash with €",
      "any person, any letters"),
 shot(4, "But first, two other things",
      f"Two things side by side on a plain table, each with a big question mark above it: left, {GAME}; right, {PIECE}.",
      "a plain wooden table against a plain wall",
      "the sealed game box and the tiny carved chess piece, with question marks",
      "any person, any money, any game character"),
 shot(5, "people forgot they had.",
      f"Two half-open drawers side by side, dusty and covered with cobwebs: in the left drawer lies {GAME}; in the right "
      f"drawer lies {PIECE}. Nobody is around.",
      "the fronts of two old wooden drawers against a plain wall",
      "the same game box and chess piece forgotten in dusty drawers",
      "any person, any money, any game character"),
 shot(6, "Back in the nineteen eighties,",
      "Wide view of the 1980s living room at Christmas: the tree with presents, the boxy old TV, the snowy window.",
      ROOM80,
      "the cosy 1980s Christmas living room, clearly from long ago",
      "any modern thing, any letters or numbers"),
 shot(7, "someone bought a Super Mario Brothers game",
      f"{DAD80} holds up {GAME} toward the viewer, grinning.",
      ROOM80,
      "the dad holding up the sealed game box",
      "any game character, any plumber, any mushroom, any letters or logo"),
 shot(8, "as a Christmas present.",
      f"{DAD80} wraps {GAME} in gift paper with a pattern of little stars and ties a big bow on it, at the desk.",
      ROOM80,
      "the game being wrapped as a Christmas present",
      "any game character, any letters"),
 shot(9, "It never got opened.",
      f"{GAME}, still sealed in its plastic, sits on a high shelf behind a pile of other boxes, pushed to the back; "
      "under the tree, children open other presents.",
      ROOM80,
      "the same game still sealed, set aside and forgotten",
      "any game character, any letters"),
 shot(10, "It went into a desk drawer",
      f"{DAD80} slides {GAME} into the top drawer of {DESK}.",
      ROOM80,
      "the sealed game going into the desk drawer",
      "any game character, any letters"),
 shot(11, "and stayed there for about thirty-five years.",
      f"{DESK}, its drawers closed, covered in dust and cobwebs. Beside it hangs a wall calendar with many of its "
      "pages flying off through the air.",
      "a quiet spare room: a plain wall, a window with a bare tree",
      "the closed desk drawer gathering dust, the calendar pages flying",
      "any person, any letters"),
 shot(12, "In twenty twenty-one,",
      f"{AUCTION}. The auctioneer raises his gavel. A small sign on the front of the podium shows \"2021\". On the "
      f"display stand sits {GAME}.",
      "the auction room, filling the frame",
      "the auction room, the game on its stand, 2021 on the podium sign",
      "any other letters, any game character"),
 shot(13, "still sealed in its plastic,",
      f"Close view: {GAME} drawn big in the middle of the frame, the plastic wrap shining with bright shine lines and "
      "small sparkle marks.",
      "the auction room's display stand, the rest of the room dim behind",
      "the game box still in its shiny sealed plastic",
      "any game character, any letters or logo"),
 shot(14, "it sold for six hundred sixty thousand dollars.",
      f"{AUCTION}. The gavel slams down with impact lines. Beside {GAME} stands a tall stack of banknotes with a \"$\" "
      "on top. Bidders gasp.",
      "the same auction room, filling the frame",
      "the gavel coming down, the game, the tall stack of cash",
      "any game character, any letters"),
 shot(15, "Then an antiques dealer in Scotland",
      f"{DEALER} stands behind the counter of his shop, polishing an old clock, shown from the waist up.",
      SHOP,
      "the old dealer in his cluttered antiques shop, the castle through the window",
      "any letters or signs"),
 shot(16, "bought a small carved chess piece in nineteen sixty-four.",
      f"{DEALER} holds up {PIECE} between two fingers, peering at it through his half-moon glasses. A small calendar on "
      "the shop wall shows \"1964\".",
      SHOP,
      "the tiny carved warrior chess piece held up, and 1964 on the calendar",
      "any other letters"),
 shot(17, "He paid five pounds.",
      f"{DEALER} hands one banknote marked \"£5\" across the counter to another dealer stick figure in a flat cap, who "
      f"hands him {PIECE}.",
      SHOP,
      "the £5 note and the chess piece changing hands",
      "any other letters"),
 shot(18, "His family kept it in a drawer",
      f"{FAMILY} at home: the woman places {PIECE} into the top drawer of {DRAWERS}.",
      HOME,
      "the chess piece being put away in a drawer at home",
      "any letters"),
 shot(19, "for more than fifty years.",
      f"{DRAWERS}, closed, dusty, with cobwebs. Beside it hangs a wall calendar with many of its pages flying off.",
      HOME,
      "the closed chest of drawers gathering dust, the calendar pages flying",
      "any person, any letters"),
 shot(20, "Then experts looked at it.",
      f"{EXPERT} studies {PIECE} up close through the magnifying glass at a table; {FAMILY} watch, nervous.",
      "an expert's viewing room: a table with a soft cloth, a desk lamp, shelves of old objects behind glass",
      "the expert examining the tiny chess piece, the family watching",
      "any letters"),
 shot(21, "It was one of the Lewis chessmen,",
      f"{PIECE} stands at the front of {SET}; all the pieces look alike in style.",
      "a museum display: a glass case on a stand, a plain wall, a small spotlight",
      "the same warrior piece matching a whole set of famous old carved chessmen",
      "any person, any letters"),
 shot(22, "a famous set carved about eight hundred years ago.",
      "Long ago, by candlelight: a carver stick figure in a hooded wool tunic sits at a rough wooden bench carving "
      "small chess pieces from a long curved walrus tusk with a little knife; finished pieces stand in a row.",
      "a stone hut long ago on a windy Scottish island: a small fire, a candle, a tiny window with sea and cliffs",
      "the carver long ago making the chess pieces",
      "any modern thing, any letters"),
 shot(23, "In twenty nineteen",
      f"{AUCTION}. On the small display stand sits {PIECE} under a glass dome. The auctioneer raises his gavel. A small "
      "sign on the front of the podium shows \"2019\".",
      "the auction room, filling the frame",
      "the chess piece on its stand, the raised gavel, 2019 on the podium sign",
      "any other letters"),
 shot(24, "it sold for seven hundred thirty-five thousand pounds.",
      f"{AUCTION}. The gavel slams down with impact lines. Beside {PIECE} stands a tall stack of banknotes with a \"£\" "
      f"on top. In the front row, {FAMILY} cheer.",
      "the same auction room, filling the frame",
      "the gavel coming down, the tiny chess piece, the tall stack of cash with £, the family cheering",
      "any letters"),
 shot(25, "Now, the vase.",
      f"{VASE}, alone on a small round table in the middle of the frame, with a spotlight cone shining down on it.",
      f"{ATTIC}; dim behind the table",
      "the same patterned vase under a spotlight",
      "any person, any money, any colour"),
 shot(26, "A family in France found it up in their attic,",
      f"{COUPLE} kneel in the dusty attic; the woman lifts {VASE} out of an old open trunk, blowing dust off it.",
      ATTIC,
      "the couple finding the vase in an old trunk in their attic",
      "any money, any colour"),
 shot(27, "with other things they'd inherited.",
      f"Wide view of the attic: {COUPLE} stand among the old trunks, the rocking horse, rolled rugs and frames; the "
      f"woman holds {VASE}. On a trunk stands an old framed photo of a grandmother.",
      ATTIC,
      "the couple among the many old inherited things, the vase among them",
      "any money, any letters"),
 shot(28, "They wrapped it in newspaper,",
      f"{COUPLE} kneel on the attic floor wrapping {VASE} in {NEWSPAPER}.",
      ATTIC,
      "the vase being wrapped in newspaper",
      "readable letters"),
 shot(29, "put it in a shoebox,",
      f"The man lowers the newspaper-wrapped vase into {SHOEBOX}; the woman holds the lid ready.",
      ATTIC,
      "the wrapped vase going into the shoebox",
      "readable letters"),
 shot(30, "and took it to Sotheby's in Paris.",
      f"{COUPLE} walk along a Paris street carrying {SHOEBOX}, past the grand auction house doors, the Eiffel Tower "
      "behind.",
      PARIS_HOUSE,
      "the couple carrying the shoebox in Paris to the auction house",
      "any logo or letters or signs"),
 shot(31, "It was a Chinese vase made for an emperor",
      f"Long ago: {EMPEROR} admires {VASE} on a low carved table, a servant bowing beside it.",
      PALACE,
      "the emperor long ago admiring the same vase",
      "any real person's face, any letters"),
 shot(32, "in the seventeen hundreds.",
      f"The same palace hall, wider: {VASE} on the carved table, and a hanging wooden plaque that shows \"1700s\".",
      PALACE,
      "the vase in the old palace and 1700s on the plaque",
      "any other letters"),
 shot(33, "The experts guessed it might sell",
      f"Two experts in suits and glasses lean over {VASE} on a table; one holds up a small paper note, guessing.",
      "an expert's viewing room in Paris: a table with a soft cloth, a desk lamp, a tall window with the Eiffel Tower",
      "the experts looking at the vase and making a guess",
      "any readable letters"),
 shot(34, "for about half a million euros.",
      f"{VASE} on the table beside a modest stack of banknotes with a \"€\" on top, about as tall as the vase.",
      "an expert's viewing room in Paris: a table with a soft cloth, a desk lamp, a tall window with the Eiffel Tower",
      "the vase with a modest stack of cash beside it",
      "a huge tower of cash, any letters"),
 shot(35, "It sold for sixteen million.",
      f"The gavel slams down with impact lines. Beside {VASE} stands a tower of banknotes with \"€\" symbols reaching "
      f"the chandelier. In the front row, {COUPLE} fall back in their chairs, overjoyed.",
      PARIS_ROOM,
      "the gavel coming down, the vase, the giant cash tower, the same couple overjoyed",
      "any letters"),
 shot(36, "So, have you checked your attic?",
      "A friendly stick figure faces the viewer and points up at an open attic hatch in the ceiling with a ladder "
      "folded down, with a curious grin; a big question mark floats above.",
      "a house hallway: the attic hatch in the ceiling, the folding ladder, a plain wall, a picture frame",
      "the stick figure pointing up at the attic hatch, and the question mark",
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
