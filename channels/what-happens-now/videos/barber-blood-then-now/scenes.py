"""Image prompts for barber-blood-then-now, written as one story (channels/SHORTS_RULES.md "How image prompts are
written"; worked example: ../tooth-key-then-now/scenes.py). Checks every line against script.md; this file approves the
script (no approval step) and writes scene + full prompt for every line into script.json.
usage: python channels/what-happens-now/videos/barber-blood-then-now/scenes.py"""
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
# back then (the sixteen hundreds)
SICK = ("a stick-figure man from the sixteen hundreds (a loose white shirt with a wide flat collar, baggy knee-length "
        "breeches, long stockings and buckled shoes, messy hair)")
BARBER = ("a barber-surgeon from the sixteen hundreds (a stick-figure man with a small pointed beard, a round flat cap, "
          "a long apron over his shirt, and a comb tucked behind one ear)")
DOCTOR = ("a doctor from the sixteen hundreds (a stick-figure man in a long dark robe down to his feet and a square "
          "flat scholar's cap)")
SHOP = ("an old barber shop in the sixteen hundreds: wooden floorboards, a heavy wooden chair with armrests, a wooden "
        "shelf with metal basins, razors and scissors on it, a small window with little diamond-shaped panes, and a "
        "wooden door")
STUDY = ("an old doctor's study in the sixteen hundreds: shelves of thick old books, a wooden desk with a candle and a "
         "feather pen, and a large sheet of paper pinned on the wall")
BODY_CHART = ("a large sheet of paper pinned on the wall with a simple outline drawing of a standing human body on it")
JARS = ("four glass jars of liquid, each a different liquid: one of blood, one of clear watery liquid, one of yellow "
        "liquid, one of black liquid")
STAFF = "a long smooth wooden staff (a pole as tall as a man, held upright)"
CLOTH = "a strip of plain cloth"
BLADE = "a small sharp lancet (a tiny pointed blade, like a small leaf of metal, on a short handle)"
BOWL = "a round shallow metal bowl"
BANDAGE = "a white cloth bandage"
POLE = ("a barber pole (a short round pole fixed beside a shop door, painted with red and white stripes that spiral "
        "around it)")
STREET_OLD = ("an old town street in the sixteen hundreds: narrow houses with wooden beams on their fronts, a "
              "cobblestone road, a barber shop door with a small window")
BEDROOM_OLD = ("a plain bedroom in the sixteen hundreds: a wooden bed with a thick blanket, a small window, a candle "
               "on a stool")
# now
NURSE = ("a nurse (a stick-figure woman with her hair tied back, in plain scrubs and gloves)")
YOU = "a stick-figure young man (short spiky hair, plain T-shirt and jeans)"
CLINIC = ("a modern clinic blood test room: a padded chair with a wide armrest, a small trolley with neat supplies, a "
          "sink, white cupboards and a window with blinds")
BAND = "a stretchy flat rubber band (a tourniquet) tied around the upper arm"
WIPE = "a small square alcohol wipe"
NEEDLE = "a thin needle in a small plastic holder"
TUBES = "small narrow blood test tubes with coloured caps (no letters on them)"
COTTON = "a small round cotton ball"
PLASTER = "a small round sticking plaster"
LAB = ("a modern hospital lab: long white benches, a big boxy testing machine with a rack for tubes, a computer "
       "screen, bright ceiling lights")
LAB_WORKER = "a lab worker (a stick-figure woman in a white lab coat, gloves and safety glasses)"
DOC_NOW = "a modern doctor (a stick-figure man in a white coat with a stethoscope around his neck)"
# ---- the one coloured thing per picture (settings.json "colour_subject") ----
C_FEVER = "the man's face: flat feverish pink, with flat light blue sweat drops"
C_DOOR = "the barber shop's wooden door: flat warm brown"
C_BLADE = "the small blade: flat shiny silver grey"
C_DOCTOR = "the doctor's long robe: flat black, with a flat red collar"
C_JARS = "the four jars of liquid: one flat red, one flat light blue, one flat yellow and one flat black"
C_BLOODJAR = "the jar of blood: flat red, overflowing"
C_TAP = "the jar of blood and the drops coming out of its tap: flat red"
C_BARBER = "the barber's long apron: flat dark green"
C_RAZOR = "the shaving foam flat white and the cut hair flat brown"
C_STAFF = "the wooden staff: flat warm brown"
C_VEINS = "the swollen veins on the arm: flat blue"
C_CLOTH = "the strip of cloth: flat light tan"
C_BLOOD_LINE = "the thin line of blood on the arm: flat red"
C_BOWL = "the blood running into the bowl: flat dark red, and the bowl flat grey"
C_SICK_PALE = "the man's pale face: flat greenish grey"
C_BANDAGE = "the bandage: filled flat bright white, so it stands out from the off-white paper"
C_POLE = "the barber pole: flat red and flat bright white stripes"
C_POLE_SIDE = ("the barber pole's flat red and flat bright white stripes, the blood in the bowl flat dark red, and the "
               "rolled bandage flat bright white")
