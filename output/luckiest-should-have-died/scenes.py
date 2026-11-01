"""Picture plan + full prompts for LuckySticks long video 1, "The Luckiest People Who Should Have Died".
Written as one story per person (channels/SHORTS_RULES.md "How image prompts are written": draw only what the line
says, every person/object/place written out in full in every prompt). 16:9, 1920x1080, stick figures like the Shorts.
Segments come from segs.py (script.md -> segments.json). Writes script.json for the "YouTube Render" workflow.
usage: python output/luckiest-should-have-died/scenes.py"""
import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
STYLE = json.loads((ROOT / "channels/found-rich/settings.json").read_text(encoding="utf-8"))["image_style"]
STYLE = STYLE.replace(" Vertical 9:16, subject centred with room above and below for captions.",
                      " Wide 16:9 landscape, the scene spread across the whole width.")
assert "9:16" not in STYLE
SEGS = json.loads((HERE / "segments.json").read_text(encoding="utf-8"))
TOTAL = len(SEGS)
NO_GORE = "blood, open wounds, injuries drawn in detail, dead bodies, skulls"
NO_TEXT = "any words, letters or numbers"


def prompt(scene):
    return ("Generate one image. 16:9 wide landscape, 1920x1080, full-bleed: the drawing fills the whole wide canvas edge "
            "to edge, like one full-screen frame of a YouTube video. Match the drawing style of the attached image "
            "exactly: the same simple stick figures, the same even black ink line, the same plain warm off-white paper "
            "(the attached image is tall; this picture is wide, so spread the scene across the width). "
            f"Scene: {scene} Style: {STYLE} "
            "Avoid: colour, shading, gradients, 3D, photographic detail, any words or letters (only the simple symbols "
            "the scene asks for), any real person's face or likeness, any game, film or cartoon character, any logo, "
            "watermark or frame.")


P = []


def shot(what, place, must, never=""):
    n = len(P) + 1
    P.append(" ".join(x for x in (
        f"This is picture {n} of {TOTAL} in one continuous picture story; draw exactly this moment.",
        what, f"Place: {place}.", f"It MUST show: {must}.",
        f"NEVER: {never}." if never else "",
        "Never write any name, label or caption under or beside anyone or anything.") if x))


# ===================================================================== 1. Vesna Vulović (1-15)
VESNA = ("a stick-figure young woman with short dark hair under a small flight attendant's cap, wearing a neat "
         "flight attendant's uniform: a fitted jacket with a skirt and a small scarf at the neck")
JET = "a 1970s passenger jet airliner with two engines at the back of its body and a tall tail fin"
TAIL = "the tail section of a passenger jet: the back end of the body with the tall tail fin, torn open at the front"
CART = "a tall narrow metal airline food cart on small wheels, with little drawers"
CABIN_TAIL = "inside the very back of a passenger jet: a narrow aisle, the last rows of seats, a small galley wall"
SKY = "high in the sky above a thick layer of white clouds"
SNOWY = "a snowy forest on a slope: tall pine trees heavy with snow, deep snow everywhere"
HOSP = "a plain hospital room: a metal hospital bed, a window, a small bedside table"

shot(f"{VESNA} stands at the bottom of the boarding stairs of {JET}, smiling, holding a small travel bag.",
     "an airport on a cold winter day: the runway, a little snow at the edges, the boarding stairs up to the plane door",
     "the flight attendant in her uniform at the plane", NO_TEXT)
shot(f"{VESNA} walks up the boarding stairs into {JET}, not knowing anything is wrong.",
     "an airport on a cold winter day, the plane parked on the runway",
     "the flight attendant boarding the plane", NO_TEXT)
shot("At an airline desk, a stick-figure man in a shirt and tie holds a clipboard with two small photos of two different "
     "smiling flight attendants side by side, and points at the wrong one by mistake. A big question mark floats over "
     "his head.", "an airline office: a desk, a wall clock, a filing cabinet",
     "the man pointing at one of the two flight attendant photos on the clipboard", NO_TEXT)
shot(f"Far view: {JET} flies {SKY}. A big burst of flame and smoke bursts out of the middle of its body.",
     SKY, "the plane exploding high above the clouds", f"{NO_GORE}, {NO_TEXT}")
shot(f"Very far view: {JET} breaks into three separate pieces high in the sky, the pieces drifting apart. Far below, "
     "poking up through the clouds, the pointed snowy peak of a tall mountain, much lower than the pieces of the plane.",
     SKY, "the plane in three pieces, far higher than the mountain peak below", f"any person, {NO_TEXT}")
shot("The three pieces of the plane fall through the clouds, small bits of debris tumbling around them.",
     "falling through thick white clouds", "the three pieces falling", f"any person, {NO_GORE}, {NO_TEXT}")
shot(f"Close view of {TAIL} falling through the sky. Through the torn front of it, {VESNA} can be seen inside, small, "
     "holding on.", SKY, "the tail section falling with the flight attendant inside it", f"{NO_GORE}, {NO_TEXT}")
shot(f"{CABIN_TAIL}, tilted. {VESNA} is pressed against the galley wall by {CART} that has rolled into her and pins her "
     "there, her eyes shut tight.", CABIN_TAIL, "the food cart pinning her against the wall inside the tail",
     f"{NO_GORE}, {NO_TEXT}")
shot(f"Far view: {TAIL} falls on its own, past the clouds, toward the snowy forest far below.",
     "the sky above a snowy forest", "the tail falling all the way down", f"any person, {NO_TEXT}")
shot(f"{TAIL} lies tilted in deep snow on the slope, snow sprayed up all around it, pine trees bent around it.",
     SNOWY, "the tail section landed at an angle in deep snow", f"any person, {NO_TEXT}")
shot(f"{VESNA} without her cap lies in a hospital bed, a white bandage around her head and both legs in white casts "
     "held up by straps.", HOSP, "her in the hospital bed with her head bandaged and both legs in casts",
     f"{NO_GORE}, {NO_TEXT}")
