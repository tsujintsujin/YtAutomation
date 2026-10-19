"""Image prompts for nail-sandwich-nugget-declaration, written as one story (the worked example for
channels/SHORTS_RULES.md "How image prompts are written"). Writes scene + full prompt for every line into script.json.
usage: python channels/found-rich/videos/nail-sandwich-nugget-declaration/scenes.py"""
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent                 # videos/<slug>
ROOT = HERE.parents[3]                                 # YtAutomation
sys.path.insert(0, str(ROOT))
from dashboard import short_prompt                     # the fixed frame around every Short prompt

D = str(HERE)
STYLE = json.loads((HERE.parents[1] / "settings.json").read_text(encoding="utf-8"))["image_style"]

# ---- the same words every time a person, object or place appears ----
PAINTING = ("a small dull old painting of a plain countryside (two low rolling hills, one small round tree, "
            "an empty sky, drawn with a few loose lines), in a big heavy ornate wooden frame with curly carved corners; "
            "about as wide as a shoebox, a little wider than tall")
TAG4 = 'a small paper price tag on a string hanging from the frame\'s lower corner, showing "$4"'
MARKET_TABLE = ("a flea-market folding table under a simple peaked tent roof, with junk on it: an old lamp, a stack of "
                "plates, a teapot, a few old books")
CREW = ("a stick-figure man with a baseball cap worn backwards, a plain short-sleeved T-shirt outline "
        "(no tie, no suit, no collar) and a lanyard round his neck with a small square badge on his chest")
NAIL = ("one press-on fake fingernail on its own, NOT attached to any finger: thin and flat like a real "
        "fingernail, shaped like a long narrow almond that tapers to a sharp point, gently curved, glossy (two short "
        "shine lines), with one small gem doodle near its wide base; it must read as a fingernail, never as a cone, a "
        "bullet, a tooth or an object standing upright")
STAGE = ("the concert stage after the show is over, with wide wooden floorboards; a long metal lighting truss (a beam of criss-cross "
         "lines) hanging high above with a row of round stage spotlights; a tall stack of black speaker boxes on the "
         "right side of the stage; beyond the front edge of the stage, rows of empty seats; confetti scraps, a few stray "
         "feathers and empty plastic cups on the floorboards")
FLAT = ("his small flat, with a plain wooden desk against the wall, a desk chair, a window with simple curtains showing a "
        "few rooftops, a small shelf with a mug")
WOMAN = ("a stick-figure woman with a high ponytail tied with a small bow and a simple triangle dress "
         "outline")
KITCHEN = ("her kitchen in Miami, with a counter with a stove and a frying pan, a fridge, upper cupboards with one open "
           "shelf, a small round table with two chairs, and a window behind the counter with one palm tree and a "
           "round sun outside")
SANDWICH = ("a grilled cheese sandwich made of two square slices of toasted bread with a few short toasting lines on top, melted "
            "cheese drooping out over the edges, nothing else inside (no lettuce, no meat, no tomato); drawn in black ink "
            "lines only on white, no yellow, no brown, no colour")
BITE = "one curved bite missing from its top-right corner"
FACE = ("burned into the top slice in thin black toasting lines: the image of the Virgin Mary, a serene woman's face "
        "with a long veil draped over her head and falling past her shoulders, eyes gently looking down, a small calm "
        "mouth, exactly like the classic Virgin Mary image people saw in this famous sandwich; black ink lines only, no "
        "brown, no yellow, never a smiley face or an emoji face in a circle")
BOX = "a clear plastic display box with a lid, drawn with thin outline lines, the sandwich inside on a small plate"
BUYER = ("a stick-figure man in a suit jacket with a tie, slicked-back hair and a big showman grin")
NUGGET = ("one chicken nugget with a funny lumpy shape: a rounded bean-shaped body, a small rounded lump "
          "on its back that is part of the same crumbly nugget (never a handle, loop or ring), and two short stubby "
          "legs at the bottom; batter texture of tiny dots; no face, "
          "no eyes, no visor, nothing drawn on it")
OWNER = ("a stick-figure person with messy spiky hair and a hoodie outline with the hood down")
DINER = ("a fast-food restaurant, with a small table with two plain chairs, a tray, a plain paper bag and an open nugget "
         "carton (no logos, no letters), a counter in the background with a menu board showing only simple food "
         "doodles (burger, fries, drink)")
ROOM = ("the nugget owner's bedroom, with a desk with an open laptop, a desk chair, a bed with a pillow, a window, a poster of "
        "simple shapes on the wall")
