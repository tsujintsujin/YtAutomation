"""Image prompts for cheeto-console-moonbag, written as one story (channels/SHORTS_RULES.md "How image prompts are written";
worked example: ../nail-sandwich-nugget-declaration/scenes.py). Checks every line against script.md; once the script
is approved (right away: no approval step, this file approves it) writes scene + full prompt for every line into script.json.
usage: python channels/found-rich/videos/cheeto-console-moonbag/scenes.py"""
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent                 # videos/<slug>
ROOT = HERE.parents[3]                                 # YtAutomation
sys.path.insert(0, str(ROOT))
from dashboard import approve, short_lines, short_prompt       # the script's lines, and the fixed frame around every prompt

STYLE = json.loads((HERE.parents[1] / "settings.json").read_text(encoding="utf-8"))["image_style"]
TOTAL = 46

# ---- the same words every time a person, object or place appears ----
LAWYER = "a stick-figure woman with a sleek straight bob haircut, a neat suit jacket and small earrings"
BAG = ("a flat white cloth pouch about the size of a folded sheet of paper, with a zip along its top edge and a small "
       "pull tab; plain, no writing, no logo; black ink outline only")
DUST = "fine grey moon dust drawn as tiny dots (black ink dots only, no colour)"
OFFICE = ("her law office in Chicago: a desk with a laptop and a stack of files, a bookshelf of thick law books, a big "
          "window with tall city towers outside")
LAB = ("a space agency science lab: white walls, long white benches, a big microscope, a glass glovebox with two rubber gloves "
       "built into the front, bright ceiling lights")
SCIENTIST = "a stick-figure scientist in a white lab coat, safety glasses and plain gloves"
ASTRONAUT = ("a stick-figure astronaut in a bulky white spacesuit with a round helmet and a dark visor, a big square "
             "backpack and thick gloves; no flag patches, no letters")
MOON = ("the surface of the moon: grey dusty ground with small craters and rocks drawn in outline, footprints, a "
        "black sky with stars, the round Earth hanging in the sky, and a four-legged moon lander with a boxy body and "
        "thin legs standing nearby")
SHOPMAN = "a stick-figure man with a backwards baseball cap, a goatee and a polo shirt"
CARDSHOP = ("a small trading-card shop in Georgia: glass counters full of trading cards in plastic sleeves, framed cards "
            "on the walls, a cash register, and a big grey safe in the back corner")
CHEETO = ("a single crunchy puffed snack about as long as a finger, bumpy all over, that by pure chance has curled into "
          "the shape of a tiny dragon: a small head with a snout, two small pointed wing bumps and a curled tail; "
          "black ink lines only, no orange, no colour; never a cartoon character, never eyes or a face")
CASE = "a small clear plastic display case"
TERRY = "a stick-figure man with short grey hair, a moustache and a knitted sweater"
SON = "a stick-figure teenage son with shaggy hair and a hoodie"
BOX = "a plain cardboard box full of old office junk: folders, a desk lamp, cables, a stapler, with no writing on it"
CONSOLE = ("a grey boxy game console: a flat wide body, a round hinged lid on top for CDs, a slot at the front for game "
           "cartridges, and a square game controller attached by a cable; no logo, no letters; black ink lines only")
ATTIC = ("a dusty attic under a sloping wooden roof: bare rafters, a small window letting in a beam of light, old "
         "suitcases, a rolled-up rug, cobwebs, a plank floor")
OFFICE_AUCTION = ("an auction in an emptied company office: bare desks pushed together, swivel chairs in rows, an "
                  "auctioneer stick figure in a suit standing on a small box with a gavel, stick-figure bidders holding "
                  "up round paddles, cardboard boxes of office things lined up on a table")
AUCTION = ("an auction room: a wooden podium at the front with an auctioneer stick figure in a suit holding a gavel, a "
           "small display stand beside the podium, rows of chairs with stick-figure bidders holding up round paddles")
CAPTIONS = ("The place fills the whole frame; keep the very top and very bottom of the frame calm (sky, wall or floor) "
            "for captions. Never write any name, label or caption under or beside anyone or anything.")


def shot(n, text, what, place, must, never=""):
    return n, text, " ".join(x for x in (
        f"This is picture {n} of {TOTAL} in one continuous picture story; draw exactly this moment.",
        what, f"Place: {place}.", f"It MUST show: {must}.", f"NEVER: {never}." if never else "", CAPTIONS) if x)