shot("Close view of the same woman lying in the hospital bed, now also wearing a stiff back brace around her middle, "
     "a doctor in a white coat beside her looking at a clipboard.", HOSP,
     "the woman in a back brace in bed, the doctor beside her", f"{NO_GORE}, {NO_TEXT}")
shot("The same woman in the hospital bed, eyes now open, looking puzzled, with an empty thought bubble above her head.",
     HOSP, "the woman awake in bed with an empty thought bubble", f"{NO_GORE}, {NO_TEXT}")
shot("A tall vertical line drawing: a tiny stick-figure woman at the very top of the picture with a long dotted line "
     "falling straight down from her to the ground, much longer than a tall mountain drawn beside it for size. A big "
     "gold-medal-shaped star sits next to the dotted line.", "a plain paper background with a small hill at the bottom",
     "the long dotted fall line next to a mountain and a star", NO_TEXT)
shot(f"{VESNA}, healthy again, sits at a desk in the airline office with papers and a telephone, smiling, a small "
     f"model of {JET} on the desk.", "an airline office: a desk, a telephone, papers, a window with planes outside",
     "her back at work for the airline, smiling", NO_TEXT)

# ===================================================================== 2. Michael Packard (16-29)
DIVER = ("a stick-figure man of about fifty-five in a black wetsuit, a diving mask, swim fins and an air tank on his "
         "back with a breathing tube to his mouth")
BOAT = "a small open fishing boat with an outboard motor"
WHALE = ("a huge humpback whale: very long body, long white flippers, a wide mouth with grooved throat folds, a small "
         "bump of a fin on its back")
BAY = "the sea off a sandy beach on a sunny day, low dunes on the shore"
UNDER = "underwater in a bay, sunlight from the surface, a sandy sea floor with rocks and seaweed"

shot(f"{DIVER} sits on the edge of {BOAT}, about to go diving, a mesh bag for lobsters in his hand.", BAY,
     "the lobster diver ready on the edge of the boat", NO_TEXT)
shot(f"{DIVER} swims down toward the sandy sea floor, reaching for a lobster among the rocks, the mesh bag in his "
     "other hand.", UNDER, "the diver underwater reaching for a lobster", NO_TEXT)
shot(f"Everything around {DIVER} turns black in a big dark rush of water, with motion lines; he tumbles.",
     "underwater, suddenly dark", "the diver tumbling as everything goes black", NO_TEXT)
shot(f"Inside total darkness, {DIVER} with wide eyes thinks of a shark: a thought bubble shows a shark's fin and "
     "teeth, crossed out with a big X.", "complete darkness all around",
     "the diver in the dark with the crossed-out shark thought bubble", NO_TEXT)
shot(f"{DIVER} in the dark, his eyes suddenly wide open, a small light bulb above his head.",
     "complete darkness all around", "the diver understanding something", NO_TEXT)
shot(f"Cut-away view: {WHALE} swims near the surface with its mouth closed, and through a cut-away window in its "
     f"cheek we see {DIVER}, tiny, curled up inside its mouth.", UNDER,
     "the diver inside the humpback whale's closed mouth", NO_TEXT)
shot(f"Close view inside the whale's dark mouth: {DIVER} curled up, the breathing tube still in his mouth, little "
     "bubbles rising from it, eyes shut.", "inside a whale's dark mouth, the soft roof of the mouth above",
     "the diver still breathing from his air tank inside the mouth", NO_TEXT)
shot(f"Inside the whale's dark mouth, {DIVER} curled up, with a thought bubble above him showing two boys, about "
     "twelve and fifteen, standing together and smiling.", "inside a whale's dark mouth",
     "the diver thinking of his two boys", NO_TEXT)
shot(f"Side view diagram of {WHALE} with its mouth open wide: a huge mouth with no teeth at all, a big tick mark beside "
     "the mouth.", UNDER, "the whale's huge open mouth with no teeth", NO_TEXT)
shot(f"Close cut-away of the whale's head: a very narrow throat tube going back from the huge mouth, with a tiny "
     f"stick-figure diver drawn next to it, much too big to fit, and a big X over the throat.",
     "a plain light background like a simple diagram", "the whale's throat far too small for a person", NO_TEXT)
shot(f"{WHALE} bursts up out of the sea surface, water splashing, its mouth closed.", BAY,
     "the whale rising up out of the water", NO_TEXT)
shot(f"{WHALE} shakes its head at the surface and {DIVER} flies out of its open mouth in a spray of water.", BAY,
     "the diver being spat out of the whale's mouth", NO_TEXT)
shot(f"A stick-figure young man in a cap leans over the side of {BOAT} and pulls {DIVER} up out of the water.",
     BAY, "the crewmate pulling the diver into the boat", f"{NO_GORE}, {NO_TEXT}")
shot("The same diver, now in a T-shirt, walks out of a hospital door with a few small round bruise marks on his arms, "
     "giving a thumbs-up.", "outside a small hospital on a sunny day", "the diver walking out of hospital",
     f"{NO_GORE}, {NO_TEXT}")

# ===================================================================== 3. Phineas Gage (30-43)
GAGE = ("a stick-figure man of about twenty-five with short dark hair and side whiskers, in an 1840s work shirt, "
        "braces and a wide-brimmed hat")
ROD = "a long straight thin iron rod, longer than a man's arm"
CUT = ("a railway cutting through grey rock in 1840s Vermont: rocky walls, a half-built track bed, green hills and "
       "trees behind")

shot(f"{GAGE} stands in front of his crew of three other stick-figure workers in work clothes, pointing like a boss.",
     CUT, "the foreman with his railway crew", NO_TEXT)
shot("The crew stands back with their hands over their ears as a blast of rock and dust bursts out of the rock wall.",
     CUT, "the gunpowder blast breaking rock", f"{NO_GORE}, {NO_TEXT}")
shot("Close view: a stick-figure worker turns a long hand drill into the rock, making a round hole.", CUT,
     "a hole being drilled into the rock", NO_TEXT)
shot(f"Close view: {GAGE} pours black powder from a small barrel into the hole, then presses it down with {ROD}.",
     CUT, "the foreman pressing the powder down with the iron rod", NO_TEXT)
