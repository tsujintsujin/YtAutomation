"""Image prompts for jeans-cards-ferrari, written as one story (channels/SHORTS_RULES.md "How image prompts are written";
worked example: ../nail-sandwich-nugget-declaration/scenes.py). Checks every line against script.md; once the script
is approved (right away: no approval step, this file approves it) writes scene + full prompt for every line into script.json.
usage: python channels/found-rich/videos/jeans-cards-ferrari/scenes.py"""
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent                 # videos/<slug>
ROOT = HERE.parents[3]                                 # YtAutomation
sys.path.insert(0, str(ROOT))
from dashboard import approve, short_lines, short_prompt       # the script's lines, and the fixed frame around every prompt

STYLE = json.loads((HERE.parents[1] / "settings.json").read_text(encoding="utf-8"))["image_style"]
TOTAL = 42

# ---- the same words every time a person, object or place appears ----
HUNTER = ("a stick-figure man with a big bushy beard, a miner's helmet with a headlamp on the front, a coil of rope over "
          "one shoulder and work gloves")
JEANS = ("an old pair of work jeans laid out full length: five pockets, small metal rivets at the pocket corners, a row "
         "of buttons at the front instead of a zip, a few small holes, frayed hems and one sewn-on patch on a knee; "
         "black ink lines only, no blue, no colour")
MINE = ("inside an abandoned mine tunnel: rough rocky walls, old wooden support beams across the ceiling, a rusty "
        "narrow rail track on a dirt floor, an old broken lantern lying on its side, darkness further in")
MINE_OUT = ("the entrance of an abandoned mine in the dry hills of the American West: a dark opening in a rocky hillside "
            "framed by old wooden beams, a few loose boards across it, an old wooden ladder going down a shaft beside "
            "it, tall cactus, dry bushes and flat-topped hills behind under a big sky")
TENT_AUCTION = ("an auction under a big festival tent in the New Mexico desert: rows of folding chairs with stick-figure "
                "bidders holding up round paddles, an auctioneer stick figure in a cowboy hat at a small wooden podium "
                "holding a gavel, a display stand beside the podium, and flat-topped desert hills seen past the open "
                "tent sides")
MUSEUM = ("a quiet museum gallery: tall glass display cases on stands, a polished floor, plain walls with a tall window")
COUSINS = ("two stick-figure cousins: a man with short hair, glasses and a checked flannel shirt, and a woman with long "
           "hair in a ponytail and a cardigan")
HOUSE_OUT = ("an old two-storey wooden house in a small Ohio town in late winter: a front porch with steps, tall narrow "
             "windows, a big bare tree in the yard, patches of old snow on the grass")
HOUSE_IN = ("inside the old house: old furniture covered with white dust sheets, a wooden staircase, faded flowered "
            "wallpaper, a framed old photo on the wall of a man with a big moustache and a straw hat, cardboard moving "
            "boxes on the floor")
ATTIC = ("a dusty attic under a sloping wooden roof: bare wooden rafters, a small round window letting in a beam of "
         "light, old trunks, a broken chair, cobwebs in the corners, a plank floor")
BOX = "a small plain cardboard box with a fold-down lid, a little dented and dusty, with no writing on it"
CARDS = ("small old baseball cards, each a narrow rectangle with a thin plain border and inside it a tiny simple drawing "
         "of a stick-figure baseball player in an old-fashioned cap (batting, pitching or catching); no names, no "
         "letters, no numbers on the cards")
GRANDPA = ("a stick-figure butcher from long ago with a big moustache, a flat straw hat and a long white apron")
MEAT_SHOP = ("a small butcher's shop in nineteen ten: a wooden counter with a big hanging scale, strings of sausages and "
             "hams hanging from hooks on the back wall, a glass jar of wrapped candies on the counter, sawdust on the "
             "floor, a big front window onto a street")
STREET_1910 = ("a small-town street around nineteen ten: a horse pulling a cart, an old-fashioned open car with big thin "
               "wheels, wooden shop fronts with awnings, gas street lamps, people in long coats and hats")
CARD_AUCTION = ("an auction in a big convention-centre hall: plain walls and rows of ceiling lights, a wooden podium at "
                "the front with an auctioneer stick figure in a suit holding a gavel, a display stand beside it, rows of "
                "chairs with stick-figure bidders holding up round paddles")
