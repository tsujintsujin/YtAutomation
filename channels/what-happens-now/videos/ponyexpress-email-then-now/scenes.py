"""Image prompts for ponyexpress-email-then-now, written as one story (channels/SHORTS_RULES.md "How image prompts are
written"; worked example: ../tooth-key-then-now/scenes.py). Checks every line against script.md; this file approves the
script (no approval step) and writes scene + full prompt for every line into script.json.
usage: python channels/what-happens-now/videos/ponyexpress-email-then-now/scenes.py"""
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent                 # videos/<slug>
ROOT = HERE.parents[3]                                 # YtAutomation
sys.path.insert(0, str(ROOT))
from dashboard import approve, short_lines, short_prompt       # the script's lines, and the fixed frame around every prompt

SETTINGS = json.loads((HERE.parents[1] / "settings.json").read_text(encoding="utf-8"))
STYLE = SETTINGS["image_style"]

# ---- the same words every time a person, object or place appears ----
# eighteen sixty
WRITER = ("a stick-figure woman from eighteen sixty (hair parted in the middle and pulled back in a bun, a long full "
          "dress with a high collar and long sleeves)")
PARLOUR = ("a parlour in eighteen sixty: a small wooden writing desk by a window with curtains, an oil lamp, a "
           "patterned rug, a framed picture on the wall")
PEN = "a dip pen (a thin wooden holder with a pointed metal nib) and a small glass ink pot"
LETTER = "a letter (a sheet of paper covered in neat squiggly handwriting lines, no readable words)"
ENVELOPE = "a plain paper envelope"
POST_OFFICE = ("a small post office in eighteen sixty: a wooden counter with a little brass scale on it, rows of "
               "wooden pigeonholes for letters behind it, a clerk in sleeve garters and a visor cap")
RIDER = ("a Pony Express rider (a young, light stick-figure man in a wide-brimmed hat, a scarf around his neck, a "
         "buckskin jacket with fringes, and riding boots)")
RIDER2 = ("a second Pony Express rider (a young stick-figure man in a flat-crowned hat, a plain shirt with a "
          "neckerchief, a vest and riding boots)")
HORSE = "a fast slim horse"
MOCHILA = ("the mail cover (a flat leather cover thrown over the saddle, with four leather pockets, two on each side, "
           "each closed with a small padlock)")
STATION = ("a small Pony Express relay station on the prairie: a little log hut with a sod roof, a wooden corral "
           "fence, a water trough, and a fresh saddled horse waiting, held by a station keeper in an apron and a hat")
HOME_STATION = ("a bigger Pony Express home station on the prairie: a long log building with a porch, a corral with "
                "several horses, a water trough, a wagon")
PRAIRIE = ("the open American West in eighteen sixty: wide flat grassy prairie, a dirt trail, a few low hills, and "
           "snowy mountains far off under a big sky")
DESERT = "a desert at night: sand, sagebrush, a few rocks, a full moon and stars"
MOUNTAINS = "a steep mountain pass: pine trees, rocky slopes, snow on the peaks"
SACRAMENTO = ("Sacramento, California, in eighteen sixty: a wide river with a steamboat, a dusty main street of "
              "wooden two-storey buildings with porches and balconies")