shot(f"Close view: the tip of {ROD} scrapes the rock at the hole and a small bright spark jumps out.", CUT,
     "the spark at the tip of the iron rod", NO_TEXT)
shot(f"A blast bursts from the hole and {ROD} shoots up out of it like a bullet, with speed lines.", CUT,
     "the iron rod flying up out of the blast", f"{NO_GORE}, {NO_TEXT}")
shot(f"Side view of {GAGE}'s head as a simple x-ray drawing: his outline with the iron rod passing at a slant from under "
     "his left cheekbone up through the top of his head, his hat flying off. Simple, clean, no blood.",
     "a plain light background like a simple diagram", "the rod's straight path from under the cheekbone out the top",
     NO_GORE)
shot(f"Far view: {ROD} lands and sticks in the ground far behind the work site; a long dotted arc shows how far it flew.",
     CUT, "the rod landing far behind", f"any person hurt, {NO_TEXT}")
shot(f"{GAGE} lies on his back on the ground, his hat beside him, his workers running toward him.", CUT,
     "the foreman on the ground and the workers running to him", f"{NO_GORE}, {NO_TEXT}")
shot(f"{GAGE} sits up on the ground with a bandage around his head, talking and waving one hand, while his workers "
     "stare at him with their mouths open.", CUT, "the foreman sitting up and talking", f"{NO_GORE}, {NO_TEXT}")
shot(f"{GAGE}, with a bandage around his head, sits up straight in the back of a wooden ox cart pulled by an ox along "
     "a dirt road into a small 1840s town.", "a dirt road into a small 1840s village with wooden houses",
     "the foreman sitting upright in the ox cart", f"{NO_GORE}, {NO_TEXT}")
shot("The same man, a few years older, without the bandage, walks along a village street; a small calendar beside "
     "him shows its pages flying away.", "a small 1840s village street", "the man years later, alive", NO_TEXT)
shot("Two stick-figure friends whisper to each other, looking at the same man from a distance, with worried faces.",
     "a small 1840s village street", "the two friends whispering about him", NO_TEXT)
shot("An 1840s country doctor with spectacles and a frock coat writes in a notebook with a quill pen at his desk, "
     "with a thought bubble above him showing the same man's face with a question mark.",
     "a doctor's room in the 1840s: a wooden desk, an oil lamp, shelves of bottles",
     "the doctor writing about the man", NO_TEXT)

# ===================================================================== 4. Harrison Okene (44-57)
COOK = "a stick-figure young man of about thirty with short hair, in a white cook's apron over a T-shirt"
TUG = "a sturdy tugboat with a tall cabin, a short funnel and big rubber tyres along its sides"
OILRIG = "a tall offshore oil platform on long legs out at sea"
DARK = "inside a capsized boat in near darkness, everything upside down: the floor above, the ceiling below"

shot(f"{COOK} stirs a pot in the small galley kitchen of {TUG}; through a round window, {OILRIG} stands out at sea.",
     "the small galley kitchen of a tugboat at sea", "the cook in the tugboat's kitchen near the oil platform", NO_TEXT)
shot(f"Early morning, the sky still dark blue: big waves crash over {TUG} and it rolls over onto its side.",
     "the open sea in rough weather before dawn", "the tugboat rolling over in big waves", f"any person, {NO_TEXT}")
shot(f"Cut-away side view: {TUG} lies upside down on the sandy sea floor far below the surface; a tall stack of "
     "ten floors of a building is drawn beside it for size, reaching from the sea floor to the surface.",
     "the deep sea, a sandy sea floor far below the surface", "the upside-down tug on the sea floor, deep as the building",
     f"any person, {NO_TEXT}")
shot(f"{COOK} in a tiny upside-down toilet room, water rushing in at his feet, the light going out.", DARK,
     "the cook in the toilet room as water rushes in", f"{NO_GORE}, {NO_TEXT}")
shot("Far view of the dark upside-down tugboat on the sea floor, quiet and still, small bubbles rising.",
     "the deep dark sea floor", "the sunken tugboat, still and quiet", f"any person, any bodies, {NO_GORE}, {NO_TEXT}")
shot(f"Inside the upside-down boat: a small pocket of air trapped up against the floor above, and {COOK} with his "
     "head and shoulders up in that air, the water up to his chest.", DARK,
     "the small air pocket and the cook's head in it", f"{NO_GORE}, {NO_TEXT}")
shot(f"Close view in near darkness: {COOK} stands with his head in the small air bubble, water to his chest, waiting.",
     DARK, "the cook waiting in the air bubble in the dark", f"{NO_GORE}, {NO_TEXT}")
shot(f"{COOK} in the air bubble holds a can of fizzy drink in one hand and a torch whose light is going out in the other.",
     DARK, "the can of drink and the dying torch", NO_TEXT)
shot("Two stick-figure divers in diving helmets with bright head lamps swim down to the upside-down tugboat.",
     "the deep sea, the upside-down tug on the sea floor", "the divers arriving at the sunken boat", f"{NO_GORE}, {NO_TEXT}")
shot(f"Inside the dark upside-down boat, a diver with a head lamp swims right past {COOK}, the beam of light passing him.",
     DARK, "the diver swimming past the cook", f"{NO_GORE}, {NO_TEXT}")
shot(f"Close view: {COOK}'s hand reaches out of the dark water and grabs the diver's gloved hand. The diver jumps in "
     "surprise.", DARK, "the cook's hand grabbing the diver's hand", f"{NO_GORE}, {NO_TEXT}")
shot(f"{COOK} sits on the deck of a rescue ship wrapped in a blanket, alive, the sea calm around them.",
     "the deck of a rescue ship at sea", "the cook rescued, alone, wrapped in a blanket", f"{NO_GORE}, {NO_TEXT}")
shot("Simple diagram: a stick figure shoots up too fast from the deep sea floor to the surface with a big black-ink "
     "warning sign (an exclamation mark in a triangle) beside him and a big X.", "a cut-away of the deep sea",
     "the warning that coming up too fast is dangerous", f"{NO_GORE}, any words or letters")
