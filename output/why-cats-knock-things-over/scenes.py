"""One image per segment in segments.json, in order: (geek in shot, silver tabby in shot, place, action).

Built by prompt_kit.py (YtAutomation root): every place and every character is written out in full in every prompt.
The only things a prompt may point to are the 3 attached images: the room, the Geek sheet, the cat sheet.
Other cats are never silver or grey tabbies, so they can't be mistaken for the Geek's cat.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from prompt_kit import HOME  # noqa: E402

cap = lambda s: s[0].upper() + s[1:]

# Characters and props other than the Geek and his cat, written out in full wherever they appear.
MUG = "a plain white ceramic mug of tea"
PEN = "a blue ballpoint pen"
KEYS = "a bunch of silver keys on a red keyring"
SPOON = "a shiny silver teaspoon"
REMOTE = "a black TV remote control"
PHONE = "a black smartphone"
EARRINGS = "a pair of small gold hoop earrings"
PLANT = "a small leafy houseplant in a white pot"
BOOK = "a thick hardback book with a plain dark-green cover"
CAP = "a red plastic bottle cap"
HAIRTIE = "a purple hair tie"
WAND = "a wand toy with a bunch of colourful feathers on a string"
TOY_MOUSE = "a small grey felt toy mouse"
TREAT_BALL = "a small blue plastic treat ball with holes in it"
WILDCAT = ("a sandy-brown African wildcat with faint darker stripes on its legs, long legs, a slim ringed tail with a black "
           "tip and amber eyes")
MOUSE = "a small brown field mouse"
LIZARD = "a small sandy-coloured lizard"
FOX = "a red fox with a white-tipped bushy tail"
EAGLE = "a large brown eagle with spread wings"
MOTHER = "a ginger-and-white mother cat with an orange tabby head and back, a white chest, belly and paws, and amber eyes"
KITTENS = ("three playful young kittens with their eyes open, one ginger, one black-and-white and one cream, with round "
           "bellies and stubby tails")
KITTEN = "a playful young black-and-white kitten with its eyes open, a round belly and a stubby tail"
ORANGE = "a plump orange tabby cat with amber eyes"
BLACK = "a sleek black cat with yellow-green eyes"
TUXEDO = "a black-and-white tuxedo cat with a white chest, white paws, a white chin and green eyes"
OLD_CAT = "an elderly thin black cat with grey hairs around its muzzle and cloudy amber eyes"
TEST_CAT = "a cream-and-white cat with amber eyes"
RESEARCHER = "a Japanese researcher with short black hair and thin glasses in a light blue shirt"
CONTAINER = "a small closed opaque white plastic container"
TODDLER = "a toddler with curly brown hair in a yellow t-shirt"
VET = "a friendly female vet with dark curly hair tied back, wearing a blue scrub top"

# This video's own places. False = not the attached room.
PLACES = dict(HOME, **{
    "desert": (False, "Dry desert scrubland in Africa in warm late-afternoon light: sandy ground, scattered rocks, low thorny "
               "bushes, clumps of dry grass, and pale hills on the horizon under a hazy sky. No buildings, roads or fences."),
    "desert_close": (False, "A close-up at ground level in dry desert scrubland: sandy earth, small stones and dry grass stems "
                     "in warm low light, the scrubland softly out of focus behind. No buildings, roads or fences."),
    "kitten_barn": (False, "A sunny corner of an old wooden barn: weathered plank walls, soft golden straw on the floor, a "
                    "wooden crate, and a shaft of sunlight from a high window."),
    "lab_kyoto": (False, "A small bright research room: plain white walls, a low grey carpeted floor, a small wooden table, and "
                  "a video camera on a tripod in the corner. Soft even daylight."),
    "family_kitchen": (False, "A bright family kitchen with pale blue walls, white cabinets, a wooden floor, and a white "
                       "wooden high chair beside a round table. Morning sunlight through a window."),
    "woodland": (False, "A quiet woodland in soft daylight: a big old oak tree with a thick low branch, green ferns and "
                 "grass on the ground, and more trees fading into the distance. No buildings, roads or fences."),
    "clinic": (False, "A bright clean vet clinic exam room: white walls, a stainless-steel exam table, pale blue cabinets and "
               "a sink."),
    "laptop_screen": (False, "A close-up of a silver laptop screen on a wooden desk in a dim room, the screen filling most of "
                      "the frame and glowing."),
    "plain_dark": (False, "There is no room and no landscape: a plain calm dark-blue background fills the frame."),
})

SCENES = [
# 1 Why does your cat knock things off the table?
(1, 1, "room_evening", f"The silver tabby cat sits on the coffee table with one white paw pushing {MUG} toward the edge, staring at the Geek, who sits on the brown sofa frozen mid-reach with a flat deadpan look."),
# 2 You watch it happen and it almost looks planned.
(1, 1, "room_evening", "The Geek sits on the brown sofa narrowing his eyes suspiciously at the silver tabby cat, which sits calmly on the coffee table next to the edge."),
# 3 One paw reaches out and the cup creeps toward the edge.
(0, 1, "room_close_evening", f"Close-up of the silver tabby cat's white paw slowly pushing {MUG} across the wooden coffee table toward the edge."),
# 4 So what on earth is going on inside that little head?
(1, 1, "room_evening", "The Geek leans in close to stare into the silver tabby cat's face with a puzzled deadpan look, while the cat stares back calmly from the coffee table."),
# 5 It's late in the evening
(1, 0, "room_evening", "Wide view of the room at night, the Geek walking in from the kitchen doorway."),
# 6 and you've just made yourself a cup of tea.
(1, 0, "kitchen_afternoon", f"The Geek pours hot water from the white electric kettle into {MUG} on the beige countertop."),
# 7 You set it down on the coffee table
(1, 0, "room_evening", f"The Geek bends down and sets {MUG} on the wooden coffee table in front of the brown sofa."),
# 8 and turn away for maybe one second.
(1, 0, "room_evening", f"The Geek turns his back to the coffee table to reach for a book on the bookshelf, {MUG} left behind on the table."),
# 9 When you look back the cat is sitting right beside the mug.
(1, 1, "room_evening", f"The Geek looks back over his shoulder to find the silver tabby cat sitting on the coffee table right beside {MUG}."),
# 10 It isn't drinking the tea and it isn't even sniffing it.
(0, 1, "room_close_evening", f"The silver tabby cat sits upright next to {MUG} on the coffee table, ignoring it completely, its nose pointed away."),
# 11 It's just looking at you. Then a single paw lifts up
(0, 1, "room_close_evening", "Front view of the silver tabby cat on the coffee table staring straight out at the viewer, one white front paw slowly lifting."),
# 12 and rests against the side of the mug.
(0, 1, "room_close_evening", f"Close-up of the silver tabby cat's white paw resting gently against the side of {MUG}."),
# 13 Slowly the mug begins to slide toward the edge.
(0, 1, "room_close_evening", f"{cap(MUG)} slides toward the edge of the wooden coffee table under the silver tabby cat's white paw, small motion lines behind it."),
# 14 The cat keeps its eyes locked on yours the entire time.
(1, 1, "room_evening", "The silver tabby cat and the Geek stare into each other's eyes, the cat's paw still on the mug at the table edge, the Geek frozen with one hand raised."),
# 15 And then over the side it goes. If you share a home
(0, 1, "room_close_evening", f"{cap(MUG)} tips over the edge of the coffee table in mid-air, tea splashing out, while the silver tabby cat watches it fall."),
# 16 with a cat you've almost certainly seen some version of this.
(1, 1, "room_evening", "The Geek kneels on the beige rug mopping up spilled tea with a towel while the silver tabby cat watches calmly from the coffee table."),
# 17 Pens roll off desks and keys vanish under the sofa.
(0, 1, "room_afternoon", f"The silver tabby cat swats {KEYS} off the arm of the brown sofa, the keys sliding toward the gap under the sofa."),
# 18 Earrings go missing from the bedside table.
(0, 1, "bedroom_morning", f"The silver tabby cat on the wooden nightstand nudges {EARRINGS} toward the edge with one white paw."),
# 19 Houseplants end up on the floor with soil sprayed everywhere.
(0, 1, "room_afternoon", f"{cap(PLANT)} lies tipped over on the honey-brown floorboards with soil spilled everywhere, the silver tabby cat sitting on the windowsill above looking innocent."),
# 20 The internet is stuffed with videos of cats doing exactly this.
(0, 0, "laptop_screen", f"The laptop screen shows a grid of small video thumbnails of different cats pushing things off tables: {ORANGE}, {BLACK} and {TUXEDO}. No text, letters or numbers on the screen."),
# 21 And in nearly every one of them
(0, 0, "laptop_screen", f"The laptop screen shows a single video of {ORANGE} pushing a glass off a kitchen counter. No text, letters or numbers on the screen."),
# 22 the cat looks completely calm about the whole thing.
(0, 0, "laptop_screen", f"The laptop screen shows a close video frame of {BLACK} sitting perfectly calm beside a fallen glass on a floor. No text, letters or numbers on the screen."),
# 23 So is your cat a tiny furry villain doing it on purpose?
(1, 1, "room_evening", "The silver tabby cat sits on top of the bookshelf in shadow, lit from below by the lamp like a movie villain, looking down at the Geek, who looks up with a deadpan face."),
# 24 Or is something else going on here?
(1, 1, "room_evening", "The Geek sits on the beige rug rubbing his chin thoughtfully, looking at the silver tabby cat on the coffee table."),
# 25 The answer turns out to be a few things tangled together.
(1, 1, "room_afternoon", "The Geek sits on the brown sofa untangling a big ball of yarn, while the silver tabby cat bats at the loose end."),
# 26 Some of it is very old
(0, 0, "desert", f"{cap(WILDCAT)} stands on a rock looking out over the scrubland."),
# 27 and some of it is really about you.
(1, 1, "room_evening", "The Geek points at himself with a surprised deadpan look while the silver tabby cat stares at him from the coffee table."),
# 28 Let's start with the oldest part.
(0, 0, "desert", "Wide view of the desert scrubland at dusk, the sun low over the pale hills."),
# 29 Your house cat comes from a small wild cat that lived
(0, 0, "desert", f"{cap(WILDCAT)} walks through the dry grass between the thorny bushes."),
# 30 in the deserts and grasslands of Africa and the Middle East.
(0, 0, "plain", "A simple map in muted colours of Africa and the Middle East with soft sandy-coloured patches showing deserts and grasslands. No labels or text."),
# 31 That wild cat lived on mice and birds and lizards and bugs.
(0, 0, "desert", f"{cap(WILDCAT)} crouches low, watching {MOUSE}, a small bird and {LIZARD} on the sandy ground ahead."),
# 32 To stay alive it had to hunt an awful lot.
(0, 0, "desert", f"{cap(WILDCAT)} stalks low through the dry grass, eyes focused, body tense."),
# 33 A small cat can't catch one big meal
(0, 0, "desert", f"{cap(WILDCAT)} looks warily at a huge zebra grazing nearby, far too big to catch."),
# 34 and then rest for a week.
(0, 0, "desert", f"A big male lion with a thick golden-brown mane sleeps sprawled under a thorny bush, full and lazy."),
# 35 It needs lots of little meals every single day.
(0, 0, "desert_close", f"{cap(WILDCAT)} pounces on {MOUSE} in the dry grass."),
# 36 So it spends a huge chunk of its life looking
(0, 0, "desert", f"{cap(WILDCAT)} sits on a rock scanning the scrubland, ears pricked."),
# 37 for things that move. And here's the thing about small prey.
(0, 0, "desert_close", f"Close-up of {MOUSE} frozen still beside a stone in the sandy earth."),
# 38 Sometimes a mouse plays dead.
(0, 0, "desert_close", f"{cap(MOUSE)} lies flat and still on its side on the sand, eyes shut, pretending to be dead."),
# 39 Sometimes a lizard freezes perfectly still against a rock.
(0, 0, "desert_close", f"{cap(LIZARD)} freezes motionless against a sandy rock, blending in."),
# 40 So a hunting cat picks up a very handy trick.
(0, 0, "desert", f"{cap(WILDCAT)} creeps toward a small still shape in the sand, one paw raised."),
# 41 When it finds something
(0, 0, "desert_close", f"{cap(WILDCAT)} sniffs at {MOUSE} lying still on the sand."),
# 42 that might be alive it gives the thing a poke with its paw.
(0, 0, "desert_close", f"Close-up of the paw of {WILDCAT} giving a gentle poke to {MOUSE} lying still on the sand."),
# 43 If it runs then dinner is on.
(0, 0, "desert_close", f"{cap(MOUSE)} darts away across the sand with {WILDCAT} pouncing after it."),
# 44 If it doesn't move then the cat pokes it again just
(0, 0, "desert_close", f"{cap(WILDCAT)} pokes {LIZARD} a second time with its paw, head tilted."),
# 45 to be sure. That little paw tap is
(0, 0, "desert_close", f"{cap(WILDCAT)} watches {LIZARD} closely with its paw hovering just above it."),
# 46 one of the most basic moves a cat owns.
(0, 1, "room_afternoon", "The silver tabby cat taps a small crumpled paper ball on the beige rug with one white paw."),
# 47 You can spot it in kittens long before they ever catch anything real.
(0, 0, "kitten_barn", f"{cap(KITTENS)} tumble on the straw, batting at each other with their paws."),
# 48 They bat at bits of string
(0, 0, "kitten_barn", f"{cap(KITTEN)} bats at a dangling piece of string with both front paws."),
# 49 and dry leaves and their mother's twitching tail.
(0, 0, "kitten_barn", f"{cap(KITTENS)} pounce at the twitching tail of {MOTHER}, who lies calmly on the straw, while a dry leaf drifts past."),
# 50 They swat at their brothers and sisters until somebody squeaks.
(0, 0, "kitten_barn", f"{cap(KITTENS)} wrestle on the straw, one swatting another on the head."),
# 51 All of that is practice for the hunting they'll need to do later.
(0, 0, "kitten_barn", f"{cap(KITTEN)} crouches in a tiny hunting pose, wiggling its rear before a pounce."),
# 52 The poke and the swat are wired deep into every single cat.
(0, 1, "room_afternoon", "The silver tabby cat crouches on the beige rug in a perfect hunting pose, one white paw raised mid-swat."),
# 53 Now picture your cat up on the kitchen counter.
(0, 1, "kitchen_afternoon", "The silver tabby cat walks along the beige countertop past the white electric kettle."),
# 54 It comes across a small object it has never seen before.
(0, 1, "kitchen_afternoon", f"The silver tabby cat stops on the countertop and sniffs at {CAP}."),
# 55 Maybe it's a bottle cap or a hair tie or your car keys.
(0, 0, "kitchen_afternoon", f"Close view of the beige countertop with {CAP}, {HAIRTIE} and {KEYS} lying on it."),
# 56 The hunter side of its brain asks one very simple question.
(0, 1, "kitchen_afternoon", f"The silver tabby cat crouches on the countertop staring intently at {CAP}, ears forward, pupils wide."),
# 57 Could this thing possibly be alive?
(0, 1, "kitchen_afternoon", f"Close view of the silver tabby cat's face tilted, studying {CAP} up close."),
# 58 And the quickest way to find out is to give it a tap.
(0, 1, "kitchen_afternoon", f"The silver tabby cat taps {CAP} with one white paw on the countertop."),
# 59 The object slides a little bit. Now that is pretty interesting.
(0, 1, "kitchen_afternoon", f"{cap(CAP)} slides a little across the countertop, and the silver tabby cat's ears perk up."),
# 60 So the cat gives it another tap.
(0, 1, "kitchen_afternoon", f"The silver tabby cat swats {CAP} a second time, a little harder."),
# 61 It slides a bit further and then it drops off the edge.
(0, 1, "kitchen_afternoon", f"{cap(CAP)} drops off the edge of the countertop in mid-air while the silver tabby cat leans over to watch."),
# 62 That's even more interesting to a cat.
(0, 1, "kitchen_afternoon", "The silver tabby cat peers over the edge of the countertop with huge round pupils, fascinated."),
# 63 Something moved and then it went somewhere new.
(0, 0, "kitchen_afternoon", f"{cap(CAP)} lies on the cream-and-grey checkered floor tiles below the counter."),
# 64 For a hunter that's about as exciting as an ordinary afternoon gets.
(0, 1, "kitchen_afternoon", "The silver tabby cat leaps down from the countertop toward the floor, eager and alert."),
# 65 There's another reason cats lean so hard on their paws.
(0, 1, "room_close_afternoon", "Close-up of the silver tabby cat's white front paws resting on the beige knitted throw."),
# 66 Cats don't actually see very well up close.
(0, 1, "room_close_afternoon", f"Close-up of the silver tabby cat looking down at {TOY_MOUSE} right under its nose, the toy drawn slightly blurry."),
# 67 Their eyes are built for spotting movement across a room or a field.
(0, 1, "room_afternoon", "The silver tabby cat sits on the windowsill staring sharply at a small bird fluttering outside the window."),
# 68 Things sitting right under their nose tend to look a bit blurry.
(0, 1, "room_close_afternoon", f"Point of view from the cat: a soft blurry {TOY_MOUSE} right in front, the silver tabby cat's white paws sharp below it."),
# 69 So for close up work a cat leans on its other senses instead.
(0, 1, "room_close_afternoon", f"The silver tabby cat lowers its whiskers forward to feel {TOY_MOUSE} on the beige knitted throw."),
# 70 Their paws are packed with sensitive nerves.
(0, 0, "plain", "A close drawing of the underside of a cat's white paw with pink toe pads and soft glowing lines showing nerves inside. No labels or text."),
# 71 Their whiskers can pick up tiny changes in the air around them.
(0, 1, "room_close_afternoon", "Close-up of the silver tabby cat's face, its whiskers spread wide with faint soft air-current lines flowing around them."),
# 72 Cats even have a few stiff whiskers
(0, 0, "plain", "A side-view drawing of a cat's front leg with a few stiff whiskers sticking out from the back of the wrist, softly highlighted. No labels or text."),
# 73 on the backs of their front legs.
(0, 1, "room_close_afternoon", "Close-up of the silver tabby cat's front leg showing a few short stiff whiskers on the back of its wrist."),
# 74 Those help them feel what's going on right under their own chin.
(0, 1, "room_close_afternoon", f"The silver tabby cat holds {TOY_MOUSE} between its front paws right under its chin."),
# 75 So when your cat pats at something
(1, 1, "room_evening", f"The silver tabby cat pats at {REMOTE} on the coffee table while the Geek watches from the brown sofa."),
# 76 on the table it's partly just getting a better look.
(0, 1, "room_close_evening", f"Close-up of the silver tabby cat's white paw resting on {REMOTE}, the cat leaning in to look."),
# 77 It's feeling the thing out to learn what it actually is.
(0, 1, "room_close_evening", f"The silver tabby cat turns {REMOTE} over with its paw, studying it."),
# 78 There's also some evidence that cats are trying
(1, 1, "room_evening", "The Geek holds up a finger with a deadpan look while the silver tabby cat sits beside him on the brown sofa."),
# 79 to work out how the world behaves.
(0, 1, "room_evening", f"The silver tabby cat watches {PEN} rolling slowly across the coffee table, head tilted like a scientist."),
# 80 In 2016 a team of researchers at Kyoto University
(0, 0, "lab_kyoto", f"{cap(RESEARCHER)} kneels by the small wooden table holding {CONTAINER}, the video camera on its tripod pointed at the table."),
# 81 in Japan ran a clever little test.
(0, 0, "lab_kyoto", f"{cap(RESEARCHER)} sits facing {TEST_CAT}, which sits on the grey carpet watching curiously."),
# 82 They shook a closed container in front of cats.
(0, 0, "lab_kyoto", f"{cap(RESEARCHER)} shakes {CONTAINER} in front of {TEST_CAT}, small motion lines around the container."),
# 83 Sometimes the container rattled like there was something inside.
(0, 0, "lab_kyoto", f"{cap(CONTAINER)} being shaken with small jagged rattle lines around it, {TEST_CAT} listening with ears forward."),
# 84 Sometimes it made no sound at all.
(0, 0, "lab_kyoto", f"{cap(RESEARCHER)} shakes {CONTAINER} with no sound lines at all, while {TEST_CAT} watches with its ears relaxed."),
# 85 Then they tipped it over.
(0, 0, "lab_kyoto", f"{cap(RESEARCHER)} tips {CONTAINER} upside down above the table while {TEST_CAT} watches."),
# 86 Sometimes an object fell out and sometimes nothing came out at all.
(0, 0, "lab_kyoto", f"A small red ball drops out of the tipped {CONTAINER} onto the table, {TEST_CAT} watching closely."),
# 87 The cats stared longer whenever the result didn't match the sound.
(0, 0, "lab_kyoto", f"{cap(TEST_CAT)} stares hard at the empty upturned container with wide eyes, puzzled."),
# 88 A rattling container that dropped nothing seemed to puzzle them.
(0, 0, "lab_kyoto", f"{cap(TEST_CAT)} tilts its head at {CONTAINER} held upside down with nothing falling out."),
# 89 A silent one that suddenly dropped something puzzled them too.
(0, 0, "lab_kyoto", f"{cap(TEST_CAT)} leans back in surprise as a small red ball drops from {CONTAINER}."),
# 90 The researchers took this as a sign
(0, 0, "lab_kyoto", f"{cap(RESEARCHER)} smiles and nods while making notes on a clipboard with no readable writing."),
# 91 that cats understand some cause and effect.
(0, 0, "plain", "A simple drawing of a shaking container with rattle lines, an arrow, and then a small ball falling out. No labels or text."),
# 92 They seem to carry a rough idea
(0, 1, "room_afternoon", "The silver tabby cat sits on the coffee table looking thoughtful, a faint cloud-shaped bubble above its head showing a little shaking box."),
# 93 that a rattle means something is inside. And they seem to expect
(0, 1, "room_afternoon", "The silver tabby cat paws at a rattling closed cardboard box on the beige rug, ears forward."),
# 94 that things fall down when nothing holds them up.
(0, 0, "plain", "A simple drawing of a ball falling straight down from a table edge with a dotted line showing its path. No labels or text."),
# 95 So maybe your cat is running little experiments of its own.
(0, 1, "office_afternoon", "The silver tabby cat sits on the wooden desk wearing a tiny pair of safety goggles like a scientist, beside a row of small objects."),
# 96 What happens if I push this pen?
(0, 1, "office_afternoon", f"The silver tabby cat pushes {PEN} toward the edge of the wooden desk with one white paw."),
# 97 The pen falls right off. What about this shiny spoon?
(0, 1, "office_afternoon", f"{cap(PEN)} falls off the desk while the silver tabby cat already eyes {SPOON} beside the laptop."),
# 98 It falls too and makes a lovely clatter.
(0, 0, "office_afternoon", f"{cap(SPOON)} bounces on the honey-brown floorboards with small bright clatter lines around it."),
# 99 Does the remote control fall as well?
(0, 1, "room_afternoon", f"The silver tabby cat pushes {REMOTE} toward the edge of the coffee table."),
# 100 It certainly does and it bounces too.
(0, 0, "room_afternoon", f"{cap(REMOTE)} bounces on the beige rug, small motion lines showing the bounce."),
# 101 Every test comes back with the same answer
(0, 1, "room_afternoon", f"The silver tabby cat sits on the coffee table looking down at {PEN}, {SPOON} and {REMOTE} scattered on the rug below."),
# 102 and somehow it never seems to get old.
(0, 1, "room_afternoon", f"The silver tabby cat pushes {BOOK} off the coffee table with a satisfied look."),
# 103 And honestly the noise might be half the fun.
(0, 1, "room_close_afternoon", "Close-up of the silver tabby cat's ears swivelled forward, listening with delight."),
# 104 A pen hitting a wooden floor makes a sharp little click.
(0, 0, "room_close_afternoon", f"Close-up of {PEN} hitting the honey-brown floorboards with a sharp little burst of sound lines."),
# 105 A spoon makes a bright ringing clatter.
(0, 0, "kitchen_afternoon", f"{cap(SPOON)} rings as it hits the checkered floor tiles, bright ringing lines around it."),
# 106 A set of keys makes a great jangly crash.
(0, 0, "room_close_afternoon", f"{cap(KEYS)} crash onto the honey-brown floorboards with jagged jangle lines."),
# 107 To an animal with ears as good as a cat's
(0, 1, "room_close_afternoon", "Close-up of the silver tabby cat's large triangular ears with pink insides, both turned toward a sound."),
# 108 that's a whole lot of interesting information.
(0, 1, "room_afternoon", "The silver tabby cat sits on the coffee table, eyes bright, small soft sound waves coming toward its ears from things on the floor."),
# 109 It's a bit like a toddler dropping a spoon
(0, 0, "family_kitchen", f"{cap(TODDLER)} sits in the white high chair, dropping {SPOON} over the side with a delighted face."),
# 110 from a high chair over and over.
(0, 0, "family_kitchen", f"{cap(TODDLER)} in the white high chair leans over to look at a pile of spoons on the wooden floor below, laughing."),
# 111 The sound is part of the reward.
(0, 1, "room_afternoon", "The silver tabby cat sits by the coffee table edge with its eyes half closed in satisfaction, a fallen spoon on the rug below."),
# 112 But the hunting instinct doesn't explain the most famous part.
(1, 1, "room_evening", "The Geek sits on the brown sofa with a flat deadpan look as the silver tabby cat on the coffee table locks eyes with him."),
# 113 It doesn't explain the stare. Why does the cat look straight at you
(0, 1, "room_close_evening", "Extreme close-up of the silver tabby cat's pale greenish-yellow eyes staring straight out at the viewer."),
# 114 while it nudges the mug toward the edge?
(1, 1, "room_evening", f"The silver tabby cat nudges {MUG} toward the coffee table edge while staring at the Geek, who points at it with a warning look."),
# 115 This is the part that's really all about you.
(1, 0, "room_evening", "The Geek sits alone on the brown sofa pointing at himself with a resigned deadpan face."),
# 116 Cats are very quick to learn what gets a reaction.
(0, 1, "room_evening", "The silver tabby cat sits on top of the bookshelf, watching the room below with a clever look."),
# 117 Think about what happens the first time
(1, 1, "room_afternoon", "The silver tabby cat walks along a shelf of the bookshelf while the Geek reads on the brown sofa, unaware."),
# 118 a cat knocks something off a shelf.
(0, 1, "room_afternoon", "A small ceramic vase falls from the bookshelf in mid-air, the silver tabby cat peering down after it."),
# 119 You jump up off the sofa.
(1, 0, "room_afternoon", "The Geek leaps up from the brown sofa in alarm, his book flying out of his hands."),
# 120 You call its name in a loud voice.
(1, 1, "room_afternoon", "The Geek shouts toward the bookshelf with his hands cupped around his mouth, while the silver tabby cat looks down from the top shelf."),
# 121 You rush over and pick the thing up.
(1, 0, "room_afternoon", "The Geek crouches by the bookshelf picking up the small ceramic vase from the floorboards."),
# 122 Maybe you scoop up the cat while you're at it.
(1, 1, "room_afternoon", "The Geek lifts the silver tabby cat down off the bookshelf in both arms."),
# 123 For a few seconds you're giving it your complete and total attention.
(1, 1, "room_afternoon", "The Geek holds the silver tabby cat at face level, staring into its eyes, and the cat looks back looking very pleased."),
# 124 From the cat's side of things that's a great result.
(0, 1, "room_afternoon", "The silver tabby cat sits on the beige rug with its tail up and a satisfied look."),
# 125 It was bored and now you're up and moving and talking.
(1, 1, "room_afternoon", "The Geek paces and gestures as he talks while the silver tabby cat watches him from the rug, ears forward and interested."),
# 126 It doesn't really matter to the cat that you're annoyed.
(1, 1, "room_afternoon", "The Geek stands with his arms crossed and an annoyed deadpan face, while the silver tabby cat rubs happily against his legs."),
# 127 Any attention at all still counts as attention.
(1, 1, "room_afternoon", "The Geek wags a finger at the silver tabby cat, which gazes up at him delighted."),
# 128 So the cat files away a simple
(0, 1, "room_afternoon", "The silver tabby cat sits on the coffee table with a thoughtful look, a faint cloud-shaped bubble above it showing a falling vase and a person running toward it."),
# 129 lesson about pushing things off the table.
(0, 1, "room_close_afternoon", f"Close-up of the silver tabby cat's white paw resting on {BOOK} near the edge of the coffee table."),
# 130 It makes the human come running every time.
(1, 1, "room_afternoon", "The Geek runs across the room toward the coffee table while the silver tabby cat sits next to a fallen book on the rug."),
# 131 And the next time it wants you it knows exactly
(0, 1, "room_evening", f"The silver tabby cat sits on the coffee table eyeing {MUG} with a knowing look."),
# 132 which button to press.
(0, 1, "room_close_evening", f"Close-up of the silver tabby cat's paw pressing on {REMOTE} like a button."),
# 133 That's why so many cats do this when they want something specific.
(1, 1, "kitchen_morning", "The silver tabby cat sits next to its empty white food bowl, staring up at the Geek in the kitchen."),
# 134 It happens a lot around mealtimes.
(0, 1, "kitchen_morning", "The silver tabby cat sits beside its empty white bowl on the checkered tiles, looking at the clock on the wall."),
# 135 The cat strolls along the dresser in the early morning.
(0, 1, "bedroom_morning", "The silver tabby cat strolls along the top of the wooden chest of drawers in the early morning light."),
# 136 It looks over at you lying in bed.
(1, 1, "bedroom_morning", "The silver tabby cat looks over from the chest of drawers at the Geek sleeping in bed under the white duvet."),
# 137 Then it sends your phone sliding onto the floor.
(0, 1, "bedroom_morning", f"The silver tabby cat swats {PHONE} off the wooden nightstand, the phone sliding through the air toward the rug."),
# 138 That's not some random accident. That's a cat that has worked out how
(1, 1, "bedroom_morning", "The Geek sits up in bed with messy hair and a flat deadpan look at the silver tabby cat, which sits proudly on the nightstand."),
# 139 to get you out of bed and into the kitchen.
(1, 1, "kitchen_morning", "The Geek shuffles sleepily into the kitchen in his green hoodie, the silver tabby cat trotting ahead with its tail high."),
# 140 It also happens when you're busy with something else.
(1, 0, "office_afternoon", "The Geek sits at the wooden desk typing on the silver laptop, focused."),
# 141 Have you noticed that cats love
(1, 1, "office_afternoon", "The silver tabby cat jumps up onto the wooden desk beside the Geek as he works."),
# 142 to clear your desk while you're working?
(1, 1, "office_afternoon", f"The silver tabby cat pushes {PEN} and a notebook off the desk while the Geek keeps typing."),
# 143 You're staring at a screen and you're ignoring them.
(1, 1, "office_afternoon", "The Geek stares at the laptop screen ignoring the silver tabby cat, which sits right beside it staring at him."),
# 144 So they stroll across the keyboard or push your pen off the edge.
(1, 1, "office_afternoon", "The silver tabby cat walks right across the laptop keyboard in front of the Geek."),
# 145 Suddenly you're looking at them again.
(1, 1, "office_afternoon", "The Geek turns from the laptop to look at the silver tabby cat, which now sits in front of the screen."),
# 146 As far as the cat is concerned that worked perfectly.
(1, 1, "office_afternoon", "The silver tabby cat sits on the laptop keyboard looking smug while the Geek strokes its back with a resigned deadpan face."),
# 147 A lot of experts also point to plain old boredom.
(0, 1, "room_afternoon", "The silver tabby cat lies flat on the beige rug with a bored face, chin on its paws."),
# 148 An indoor cat has a hunter's body and a hunter's brain.
(0, 1, "room_afternoon", "The silver tabby cat crouches on the brown sofa's backrest in a hunting pose, muscles tense."),
# 149 But plenty of indoor cats have almost nothing to hunt.
(0, 1, "room_afternoon", "The silver tabby cat looks around the tidy empty room with nothing moving, ears down."),
# 150 They sleep and eat and stare out of the window.
(0, 1, "room_afternoon", "The silver tabby cat sits on the windowsill staring out at the street."),
# 151 Knocking things over is fun
(0, 1, "room_afternoon", f"The silver tabby cat bats {PEN} off the coffee table with a playful look."),
# 152 and it uses every one of those hunting moves.
(0, 1, "room_afternoon", "The silver tabby cat leaps off the coffee table after a falling pen, body stretched in mid-pounce."),
# 153 If a cat doesn't get enough play
(0, 1, "room_afternoon", "The silver tabby cat sits next to a basket of untouched toys looking bored."),
# 154 it will happily invent its own games.
(0, 1, "room_afternoon", f"The silver tabby cat chases {HAIRTIE} across the honey-brown floorboards."),
# 155 And your belongings make very convenient toys.
(0, 1, "room_afternoon", f"The silver tabby cat plays on the beige rug among {KEYS}, a sock and {PEN}."),
# 156 Young cats tend to do this more than old ones.
(0, 0, "plain", f"Side by side: {KITTEN} leaping energetically on the left, and {OLD_CAT} sitting calmly on the right. No labels or text."),
# 157 A kitten or a young adult cat has a ridiculous amount of energy.
(0, 0, "kitten_barn", f"{cap(KITTEN)} races across the straw at full speed, ears back."),
# 158 A senior cat usually prefers a sunny windowsill and a long nap.
(0, 0, "plain", f"{cap(OLD_CAT)} sleeps curled in a soft patch of sunlight on a cushion. No labels or text."),
# 159 So if your young cat is clearing every shelf
(0, 1, "room_afternoon", "The silver tabby cat walks along a shelf of the bookshelf, books tipping over behind it."),
# 160 in the house it might simply need more to do.
(1, 1, "room_afternoon", "The Geek looks at a row of tipped-over books on the bookshelf, then at the silver tabby cat, with a deadpan face."),
# 161 Sometimes the reason is even simpler than that.
(1, 0, "room_afternoon", "The Geek shrugs with a deadpan face, standing beside the coffee table."),
# 162 The cat wants to be exactly where the object is.
(0, 1, "room_afternoon", f"The silver tabby cat eyes the exact spot on the coffee table where {BOOK} sits."),
# 163 Cats love lying on tables and shelves and desks. If your book is
(0, 1, "room_afternoon", f"The silver tabby cat steps onto the coffee table next to {BOOK}."),
# 164 in the way the cat may just shove it aside to make room.
(0, 1, "room_afternoon", f"The silver tabby cat shoves {BOOK} aside with its body to lie down in its place."),
# 165 In that case the falling part isn't the point at all.
(0, 1, "room_afternoon", f"The silver tabby cat lies comfortably on the coffee table while {BOOK} lies forgotten on the rug."),
# 166 It's more like tidying up in a very cat sort of way.
(0, 1, "room_afternoon", "The silver tabby cat stretches out on the now-empty coffee table, looking satisfied with its work."),
# 167 And there's a good reason your cat wants
(0, 1, "room_afternoon", "The silver tabby cat looks up longingly at the top of the tall bookshelf."),
# 168 to be up there in the first place.
(0, 1, "room_afternoon", "The silver tabby cat sits on top of the tall bookshelf, surveying the room below."),
# 169 Cats love high places.
(0, 1, "room_afternoon", "Low angle looking up at the silver tabby cat perched high on top of the bookshelf."),
# 170 Out in the wild a small cat is a hunter
(0, 0, "desert", f"{cap(WILDCAT)} stalks through the dry grass toward {MOUSE}."),
# 171 but it's also somebody else's prey.
(0, 0, "desert", f"{cap(WILDCAT)} freezes and looks up nervously at a large shadow passing over the grass."),
# 172 Foxes and eagles and bigger cats would all happily eat it.
(0, 0, "woodland", f"{cap(FOX)} prowls on the ground while {EAGLE} circles above the trees."),
# 173 So a high perch is a safe perch.
(0, 0, "woodland", f"{cap(WILDCAT)} rests safely on the thick low branch of the oak tree."),
# 174 From up there a cat can see everything coming
(0, 0, "woodland", f"{cap(WILDCAT)} looks down from the oak branch at {FOX} passing on the ground below."),
# 175 and nothing can sneak up on it. Your kitchen counter
(0, 1, "kitchen_afternoon", "The silver tabby cat sits high on top of the white fridge, looking down over the kitchen."),
# 176 and your bookshelf are the living room version of a tree branch.
(0, 1, "room_afternoon", "The silver tabby cat lies stretched along the top of the tall bookshelf like a leopard on a branch."),
# 177 So the cat climbs up to its lookout spot.
(0, 1, "room_afternoon", "The silver tabby cat leaps from the brown sofa's backrest up to a shelf of the bookshelf."),
# 178 And anything sitting on the lookout spot is fair game.
(0, 1, "room_afternoon", "The silver tabby cat on a bookshelf shelf eyes a small ceramic ornament beside it, one paw raised."),
# 179 So how do you stop it?
(1, 1, "room_evening", "The Geek sits on the beige rug surrounded by fallen objects, looking at the silver tabby cat with a tired deadpan face."),
# 180 Or at least how do you make it happen a little less?
(1, 1, "room_evening", "The Geek holds up his thumb and finger a small distance apart toward the silver tabby cat."),
# 181 The first rule is not to punish your cat for it.
(1, 1, "room_evening", "The Geek puts down a spray bottle on the coffee table and shakes his head, while the silver tabby cat watches."),
# 182 Yelling at a cat or spraying it
(1, 1, "room_evening", "The Geek shouting with his arms raised at the silver tabby cat, which flattens its ears, the scene drawn with a big red diagonal line across it. No labels or text."),
# 183 with water doesn't teach it that knocking things over is wrong.
(0, 1, "room_evening", "The silver tabby cat shakes water drops off its fur with an offended look."),
# 184 It just teaches the cat that you can be scary.
(1, 1, "room_evening", "The silver tabby cat hides behind the brown sofa peeking out warily at the Geek."),
# 185 And in some cases the yelling was the reward the cat was
(1, 1, "room_evening", "The Geek yells while the silver tabby cat sits in front of him looking delighted by all the attention."),
# 186 after anyway. The easiest fix is also the most boring one.
(1, 0, "room_afternoon", "The Geek holds a cardboard box, packing small objects off the shelves."),
# 187 Put the precious stuff away.
(1, 0, "room_afternoon", "The Geek places a small ceramic vase inside a cabinet and closes the door."),
# 188 Keep glasses and mugs well back from the edge of the table.
(1, 0, "room_afternoon", f"The Geek slides {MUG} to the middle of the coffee table, far from the edge."),
# 189 Tuck anything breakable inside a cabinet. If there's nothing fragile
(1, 0, "kitchen_afternoon", "The Geek places glasses into a dark-wood cabinet above the counter."),
# 190 to knock over then a knocked over object is no big deal.
(0, 1, "room_afternoon", f"The silver tabby cat knocks {TOY_MOUSE} off the coffee table, and nothing breaks."),
# 191 Some people use a little museum putty
(1, 0, "room_afternoon", "The Geek presses a small blob of putty under a ceramic ornament on a shelf."),
# 192 to stick ornaments down so they can't budge.
(1, 1, "room_afternoon", "The silver tabby cat pushes hard at a ceramic ornament stuck firmly to the shelf, while the Geek watches with a tiny smug look."),
# 193 The second fix is to give your cat a better hunt.
(1, 1, "room_afternoon", f"The Geek holds up {WAND} while the silver tabby cat stares at the feathers."),
# 194 Play with it every day using a wand toy
(1, 1, "room_afternoon", f"The Geek waves {WAND} across the beige rug while the silver tabby cat crouches to pounce."),
# 195 with feathers or a toy mouse on a string.
(1, 1, "room_afternoon", f"The Geek drags {TOY_MOUSE} on a string across the floorboards while the silver tabby cat chases it."),
# 196 Let it stalk and chase and pounce.
(0, 1, "room_afternoon", "The silver tabby cat leaps through the air toward a bunch of colourful feathers on a string."),
# 197 Let it catch the toy at the end
(0, 1, "room_afternoon", f"The silver tabby cat catches {TOY_MOUSE} between its front paws on the beige rug."),
# 198 so it feels like a real win.
(0, 1, "room_afternoon", f"The silver tabby cat walks proudly with {TOY_MOUSE} in its mouth, tail high."),
# 199 Plenty of cat experts suggest playing right before a meal.
(1, 1, "kitchen_afternoon", f"The Geek plays with {WAND} with the silver tabby cat in the kitchen, the white food bowl waiting nearby."),
# 200 That way the cat gets to hunt
(0, 1, "kitchen_afternoon", "The silver tabby cat pounces on a bunch of colourful feathers on the checkered tiles."),
# 201 and then eat just like a wild cat would.
(0, 1, "kitchen_afternoon", "The silver tabby cat eats from its full white bowl on the checkered tiles."),
# 202 A cat that has had a good hunt is usually much happier
(0, 1, "room_afternoon", "The silver tabby cat licks its paw contentedly on the brown sofa."),
# 203 to curl up and snooze.
(0, 1, "room_afternoon", "The silver tabby cat sleeps curled up on the beige knitted throw on the brown sofa."),
# 204 Puzzle feeders help a lot as well.
(0, 1, "room_afternoon", f"The silver tabby cat sniffs at {TREAT_BALL} on the honey-brown floorboards."),
# 205 These are toys that hold dry food or a few treats.
(0, 0, "room_close_afternoon", f"Close-up of {TREAT_BALL} on the floorboards with a few pieces of dry cat food inside it."),
# 206 The cat has to bat and roll
(0, 1, "room_afternoon", f"The silver tabby cat bats {TREAT_BALL} with one white paw."),
# 207 and paw at them to get the food out.
(0, 1, "room_close_afternoon", f"A piece of dry food drops out of {TREAT_BALL} as the silver tabby cat paws at it."),
# 208 That turns all that swatting energy into something useful.
(0, 1, "room_afternoon", f"The silver tabby cat happily chases {TREAT_BALL} across the room."),
# 209 Some cats will happily spend ages chasing a treat ball across the floor.
(1, 1, "room_afternoon", f"The Geek reads on the brown sofa while the silver tabby cat chases {TREAT_BALL} across the beige rug."),
# 210 You can also give your cat a shelf
(1, 0, "room_afternoon", "The Geek fixes a low wooden shelf to the sage-green wall with a screwdriver."),
# 211 with its very own things on it. A few safe toys
(1, 0, "room_afternoon", f"The Geek places {TOY_MOUSE} and a few soft toy balls on the low wooden shelf."),
# 212 on a low shelf can become its private knocking spot.
(0, 1, "room_afternoon", "The silver tabby cat sits on the low wooden shelf among its soft toys."),
# 213 If something falls off there then it really doesn't matter.
(0, 1, "room_afternoon", "The silver tabby cat knocks a soft toy ball off the low wooden shelf; it lands gently on the rug."),
# 214 And when your cat does push something over try not
(1, 1, "room_evening", "The Geek stays seated calmly on the brown sofa as a book falls off the coffee table beside the silver tabby cat."),
# 215 to make a big scene.
(1, 1, "room_evening", "The Geek keeps reading with a calm deadpan face, not looking up, while the silver tabby cat stares at him."),
# 216 Stay calm and pick it up a bit later.
(1, 0, "room_evening", "The Geek calmly picks up a book from the beige rug and puts it back on the coffee table."),
# 217 If you rush over every single time the cat learns
(1, 1, "room_evening", "The Geek dashes toward the coffee table in a blur of motion lines while the silver tabby cat watches, delighted."),
# 218 that the trick works.
(0, 1, "room_evening", "The silver tabby cat sits on the coffee table with a satisfied look, tail curled."),
# 219 If nothing exciting happens the game slowly gets less fun.
(0, 1, "room_evening", "The silver tabby cat yawns on the coffee table next to a fallen pen nobody came for."),
# 220 Then make sure your cat gets plenty of attention at other times too.
(1, 1, "room_evening", "The Geek strokes the silver tabby cat on his lap on the brown sofa."),
# 221 Give it that attention when it's calm
(1, 1, "room_evening", "The Geek scratches the silver tabby cat's chin as it lies calmly beside him."),
# 222 and gentle and not only when it's causing trouble.
(1, 1, "room_evening", "The Geek and the silver tabby cat relax together on the brown sofa, the coffee table tidy."),
# 223 There's one more thing worth saying here.
(1, 0, "room_evening", "The Geek raises one finger with a serious deadpan face."),
# 224 A cat that suddenly starts knocking things over far more
(0, 1, "room_evening", "The silver tabby cat stands among many fallen objects on the rug: books, pens and keys."),
# 225 than usual might be trying to tell you something.
(0, 1, "room_close_evening", "Close-up of the silver tabby cat looking up with an earnest expression."),
# 226 It could be bored after a change in your routine.
(1, 1, "hallway_evening", "The Geek walks out of the front door with a coat on while the silver tabby cat watches from the floor, looking lonely."),
# 227 It could be hungry because its food has changed.
(0, 1, "kitchen_afternoon", "The silver tabby cat sniffs at an unfamiliar new bag of cat food next to its white bowl, unsure."),
# 228 Older cats sometimes act differently when their eyesight starts to fade.
(0, 0, "plain", f"{cap(OLD_CAT)} squints at a blurry room, the edges of the picture soft and out of focus. No labels or text."),
# 229 If the change is big
(1, 1, "clinic", f"The Geek carries the silver tabby cat into the exam room where {VET} waits."),
# 230 and sudden it does no harm to mention it to your vet.
(1, 1, "clinic", f"{cap(VET)} gently examines the silver tabby cat on the stainless-steel table while the Geek explains."),
# 231 So why does your cat knock things off the table?
(1, 1, "room_evening", f"The Geek sits on the brown sofa looking thoughtfully at the silver tabby cat sitting beside {MUG} on the coffee table."),
# 232 Because it's a hunter at heart
(0, 0, "desert", f"{cap(WILDCAT)} stalks through the scrubland at dusk."),
# 233 and a quick tap is how hunters check if something is alive.
(0, 1, "room_close_afternoon", f"The silver tabby cat taps {TOY_MOUSE} with one white paw."),
# 234 Because its eyes aren't great up close and its paws help it explore.
(0, 1, "room_close_afternoon", f"The silver tabby cat feels {REMOTE} with its whiskers and paw."),
# 235 Because it seems curious about how things fall and what noise they make.
(0, 1, "room_afternoon", f"The silver tabby cat watches {SPOON} fall from the coffee table with fascination."),
# 236 Because it has learned
(1, 1, "room_afternoon", "The silver tabby cat sits on the coffee table looking clever, the Geek visible behind it on the brown sofa."),
# 237 that a falling object makes you jump up and pay attention.
(1, 1, "room_afternoon", "The Geek jumps up from the brown sofa as a book falls, the silver tabby cat watching him."),
# 238 And because sometimes it's just plain bored
(0, 1, "room_afternoon", "The silver tabby cat lies bored on the windowsill, tail drooping."),
# 239 and your stuff makes a really fun toy.
(0, 1, "room_afternoon", f"The silver tabby cat bats {KEYS} across the floorboards happily."),
# 240 So the next time a paw slides
(0, 1, "room_close_evening", f"Close-up of the silver tabby cat's white paw on {MUG} at the edge of the coffee table."),
# 241 your mug toward the edge take a breath before you shout.
(1, 1, "room_evening", "The Geek closes his eyes and takes a slow deep breath on the brown sofa, while the silver tabby cat sits by the mug on the coffee table."),
# 242 Look at the cat looking right back at you.
(1, 1, "room_evening", "The Geek and the silver tabby cat look at each other across the coffee table."),
# 243 It isn't being evil and it isn't out to get you.
(0, 1, "room_close_evening", "The silver tabby cat looks up with soft innocent eyes."),
# 244 It's a tiny desert hunter stuck inside a living room.
(0, 1, "room_evening", "The silver tabby cat crouches in a hunting pose on the beige rug, a faint dreamy outline of desert sand dunes drawn softly behind it."),
# 245 And right now it mostly just wants you to come and play.
(1, 1, "room_evening", f"The Geek kneels on the beige rug playing with the silver tabby cat using {WAND}, both happy."),
]
