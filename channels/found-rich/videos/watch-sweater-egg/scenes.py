"""Image prompts for watch-sweater-egg, written as one story (channels/SHORTS_RULES.md "How image prompts are written";
worked example: ../nail-sandwich-nugget-declaration/scenes.py). Checks every line against script.md; once the script
is approved (script.json exists) writes scene + full prompt for every line into script.json.
usage: python channels/found-rich/videos/watch-sweater-egg/scenes.py"""
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent                 # videos/<slug>
ROOT = HERE.parents[3]                                 # YtAutomation
sys.path.insert(0, str(ROOT))
from dashboard import short_lines, short_prompt        # the script's lines, and the fixed frame around every prompt

STYLE = json.loads((HERE.parents[1] / "settings.json").read_text(encoding="utf-8"))["image_style"]
TOTAL = 39

# ---- the same words every time a person, object or place appears ----
EGG = ("a small golden egg about as tall as a hand, egg-shaped, covered with thin upright ridges from top to bottom, "
       "with a band of tiny round gem dots around its middle, standing on a small round stand with three short "
       "curved feet; drawn in black ink lines only, no yellow, no gold colour, no colour")
EGG_OPEN = ("the same golden egg with its top half swung open on a little hinge, and inside it a tiny round clock face "
            "with two hands and tick marks (no numbers, no letters)")
DEALER = ("a stick-figure man with a thick moustache, a flat cap, a work apron over his shirt and thick work gloves")
SELLER = "a stick-figure man in a round bucket hat sitting on a folding chair behind his table"
MARKET = ("an outdoor flea market in the American Midwest: rows of folding tables under simple peaked tent roofs, "
          "covered with old things (lamps, plates, tools, old clocks), flat farmland behind with one tall round water "
          "tower and a plain wooden barn")
YARD = ("his scrap metal yard: piles of old metal (pipes, wheels, pots, bent bicycle frames), a chain-link fence, a "
        "small wooden shed with a workbench, and on the ground a big round melting pot on a small metal furnace")
NIGHT_KITCHEN = ("his small kitchen at night: a wooden table with a laptop on it, a hanging lamp above the table, a "
                 "window showing a dark sky with a crescent moon and a few stars, a fridge and a stove behind")
COLLECTOR = "a stick-figure man with round glasses, a woolly bobble hat and a small bag over his shoulder"
WATCH = ("an old wristwatch with a round face, a thick outer ring with small tick marks round the edge, two plain "
         "hands, no numbers and no letters, on a plain worn leather strap")
BOOTSALE = ("a car boot sale in a grassy field in England: a row of parked cars with their back doors (boots) lifted "
            "open, folding tables beside each car covered with old things (lamps, books, toys, cups, a small box of "
            "old watches), a few trees and a cloudy sky behind")
AUCTION = ("an auction room: a wooden podium at the front with an auctioneer stick figure in a suit holding a gavel, a "
           "small display stand beside the podium, rows of chairs with stick-figure bidders holding up round paddles")
HUSBAND = "a stick-figure man with a short beard and a trucker cap worn backwards"
WIFE = "a stick-figure woman with curly shoulder-length hair and big round hoop earrings"
COUPLE = f"two people side by side: {HUSBAND}, and {WIFE}"
HOME = ("their small home: a sofa, a small TV on a low cabinet, a clothes rack on wheels full of old shirts and "
        "jackets, a lamp, a rug")
BINS = ("a Goodwill bin store: a big plain warehouse room with long low open bins on wheels, each piled high with "
        "jumbled clothes, plain walls, a till counter at the side")
SWEATER = ("an old knitted sweater with ribbed cuffs and a ribbed round collar, a little faded, with one big plain "
           "shield shape across the chest where its lettering is (no readable letters)")
TAG = ("a small cloth label sewn inside the sweater's collar, with one short line of handwritten ink scribble on it "
       "(no readable letters)")
COACH = ("a stick-figure football coach in an old knitted sweater with the same big plain shield shape on its chest, "
         "a whistle round his neck, standing on a football field with goal posts behind")
CAPTIONS = ("The place fills the whole frame; keep the very top and very bottom of the frame calm (sky, wall or floor) "
            "for captions. Never write any name, label or caption under or beside anyone or anything.")


