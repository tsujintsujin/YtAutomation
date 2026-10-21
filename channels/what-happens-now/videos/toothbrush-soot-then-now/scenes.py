"""Image prompts for toothbrush-soot-then-now, written as one story (channels/SHORTS_RULES.md "How image prompts are
written"; worked example: ../tooth-key-then-now/scenes.py). Checks every line against script.md; this file approves the
script (no approval step) and writes scene + full prompt for every line into script.json.
usage: python channels/what-happens-now/videos/toothbrush-soot-then-now/scenes.py"""
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
# the seventeen hundreds
MAN1700 = ("a stick-figure man from the seventeen hundreds (a white shirt with a loose neck tie, a waistcoat, knee "
           "breeches, his hair tied back in a short ponytail)")
ROOM1700 = ("a plain bedroom in the seventeen hundreds: wooden floorboards, a small window with little square panes, "
            "a wooden washstand with a china jug and basin, a small mirror on the wall, a candle")
RAG = "a small rag (a scrap of plain cloth)"
SOOT = "a small dish of black soot"
SALT = "a small dish of white salt"
# ancient times
EGYPTIAN = ("a man from ancient Egypt (a stick figure in a simple white wrap-around kilt, bare chest, short black hair "
            "and a wide collar necklace)")
NILE = ("the bank of the Nile in ancient Egypt: tall papyrus reeds, a palm tree, the river, and a small pyramid far "
        "off under a hot sun")
TWIG = "a short twig, as long as a finger"
MORTAR = "a stone mortar (a small heavy stone bowl) and a pestle"
# Addis
PRISON_OUT = ("an old London prison in the seventeen hundreds: a high grey stone wall, a heavy arched wooden gate with "
              "iron studs, small barred windows")
CELL = ("a bare prison cell in the seventeen hundreds: stone walls, a small high barred window, a straw mattress on the "
        "floor, a wooden stool and a heavy wooden door")
ADDIS = ("a prisoner (a stick-figure man with a long untidy coat, a loose shirt and messy hair)")
GUARD = "a prison guard (a stick-figure man in a long coat with a ring of keys on his belt)"
BONE = "a small smooth animal bone, as long as a hand"
NAIL = "an iron nail"
BRISTLES = "small tufts of stiff pig bristle"
BONE_BRUSH = ("a bone toothbrush (a small smooth bone handle with neat rows of stiff bristle tufts stuck into holes at "
              "one end)")
SHOP1780 = ("a small shop in the seventeen eighties: a wooden counter, shelves behind it, a big window with small "
            "square panes, a wooden floor")
CUSTOMER = ("a customer from the seventeen eighties (a stick-figure woman in a long full dress and a white cap)")
SIBERIA = ("a snowy land in Siberia: deep snow, tall dark pine trees, a grey winter sky, snowflakes falling")
PIGS = "a few shaggy pigs with long thick bristly hair"
# now
YOU = "a stick-figure young man (short spiky hair, plain T-shirt)"
BATHROOM = ("a modern bathroom: a white sink with a tap, a big mirror above it, tiled walls, a cup on the sink edge, "
            "a towel on a rail, a small bin")