shot(f"{COOK} sits inside a round metal pressure chamber, like a big metal tube with a small round window and a "
     "heavy door, waiting patiently.", "the deck of a diving ship with a large round metal pressure chamber",
     "the cook inside the pressure chamber", NO_TEXT)

# ===================================================================== 5. Ann Hodges (58-69)
ANN = ("a stick-figure woman of about thirty-five with short curled 1950s hair, wearing a simple 1950s house dress")
LIVING = ("a small 1950s living room: a couch, a big wooden floor radio cabinet next to it, a lamp, a framed picture, "
          "a window")
TOWN = "a small 1950s town in Alabama: a few small wooden houses with porches, trees, a quiet road"
ROCK = "a dark lumpy rock about the size of a loaf of bread, with small pits on it"

shot(f"Wide view of {TOWN}, with {ANN} standing on the porch of one small house.", TOWN,
     "the woman at her small house in the quiet town", NO_TEXT)
shot(f"{ANN} lies asleep on the couch, a blanket over her, little Z shapes above her head.", LIVING,
     "the woman asleep on the couch", NO_TEXT)
shot(f"{ROCK} crashes down through the ceiling of the living room with a burst of broken plaster, fire trails above it "
     f"showing it came from the sky, while {ANN} sleeps on the couch below.", LIVING,
     "the space rock crashing through the ceiling", f"{NO_GORE}, {NO_TEXT}")
shot(f"{ROCK} bounces off the top of the wooden radio cabinet (a dent and motion lines) and hits {ANN} on the hip; "
     "she jolts awake.", LIVING, "the rock bouncing off the radio onto her hip", f"{NO_GORE}, {NO_TEXT}")
shot(f"{ANN} sits up on the couch holding her hip, wincing, a big round bruise mark on her hip, the rock on the floor.",
     LIVING, "her holding her bruised hip, the rock beside her", f"{NO_GORE}, {NO_TEXT}")
shot(f"{ANN} stands beside the couch looking amazed at {ROCK}, a small star burst above it, and a little doodle of a "
     "shooting star in a thought bubble above her.", LIVING, "her looking at the rock from space", NO_TEXT)
shot(f"Simple drawing: a shooting star streaks down from the sky toward a tiny stick-figure woman lying on a "
     "couch, and a big star badge sits beside it, as if for a first.", "a plain paper background with a night sky at the top",
     "the shooting star coming down to the woman and the star badge", NO_TEXT)
shot(f"Outside the small house, a crowd of stick-figure reporters with 1950s flash cameras and notepads crowd the "
     f"porch, all trying to see {ROCK} held up in the doorway.", TOWN,
     "the crowd of reporters around her house", NO_TEXT)
shot(f"{ANN} looks worried as a stick-figure older woman with her hair in a bun and a stern face points at {ROCK}.",
     LIVING, "the stern landlady pointing at the rock", NO_TEXT)
shot(f"In a small 1950s courtroom, the stern older woman with her hair in a bun points at {ROCK} on a table, while "
     f"{ANN} sits on the other side, worried; a judge sits high at the back.",
     "a small 1950s courtroom: a judge's bench, two tables, wooden chairs", "the two women in court over the rock", NO_TEXT)
shot(f"{ANN} and the stern older woman shake hands across the table, the rock on Ann's side, the landlady turning away.",
     "a small 1950s office", "the two women making a deal, the rock staying with Ann", NO_TEXT)
shot(f"{ROCK} sits in a glass display case in a museum, a few stick-figure visitors looking at it.",
     "a museum hall with glass display cases", "the rock on show in a museum", NO_TEXT)

# ===================================================================== 6. Betty Lou Oliver (70-83)
BETTY = ("a stick-figure young woman of twenty with shoulder-length 1940s curled hair, in a neat 1940s elevator "
         "operator's uniform: a fitted jacket with buttons and a small cap")
TOWER = "the Empire State Building: a very tall stepped skyscraper with a tall spire on top, above other city buildings"
LIFT = "a 1940s elevator car: a small box with a folding metal gate door and a lever control"
SHAFT = "a long dark elevator shaft seen from the side, going down many floors"

shot(f"{BETTY} stands in {LIFT}, her hand on the lever, smiling. Through the open gate, a city view far below.",
     "inside an elevator high up in a skyscraper", "the young elevator operator at work", NO_TEXT)
shot(f"Far view of {TOWER} with thick fog rolling over the whole city, the top of the building disappearing into it.",
     "New York City in the 1940s, covered in thick fog", "the skyscraper in thick fog", f"any person, {NO_TEXT}")
shot(f"A 1940s twin-engine army bomber plane flies out of the fog straight into the side of {TOWER}, a burst of flame "
     "and smoke where it hits, high up.", "New York City in the 1940s, thick fog",
     "the bomber hitting the skyscraper", f"any person, {NO_GORE}, {NO_TEXT}")
shot(f"{BETTY} is thrown out of {LIFT} into a corridor by a blast of smoke, her cap flying off.",
     "a smoky corridor high up inside the skyscraper", "her being thrown out of the elevator",
     f"{NO_GORE}, {NO_TEXT}")
shot(f"Two stick-figure helpers lift {BETTY}, bandaged on her arms, on a stretcher into another elevator with a "
     "folding gate.", "a smoky corridor inside the skyscraper, an elevator door open",
     "the helpers putting her in another elevator", f"{NO_GORE}, {NO_TEXT}")
shot(f"Cut-away view of {SHAFT}: high at the top, the elevator's cables are snapped and loose; the elevator car with "
     "her inside drops fast down the shaft, motion lines above it, many floors below it.", SHAFT,
     "the elevator falling down the shaft with snapped cables", f"{NO_GORE}, {NO_TEXT}")
shot(f"Same cut-away of {SHAFT}: the elevator car far down near the very bottom, still falling, the long dark shaft "
     "above it.", SHAFT, "the elevator near the bottom of the long shaft", f"{NO_GORE}, {NO_TEXT}")
