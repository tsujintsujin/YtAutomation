"""Image prompts for card-penny-ring, written as one story (channels/SHORTS_RULES.md "How image prompts are written";
worked example: ../nail-sandwich-nugget-declaration/scenes.py). Checks every line against script.md; once the script
is approved (right away: no approval step, this file approves it) writes scene + full prompt for every line into script.json.
usage: python channels/found-rich/videos/card-penny-ring/scenes.py"""
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent                 # videos/<slug>
ROOT = HERE.parents[3]                                 # YtAutomation
sys.path.insert(0, str(ROOT))
from dashboard import approve, short_lines, short_prompt       # the script's lines, and the fixed frame around every prompt

STYLE = json.loads((HERE.parents[1] / "settings.json").read_text(encoding="utf-8"))["image_style"]
TOTAL = 45

# ---- the same words every time a person, object or place appears ----
WOMAN = ("a stick-figure woman with big curly hair, hoop earrings and a long cardigan")
RING = ("a chunky old ring with one big clear square-ish gemstone with rounded corners and many small cut facets, held "
        "in a plain dull metal setting with four claws; black ink lines only, no colour")
LONDON_HOME = ("her small London kitchen: a sink with a window above it, through which a row of brick terraced houses "
               "and a double-decker bus (black ink lines only, no red) can be seen, a kettle, a mug tree, a fridge with magnets")
BOOTSALE = ("a car boot sale in a grassy field in West London: a row of parked cars with their boots open and full of "
            "things for sale (boxes of bric-a-brac, old toys, lamps, clothes), folding tables in front of them, "
            "people browsing, terraced rooftops behind")
JEWELLER = ("a stick-figure jeweller with a bald head, a small grey beard and a magnifying eyepiece in one eye")
JEWEL_SHOP = ("a small jeweller's workshop: a wooden workbench with tiny tools, a bright lamp on a bendy arm, glass cases "
              "with rings and watches")
MAINE_MAN = ("a stick-figure man with a full beard, a floppy fishing hat and a checked shirt")
YARDSALE = ("a yard sale on the lawn of an old white farmhouse in a small Maine town near the woods: folding tables of old "
            "things (photo albums, glass soda bottles in a crate, lamps), two old wooden chairs on the grass, pine trees "
            "behind")
YARD_SELLER = "a stick-figure older woman with a grey bun and a quilted vest"
ALBUM = ("an old thick photo album with a worn cloth cover and stiff dark pages, no writing")
CARD = ("a small old card made of thick stiff cardboard with a small faded photo glued onto it: a team of nine "
        "baseball players and a manager posing in two rows, in old-fashioned long-sleeved shirts, long trousers and "
        "little caps, one holding a bat; no letters or names")
BOY = "a stick-figure teenage boy with neat short combed hair, a knitted sweater vest over a shirt, and trousers"
SCHOOL = ("a school lunchroom in the nineteen forties: a long counter with trays, a lunch lady in an apron and a "
          "hairnet behind it, long wooden tables with benches, tall windows")
PENNY = ("a small round copper penny with a thin raised rim, a simple side-view outline of a man's head on it, and the "
         "date \"1943\" printed small; black ink lines only, no orange, no brown, no colour; no other letters")
STEEL = ("small round grey steel pennies, drawn with a lighter outline and little shine marks, no letters")
MINT = ("a coin factory in the nineteen forties: a big heavy stamping machine on a factory floor, conveyor belts and bins "
        "of coins, workers in overalls and caps")
AUCTION = ("an auction room: a wooden podium at the front with an auctioneer stick figure in a suit holding a gavel, a "
           "small display stand beside the podium, rows of chairs with stick-figure bidders holding up round paddles")
CAPTIONS = ("The place fills the whole frame; keep the very top and very bottom of the frame calm (sky, wall or floor) "
            "for captions. Never write any name, label or caption under or beside anyone or anything.")


def shot(n, text, what, place, must, never=""):
    return n, text, " ".join(x for x in (
        f"This is picture {n} of {TOTAL} in one continuous picture story; draw exactly this moment.",
        what, f"Place: {place}.", f"It MUST show: {must}.", f"NEVER: {never}." if never else "", CAPTIONS) if x)