POLES = "a long line of wooden telegraph poles with one wire strung between them, running to the horizon"
# now
YOU = "a stick-figure young man (short spiky hair, plain T-shirt and jeans)"
FRIEND = "a stick-figure young woman (long hair in a ponytail, a hoodie)"
ROOM_NOW = ("a modern living room: a sofa, a small table with a laptop on it, a window, a lamp")
LAPTOP = "a laptop (an open screen above a keyboard)"
PHONE = "a smartphone (a flat rectangle with a screen)"
PACKETS = "small square boxes (the packets)"
CABLE = "a thick cable drawn see-through, so you can see the glass threads inside it"
SEAFLOOR = ("the bottom of the ocean: sand, rocks, seaweed, a few fish, dark water above with light rays from far up")
# ---- the one coloured thing per picture (settings.json "colour_subject") ----
C_SKY = "the big sky: flat light blue, with the far mountains' snow flat white"
C_LETTER = "the letter in the saddle pouch: flat cream white"
C_INK = "the ink: flat deep blue in the pot and on the nib"
C_ENVELOPE = "the envelope: flat cream white"
C_COINS = "the gold coins: flat gold yellow"
C_SCALE = "the letter flat cream white and the gold coins flat gold yellow"
C_STATION = "the Pony Express station's log walls: flat warm brown"
C_MOCHILA = "the leather mail cover: flat tan brown"
C_LOCKS = "the four small padlocks: flat gold"
C_HORSE = "the galloping horse: flat chestnut brown"
C_FRESH = "the fresh horse: flat grey-white"
C_RIDER = "the rider's buckskin jacket: flat tan"
C_RIDER2 = "the new rider's vest: flat dark red"
C_MOON = "the full moon: flat pale yellow, and the night sky flat deep blue"
C_RIVER = "the river: flat blue"
C_BOARD = "the boards nailed across the door: flat raw brown"
C_WIRE = "the telegraph wire and poles: flat dark brown poles with a flat black wire"
C_LAPTOP = "the laptop screen: flat light blue"
C_BITS = "the streams of ones and zeros: flat bright green"
C_PACKETS = "the packets: flat orange"
C_TAGS = "the packets flat orange, each with a small flat white address tag"
C_LIGHT = "the flashes of light: flat bright yellow"
C_CABLE = "the cable on the ocean floor: flat black, with a flat bright yellow light glow"
C_ROUTES = "the packets: flat orange"
C_ORDER = "the packets clicking into a row: flat orange"
C_PHONE = "the phone's screen with the new message envelope icon: flat bright blue"
C_TIRED = "the tired horses: flat chestnut brown"
C_WATCH = "the tiny stopwatch: flat red"
CAPTIONS = ("The place fills the whole frame; keep the very top and very bottom of the frame calm (sky, wall or floor) "
            "for captions. Never write any name, label or caption under or beside anyone or anything.")

M = 29


def shot(n, text, what, place, must, never="", colour=""):
    what = re.sub(r"(^|\. )([a-z])", lambda m: m[1] + m[2].upper(), what)   # blocks start lowercase
    return n, text, " ".join(x for x in (
        f"This is picture {n} of {M} in one continuous picture story; draw exactly this moment.",
        what, f"Place: {place}.",
        f"The one coloured thing in this picture is {colour}; every other person, object and the whole place are black "
        "ink lines only, no colour.",
        f"It MUST show: {must}.", f"NEVER: {never}." if never else "", CAPTIONS) if x)