BRUSH = "a modern toothbrush (a smooth plastic handle with a neat block of straight bristles)"
TUBE = "a tube of toothpaste (no letters on it)"
TEETH = ("a close view of a row of clean rounded teeth, upper and lower, with the gums drawn as a simple outline")
# ---- the one coloured thing per picture (settings.json "colour_subject") ----
C_JUG = "the china jug and basin: flat pale blue"
C_RAG = "the rag: flat pale tan"
C_SOOT = "the soot flat black and the salt flat white, in two small dishes"
C_SMUDGE = "the black soot smudges on his teeth: flat black"
C_TWIG = "the twig: flat warm brown"
C_FRAY = "the frayed end of the twig: flat light tan fibres"
C_SUN = "the hot sun: flat yellow, and the Nile flat blue"
C_POWDER = "the white powder: filled flat bright white"
C_SHELLS = "the crushed eggshells and shells: flat creamy white with flat pale pink bits"
C_PRISON = "the prison's stone wall: flat grey"
C_DOOR = "the heavy cell door: flat dark brown"
C_BONE = "the bone: flat creamy white"
C_NAIL = "the iron nail: flat dark grey"
C_BRISTLE = "the bristle tufts: flat dark brown"
C_BRUSH_OLD = "the bone toothbrush: its handle flat creamy white, its bristles flat dark brown"
C_BRUSHES = "the row of bone toothbrushes: handles flat creamy white, bristles flat dark brown"
C_PIGS = "the shaggy pigs: flat reddish brown"
C_BRUSH_NEW = "the modern toothbrush: its handle flat bright blue, its bristles flat white and flat light blue"
C_PASTE = "the toothpaste: flat white with a flat mint green stripe"
C_SHIELD = "the shield flat bright blue, and the germ blobs flat green"
C_SUNMOON = "the sun flat yellow and the moon flat pale yellow"
C_CIRCLES = "the small circle arrows: flat bright blue"
C_FOAM = "the foam: flat white with a flat mint green tint"
C_WATER = "the tap water: flat bright blue"
C_NEW = "the new toothbrush flat bright blue, and the old worn one flat grey"
C_SPLIT = "the bone brush flat creamy white with flat dark brown bristles, and the soot flat black"
C_FINAL = "the modern toothbrush flat bright blue, and the toothpaste blob flat white with a flat mint green stripe"
CAPTIONS = ("The place fills the whole frame; keep the very top and very bottom of the frame calm (sky, wall or floor) "
            "for captions. Never write any name, label or caption under or beside anyone or anything.")

M = 28


def shot(n, text, what, place, must, never="", colour=""):
    what = re.sub(r"(^|\. )([a-z])", lambda m: m[1] + m[2].upper(), what)   # blocks start lowercase
    return n, text, " ".join(x for x in (
        f"This is picture {n} of {M} in one continuous picture story; draw exactly this moment.",
        what, f"Place: {place}.",
        f"The one coloured thing in this picture is {colour}; every other person, object and the whole place are black "
        "ink lines only, no colour.",
        f"It MUST show: {must}.", f"NEVER: {never}." if never else "", CAPTIONS) if x)