S = [
 shot(1, "A woman wore a ten-pound ring for years.",
      f"{WOMAN} holds her hand up and admires {RING} on her finger; a small paper price tag dangles from it on a "
      "string showing \"£10\".",
      LONDON_HOME,
      "the woman wearing the big-stoned ring, with a £10 tag",
      "any other numbers or letters, any money"),
 shot(2, "She thought the stone was fake.",
      f"{WOMAN} shrugs with a grin, wearing {RING}; a thought bubble above her shows a cheap plastic toy ring from a "
      "gumball machine.",
      LONDON_HOME,
      "the woman thinking her ring is a cheap fake",
      "any money, any letters"),
 shot(3, "It sold for over six hundred fifty thousand pounds.",
      f"{RING} on a small velvet cushion beside a tower of banknotes with \"£\" symbols reaching the top of the frame; "
      "sparkle marks around the stone.",
      LONDON_HOME,
      "the ring beside a huge tower of pound cash",
      "any person, any letters"),
 shot(4, "But first, two tiny things",
      f"Two people side by side, a big question mark above each. Left: {MAINE_MAN}, holding up {CARD}. Right: {BOY}, "
      f"holding up {PENNY} between finger and thumb.",
      "a plain town pavement with a low brick wall behind the people and a lamp post at one side",
      "the bearded man with the small old card and the boy with the penny",
      "any money, any letters except 1943 on the penny"),
 shot(5, "that were hiding in plain sight.",
      f"On a plain table lie {ALBUM}, open, and a school lunch tray with a few coins and a sandwich on it; a big "
      "magnifying glass hovers over them.",
      "a plain room with a wooden table and a plain wall behind",
      "everyday things with a magnifying glass over them: something hidden in plain sight",
      "any person, any letters"),
 shot(6, "In Maine, a man bought an old photo album",
      f"{MAINE_MAN} lifts {ALBUM} from a yard-sale table, flipping it open with interest.",
      YARDSALE,
      "the bearded man in the fishing hat picking up the old photo album",
      "any letters"),
 shot(7, "at a yard sale.",
      f"Wide view of the yard sale: the tables on the lawn, {YARD_SELLER} in a lawn chair, and {MAINE_MAN} with "
      f"{ALBUM} under his arm.",
      YARDSALE,
      "the yard sale at the old farmhouse and the man with the album",
      "any signs or letters"),
 shot(8, "He also got some old soda bottles",
      f"{MAINE_MAN} holds a wooden crate of old glass soda bottles, {ALBUM} tucked under his arm.",
      YARDSALE,
      "the man holding a crate of old glass bottles",
      "any brand names, logos or letters"),
 shot(9, "and a couple of chairs.",
      f"{MAINE_MAN} wobbles across the lawn carrying two old wooden chairs on top of the crate of bottles, the album "
      "under his arm, motion lines.",
      YARDSALE,
      "the man carrying two wooden chairs as well, wobbling",
      "any letters"),
 shot(10, "All of it cost less than a hundred dollars.",
      f"{MAINE_MAN} hands a few banknotes to {YARD_SELLER}; the chairs, the crate of bottles and {ALBUM} are piled "
      "beside him.",
      YARDSALE,
      "the man paying a small amount for the whole pile",
      "any big money, any letters"),
 shot(11, "Inside the album was a small photo of a baseball team",
      f"Close view: {ALBUM} open on a kitchen table, and on one stiff page sits {CARD}; the man's finger points at it.",
      "a farmhouse kitchen: a wooden table, a window with pine trees outside",
      "the old team photo inside the album",
      "any letters or names"),
 shot(12, "from eighteen sixty-five,",
      "Long ago: a team of nine stick-figure baseball players and a manager in a bowler hat pose in two rows on a "
      "grass field, in old-fashioned long-sleeved shirts, long trousers and little caps, one holding a bat; a "
      "photographer stands under the black cloth of a big old box camera on a wooden tripod.",
      "a grassy ball field long ago with a wooden fence and a few old brick buildings behind",
      "the team from long ago posing for an old-time camera",
      "any modern thing, any letters"),
 shot(13, "glued onto a card.",
      f"Close view: {CARD}, drawn big, held between two fingers; the thick card edge shows the photo glued on top.",
      "a farmhouse kitchen: only the wooden table top shows behind",
      "the old photo glued onto thick card",
      "any letters or names"),
 shot(14, "It was one of the oldest baseball cards ever found.",
      f"{CARD}, alone in the middle of the frame, under a spotlight cone with sparkle marks around it.",
      "a dark plain room, only the spotlight",
      "the old baseball card shining under a spotlight",
      "any person, any letters"),
 shot(15, "A card just like it",
      f"Two copies of {CARD} side by side on a plain cloth, each under its own small spotlight; nothing else.",
      "a plain dark gallery wall behind a long low table with a soft cloth",
      "two nearly matching old cards side by side",
      "a third card, any person, any letters"),
 shot(16, "sits in the Library of Congress.",
      f"One copy of {CARD} sits in a glass case in a grand library hall; a visitor stick figure looks at it.",
      "a grand library reading room: a huge round dome with painted panels, tall arched windows, curved rows of "
      "wooden reading desks with lamps, shelves of books all around",
      "the other card in a glass case in the grand domed library",
      "any letters or signs"),
 shot(17, "In twenty thirteen,",
      f"{AUCTION}. On the display stand sits {CARD} in a small frame. A small sign on the front of the podium shows "
      "\"2013\".",
      "the auction room, filling the frame",
      "the auction room, the card on its stand, 2013 on the podium sign",
      "any letters other than 2013"),
 shot(18, "the card sold for ninety-two thousand dollars.",
      f"{AUCTION}. The gavel slams down with impact lines. Beside {CARD} stands a tall stack of banknotes with a "
      f"\"$\" on top.",
      "the same auction room, filling the frame",
      "the gavel coming down, the card and the tall stack of cash",
      "any letters"),
 shot(19, "Then, in nineteen forty-seven,",
      "An old brick school building in a small town in the nineteen forties, with a flag pole with a plain flag, "
      "rounded old cars parked outside, and a calendar hanging in the front window showing \"1947\".",
      "a small Massachusetts town street in the nineteen forties with bare autumn trees",
      "an old school from the 1940s and 1947 on the calendar",
      "any letters other than 1947"),
 shot(20, "a sixteen-year-old boy in Massachusetts",
      f"{BOY} walks up the school steps with a satchel over his shoulder, whistling.",
      "a small Massachusetts town street in the nineteen forties with bare autumn trees and the old brick school",
      "the teenage boy in a sweater vest going into school",
      "any letters"),
 shot(21, "bought lunch at school.",
      f"{BOY} stands at the lunch counter holding a tray with a sandwich and a carton of milk, handing a coin to the "
      "lunch lady.",
      SCHOOL,
      "the boy buying lunch at the school lunch counter",
      "any letters"),
 shot(22, "In his change was a copper penny",
      f"The lunch lady drops a few coins of change into {BOY}'s open palm; one of them is {PENNY}, with a tiny "
      "sparkle.",
      SCHOOL,
      "change dropping into the boy's hand, one penny sparkling",
      "any other letters or numbers"),
 shot(23, "from nineteen forty-three.",
      f"Close view: {PENNY}, drawn big in the middle of the frame between the boy's finger and thumb.",
      f"{SCHOOL}; only a blurred tray and table show behind",
      "the penny up close with 1943 on it",
      "any other letters or numbers, any colour"),
 shot(24, "That year, pennies were made of steel,",
      f"In the coin factory, the big stamping machine thumps out a stream of {STEEL} into a bin.",
      MINT,
      "a machine making lots of grey steel pennies",
      "any copper pennies, any letters"),
 shot(25, "to save copper for the war.",
      "Workers load copper pots, pans and coils of copper wire onto a nineteen-forties army truck heading off to a "
      "wartime factory with smoking chimneys.",
      "a factory yard in the nineteen forties with tall smoking chimneys",
      "copper things being collected for the war",
      "any weapons, any letters or flags"),
 shot(26, "Only a few copper ones were made, by mistake.",
      f"At the stamping machine, among a stream of {STEEL}, one {PENNY.replace('a small round', 'small round')} slides "
      "out different from the others; a worker in overalls slaps his forehead, \"oops\" lines around him.",
      MINT,
      "one odd copper penny coming out among the grey steel ones by mistake",
      "any letters except 1943 on the penny"),
 shot(27, "He wrote to the government,",
      f"{BOY} sits at a desk in his bedroom writing a letter with a fountain pen, {PENNY} on the desk beside the "
      "envelope.",
      "a 1940s boy's bedroom: a desk with a lamp, a bed, a baseball pennant shape on the wall with no letters",
      "the boy writing a letter about his penny",
      "any readable letters on the paper"),
 shot(28, "and they told him copper ones didn't exist.",
      f"{BOY} reads a typed reply letter with a frown; a thought bubble above him shows {PENNY} with a big X across it.",
      "a 1940s boy's bedroom: a desk with a lamp, a bed, a baseball pennant shape on the wall with no letters",
      "the boy being told his copper penny can't be real",
      "any readable words"),
 shot(29, "He kept it anyway, his whole life.",
      f"Three versions of the same man in a row, left to right: the teenage boy, a grown man in a suit, and a white-"
      f"haired old man with a cane; each holds {PENNY} in an open palm.",
      "a plain room with a soft wall behind",
      "the same person keeping the penny from boyhood to old age",
      "any letters except 1943 on the pennies"),
 shot(30, "After he died,",
      "A quiet empty armchair by a window with a pair of round glasses resting on its seat and a small lit candle on "
      "a side table; soft light.",
      "a quiet old living room: the armchair, a side table, a window with a tree outside",
      "a gentle, quiet picture of someone gone",
      "any person, any money, any letters"),
 shot(31, "it sold for two hundred four thousand dollars.",
      f"{AUCTION}. The gavel slams down with impact lines. On the display stand sits {PENNY} in a small clear case, "
      "beside a tall stack of banknotes with a \"$\" on top.",
      "the auction room, filling the frame",
      "the gavel, the tiny penny and the tall stack of cash",
      "any letters except 1943 on the penny"),
 shot(32, "He left the money to his town's library.",
      "An old stone town library with columns and wide steps; a bundle of banknotes floats in through the open front "
      "door; inside, people read at tables; a child carries books out, smiling.",
      "a town street with trees in front of the old library",
      "the money going to the town library",
      "any letters or signs on the building"),
 shot(33, "Now, the ring.",
      f"{RING}, alone in the middle of the frame, under a spotlight cone, sparkle marks around the stone.",
      "a dark plain room, only the spotlight",
      "the ring under a spotlight",
      "any person, any money, any colour, any letters"),
 shot(34, "In the late nineteen eighties, a woman in London",
      f"{WOMAN} walks down a London street with a shopping bag; a double-decker bus and a phone box behind her (black ink lines only, no red)."
      "her.",
      "a London street in the late nineteen eighties: brick terraced houses, a corner shop, a double-decker bus, "
      "a phone box, chunky eighties cars",
      "the woman with big curly hair on a London street in the eighties",
      "any letters or signs"),
 shot(35, "paid ten pounds for a box of old jewellery",
      f"{WOMAN} hands a banknote to a seller stick figure with a flat cap at a car boot; she holds a shoebox full of "
      "tangled bangles, beads and rings.",
      BOOTSALE,
      "the woman buying a box of cheap old jewellery",
      "any letters"),
 shot(36, "at a car boot sale.",
      f"Wide view of the car boot sale: the row of cars with open boots, tables of bric-a-brac, crowds browsing; "
      f"{WOMAN} small in the middle with the shoebox.",
      BOOTSALE,
      "a busy car boot sale: cars with open boots full of things for sale",
      "any signs or letters"),
 shot(37, "One ring had a big, clear stone.",
      f"{WOMAN} picks {RING} out of the tangled shoebox of jewellery and holds it up to the light.",
      LONDON_HOME,
      "the woman holding up the big-stoned ring from the box",
      "any money, any letters"),
 shot(38, "She thought it was fake,",
      f"{WOMAN} slips {RING} onto her finger with a shrug; a thought bubble shows a cheap plastic toy ring.",
      LONDON_HOME,
      "the woman thinking the ring is fake",
      "any money, any letters"),
 shot(39, "so she just wore it all the time.",
      f"Three small scenes in a row, all with {WOMAN} wearing {RING}: washing dishes at the sink, pushing a "
      "supermarket trolley, digging in a garden.",
      "three panels side by side: her kitchen, a supermarket aisle, a small back garden",
      "the woman wearing the ring in everyday life",
      "any letters"),
 shot(40, "About thirty years later,",
      f"{WOMAN}, now older with grey curly hair and reading glasses, still wearing {RING}; behind her a wall calendar "
      "with many pages flying off.",
      LONDON_HOME,
      "the same woman many years older, still wearing the ring, time flying",
      "any letters or numbers"),
 shot(41, "a jeweller took a closer look.",
      f"{JEWELLER} leans over {RING} under the bright lamp, studying it through his eyepiece; the older woman watches "
      "across the workbench.",
      JEWEL_SHOP,
      "the jeweller studying the ring closely",
      "any letters"),
 shot(42, "It was a real diamond, over twenty-six carats.",
      f"{RING}, drawn huge in the middle of the frame, blazing with sparkle marks; at the edge the older woman's jaw "
      "drops and her glasses slide off.",
      JEWEL_SHOP,
      "the big real diamond blazing with sparkle, the woman shocked",
      "any colour, any letters"),
 shot(43, "In twenty seventeen,",
      f"{AUCTION.replace('an auction room', 'a grand auction room with chandeliers')}. On the display stand sits "
      f"{RING} on a velvet cushion. A small sign on the front of the podium shows \"2017\".",
      "the grand auction room, filling the frame",
      "the auction room, the ring on its cushion, 2017 on the podium sign",
      "any letters other than 2017"),
 shot(44, "the ring sold for over six hundred fifty thousand pounds.",
      f"{AUCTION.replace('an auction room', 'a grand auction room with chandeliers')}. The gavel slams down with impact "
      f"lines. Beside {RING} rises a tower of banknotes with \"£\" symbols reaching the top of the frame.",
      "the same grand auction room, filling the frame",
      "the gavel coming down, the ring and the giant pound cash tower",
      "any letters"),
 shot(45, "What are you wearing right now?",
      "A friendly stick figure faces the viewer, holding up one hand and looking at the rings on their own fingers "
      "with a curious grin; a big question mark floats above.",
      "a cosy living room: a sofa, a lamp, a window",
      "the stick figure looking at their own rings, and the question mark",
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