C_BLANKET = "the blanket on the bed: flat dull brown"
C_X = "the big X: flat bright red"
C_NURSE = "the nurse's scrubs: flat teal"
C_BAND = "the stretchy band: flat bright blue"
C_WIPE = "the alcohol wipe: flat white with a flat light blue edge"
C_NEEDLE = "the needle holder: flat light blue, the needle flat silver grey"
C_TUBES = "the blood in the tubes flat dark red, and the tube caps flat purple, flat green and flat yellow"
C_PLASTER = "the cotton ball flat bright white and the round plaster flat tan"
C_MACHINE = "the lab testing machine: flat light grey with a flat green light"
C_SCREEN = "the screen: flat dark blue, with a simple white bar chart where one bar is flat red"
C_SPLIT = ("on the left the blood in the barber's bowl flat dark red, and on the right the small tubes' caps flat "
           "purple, flat green and flat yellow")
CAPTIONS = ("The place fills the whole frame; keep the very top and very bottom of the frame calm (sky, wall or floor) "
            "for captions. Never write any name, label or caption under or beside anyone or anything.")

M = 33


def shot(n, text, what, place, must, never="", colour=""):
    what = re.sub(r"(^|\. )([a-z])", lambda m: m[1] + m[2].upper(), what)   # blocks start lowercase
    return n, text, " ".join(x for x in (
        f"This is picture {n} of {M} in one continuous picture story; draw exactly this moment.",
        what, f"Place: {place}.",
        f"The one coloured thing in this picture is {colour}; every other person, object and the whole place are black "
        "ink lines only, no colour.",
        f"It MUST show: {must}.", f"NEVER: {never}." if never else "", CAPTIONS) if x)