S = [
 shot(1, "In the seventeen hundreds,",
      f"{MAN1700} stands at the wooden washstand in the morning, looking into the small mirror.",
      ROOM1700,
      "the man of the seventeen hundreds at his washstand",
      "any toothbrush, any modern thing",
      colour=C_JUG),
 shot(2, "you cleaned your teeth with a rag,",
      f"{MAN1700} holds {RAG} up to his bared teeth, looking in the mirror.",
      ROOM1700,
      "the man holding a rag up to his teeth",
      "any toothbrush",
      colour=C_RAG),
 shot(3, "dipped in soot and salt.",
      f"{MAN1700} dips {RAG} into {SOOT} on the washstand; beside it sits {SALT}.",
      ROOM1700,
      "the rag being dipped into the soot, with the salt beside it",
      "any toothbrush, any letters",
      colour=C_SOOT),
 shot(4, "You rubbed the black, gritty mix over every tooth.",
      f"{MAN1700} rubs the blackened rag hard over his teeth in a big grin; his teeth are smudged black, and he "
      "squints at the gritty taste.",
      ROOM1700,
      "the man rubbing the black soot over his teeth",
      "any toothbrush",
      colour=C_SMUDGE),
 shot(5, "Long before that, people used a chew stick.",
      f"{EGYPTIAN} stands by the river holding up {TWIG}.",
      NILE,
      "the ancient man holding up the chew stick twig",
      "any toothbrush, any letters or hieroglyphs",
      colour=C_SUN),
 shot(6, "You chewed the end of a twig",
      f"{EGYPTIAN} chews on the end of {TWIG}, his cheeks working, small chew lines.",
      NILE,
      "the man chewing the end of the twig",
      "any toothbrush",
      colour=C_TWIG),
 shot(7, "until it frayed into a little brush.",
      f"Close view of the end of {TWIG}: its end is split into a little bunch of soft frayed fibres, like a tiny "
      "brush.",
      NILE + "; the close view of the twig fills most of the frame",
      "the twig's end frayed into a little brush",
      "any modern toothbrush",
      colour=C_FRAY),
 shot(8, "Then you rubbed it over your teeth.",
      f"{EGYPTIAN} rubs the frayed end of {TWIG} over his bared teeth in a big grin, small scrub lines.",
      NILE,
      "the man rubbing the frayed twig over his teeth",
      "any toothbrush",
      colour=C_TWIG),
 shot(9, "Some scrubbed with powder",
      "A stick-figure hand sprinkles fine white powder from a small clay pot onto one fingertip of the other hand.",
      "a simple clay table with a small clay pot, by a mud-brick wall in ancient times",
      "white powder being sprinkled onto a fingertip",
      "any toothbrush, any letters",
      colour=C_POWDER),
 shot(10, "made from crushed eggshells or burnt shells.",
      f"{MORTAR}: the pestle pounds broken eggshells and sea shells into powder in the mortar; a few whole eggshells "
      "and shells lie beside it.",
      "a simple clay table by a mud-brick wall in ancient times",
      "eggshells and shells being crushed into powder",
      "any letters",
      colour=C_SHELLS),
 shot(11, "Then, in seventeen seventy,",
      "Wide view of the old London prison under a grey sky, a few people in tricorn hats passing on the street.",
      PRISON_OUT,
      "the old London prison",
      "any letters or signs",
      colour=C_PRISON),
 shot(12, "a man named William Addis was thrown in prison.",
      f"{GUARD} slams the heavy wooden door of the cell shut on {ADDIS}, who looks back through the small bars of the "
      "door's window.",
      CELL,
      "the man being locked in the prison cell",
      "any name written anywhere, any likeness of a real person",
      colour=C_DOOR),
 shot(13, "He saved a bone from his dinner.",
      f"{ADDIS} sits on the wooden stool holding up {BONE} from an empty tin plate on his lap, studying it with a "
      "bright idea look.",
      CELL,
      "the prisoner holding up a bone saved from his dinner",
      "any brush yet",
      colour=C_BONE),
 shot(14, "He poked little holes in it,",
      f"{ADDIS} pokes small holes into one end of {BONE} with {NAIL}, concentrating.",
      CELL,
      "the prisoner poking little holes in the bone",
      "any modern tool",
      colour=C_NAIL),
 shot(15, "and pushed in tufts of stiff pig hair.",
      f"Close view of the prisoner's hands pushing {BRISTLES} into the little holes in the end of {BONE}; some holes "
      "already have tufts in them.",
      CELL + "; the close view of the hands fills most of the frame",
      "the bristle tufts being pushed into the holes in the bone",
      "any plastic, any modern brush",
      colour=C_BRISTLE),
 shot(16, "After he got out,",
      f"{ADDIS} walks out through the arched prison gate into the street, holding up {BONE_BRUSH} and smiling.",
      PRISON_OUT,
      "the man leaving the prison with his bone toothbrush",
      "any letters",
      colour=C_BRUSH_OLD),
 shot(17, "he started selling brushes just like it.",
      f"Behind the wooden counter of his shop, the same man (a stick-figure man, now neat in a buttoned coat) shows "
      f"{CUSTOMER} a row of bone toothbrushes (each a small smooth bone handle with neat rows of stiff bristle tufts at one "
      "end) laid out on the counter, and she pays a coin.",
      SHOP1780,
      "the man selling rows of bone toothbrushes in his shop",
      "any letters or signs",
      colour=C_BRUSHES),
 shot(18, "The stiffest hairs came from pigs in cold places, like Siberia.",
      f"{PIGS} stand in the deep snow, their long bristly hair standing up against the cold, snowflakes on their "
      "backs.",
      SIBERIA,
      "shaggy bristly pigs in the cold snowy land",
      "any letters, any people",
      colour=C_PIGS),
 shot(19, "Today, the bristles are nylon, a kind of plastic.",
      f"{BRUSH} drawn big, standing upright in the cup on the edge of the sink.",
      BATHROOM,
      "the modern toothbrush with its neat plastic bristles",
      "any letters or logos",
      colour=C_BRUSH_NEW),
 shot(20, "You squeeze on a little blob of toothpaste.",
      f"{YOU} squeezes {TUBE} so a small neat blob of toothpaste lands on the bristles of {BRUSH}.",
      BATHROOM,
      "a little blob of toothpaste going onto the brush",
      "any letters on the tube",
      colour=C_PASTE),
 shot(21, "It has fluoride, which helps your teeth fight off holes.",
      "One big friendly tooth holding up a round shield; small round germ blobs with grumpy faces bounce off the "
      "shield.",
      BATHROOM + "; the tooth fills most of the frame",
      "the tooth protected by a shield against the germs",
      "any letters, any scary monster",
      colour=C_SHIELD),
 shot(22, "You brush for two minutes, twice a day.",
      f"{YOU} brushes his teeth at the mirror with {BRUSH}, foam on his lips; in the top corners of the picture a "
      "small sun and a small moon.",
      BATHROOM,
      "the young man brushing his teeth, morning and night",
      "any numbers or letters",
      colour=C_SUNMOON),
 shot(23, "Small circles, on the front, back and top of every tooth.",
      f"{TEETH}; the bristles of a modern toothbrush rest on the teeth, and small circle arrows are drawn on the "
      "front, on the back and on the top of the teeth.",
      "inside a mouth; the close view of the teeth fills the frame",
      "small circle arrows on the front, back and top of the teeth",
      "any letters",
      colour=C_CIRCLES),
 shot(24, "You spit it out, and don't swallow.",
      f"{YOU} leans over the sink and spits out a little foam; a small swallow symbol (a throat with an arrow) is "
      "crossed out beside him.",
      BATHROOM,
      "the young man spitting the toothpaste foam into the sink",
      "any letters",
      colour=C_FOAM),
 shot(25, "Rinse the brush, and let it dry.",
      f"{YOU} rinses {BRUSH} under the running tap, then stands it upright in the cup on the edge of the sink, a "
      "few drops falling.",
      BATHROOM,
      "the brush being rinsed and stood up to dry",
      "any letters",
      colour=C_WATER),
 shot(26, "And every three months or so, you get a new one.",
      f"{YOU} drops an old worn toothbrush with splayed, bent bristles into the small bin and holds up a brand new "
      f"{BRUSH[2:]}, smiling.",
      BATHROOM,
      "the old worn brush going in the bin and a new one in his hand",
      "any numbers or letters, any calendar",
      colour=C_NEW),
 shot(27, "Back then, a bone, pig hair, and soot.",
      f"{BONE_BRUSH} lies on the old wooden washstand beside {SOOT}.",
      ROOM1700,
      "the bone toothbrush with pig bristles beside the dish of soot",
      "any modern thing, any people",
      colour=C_SPLIT),
 shot(28, "Now? Plastic bristles and a minty blob.",
      f"{BRUSH} with a neat blob of toothpaste on its bristles, held up by {YOU} with a big clean smile, sparkle "
      "lines on his teeth.",
      BATHROOM,
      "the modern toothbrush with its blob of toothpaste and a clean smile",
      "any letters or logos",
      colour=C_FINAL),
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
