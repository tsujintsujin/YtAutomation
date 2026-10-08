"""One image per segment in segments.json, in order: (geek in shot, silver tabby in shot, place, action).

Built by prompt_kit.py (YtAutomation root): every place and every character is written out in full in every prompt.
The only things a prompt may point to are the 3 attached images: the room, the Geek sheet, the cat sheet.
Other cats are never silver or grey tabbies, so they can't be mistaken for the Geek's cat.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from prompt_kit import HOME, HOME_BEDROOM  # noqa: E402

cap = lambda s: s[0].upper() + s[1:]

# Characters other than the Geek and his cat, written out in full wherever they appear.
MOTHER = "a ginger-and-white mother cat with an orange tabby head and back, a white chest, belly and paws, and amber eyes"
KITTENS = ("three tiny newborn kittens, one ginger, one black-and-white and one cream, with their eyes sealed shut and their "
           "tiny ears folded flat")
KITTEN1 = "a tiny newborn ginger kitten with its eyes sealed shut and its tiny ears folded flat"
KITTEN2 = "a tiny newborn black-and-white kitten with its eyes sealed shut and its tiny ears folded flat"
KITTEN3 = "a tiny newborn cream kitten with its eyes sealed shut and its tiny ears folded flat"
WILDCAT = ("a sandy-brown African wildcat with faint darker stripes on its legs, long legs, a slim ringed tail with a black "
           "tip and amber eyes")
JACKAL = "a lean golden jackal with large pointed ears and a bushy black-tipped tail"
CHEETAH = "a slim cheetah with a golden coat covered in solid black spots and black tear lines running down from its eyes"
PUMA = "a tawny puma with a plain light-brown coat, a pale muzzle and a long dark-tipped tail"
LYNX = "a lynx with a thick spotted beige-brown coat, long black ear tufts and a short black-tipped tail"
BOBCAT = "a reddish-brown bobcat with dark spots and a short bobbed tail"
LION = "a large male lion with a thick golden-brown mane"
TIGER = "a large orange tiger with bold black stripes"
LEOPARD = "a leopard with a golden coat covered in small black rosettes"
JAGUAR = "a stocky jaguar with a golden coat covered in large black rosettes with spots inside them"
TORTIE = "a tortoiseshell cat with a mottled black-and-orange coat and amber eyes"
TUXEDO = "a black-and-white tuxedo cat with a white chest, white paws, a white chin and green eyes"
SIAMESE = "a slim cream-colored Siamese cat with dark brown points on its face, ears, paws and tail, and bright blue eyes"
ORANGE = "a plump orange tabby cat with amber eyes"
GINGER = "a slim ginger tabby cat with amber eyes"
BLACK = "a sleek black cat with yellow-green eyes"
CALICO = "a calico cat with patches of white, black and orange"
CALICO_MOM = "a heavily pregnant calico cat with patches of white, black and orange and a round belly"
OLD_CAT = "an elderly thin black cat with grey hairs around its muzzle and cloudy amber eyes"
MERLIN = "a large black-and-white cat with a white chest, white paws and green eyes"
VET = "a friendly female vet with dark curly hair tied back, wearing a blue scrub top"
VET2 = "an older male vet with a grey moustache, wearing a green scrub top"
BEAGLE = "a friendly brown-and-white beagle"
WOMAN = "a woman with short brown hair in a red sweater"
FRIEND = "a man with a short grey beard in a brown cardigan"
SCHOLAR = "an old scholar with white side-whiskers, small round spectacles, a white shirt and a brown waistcoat"
WRITER = "a man in 1600s clothing with long brown hair, a white ruffled collar and a black doublet"
SCIENTIST = "a scientist with short grey hair and rectangular glasses in a white lab coat"
SCIENTIST2 = "a younger scientist with a dark ponytail in a white lab coat and blue gloves"
RESEARCHER = "a woman researcher with shoulder-length blonde hair in a navy fleece jacket"
DOCTOR = "a doctor with short black hair in a white coat with a stethoscope around his neck"
PATIENT = "an older woman with white hair in a lilac tracksuit"
KAREN = "a woman scientist with short dark-brown hair in a grey cardigan"
LISTENER1 = "a young man with a short beard in a blue shirt"
LISTENER2 = "an older woman with white hair in a lilac cardigan"
NERVOUS = "a young man with curly red hair in a mustard sweater"
PARENT = "a young father with short black hair in a grey t-shirt"
WOMAN_FR = "a woman with a short black bob in a striped navy-and-white top and a red scarf"
MAN_DE = "an older man with a grey beard in a green wool vest over a white shirt"
WOMAN_JP = "a young woman with long straight black hair in a light blue sweater"
MEASURER = "a man with short sandy hair in a navy jumper"
VIB = "faint soft curved vibration lines drawn around its throat"

# This video's own places. False = not the attached room.
CAT_HOME = ("A cozy cottage living room with pale yellow walls, a cream two-seat sofa with green cushions, a wooden floor "
            "with a round braided rug, a window with white curtains, and a small wooden side table with a lamp with a red "
            "shade.")
DEVON = ("A cozy English cottage living room: a low ceiling with dark wooden beams, cream walls, a stone fireplace, a red "
         "armchair with a knitted cushion, and a small window looking out onto green hills.")
UNI = ("A university office: tall shelves of books, a big window looking onto green lawns and red-brick buildings, and a "
       "wooden desk with a computer and a pair of small speakers.")
PLACES = dict(HOME, **{
    "bedroom_close_morning": (False, "A close-up on a bed made with a crisp white duvet, in a small bedroom with pale "
                              "sage-green walls softly out of focus behind, lit by bright morning sunlight from a window "
                              "with cream curtains."),
    "bedroom_dawn": (False, HOME_BEDROOM + " Very early dawn: the window shows a pale grey-blue sky, the room is dim and "
                     "cool, and the bedside lamp is off."),
    "bedroom_close_dawn": (False, "A close-up on a white pillow in a small dim bedroom with pale sage-green walls softly out "
                           "of focus behind, in cool grey-blue dawn light."),
    "kitten_box": (False, "A quiet laundry-room corner at night, lit only by a small plug-in night light with a warm amber "
                   "glow: a low open cardboard box lined with soft cream towels stands on grey floor tiles beside a white "
                   "washing machine."),
    "kitten_box_close": (False, "A close-up inside a low open cardboard box lined with soft cream towels, in the warm dim "
                         "amber glow of a small night light."),
    "old_study": (False, "A dim old-fashioned scholar's study lit by an oil lamp: dark wood-panelled walls, tall shelves of "
                  "leather-bound books, a big wooden desk with an open book and an inkwell, a leather armchair, and a small "
                  "window showing night outside."),
    "writing_room": (False, "A 1600s English writing room: dark oak ceiling beams, whitewashed plaster walls, a heavy oak "
                     "table with a lit candle in a brass holder, loose sheets of paper and a goose-feather quill, and a small "
                     "leaded window."),
    "lab": (False, "A tidy science laboratory: white walls, long white lab benches with microscopes and glass beakers, a "
            "computer screen showing a wavy line graph, and bright ceiling lights."),
    "sound_lab": (False, "A small acoustics lab with dark grey sound-absorbing foam on the walls, a desk with a laptop showing "
                  "a wavy line graph, a microphone on a stand and a pair of big headphones."),
    "physio": (False, "A bright physiotherapy clinic room: pale grey walls, a padded blue treatment table, a white skeleton "
               "model on a stand, two exercise balls and a window with white blinds."),
    "clinic": (False, "A bright clean vet clinic exam room: white walls, a stainless-steel exam table, pale blue cabinets and "
               "a sink."),
    "waiting_room": (False, "A small waiting room with pale blue walls, a row of grey plastic chairs, a potted plant and a "
                     "closed white door."),
    "savanna": (False, "Open African grassland at dusk: tall dry golden grass, a few rocks and thorny bushes, a lone "
                "flat-topped acacia tree in the distance, low hills on the horizon and an orange evening sky. No buildings, "
                "roads or fences anywhere."),
    "jungle": (False, "A dense tropical jungle: huge glossy green leaves, hanging vines, thick tree trunks and a shallow "
               "river, with soft misty daylight. No buildings, roads or fences anywhere."),
    "mountain_forest": (False, "A rocky mountain forest: tall pine trees, grey boulders covered in green moss, ferns, and soft "
                        "daylight filtering through the branches. No buildings, roads or fences anywhere."),
    "sanctuary": (False, "A big-cat sanctuary enclosure in sunny daylight: green grass with patches of dry earth, tall leafy "
                  "trees, wooden platforms, beds of straw, and a high wire fence at the back."),
    "garden_wall": (False, "A garden on a calm afternoon: a low grey stone wall covered in ivy, flower beds along it, a green "
                    "lawn and a brick house wall behind."),
    "paris": (False, "A small Paris apartment balcony on a sunny day: black wrought-iron railings, red geraniums in pots, a "
              "little round metal table, and cream stone buildings with grey roofs across the street."),
    "german_kitchen": (False, "A cozy German farmhouse kitchen: dark timber beams, white walls, a green tiled stove, a long "
                       "wooden bench and a window box full of red flowers. Warm daylight."),
    "japan_room": (False, "A traditional Japanese room: a tatami mat floor, sliding paper shoji screens, a low wooden table "
                   "with flat cushions, and an open view of a small garden with a red maple tree. Soft daylight."),
    "cat_home": (False, CAT_HOME + " Afternoon daylight through the window."),
    "cat_home_evening": (False, CAT_HOME + " Evening: the window is dark and the red-shaded side lamp is on, casting a warm glow."),
    "cat_home_kitchen": (False, "A cottage kitchen with pale yellow walls, white cabinets, a white stove, a small wooden table "
                         "with two chairs, a wooden floor and a window with white curtains. Sunny daylight."),
    "closet": (False, "Inside a wooden walk-in closet with pale yellow walls: shelves of folded towels, and a heap of soft "
               "blankets in green, mustard and cream on the wooden floor. Warm dim light."),
    "uni": (False, UNI + " Daylight."),
    "uni_close": (False, "A close-up of a computer screen on a wooden desk in a university office, with shelves of books "
                  "softly out of focus behind."),
    "karen_bedroom": (False, "A small cottage bedroom with pale blue walls, a wooden bed with a blue quilt and white pillows, "
                      "and a window showing a dark early-morning sky."),
    "nursery": (False, "A soft nursery with pale yellow walls, a white wooden crib, a hanging mobile of felt stars and a "
                "wooden rocking chair. Gentle daylight."),
    "devon": (False, DEVON + " Soft daylight."),
    "devon_outside": (False, "A small white cottage with a thatched roof and a green front door among rolling green hills, "
                      "dry-stone walls and hedges under a soft cloudy English sky."),
})

SCENES = [
# 1 Why does your cat purr?
(1, 1, "bedroom_morning", f"The Geek lies in bed under the white duvet, propped on one elbow, looking with a puzzled deadpan expression at the silver tabby cat sitting on his chest, its eyes half closed, {VIB}."),
# 2 Ask most people and they'll say a purr just means a happy cat.
(1, 1, "room_afternoon", f"The silver tabby cat lies curled on the Geek's lap on the brown sofa, eyes closed and blissful, {VIB}, while he gives a small thumbs up with a deadpan face."),
# 3 But cats also purr at the vet and when they're badly hurt.
(1, 1, "clinic", f"The silver tabby cat crouches tensely on the stainless-steel exam table, ears slightly back, {VIB}, while {VET} gently examines it and the Geek stands beside the table looking worried."),
# 4 So what is that purr really trying to tell you?
(1, 1, "room_close_evening", "The Geek leans down with his ear close to the silver tabby cat on the brown sofa, listening intently with a serious deadpan look, while the cat purrs with its eyes half closed."),
# 5 Picture a slow Sunday morning and you're still in bed.
(1, 0, "bedroom_morning", "The Geek lies in bed under the white duvet, awake but sleepy, hair messy, staring calmly at the ceiling."),
# 6 The cat climbs up and plants itself right on your chest.
(1, 1, "bedroom_morning", "The silver tabby cat steps up onto the Geek's chest as he lies in bed under the white duvet, one white front paw planted on his green hoodie, while he lifts his head to look at it."),
# 7 A few seconds later the little motor kicks in.
(1, 1, "bedroom_morning", f"The silver tabby cat settles in a loaf position on the Geek's chest as he lies in bed, eyes half closing, {VIB}."),
# 8 It's a soft and steady rumble
(0, 1, "bedroom_close_morning", f"Close-up of the silver tabby cat's face and white chest as it lies on the white duvet, eyes shut, {VIB}."),
# 9 that you feel more than you actually hear.
(1, 1, "bedroom_close_morning", "Close view of the Geek's hand resting flat on the silver tabby cat's back as it lies on his chest on the white duvet, faint ripple lines spreading under his palm."),
# 10 Your whole ribcage seems to hum along with it.
(1, 1, "bedroom_morning", "Top-down view of the Geek lying flat on his back in bed with the silver tabby cat on his chest, gentle ripple lines spreading across his green hoodie, his eyes wide in mild surprise."),
# 11 The cat's eyes drift shut and somehow the room gets a little quieter.
(1, 1, "bedroom_morning", "Wide calm view of the bedroom: the Geek and the silver tabby cat both have their eyes closed, peaceful in bed, sunlight across the white duvet."),
# 12 It might be one of the nicest sounds in the world.
(1, 1, "bedroom_close_morning", "The Geek smiles slightly with his eyes closed, his cheek resting on the white pillow near the silver tabby cat, which is curled up and purring."),
# 13 It's also one of the strangest. For a very long time nobody could
(1, 1, "bedroom_morning", "The Geek opens one eye and peers suspiciously at the purring silver tabby cat on his chest, as if it were a mysterious little machine."),
# 14 even explain how a cat makes it.
(0, 0, "old_study", f"{SCHOLAR} sits at the desk scratching his head and frowning at an open book that shows a pencil sketch of a cat with no writing on the page."),
# 15 And the reasons behind it turn out
(1, 1, "room_afternoon", "The Geek sits cross-legged on the beige rug facing the silver tabby cat, rubbing his chin thoughtfully, while the cat sits upright looking back at him."),
# 16 to be way more interesting than plain old happiness.
(1, 1, "room_afternoon", "The Geek holds up a large magnifying glass toward the silver tabby cat on the brown sofa, peering through it with a deadpan curious look."),
# 17 So let's go right back to the start.
(0, 0, "kitten_box", "Wide view of the laundry-room corner at night, the cardboard box glowing softly under the amber night light, the edge of a cream towel hanging over its side."),
# 18 Let's go back to a cardboard box full of newborn kittens.
(0, 0, "kitten_box", f"Looking down into the cardboard box: {MOTHER} lies on her side on the cream towels with {KITTENS} snuggled against her belly."),
# 19 A kitten comes into the world blind and deaf.
(0, 0, "kitten_box_close", f"Close-up of {KITTEN1} lifting its tiny nose and sniffing blindly on the cream towels."),
# 20 Its eyes stay sealed for roughly the first week or two.
(0, 0, "kitten_box_close", f"Close-up of the sleeping faces of {KITTENS}, pressed together in a little heap on the cream towels."),
# 21 Its ears are folded down and closed up tight.
(0, 0, "kitten_box_close", f"Extreme close-up of the head of {KITTEN2}, showing its tiny ear folded down flat against its head."),
# 22 It can't walk yet and it can't keep itself warm.
(0, 0, "kitten_box_close", f"{cap(KITTEN1)} wobbles on weak little legs on the cream towels, belly low and legs splayed, unable to stand up properly."),
# 23 About all it can manage is to wriggle toward its mother and eat.
(0, 0, "kitten_box", f"{cap(KITTENS)} crawl blindly across the cream towels toward the belly of {MOTHER}, who lies on her side."),
# 24 Now think about the problem that leaves the mother with.
(0, 0, "kitten_box", f"{cap(MOTHER)} lifts her head and looks down at her kittens with gentle concern; the kittens are {KITTENS}."),
# 25 She's got a heap of tiny kittens
(0, 0, "kitten_box", f"Top-down view of {KITTENS} lying in a sleepy heap on the cream towels beside {MOTHER}."),
# 26 that can't see her or hear her.
(0, 0, "kitten_box_close", f"{cap(MOTHER)} leans her face close to {KITTENS}, who do not react at all."),
# 27 How is she supposed to let them know she's close by?
(0, 0, "kitten_box", f"{cap(MOTHER)} curls her body around {KITTENS} in a protective ring."),
# 28 And how do they let her know they're doing alright?
(0, 0, "kitten_box_close", f"{cap(KITTEN1)} lifts its tiny head toward the soft ginger-and-white fur of its mother, mouth slightly open."),
# 29 The answer turns out to be the purr.
(0, 0, "kitten_box", f"{cap(MOTHER)} lies with her eyes half closed, purring, faint soft curved vibration lines drawn around her throat, while {KITTENS} rest against her belly."),
# 30 Kittens start purring when they're only a few days old.
(0, 0, "kitten_box_close", f"Close-up of {KITTEN1} nursing against the ginger-and-white belly of its mother, {VIB}."),
# 31 The mother purrs right back at them while they nurse.
(0, 0, "kitten_box", f"{cap(KITTENS)} nurse in a row along the belly of {MOTHER}, who purrs with her eyes closed, soft vibration lines drawn around her."),
# 32 A deaf kitten can't hear much of anything.
(0, 0, "kitten_box_close", f"Close-up of {KITTEN2} resting calmly on the cream towels, its tiny folded ear in front."),
# 33 What it can do is feel
(0, 0, "kitten_box_close", f"Close-up of {KITTEN2} pressed against the soft ginger-and-white belly fur of its mother."),
# 34 a vibration running through its whole little body.
(0, 0, "kitten_box_close", f"{cap(KITTEN2)} pressed against the ginger-and-white fur of its mother, gentle glowing ripple lines spreading from the mother's body through the kitten's whole little body."),
# 35 So the purr becomes a quiet signal passed between them.
(0, 0, "kitten_box", f"{cap(MOTHER)} and {KITTENS}, with soft warm wave lines drawn passing back and forth between them like a quiet signal."),
# 36 The mother is saying that she's right here.
(0, 0, "kitten_box", f"{cap(MOTHER)} gently licks the head of {KITTEN1} while purring."),
# 37 The kittens are saying that everything is fine.
(0, 0, "kitten_box", f"{cap(KITTENS)} sleep peacefully against {MOTHER}, their tiny bellies round and full."),
# 38 There's a clever little detail hiding in this too.
(1, 0, "room_afternoon", "The Geek stands by the bookshelf and raises one finger as if he has just had an idea, with a deadpan expression."),
# 39 A kitten can't meow while it's drinking milk.
(0, 0, "kitten_box_close", f"Close-up of {KITTEN1} nursing from {MOTHER}, its mouth busy, cheeks working."),
# 40 Its mouth is far too busy for that.
(0, 0, "kitten_box_close", f"Close-up of {KITTEN3} nursing eagerly, its tiny paws pressing into the ginger-and-white belly fur of its mother."),
# 41 But it can purr with a mouth full of milk just fine.
(0, 0, "kitten_box_close", f"Close-up of {KITTEN3} still nursing while {VIB}."),
# 42 So the purr lets a kitten talk to its mom while it eats.
(0, 0, "kitten_box", f"{cap(MOTHER)} looks down tenderly at {KITTENS} nursing, small soft wave lines connecting the kittens and the mother."),
# 43 That means purring is one of the very
(0, 0, "kitten_box", f"Wide view: {MOTHER} and {KITTENS} asleep together in the cardboard box in the amber night light."),
# 44 first things a cat ever does.
(0, 0, "kitten_box_close", f"Close-up of {KITTEN2} purring in its sleep, its tiny paws curled, {VIB}."),
# 45 It belongs to the warmest and safest days of its whole life.
(0, 0, "kitten_box", f"{cap(KITTENS)} snuggled deep in the cream towels with {MOTHER} curled around them, cozy and warm."),
# 46 And just like kneading it never really goes away.
(1, 1, "room_afternoon", "The silver tabby cat kneads the beige knitted throw on the Geek's lap as he sits on the brown sofa, eyes half closed, purring."),
# 47 So when your grown cat purrs
(1, 1, "room_afternoon", f"The silver tabby cat lies curled on the Geek's lap on the brown sofa, eyes closed, {VIB}."),
# 48 on your lap it's speaking its oldest language.
(1, 1, "room_close_afternoon", "Close view of the silver tabby cat on the Geek's lap, looking up at him with soft half-closed eyes."),
# 49 A lot of experts think it's treating you a bit like its mother.
(1, 1, "room_afternoon", "The silver tabby cat nuzzles into the Geek's green hoodie like a kitten as he sits on the brown sofa, and he looks down with a flat, slightly bewildered deadpan look."),
# 50 You're warm and you're soft and you're the one who brings the food.
(1, 1, "kitchen_afternoon", "The Geek pours dry cat food into a white bowl on the checkered tile floor while the silver tabby cat rubs against his leg."),
# 51 From where the cat is sitting that's a pretty decent mom.
(1, 1, "room_afternoon", "The silver tabby cat sleeps contentedly on the Geek's chest as he reclines on the brown sofa, his hand resting on its back."),
# 52 But how does a cat actually make that sound?
(1, 1, "room_close_afternoon", "The Geek peers closely at the silver tabby cat's throat through a magnifying glass while the cat purrs with its eyes closed."),
# 53 Honestly this one stumped scientists for a surprisingly long time.
(0, 0, "lab", f"{cap(SCIENTIST)} stands at a lab bench scratching her head and frowning, puzzled."),
# 54 Some of the early guesses were a little out there.
(0, 0, "old_study", f"{cap(SCHOLAR)} sits at the desk holding up a magnifying glass over a drawing of a cat, looking baffled; the page has no writing."),
# 55 One old theory said the purr came
(0, 0, "plain", "A simple side-view outline drawing of a cat's body, drawn like a diagram in muted colours, with a red blood vessel running through its chest. No labels or text."),
# 56 from blood rushing through a big vein in the chest.
(0, 0, "plain", "A close diagram-style drawing of a cat's chest with a thick red vein and swirling red flow lines rushing inside it. No labels or text."),
# 57 Another claimed cats had a second set of vocal cords just for purring.
(0, 0, "plain", "A side-view outline drawing of a cat's head and throat with two pairs of small pink vocal cords drawn inside the throat, one pair above the other. No labels or text."),
# 58 Neither one held up in the end.
(0, 0, "old_study", f"{cap(SCHOLAR)} crumples a sheet of paper and tosses it into a wastebasket already full of crumpled paper."),
# 59 For years the best answer came down to muscles.
(0, 0, "plain", "A side-view outline drawing of a cat's head and neck with the small throat muscles shown in soft pink. No labels or text."),
# 60 Tucked inside a cat's throat is the voice box.
(0, 0, "plain", "A side-view outline drawing of a cat's head and neck with a small voice box glowing softly inside the throat. No labels or text."),
# 61 When a cat purrs the muscles around that voice box twitch incredibly fast.
(0, 0, "plain", "A close diagram of a small voice box with pink muscles wrapped around it, quick little motion lines showing the muscles twitching. No labels or text."),
# 62 We're talking twenty to thirty twitches every single second.
(1, 0, "room_afternoon", "The Geek stands on the beige rug snapping his fingers very fast, his hand a blur of motion lines, with a deadpan expression."),
# 63 Each twitch snaps the gap between the vocal cords open and shut again.
(0, 0, "plain", "Two side-by-side drawings of a pair of pink vocal cords seen from above: on the left they are pressed shut, on the right they are open with a gap between them, with simple curved arrows showing the movement. No labels or text."),
# 64 The air rushing through gets chopped up into that quick and steady rumble.
(0, 0, "plain", "A stream of pale blue air drawn flowing up through a cat's throat in side view and breaking into short regular puffs that turn into a wavy line. No labels or text."),
# 65 And the cat keeps it going
(0, 1, "room_close_afternoon", "Side view of the silver tabby cat lying on the beige knitted throw, chest rising, eyes closed, purring."),
# 66 while it breathes in and while it breathes out.
(0, 0, "plain", "A side-view outline drawing of a cat's head and chest with two curved blue arrows, one for air going in and one for air going out, and a steady wavy line running along both. No labels or text."),
# 67 That's why a purr can roll on and on without a single break.
(0, 1, "room_close_afternoon", "The silver tabby cat dozes on the beige knitted throw, a long smooth unbroken wavy line drawn floating from its throat across the frame."),
# 68 Most cat sounds only happen on the way out.
(0, 1, "room_afternoon", "The silver tabby cat stands on the beige rug with its mouth open mid-meow, a small puff of breath drawn coming out."),
# 69 A meow is made with air going out.
(0, 1, "room_close_afternoon", "Close view of the silver tabby cat meowing with its mouth open, a curved pale blue arrow of air drawn flowing out of its mouth."),
# 70 A hiss is made with air going out too.
(0, 1, "room_afternoon", "The silver tabby cat hisses with its ears flat and its back arched at a small red vacuum cleaner standing on the beige rug."),
# 71 The purr is special because it runs in both directions.
(0, 0, "plain", "A side-view outline drawing of a cat's head with a looping two-way pale blue arrow inside its throat, air going down and coming back up. No labels or text."),
# 72 If you listen really closely you can
(1, 1, "room_afternoon", "The Geek lies on the beige rug with his ear pressed gently against the side of the silver tabby cat, eyes closed in concentration."),
# 73 sometimes catch it shifting as the cat breathes.
(1, 1, "room_close_afternoon", "Close-up of the Geek's ear resting against the silver tabby cat's furry side as the cat's chest rises with a breath."),
# 74 Then in 2023 a team of scientists turned up a twist.
(0, 0, "lab", f"{cap(SCIENTIST)} and {SCIENTIST2} stand at a lab bench looking surprised at a computer screen that shows a wavy line graph."),
# 75 They studied the voice boxes of cats that had died of illness.
(0, 0, "lab", f"{cap(SCIENTIST2)} looks through a microscope at a small tissue sample in a glass dish, calm and focused."),
# 76 And they found a voice box could make a purring sound
(0, 0, "lab", "A small glass laboratory apparatus on the lab bench connected to a thin clear air hose, a soft wavy line drawn coming out of it, and the computer screen showing a matching wave."),
# 77 with no twitching muscles at all.
(0, 0, "lab", f"{cap(SCIENTIST)} raises her eyebrows in surprise and points at the wavy line on the computer screen."),
# 78 Just blowing air through it was enough to do the trick.
(0, 0, "lab", "Close view of a thin clear air hose blowing a gentle stream of air, drawn as pale blue lines, into a small glass apparatus on the lab bench."),
# 79 Inside the vocal cords they spotted small pads of soft tissue.
(0, 0, "plain", "A close diagram of a pair of pink vocal cords seen from above, with small soft round pads drawn inside them. No labels or text."),
# 80 Those pads make the cords heavier so they can wobble very slowly.
(0, 0, "plain", "A pair of thick pink vocal cords with soft pads inside, drawn with slow wide wavy motion lines. No labels or text."),
# 81 That's how such a small animal pulls off such a deep sound.
(0, 1, "room_afternoon", "The silver tabby cat sits small on the big brown sofa while big, deep, low wavy lines roll out from it across the room."),
# 82 So the real answer is probably a bit of both.
(0, 0, "plain", "A side-view outline drawing of a cat's head with a small softly glowing brain and a softly glowing voice box, joined by a thin glowing line. No labels or text."),
# 83 The brain and the muscles get the purr started and keep it going.
(0, 0, "plain", "A side-view outline drawing of a cat's head and neck with a gentle glowing path running from the brain down to the throat muscles. No labels or text."),
# 84 The odd build of the voice box gives it
(0, 0, "plain", "A close diagram of a cat's small voice box with thick padded vocal cords inside it, softly shaded. No labels or text."),
# 85 that deep and steady rumble.
(0, 1, "room_close_afternoon", "The silver tabby cat purrs with its eyes closed, a deep steady wavy line drawn flowing from its throat."),
# 86 Scientists are still sorting out the details.
(0, 0, "lab", f"{cap(SCIENTIST)} and {SCIENTIST2} sit at the lab bench surrounded by sheets of paper with no readable writing, deep in discussion."),
# 87 And I find it kind of amazing that one of the most familiar sounds
(1, 1, "room_evening", "The Geek sits on the brown sofa holding a mug, gazing in quiet wonder at the silver tabby cat purring beside him."),
# 88 in your house is still partly a mystery.
(1, 1, "room_evening", "The Geek tilts his head with a puzzled deadpan look at the silver tabby cat, and the cat tilts its head back at him."),
# 89 Here's another fun one for you.
(1, 1, "room_afternoon", "The Geek sits on the brown sofa holding open a picture book with a painting of a cheetah and no writing, showing it to the silver tabby cat beside him."),
# 90 Not every cat can purr at all.
(0, 0, "savanna", f"{cap(LION)} sits on a flat rock with his mouth closed, looking out over the grass."),
# 91 Your house cat purrs and so does a cheetah.
(0, 0, "savanna", f"{cap(CHEETAH)} lies in the golden grass with its eyes half closed, purring, {VIB}."),
# 92 So does a puma and a lynx and a bobcat.
(0, 0, "mountain_forest", f"{cap(PUMA)}, {LYNX} and {BOBCAT} rest on mossy boulders near each other, all with their eyes half closed, purring."),
# 93 The big famous cats are a different story though.
(0, 0, "savanna", f"{cap(LION)} stands proudly on a rock with a lioness with a plain tawny coat beside him."),
# 94 Lions and tigers and leopards
(0, 0, "jungle", f"{cap(TIGER)} and {LEOPARD} walk along the muddy riverbank."),
# 95 and jaguars can't purr the way your cat does.
(0, 0, "jungle", f"{cap(JAGUAR)} lies on a thick branch over the river with its mouth closed, staring calmly."),
# 96 Those four are the ones that can roar.
(0, 0, "savanna", f"{cap(LION)} roars with his mouth wide open and his head raised, his mane blowing."),
# 97 For a long time people thought it all came down
(0, 0, "old_study", f"{cap(SCHOLAR)} studies a big drawing of a lion's skull at his desk by lamp light; the paper has no writing."),
# 98 to a small bone in the throat.
(0, 0, "plain", "A side-view outline drawing of a lion's head and throat with a small curved bone in the throat softly highlighted. No labels or text."),
# 99 In the roaring cats part of that bone stays soft and stretchy.
(0, 0, "plain", "A close drawing of a small curved throat bone where one section is a soft stretchy band, shown stretching like elastic. No labels or text."),
# 100 That was supposed to explain why they roar instead of purr.
(0, 0, "savanna", f"{cap(LION)} roars from a rock at dusk, powerful wave lines bursting from his mouth."),
# 101 These days the picture looks a lot messier.
(0, 0, "lab", f"{cap(SCIENTIST)} frowns at a messy tangle of papers and diagrams with no writing spread over the lab bench."),
# 102 The shape of their vocal cords seems to matter quite a bit too.
(0, 0, "plain", "Two pairs of pink vocal cords seen from above, side by side: a small thin pair on the left and a large thick flat-edged pair on the right. No labels or text."),
# 103 A lion can make a sort of purring sound as it breathes out.
(0, 0, "savanna", f"{cap(LION)} lies relaxed in the grass with his eyes half closed, a soft puff of breath and a gentle wavy line drawn coming from his nose."),
# 104 What it can't do is keep the rumble going
(0, 0, "savanna", f"{cap(LION)} lies in the grass with his mouth closed, a short broken dotted wave line drawn beside him."),
# 105 in and out like your cat.
(0, 1, "room_close_afternoon", "The silver tabby cat purrs on the beige knitted throw with a smooth unbroken looping wave line drawn around it."),
# 106 So there's a rough rule in the cat family.
(0, 0, "plain", "A row of five members of the cat family standing side by side in muted colours: a small black house cat, a spotted cheetah, a tawny puma, a maned lion and a striped tiger. No labels or text."),
# 107 Most cats get to purr or roar but not both.
(0, 0, "plain", "Two groups of animals: on the left a small black house cat, a spotted cheetah and a lynx with ear tufts sit calmly with their eyes half closed; on the right a maned lion, a striped tiger and a spotted jaguar roar with their mouths open. No labels or text."),
# 108 Very few of them can really pull off the two.
(0, 0, "savanna", f"{cap(CHEETAH)} and {LION} sit side by side in the golden grass, the cheetah calm and the lion yawning wide."),
# 109 Your little cat ended up with the purr.
(0, 1, "room_afternoon", f"The silver tabby cat sits proudly on the brown sofa with its chest puffed out, {VIB}."),
# 110 And honestly that's the better deal when you're curled up on a lap.
(1, 1, "room_afternoon", "The silver tabby cat curls up on the Geek's lap on the brown sofa, purring, while he reads a book."),
# 111 People have been charmed by this sound for ages.
(0, 0, "old_study", f"{cap(SCHOLAR)} sits in the leather armchair with {TORTIE} purring on his lap, smiling softly."),
# 112 The English word purr was first written down back in the 1600s.
(0, 0, "writing_room", f"{cap(WRITER)} writes with the quill by candlelight while {TORTIE} purrs on the table beside the paper; the paper shows only faint squiggly lines, no readable writing."),
# 113 It was made to sound just like the noise it describes.
(0, 0, "writing_room", f"{cap(WRITER)} pauses with his quill raised, listening with a smile to {TORTIE}, who purrs on the table with soft vibration lines around its throat."),
# 114 Plenty of other languages did the exact same thing.
(0, 0, "plain", "A cheerful world map in muted colours with small cats of different colours sitting on the different continents, none of them grey or silver. No labels or text."),
# 115 In French a contented cat goes ronron.
(0, 0, "paris", f"{cap(WOMAN_FR)} sits at the little round table on the balcony stroking {BLACK}, which purrs on the table with its eyes closed."),
# 116 In German a happy cat will schnurren.
(0, 0, "german_kitchen", f"{cap(MAN_DE)} sits on the long wooden bench with {ORANGE} purring on his lap."),
# 117 In Japanese the purr is goro goro.
(0, 0, "japan_room", f"{cap(WOMAN_JP)} kneels at the low table with {CALICO} purring on a flat cushion beside her."),
# 118 Pretty much anywhere people live with cats they came up
(0, 0, "plain", f"Four cats sitting side by side, all purring with their eyes closed: {BLACK}, {ORANGE}, {CALICO} and {TUXEDO}. No labels or text."),
# 119 with a word for that rumble.
(1, 1, "room_afternoon", "The Geek holds the purring silver tabby cat up near his ear on the brown sofa, listening with a deadpan look."),
# 120 Okay so now we get to the real puzzle.
(1, 1, "room_evening", "The Geek sits at the coffee table with a blank notepad, frowning thoughtfully, while the silver tabby cat watches from the brown sofa."),
# 121 If a purr means a happy cat then why do cats purr
(1, 1, "room_evening", "The Geek holds the purring silver tabby cat out at arm's length, studying it with a skeptical deadpan look."),
# 122 when they're miserable?
(0, 1, "room_evening", f"The silver tabby cat sits hunched and tense in the corner by the bookshelf, ears slightly back, eyes wide, {VIB}."),
# 123 Ask any vet and you'll hear the same thing.
(0, 0, "clinic", f"{cap(VET)} stands by the exam table with her arms folded, giving a knowing nod."),
# 124 Cats purr up on the exam table.
(1, 1, "clinic", f"The silver tabby cat sits tensely on the stainless-steel exam table, {VIB}, while {VET} listens to its chest with a stethoscope and the Geek watches."),
# 125 They purr when they're frightened.
(0, 1, "room_evening", f"The silver tabby cat crouches under the coffee table with wide eyes and flattened ears as lightning flashes in the dark window, {VIB}."),
# 126 They purr when they're injured and in real pain.
(0, 1, "clinic", f"The silver tabby cat lies on the stainless-steel exam table with a small white bandage around one front leg, purring softly, while {VET} strokes its head."),
# 127 Mother cats purr while they're giving birth. And some cats purr softly
(0, 0, "closet", f"{cap(CALICO_MOM)} lies on the soft blankets with her eyes half closed, purring, faint soft vibration lines around her throat."),
# 128 when they're very old and close to the end.
(0, 0, "cat_home", f"{cap(OLD_CAT)} sleeps curled on a soft blanket in a patch of sunlight on the round braided rug, peaceful."),
# 129 None of those are what you'd call happy moments.
(1, 1, "room_evening", "The Geek sits on the beige rug looking gently concerned at the silver tabby cat, which sits close beside him."),
# 130 So the purr can't simply mean a cat is content.
(1, 1, "room_evening", "The Geek slowly shakes his head with a deadpan look, holding a feather toy, as the silver tabby cat looks up at him."),
# 131 A lot of experts now see the purr as a way
(0, 1, "room_close_evening", "The silver tabby cat sits with its eyes closed, purring, its body slowly loosening from a tense hunch."),
# 132 for a cat to calm itself down.
(0, 1, "room_close_evening", "The silver tabby cat lies down on the beige knitted throw, shoulders softening and eyes closing, purring."),
# 133 It's a bit like a person humming under their breath when they're nervous.
(0, 0, "waiting_room", f"{cap(NERVOUS)} sits on a grey chair humming to himself with his eyes closed and his hands clasped, a few small musical note shapes floating up."),
# 134 Or rocking back and forth a little when something hurts.
(0, 0, "waiting_room", f"{cap(NERVOUS)} rocks gently forward and back on his grey chair, holding his bandaged hand."),
# 135 That steady rhythm seems to soothe the cat.
(0, 1, "room_close_evening", "The silver tabby cat dozes on the beige knitted throw, soft even wave lines rising and falling around it in a calm rhythm."),
# 136 Some scientists think purring might even help the body release chemicals
(0, 0, "plain", "A side-view outline drawing of a cat's body with soft glowing golden dots spreading from its head down through its body. No labels or text."),
# 137 that ease pain and stress. Nobody has proven that one yet.
(0, 0, "lab", f"{cap(SCIENTIST)} shrugs with both palms up beside a lab bench, with a gentle uncertain expression."),
# 138 But it would explain an awful lot.
(1, 1, "room_evening", "The Geek nods slowly with his chin in his hand, sitting next to the purring silver tabby cat on the brown sofa."),
# 139 It fits the kitten story too. From the very first days of life
(0, 0, "kitten_box", f"{cap(MOTHER)} curls around {KITTENS}, all of them purring, in the warm amber glow."),
# 140 a purr was the sound of being safe.
(0, 0, "kitten_box_close", f"{cap(KITTEN1)} sleeps against the ginger-and-white fur of its mother, completely relaxed."),
# 141 So when a grown cat feels scared
(0, 1, "room_evening", "The silver tabby cat crouches tensely at the edge of the beige rug with its ears pulled back."),
# 142 or sore it reaches back for that old sound.
(0, 1, "room_close_evening", "The silver tabby cat curls up tight on the beige knitted throw, eyes closed, purring softly to itself."),
# 143 It's almost as if the cat is telling itself
(0, 1, "room_close_evening", f"The silver tabby cat with its eyes closed and its chin tucked in, {VIB}, calm and steady."),
# 144 that it's going to be okay.
(0, 1, "room_evening", "The silver tabby cat stretches out on the brown sofa, calm and relaxed, its tail draped loosely."),
# 145 And this matters for you as an owner.
(1, 1, "room_evening", "The Geek kneels beside the silver tabby cat on the beige rug, watching it attentively with a serious face."),
# 146 A purring cat isn't always a healthy cat.
(0, 1, "room_evening", f"The silver tabby cat lies flat and droopy on the beige rug, eyes half closed, {VIB}, looking a little unwell."),
# 147 Cats are remarkably good at hiding pain. Out in the wild a cat
(0, 0, "savanna", f"{cap(WILDCAT)} limps slightly through the tall golden grass, glancing around warily."),
# 148 that looks weak can quickly become somebody's dinner.
(0, 0, "savanna", f"{cap(JACKAL)} watches from behind a thorny bush, its eyes fixed on {WILDCAT} in the distance."),
# 149 So a sick cat might tuck itself away somewhere and purr.
(0, 1, "room_evening", "The silver tabby cat hides in the dark gap under the brown sofa, only its eyes and white paws showing."),
# 150 If your cat is purring but also hiding or skipping meals,
(0, 1, "kitchen_afternoon", "The silver tabby cat sits beside a full, untouched white bowl of cat food on the checkered tile floor, looking away from it."),
# 151 please give your vet a call.
(1, 1, "room_evening", "The Geek holds a phone to his ear with a concerned face, the silver tabby cat sitting beside him on the brown sofa."),
# 152 Now here's what I think is the most surprising idea of the lot.
(1, 0, "room_evening", "The Geek leans forward on the brown sofa with wide eyes behind his glasses, intrigued."),
# 153 Some scientists think the purr might actually help a cat heal.
(0, 1, "room_close_evening", "The silver tabby cat lies on the beige knitted throw with a small white bandage on one front leg, purring, soft golden glow lines around the leg."),
# 154 You've probably heard the old saying that cats have nine lives.
(0, 0, "plain", "Nine small cat silhouettes in a neat row in muted colours, each in a different pose: sitting, leaping, sleeping and stretching. No labels or text."),
# 155 And cats do seem to bounce back from injuries remarkably well.
(0, 0, "garden_wall", f"{cap(ORANGE)} leaps lightly up onto the low stone wall and lands perfectly."),
# 156 There are old stories among vets
(0, 0, "clinic", f"{cap(VET)} and {VET2} chat beside the exam table holding coffee mugs, smiling."),
# 157 that cats mend broken bones faster than dogs do.
(0, 0, "clinic", f"{cap(BEAGLE)} with a white cast on one front leg sits on the floor looking glum, while {TUXEDO} with a small healed shaved patch on its leg trots past it."),
# 158 Cats also seem to run into fewer problems
(0, 0, "garden_wall", f"{cap(TUXEDO)} stretches long and supple along the top of the low stone wall."),
# 159 with their bones and joints as they get older.
(0, 0, "plain", "A side-view drawing of a walking cat with its skeleton and joints softly visible through its body. No labels or text."),
# 160 Around the year 2001 a researcher named Elizabeth von
(0, 0, "sound_lab", f"{cap(RESEARCHER)} sits at the desk wearing big headphones, studying a wavy line graph on the laptop."),
# 161 Muggenthaler recorded the purrs of lots of different cats.
(0, 0, "sound_lab", f"{cap(RESEARCHER)} holds the microphone on its stand close to {TUXEDO}, which sits on the desk purring."),
# 162 She recorded house cats and cheetahs and pumas and more besides.
(0, 0, "sanctuary", f"{cap(RESEARCHER)} holds a microphone on a long pole toward {CHEETAH}, which lies in the grass inside the fence."),
# 163 Most of those purrs sat
(0, 0, "sound_lab", "Close view of the laptop screen showing a low, slow, regular wavy line. No numbers or text."),
# 164 in a low range of about twenty five to fifty vibrations per second.
(0, 0, "plain", "A gentle wavy line with wide, even, slow waves running across the frame, softly shaded. No labels or text."),
# 165 And that happened to line up with something interesting from human medicine.
(0, 0, "physio", f"{cap(DOCTOR)} holds up an X-ray of a leg bone against the window light, studying it."),
# 166 Doctors have studied gentle vibration as a way to help bones grow stronger.
(0, 0, "physio", f"{cap(PATIENT)} stands on a low vibration platform holding its handles, while {DOCTOR} watches a tablet beside her."),
# 167 Some of the frequencies used in that work land
(0, 0, "plain", "Two gentle wavy lines drawn one above the other, with matching wide even waves. No labels or text."),
# 168 in the same low range as a purr.
(0, 0, "plain", "A wavy line coming from a small cat silhouette on the left meeting a matching wavy line coming from a small bone shape on the right. No labels or text."),
# 169 So the idea goes something like this. A cat lounging around for hours
(0, 1, "room_afternoon", "The silver tabby cat sprawls on the sunny windowsill, napping and purring."),
# 170 on end might use its purr like a built in massage machine.
(0, 1, "room_close_afternoon", "The silver tabby cat naps in a sunbeam on the beige knitted throw, soft gentle ripple lines spreading through its body like a massage."),
# 171 That low buzz could keep its bones
(0, 0, "plain", "A side-view drawing of a sleeping cat with its skeleton softly visible and gentle vibration lines around the bones. No labels or text."),
# 172 and muscles strong while it naps the day away.
(0, 1, "room_afternoon", "The silver tabby cat sleeps stretched out long on the brown sofa in a patch of sunlight."),
# 173 It might even help an injury knit back together a bit faster.
(0, 0, "plain", "A close drawing of a cracked bone slowly joining back together, with soft golden glow lines around the crack. No labels or text."),
# 174 It's a lovely idea and I really want it to be true.
(1, 1, "room_afternoon", "The Geek hugs an olive-green cushion on the brown sofa, gazing hopefully at the silver tabby cat napping in the sun."),
# 175 But we have to be honest about where it stands.
(1, 0, "room_afternoon", "The Geek sits up straight on the brown sofa and raises one finger with a serious deadpan face."),
# 176 Nobody has actually proven that purring heals cats.
(0, 0, "lab", f"{cap(SCIENTIST)} opens an empty folder and shakes her head gently."),
# 177 It's a theory that happens to fit some of the facts.
(1, 0, "office_afternoon", "The Geek pins a few pictures of cats onto the cork board and links them with red string, rubbing his chin."),
# 178 Nobody has done the big careful studies that would show it really works.
(0, 0, "lab", "Rows of empty lab benches with dust sheets over the microscopes and nobody there."),
# 179 So file it under fascinating maybe and not under settled fact.
(1, 0, "office_afternoon", "The Geek slides a plain manila folder into a desk drawer with a deadpan shrug."),
# 180 Some people take it one step further.
(1, 1, "room_evening", "The Geek lies on the brown sofa with the silver tabby cat on his chest, eyebrows raised."),
# 181 They say a purring cat can help heal humans as well.
(1, 1, "room_evening", "The Geek lies on the brown sofa holding up his finger with a small bandage on it near the purring silver tabby cat on his chest, looking hopeful."),
# 182 That hasn't been proven either. Still plenty of cat owners will tell you
(0, 0, "cat_home", f"{cap(WOMAN)} relaxes on the cream sofa with {ORANGE} purring on her lap, her eyes closed and smiling."),
# 183 a purring cat takes the edge off their stress.
(0, 0, "cat_home_evening", f"{cap(WOMAN)} lies back on the cream sofa, shoulders dropping in relief, as {ORANGE} purrs on her chest."),
# 184 And one large study found
(0, 0, "lab", f"{cap(SCIENTIST)} looks through a tall stack of paper forms with no readable writing."),
# 185 that cat owners were less likely to die of a heart attack.
(0, 0, "plain", "A soft red heart shape with a small orange cat curled around it, asleep. No labels or text."),
# 186 Whether the purr is the reason is anybody's guess.
(1, 1, "room_evening", "The Geek shrugs with both hands up and a deadpan face, the silver tabby cat curled beside him on the brown sofa."),
# 187 But it's hard to argue with a warm cat rumbling
(1, 1, "room_evening", "The Geek slumps on the brown sofa looking exhausted, his sneakers kicked off, as the silver tabby cat climbs onto his chest."),
# 188 on your chest after a rotten day.
(1, 1, "room_evening", f"The Geek lies on the brown sofa with his eyes closed and a small relieved smile, the silver tabby cat on his chest with {VIB}."),
# 189 Now let's talk about the purr your cat saves just for you.
(1, 1, "kitchen_morning", "The silver tabby cat sits beside its empty white food bowl on the checkered tiles, staring up at the Geek."),
# 190 Have you ever been woken up
(1, 1, "bedroom_dawn", "The Geek sleeps in bed under the white duvet with his mouth open, while the silver tabby cat sits on the pillow beside his head staring at him."),
# 191 at five in the morning by a purring cat?
(1, 1, "bedroom_dawn", f"The round black alarm clock on the nightstand, its plain face showing two hands and no numbers, sits beside the bed where the silver tabby cat stands over the sleeping Geek with {VIB}."),
# 192 One that parks itself on your pillow
(1, 1, "bedroom_dawn", "The silver tabby cat settles down on the Geek's pillow right next to his face as he sleeps."),
# 193 and purrs straight into your face?
(1, 1, "bedroom_close_dawn", "Close-up: the silver tabby cat's face pressed right up to the Geek's sleeping face on the pillow, purring, his eyes squeezed shut."),
# 194 There's a reason that particular purr is so hard to ignore.
(1, 1, "bedroom_dawn", "The Geek pulls the white duvet over his head while the silver tabby cat stands on top of him, purring loudly with big vibration lines."),
# 195 In 2009 a scientist named Karen McComb
(0, 0, "uni", f"{cap(KAREN)} sits at the desk listening to the speakers with a thoughtful look."),
# 196 at the University of Sussex decided to dig into this.
(0, 0, "uni", f"{cap(KAREN)} leans in to study a wavy line graph on the computer screen."),
# 197 Her own cat had a habit of waking her up early for breakfast.
(0, 0, "karen_bedroom", f"{cap(KAREN)} lies half asleep in bed while {GINGER} sits on her pillow purring at her face."),
# 198 So she and her team recorded cats purring in two different situations.
(0, 0, "cat_home_kitchen", f"{cap(WOMAN)} holds a small digital audio recorder out toward {ORANGE}, which sits on the kitchen counter."),
# 199 In the first one the cats were just relaxing.
(0, 0, "cat_home", f"{cap(ORANGE)} lies relaxed on the cream sofa with its eyes closed, a small digital audio recorder on the cushion beside it."),
# 200 In the second one the cats were asking their owners for food.
(0, 0, "cat_home_kitchen", f"{cap(ORANGE)} sits by an empty food bowl staring up at {WOMAN}, mouth slightly open, a small digital audio recorder on the floor."),
# 201 Then they played both kinds of purr back to people.
(0, 0, "uni", f"{cap(LISTENER1)} and {LISTENER2} sit at a table wearing headphones, listening carefully."),
# 202 Even folks who had never owned a cat could tell them apart.
(0, 0, "uni", f"{cap(LISTENER1)}, wearing headphones, raises his eyebrows and confidently points at one of two plain buttons on a small device."),
# 203 The food purrs came across as more urgent and less pleasant.
(0, 0, "uni", f"{cap(LISTENER2)} winces slightly while listening on her headphones."),
# 204 People found them a whole lot harder to tune out.
(0, 0, "uni", f"{cap(LISTENER1)} and {LISTENER2} both lift their headphones off one ear, looking bothered."),
# 205 When the team dug a little deeper they found the secret.
(0, 0, "uni", f"{cap(KAREN)} leans close to the computer screen, her eyes widening."),
# 206 Hidden inside the hungry purr was a high pitched sound.
(0, 0, "uni_close", "The computer screen shows a low wide wavy grey line with a thin, sharp, spiky orange line hidden inside it. No numbers or text."),
# 207 It was a bit like a cry stirred into the rumble.
(0, 0, "plain", "A low, wide, soft grey wavy line with a thin bright orange high-pitched squiggle woven through it. No labels or text."),
# 208 And it sat in a range close
(0, 0, "plain", "Two thin orange squiggles drawn one above the other with matching shapes: a small cat silhouette beside the top one and a small baby bottle beside the bottom one. No labels or text."),
# 209 to the cry of a human baby.
(0, 0, "nursery", "A baby in a white onesie cries in the crib with its mouth open and its little fists up."),
# 210 People are wired to respond when a baby cries.
(0, 0, "nursery", f"{cap(PARENT)} rushes into the nursery toward the crying baby in the crib, arms out."),
# 211 So the cat had figured out how
(0, 1, "kitchen_morning", "The silver tabby cat sits on the kitchen counter beside the coffee maker, looking sly and purring."),
# 212 to tug on that very same string.
(1, 1, "kitchen_morning", "The Geek reaches for the bag of cat food as if pulled by an invisible string, while the silver tabby cat watches calmly from the floor."),
# 213 Scientists call this the solicitation purr.
(0, 1, "kitchen_morning", "The silver tabby cat sits upright beside its empty white bowl on the checkered tiles, purring and looking up expectantly."),
# 214 Basically it's a purr with a request baked right in.
(0, 1, "kitchen_morning", "Close view of the silver tabby cat's face, mouth slightly open, soft vibration lines around its throat with one thin orange squiggle mixed in."),
# 215 Cats that live closely with one person seem to use it the most.
(1, 1, "room_morning", "The Geek and the silver tabby cat sit side by side on the brown sofa, both looking out of the window."),
# 216 Over time they learn exactly which sound gets the bowl filled.
(1, 1, "kitchen_morning", "The silver tabby cat purrs at the Geek's feet as he fills its white bowl with dry food."),
# 217 In other words your cat may well have trained you.
(1, 1, "kitchen_morning", "The Geek stands by the counter holding the cat food bag like an obedient servant, while the silver tabby cat sits on the counter looking down at him like a boss."),
# 218 And it pulled the whole thing off with a purr.
(0, 1, "kitchen_morning", "The silver tabby cat eats happily from its full white bowl on the checkered tiles, tail up."),
# 219 So listen closely the next time your cat purrs
(1, 1, "kitchen_morning", "The Geek crouches on the checkered tiles, cupping one hand behind his ear toward the purring silver tabby cat."),
# 220 at you near the kitchen.
(0, 1, "kitchen_morning", "Wide view of the kitchen: the silver tabby cat sits in the middle of the checkered floor purring, facing the fridge."),
# 221 You might catch that little cry tucked inside the rumble.
(0, 1, "kitchen_morning", "Close view of the silver tabby cat's face, mouth slightly open, eyes wide and pleading."),
# 222 That isn't just love doing the talking.
(1, 1, "kitchen_morning", "The Geek opens his arms for a hug toward the silver tabby cat, which looks right past him at the food cupboard."),
# 223 That's a breakfast order being placed.
(0, 1, "kitchen_morning", "The silver tabby cat sits on a chair at the small round wooden table like a customer, an empty white food bowl in front of it, looking demanding."),
# 224 Purrs come in all sorts of sizes too.
(0, 0, "plain", "Three wavy lines one above the other: a tiny faint one, a medium one, and a large bold one. No labels or text."),
# 225 Some cats purr so softly you only notice
(1, 1, "room_close_afternoon", "Close view of the Geek's fingertips resting gently on the silver tabby cat's white throat, the cat's eyes closed."),
# 226 when your fingers brush their throat.
(1, 1, "room_close_afternoon", "Close view of the Geek's fingers brushing the silver tabby cat's white chin and throat, faint tiny vibration lines under his fingertips."),
# 227 Others purr so loudly you can hear them from across the room.
(0, 0, "cat_home", f"{cap(ORANGE)} purrs on the cream sofa with huge vibration lines, while {WOMAN} across the room by the window turns her head in surprise."),
# 228 The loudest purr on record belonged
(0, 0, "devon", f"{cap(MERLIN)} sits on the red armchair purring, big vibration lines around its throat."),
# 229 to a cat named Merlin from Devon in England.
(0, 0, "devon_outside", "Wide view of the white thatched cottage among the green hills, with smoke curling from its chimney."),
# 230 Back in 2015 his purr was measured at almost sixty eight decibels.
(0, 0, "devon", f"{cap(MEASURER)} holds a small handheld sound meter with a blank screen near {MERLIN}, which purrs on the red armchair."),
# 231 That's about as loud as two people chatting.
(0, 0, "cat_home_kitchen", f"{cap(WOMAN)} and {FRIEND} chat over cups of tea at the small wooden table."),
# 232 It's close to the hum of a dishwasher running in the kitchen.
(0, 0, "kitchen_afternoon", "A white dishwasher built in among the dark-wood cabinets is running, soft hum lines drawn around its door."),
# 233 And all of that came out of one ordinary house cat.
(0, 0, "devon", f"{cap(MERLIN)} sits calmly on the red armchair looking ordinary and pleased with itself."),
# 234 Some cats purr while they eat.
(0, 1, "kitchen_afternoon", f"The silver tabby cat eats from its white bowl on the checkered tiles, {VIB}."),
# 235 Some cats purr right through their naps.
(0, 1, "room_afternoon", "The silver tabby cat sleeps on its back on the brown sofa, paws curled, purring."),
# 236 Some start up the moment you so much as glance at them.
(1, 1, "room_afternoon", "The Geek glances sideways over his book at the silver tabby cat, which instantly starts purring with vibration lines."),
# 237 And some cats hardly ever purr at all.
(0, 0, "cat_home", f"{cap(SIAMESE)} sits quietly on the windowsill with its mouth closed, calm."),
# 238 That's completely normal as well.
(0, 0, "cat_home", f"{cap(WOMAN)} gently strokes {SIAMESE} on the cream sofa, both calm."),
# 239 A quiet cat isn't an unhappy cat.
(0, 0, "cat_home", f"{cap(SIAMESE)} rolls onto its back on the round braided rug, relaxed and content."),
# 240 Some cats just show how they feel in other ways.
(0, 0, "cat_home", f"{cap(SIAMESE)} rubs its cheek against the ankle of {WOMAN} with its tail held straight up."),
# 241 So how can you tell what your cat's purr means?
(1, 1, "room_afternoon", "The Geek sits cross-legged on the beige rug studying the silver tabby cat through a magnifying glass, a blank notepad on his knee."),
# 242 The trick is to watch the whole cat instead of only listening.
(0, 1, "room_afternoon", "Full-body view of the silver tabby cat standing on the beige rug, from its ears to its tail tip."),
# 243 A happy purr usually comes with a loose and relaxed body.
(0, 1, "room_afternoon", "The silver tabby cat lies loosely stretched out on the beige knitted throw on the brown sofa, body soft and relaxed."),
# 244 The eyes are half closed or doing that slow blink.
(0, 1, "room_close_afternoon", "Close-up of the silver tabby cat's face doing a slow blink, eyes half closed."),
# 245 The tail lies calm and still.
(0, 1, "room_close_afternoon", "Close-up of the silver tabby cat's ringed tail lying calm and still on the beige knitted throw."),
# 246 The cat might knead or rub its face against you.
(1, 1, "room_afternoon", "The silver tabby cat rubs its cheek against the Geek's hand as he sits on the brown sofa."),
# 247 That's the purr of a cat that feels completely safe.
(1, 1, "room_afternoon", "The silver tabby cat sleeps curled on the Geek's lap on the brown sofa, purring, peaceful."),
# 248 A stressed purr looks pretty different.
(0, 1, "room_evening", "The silver tabby cat stands stiffly by the kitchen doorway, tense, its ears turned sideways."),
# 249 The body is tense or hunched up tight.
(0, 1, "room_evening", "The silver tabby cat crouches hunched up tight on the beige rug, paws tucked under, body tense."),
# 250 The ears may be pulled back flat.
(0, 1, "room_close_evening", "Close-up of the silver tabby cat's head with its ears pulled back flat and its eyes wide."),
# 251 The cat might be hiding or breathing a little fast.
(0, 1, "room_evening", "The silver tabby cat peers out from behind the terracotta plant pot, breathing fast, quick motion lines at its sides."),
# 252 That purr is a cat working hard to calm itself down.
(0, 1, "room_close_evening", f"The silver tabby cat with its eyes shut tight and tense shoulders, {VIB}."),
# 253 And the hungry purr tends to come
(0, 1, "kitchen_morning", "The silver tabby cat sits on the checkered tiles purring loudly, big vibration lines around its throat."),
# 254 with a cat that is staring right at you.
(0, 1, "kitchen_morning", "Front view: the silver tabby cat stares straight out at the viewer, unblinking."),
# 255 Or staring at the food bowl instead.
(0, 1, "kitchen_morning", "The silver tabby cat stares down intensely at its empty white bowl on the checkered tiles."),
# 256 Or pacing back and forth between the two of you.
(1, 1, "kitchen_morning", "The silver tabby cat walks back and forth between the Geek's feet and its empty bowl, motion lines tracing its path, while he holds a coffee mug."),
# 257 You'll learn that one fast enough.
(1, 1, "kitchen_morning", "The Geek sighs with a deadpan face and opens the cupboard while the silver tabby cat watches."),
# 258 Trust me your cat will make sure of it.
(1, 1, "kitchen_morning", "The silver tabby cat sits on the counter staring at the Geek, who gives a weary thumbs up."),
# 259 So why does your cat purr?
(1, 1, "room_evening", "The Geek sits on the brown sofa holding the purring silver tabby cat, looking at it thoughtfully."),
# 260 Because it's the very first language it ever spoke.
(0, 0, "kitten_box", f"{cap(MOTHER)} purrs with {KITTENS} nursing at her belly."),
# 261 It started in a pile of blind kittens snuggled against a warm mother.
(0, 0, "kitten_box_close", f"{cap(KITTENS)} snuggled against the warm ginger-and-white belly of their mother."),
# 262 Because the purr is how a cat tells you that it feels safe.
(1, 1, "room_evening", "The silver tabby cat purrs on the Geek's lap on the brown sofa, both relaxed in the warm lamp light."),
# 263 Because it's also how a scared or hurting cat calms itself down.
(0, 1, "room_close_evening", "The silver tabby cat curled up tight on the beige knitted throw with its eyes closed, purring itself calm."),
# 264 Because it might even help its bones and body heal.
(0, 0, "plain", "A side-view drawing of a sleeping cat with its bones softly glowing gold. No labels or text."),
# 265 And because some clever cats have learned to use it to get breakfast.
(0, 1, "kitchen_morning", "The silver tabby cat sits beside its white bowl looking smug as dry food pours into it from a tilted cat food bag."),
# 266 A purr isn't just one message.
(0, 0, "plain", "A small cat silhouette with several different thin coloured wavy lines coming from it. No labels or text."),
# 267 It's a whole bundle of messages wrapped up in one rumble.
(0, 0, "plain", "Several thin coloured wavy lines twisting together into one thick soft wave. No labels or text."),
# 268 To read it properly you have to look at the whole cat.
(1, 1, "room_evening", "The Geek and the silver tabby cat sit facing each other on the beige rug, studying each other."),
# 269 But here's the part I like best.
(1, 1, "room_evening", "The Geek smiles a rare small smile, stroking the silver tabby cat on his lap on the brown sofa."),
# 270 Your cat once purred only for its mother in those first blind days.
(0, 0, "kitten_box", f"{cap(MOTHER)} purrs softly over {KITTENS} in the warm amber glow."),
# 271 Now it purrs for you. So soak it in the next time
(1, 1, "bedroom_morning", "The silver tabby cat lies on the Geek's chest in bed, purring, as he looks at it fondly."),
# 272 that warm little motor starts up on your chest.
(1, 1, "bedroom_close_morning", f"Close view of the silver tabby cat on the Geek's chest on the white duvet, eyes closed, {VIB}."),
# 273 That sound is the oldest way a cat knows
(1, 1, "bedroom_morning", "The Geek and the silver tabby cat slow-blink at each other in the morning sunlight."),
# 274 to tell you that you're family.
(1, 1, "bedroom_morning", "Wide view of the sunny bedroom: the Geek asleep in bed with the silver tabby cat curled on his chest, both peaceful."),
]