shot("A stick-figure narrator with a pointer stands next to a simple drawing of the elevator shaft and holds up two "
     "fingers.", "a plain wall with a simple drawing of an elevator shaft on it", "the narrator holding up two fingers",
     NO_TEXT)
shot(f"Cut-away of {SHAFT}: the long snapped cables fall down the shaft ahead of the elevator car.", SHAFT,
     "the cables falling down the shaft first", f"any person, {NO_TEXT}")
shot("Cut-away of the bottom of the shaft: the cables lie piled up in big springy coils, and the elevator car lands on "
     "top of them, the coils squashing like a spring.", "the bottom of an elevator shaft",
     "the elevator landing on the coiled cables", f"{NO_GORE}, {NO_TEXT}")
shot("Cut-away of the shaft: the elevator car falling, with a cushion of air under it drawn as curved arrows pushing "
     "up against its floor.", SHAFT, "the trapped air pushing up and slowing the elevator", f"{NO_GORE}, {NO_TEXT}")
shot(f"{BETTY} without her cap lies in a hospital bed in a neck brace, alive, with a small smile.", HOSP,
     "her alive in the hospital bed in a neck brace", f"{NO_GORE}, {NO_TEXT}")
shot("A tall vertical drawing: a long dotted line straight down a tall building's elevator shaft, with a star at the "
     "bottom.", "a plain paper background", "the record fall line down the building with a star", NO_TEXT)
shot(f"{BETTY}, healthy again, steps into {LIFT} and smiles as the gate closes.", "the lobby of a 1940s skyscraper",
     "her riding an elevator again", NO_TEXT)

# ===================================================================== 7. Roy Sullivan (84-100)
ROY = ("a big stick-figure man of about forty with short hair, in a park ranger's uniform: a shirt with a badge and a "
       "flat-brimmed ranger hat")
LIGHTNING = "a bright zig-zag bolt of lightning from a dark storm cloud"
MOUNTS = "forested mountains in Virginia under a stormy sky"

shot(f"{ROY} stands proudly on a mountain trail, hands on his hips.", MOUNTS, "the park ranger on the trail", NO_TEXT)
shot(f"{ROY} stands in the middle; around him, seven small {LIGHTNING}s strike down in a circle, and he gives a "
     "thumbs-up.", MOUNTS, "the ranger with seven lightning bolts around him", NO_TEXT)
shot(f"{LIGHTNING} strikes a tall wooden fire lookout tower on a mountain top, with {ROY} inside its little cabin.",
     "a wooden fire lookout tower on a forested mountain top", "the lightning hitting the lookout tower", NO_TEXT)
shot(f"Close view: {ROY}'s boot with a small smoking hole burned right through it.", "a wooden floor",
     "the shoe with a hole burned through it", f"{NO_GORE}, {NO_TEXT}")
shot("A wall calendar with its pages flying off in a long stream, a cobweb on its corner.", "a plain wall",
     "the calendar pages flying away for years", NO_TEXT)
shot(f"{LIGHTNING} strikes a 1960s pickup truck on a mountain road with {ROY} at the wheel.",
     "a winding mountain road", "the lightning hitting the truck", NO_TEXT)
shot(f"{ROY} slumped in the truck seat with spiral eyes, his eyebrows gone, little smoke wisps from his forehead.",
     "inside a pickup truck", "the ranger knocked out with no eyebrows", f"{NO_GORE}, {NO_TEXT}")
shot(f"{LIGHTNING} strikes {ROY} in the front yard of a small house; he holds his smoking shoulder.",
     "the front yard of a small house with a fence", "the lightning hitting him in his yard", f"{NO_GORE}, {NO_TEXT}")
shot(f"Inside a small ranger station, {LIGHTNING} comes through the window and {ROY}'s hair is on fire with little "
     "flames; he looks shocked.", "inside a small ranger station: a desk, a map on the wall, a window",
     "the ranger's hair on fire inside the station", f"{NO_GORE}, {NO_TEXT}")
shot(f"Outside on patrol, {ROY}'s hair is on fire again, little flames on top of his head, his hat flying off.",
     MOUNTS, "his hair on fire again", f"{NO_GORE}, {NO_TEXT}")
shot(f"{ROY} pours a can of water over his own head, steam rising, a relieved face.", MOUNTS,
     "him pouring water over his head", NO_TEXT)
shot(f"{LIGHTNING} strikes near {ROY}'s ankle as he walks; he hops on one foot holding his ankle.", MOUNTS,
     "the lightning getting his ankle", f"{NO_GORE}, {NO_TEXT}")
shot(f"{ROY} stands at the edge of a small mountain pool with a fishing rod, a storm cloud building above.",
     "a small freshwater pool in the mountain woods", "the ranger fishing", NO_TEXT)
shot(f"{LIGHTNING} hits {ROY} right on the top of his head as he holds his fishing rod; his hat flies up.",
     "a small freshwater pool in the mountain woods", "the lightning hitting the top of his head", f"{NO_GORE}, {NO_TEXT}")
shot(f"A big black bear walks up and grabs the fish hanging from {ROY}'s fishing line, while Roy, still smoking a "
     "little, stares at it.", "a small freshwater pool in the mountain woods",
     "the bear trying to steal his fish", f"{NO_GORE}, {NO_TEXT}")
shot(f"{ROY} swings a tree branch at the big black bear, which runs off without the fish.",
     "a small freshwater pool in the mountain woods", "the ranger chasing the bear off with a branch",
     f"{NO_GORE}, {NO_TEXT}")
shot(f"{ROY} stands proudly next to a giant open record book and a big star; seven little lightning bolts are drawn "
     "around him.", "a plain room", "the ranger with the record book and seven bolts", NO_TEXT)

# ===================================================================== 8. Juliane Koepcke (101-114)
JULIANE = ("a stick-figure teenage girl of seventeen with long straight hair, in a short-sleeved 1970s summer dress "
           "and sandals")
MOTHER = "a stick-figure woman of about forty-five with short hair, in a blouse and skirt"
PROP = "a 1970s four-engine propeller airliner"
JUNGLE = "a thick tropical rainforest: huge trees, hanging vines, giant leaves, ferns on the ground"