MAN = ("a stick-figure man with a short beard, a flat cap and a simple button-up shirt outline")
MARKET = ("an outdoor flea market in Pennsylvania, with rows of folding tables under simple peaked tent roofs, the tables "
          "covered with junk (old lamps, plates, a toy car, stacks of books, picture frames), a few trees behind, two or "
          "three other stick figures browsing")
SELLER = "a stick-figure man in a round bucket hat sitting on a folding chair behind his table"
SHOP = ("his workshop at home, with a wooden workbench, a pegboard on the wall with hanging tools (hammer, saw, "
        "screwdrivers), a small hanging lamp")
SHEET = ("a big old printed sheet of paper, taller than wide, with rough worn edges and old fold "
         "creases making a grid, covered in rows of tiny wavy lines for text and one thicker wavy line across the top "
         "as the heading (no readable letters)")
AUCTION = ("an auction room, with a wooden podium at the front with an auctioneer stick figure in a suit holding a "
           "gavel, an easel beside the podium, rows of chairs with stick-figure bidders holding up round paddles with "
           "simple numbers on them")
CALENDAR = "a wall calendar with many of its pages flying off it through the air"
CAPTIONS = ("The place fills the whole frame; keep the very top and very bottom of the frame calm (sky, wall or floor) "
            "for captions. Never write any name, label or caption under or beside anyone or anything.")


def shot(n, text, what, place, must, never=""):
    return n, text, " ".join(x for x in (
        f"This is picture {n} of 42 in one continuous picture story; draw exactly this moment.",
        what, f"Place: {place}.", f"It MUST show: {must}.", f"NEVER: {never}." if never else "", CAPTIONS) if x)


