"""Image prompts for photo-plate-then-now, written as one story (channels/SHORTS_RULES.md "How image prompts are
written"; worked example: ../tooth-key-then-now/scenes.py). Checks every line against script.md; this file approves the
script (no approval step) and writes scene + full prompt for every line into script.json.
usage: python channels/what-happens-now/videos/photo-plate-then-now/scenes.py"""
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
# the eighteen forties
STUDIO = ("a photo studio in the eighteen forties: a big skylight window in the ceiling letting in bright daylight, a "
          "heavy curtain hanging as a backdrop, a plain wooden posing chair, a small side table, a wooden floor")
CAMERA = ("a big wooden box camera on a three-legged wooden stand, with a short brass lens tube on the front closed "
          "by a round brass lens cap")
PHOTOGRAPHER = ("the photographer (a stick-figure man with bushy side-whiskers, a waistcoat, a bow tie and his shirt "
                "sleeves rolled up)")
SITTER = ("the sitter (a stick-figure man in a dark frock coat, a high stiff collar and a cravat, his hair neatly "
          "combed)")
PLATE = "a small rectangular silver-coated copper plate, about the size of a hand"
HEAD_STAND = ("a head stand (a tall iron stand behind the chair with a small curved clamp at the top that holds the "
              "back of the sitter's head)")
DARKROOM = ("a small dark room in the eighteen forties: one dim lamp behind a red glass shade, a wooden workbench with "
            "small wooden boxes, glass jars and dishes, shelves with bottles (no labels)")
IODINE_BOX = "a small wooden box with fumes curling up out of its open top"
MERCURY_BOX = "a small wooden box on legs with a little spirit-lamp flame under it, fumes curling up out of its top"
SALT_DISH = "a flat glass dish of salt water"
CASE = "a small hinged leather-covered case, open, with the picture plate behind glass on one side"
# now
YOU = "a stick-figure young woman (long hair in a ponytail, a plain T-shirt)"
PARK = "a sunny park: green grass, trees, a path, a bench, a few clouds"
PHONE = "a smartphone (a flat rectangle with a screen and a small round camera lens on its back)"
PHONE_CUT = ("a cut-away side view of a smartphone's camera, as if sliced: a tiny round lens at the back of the phone, "
             "and right behind it a tiny flat square sensor chip")