shot(f"Inside {PROP}, {JULIANE} sits by the window next to {MOTHER}; out of the window, green rainforest far below. A "
     "small wrapped Christmas present sits on her lap.", "inside a 1970s airliner cabin",
     "the girl and her mother on the plane over the rainforest", NO_TEXT)
shot(f"{PROP} flies into a huge dark storm cloud over the rainforest.", "the sky above a rainforest, a dark storm",
     "the plane flying into the storm", f"any person, {NO_TEXT}")
shot(f"{LIGHTNING} strikes {PROP} and it breaks apart in the air.", "the sky above a rainforest, a dark storm",
     "the plane breaking apart in the storm", f"any person, {NO_GORE}, {NO_TEXT}")
shot(f"{JULIANE} falls through the sky still buckled into a row of three plane seats, the green rainforest far below.",
     "high in the sky above a rainforest", "the girl falling strapped into her row of seats", f"{NO_GORE}, {NO_TEXT}")
shot(f"{JULIANE} lies on the jungle floor among giant leaves, opening her eyes, holding her shoulder.", JUNGLE,
     "the girl waking up alone on the jungle floor", f"{NO_GORE}, {NO_TEXT}")
shot(f"{JULIANE} sits up with a cut on her arm (a simple line, no blood), one eye half closed, holding her knee, "
     "looking around; no one anywhere.", JUNGLE, "the hurt girl alone in the jungle", f"{NO_GORE}, {NO_TEXT}")
shot(f"{JULIANE} kneels at a small trickling creek and looks along it.", JUNGLE, "the girl finding the creek", NO_TEXT)
shot(f"{JULIANE} wades along the creek; the creek grows wider ahead and becomes a river; a sun and a moon above show "
     "days passing.", JUNGLE, "the girl walking and wading downstream for days", NO_TEXT)
shot(f"{JULIANE} reaches a small empty camp on a riverbank: a palm-roofed shelter, a long canoe pulled up, a few "
     "logs and an axe.", "a riverbank in the rainforest", "the girl finding the empty lumberjack camp", NO_TEXT)
shot(f"Three stick-figure lumberjacks in boots and hats come back to the camp and stop in surprise at seeing "
     f"{JULIANE} sitting under the shelter.", "a riverbank in the rainforest", "the lumberjacks finding the girl",
     NO_TEXT)
shot(f"{JULIANE} wrapped in a blanket in a long canoe, the lumberjacks paddling along the river.",
     "a wide river through the rainforest", "the girl being taken away in the canoe", NO_TEXT)
shot(f"{JULIANE} sits alone in the canoe, wrapped in a blanket, quiet and thoughtful.",
     "a wide river through the rainforest", "the girl alone, the only one", f"{NO_GORE}, {NO_TEXT}")
shot("The same girl, now a grown woman with long hair tied back and a backpack, walks into the rainforest.", JUNGLE,
     "the grown woman going back into the rainforest", NO_TEXT)
shot("The same grown woman holds a small bat gently in her hands, studying it, in front of a small wooden research "
     "hut.", "a small wooden research station in the rainforest", "the woman studying a bat at her research station",
     NO_TEXT)

# ===================================================================== 9. Bill Morgan (115-126)
BILL = "a stick-figure man of about forty with short hair and a moustache, in a plain T-shirt and jeans"
TRUCK = "a big long-distance truck with a flat front"

shot(f"{BILL} sits behind the wheel of {TRUCK} on a long straight outback road, red-dirt plains around.",
     "a straight road through the flat Australian outback", "the truck driver at the wheel", NO_TEXT)
shot(f"{BILL} lies in a hospital bed; a small bandage on his forehead from a car crash; a doctor holds out a small medicine bottle to "
     "him, and a black-ink warning sign (an exclamation mark in a triangle) floats above the bottle.", HOSP,
     "him being given the medicine he is allergic to",
     f"{NO_GORE}, any words or letters")
shot(f"A heart monitor beside the bed shows a flat line; {BILL} lies still, doctors rushing in.", HOSP,
     "the flat line on the heart monitor", f"{NO_GORE}, {NO_TEXT}")
shot("Two doctors stand over the bed with paddles; the heart monitor's line jumps back up in a zig-zag.", HOSP,
     "his heart starting again", f"{NO_GORE}, {NO_TEXT}")
shot(f"{BILL} lies still in the hospital bed with tubes and machines around him, eyes closed, little Z shapes above.",
     HOSP, "him in a coma in the hospital bed", f"{NO_GORE}, {NO_TEXT}")
shot(f"In the hospital corridor, a doctor talks quietly to a sad stick-figure family of three; behind the window, "
     f"{BILL} in bed with the machines.", "a hospital corridor with a window into a room",
     "the doctor talking to the sad family", f"{NO_GORE}, {NO_TEXT}")
shot(f"{BILL} sits up in the hospital bed, eyes wide open, waving; the family rushes in happily.", HOSP,
     "him waking up and the happy family", NO_TEXT)
shot(f"{BILL} scratches a scratch card at a shop counter, then jumps for joy next to a shiny new car with a big bow "
     "on it.", "a small shop counter and a car park outside", "him winning a car with a scratch card", NO_TEXT)
shot(f"A TV news crew with a big TV camera on a shoulder and a fluffy microphone films {BILL} outside the shop.",
     "outside a small shop", "the TV crew filming him", NO_TEXT)
shot(f"At the shop counter, {BILL} buys another scratch card while the TV camera films him over his shoulder.",
     "inside a small shop, the counter", "him buying another card on camera", NO_TEXT)
shot(f"Close view: {BILL} scratches the card with a coin, the camera crew leaning in.", "inside a small shop",
     "him scratching the card on camera", NO_TEXT)
shot(f"{BILL} jumps in the air with his arms up, the scratch card in his hand, a shower of $ symbols around him; the "
     "camera crew cheers.", "inside a small shop", "him winning big on camera",
     "any words or letters (only $ symbols)")