S = [
 shot(1, "A woman paid nine hundred ninety-five dollars",
      f"{LAWYER} sits at her desk and clicks a button on her laptop; the laptop screen shows \"$995\" big.",
      OFFICE,
      "the woman paying $995 on her laptop",
      "any other numbers or letters, any moon yet"),
 shot(2, "for an old zipper bag.",
      f"{LAWYER} holds up {BAG} by one corner, looking at it, unimpressed, one eyebrow raised.",
      OFFICE,
      "the woman holding up the plain flat zipper bag",
      "any writing on the bag, any dust yet"),
 shot(3, "It had dust from the moon inside,",
      f"{BAG} lies unzipped on the desk; inside it shows a little {DUST}; a small round moon with craters glows "
      "above the bag with sparkle lines.",
      OFFICE,
      "the open bag with grey moon dust inside and the moon above it",
      "any colour, any letters"),
 shot(4, "and it sold for one point eight million.",
      f"{BAG} on the desk beside a tower of banknotes with \"$\" symbols reaching the top of the frame; sparkle marks.",
      OFFICE,
      "the plain bag beside a huge tower of cash",
      "any person, any letters"),
 shot(5, "But first, two more strange buys",
      f"Two people side by side, a big question mark above each. Left: {SHOPMAN}, holding up {CASE} with {CHEETO} "
      f"inside. Right: {TERRY}, holding {BOX}.",
      "a plain town pavement with a low brick wall behind the people and a lamp post at one side",
      "the man with the tiny dragon-shaped snack in a case, and the man with the box of office junk",
      "any money yet, any cartoon character, any letters"),
 shot(6, "that turned into big money.",
      f"The same two people in the same places cheering as banknotes rain down: {SHOPMAN} with {CASE} holding "
      f"{CHEETO}; {TERRY} with {BOX}.",
      "a plain town pavement with a low brick wall behind the people and a lamp post at one side",
      "the same two people getting rich, money raining down",
      "any letters"),
 shot(7, "In Georgia, a man who owns a card shop",
      f"{SHOPMAN} stands behind his glass counter full of trading cards, arms spread proudly.",
      CARDSHOP,
      "the man in the backwards cap in his trading-card shop",
      "any readable card names or letters, any cartoon characters on the cards"),
 shot(8, "bought a single Cheeto online",
      f"{SHOPMAN} sits at a computer at the shop counter; the computer screen shows a photo of {CHEETO}, alone.",
      CARDSHOP,
      "the man looking at one single snack on his computer screen",
      "a whole bag of snacks, any letters"),
 shot(9, "for three hundred fifty dollars.",
      f"{SHOPMAN} clicks the mouse with a grin; the computer screen shows \"$350\" big beside the photo of the snack.",
      CARDSHOP,
      "the man paying $350 for the one snack",
      "any other numbers or letters"),
 shot(10, "It was shaped just like the Pokémon Charizard.",
      f"Close view: {CHEETO}, drawn big in the middle of the frame inside {CASE}, sparkle marks around it.",
      f"{CARDSHOP}; only the glass counter shows behind",
      "the snack's dragon shape up close: head, wing bumps, curled tail",
      "any cartoon character, any eyes or face, any colour, any letters"),
 shot(11, "Then he forgot about it.",
      f"{SHOPMAN} puts {CASE} with {CHEETO} into the big grey safe and swings the door shut, already looking away and "
      "whistling, musical notes in the air.",
      CARDSHOP,
      "the man shutting the snack in the safe and forgetting it",
      "any letters"),
 shot(12, "It sat in his safe for about five years.",
      "The big grey safe, door shut, with cobwebs on it and dust; on the wall above it a calendar with many pages "
      "flying off.",
      CARDSHOP,
      "the shut safe gathering cobwebs and time flying by",
      "any person, any letters or numbers"),
 shot(13, "When he found it again,",
      f"{SHOPMAN}, holding a feather duster, has the safe door open and holds up {CASE} with {CHEETO}, eyebrows up in "
      "surprise.",
      CARDSHOP,
      "the man finding the snack again while cleaning",
      "any letters"),
 shot(14, "he sold it for ten thousand dollars.",
      f"At a busy collectors' fair table, {SHOPMAN} hands {CASE} with {CHEETO} to a buyer stick figure in a "
      "smart jacket, and gets a small stack of banknotes with a \"$\" on top.",
      "a collectors' convention hall: rows of tables with trading cards and toys, banners with no letters, crowds",
      "the man selling the snack and getting a small stack of cash",
      "any letters"),
 shot(15, "And in twenty twenty-five,",
      f"{CASE} with {CHEETO} on a small stand; beside it a wall calendar shows \"2025\".",
      "an auction company's photo studio: a plain white backdrop, a camera on a tripod, soft lights",
      "the snack in its case and 2025 on the calendar",
      "any person, any letters other than 2025"),
 shot(16, "it sold again at an auction,",
      f"A giant screen on a wall shows a photo of {CASE} with {CHEETO}, with arrows going up; in front of it many "
      "stick figures at laptops excitedly clicking to bid.",
      "a big room with a wall screen and rows of desks with laptops",
      "an online auction for the snack with bids going up",
      "any letters or numbers"),
 shot(17, "for over eighty-seven thousand dollars.",
      f"{CASE} with {CHEETO} on a small stand beside a tall stack of banknotes with \"$\" symbols; sparkle marks.",
      "an auction company's photo studio: a plain white backdrop, soft lights",
      "the tiny snack next to a tall stack of cash",
      "any person, any letters"),
 shot(18, "For one Cheeto.",
      f"{CHEETO} alone on a huge empty table; a stick figure leans in close, staring at it with a baffled face and "
      "one hand scratching his head.",
      "a plain room with a long table and a plain wall",
      "the funny contrast: one tiny snack, one baffled person",
      "any money, any letters"),
 shot(19, "Then a man bought a box of old stuff",
      f"{TERRY} lifts {BOX} up from a table of boxes and peers inside.",
      OFFICE_AUCTION,
      "the man in the sweater picking up a box of office junk",
      "the console yet, any letters"),
 shot(20, "at an auction for seventy-five dollars.",
      f"The auctioneer points his gavel at {TERRY}, who holds up his paddle; {BOX} sits in front of him with a small "
      "paper tag on it showing \"$75\".",
      OFFICE_AUCTION,
      "the man winning the box at the office auction, $75 on the tag",
      "any other numbers or letters"),
 shot(21, "The box came from the office",
      "An empty company office: bare desks, chairs stacked upside down, cardboard boxes everywhere, dead plants, "
      "lights off.",
      "the emptied company office with tall windows onto a city",
      "an empty, closed-down office full of boxes",
      "any person, any letters or logos"),
 shot(22, "of a company that went broke.",
      "In the empty office, a sad boss stick figure in a suit turns out his empty trouser pockets; a moth flutters out; "
      "a small storm cloud over his head.",
      "the emptied company office with tall windows onto a city",
      "a company boss with no money left",
      "any letters or logos"),
 shot(23, "It sat in his attic for years.",
      f"{BOX} sits in a corner of the attic among old suitcases, covered in dust and cobwebs.",
      ATTIC,
      "the box forgotten in a dusty attic",
      "any person, any letters"),
 shot(24, "Then his son looked inside",
      f"{SON} kneels in the attic and opens the flaps of {BOX}, shining a phone torch inside.",
      ATTIC,
      "the teenage son opening the old box in the attic",
      "the console yet, any letters"),
 shot(25, "and found a strange game console.",
      f"{SON} lifts {CONSOLE} out of the box with both hands, eyes wide, mouth open.",
      ATTIC,
      "the son holding up the strange grey game console",
      "any logo or letters"),
 shot(26, "Nintendo and Sony had made it together,",
      f"Two engineer stick figures in shirts and ties, one on each side of a workbench, shake hands over {CONSOLE}.",
      "an early-1990s electronics workshop: workbenches with soldering irons, chunky beige computers with boxy "
      "screens, wires and circuit boards",
      "two people from two companies shaking hands over the console they made together",
      "any logos, any company names, any letters"),
 shot(27, "back when they were partners.",
      "The same two engineers walk side by side arm in arm, smiling, past rows of chunky early-1990s computers.",
      "an early-1990s electronics workshop: workbenches with soldering irons, chunky beige computers with boxy "
      "screens, wires and circuit boards",
      "the two partners being friends back then",
      "any logos or letters"),
 shot(28, "Only about two hundred were made,",
      f"A long factory table with rows and rows of identical {CONSOLE.replace('a grey boxy', 'grey boxy')}, many of "
      "them.",
      "a small factory room: long tables, overhead lamps, a conveyor belt",
      "many identical consoles in rows",
      "any letters or numbers"),
 shot(29, "and it's the only one known to still exist.",
      f"{CONSOLE}, alone in the middle of the frame, under a spotlight cone; empty space all around.",
      "a dark plain room, only the spotlight",
      "just one console left, alone under a spotlight",
      "any other console, any person, any letters"),
 shot(30, "In twenty twenty,",
      f"{AUCTION}. On the display stand sits {CONSOLE}. A small sign on the front of the podium shows \"2020\".",
      "the auction room, filling the frame",
      "the auction room, the console on its stand, 2020 on the podium sign",
      "any letters other than 2020"),
 shot(31, "it sold for three hundred sixty thousand dollars.",
      f"{AUCTION}. The gavel slams down with impact lines. Beside {CONSOLE} stands a tall stack of banknotes with "
      f"a \"$\" on top.",
      "the same auction room, filling the frame",
      "the gavel coming down, the console and the tall stack of cash",
      "any letters"),
 shot(32, "Now, the bag.",
      f"{BAG}, alone in the middle of the frame, under a spotlight cone.",
      f"{OFFICE}; dim behind the spotlight",
      "the plain zipper bag under a spotlight",
      "any person, any dust showing, any letters"),
 shot(33, "In twenty fifteen, a lawyer near Chicago",
      f"{LAWYER} sits at her desk with files; a small desk calendar shows \"2015\".",
      OFFICE,
      "the lawyer in her Chicago office, 2015 on the calendar",
      "any letters other than 2015"),
 shot(34, "saw it on a government auction website.",
      f"{LAWYER} leans toward her laptop; the screen shows a simple web page with a photo of {BAG} and a small "
      "eagle-shaped government seal (no letters).",
      OFFICE,
      "the lawyer looking at the bag for sale on a government website",
      "any readable words"),
 shot(35, "She paid nine hundred ninety-five dollars.",
      f"{LAWYER} clicks the mouse with a small smile; the laptop screen shows \"$995\" big beside the photo of the bag.",
      OFFICE,
      "the lawyer paying $995",
      "any other numbers or letters"),
 shot(36, "She sent it to NASA to be tested.",
      f"{SCIENTIST} holds {BAG} inside the glass glovebox with the built-in gloves; another scientist takes notes.",
      LAB,
      "scientists testing the bag in a lab",
      "any logos or letters"),
 shot(37, "There was moon dust inside.",
      f"Close view through a round microscope view (a circle filling the frame): {DUST}, little rough grains in the "
      "circle.",
      "the round microscope view fills the frame, the lab bench just visible around the edges",
      "grains of moon dust seen up close",
      "any colour, any letters"),
 shot(38, "It was the bag from the very first moon landing,",
      f"{ASTRONAUT} stands on the moon beside the lander, holding {BAG} in one gloved hand.",
      MOON,
      "an astronaut on the moon with the same zipper bag",
      "any flag with letters, any likeness of a real person"),
 shot(39, "in nineteen sixty-nine.",
      "A family of four in nineteen-sixties clothes sits on a sofa in front of a small boxy television on legs; on the "
      "screen a tiny astronaut on the moon; a wall calendar shows \"1969\".",
      "a nineteen-sixties living room: patterned wallpaper, a lamp with a round shade, a rug",
      "a family watching the moon landing on an old TV, 1969 on the calendar",
      "any letters other than 1969"),
 shot(40, "It held the first bits of the moon",
      f"{ASTRONAUT} bends and scoops moon dirt with a small long-handled scoop into {BAG}, held open in the other hand.",
      MOON,
      "the astronaut putting moon dirt into the bag",
      "any letters"),
 shot(41, "anyone ever picked up.",
      f"Close view: the astronaut's thick glove holding the small scoop full of {DUST}; boot footprints in the grey "
      "dust around it; the Earth in the black sky.",
      MOON,
      "the very first scoop of moon dirt up close",
      "any colour, any letters"),
 shot(42, "NASA wanted to keep it,",
      f"In the lab, a space agency man stick figure in a white shirt and tie hides a bag behind his back, the bag being {BAG}; {LAWYER} stands "
      "facing him, pointing at it, upset.",
      LAB,
      "the space agency man keeping the bag and the lawyer upset",
      "any logos or letters"),
 shot(43, "so she went to court, and she won.",
      f"A courtroom: a judge stick figure in a black robe at a high wooden bench bangs a gavel; {LAWYER} throws both "
      "fists up in joy at her table.",
      "a courtroom: a high wooden judge's bench, wooden tables, rows of benches, tall windows",
      "the judge's gavel and the lawyer celebrating her win",
      "any letters"),
 shot(44, "In twenty seventeen,",
      f"{AUCTION}. On the display stand lies {BAG}. A small sign on the front of the podium shows \"2017\".",
      "the auction room, filling the frame",
      "the auction room, the bag on its stand, 2017 on the podium sign",
      "any letters other than 2017"),
 shot(45, "the bag sold for one point eight million dollars.",
      f"{AUCTION}. The gavel slams down with impact lines. Beside {BAG} rises a tower of banknotes with \"$\" "
      f"symbols reaching the top of the frame.",
      "the same auction room, filling the frame",
      "the gavel coming down, the bag and the giant cash tower",
      "any letters"),
 shot(46, "What strange thing would you buy?",
      "A friendly stick figure faces the viewer, sitting at a laptop with one finger on their chin, thinking, with a "
      "curious grin; a big question mark floats above.",
      "a cosy living room: a sofa, a small table with the laptop, a window",
      "the stick figure thinking about what to buy, and the question mark",
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