GRID = "a close view of the sensor: a grid of very many tiny squares in neat rows"
# ---- the one coloured thing per picture (settings.json "colour_subject") ----
C_CAMERA = "the wooden box camera: flat warm brown with a flat gold brass lens"
C_SITTER = "the sitter's frock coat: flat dark blue"
C_CLOCK = "the clock: flat white face with a flat red hand"
C_PLATE = "the plate: flat shiny silver"
C_MIRROR = "the plate's mirror shine: flat shiny silver"
C_FUMES = "the iodine fumes: flat purple"
C_SUN = "the small sun symbol flat yellow and the plate flat shiny silver"
C_CHAIR = "the posing chair: flat red velvet seat"
C_STAND = "the iron head stand: flat dark iron grey"
C_FACE = "the sitter's stiff face: flat pale pink"
C_CAP = "the round brass lens cap: flat gold"
C_RELIEF = "the sitter's frock coat: flat dark blue"
C_MERCURY = "the mercury fumes: flat silvery grey"
C_APPEAR = "the face appearing on the plate: flat silver grey"
C_SKULL = "the skull warning symbol: flat red"
C_SALT = "the salt water: flat light blue"
C_CASE = "the little case: flat dark red leather with a flat gold edge"
C_ONE = "the number 1: flat bright red"
C_REVERSE = "the arrows showing the hand on opposite sides: flat bright red"
C_PHONE = "the phone: flat dark blue"
C_LIGHT = "the light rays: flat bright yellow"
C_GRID = "the grid of tiny squares: flat light blue"
C_BRIGHT = "the light rays: flat bright yellow, with the lit squares flat pale yellow"
C_FILTERS = "the coloured filters: flat red, flat green and flat blue squares in a pattern"
C_NUMBERS = "the photo coming out of the chip: flat green grass and flat blue sky"
C_SCREEN = "the photo on the phone screen: flat green grass and flat blue sky"
C_COPIES = "the flying copies of the photo: flat green grass and flat blue sky in each"
C_FROZEN = "the iron head stand: flat dark iron grey"
C_SELFIE = "the young woman's T-shirt: flat bright yellow"
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
 shot(1, "In the eighteen forties,",
      f"Wide view of the studio: {CAMERA} stands facing the empty posing chair under the skylight.",
      STUDIO,
      "the old photo studio with its big box camera",
      "any modern camera, any phone",
      colour=C_CAMERA),
 shot(2, "getting your photo taken meant sitting perfectly still.",
      f"{SITTER} sits bolt upright in the posing chair, hands on his knees, staring at {CAMERA}.",
      STUDIO,
      "the man sitting stiff and still in front of the camera",
      "a smile, any modern thing",
      colour=C_SITTER),
 shot(3, "Sometimes for close to a minute.",
      f"{SITTER} sits frozen in the posing chair; beside him a big round wall clock's hand sweeps around almost a "
      "full circle, with a curved arrow.",
      STUDIO,
      "the sitter frozen while the clock hand sweeps round",
      "any numbers on the clock",
      colour=C_CLOCK),
 shot(4, "First, the photographer polished a silver-coated copper plate",
      f"{PHOTOGRAPHER} buffs {PLATE} on the side table with a soft cloth pad, rubbing hard.",
      STUDIO,
      "the photographer polishing the small metal plate",
      "any paper photo",
      colour=C_PLATE),
 shot(5, "until it shone like a mirror.",
      f"{PHOTOGRAPHER} holds up {PLATE}; it shines like a mirror and shows a small reflection of his own face, with "
      "sparkle lines.",
      STUDIO,
      "the plate shining like a mirror",
      "any letters",
      colour=C_MIRROR),
 shot(6, "In the dark, he held it over iodine fumes,",
      f"{PHOTOGRAPHER} holds {PLATE} face-down over {IODINE_BOX}.",
      DARKROOM,
      "the plate held over the box of fumes in the dark room",
      "any labels or letters on bottles",
      colour=C_FUMES),
 shot(7, "so it would react to light.",
      f"Close view of {PLATE}; above it a small sun symbol, with tiny sparkle lines on the plate's surface.",
      DARKROOM + "; the close view of the plate fills most of the frame",
      "the plate now ready to catch light",
      "any letters",
      colour=C_SUN),
 shot(8, "Then you sat down.",
      f"{SITTER} lowers himself into the posing chair, straightening his coat.",
      STUDIO,
      "the sitter sitting down in the posing chair",
      "any phone",
      colour=C_CHAIR),
 shot(9, "A metal stand behind you held your head still.",
      f"Side view: {SITTER} sits in the posing chair, and {HEAD_STAND} stands behind the chair, its clamp pressed "
      "against the back of his head.",
      STUDIO,
      "the iron stand holding the sitter's head still from behind",
      "anything around his neck, anything painful",
      colour=C_STAND),
 shot(10, "That's probably one reason nobody smiled.",
      f"Close view of the face of {SITTER}: a stiff, serious straight-line mouth, eyes wide open, not a hint of a "
      "smile.",
      STUDIO + "; the face fills most of the frame",
      "the sitter's stiff, serious, unsmiling face",
      "a smile",
      colour=C_FACE),
 shot(11, "He took the cap off the lens, and you froze.",
      f"{PHOTOGRAPHER} lifts the round brass lens cap off {CAMERA}; {SITTER} sits frozen stiff in the chair with "
      "small freeze lines around him, held by the head stand.",
      STUDIO,
      "the lens cap coming off and the sitter freezing",
      "any flash, any phone",
      colour=C_CAP),
 shot(12, "Then he put the cap back on.",
      f"{PHOTOGRAPHER} puts the round brass lens cap back on {CAMERA}; {SITTER} slumps in the chair with a big "
      "puff of relief.",
      STUDIO,
      "the cap going back on and the sitter slumping with relief",
      "any phone",
      colour=C_RELIEF),
 shot(13, "In a dark room, he held the plate over hot mercury fumes,",
      f"{PHOTOGRAPHER} holds {PLATE} face-down over {MERCURY_BOX}, leaning back from the fumes.",
      DARKROOM,
      "the plate held over the heated box of mercury fumes",
      "any labels or letters",
      colour=C_MERCURY),
 shot(14, "and your face slowly appeared.",
      f"Close view of {PLATE}: the faint outline of the sitter's face and shoulders slowly fading in on its surface.",
      DARKROOM + "; the close view of the plate fills most of the frame",
      "the sitter's face slowly appearing on the plate",
      "any letters",
      colour=C_APPEAR),
 shot(15, "Mercury is poisonous.",
      f"The fumes curling up from {MERCURY_BOX}, with a simple skull warning symbol floating in them; "
      f"{PHOTOGRAPHER} coughs and waves the fumes away.",
      DARKROOM,
      "the poisonous fumes, shown with a skull warning symbol",
      "any letters",
      colour=C_SKULL),
 shot(16, "Salt water stopped the picture from changing.",
      f"{PHOTOGRAPHER} dips {PLATE} into {SALT_DISH}; the face on the plate stays clear.",
      DARKROOM,
      "the plate dipped in the dish of salt water",
      "any labels or letters",
      colour=C_SALT),
 shot(17, "He sealed it behind glass, in a little case.",
      f"{PHOTOGRAPHER} presses the plate behind glass into {CASE[2:]}, the sitter's portrait showing inside.",
      STUDIO,
      "the picture sealed behind glass in the little case",
      "any letters",
      colour=C_CASE),
 shot(18, "And there was only one.",
      f"{CASE} sits alone on the side table, and beside it floats one big number 1.",
      STUDIO,
      "the one single picture, with no copies",
      "any copies, any other numbers or letters",
      colour=C_ONE),
 shot(19, "It was even backwards, like a mirror.",
      f"Left: {SITTER} with his right hand on his chest. Right: his picture in the open case, with the hand on the "
      "other side; two small curved arrows show it is flipped.",
      STUDIO,
      "the sitter and his picture flipped like a mirror",
      "any letters",
      colour=C_REVERSE),
 shot(20, "Today, you tap a button.",
      f"{YOU} holds up {PHONE} and taps the round shutter button on its screen with her thumb.",
      PARK,
      "the young woman tapping the button to take a photo",
      "any logos or letters",
      colour=C_PHONE),
 shot(21, "Light goes through a tiny lens onto a sensor.",
      f"{PHONE_CUT}; rays of light come in from the park, pass through the tiny lens and land on the sensor chip.",
      "a plain flat white background; the cut-away phone fills most of the frame",
      "light rays going through the lens onto the sensor",
      "any letters",
      colour=C_LIGHT),
 shot(22, "It's a grid of millions of tiny squares, called pixels.",
      f"{GRID}, stretching to the edges of the frame.",
      "inside a phone camera; the grid fills the frame",
      "the grid of very many tiny squares",
      "any letters or numbers",
      colour=C_GRID),
 shot(23, "Each one measures how much light hits it.",
      f"{GRID}: light rays land on the squares; some squares glow bright where lots of light hits, others stay dark.",
      "inside a phone camera; the grid fills the frame",
      "each little square catching more or less light",
      "any letters or numbers",
      colour=C_BRIGHT),
 shot(24, "Tiny colored filters let each pixel see red, green, or blue.",
      f"{GRID}, each tiny square covered by a little coloured filter in a repeating checkerboard pattern.",
      "inside a phone camera; the grid fills the frame",
      "the pattern of red, green and blue filters on the squares",
      "any letters or numbers",
      colour=C_FILTERS),
 shot(25, "A chip puts all those numbers together into your photo.",
      "Streams of small numbers flow from the grid into a small square chip with short legs, and out of the other "
      "side comes a finished photo of the park.",
      "a plain flat white background with a simple table line",
      "the chip turning the numbers into a photo",
      "any letters",
      colour=C_NUMBERS),
 shot(26, "It cleans it up and saves it, in less than a second.",
      f"The park photo appears on the screen of {PHONE}; a tiny stopwatch beside it has barely moved.",
      PARK,
      "the photo appearing on the phone screen almost instantly",
      "any numbers or letters",
      colour=C_SCREEN),
 shot(27, "And you can send copies to anyone.",
      f"{YOU} taps her phone, and copies of the same park photo fly out as small pictures to several other phones "
      "held by stick-figure friends around her.",
      PARK,
      "copies of the photo flying out to friends' phones",
      "any letters or logos",
      colour=C_COPIES),
 shot(28, "Back then, a minute of sitting frozen.",
      f"{SITTER} sits frozen stiff in the posing chair, his head held by {HEAD_STAND}, staring at {CAMERA}.",
      STUDIO,
      "the sitter frozen in the chair with his head clamped",
      "any modern thing",
      colour=C_FROZEN),
 shot(29, "Now? Tap. Done.",
      f"{YOU} holds {PHONE} out at arm's length and takes a selfie, grinning widely, making a peace sign.",
      PARK,
      "the young woman taking a quick smiling selfie",
      "any letters or logos",
      colour=C_SELFIE),
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
