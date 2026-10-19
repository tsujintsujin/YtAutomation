"""Image prompts for tooth-key-then-now, written as one story (channels/SHORTS_RULES.md "How image prompts are
written", copied from found-rich/videos/nail-sandwich-nugget-declaration/scenes.py). Writes scene + full prompt for
every line into script.json.
usage: python channels/what-happens-now/videos/tooth-key-then-now/scenes.py"""
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent                 # videos/<slug>
ROOT = HERE.parents[3]                                 # YtAutomation
sys.path.insert(0, str(ROOT))
from dashboard import short_prompt                     # the fixed frame around every Short prompt

SETTINGS = json.loads((HERE.parents[1] / "settings.json").read_text(encoding="utf-8"))
STYLE = SETTINGS["image_style"]

# ---- the same words every time a person, object or place appears ----
# back then (the seventeen hundreds)
PULLER = ("a travelling tooth-puller from the seventeen hundreds (a tall thin stick-figure man in a big three-cornered "
          "hat and a long coat that reaches his knees, with a row of big round buttons down the front)")
PATIENT = ("a stick-figure man (plain loose shirt with the sleeves rolled up, simple baggy trousers, one cheek "
           "puffed out and swollen from a toothache)")
CROWD = ("a crowd of plain stick figures in simple old-fashioned clothes (some men in three-cornered hats, some women "
         "in bonnets and long skirts)")
KEY = ("a tooth key (a long straight metal rod about as long as a hand, with a short wooden bar fixed crosswise at one "
       "end as the handle so together they make a T shape, and a small curved metal claw at the other end; the whole "
       "tool looks like a big old door key, never like pliers, a wrench, a screwdriver or a hammer)")
DOOR_KEY = "a big old-fashioned iron door key with a round loop handle and a flat toothed bit at the end"
TOOLBOX = "a small wooden box with a rope carry handle"
STOOL = "a plain three-legged wooden stool"
SQUARE = ("a busy old town market square in the seventeen hundreds: round cobblestones on the ground, wooden market "
          "stalls with striped cloth awnings and baskets of apples and loaves of bread (black ink lines only, no colour), "
          "a round stone well in the middle, and a row of narrow old houses with pointed roofs and small square windows "
          "behind")
ROAD = ("a dirt country road winding between low rolling hills, a wooden fence along one side, a few trees, a small "
        "village of houses with pointed roofs far behind and another small village far ahead")
MOUTH_THEN = ("A close view straight into a wide-open mouth: the lips as a simple outline around the edge of the frame, "
              "an upper and a lower row of simple rounded teeth, the tongue, and one big back tooth with a dark scribbled "
              "patch on it showing it is rotten")
DOOR = ("the heavy wooden front door of an old house in the seventeen hundreds, with iron hinges, an iron door handle and "
        "a big old keyhole lock, set in a stone wall")
# eighteen forty-four
WELLS = ("a dentist from the eighteen forties (a stick-figure man with neat short side-parted hair, a bow tie and a "
         "short buttoned waistcoat over a shirt)")
FRIEND = ("his friend, a second dentist from the eighteen forties (a stick-figure man with a small curled mustache and "
          "a long coat)")
GAS_BAG = ("a soft round cloth bag of laughing gas (about the size of a football, with a short wooden tube coming out "
           "of it as a mouthpiece)")
OLD_PLIERS = "a pair of old metal tooth pliers with long straight handles and short curved tips"
ROOM1844 = ("a small dentist room in the eighteen forties: wooden floorboards, a tall window with curtains tied back, a "
            "high-backed wooden chair with armrests in the middle, a small side table with a candle and a few metal tools")
# now
DENTIST = ("a modern dentist (a stick-figure man in a round cloth cap, a face mask over his mouth and nose, a "
           "short-sleeved work top and gloves)")
YOU = ("a stick-figure young man (short spiky hair, plain T-shirt and jeans)")
XRAY = ("a dental X-ray picture on a flat screen on the wall (a simple outline drawing of one big back tooth with two "
        "long roots going down into the jawbone)")