# ===================================================================== 10. José Salvador Alvarenga (127-139)
JOSE = "a stick-figure man of about thirty-five with shaggy dark hair and a beard, in a T-shirt and shorts"
YOUNG = "a stick-figure young man of about twenty with short hair, in a T-shirt and shorts"
SKIFF = "a small open fibreglass fishing boat, about the size of a car, with an outboard motor and a big icebox"
OCEAN = "the open Pacific Ocean, nothing but water to the horizon"

shot(f"{JOSE} stands on a beach in Mexico next to {SKIFF}, holding a fishing line.",
     "a beach in Mexico with small fishing boats pulled up on the sand", "the fisherman with his boat", NO_TEXT)
shot(f"{JOSE} and {YOUNG} push {SKIFF} out into the water, ready to go fishing.",
     "a beach in Mexico in the morning", "the two men setting out to fish", NO_TEXT)
shot(f"A wild storm: big waves toss {SKIFF} with the two men holding on, rain pouring down.", OCEAN,
     "the storm hitting the small boat", f"{NO_GORE}, {NO_TEXT}")
shot(f"{SKIFF} drifts with a broken smoking motor, the coast far behind, tiny, both men looking back at it.", OCEAN,
     "the boat with the broken motor drifting out to sea", NO_TEXT)
shot(f"{JOSE} sits up in {SKIFF}, looking out at the huge sea with a determined face, his crewmate beside him.", OCEAN,
     "him learning to live on the boat", NO_TEXT)
shot(f"{JOSE} grabs a fish with his bare hands over the side of the boat; a sea turtle and a seabird nearby.", OCEAN,
     "him catching food with his bare hands", NO_TEXT)
shot(f"{JOSE} holds a sea turtle in the boat, looking grim; a clear empty sky with no rain cloud.", OCEAN,
     "him with the turtle when there is no rain", f"{NO_GORE}, {NO_TEXT}")
shot(f"{JOSE} sits alone in {SKIFF}, head down, sad; the other side of the boat empty.", OCEAN,
     "him alone in the boat", f"{NO_GORE}, any second person, {NO_TEXT}")
shot(f"Very far view: tiny {SKIFF} drifts on the huge empty ocean; sun and moon symbols across the sky show many days.",
     OCEAN, "the tiny boat drifting for months", NO_TEXT)
shot(f"{JOSE}, thin and shaggy, stands up in the boat pointing at a tiny low island on the horizon.", OCEAN,
     "him spotting the island", NO_TEXT)
shot(f"{JOSE} swims toward the small island beach, then crawls up onto the sand.",
     "the edge of a tiny low island with a sandy beach", "him swimming ashore onto the beach", NO_TEXT)
shot("A tally of many little scratch marks on the side of the boat, in groups of five, filling the whole picture.",
     "close view of the side of a fibreglass boat", "a huge number of tally marks for days", "any words or letters")
shot("Simple map drawing: a long dotted line curving all the way across a wide ocean from a coastline on the right "
     "side to a tiny island on the left side, with a tiny boat at the island end.", "a plain paper map with no labels",
     "the long dotted drift line across the ocean", NO_TEXT)

# ===================================================================== 11. Violet Jessop (140-152)
VIOLET = ("a stick-figure young woman with her hair pinned up, in a 1910s stewardess's uniform: a long dark dress, a "
          "white apron and a small white cap")
NURSE = ("the same young woman in a 1910s nurse's uniform: a long dress, a white apron with a small cross on it, "
         "and a white headscarf")
LINER = "a huge 1910s ocean liner with four tall funnels"

shot(f"{VIOLET} carries a tray of teacups along a ship's corridor, smiling at a stick-figure passenger.",
     "a fancy corridor inside a 1910s ocean liner", "the stewardess looking after passengers", NO_TEXT)
shot(f"{VIOLET} stands on a dock in front of three huge ocean liners in a row, each with four tall funnels.",
     "a harbour dock", "the stewardess and the three ships", NO_TEXT)
shot(f"{LINER} scrapes side to side with a grey navy warship, a dent and splash where they hit.",
     "the sea near a harbour", "the liner crashing into the warship", f"any person hurt, {NO_TEXT}")
shot(f"{VIOLET} on the deck straightens her cap, unhurt, calm.", "the deck of a 1910s ocean liner",
     "her fine after the crash", NO_TEXT)
shot(f"{LINER} sails proudly at night, lights glowing in its round windows.", "the open sea at night",
     "the second sister ship sailing", f"any person, {NO_TEXT}")
shot(f"{VIOLET} sits in a lifeboat being lowered down the side of the tilting ship, holding a baby wrapped in a "
     "blanket that an officer has just handed her.", "the side of a tilting ocean liner at night, an iceberg nearby",
     "her in the lifeboat holding the baby", f"{NO_GORE}, {NO_TEXT}")
shot(f"{NURSE} stands on the deck of a white 1910s hospital ship with four funnels and a wide band along its side "
     "with crosses on it.", "the deck of a hospital ship at sea", "her as a nurse on the third ship", NO_TEXT)
shot("A splash of water and smoke bursts up at the side of the white hospital ship, and it starts to tilt.",
     "the sea", "the ship hitting a mine and tilting", f"any person hurt, {NO_GORE}, {NO_TEXT}")
shot(f"{NURSE} sits in a small lifeboat in the water beside the tilting ship.", "the sea beside a tilting ship",
     "her in a lifeboat", f"{NO_GORE}, {NO_TEXT}")
shot("At the back of the tilting ship, its giant propellers still turn above the water, churning white foam, and "
     "broken lifeboat planks fly up around them.", "the stern of a tilting ship at sea",
     "the propellers wrecking the lifeboats", f"any person, {NO_GORE}, {NO_TEXT}")
shot(f"{NURSE} floats in the sea beside her empty lifeboat, holding her head, a bump and little "
     "stars around it, alive, a rescue boat coming toward her.", "the sea beside a tilting ship",
     "her jumping out, hitting her head and surviving", f"{NO_GORE}, {NO_TEXT}")