S = [
 shot(1, "In eighteen sixty,",
      "Wide empty view of the open West, the dirt trail running toward the far mountains.",
      PRAIRIE,
      "the wide open American West of eighteen sixty",
      "any modern thing, any roads or cars",
      colour=C_SKY),
 shot(2, "a letter across America rode on a galloping horse.",
      f"{RIDER} gallops along the trail on {HORSE}; a letter sticks out of a pocket of {MOCHILA}, speed lines and "
      "dust behind.",
      PRAIRIE,
      "the letter riding along in the saddle pocket of a galloping horse",
      "any modern thing, any letters or words",
      colour=C_LETTER),
 shot(3, "You wrote it with a pen you dipped in ink.",
      f"{WRITER} sits at the writing desk and dips the pointed metal nib of a dip pen (a thin wooden holder with a "
      f"pointed metal nib) into a small glass ink pot, a half-written {LETTER[2:]} in front of her.",
      PARLOUR,
      "the woman dipping her pen in the ink to write the letter",
      "a ballpoint pen, any readable words",
      colour=C_INK),
 shot(4, "You folded it into an envelope.",
      f"{WRITER} folds {LETTER} in thirds and slides it into {ENVELOPE}.",
      PARLOUR,
      "the letter being folded into the envelope",
      "any readable words, any stamps with letters",
      colour=C_ENVELOPE),
 shot(5, "Then you paid five dollars to send it,",
      f"{WRITER} hands five gold coins across the wooden counter to the clerk, who holds her envelope.",
      POST_OFFICE,
      "the woman paying five gold coins to send the letter",
      "paper money, any numbers or letters",
      colour=C_COINS),
 shot(6, "for half an ounce of paper.",
      "Close view of the little brass scale on the counter: the thin envelope sits on one pan, light as a feather, "
      "and beside the scale lie five gold coins, looking heavy.",
      POST_OFFICE + "; the close view of the counter fills most of the frame",
      "the tiny light letter next to the five coins it cost",
      "any numbers or letters",
      colour=C_SCALE),
 shot(7, "In Missouri, the Pony Express took it.",
      f"{RIDER} stands beside {HORSE} in front of a small wooden Pony Express office on a town street, ready to "
      "ride, as a clerk hands him a bundle of envelopes.",
      "a small town street in Missouri in eighteen sixty: wooden buildings with porches, a dirt road, hitching posts",
      "the Pony Express rider taking the mail, ready to ride",
      "any letters or signs",
      colour=C_STATION),
 shot(8, "A rider put it in a leather cover over his saddle,",
      f"{RIDER} stuffs the bundle of envelopes into one pocket of {MOCHILA} on the saddle of {HORSE}.",
      "a small town street in Missouri in eighteen sixty: wooden buildings with porches, a dirt road, hitching posts",
      "the rider putting the letters into the leather saddle cover",
      "any letters or words",
      colour=C_MOCHILA),
 shot(9, "with four locked pockets.",
      f"Close view of {MOCHILA} over the saddle, all four pockets clearly visible with their small padlocks.",
      "a small town street in Missouri in eighteen sixty; the close view of the saddle fills most of the frame",
      "the leather cover with its four locked pockets",
      "any letters or words",
      colour=C_LOCKS),
 shot(10, "He galloped as hard as his horse could go.",
      f"{RIDER} leans low over the neck of {HORSE}, galloping flat out along the trail, dust clouds and speed lines "
      "behind.",
      PRAIRIE,
      "the rider galloping as fast as the horse can go",
      "any modern thing",
      colour=C_HORSE),
 shot(11, "Every ten to fifteen miles, there was a station.",
      f"{RIDER} gallops up the trail toward the small relay station.",
      STATION,
      "the small relay station with a fresh horse waiting",
      "any letters or signs",
      colour=C_FRESH),
 shot(12, "He jumped onto a fresh horse, and kept going.",
      f"{RIDER} leaps from his tired, sweating horse onto the fresh grey horse, swinging {MOCHILA} across with him, "
      "while the station keeper holds the reins.",
      STATION,
      "the rider jumping from the tired horse onto the fresh horse",
      "any letters or signs",
      colour=C_FRESH),
 shot(13, "After seventy-five miles or more,",
      f"{RIDER}, dusty and tired, rides up to the bigger home station on a worn-out horse.",
      HOME_STATION,
      "the tired rider arriving at the bigger station",
      "any letters or signs",
      colour=C_RIDER),
 shot(14, "a new rider grabbed the leather cover and rode on.",
      f"{RIDER2} throws {MOCHILA} over his own saddle and gallops away, while the first rider sits down on the porch, "
      "exhausted.",
      HOME_STATION,
      "the new rider taking the mail cover and galloping away",
      "any letters or signs",
      colour=C_RIDER2),
 shot(15, "Day and night, across deserts and mountains.",
      f"The picture is split across the middle by a simple line. Top half: {RIDER2} gallops across {DESERT}. "
      f"Bottom half: he rides up through {MOUNTAINS}.",
      f"top half: {DESERT}; bottom half: {MOUNTAINS}",
      "the rider crossing the desert at night and the mountains",
      "any modern thing",
      colour=C_MOON),
 shot(16, "About ten days later, it reached California.",
      f"{RIDER2} rides into the main street of the town by the river, holding up a letter, as townspeople look up.",
      SACRAMENTO,
      "the rider arriving in California with the letter",
      "any letters or signs on buildings",
      colour=C_RIVER),
 shot(17, "But it only lasted a year and a half.",
      "The small relay station stands empty: the corral is empty, the water trough dry, and wooden boards are nailed "
      "in an X across its door.",
      STATION.replace(", and a fresh saddled horse waiting, held by a station keeper in an apron and a hat", ""),
      "the Pony Express station closed and empty",
      "any letters or words",
      colour=C_BOARD),
 shot(18, "A telegraph wire across the country beat it.",
      f"{POLES}; {RIDER} has stopped his horse beside them and stares along the wire, surprised.",
      PRAIRIE,
      "the telegraph wire stretching across the land, beating the rider",
      "any letters or words",
      colour=C_WIRE),
 shot(19, "Today, you type an email and press send.",
      f"{YOU} sits on the sofa with {LAPTOP} on the table and taps one key with a finger.",
      ROOM_NOW,
      "the young man pressing send on his laptop",
      "any readable letters on the screen, any logos",
      colour=C_LAPTOP),
 shot(20, "Your words turn into ones and zeros.",
      f"Close view of the screen of {LAPTOP}: lines of squiggly writing stream off the screen and turn into long "
      "streams of the digits 1 and 0.",
      ROOM_NOW + "; the close view of the laptop fills most of the frame",
      "the words turning into streams of 1s and 0s",
      "any readable words",
      colour=C_BITS),
 shot(21, "They're split into tiny packets.",
      f"A long stream of 1s and 0s is chopped by a pair of scissors into {PACKETS}, each holding a short piece of the "
      "stream.",
      "a plain flat white background with a simple floor line",
      "the stream being split into small packets",
      "any readable words",
      colour=C_PACKETS),
 shot(22, "Each packet gets the address of where it's going.",
      f"A row of {PACKETS}; a stick-figure hand sticks a small tag with a little house symbol on each one.",
      "a plain flat white background with a simple floor line",
      "every packet getting an address tag",
      "any readable words or numbers on the tags",
      colour=C_TAGS),
 shot(23, "They race through cables as flashes of light.",
      f"{CABLE}: bright flashes of light zoom along the glass threads inside it, carrying the small square packets.",
      "a plain flat white background; the cable runs across the whole frame",
      "flashes of light racing through the cable",
      "any letters",
      colour=C_LIGHT),
 shot(24, "Some cables lie on the bottom of the ocean.",
      "A long thick cable lies along the sea floor and disappears into the distance, a faint light glowing inside "
      "it; fish swim past and a crab sits beside it.",
      SEAFLOOR,
      "the cable lying on the bottom of the ocean",
      "any divers, any letters",
      colour=C_CABLE),
 shot(25, "Each packet can take a different road.",
      f"A simple map of lines and dots like a road map, from one house on the left to one house on the right; "
      f"{PACKETS} travel along different lines, each taking its own route.",
      "a plain flat white background with a simple map of lines",
      "the packets taking different routes across the map",
      "any letters or names",
      colour=C_ROUTES),
 shot(26, "At the other end, they're put back together, in order.",
      f"{PACKETS} arriving from different directions click together into one neat straight row, side by side.",
      "a plain flat white background with a simple floor line",
      "the packets lining back up in order",
      "any numbers or letters",
      colour=C_ORDER),
 shot(27, "And it lands in the inbox in about a second.",
      f"{FRIEND} sits in a café holding {PHONE}; its screen lights up with a simple closed-envelope icon, small "
      "ding lines around it.",
      "a modern café: a small round table, a coffee cup, a big window, a plant",
      "the message arriving on her phone",
      "any readable words, any logos",
      colour=C_PHONE),
 shot(28, "Back then, ten days and a lot of tired horses.",
      "A row of tired horses at a corral fence, heads drooping, panting, sweat drops, one lying down.",
      HOME_STATION,
      "a row of exhausted horses",
      "any modern thing, any letters",
      colour=C_TIRED),
 shot(29, "Now? About one second.",
      f"{FRIEND} reads her phone, smiling; beside her floats a tiny stopwatch whose hand has barely moved.",
      "a modern café: a small round table, a coffee cup, a big window, a plant",
      "the woman already reading the message, with a stopwatch showing almost no time",
      "any numbers or readable words",
      colour=C_WATCH),
]

lines = short_lines((HERE / "script.md").read_text(encoding="utf-8"))
assert len(S) == M and [(i, t) for i, t, _, _ in lines] == [(n, t) for n, t, _ in S], "scenes.py and script.md differ"
p = HERE / "script.json"
if not p.exists():
    print(approve(HERE.name)["message"])            # no approval step (Justin, 2026-10-19)
data = json.load(open(p, encoding="utf-8"))
segs = data["segments"]
assert len(segs) == M
for seg, (n, text, scene) in zip(segs, S):
    assert seg["id"] == n and seg["text"] == text, (n, seg["text"], text)
    seg["scene"] = scene
    seg["prompt"] = short_prompt(scene, STYLE, SETTINGS["colour_subject"], "paper_ref" in SETTINGS)
json.dump(data, open(p, "w", encoding="utf-8"), indent=1, ensure_ascii=False)
print("written", len(segs), "longest", max(len(s["prompt"]) for s in segs), "shortest", min(len(s["prompt"]) for s in segs))