S = [
 shot(1, "Feeling sick in the sixteen hundreds?",
      f"{SICK} stands in the street hugging himself and shivering, his face hot with fever, sweat drops flying, wavy "
      "shiver lines around him.",
      STREET_OLD,
      "the man from the sixteen hundreds looking sick with a fever",
      "any modern thing, any blood",
      colour=C_FEVER),
 shot(2, "You went to the barber.",
      f"{SICK}, still shivering, pushes open the wooden door of the barber shop and steps inside; through the door "
      "you can see the heavy wooden chair.",
      STREET_OLD,
      "the sick man walking into the old barber shop",
      "any barber pole yet, any letters on the shop",
      colour=C_DOOR),
 shot(3, "And he cut into your arm.",
      f"{SICK} sits in the heavy wooden chair with one bare arm stretched out on the armrest; {BARBER} leans over "
      f"him holding {BLADE} just above the inside of the elbow; the man's eyes are wide.",
      SHOP,
      "the barber holding the small blade over the man's bare arm",
      "any blood yet, a big knife, a saw",
      colour=C_BLADE),
 shot(4, "Back then, doctors thought your body",
      f"{DOCTOR} stands beside {BODY_CHART} and points at it with a long thin stick, as if teaching.",
      STUDY,
      "the old doctor pointing at the drawing of a human body",
      "any letters or labels on the drawing",
      colour=C_DOCTOR),
 shot(5, "was full of four liquids.",
      f"Close view of {BODY_CHART}: drawn inside the body outline are {JARS}, standing in a row in the chest and "
      "belly.",
      STUDY + "; the sheet of paper fills most of the frame",
      "four jars of four different liquids inside the body drawing",
      "any letters or labels",
      colour=C_JARS),
 shot(6, "Too much blood, and you got sick.",
      f"Inside the body outline on the sheet, the jar of blood is overflowing, spilling over its rim, while the other "
      f"three jars stay level; beside the sheet, {SICK} holds his head, looking sick.",
      STUDY,
      "the overflowing blood jar next to the sick man",
      "any letters or labels",
      colour=C_BLOODJAR),
 shot(7, "So the cure was to let some out.",
      "Close view of the overflowing jar of blood drawn on the sheet: a small tap now sticks out of its side, open, "
      "and a few drops run out of it, so the level drops back down to the rim; a small arrow points down.",
      STUDY + "; the sheet of paper fills most of the frame",
      "some blood being let out of the too-full jar so it is no longer overflowing",
      "any letters",
      colour=C_TAP),
 shot(8, "The barber did the cutting,",
      f"{BARBER} stands in his shop holding up {BLADE} in one hand, ready, looking proud.",
      SHOP,
      "the barber holding the small blade, ready to cut",
      "a big knife, a sword, any blood",
      colour=C_BARBER),
 shot(9, "right next to the haircuts and shaves.",
      f"Wide view of the shop: in one chair a stick-figure customer with a soapy foamed chin gets a shave from {BARBER} "
      "with an open razor; next to him another stick-figure customer gets a haircut, cut hair falling to the floor; "
      "and in the corner the sick man waits in his chair with his sleeve rolled up.",
      SHOP + ", with a second plain wooden chair",
      "shaving and haircuts going on in the same shop where the bleeding is done",
      "any blood, any modern clippers",
      colour=C_RAZOR),
 shot(10, "You sat down and gripped a wooden pole.",
      f"{SICK} sits in the heavy wooden chair, his shirt sleeve rolled up, gripping {STAFF} tightly in his fist, the "
      "bottom of the staff resting on the floor.",
      SHOP,
      "the man sitting and gripping the tall wooden staff",
      "any blood yet",
      colour=C_STAFF),
 shot(11, "Squeezing it made the veins in your arm swell up.",
      "Close view of a bare stick-figure forearm and fist squeezing a smooth wooden staff, small squeeze lines "
      "around the fist, and the veins on the inside of the arm standing out as raised lines.",
      SHOP + "; the close view of the arm fills most of the frame",
      "the veins swelling up on the arm as the hand squeezes the staff",
      "any blood, any cut",
      colour=C_VEINS),
 shot(12, "He tied a strip of cloth tight around your upper arm.",
      f"{BARBER} pulls {CLOTH} tight around the bare upper arm of {SICK}, who sits in the heavy wooden chair still "
      f"gripping {STAFF}; small pull lines at the knot.",
      SHOP,
      "the barber tying the cloth tight around the upper arm",
      "any blood yet",
      colour=C_CLOTH),
 shot(13, "Then he took a small, sharp blade",
      f"{BARBER} picks {BLADE} up off the wooden shelf with two fingers, a tiny shine mark on its tip.",
      SHOP,
      "the barber picking up the small sharp blade",
      "a big knife, any blood",
      colour=C_BLADE),
 shot(14, "and cut into a vein.",
      f"Close view: the tip of {BLADE} touches the inside of a bare elbow above {CLOTH} tied around the upper arm, and "
      "a thin short red line appears on the skin.",
      SHOP + "; the close view of the arm fills most of the frame",
      "the blade touching the inside of the elbow and a thin red line",
      "a deep wound, gore, a big knife",
      colour=C_BLOOD_LINE),
 shot(15, "Your blood ran out into a metal bowl.",
      f"{SICK} sits in the heavy wooden chair gripping {STAFF}; a thin stream of blood runs from the inside of his "
      f"elbow down into {BOWL}, which {BARBER} holds under the arm.",
      SHOP,
      "the thin stream of blood running from the arm into the metal bowl",
      "gore, splashes everywhere",
      colour=C_BOWL),
 shot(16, "He let it run until he thought you'd lost enough.",
      f"{BOWL} under the arm is now almost full; {SICK} slumps in the chair, his face pale and dizzy, little swirl "
      f"lines above his head; {BARBER} peers into the bowl, thinking.",
      SHOP,
      "the man pale and dizzy as the bowl fills up",
      "gore",
      colour=C_SICK_PALE),
 shot(17, "Then he wrapped your arm in a white bandage.",
      f"{BARBER} wraps {BANDAGE} around the inside of the elbow of {SICK}, who sits weak in the heavy wooden chair.",
      SHOP,
      "the barber wrapping the arm in the white bandage",
      "any blood showing",
      colour=C_BANDAGE),
 shot(18, "That's probably why barber poles have red and white stripes.",
      f"{POLE} beside the wooden door of a barber shop on the old street.",
      STREET_OLD,
      "the red and white striped barber pole beside the shop door",
      "any letters or sign words",
      colour=C_POLE),
 shot(19, "The red for blood. The white for bandages.",
      f"{POLE} stands in the middle; on its left, {BOWL} of blood, with a small arrow from the bowl to a red stripe; on "
      f"its right, a rolled-up {BANDAGE}, with a small arrow from it to a white stripe.",
      STREET_OLD,
      "the red stripes matched to the bowl of blood and the white stripes matched to the bandage",
      "any letters",
      colour=C_POLE_SIDE),
 shot(20, "And it didn't cure much.",
      f"{SICK} lies in a wooden bed under a thick blanket, a white bandage on his arm, still shivering with fever, "
      "sweat drops on his face.",
      BEDROOM_OLD,
      "the man still sick in bed after the bleeding",
      "any doctor, any modern thing",
      colour=C_BLANKET),
 shot(21, "It often left people weaker.",
      f"{SICK} lies in the wooden bed, pale and weak, trying to lift his bandaged arm and barely managing, droopy "
      "eyes, a small sweat drop.",
      BEDROOM_OLD,
      "the man too weak to lift his arm",
      "any blood, any death imagery",
      colour=C_SICK_PALE),
 shot(22, "Today, nobody drains your blood to cure a cold.",
      f"{BOWL} and {BLADE} lie side by side on plain ground, and one big hand-drawn X is drawn across both of them.",
      "a plain flat white background with a simple floor line, nothing else",
      "the barber's bowl and blade crossed out",
      "any people, any letters",
      colour=C_X),
 shot(23, "But a nurse still takes a little, to test it.",
      f"{NURSE} smiles and waves {YOU} toward the padded chair as he walks in.",
      CLINIC,
      "the nurse welcoming the young man into the clinic blood test room",
      "any blade, any bowl",
      colour=C_NURSE),
 shot(24, "She ties a stretchy band around your arm.",
      f"{YOU} sits in the padded chair with his arm on the wide armrest; {NURSE} ties {BAND} around his upper arm.",
      CLINIC,
      "the nurse tying the stretchy band around the upper arm",
      "any cloth strip, any blade",
      colour=C_BAND),
 shot(25, "She wipes the spot clean.",
      f"{NURSE} wipes the inside of the young man's elbow with {WIPE}; the stretchy band is still on his upper arm.",
      CLINIC,
      "the nurse wiping the inside of the elbow clean",
      "any needle yet",
      colour=C_WIPE),
 shot(26, "A thin needle slips into the vein.",
      f"Close view: {NEEDLE} slides gently into the inside of the elbow at a shallow angle, held by a gloved hand; at "
      "the edge of the frame the young man's face looks away, calm.",
      CLINIC + "; the close view of the arm fills most of the frame",
      "the thin needle going gently into the vein",
      "any blood running down the arm, any big knife",
      colour=C_NEEDLE),
 shot(27, "A few small tubes fill up.",
      f"Close view: one of the {TUBES} is pushed onto the needle holder and fills with blood; two more filled tubes "
      "stand in a small rack beside it.",
      CLINIC + "; the close view fills most of the frame",
      "the small tubes filling with blood",
      "a bowl, any letters on the tubes",
      colour=C_TUBES),
 shot(28, "Off comes the band, and out comes the needle.",
      f"{NURSE} pulls the needle out of the young man's arm with one hand; the stretchy band hangs loose and open "
      "on his upper arm; small arrows show the needle coming out and the band coming off.",
      CLINIC,
      "the needle coming out and the band coming off",
      "any blood running",
      colour=C_BAND),
 shot(29, "A cotton ball, a little pressure, and a bandage.",
      f"{YOU} presses {COTTON} on the inside of his elbow with two fingers, and {NURSE} sticks {PLASTER} on it; he "
      "smiles.",
      CLINIC,
      "the cotton ball pressed on the arm and the small plaster going on",
      "a big bandage wrap, any blood",
      colour=C_PLASTER),
 shot(30, "Then a lab checks your blood",
      f"{LAB_WORKER} slides a rack of the {TUBES} into the big boxy testing machine.",
      LAB,
      "the filled tubes going into the lab testing machine",
      "any letters on the machine or tubes",
      colour=C_MACHINE),
 shot(31, "for what's really wrong.",
      f"{DOC_NOW} points at a computer screen showing a simple bar chart, one bar standing out; {YOU} sits beside "
      "him and nods, understanding.",
      "a modern doctor's office: a desk with a computer screen, two chairs, a window with blinds, a plant",
      "the doctor showing the young man what the blood test found",
      "any letters or numbers on the screen",
      colour=C_SCREEN),
 shot(32, "Back then, a blade and a bowl at the barber.",
      f"{BARBER} holds {BLADE} in one hand and {BOWL} of blood in the other; {SICK} slumps pale in the heavy wooden "
      "chair, his arm wrapped in a bandage.",
      SHOP,
      "the barber with his blade and the bowl of blood beside the pale man",
      "gore, any modern thing",
      colour=C_BOWL),
 shot(33, "Now? A tiny needle, and a few small tubes.",
      f"{NURSE} holds up three of the {TUBES}; {YOU} sits in the padded chair with a small plaster on his arm and "
      "gives a thumbs up.",
      CLINIC,
      "the nurse holding up the few small tubes and the happy young man",
      "any bowl, any blade",
      colour=C_TUBES),
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