SYRINGE = "a small dental syringe with a thin short needle"
GAUZE = "a small folded square of gauze cloth (a soft little pad drawn with a few thin crossing lines)"
ELEVATOR = ("a thin straight metal dental tool (like a small narrow chisel: a thick round handle and a long thin shaft "
            "ending in a narrow flat tip)")
FORCEPS = ("dental forceps (metal pliers with two long curved handles and short curved tips that close around a tooth)")
TOOTH = "one whole big back tooth with two long roots"
OFFICE = ("a modern dentist office: a long reclining dental chair in the middle, a round lamp on a bent arm above the "
          "chair, a small tray of tools on a stand beside it, a flat screen on the wall, cupboards and a small sink "
          "along the back wall, a window with blinds")
MOUTH_NOW = ("A close view straight into a wide-open mouth: the lips as a simple outline around the edge of the frame, "
             "an upper and a lower row of simple rounded teeth, the tongue, and one big back tooth with a dark scribbled "
             "patch on it showing it is rotten; the round dental lamp shape in one top corner")
MOUTH_GAP = ("A close view straight into a wide-open mouth: the lips as a simple outline around the edge of the frame, "
             "an upper and a lower row of simple rounded teeth, the tongue, and an empty gap in the back where one big "
             "back tooth used to be; the round dental lamp shape in one top corner")
STREET = ("a quiet modern street: a small dentist office building with a glass front door and a big window, a "
          "sidewalk, a parked car, a tree, and a row of small houses further down the street")
# ---- the one coloured thing per picture (settings.json "colour_subject"; Justin 2026-10-19: colour the main object of
# each scene, everything else black ink) ----
C_KEY = "the tooth key: its long rod and small claw flat steel grey, its wooden bar handle flat warm brown"
C_DOOR_KEY = "the old door key: flat dark iron grey"
C_KEYS = ("the two keys: the tooth key with its long rod and small claw flat steel grey and its wooden bar handle flat "
          "warm brown, and the old door key flat dark iron grey")
C_CHEEK = "the man's swollen cheek: flat soft pink"
C_X = "the big hand-drawn X: flat bright red"
C_PULLER = "the tooth-puller's clothes: his three-cornered hat flat black, his long coat flat dark blue with flat gold buttons"
C_AWNINGS = "the cloth awnings over the market stalls: flat red and white stripes"
C_CROWD = ("the clothes of the people in the crowd: each person's clothes in one flat plain colour (red, blue, green, "
           "yellow or brown)")
C_STOOL = "the three-legged wooden stool: flat warm brown"
C_BOX = "the small wooden box: flat warm brown"
C_BAD_TOOTH = "the rotten back tooth: flat creamy yellow, with the rotten patch flat dark brown"
C_CLAW_TOOTH = ("the claw and the rotten back tooth: the claw flat steel grey; the tooth flat creamy yellow, with the "
                "rotten patch flat dark brown")
C_TOOTH = "the pulled-out tooth with its two roots: flat creamy yellow, with a rotten patch flat dark brown"
C_CRACK = "the zigzag crack line across the jaw: flat bright orange, like a small lightning bolt"
C_CALENDAR = "the wall calendar: its page flat cream, the numbers 1844 flat red"
C_WELLS = "the 1840s dentist's clothes: his bow tie flat dark red, his waistcoat flat brown"
C_GAS = "the cloth bag of laughing gas: flat pale blue, its wooden tube flat brown"
C_PLIERS = "the old tooth pliers: flat steel grey"
C_PIN = "the tiny sewing pin: flat silver grey with a small round flat red head"
C_DENTIST = "the modern dentist's clothes: his cap, face mask and work top flat light blue, his gloves flat white"
C_XRAY = "the X-ray screen: flat dark navy blue, with the tooth and its two roots drawn on it in flat white"
C_SYRINGE = "the dental syringe: its body flat pale blue, its needle flat silver grey"
C_GAUZE = "the gauze pad: filled flat bright white, so it stands out clearly from the off-white paper"
C_ELEVATOR = "the thin dental tool: its shaft and tip flat silver grey, its handle flat blue"
C_FORCEPS = "the forceps: flat silver grey"
C_YOU = "the young man's clothes: his T-shirt flat green, his jeans flat blue"
C_SPLIT = ("the dental syringe on the left (its body flat pale blue, its needle flat silver grey) and the young man's "
           "clothes on the right (his T-shirt flat green, his jeans flat blue)")