S = [
 shot(1, "A four-dollar painting",
      f"{PAINTING}, {TAG4}. It leans upright on {MARKET_TABLE}, in the middle of the frame, drawn big enough to fill "
      "about half the frame's width. Nobody is around it. It looks boring and cheap.",
      "an outdoor flea market: the table and tent roof around the painting, a tree and the next tent behind",
      "the painting with its ornate frame and the $4 tag, clearly the most important thing in the picture",
      "any money, any glow, any person"),
 shot(2, "was hiding eight million dollars.",
      f"{PAINTING}, {TAG4}, leaning on the same {MARKET_TABLE}. "
      "Now the lower-left corner of the canvas is peeled back from the frame like a page corner, and from the gap "
      "behind it bright light rays, big \"$\" symbols and banknotes burst out into the air.",
      "an outdoor flea market: the table and tent roof around the painting, a tree and the next tent behind",
      "the same painting and frame, the peeled corner, and money bursting out from behind the canvas",
      "a different painting, any person"),
 shot(3, "But first, three other weird things",
      f"Three people stand side by side in a row, each holding their own weird find out toward the viewer, with a "
      f"big question mark above each find. Left: {CREW}, holding up between two fingers {NAIL}. Middle: "
      f"{WOMAN}, holding up {SANDWICH}, {BITE}, and {FACE}. Right: {OWNER}, holding up {NUGGET}. Each find is drawn "
      "big enough to recognise.",
      "a plain street pavement with a low brick wall behind the three people and a lamp post at one side",
      "the three different people, each showing their own weird thing, with question marks; no money yet",
      "any money, a shelf, objects without people"),
 shot(4, "that made people rich.",
      f"The same three people in the same row, now rich: banknotes rain down on them from above, each holds a big "
      f"fan of cash in one hand and their weird find in the other, and each stands on a pile of money, grinning and "
      f"cheering. Left: {CREW}, holding {NAIL}. Middle: {WOMAN}, holding {SANDWICH}, {BITE}, and {FACE}. Right: "
      f"{OWNER}, holding {NUGGET}. \"$\" symbols on the money.",
      "a plain street pavement with a low brick wall behind the three people and a lamp post at one side",
      "the three people clearly getting rich (cash raining, piles of money, cheering), each still holding their find",
      "a shelf, objects without people, any colour"),
 shot(5, "A stage worker in Dublin",
      f"{CREW}. He stands in the middle of the stage holding a long push broom, smiling at the viewer, shown from head "
      "to feet.",
      STAGE,
      "the stage worker with his backwards cap, lanyard and broom, and the truss of spotlights above him",
      "a tie, a suit, any singer or real person"),
 shot(6, "was cleaning up after a Lady Gaga show.",
      f"{CREW}. Seen in a wide shot, he sweeps a big pile of confetti, feathers and plastic cups across the stage "
      "with his push broom, mid-stroke, with small motion lines at the broom. Signs of a glamorous pop show lie in "
      "the mess: a dropped sparkly high-heeled boot, a feather boa, a broken disco ball and glitter.",
      f"{STAGE}; the empty seats beyond the stage edge are clearly visible, showing the show is over",
      "the stage worker sweeping, the mess on the stage, and the empty seats",
      "a tie, a suit, any singer or performer, any real person, any poster or logo"),
 shot(7, "On the floor",
      f"{CREW}. Closer view from the side: he is bent forward over his push broom, sweeping, eyes looking down at "
      "the floorboards. Just in front of the broom bristles, among the confetti, one tiny object gives off a small "
      "glint (a little four-point sparkle). He has not noticed it yet.",
      f"{STAGE}; we see the floorboards across the bottom half of the frame, with the speaker stack and part of the "
      "truss still visible behind him",
      "the stage worker sweeping and looking at the floor, and the tiny glint in front of his broom",
      "an empty floor with no person, a tie, a suit"),
 shot(8, "he spotted something small and shiny.",
      f"{CREW}. The moment right after he saw a glint while sweeping: he has stopped sweeping, his push broom lies on the "
      "floorboards beside him, and he crouches down low, pointing at a tiny shiny object on the floor with three "
      "sparkle marks around it. His eyebrows are raised, curious.",
      f"{STAGE}; the speaker stack behind him, confetti around his feet",
      "the crouching stage worker pointing at the tiny shiny thing, the broom on the floor",
      "a tie, a suit, an angry face"),
 shot(9, "He thought it was a guitar pick.",
      f"{CREW}. He stands up, holding the tiny shiny object between his thumb and finger close to his face, "
      "squinting at it, unsure. It is so small you can only see it is shiny. A thought bubble above his head shows "
      "a plain guitar pick (a rounded triangle).",
      f"{STAGE}; his push broom leans against the speaker stack behind him",
      "the stage worker, the tiny shiny thing in his fingers, and the guitar pick in his thought bubble",
      "a tie, a suit, a whole finger or hand drawn huge"),
 shot(10, "It was one of her fake nails.",
      f"Close view: the stage worker's fingertips hold up {NAIL}, drawn big in the middle of the frame so it is "
      f"clearly a separate fake nail and not a finger. Beside it, the face of {CREW}: eyes wide, mouth a round O, "
      "shocked.",
      f"{STAGE}; only the lighting truss with its spotlights is visible above and behind him",
      "the detached fake nail held in his fingertips, and his shocked face with the backwards cap",
      "a whole finger with the nail on it, a tie, a suit"),
 shot(11, "He sold it online",
      f"{CREW}, now at home, sits on the desk chair typing on a laptop. The laptop screen faces the viewer and shows "
      f"a simple auction page: a photo of {NAIL}, a small gavel icon and an empty price box with a \"$\". On the "
      "desk beside the laptop lies the real nail inside a tiny clear zip bag.",
      FLAT,
      "the same stage worker (backwards cap, T-shirt, lanyard), the laptop screen with the nail on it",
      "an empty desk with no person, a tie, a suit, any website logo or letters"),
 shot(12, "for about twelve thousand dollars.",
      f"{CREW} at home, the moment the auction ends: he leaps up off his desk chair with both arms in the air and a "
      "huge grin. The laptop screen shows \"$12,000\" big, with the small gavel icon. On the desk next to the "
      "laptop stands a tall stack of banknotes with a \"$\" on top; the tiny zip bag is gone.",
      FLAT,
      "the same stage worker cheering, the $12,000 on the laptop screen, the stack of cash",
      "a tie, a suit"),
 shot(13, "A woman in Miami",
      f"{WOMAN}. She stands in her kitchen next to the counter, waving at the viewer with a friendly smile, shown "
      "from head to feet.",
      KITCHEN,
      "the woman with her ponytail and bow, her kitchen, and the palm tree through the window",
      "any other person"),
 shot(14, "did even better with her lunch.",
      f"A side-by-side comparison. Left, smaller: {CREW}, standing beside a small stack of banknotes with a \"$\" "
      f"on top, holding {NAIL}. Right, bigger: {WOMAN}, standing in her kitchen holding a plate with {SANDWICH} "
      "(whole, no bite yet), beside a stack of banknotes twice as tall as his, with a \"$\" on top. She looks at "
      "the viewer with a smug, confident smile and one eyebrow raised.",
      f"left half: a bit of the concert stage floorboards behind the stage worker; right half: {KITCHEN}",
      "the woman's cash stack clearly twice as tall as the stage worker's, and her lunch plate with the grilled cheese",
      "any thought bubble, a bite out of the sandwich yet"),
 shot(15, "She made a grilled cheese sandwich, took one bite,",
      f"{WOMAN}. She sits at the small round kitchen table holding {SANDWICH}, {BITE}, chewing with her cheeks puffed "
      "and a few crumbs falling. The empty frying pan is on the stove behind her.",
      KITCHEN,
      "the same woman, the grilled cheese with the bite clearly missing from its top-right corner, and her chewing",
      "a face on the toast yet, any other kind of sandwich"),
 shot(16, "and saw a face in the toast.",
      f"Closer view: {WOMAN}, still at the kitchen table, holds the same sandwich in front of her face: {SANDWICH}, "
      f"{BITE}, and {FACE}. She has stopped chewing; her eyes are wide and she leans in to look at it.",
      f"{KITCHEN}; the window with the palm tree behind her",
      "the grilled cheese with the bite missing AND the face on the toast, and the same ponytail woman staring at it",
      "a plain slice of bread, a smiley cartoon face, any other person"),
 shot(17, "To her, it looked like the Virgin Mary.",
      f"{WOMAN} stands in her kitchen holding the same sandwich high above her head with both hands: {SANDWICH}, "
      f"{BITE}, and {FACE}. A soft round halo ring and gentle light rays shine around the sandwich, with small "
      "sparkle marks. She gazes up at it in awe, mouth open.",
      KITCHEN,
      "the exact same grilled cheese with its bite and its face, glowing, held up by the same ponytail woman",
      "a different sandwich, lettuce or any filling, a sandwich without the face, a woman without the ponytail, any "
      "cartoon smiley face"),
 shot(18, "So she kept it.",
      f"{WOMAN} carefully lowers the lid onto {BOX}; the sandwich inside is {SANDWICH}, {BITE}, and {FACE}. The box "
      "stands on the open kitchen shelf; she smiles proudly.",
      KITCHEN,
      "the same woman, the clear box on the kitchen shelf, the sandwich inside with its bite and face",
      "a different sandwich"),
 shot(19, "For ten years.",
      f"The same open kitchen shelf with {BOX}; the sandwich inside is {SANDWICH}, {BITE}, and {FACE}. Dust lines on "
      f"the lid and a cobweb in the shelf corner. Next to the shelf hangs {CALENDAR}.",
      KITCHEN,
      "the boxed sandwich with its bite and face, dust and cobweb, and the calendar pages flying",
      "a different sandwich, any person"),
 shot(20, "In 2004, an online casino",
      f"{BUYER}. He sits at an office desk in front of a big laptop and points at its screen, grinning. The screen "
      "faces the viewer and shows a casino WEBSITE: on its left half a small slot machine doodle, two dice and "
      f"playing cards with \"$\" symbols; on its right half a photo of the boxed grilled cheese (the sandwich with "
      "the bite and the face, in its clear box) with a small gavel icon next to it.",
      "his office: the desk with a small desk calendar showing \"2004\", an office chair, a window with tall city "
      "buildings, a framed \"$\" picture on the wall",
      "the casino man at the laptop, the casino website on the screen, and the boxed sandwich on that website",
      "a real slot machine standing in the room, any casino logo or letters"),
 shot(21, "paid twenty-eight thousand dollars for it.",
      f"{WOMAN} sits at the small round kitchen table at an open laptop, both arms up, cheering. The laptop screen "
      f"faces the viewer and shows the online auction: a photo of {BOX} with the sandwich inside ({SANDWICH}, "
      f"{BITE}, and {FACE}), a small gavel icon, and \"$28,000\" big. On the table beside the laptop lies a big "
      "pile of banknotes with \"$\" symbols.",
      KITCHEN,
      "the same ponytail woman cheering, $28,000 on the laptop screen with the boxed sandwich, and the pile of cash",
      "the casino man in the kitchen, a different sandwich, a woman without the ponytail, any logo or letters"),
 shot(22, "Then came a single chicken nugget.",
      f"{NUGGET}, alone on a small paper tray in the middle of a fast-food restaurant table, drawn big, with small "
      "sparkle marks around it. Nothing else on the table.",
      DINER,
      "the one lumpy nugget alone on its tray, the clear star of the picture",
      "any game character, any face on the nugget, any person, any logo or letters"),
 shot(23, "In 2021, someone got a McDonald's nugget",
      f"{OWNER}. They sit at the restaurant table eating, about to dip a nugget; the open carton is full of ordinary "
      "nuggets. They have not noticed anything yet.",
      DINER,
      "the nugget owner with spiky hair and hoodie at the fast-food table with the nugget carton",
      "any logo, any golden arches, any letters, any mascot or real person"),
 shot(24, "shaped like a crewmate from the game Among Us.",
      f"{OWNER}, still at the restaurant table, holds one nugget up close to their face, laughing and pointing at "
      f"it. The nugget is drawn big: {NUGGET}.",
      DINER,
      "the same owner laughing at the lumpy nugget with its backpack bump and two stubby legs",
      "any game character, any visor or face on the nugget, any colour, any logo or letters"),
 shot(25, "They put it on eBay",
      f"{OWNER}, now at home, stands at the desk taking a photo with a phone of {NUGGET} lying on a small plate. "
      "The phone screen shows the nugget too.",
      ROOM,
      "the same owner photographing the same lumpy nugget on a plate",
      "any logo or letters, any game character"),
 shot(26, "for ninety-nine cents.",
      f"Close view of the laptop on the owner's desk: the screen shows a simple auction page with a photo of "
      f"{NUGGET}, a small gavel icon and a price tag showing \"$0.99\". The owner's hand rests on the keyboard; the "
      "real nugget on its plate sits beside the laptop.",
      f"{ROOM}; the desk and part of the window visible around the laptop",
      "the auction page with the same nugget and the $0.99 price",
      "any website logo or letters, any game character"),
 shot(27, "A hundred and eighty-four bids later,",
      f"{OWNER} sits at the desk, leaning back in the chair in shock, hands on head. The laptop screen shows the "
      f"nugget photo ({NUGGET}) and, around it, a crowd of many tiny stick-figure bidders squeezed onto the screen, "
      "each raising a small paddle with a \"$\" on it, while a steep arrow climbs up out of the top of the screen.",
      ROOM,
      "the same owner shocked, the laptop with the nugget and the crowd of bidders raising $ paddles",
      "any logo or letters, any game character"),
 shot(28, "it sold for ninety-nine thousand, nine hundred and ninety-seven dollars.",
      f"{OWNER} jumps in the air in the bedroom, both arms up, huge grin. The laptop screen shows \"$99,997\" big "
      f"with the gavel icon. Next to the laptop stands a tall tower of banknotes with a \"$\" on top, and {NUGGET} "
      "on its small plate.",
      ROOM,
      "the same owner celebrating, $99,997 on the screen, the cash tower and the nugget",
      "any logo, any game character"),
 shot(29, "Now, the painting.",
      f"The same painting from the very first picture: {PAINTING}, {TAG4}. It leans upright on the same "
      f"{MARKET_TABLE}, in the middle of the frame, with a spotlight cone shining down on it.",
      "the outdoor flea market: the table and tent roof around the painting, a tree and the next tent behind",
      "the exact same painting, frame and $4 tag as the first picture, under a spotlight",
      "any money, any glow from behind the canvas, any person"),
 shot(30, "A man bought it at a flea market in Pennsylvania",
      f"{MAN} walks between the tables, stops and looks at {PAINTING}, {TAG4}, leaning on a table among the junk. "
      "He rubs his beard, interested.",
      MARKET,
      "the frame man with beard and flat cap noticing the same painting with its $4 tag at the flea market",
      "any letters or shop signs"),
 shot(31, "for four dollars.",
      f"{MAN} stands at the seller's table and hands four banknotes, each marked \"$1\", across the table to "
      f"{SELLER}, who hands him {PAINTING} with its $4 tag. Both smile.",
      MARKET,
      "the same frame man, the seller in the bucket hat, four $1 bills and the same painting changing hands",
      "a different painting"),
 shot(32, "He only wanted the frame.",
      f"{MAN} at home holds {PAINTING} at arm's length. He makes a bored face and a thumbs-down at the dull "
      "countryside picture, while a big heart floats over the fancy carved frame corner he points at.",
      SHOP,
      "the same frame man, the same painting, the thumbs-down at the picture and the heart over the frame",
      "a different painting"),
 shot(33, "When he took it apart,",
      f"The same painting's frame (the big ornate frame with curly carved corners) lies face down on the workbench. "
      f"{MAN} pries the thin backboard off the back with a flat screwdriver; a few tiny nails pop out with motion "
      "lines.",
      SHOP,
      "the same frame man opening the back of the same frame on the workbench",
      "a different frame"),
 shot(34, "he found a folded paper hidden behind the canvas.",
      f"{MAN} lifts a small folded packet of old yellowed paper out of the opened back of the frame on the workbench "
      "(the backboard set aside, the back of the canvas showing). His eyes are wide, eyebrows high.",
      SHOP,
      "the same frame man pulling the folded old paper out from behind the canvas of the same frame",
      "readable letters"),
 shot(35, "It was an original copy of the Declaration of Independence,",
      f"{MAN} holds up {SHEET}, fully unfolded, with both arms stretched out; his jaw drops. Small glow lines and "
      "sparkles around the sheet. The empty frame lies on the workbench behind him.",
      SHOP,
      "the same frame man holding up the big old printed sheet with fold creases",
      "readable letters or words, any real person's face or portrait"),
 shot(36, "printed in 1776.",
      f"An old wooden hand printing press in an old print shop. A printer stick figure in an apron and a three-cornered "
      f"hat pulls the long press lever; {SHEET} comes out of the press fresh and flat (no folds yet). A small plaque on "
      "the wall shows \"1776\".",
      "an old print shop: brick walls, a candle lantern, shelves of ink pots and paper stacks",
      "the old printing press making the same big sheet, and 1776 on the plaque",
      "readable letters or words, any real person's face"),
 shot(37, "Only about two dozen are known.",
      f"A long museum wall, mostly empty, with only a few framed copies of {SHEET} hanging far apart, each with a "
      "small spotlight above it.",
      "a museum gallery: a long plain wall, a polished floor, a bench, a velvet rope on posts",
      "the long, mostly empty wall with only a few framed copies: they are rare",
      "readable letters, any person"),
 shot(38, "In 1991",
      f"{AUCTION}. {SHEET}, now in a glass frame, stands on the easel. The auctioneer raises his gavel. A small "
      "sign on the front of the podium shows \"1991\".",
      "the auction room, filling the frame",
      "the auction room, the framed sheet on the easel, the raised gavel, 1991 on the podium sign",
      "readable letters"),
 shot(39, "it sold for two point four million dollars.",
      f"{AUCTION}. The gavel slams down with impact lines. {SHEET} in its glass frame stands on the easel next to a "
      "big stack of banknotes with a \"$\" on top. Bidders hold up paddles; one shouts with a big open mouth.",
      "the same auction room, filling the frame",
      "the gavel coming down, the same framed sheet and the stack of cash",
      "readable letters"),
 shot(40, "Nine years later",
      f"{SHEET} in its glass frame stands on an easel at the front of a new, grander auction room with tall "
      f"windows and a chandelier. On the wall beside it hangs {CALENDAR}.",
      "a grand auction room: the easel and podium at the front, rows of chairs, tall windows, a chandelier",
      "the same framed sheet on the easel and the calendar pages flying",
      "readable letters"),
 shot(41, "it sold again, for eight million.",
      f"The same grand auction room. {SHEET} in its glass frame stands on the easel next to a tower of banknotes "
      "with \"$\" symbols that reaches all the way up to the chandelier. The auctioneer's gavel slams down; the "
      "stick-figure crowd gasps with hands on cheeks.",
      "the grand auction room with tall windows and a chandelier",
      "the same framed sheet, the huge cash tower, the gasping crowd",
      "readable letters"),
 shot(42, "What's the weirdest thing you've ever found?",
      "A friendly stick figure faces the viewer, holding an open cardboard box toward the camera; a big question "
      "mark floats up out of the box. The figure shrugs with a curious grin, inviting the viewer to answer.",
      "a dusty attic: sloped wooden roof beams, stacked cardboard boxes, an old lamp, a small round window",
      "the stick figure, the open box and the big question mark",
      "any letters"),
]

p = HERE / "script.json"
data = json.load(open(p, encoding="utf-8"))
segs = data["segments"]
assert len(segs) == len(S) == 42
for seg, (n, text, scene) in zip(segs, S):
    assert seg["id"] == n and seg["text"] == text, (n, seg["text"], text)
    seg["scene"] = scene
    seg["prompt"] = short_prompt(scene, STYLE)
json.dump(data, open(p, "w", encoding="utf-8"), indent=1, ensure_ascii=False)
print("written", len(segs), "longest", max(len(s["prompt"]) for s in segs), "shortest", min(len(s["prompt"]) for s in segs))