def shot(n, text, what, place, must, never=""):
    return n, text, " ".join(x for x in (
        f"This is picture {n} of {TOTAL} in one continuous picture story; draw exactly this moment.",
        what, f"Place: {place}.", f"It MUST show: {must}.", f"NEVER: {never}." if never else "", CAPTIONS) if x)


S = [
 shot(1, "A man paid fourteen thousand dollars",
      f"{DEALER} stands at a flea-market table and hands a thick stack of banknotes with a \"$\" on top across the "
      f"table to {SELLER}. On the table between them sits {EGG}, small but clearly visible.",
      MARKET,
      "the dealer paying a big stack of cash, and the small golden egg on the table between them",
      "any thought bubble, any fire, any shop sign with letters"),
 shot(2, "for a golden egg.",
      f"Close view of the flea-market table: {EGG}, drawn big in the middle of the frame, with three small sparkle "
      f"marks around it. The gloved hand of {DEALER} reaches in from the side to pick it up.",
      f"{MARKET}; only the table top, the tent roof edge and a bit of farmland show around the egg",
      "the golden egg on its little stand, clearly the most important thing in the picture",
      "any colour, any clock showing yet, any money"),
 shot(3, "He planned to melt it down.",
      f"{DEALER} stands in his yard holding {EGG} in his gloved hand, looking at it with a calculating grin. A "
      "thought bubble above his head shows the same egg dropping into a big melting pot with flames under it.",
      YARD,
      "the dealer, the egg in his hand, and the thought bubble of the egg going into the melting pot",
      "the real melting pot burning, any colour"),
 shot(4, "Lucky for him, he didn't.",
      f"{EGG} sits safe and whole on the workbench by the shed. Next to it the big melting pot stands cold and empty "
      f"on the furnace (no fire, a few cobweb lines on it). {DEALER} stands beside the bench, scratching his head.",
      YARD,
      "the egg whole and safe, and the melting pot cold with no fire",
      "any fire or flames, a melted or broken egg, any money, any clock showing"),
 shot(5, "But first, two other cheap finds",
      f"Two groups stand side by side on a plain pavement, each holding their find out toward the viewer, with a big "
      f"question mark above each find. Left: {COLLECTOR}, holding up {WATCH}, with a small paper price tag on a "
      f"string showing \"£25\". Right: {COUPLE}, holding up {SWEATER} between them, with a small paper price tag "
      "showing \"58¢\".",
      "a plain town pavement with a low brick wall behind the people and a lamp post at one side",
      "the man with the old watch and its £25 tag, the couple with the old sweater and its 58¢ tag, question marks",
      "any money piles yet, the golden egg"),
 shot(6, "that turned out to be worth a fortune.",
      f"The same people in the same places, now rich: banknotes rain down from above, each stands on a pile of "
      f"money, grinning and cheering. Left: {COLLECTOR}, holding {WATCH} in one hand and a fan of cash in the other. "
      f"Right: {COUPLE}, holding {SWEATER} up between them, each with a fan of cash. \"$\" and \"£\" symbols on the "
      "money.",
      "a plain town pavement with a low brick wall behind the people and a lamp post at one side",
      "the same three people clearly getting rich, each still holding their find",
      "the golden egg, any colour"),
 shot(7, "A man in England",
      f"{COLLECTOR} walks across a grassy field toward the viewer, shown from head to feet, smiling, hands in his "
      "pockets. Behind him in the distance, the row of parked cars with their boots open.",
      BOOTSALE,
      "the man with round glasses, the woolly bobble hat and the shoulder bag, in a grassy English field",
      "any tie or suit, any shop with letters"),
 shot(8, "was looking around a car boot sale.",
      f"Wide view: {COLLECTOR} strolls slowly along the row of cars, bending to look at the tables of old things "
      "beside each open car boot. Two or three other stick figures browse too.",
      BOOTSALE,
      "the row of cars with their back doors lifted open, the tables of old things beside them, and the man browsing",
      "a shop building, any letters or signs"),
 shot(9, "That's a market where people sell old stuff",
      "Close view of one folding table beside a car: an old lamp, a pile of old books, a toy car, chipped cups, a "
      "small box of old wristwatches, each with a small price tag. Nobody's face is in the picture, only the table.",
      f"{BOOTSALE}; the open car boot behind the table and the grass under it",
      "a table of ordinary old things for sale, with small price tags",
      "any letters, any person's face"),
 shot(10, "from the back of their cars.",
      "A seller stick figure in a rain jacket lifts a cardboard box of old things out of the open boot of a small "
      "car and sets it on the folding table beside the car. More old things sit inside the boot.",
      BOOTSALE,
      "the open car boot with old things inside, and the seller unloading them onto the table",
      "a shop, any letters"),
 shot(11, "He spotted an old watch for twenty-five pounds.",
      f"{COLLECTOR} stands at the table holding up {WATCH} between two fingers, his eyes wide behind his round "
      "glasses. A small paper price tag on a string hangs from the strap, showing \"£25\".",
      BOOTSALE,
      "the man with the old watch held up and its £25 tag",
      "a different watch, any letters on the watch"),
 shot(12, "It turned out to be the watch James Bond wore",
      f"{WATCH}, drawn big in the middle of the frame and floating, with small sparkle marks. Beside it on one side "
      "an old movie camera on a tripod, on the other side a round film reel with a strip of film curling out.",
      "a film studio: a plain studio wall with a big studio spotlight on a stand and a director's chair",
      "the same old watch, the movie camera and the film reel: it was a watch from a film",
      "any real actor's face, any person, a tuxedo, a gun, any letters"),
 shot(13, "in the film Thunderball.",
      f"An old cinema seen from the seats: the big screen shows a stick-figure diver swimming underwater in a "
      f"mask and flippers, bubbles rising, fish around him; on his wrist is {WATCH}, drawn a little big so it "
      "shows. Rows of seat backs in the dark at the bottom of the frame.",
      "an old cinema: heavy drawn-back curtains at the sides of the big screen, rows of seats in front",
      "the movie screen with the underwater diver wearing the same old watch",
      "any real actor's face or likeness, a tuxedo, a gun, any letters or title"),
 shot(14, "In twenty thirteen,",
      f"{AUCTION}. On the small display stand sits {WATCH}. The auctioneer raises his gavel. A small sign on the "
      "front of the podium shows \"2013\".",
      "the auction room, filling the frame",
      "the auction room, the same watch on its stand, the raised gavel, 2013 on the podium sign",
      "any letters other than 2013"),
 shot(15, "it sold for over a hundred thousand pounds.",
      f"{AUCTION}. The gavel slams down with impact lines. Beside {WATCH} on its stand stands a tall stack of "
      f"banknotes with a \"£\" symbol on top. In the front row, {COLLECTOR} jumps up with both arms in the air.",
      "the same auction room, filling the frame",
      "the gavel coming down, the watch, the tall stack of cash with £, and the same collector cheering",
      "any letters"),
 shot(16, "Then there's a couple who sell old clothes online.",
      f"{COUPLE} at home: the man takes a photo with a phone of an old jacket the woman holds up in front of the "
      "clothes rack. An open laptop on the cabinet shows a simple online shop page with small photos of clothes "
      "and \"$\" price tags.",
      HOME,
      "the couple photographing old clothes to sell, the clothes rack and the laptop shop page",
      "any website logo or letters"),
 shot(17, "At a Goodwill bin store,",
      f"{COUPLE} lean over one of the long low bins and dig through the jumbled clothes with both hands. Other "
      "shoppers dig in the bins behind them.",
      BINS,
      "the long low bins piled with jumbled clothes and the same couple digging through them",
      "any shop sign or logo or letters"),
 shot(18, "they paid fifty-eight cents",
      f"At the till counter, {HUSBAND} drops a few small coins into a cashier stick figure's open hand. A small "
      f"price screen on the till shows \"58¢\". {WIFE} stands beside him holding a folded sweater.",
      BINS,
      "the few small coins changing hands and 58¢ on the till",
      "banknotes, any letters"),
 shot(19, "for an old sweater with West Point on the front.",
      f"{WIFE} holds up {SWEATER} at arm's length with both hands, showing its front to the viewer, smiling. "
      f"{HUSBAND} gives a thumbs-up beside her.",
      BINS,
      "the old knitted sweater with the big shield shape on its chest, held up by the same woman",
      "any readable letters or words on the sweater, any logo"),
 shot(20, "Later, while watching a show",
      f"{COUPLE} sit on their sofa in the evening, relaxed, watching the TV. {SWEATER} lies folded over the arm "
      "of the sofa.",
      f"{HOME}; a dark window behind the sofa",
      "the same couple on the sofa watching TV, the sweater folded on the sofa arm",
      "any letters on the TV"),
 shot(21, "about football coach Vince Lombardi,",
      f"Close view of the TV screen, filling most of the frame: an old black-and-white photo of {COACH}. The edge "
      "of the TV cabinet shows at the bottom.",
      HOME,
      "the TV showing the football coach standing on a football field with goal posts",
      "any real person's face or likeness, any letters or name"),
 shot(22, "they saw him wearing that same kind of sweater.",
      f"Over-the-shoulder view: {COUPLE} sit forward on the sofa, both pointing at the TV with shocked faces. The TV "
      f"shows {COACH}. {WIFE} holds up {SWEATER} beside the screen: the two shield shapes match.",
      HOME,
      "the sweater on the TV coach and the sweater in the woman's hands, both with the same shield shape",
      "any real person's face or likeness, any letters"),
 shot(23, "They checked the tag.",
      f"{WIFE} turns the collar of {SWEATER} inside out with her fingers; {HUSBAND} leans in close, squinting.",
      HOME,
      "the woman folding the collar inside out to look for the tag, the man leaning in",
      "any readable letters"),
 shot(24, "It said Lombardi.",
      f"Close view: {TAG}, drawn big in the middle of the frame. At the edges of the frame, the faces of {HUSBAND} "
      f"and {WIFE} gasp, mouths round O's.",
      f"{HOME}; only the sofa cushion behind the sweater collar shows",
      "the small cloth tag with the handwritten ink line, and the couple gasping",
      "readable letters or a name written out"),
 shot(25, "It sold for forty-three thousand dollars.",
      f"{COUPLE} jump up from the sofa cheering, arms in the air. On the cabinet an open laptop shows an auction "
      f"page with a photo of {SWEATER}, a small gavel icon and \"$43,000\" big. A stack of banknotes with \"$\" "
      "stands beside the laptop.",
      HOME,
      "the same couple cheering, $43,000 on the laptop with the sweater, and the cash",
      "any letters or logos"),
 shot(26, "Now, the egg.",
      f"{EGG}, alone on a plain wooden workbench in the middle of the frame, with a spotlight cone shining down on it.",
      f"{YARD}; the shed's workbench in front, scrap piles dim behind",
      "the same golden egg on its stand under a spotlight",
      "any person, any money, any fire, any clock showing"),
 shot(27, "A scrap metal dealer bought it",
      f"{DEALER} stands among the scrap piles holding {EGG} carefully in both gloved hands, looking pleased.",
      YARD,
      "the dealer with moustache, flat cap, apron and gloves, holding the golden egg among scrap metal",
      "any fire, any money"),
 shot(28, "at a market in the American Midwest.",
      f"Wide view of the flea market. {DEALER} walks between the tables carrying {EGG} under his arm; a few other "
      "stick figures browse.",
      MARKET,
      "the flea market with flat farmland and the water tower behind, and the dealer with the egg",
      "any letters or signs"),
 shot(29, "He wanted to melt it for the gold.",
      f"{DEALER} holds {EGG} above the big melting pot on the furnace (no fire lit yet) with one hand, and long "
      "metal tongs in the other, sizing it up.",
      YARD,
      "the dealer holding the egg over the melting pot with tongs in his other hand",
      "flames, a melted egg"),
 shot(30, "But nobody would pay what he asked.",
      f"{DEALER} holds out {EGG} on his gloved palm toward two buyer stick figures, who shake their heads (motion "
      "lines) and walk away waving a hand. He looks let down.",
      YARD,
      "the dealer offering the egg and the two buyers shaking their heads and leaving",
      "any money changing hands"),
 shot(31, "So one night he searched online",
      f"{DEALER}, without his gloves, sits at the kitchen table typing on the laptop, his face lit by the screen. "
      f"{EGG} stands on the table beside the laptop.",
      NIGHT_KITCHEN,
      "the dealer at night typing on the laptop with the egg beside him",
      "any letters on the screen"),
 shot(32, "for the name on the little clock inside.",
      f"Close view: {EGG_OPEN}, on the kitchen table. The face of {DEALER} leans in from the side, squinting at the "
      "tiny clock; a magnifying glass in his hand.",
      f"{NIGHT_KITCHEN}; only the table, the lamp light and the dark window show",
      "the egg opened on its hinge with the tiny clock inside, and the dealer squinting at it",
      "readable letters or numbers on the clock"),
 shot(33, "The egg was made by Fabergé",
      f"An old jeweller's workshop long ago: a jeweller stick figure with a small round magnifier clipped over one "
      f"eye sits at a wooden workbench making {EGG} with tiny tools; little gems and tools lie on the bench.",
      "an old jeweller's workshop: a wooden workbench under a tall window, an oil lamp, shelves with small boxes",
      "the jeweller carefully making the same golden egg",
      "any real person's face, any letters"),
 shot(34, "for the Russian royal family,",
      f"A grand palace hall: a stick-figure king in a simple crown and a long cloak with a fur edge receives {EGG} "
      "on a small cushion from a bowing servant. A stick-figure queen in a crown stands beside him.",
      "a grand palace hall: tall arched windows, a big chandelier, a polished floor, onion-dome towers seen through "
      "the windows",
      "the crowned king and queen receiving the same golden egg on a cushion",
      "any real person's face or likeness, any letters"),
 shot(35, "back in the eighteen eighties.",
      f"The same grand palace hall, wider: {EGG} stands on a small table by the tall window, and a framed plaque on "
      "the wall shows \"1887\". The crowned king and queen admire it.",
      "a grand palace hall: tall arched windows, a big chandelier, a polished floor, onion-dome towers seen through "
      "the windows",
      "the egg in the palace, and 1887 on the wall plaque",
      "any other letters or numbers"),
 shot(36, "It had been lost for decades.",
      f"{EGG} sits alone on a dusty shelf in a dim storeroom, with cobwebs over it and dust lines. Beside the shelf "
      "hangs a wall calendar with many of its pages flying off through the air.",
      "a dim dusty storeroom: wooden shelves with old boxes and junk, one small high window",
      "the egg forgotten under dust and cobwebs, and the calendar pages flying",
      "any person"),
 shot(37, "Experts said it was worth",
      f"An expert stick figure in a suit and round glasses studies {EGG} through a big magnifying glass at a table. "
      f"{DEALER} stands beside him, nervous, hands clasped.",
      "an expert's office: shelves of old books, a glass display case, a desk lamp, a window with city buildings",
      "the expert examining the golden egg with a magnifying glass, and the nervous dealer",
      "any real person's face, any letters"),
 shot(38, "about thirty-three million dollars.",
      f"{DEALER}'s jaw drops and his cap flies off his head. Beside {EGG} on the table stands a tower of banknotes "
      "with \"$\" symbols that reaches all the way to the top of the frame. The expert smiles.",
      "the same expert's office: shelves of old books, a glass display case, a desk lamp, a window with city buildings",
      "the dealer's shock, the egg, and the huge cash tower",
      "any letters"),
 shot(39, "Would you have melted it?",
      f"{DEALER} faces the viewer with a shrug and a curious grin, holding {EGG} in one gloved hand and long metal "
      "tongs in the other; the cold melting pot stands beside him. A big question mark floats above his head.",
      YARD,
      "the dealer, the egg in one hand, the tongs in the other, and the question mark",
      "any fire, any letters"),
]

lines = short_lines((HERE / "script.md").read_text(encoding="utf-8"))
assert len(S) == TOTAL and [(i, t) for i, t, _, _ in lines] == [(n, t) for n, t, _ in S], "scenes.py and script.md differ"
p = HERE / "script.json"
if not p.exists():
    sys.exit(f"ok: {TOTAL} scenes match script.md; script.json is written after approval")
data = json.load(open(p, encoding="utf-8"))
segs = data["segments"]
assert len(segs) == TOTAL
for seg, (n, text, scene) in zip(segs, S):
    assert seg["id"] == n and seg["text"] == text, (n, seg["text"], text)
    seg["scene"] = scene
    seg["prompt"] = short_prompt(scene, STYLE)
json.dump(data, open(p, "w", encoding="utf-8"), indent=1, ensure_ascii=False)
print("written", len(segs), "longest", max(len(s["prompt"]) for s in segs), "shortest", min(len(s["prompt"]) for s in segs))