CAPTIONS = ("The place fills the whole frame; keep the very top and very bottom of the frame calm (sky, wall or floor) "
            "for captions. Never write any name, label or caption under or beside anyone or anything.")

M = 43


def shot(n, text, what, place, must, never="", colour=""):
    what = re.sub(r"(^|\. )([a-z])", lambda m: m[1] + m[2].upper(), what)   # blocks start lowercase
    return n, text, " ".join(x for x in (
        f"This is picture {n} of {M} in one continuous picture story; draw exactly this moment.",
        what, f"Place: {place}.",
        f"The one coloured thing in this picture is {colour}; every other person, object and the whole place are black "
        "ink lines only, no colour.",
        f"It MUST show: {must}.", f"NEVER: {never}." if never else "", CAPTIONS) if x)


S = [
 shot(1, "In the seventeen hundreds, a toothache meant",
      f"{PATIENT}. He stands in the market square holding his swollen cheek with one hand, his face twisted in pain, "
      "eyebrows tilted up, mouth turned down. Small pain lines around his cheek. Shown from head to feet.",
      SQUARE,
      "the man with the swollen cheek in pain, in the old market square",
      "any tool, any dentist, any modern thing",
      colour=C_CHEEK),
 shot(2, "a stranger shoving a metal key in your mouth.",
      f"{PULLER} stands over {PATIENT}, who sits on {STOOL}. The tooth-puller pushes {KEY} into the patient's open "
      "mouth, claw end first, his other hand holding the patient's head still. The patient's eyes are wide with fear.",
      SQUARE,
      "the tooth-puller pushing the T-shaped tooth key into the scared patient's mouth",
      "pliers, a wrench, a modern dentist, any crowd yet",
      colour=C_KEY),
 shot(3, "And then he turned it.",
      f"{PULLER} grips the wooden bar handle of {KEY} with both hands and twists it hard; a big curved arrow around "
      f"the handle shows it turning. The claw end is inside the mouth of {PATIENT}, who sits on {STOOL}, gripping the "
      "stool's edge with both hands, eyes squeezed shut.",
      SQUARE,
      "the tooth key being twisted in the patient's mouth, the curved turning arrow, the patient's pain",
      "pliers, a wrench, any blood",
      colour=C_KEY),
 shot(4, "There were no dentists like we have now.",
      "In the middle of the old market square stands a modern dentist's chair (a long reclining dental chair with a "
      "round lamp on a bent arm), drawn only in thin dotted lines like a ghost of something that does not exist yet, "
      "with one big hand-drawn X crossed over it. Stick figures in old-fashioned clothes walk past without looking.",
      SQUARE,
      "the dotted modern dental chair crossed out with a big X, in the old square",
      "a solid real dental chair, any dentist, any modern person",
      colour=C_X),
 shot(5, "Tooth-pullers went from town to town instead.",
      f"{PULLER} walks along the road with long strides, carrying {TOOLBOX}, a walking stick in "
      "his other hand. Small dust puffs behind his feet.",
      ROAD,
      "the tooth-puller on the road between two villages, carrying his small wooden box",
      "a horse, a carriage, a car",
      colour=C_PULLER),
 shot(6, "They picked market days,",
      f"{PULLER} arrives at the edge of the market square and sets {TOOLBOX} down on {STOOL}, looking around at the "
      "busy stalls. A few shoppers with baskets walk by.",
      SQUARE,
      "the tooth-puller arriving at the market and setting down his box, the market stalls busy",
      "any patient yet",
      colour=C_AWNINGS),
 shot(7, "when the square was full of people.",
      f"Wide view of the whole square packed with many stick figures: shoppers with baskets, sellers behind the "
      f"stalls, children running. In the middle, {PULLER} stands beside {STOOL} with {TOOLBOX} on it, waving his hat "
      "to call people over.",
      SQUARE,
      "the square crowded with people, and the tooth-puller in the middle calling them",
      "an empty square",
      colour=C_CROWD),
 shot(8, "So you sat down right there,",
      f"{PATIENT} sits down on {STOOL} in the middle of the square, still holding his swollen cheek, looking nervous. "
      f"{PULLER} stands beside him, rolling up his coat sleeves. {TOOLBOX} sits open on the cobblestones.",
      SQUARE,
      "the patient sitting down on the stool out in the open square, the tooth-puller beside him",
      "a room, a chair with a back, any modern thing",
      colour=C_STOOL),
 shot(9, "in front of everyone.",
      f"{CROWD} gathers in a tight half circle around {PATIENT}, who sits on {STOOL} in the middle; people lean in to "
      f"look. The patient looks around at them, nervous. {PULLER} stands beside him.",
      SQUARE,
      "the crowd gathered close around the patient on the stool",
      "any modern thing",
      colour=C_CROWD),
 shot(10, "Nothing to numb it. Nothing at all.",
      f"{PULLER} faces the viewer and shows both hands open and empty, palms up, with a small shrug. Beside him "
      f"{PATIENT} sits on {STOOL} holding his swollen cheek, his eyes wide and worried. {TOOLBOX} lies open on the "
      "cobblestones with nothing in it but the tooth key.",
      SQUARE,
      "the tooth-puller's empty open hands and the worried patient: no medicine of any kind",
      "any bottle, cup, pill, needle, cloth or medicine",
      colour=C_BOX),
 shot(11, "His tool looked like a big old door key.",
      f"Close view of {TOOLBOX}, its lid open, on the cobblestones beside {STOOL}. On the left lies {KEY}, and on the right, the same "
      f"size, lies {DOOR_KEY}. They are drawn big and side by side so you can see they look alike. A small "
      "\"=\" sign between them.",
      f"{SQUARE}; only the cobblestones and the bottom of a market stall show around the box",
      "the tooth key and the door key side by side, looking alike",
      "pliers, a wrench, a modern key",
      colour=C_KEYS),
 shot(12, "He slid it into your mouth sideways.",
      f"{PULLER} bends over {PATIENT}, who sits on {STOOL} with his mouth wide open, and slides {KEY} into the mouth "
      "sideways: the long rod lies level across the mouth, the wooden bar handle sticking out from the corner of the "
      "lips. A small arrow shows it sliding in.",
      SQUARE,
      "the tooth key going sideways (level) into the patient's open mouth",
      "the key going in straight from the front, pliers",
      colour=C_KEY),
 shot(13, "A little metal claw on the end",
      f"{MOUTH_THEN}. The claw end of {KEY} comes in from one side, the long rod lying level across the mouth; the "
      "small curved metal claw is drawn big and clear, close to the rotten back tooth.",
      "inside the patient's mouth; the close view fills the whole frame",
      "the small curved claw at the end of the rod, right next to the rotten tooth",
      "pliers, a drill, any blood",
      colour=C_KEY),
 shot(14, "hooked around your bad tooth.",
      f"{MOUTH_THEN}. The small curved metal claw at the end of {KEY} is now hooked tightly around the rotten back "
      "tooth, gripping it.",
      "inside the patient's mouth; the close view fills the whole frame",
      "the claw wrapped around the rotten back tooth",
      "pliers, a drill, any blood",
      colour=C_CLAW_TOOTH),
 shot(15, "Then he turned the handle,",
      f"{PULLER} leans in and turns the wooden bar handle of {KEY} with both hands, a big curved arrow around the "
      f"handle; the rod sticks out from the mouth of {PATIENT}, who sits on {STOOL} gripping its edge.",
      SQUARE,
      "the tooth-puller's hands turning the T-shaped handle, the curved arrow",
      "pliers, a wrench, any blood",
      colour=C_KEY),
 shot(16, "the way you'd open a lock.",
      f"{DOOR}. A stick-figure hand turns {DOOR_KEY} in the keyhole, a curved arrow around the key showing it turning.",
      "a quiet corner of the old town in the seventeen hundreds, cobblestones under the door",
      "the hand turning the old key in the door lock",
      "the tooth key, a mouth, any modern lock",
      colour=C_DOOR_KEY),
 shot(17, "Your tooth twisted and twisted",
      f"{MOUTH_THEN}. The small curved metal claw at the end of {KEY} grips the rotten back tooth, and the tooth is "
      "tilted over sideways, with two curved arrows around it showing it twisting.",
      "inside the patient's mouth; the close view fills the whole frame",
      "the rotten tooth tilting and twisting in the claw",
      "pliers, any blood",
      colour=C_BAD_TOOTH),
 shot(18, "until it came loose.",
      f"{PULLER} holds {KEY} up high, with {TOOTH} caught in its claw. {PATIENT} sits on {STOOL} "
      "holding his jaw.",
      SQUARE,
      "the pulled-out tooth with its roots held up in the claw of the tooth key",
      "pliers, any blood",
      colour=C_TOOTH),
 shot(19, "Or it snapped. That happened a lot.",
      f"{MOUTH_THEN}. The small curved metal claw at the end of {KEY} grips the rotten back tooth, and the tooth breaks "
      "in two with a jagged crack: the top half flies off with small burst lines, the bottom half stays stuck in "
      "the gum.",
      "inside the patient's mouth; the close view fills the whole frame",
      "the tooth snapping in two in the claw, half left in the gum",
      "any red, any blood",
      colour=C_BAD_TOOTH),
 shot(20, "Sometimes your jaw cracked along with it.",
      f"{PATIENT} sits on {STOOL} holding his jaw with both hands, a zigzag crack line drawn across his jaw, his mouth "
      f"open in a yell. {PULLER} stands beside him holding {KEY}.",
      SQUARE,
      "the patient's cracked jaw (zigzag line) and his yell",
      "any red, any blood",
      colour=C_CRACK),
 shot(21, "And the whole crowd?",
      f"Wide view from behind {PULLER} and the stool: {CROWD} stands packed in a half circle, every head turned "
      "toward us.",
      SQUARE,
      "the big crowd in a half circle, all turned toward the tooth-puller",
      "an empty square",
      colour=C_CROWD),
 shot(22, "They watched the entire thing.",
      f"{CROWD} watches with wide eyes and open mouths. In the middle {PULLER} works {KEY} in the mouth of {PATIENT}, who sits on {STOOL}.",
      SQUARE,
      "the crowd's shocked faces watching the tooth being pulled",
      "any modern thing",
      colour=C_CROWD),
 shot(23, "Then came eighteen forty-four.",
      f"A wall calendar hangs on the wall of the room, its page showing big numbers \"1844\". Morning light comes "
      "through the window. Nobody is in the room yet.",
      ROOM1844,
      "the calendar showing 1844 in the old dentist room",
      "any person, any other numbers or words",
      colour=C_CALENDAR),
 shot(24, "A dentist named Horace Wells",
      f"{WELLS} stands beside the high-backed wooden chair with his hands on his hips, facing the viewer, "
      "shown from head to feet.",
      ROOM1844,
      "the 1840s dentist with his bow tie and waistcoat, in his dentist room",
      "any real person's face or likeness, a modern dentist",
      colour=C_WELLS),
 shot(25, "breathed in laughing gas,",
      f"{WELLS} sits in the high-backed wooden chair holding {GAS_BAG} in his lap and breathing through its wooden "
      "tube; a few small curly lines float up from the bag. His eyes are half closed and he smiles a calm "
      "smile.",
      ROOM1844,
      "the dentist breathing from the bag of laughing gas and starting to smile",
      "a gas mask, a modern machine, any real person's face",
      colour=C_GAS),
 shot(26, "and a friend pulled one of his teeth.",
      f"{WELLS} sits asleep in the high-backed wooden chair, head tipped back, mouth open, {GAS_BAG} in his lap. "
      f"{FRIEND} leans over him and pulls a tooth out of his mouth with {OLD_PLIERS}; a small pop of motion lines.",
      ROOM1844,
      "the friend pulling a tooth from the sleeping dentist with the old pliers",
      "the tooth key, any pain on the sleeping man's face, any real person's face",
      colour=C_PLIERS),
 shot(27, "Afterward, he said",
      f"{WELLS} sits up awake in the high-backed wooden chair, pointing at his own cheek and talking excitedly with "
      f"a big smile. {FRIEND} stands beside him holding up {OLD_PLIERS} with {TOOTH} in the tips.",
      ROOM1844,
      "the awake, smiling dentist talking, his friend holding up the pulled tooth",
      "a speech bubble with words, any pain",
      colour=C_WELLS),
 shot(28, "it hurt less than a pin prick.",
      f"Closer view: {WELLS} sits in the high-backed wooden chair, smiling and relaxed, holding up one tiny sewing "
      "pin between his thumb and finger and giving a thumbs up with his other hand.",
      ROOM1844,
      "the happy dentist holding up a tiny sewing pin, no pain at all",
      "any blood, any pain, a speech bubble with words",
      colour=C_PIN),
 shot(29, "Today it's a whole different story.",
      f"{DENTIST} stands in the bright clean office and waves hello toward {YOU}, who walks in through the door "
      "smiling. The round lamp shines with a few short light lines.",
      OFFICE,
      "the modern dentist welcoming the young man into the clean modern office",
      "any crowd, any market, any old-fashioned thing",
      colour=C_DENTIST),
 shot(30, "The dentist takes an X-ray first,",
      f"{YOU} sits in the dental chair. {DENTIST} stands beside him and points up at {XRAY}; both look at it.",
      OFFICE,
      "the dentist and the patient looking at the tooth X-ray on the wall screen",
      "any blood, any tool in the mouth yet",
      colour=C_XRAY),
 shot(31, "to see the roots.",
      f"Close view of {XRAY}. A gloved finger points at the two long roots of the tooth on the screen.",
      f"{OFFICE}; only the screen on the wall and the edge of the window blinds show",
      "the tooth's two long roots on the X-ray, with the gloved finger pointing at them",
      "letters or numbers on the screen",
      colour=C_XRAY),
 shot(32, "One small shot numbs the whole area.",
      f"{YOU} lies back in the dental chair with his mouth open, calm. {DENTIST} gently gives him a shot in the gum "
      f"with {SYRINGE}. A soft little wavy line around the young man's cheek shows it going numb.",
      OFFICE,
      "the small shot into the gum and the patient staying calm",
      "a big scary needle, any blood, any pain face",
      colour=C_SYRINGE),
 shot(33, "Gauze goes in behind the tooth,",
      f"{MOUTH_NOW}. A gloved hand places {GAUZE} in the mouth just behind the rotten back tooth.",
      "inside the patient's mouth at the modern dentist; the close view fills the whole frame",
      "the gloved hand putting the gauze in behind the rotten tooth",
      "any blood, the tooth key",
      colour=C_GAUZE),
 shot(34, "so it can't slip down your throat.",
      f"{MOUTH_NOW}. {GAUZE} sits behind the rotten back tooth like a little wall at the back of the mouth. A small "
      "dotted arrow goes from the tooth toward the throat and stops at the gauze, with a short stop bar across it.",
      "inside the patient's mouth at the modern dentist; the close view fills the whole frame",
      "the gauze blocking the way to the throat, the dotted arrow stopped by it",
      "any blood",
      colour=C_GAUZE),
 shot(35, "A thin tool slides in beside the tooth",
      f"{MOUTH_NOW}. {GAUZE} sits behind the rotten back tooth. {ELEVATOR} slides in, its narrow flat tip pressing "
      "down right beside the rotten back tooth; a gloved hand holds the handle at the edge of the frame.",
      "inside the patient's mouth at the modern dentist; the close view fills the whole frame",
      "the thin flat-tipped tool going in right next to the rotten tooth",
      "pliers yet, the tooth key, any blood",
      colour=C_ELEVATOR),
 shot(36, "and wiggles it loose.",
      f"{MOUTH_NOW}. {GAUZE} sits behind the rotten back tooth. {ELEVATOR} presses beside the rotten back tooth, which "
      "now leans a little, with small back-and-forth wiggle lines on both sides of it.",
      "inside the patient's mouth at the modern dentist; the close view fills the whole frame",
      "the rotten tooth wiggling loose next to the thin tool",
      "any blood, the tooth key",
      colour=C_BAD_TOOTH),
 shot(37, "Then pliers called forceps rock it side to side",
      f"{MOUTH_NOW}. {GAUZE} sits behind the rotten back tooth. {FORCEPS} grip the rotten back tooth; two small curved "
      "arrows, one to the left and one to the right, show it rocking side to side.",
      "inside the patient's mouth at the modern dentist; the close view fills the whole frame",
      "the forceps gripping the tooth and the left-right rocking arrows",
      "the tooth key, any blood",
      colour=C_FORCEPS),
 shot(38, "and pull it straight out.",
      f"{DENTIST} holds up {FORCEPS} with {TOOTH} in the tips, a small straight arrow pointing up. {YOU} lies in the "
      "dental chair, calm and relaxed, eyes open.",
      OFFICE,
      "the whole tooth held up in the forceps, and the calm patient",
      "any pain face, any blood, the tooth key",
      colour=C_TOOTH),
 shot(39, "You bite down on gauze",
      f"{YOU} sits up in the dental chair biting down on {GAUZE}, one cheek a little round, giving a thumbs up. "
      f"{DENTIST} stands beside him nodding.",
      OFFICE,
      "the young man biting down on the gauze pad and giving a thumbs up",
      "any blood, any pain face",
      colour=C_GAUZE),
 shot(40, "to stop the bleeding.",
      f"{MOUTH_GAP}. {GAUZE} is pressed down firmly into the gap by the teeth above it.",
      "inside the patient's mouth at the modern dentist; the close view fills the whole frame",
      "the gauze pressed into the empty gap where the tooth was",
      "any red, any blood, any blood drops",
      colour=C_GAUZE),
 shot(41, "And you go home that same day.",
      f"{YOU} walks out of the glass front door of the dentist office onto the sidewalk, smiling and waving back, "
      f"{GAUZE} still in his cheek, heading toward the houses down the street. A bright sun in the sky.",
      STREET,
      "the young man walking out of the dentist office and heading home, happy",
      "a hospital bed, an ambulance",
      colour=C_YOU),
 shot(42, "Back then, a key, a crowd, and no numbing.",
      f"{PULLER} turns {KEY} in the mouth of {PATIENT}, who sits on {STOOL} with his eyes squeezed shut; {CROWD} "
      "stands in a half circle around them, staring.",
      SQUARE,
      "the tooth key, the crowd and the patient in pain, all in one picture",
      "any modern thing",
      colour=C_KEY),
 shot(43, "Now? One shot. Then home.",
      f"The picture is split down the middle by a simple vertical line. Left half: in the modern dentist office, "
      f"{DENTIST} gives {YOU} one small shot in the gum with {SYRINGE} while the young man lies calm in the dental "
      f"chair. Right half: on a quiet modern street, the same {YOU[2:]} walks home waving, {GAUZE} in his "
      "cheek.",
      f"left half: {OFFICE}; right half: {STREET}",
      "the one shot on the left and the young man walking home on the right",
      "the tooth key, any crowd, any blood",
      colour=C_SPLIT),
]

p = HERE / "script.json"
data = json.load(open(p, encoding="utf-8"))
segs = data["segments"]
assert len(segs) == len(S) == M
for seg, (n, text, scene) in zip(segs, S):
    assert seg["id"] == n and seg["text"] == text, (n, seg["text"], text)
    seg["scene"] = scene
    seg["prompt"] = short_prompt(scene, STYLE, SETTINGS["colour_subject"], "paper_ref" in SETTINGS)
json.dump(data, open(p, "w", encoding="utf-8"), indent=1, ensure_ascii=False)
print("written", len(segs), "longest", max(len(s["prompt"]) for s in segs), "shortest", min(len(s["prompt"]) for s in segs))