BAILLON = ("a stick-figure man in a nineteen-sixties suit and thin tie, with slicked-back hair, standing proud")
OLD_CARS = ("a long row of different old cars from the nineteen thirties to the nineteen sixties: rounded fenders, big "
            "round headlights, running boards, spoked wheels")
FERRARI = ("a long, low, open-top sports car from the early nineteen sixties: a long smooth rounded bonnet, two round "
           "headlights under clear covers set into the front curves, a small oval grille, a low windscreen, two seats, "
           "spoked wheels; black ink lines only, no red, no colour, no badge or letters")
BARN_OUT = ("old farm buildings in the French countryside: barns and sheds with rough stone walls, sagging tiled roofs and "
            "big wooden double doors, tall grass and weeds around them, rolling fields and a row of poplar trees behind")
BARN_IN = ("inside a dim old barn: rough stone walls, a high roof with wooden beams, thick cobwebs hanging, a dirt floor, "
           "beams of light through gaps in the doors, dust in the air")
MAGS = ("tall stacks of old magazines tied with string, piled high on top of and all around a car")
FAMILY_FR = ("three stick-figure family members: an older man with a grey beard, a woman with short curly hair, and a "
             "young man in a hoodie")
PARIS_AUCTION = ("a grand auction hall in Paris: crystal chandeliers, a low stage at the front, an auctioneer stick figure "
                 "in a suit at a podium holding a gavel, rows of chairs with stick-figure bidders holding up round "
                 "paddles, tall arched windows with the Eiffel Tower seen through one of them")
CAPTIONS = ("The place fills the whole frame; keep the very top and very bottom of the frame calm (sky, wall or floor) "
            "for captions. Never write any name, label or caption under or beside anyone or anything.")


def shot(n, text, what, place, must, never=""):
    return n, text, " ".join(x for x in (
        f"This is picture {n} of {TOTAL} in one continuous picture story; draw exactly this moment.",
        what, f"Place: {place}.", f"It MUST show: {must}.", f"NEVER: {never}." if never else "", CAPTIONS) if x)