shot(f"{VIOLET}, a bit older, smiles on the deck of an ocean liner, a tray of teacups in her hands again.",
     "the deck of an ocean liner at sea", "her back at sea", NO_TEXT)
shot("The same woman, older with grey hair, still in a stewardess's uniform on a ship's deck; a calendar beside her "
     "with its pages flying off.", "the deck of a ship at sea", "her working on ships for many more years", NO_TEXT)

# ===================================================================== 12. Tsutomu Yamaguchi (153-166)
MAN = ("a stick-figure Japanese man of about thirty with short neat black hair and round glasses, wearing a plain "
       "short-sleeved work shirt and long trousers")
MAN_BAND = ("a stick-figure Japanese man of about thirty with short neat black hair and round glasses, in a plain work "
            "shirt, with white bandages wrapped around his left arm and over the left side of his face")
BOSS = "a stick-figure older Japanese man with grey hair and a small moustache, in a shirt and tie, at a desk"
FLASH = "a huge, blinding pure white flash of light with bright straight rays shooting out from it"
CLOUD = "a tall mushroom-shaped cloud: a thin column with a big round billowing top"
HIRO = ("a Japanese harbour city street in the 1940s: low wooden houses with curved tiled roofs, electric poles with "
        "wires, the docks at the end of the street with tall cranes")
NAGA = ("the harbour city of Nagasaki in the 1940s: green hills around a long narrow bay, low houses with tiled roofs, "
        "a shipyard with tall cranes")
OFFICE = ("a small 1940s shipyard office: wooden desks with papers, a drafting table with rolled-up plans, a big window "
          "with cranes outside")

shot(f"{MAN} bends over a drafting table drawing a ship with a pencil and ruler.", OFFICE,
     "the engineer at work", NO_TEXT)
shot(f"{MAN} with a small briefcase stands at the edge of a harbour city street, looking around.",
     HIRO, "him arriving in the city for work", NO_TEXT)
shot(f"{MAN} walks down the street toward the docks with his briefcase on a sunny morning.", HIRO,
     "him walking toward the docks", NO_TEXT)
shot(f"{FLASH} fills the sky over the city; {MAN} throws his arm over his eyes.", HIRO,
     "the giant white flash over the city", f"{NO_GORE}, {NO_TEXT}")
shot(f"{MAN} sits in the dust, his shirt torn, holding his hands over his ears with ringing lines, heat lines rising "
     "from his left arm.", "a wrecked 1940s Japanese street with fallen roof tiles and smoke",
     "him hurt by the blast, holding his ears", f"{NO_GORE}, {NO_TEXT}")
shot(f"{MAN} sits alone against a broken wall at night, a dark sky with smoke.",
     "the ruins of a city at night: broken houses, smoke", "him spending the night in the ruins", f"{NO_GORE}, {NO_TEXT}")
shot(f"{MAN} with his torn shirt walks along a road toward a harbour city among green hills.", NAGA,
     "him going home to Nagasaki", f"{NO_GORE}, {NO_TEXT}")
shot(f"{MAN_BAND} walks into the shipyard office with his briefcase.", OFFICE,
     "him going back to work in bandages", f"{NO_GORE}, {NO_TEXT}")
shot(f"{MAN_BAND} stands at {BOSS}'s desk, spreading his arms wide to show how big the flash was; the boss listens.", OFFICE, "him telling his boss about the flash", f"{NO_GORE}, {NO_TEXT}")
shot(f"{FLASH} bursts in through the office window, filling the room with white; both men throw an arm over their "
     "eyes.", OFFICE, "the white light filling the office", f"{NO_GORE}, {NO_TEXT}")
shot(f"Far view: {CLOUD} rising behind the green hills over the harbour city.", NAGA,
     "the mushroom cloud over his home city", f"any person, {NO_GORE}, {NO_TEXT}")
shot(f"{MAN_BAND} lowers his arm in the office, alive, looking around in disbelief.", OFFICE,
     "him alive after the second flash", f"{NO_GORE}, {NO_TEXT}")
shot("The same man, older, in a suit, receives a folded certificate with a round seal from a stick-figure "
     "official, both bowing.", "a plain government office", "him being officially recognised", NO_TEXT)
shot("The same man as a very old man with thin white hair and round glasses, in a cardigan, smiling at a low table "
     "with a cup of tea.", "a quiet Japanese home with sliding paper doors", "him very old and smiling", NO_TEXT)

# ===================================================================== End (167-168)
shot("A friendly stick figure (round head, simple smile) waves at the viewer and points at a big round subscribe-style "
     "button with a bell shape on it.", "a plain room with a plain wall", "the friendly figure pointing at the button",
     NO_TEXT)
shot("Twelve tiny stick figures stand in a row, each holding a small symbol of their story (a food cart, a whale, an "
     "iron rod, a can, a rock, an elevator, a lightning bolt, a bat, a scratch card, a turtle, a lifeboat, a briefcase), "
     "with a speech bubble containing a question mark above them.", "a plain room with a plain wall",
     "the twelve figures and the question mark", NO_TEXT)

assert len(P) == TOTAL, f"{len(P)} scenes for {TOTAL} segments"
segments = [{"id": i, "text": s["text"], "chapter": s["chapter"], "scene": sc, "prompt": prompt(sc)}
            for i, (s, sc) in enumerate(zip(SEGS, P), 1)]
norm = lambda s: re.sub(r"\s+", " ", s).strip()
spoken = norm(" ".join(t for t in (l for l in (HERE / "script.md").read_text(encoding="utf-8").split("\n")
                                    if l.strip() and not l.startswith("#") and not l.startswith("LuckySticks long")
                                    and not l.startswith("Each `##`"))))
assert norm(" ".join(s["text"] for s in segments)) == spoken, "segments drifted from script.md"
(HERE / "script.json").write_text(json.dumps({"title": "The Luckiest People Who Should Have Died", "channel": "found-rich",
                                             "voice": "am_liam", "segments": segments}, indent=1, ensure_ascii=False),
                                  encoding="utf-8")
print(len(segments), "segments; longest prompt", max(len(s["prompt"]) for s in segments))