S = [
 shot(1, "A car sat under piles of old magazines",
      f"In the barn, {MAGS}: the car is almost completely hidden; only the curve of its front and one round headlight "
      "peek out from under the stacks.",
      BARN_IN,
      "towering stacks of old magazines covering a car, with just a bit of the car's front showing",
      "the whole car visible, any person, any money, any letters on the magazines"),
 shot(2, "for fifty years.",
      f"The same pile in the barn: {MAGS}, with only one round headlight peeking out; thick cobwebs stretch from the "
      "stacks to the beams. On the stone wall hangs an old calendar with many pages flying off through the air.",
      BARN_IN,
      "the magazine pile and cobwebs, and the calendar pages flying: a very long time passing",
      "any person, any money, any letters or numbers on the calendar"),
 shot(3, "Then it sold for over sixteen million euros.",
      f"{FERRARI} stands clean in the middle of the frame, the magazines gone. Beside it rises a tower of banknotes "
      "marked with \"€\" symbols, reaching the top of the frame; sparkle marks around the car.",
      BARN_IN,
      "the old sports car next to a huge tower of euro cash",
      "any person, any auction room, any letters"),
 shot(4, "But first, two other things",
      f"Two scenes side by side, a big question mark above each. Left: {HUNTER}, holding up {JEANS}. Right: {COUSINS}, "
      f"holding {BOX} between them, its lid open, with {CARDS} peeking out.",
      "a plain town pavement with a low brick wall behind the people and a lamp post at one side",
      "the bearded man holding the old jeans, and the two cousins holding the box of old baseball cards",
      "any money, the car, any letters"),
 shot(5, "that people left behind and forgot about.",
      f"Three tall panels side by side, each one dim and dusty with cobwebs. Left panel: {JEANS}, lying crumpled in "
      f"the dirt of a dark mine tunnel. Middle panel: {BOX}, sitting alone on the plank floor of a dusty attic. Right "
      f"panel: {MAGS}, in a dim stone barn.",
      "the three panels fill the whole frame: a mine tunnel, an attic and a barn",
      "three forgotten things in three forgotten places, with no people",
      "any person, any money, any letters"),
 shot(6, "A man who hunts for old jeans",
      f"{HUNTER} stands beside a heap of old worn jeans and shirts he has found, holding one pair up to the light, "
      "grinning.",
      MINE_OUT,
      "the bearded man with the headlamp helmet, a jeans hunter with his finds",
      "any letters or logos"),
 shot(7, "climbed down into an abandoned mine",
      f"{HUNTER} climbs down the old wooden ladder into the dark mine shaft, his headlamp shining, the rope over his "
      "shoulder.",
      MINE_OUT,
      "the same man climbing down a ladder into the dark old mine",
      "any letters or signs"),
 shot(8, "in the American West.",
      f"Wide view: the boarded-up mine entrance small in the middle of the frame among dry hills, cactus and dry "
      f"bushes; the top of the ladder sticks out of the shaft; {HUNTER}'s helmet light glows down inside.",
      MINE_OUT,
      "the old mine in the wide dry desert hills of the American West",
      "any town, any letters"),
 shot(9, "In the dirt,",
      f"Inside the tunnel, {HUNTER} kneels on the dirt floor, his headlamp beam shining down on a patch of dirt; he "
      "brushes the dirt with his gloved hand.",
      MINE,
      "the same man in the dark tunnel, headlamp on the dirt floor",
      "the jeans yet, any letters"),
 shot(10, "he found a pair of Levi's from the eighteen eighties.",
      f"{HUNTER} lifts {JEANS} up out of the dirt, dust falling off it, his eyes wide in the light of his headlamp.",
      MINE,
      "the same man pulling the old jeans out of the dirt in the mine",
      "any brand label, any letters"),
 shot(11, "They were worn,",
      f"Close view: {JEANS}, drawn big in the middle of the frame, in the man's gloved hands: the holes, the frayed "
      "hems and the knee patch are clear.",
      f"{MINE}; only the rock wall and a wooden beam show behind",
      "the jeans up close, clearly old and worn with holes and frays",
      "any label, any colour"),
 shot(12, "but they were still in one piece.",
      f"{HUNTER} stands holding {JEANS} up by the waist at full length in front of him, both legs hanging down whole; "
      "he smiles proudly.",
      MINE,
      "the whole pair of jeans in one piece, held up full length",
      "torn-off legs, any letters"),
 shot(13, "Only a couple of pairs like them are known.",
      f"Two tall glass display cases side by side, each holding one copy of {JEANS} hung up flat; a small spotlight "
      "above each; empty space all around.",
      MUSEUM,
      "exactly two old pairs of jeans in museum cases, and nothing else: they are rare",
      "a third pair, any person, any letters"),
 shot(14, "In twenty twenty-two,",
      f"{TENT_AUCTION}. On the display stand hangs {JEANS}. A small sign on the front of the podium shows \"2022\".",
      "the festival tent auction, filling the frame",
      "the desert tent auction, the old jeans on the stand, 2022 on the podium sign",
      "any letters other than 2022"),
 shot(15, "they sold at an auction for over eighty-seven thousand dollars.",
      f"{TENT_AUCTION}. The gavel slams down with impact lines. Beside {JEANS} on its stand stands a tall stack of "
      "banknotes with a \"$\" on top; bidders' paddles fly up.",
      "the same festival tent auction, filling the frame",
      "the gavel coming down, the old jeans and the tall stack of cash",
      "any letters"),
 shot(16, "Not bad for a dirty pair of pants.",
      f"{JEANS}, hanging alone on a simple display stand, a little dust puffing off them, beside a tall stack of "
      "banknotes with \"$\" symbols; sparkle marks around the jeans.",
      "the same festival tent, empty chairs behind, the desert hills past the tent sides",
      "the dusty old jeans next to the big pile of money, a funny contrast",
      "any person, any letters"),
 shot(17, "Then in Ohio, a family was clearing out",
      f"{COUSINS} carry cardboard moving boxes down the porch steps of the old house; more boxes wait on the porch.",
      HOUSE_OUT,
      "the two cousins clearing out the old wooden house in winter",
      "any letters on the boxes"),
 shot(18, "their grandfather's old house.",
      f"Inside, {COUSINS} stand in the hall, looking around at the old furniture under dust sheets; the woman points "
      "at the framed old photo of the grandfather on the wall.",
      HOUSE_IN,
      "the old house inside and the photo of the moustached grandfather",
      "any letters"),
 shot(19, "In the attic, they found an old box.",
      f"In the attic, the woman from {COUSINS} kneels and lifts {BOX} out from behind an old trunk, blowing dust off "
      "it; the man holds a torch.",
      ATTIC,
      "the cousins finding the plain dusty box in the attic",
      "the cards yet, any letters"),
 shot(20, "Inside were about seven hundred baseball cards",
      f"Close view looking down into {BOX}, lid open: it is packed full with {CARDS}, hundreds of them standing in "
      "tight rows. The cousins' faces at the edges of the frame, eyes wide.",
      f"{ATTIC}; only the plank floor and a rafter show behind",
      "the box packed with hundreds of old baseball cards",
      "any names or numbers on the cards, any money"),
 shot(21, "from around nineteen ten.",
      f"Long ago: {STREET_1910}. A small hanging sign over one shop door shows \"1910\".",
      STREET_1910,
      "a street from long ago, around 1910",
      "any modern car, any letters other than 1910"),
 shot(22, "Back then, you got them free with candy.",
      f"Inside {MEAT_SHOP}: a small boy in a flat cap and short trousers stands at the counter, happily holding a "
      f"wrapped candy in one hand and one of {CARDS} in the other.",
      MEAT_SHOP,
      "a boy getting a free baseball card along with his candy",
      "any letters, any money"),
 shot(23, "Their grandfather probably handed them out",
      f"{GRANDPA} leans over the wooden counter and hands one of {CARDS} to the same small boy in a flat cap, smiling.",
      MEAT_SHOP,
      "the grandfather with the moustache and apron handing a card over the counter",
      "any letters"),
 shot(24, "at his meat market.",
      f"Wide view of {MEAT_SHOP}, with {GRANDPA} behind the counter by the big scale, sausages and hams hanging behind "
      "him, a customer at the door.",
      MEAT_SHOP,
      "the grandfather's old butcher shop",
      "any shop name or letters"),
 shot(25, "The cards looked almost new.",
      f"Close view: a fan of five of {CARDS} held in the woman's fingers, crisp and clean with sharp corners, sparkle "
      "marks around them.",
      f"{ATTIC}; only the round window and a rafter show softly behind",
      "the old cards looking crisp and almost new",
      "bent or torn cards, any names or numbers"),
 shot(26, "Just thirty-seven of them",
      f"A short neat row of {CARDS} laid out on a clean table under a lamp, a small handful only, while the open box "
      "full of hundreds more sits at the far side of the table.",
      "an expert's viewing room: a table with a soft cloth, a desk lamp, shelves of framed cards on the wall",
      "only a small group of cards picked out from the big box",
      "any numbers or letters, any money"),
 shot(27, "sold for over five hundred sixty thousand dollars.",
      f"{CARD_AUCTION}. The gavel slams down with impact lines. On the stand is a frame holding a row of {CARDS}. "
      f"Beside it stands a tall stack of banknotes with a \"$\" on top. ",
      "the same auction hall, filling the frame",
      "the gavel coming down, the framed cards and the tall stack of cash",
      "any letters or names"),
 shot(28, "Now, the car.",
      f"{FERRARI}, alone in the middle of the frame with a spotlight cone shining down on it.",
      f"{BARN_IN}; dim behind the spotlight",
      "the same old sports car under a spotlight",
      "any person, any money, any letters"),
 shot(29, "In France, a man named Roger Baillon",
      f"{BAILLON} stands with his hands on his hips in front of {OLD_CARS}, chest out, proud.",
      f"a big tidy garage yard in the French countryside in the nineteen sixties, a stone farmhouse and poplar trees "
      f"behind",
      "the proud man in a 1960s suit in front of his row of old cars",
      "any likeness of a real person, any letters"),
 shot(30, "collected fancy cars.",
      f"{BAILLON} polishes the shiny bonnet of one car with a cloth, smiling; the rest of {OLD_CARS} gleam beside it, "
      "with sparkle marks.",
      f"a big tidy garage yard in the French countryside in the nineteen sixties, a stone farmhouse and poplar trees "
      f"behind",
      "the same man polishing his collection of fancy old cars",
      "any letters"),
 shot(31, "He dreamed of opening a museum.",
      f"{BAILLON} gazes upward, smiling; a big thought bubble above him shows a grand museum building with columns "
      "and, through its big glass front, rows of old cars on display with visitors looking at them.",
      f"a big tidy garage yard in the French countryside in the nineteen sixties, a stone farmhouse and poplar trees "
      f"behind",
      "the man dreaming of a big car museum in a thought bubble",
      "any letters or signs on the museum"),
 shot(32, "Then the money ran out.",
      f"{BAILLON} holds his wallet open upside down, frowning; nothing falls out but a small moth fluttering away. "
      "A small storm cloud hangs over his head.",
      f"a big tidy garage yard in the French countryside, a stone farmhouse and poplar trees behind",
      "the same man with an empty wallet, sad",
      "any money, any letters"),
 shot(33, "His cars were left in old barns and sheds.",
      f"Wide view: {BARN_OUT}; all the big doors are shut, ivy and weeds creep up the walls, nobody around.",
      BARN_OUT,
      "the shut old stone barns and sheds standing forgotten",
      "any person, any car outside, any letters"),
 shot(34, "In twenty fourteen, his family opened the doors.",
      f"{FAMILY_FR} pull open the big wooden double doors of one barn together, leaning back with the effort; dust "
      "puffs out. A small paper calendar nailed beside the door shows \"2014\".",
      BARN_OUT,
      "the family pulling open the barn doors, and 2014 on the calendar",
      "any letters other than 2014"),
 shot(35, "Inside were about sixty old cars, all covered in dust.",
      f"Inside the barn: rows and rows of {OLD_CARS.replace('a long row of ', '')}, all dull with dust and draped in "
      f"cobwebs, some with flat tyres; {FAMILY_FR} stand at the doorway in the light, staring.",
      BARN_IN,
      "rows of many dusty old cars in the dim barn, and the family staring",
      "shiny clean cars, any letters"),
 shot(36, "Under stacks of old magazines",
      f"In a corner of the barn, the young man in a hoodie from {FAMILY_FR} lifts a tied stack of magazines off a "
      f"huge pile: {MAGS}; under the gap, the curve of a car's front and one round headlight show.",
      BARN_IN,
      "the family lifting magazines off a big pile that hides a car",
      "the whole car visible yet, any letters on the magazines"),
 shot(37, "sat a Ferrari from nineteen sixty-one.",
      f"The magazines are moved aside in piles on the floor: {FERRARI} is fully uncovered, dusty but whole. "
      f"{FAMILY_FR} stand around it with their jaws dropped.",
      BARN_IN,
      "the old sports car uncovered from under the magazines, the family amazed",
      "any badge or letters"),
 shot(38, "A French movie star had once owned it.",
      f"Long ago: a stick figure in dark sunglasses and a smart jacket drives {FERRARI} along a seaside road, one "
      "hand waving; at the roadside, photographers with old flash cameras snap pictures of him, flash bursts.",
      "a sunny seaside road in the nineteen sixties with palm trees and the sea",
      "a famous star from long ago driving the same sports car, photographers snapping him",
      "any likeness of a real person, any letters"),
 shot(39, "In twenty fifteen,",
      f"{PARIS_AUCTION}. {FERRARI} stands on the low stage. A small sign on the front of the podium shows \"2015\".",
      "the Paris auction hall, filling the frame",
      "the grand Paris auction hall, the sports car on stage, 2015 on the podium sign",
      "any letters other than 2015"),
 shot(40, "it sold at an auction in Paris",
      f"{PARIS_AUCTION}. The auctioneer raises his gavel high; many bidders lift their paddles; {FERRARI} gleams on "
      "the stage.",
      "the same Paris auction hall, filling the frame",
      "the raised gavel, bidders' paddles up, the Eiffel Tower through the window",
      "any letters"),
 shot(41, "for over sixteen million euros.",
      f"{PARIS_AUCTION}. The gavel slams down with impact lines. Beside {FERRARI} rises a tower of banknotes with "
      f"\"€\" symbols reaching the top of the frame.",
      "the same Paris auction hall, filling the frame",
      "the gavel coming down, the sports car and the giant euro cash tower",
      "any letters"),
 shot(42, "What's been sitting in your garage all these years?",
      "A friendly stick figure faces the viewer, lifting the corner of a dusty sheet off something big in a cluttered "
      "home garage, with a curious grin; a big question mark floats above.",
      "a cluttered home garage: shelves of paint tins and boxes, a bicycle on the wall, a lawn mower, a closed "
      "roller door",
      "the stick figure peeking under a dusty sheet in a garage, and the question mark",
      "showing what is under the sheet, any letters"),
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
