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
BOX = "a plain brown cardboard box with its flaps open and no writing on it"
PARCEL = "a closed plain brown cardboard box taped shut, with no writing on it"
SMALL_BOX = "a small plain white shoe box with no writing on it"
BED = "a brand-new round plush cat bed in soft cream fabric"
CAT_TREE = "a tall new cat tree with beige carpeted platforms"
LAMP = "a new table lamp with a white shade"
SHOES = "a pair of new white sneakers"
TAPE_SQUARE = "a square outline made of four strips of blue painter's tape stuck on the floor, empty inside"
KANIZSA = ("four black circles placed at the corners of an imaginary square, each with a quarter wedge cut out facing inward "
           "like little round pac men, so that the eye sees a white square between them that has no drawn edges")
WILDCAT = ("a sandy-brown African wildcat with faint darker stripes on its legs, long legs, a slim ringed tail with a black "
           "tip and amber eyes")
FOX = "a red fox with a white-tipped bushy tail"
JACKAL = "a lean golden jackal with large pointed ears and a bushy black-tipped tail"
EAGLE = "a large brown eagle with spread wings"
WOLVES = "two grey wolves running with their tongues out"
MOUSE = "a small brown field mouse"
MOTHER = "a ginger-and-white mother cat with an orange tabby head and back, a white chest, belly and paws, and amber eyes"
KITTENS = ("three tiny newborn kittens, one ginger, one black-and-white and one cream, with their eyes sealed shut and their "
           "tiny ears folded flat")
KITTEN = "a tiny newborn ginger kitten with its eyes sealed shut"
TORTIE = "a tortoiseshell cat with a mottled black-and-orange coat and amber eyes"
BLACK = "a sleek black cat with yellow-green eyes"
ORANGE = "a plump orange tabby cat with amber eyes"
TUXEDO = "a black-and-white tuxedo cat with a white chest, white paws, a white chin and green eyes"
LION = "a large male lion with a thick golden-brown mane"
TIGER = "a large orange tiger with bold black stripes"
STAFF = "a shelter worker with a brown ponytail in a green polo shirt"
RESEARCHER = "a researcher with dark hair in a bun and a burgundy sweater"
OWNER = "a woman with short brown hair in a red sweater"
COURIER = "a delivery driver in a brown uniform and cap"
VET = "a friendly female vet with dark curly hair tied back, wearing a blue scrub top"
GUESTS = "a small group of party guests chatting and laughing, holding drinks"

# This video's own places. False = not the attached room.
PLACES = dict(HOME, **{
    "doorstep": (False, "The front doorstep of an apartment building on a quiet afternoon: a dark-wood front door with a "
                 "brass handle, a plain doormat, a pale brick wall and a small potted shrub."),
    "desert": (False, "Dry desert scrubland in Africa in warm late-afternoon light: sandy ground, scattered rocks, low thorny "
               "bushes, clumps of dry grass, and pale hills on the horizon under a hazy sky. No buildings, roads or fences."),
    "desert_close": (False, "A close-up at ground level in dry desert scrubland: sandy earth, small stones and dry grass stems "
                     "in warm low light, the scrubland softly out of focus behind. No buildings, roads or fences."),
    "rocks": (False, "A jumble of large sandy boulders in desert scrubland at dusk, with dark narrow gaps between the rocks "
              "and dry grass around them. No buildings, roads or fences."),
    "forest_snow": (False, "A snowy forest clearing on a grey winter day: tall dark pine trees, deep white snow and a frozen "
                    "stream. No buildings, roads or fences."),
    "shelter": (False, "An animal shelter cat room: pale green walls, a row of large clean wire-fronted cat pens with soft "
                "blankets inside, a tiled floor and bright overhead lights."),
    "shelter_pen": (False, "Inside a clean wire-fronted cat pen at an animal shelter: a soft blanket on the floor, a water "
                    "bowl, a small litter tray in the corner, and bright light from the room outside."),
    "closet": (False, "Inside a wooden walk-in closet with pale yellow walls: shelves of folded towels, and a heap of soft "
               "blankets in green, mustard and cream on the wooden floor. Warm dim light."),
    "bathroom": (False, "A small apartment bathroom with pale sage-green walls, white square tiles, a white sink in a "
                 "wooden vanity unit, a round mirror and a cream bath mat."),
    "cat_home": (False, "A cozy cottage living room with pale yellow walls, a cream two-seat sofa with green cushions, a "
                 "wooden floor with a round braided rug, a window with white curtains, and a small wooden side table with "
                 "a lamp with a red shade. Afternoon daylight."),
    "sanctuary": (False, "A big-cat sanctuary enclosure in sunny daylight: green grass with patches of dry earth, tall leafy "
                  "trees, wooden platforms, beds of straw, and a high wire fence at the back."),
    "clinic": (False, "A bright clean vet clinic exam room: white walls, a stainless-steel exam table, pale blue cabinets and "
               "a sink."),
    "research_office": (False, "A small bright research office: white walls, a wooden desk with an open laptop, a cork board "
                        "pinned with photos of cats, and a window with daylight."),
    "plain_dark": (False, "There is no room and no landscape: a plain calm dark-blue background fills the frame."),
})

SCENES = [
# 1 Why do cats love boxes so much?
(1, 1, "room_afternoon", f"The silver tabby cat sits snugly inside {BOX} on the beige rug, only its head and ears showing, while the Geek stands beside it with a flat deadpan look."),
# 2 You buy your cat a fancy new bed and it ignores it completely.
(1, 1, "room_afternoon", f"The Geek holds out {BED} toward the silver tabby cat, which turns its head away, ignoring it."),
# 3 Then it climbs straight into the cardboard box the bed came in.
(1, 1, "room_afternoon", f"The silver tabby cat steps happily into {BOX} on the beige rug, while the Geek still holds {BED} with a deadpan stare."),
# 4 So what is it about a plain old box
(1, 1, "room_afternoon", f"The Geek crouches beside {BOX} with the silver tabby cat inside, studying the box with a puzzled deadpan look."),
# 5 that a cat just can't resist?
(0, 1, "room_close_afternoon", f"Close-up of the silver tabby cat peeking over the edge of {BOX}, eyes wide and content."),
# 6 A parcel turns up at your door on a quiet afternoon.
(0, 0, "doorstep", f"{cap(COURIER)} sets {PARCEL} down on the doormat."),
# 7 You carry it inside and set it down on the floor.
(1, 0, "room_afternoon", "The Geek carries a closed plain brown cardboard box with no writing into the room and sets it down on the beige rug."),
# 8 You open it up and lift out whatever you ordered.
(1, 0, "room_afternoon", "The Geek kneels by the opened plain brown cardboard box, lifting out packing paper."),
# 9 Maybe it's a lamp or a pair of shoes
(1, 0, "room_afternoon", f"The Geek holds up {LAMP} in one hand and {SHOES} in the other beside the open cardboard box."),
# 10 or a lovely new cat tree. And before you've even folded the flaps
(1, 0, "room_afternoon", f"The Geek stands {CAT_TREE} upright next to the open cardboard box, looking pleased."),
# 11 down there's a cat sitting inside the box.
(1, 1, "room_afternoon", f"The Geek turns around to find the silver tabby cat already sitting inside {BOX}, ignoring {CAT_TREE}."),
# 12 It doesn't matter how big the box is.
(0, 1, "room_afternoon", "The silver tabby cat sits inside a huge plain brown cardboard box with no writing, looking tiny inside it."),
# 13 It doesn't matter if the cat barely fits.
(0, 1, "room_afternoon", f"The silver tabby cat squeezes halfway into {SMALL_BOX} on the beige rug."),
# 14 A big chunky cat will happily cram itself
(0, 0, "cat_home", f"{cap(ORANGE)} crams itself into {SMALL_BOX} on the round braided rug."),
# 15 into a tiny shoe box with its sides spilling over the edges.
(0, 0, "cat_home", f"{cap(ORANGE)} sits wedged in {SMALL_BOX}, its fluffy sides bulging out over all the edges."),
# 16 Then it just sits there looking extremely pleased with itself.
(0, 0, "cat_home", f"{cap(ORANGE)} sits in {SMALL_BOX} with half-closed eyes and a smug, satisfied look."),
# 17 Meanwhile the expensive thing that came
(0, 1, "room_afternoon", f"{cap(CAT_TREE)} stands untouched in the corner while the silver tabby cat sits in {BOX} on the rug."),
# 18 in the box lies forgotten on the floor.
(0, 0, "room_afternoon", f"{cap(BED)} lies forgotten on the honey-brown floorboards by the sofa."),
# 19 People joke about this constantly. You can spend a small fortune on toys
(1, 1, "room_afternoon", "The Geek sits among a pile of expensive cat toys on the beige rug while the silver tabby cat plays with the empty cardboard box instead."),
# 20 and the cat would still rather have the packaging.
(0, 1, "room_afternoon", "The silver tabby cat lies happily in a nest of crumpled packing paper inside a cardboard box."),
# 21 But there are real reasons hiding behind it.
(1, 1, "room_afternoon", f"The Geek holds up a magnifying glass to the side of {BOX} that the silver tabby cat sits in."),
# 22 Some of them go back thousands of years
(0, 0, "desert", f"{cap(WILDCAT)} walks through the dry grass between the thorny bushes."),
# 23 and some are about how a cat feels on the inside.
(0, 1, "room_close_afternoon", f"Close-up of the silver tabby cat resting calmly in {BOX}, eyes half closed."),
# 24 Let's start with the oldest one.
(0, 0, "desert", "Wide view of the desert scrubland at dusk, the sun low over the pale hills."),
# 25 Your house cat comes from a small wild cat
(0, 0, "desert", f"{cap(WILDCAT)} stands on a rock looking out over the scrubland."),
# 26 that lived in deserts and dry grasslands.
(0, 0, "desert", f"{cap(WILDCAT)} pads across the sandy ground with the pale hills behind."),
# 27 That wild cat was a hunter.
(0, 0, "desert_close", f"{cap(WILDCAT)} crouches low in the dry grass, eyes locked on {MOUSE}."),
# 28 But it was also small enough to end up as somebody else's lunch.
(0, 0, "desert", f"{cap(WILDCAT)} looks up nervously as a large bird's shadow passes over the sand."),
# 29 Foxes and jackals and birds of prey
(0, 0, "desert", f"{cap(FOX)} and {JACKAL} prowl through the scrubland while {EAGLE} circles above."),
# 30 and bigger cats would all have been glad to eat it.
(0, 0, "desert", f"{cap(LION)} watches from the dry grass in the distance."),
# 31 So a small wild cat needed two things at the same time.
(0, 0, "desert", f"{cap(WILDCAT)} sits alert, looking left and right."),
# 32 It needed a way to hunt
(0, 0, "desert_close", f"{cap(WILDCAT)} pounces on {MOUSE} in the dry grass."),
# 33 and it needed a way to stay out of sight.
(0, 0, "desert", f"{cap(WILDCAT)} slips quietly behind a thorny bush, half hidden."),
# 34 The answer to both turned out to be a good hiding spot.
(0, 0, "rocks", f"{cap(WILDCAT)} peers out from a dark gap between the boulders."),
# 35 Think of a gap between two rocks
(0, 0, "rocks", "A narrow dark gap between two large sandy boulders, just big enough for a small cat."),
# 36 or a hollow under a thorny bush.
(0, 0, "desert", "A shady hollow under a low thorny bush on the sandy ground."),
# 37 Or maybe an old burrow dug into the ground by some other animal.
(0, 0, "desert_close", "The round dark entrance of an old burrow dug into a sandy bank."),
# 38 Somewhere small and dark with walls on every side.
(0, 0, "rocks", f"{cap(WILDCAT)} curls up in a small dark rocky hollow with stone on every side."),
# 39 Tucked in there the cat could rest without anything creeping up behind it.
(0, 0, "rocks", f"{cap(WILDCAT)} sleeps in the rocky hollow while {JACKAL} walks past outside without noticing."),
# 40 And it could watch the world outside without being seen.
(0, 0, "rocks", f"Only the amber eyes of {WILDCAT} glow from the dark gap between the boulders, watching."),
# 41 Cats are what scientists call ambush hunters.
(0, 0, "desert", f"{cap(WILDCAT)} lies flat and hidden in the dry grass, perfectly still."),
# 42 They don't chase prey for miles the way wolves do.
(0, 0, "forest_snow", f"{cap(WOLVES)} chase through the deep snow between the pine trees."),
# 43 Instead they wait patiently and quietly.
(0, 0, "desert_close", f"Close-up of {WILDCAT} hidden in the grass, eyes narrowed, waiting."),
# 44 They hide somewhere still and they barely move a whisker.
(0, 0, "desert_close", f"Extreme close-up of the face of {WILDCAT} among grass stems, whiskers still."),
# 45 Then when a mouse wanders close enough they explode out
(0, 0, "desert_close", f"{cap(MOUSE)} sniffs along the sand close to a clump of grass where amber eyes are watching."),
# 46 in one fast pounce. For an ambush hunter a good hiding
(0, 0, "desert_close", f"{cap(WILDCAT)} explodes out of the grass in a fast pounce, motion lines behind it."),
# 47 spot is the most important tool there is.
(0, 0, "rocks", f"{cap(WILDCAT)} settles back into its rocky hollow, satisfied."),
# 48 Now look at a cardboard box the way your cat does.
(0, 1, "room_afternoon", f"The silver tabby cat stares at {BOX} on the beige rug with intense focus."),
# 49 It has walls on every side.
(0, 0, "room_close_afternoon", f"Close view looking into {BOX}, its four brown walls around an empty inside."),
# 50 It has one opening to peek out of.
(0, 1, "room_close_afternoon", f"The silver tabby cat's eyes and ears peek out over the edge of {BOX}."),
# 51 It's just big enough for one cat.
(0, 1, "room_afternoon", f"The silver tabby cat fits perfectly inside {BOX}, curled snugly."),
# 52 Honestly it's pretty much the perfect hunting hide.
(0, 1, "room_afternoon", f"The silver tabby cat crouches low inside {BOX} in a hunting pose, only its eyes showing."),
# 53 Your cat sits in there with only its eyes and ears poking out.
(0, 1, "room_close_afternoon", f"Close-up of the silver tabby cat's eyes and ears poking out over the rim of {BOX}."),
# 54 It feels safe and it feels ready for action.
(0, 1, "room_close_afternoon", f"The silver tabby cat inside {BOX} with its pupils wide and its rear wiggling, ready to pounce."),
# 55 Anything that wanders past is about to get ambushed.
(1, 1, "room_afternoon", f"The Geek walks past {BOX} carrying a mug while the silver tabby cat crouches inside, watching his feet."),
# 56 And quite often that something turns out to be your ankle.
(1, 1, "room_afternoon", f"The silver tabby cat leaps out of {BOX} and grabs the Geek's ankle, and he freezes mid-step with a deadpan wince."),
# 57 The second big reason is stress.
(0, 1, "room_evening", "The silver tabby cat crouches tense on the brown sofa, ears turned sideways."),
# 58 Cats are animals that like things to stay the same.
(0, 1, "room_afternoon", "The silver tabby cat sleeps in its usual sunny spot on the windowsill."),
# 59 They like the same food
(0, 1, "kitchen_morning", "The silver tabby cat eats from its white bowl on the checkered tiles."),
# 60 and the same routine and the same quiet corners.
(0, 1, "room_afternoon", "The silver tabby cat naps in the quiet corner beside the tall plant pot."),
# 61 When something changes they can get anxious pretty quickly.
(0, 1, "room_evening", "The silver tabby cat stares with wide eyes at a newly moved armchair in the room."),
# 62 A new house or a new pet
(0, 1, "room_afternoon", "The silver tabby cat puffs up its tail at a small brown puppy sniffing around the rug."),
# 63 or a loud party can all rattle a cat.
(1, 1, "room_evening", f"{cap(GUESTS)} fill the room around the Geek, while the silver tabby cat hides under the coffee table with flattened ears."),
# 64 And when a cat feels stressed its first instinct is usually to hide.
(0, 1, "room_evening", "The silver tabby cat squeezes into the dark gap behind the brown sofa."),
# 65 Scientists have actually put this to the test.
(0, 0, "shelter", f"{cap(STAFF)} walks along the row of cat pens holding a clipboard with no readable writing."),
# 66 In 2014 a team at Utrecht University in the Netherlands studied cats
(0, 0, "shelter", f"{cap(STAFF)} kneels and gently looks into a cat pen where {TORTIE} sits."),
# 67 that had just arrived at an animal shelter.
(0, 0, "shelter", f"{cap(STAFF)} carries a pet carrier with {BLACK} peeking out into the room."),
# 68 A shelter is a really stressful place for a cat.
(0, 0, "shelter_pen", f"{cap(BLACK)} crouches tense at the back of the pen, eyes wide."),
# 69 Everything is new and noisy and smells of strangers.
(0, 0, "shelter", f"{cap(BLACK)} in its pen flattens its ears as people walk past and other cats meow nearby."),
# 70 Some of the new arrivals were given a box to hide in.
(0, 0, "shelter_pen", f"{cap(TORTIE)} steps into {BOX} placed inside its pen."),
# 71 The others didn't get one.
(0, 0, "shelter_pen", f"{cap(BLACK)} sits on the open blanket of its pen with nowhere to hide."),
# 72 The cats with boxes settled in much faster.
(0, 0, "shelter_pen", f"{cap(TORTIE)} lies relaxed in {BOX} in its pen, eyes half closed."),
# 73 Within a few days they were calmer
(0, 0, "shelter_pen", f"{cap(TORTIE)} stretches out of {BOX}, calm and curious."),
# 74 and less stressed than the cats without boxes.
(0, 0, "shelter", f"Two pens side by side: in one {TORTIE} rests calmly in a box; in the other {BLACK} crouches tensely with no box."),
# 75 They got used to their new surroundings
(0, 0, "shelter_pen", f"{cap(TORTIE)} walks out of its box to sniff around the pen with its tail up."),
# 76 and the people around them more quickly.
(0, 0, "shelter", f"{cap(TORTIE)} rubs its cheek against the hand of {STAFF} through the open pen door."),
# 77 Something as simple as a cardboard box made a real difference.
(0, 0, "shelter_pen", f"Close view of {BOX} inside the clean pen, {TORTIE} asleep in it."),
# 78 So a box isn't just a toy for a cat.
(0, 1, "room_afternoon", f"The silver tabby cat sits seriously inside {BOX}."),
# 79 It's more like a safe room.
(0, 1, "room_close_afternoon", f"The silver tabby cat curled up deep inside {BOX}, safe and calm."),
# 80 When the world gets too loud the cat can duck inside
(1, 1, "room_evening", f"The Geek vacuums the rug with a loud vacuum cleaner while the silver tabby cat ducks down into {BOX}."),
# 81 and shut it all out.
(0, 1, "room_close_evening", f"Looking down into {BOX}: the silver tabby cat lies curled with its eyes closed, calm."),
# 82 In there nothing can come at it from behind or from the side.
(0, 1, "room_close_afternoon", f"The silver tabby cat in {BOX}, the four brown walls around it on every side."),
# 83 It only has to keep an eye on one small opening.
(0, 1, "room_close_afternoon", f"The silver tabby cat watches the open top of {BOX} with calm eyes."),
# 84 For a nervous animal that's a huge weight off its shoulders.
(0, 1, "room_afternoon", f"The silver tabby cat lets out a big relaxed sigh inside {BOX}, shoulders dropping."),
# 85 That's also why cats love all sorts of other small spaces.
(1, 1, "room_afternoon", "The Geek looks around the room for the silver tabby cat, which is squeezed onto a bookshelf between two rows of books."),
# 86 Think about all the odd places you've found your cat over the years.
(1, 0, "room_afternoon", "The Geek scratches his head, looking around the room with a deadpan puzzled face."),
# 87 Your cat has probably curled up inside an open drawer.
(0, 1, "bedroom_morning", "The silver tabby cat curls up asleep in an open drawer of the wooden chest of drawers among folded clothes."),
# 88 It has probably squeezed under the bed or into the bathroom sink.
(0, 1, "bathroom", "The silver tabby cat curls up snugly inside the round white sink."),
# 89 Laundry baskets and paper shopping bags are big favorites too.
(0, 1, "bedroom_morning", "The silver tabby cat sits in a wicker laundry basket full of clothes beside a brown paper shopping bag on the rug."),
# 90 Some cats wedge themselves onto a shelf between two rows of books.
(0, 1, "room_afternoon", "The silver tabby cat lies wedged on a shelf of the bookshelf between two rows of books."),
# 91 All of those spots share one thing in common.
(1, 1, "room_afternoon", "The Geek holds up one finger with a deadpan look, the silver tabby cat peeking out of a paper bag at his feet."),
# 92 They wrap around the cat and make it feel snug and protected.
(0, 1, "room_close_afternoon", "The silver tabby cat curled snugly inside a brown paper shopping bag, only its face showing."),
# 93 And remember how much time a cat spends asleep.
(0, 1, "room_afternoon", "The silver tabby cat sleeps stretched out on the brown sofa."),
# 94 Most cats doze for a big part of every single day.
(0, 1, "room_afternoon", "The silver tabby cat sleeps in a sunbeam on the floorboards."),
# 95 An animal that sleeps that much is going
(0, 1, "room_evening", "The silver tabby cat sleeps curled on the beige knitted throw as the evening lamp glows."),
# 96 to be very fussy about where it sleeps.
(0, 1, "room_afternoon", "The silver tabby cat sniffs at several spots on the sofa, choosing carefully."),
# 97 A sleeping cat can't keep watch. So it wants a spot
(0, 1, "room_afternoon", "The silver tabby cat sleeps with one eye slightly open on the brown sofa."),
# 98 where nothing can sneak up on it while it naps.
(0, 1, "room_afternoon", f"The silver tabby cat steps into {BOX} on the rug and lies down."),
# 99 A box gives it exactly that.
(0, 1, "room_close_afternoon", f"The silver tabby cat sleeps soundly inside {BOX}."),
# 100 This love of tight spaces starts very early.
(0, 0, "closet", f"{cap(MOTHER)} lies on the soft blankets, heavily pregnant with a round belly."),
# 101 When a mother cat is about
(0, 0, "closet", f"{cap(MOTHER)}, with a round pregnant belly, sniffs around the blankets on the closet floor."),
# 102 to give birth she goes looking for a nest.
(0, 0, "closet", f"{cap(MOTHER)}, with a round pregnant belly, pats down the soft blankets to make a nest."),
# 103 She wants somewhere dark and quiet and tucked well out of the way.
(0, 0, "closet", f"{cap(MOTHER)} settles into the back corner of the dim closet among the blankets."),
# 104 A closet floor or the back of a cupboard
(0, 0, "closet", "The dim closet floor heaped with soft blankets, quiet and cozy."),
# 105 or yes an old cardboard box.
(0, 0, "closet", f"{cap(MOTHER)} lies inside {BOX} lined with a blanket on the closet floor."),
# 106 If she feels the nest isn't safe enough
(0, 0, "closet", f"{cap(MOTHER)} looks up alertly from {BOX} where {KITTENS} sleep."),
# 107 she may even carry her kittens somewhere new. She picks them up one
(0, 0, "closet", f"{cap(MOTHER)} gently carries {KITTEN} in her mouth by the scruff of its neck."),
# 108 at a time by the scruff of the neck.
(0, 0, "closet", f"Close view of {MOTHER} holding {KITTEN} gently by the scruff, the kitten hanging calmly."),
# 109 So the very first home most kittens
(0, 0, "closet", f"{cap(KITTENS)} sleep in a heap inside {BOX} lined with a blanket."),
# 110 ever know is a small enclosed space.
(0, 0, "closet", f"Looking down into {BOX}: {MOTHER} curled around {KITTENS}."),
# 111 It's warm and it's dark and it's full of their mother's smell.
(0, 0, "closet", f"{cap(KITTENS)} snuggled against the warm belly of {MOTHER} inside the box, cozy."),
# 112 No wonder a box still feels like home years later.
(0, 1, "room_afternoon", f"The silver tabby cat curls up inside {BOX} with a content look."),
# 113 And this explains the fancy bed problem too.
(1, 1, "room_afternoon", f"The Geek points at {BED} and then at {BOX}, while the silver tabby cat sits in the box."),
# 114 A brand new cat bed is usually open
(0, 0, "room_afternoon", f"{cap(BED)} sits alone in the middle of the beige rug."),
# 115 on top and open on the sides.
(0, 0, "room_close_afternoon", f"Close view of {BED}, low and open on every side."),
# 116 It sits out in the middle of the room
(0, 0, "room_afternoon", f"Wide view of the room with {BED} sitting exposed in the middle of the floor."),
# 117 where everyone can see it.
(1, 0, "room_afternoon", f"The Geek walks right past {BED} in the middle of the room."),
# 118 It also smells of the factory and the shop instead of the cat.
(0, 1, "room_close_afternoon", f"The silver tabby cat sniffs {BED} and pulls its head back with a wrinkled nose."),
# 119 The box it came in might smell strange too.
(0, 1, "room_close_afternoon", f"The silver tabby cat sniffs the edge of {BOX} curiously."),
# 120 But the box has walls
(0, 1, "room_afternoon", f"The silver tabby cat steps into {BOX} beside {BED}."),
# 121 and a roof of sorts and only one way in.
(0, 1, "room_afternoon", f"The silver tabby cat sits under the half-closed flaps of {BOX}, peeking out of the single opening."),
# 122 To a cat that's a far better deal.
(0, 1, "room_afternoon", f"The silver tabby cat lies smugly in {BOX}, ignoring {BED} right beside it."),
# 123 Give the new bed a few weeks
(1, 0, "room_afternoon", f"The Geek places {BED} in a quiet corner beside the tall plant pot."),
# 124 and an old blanket that smells of home.
(1, 0, "room_afternoon", f"The Geek lays the beige knitted throw inside {BED}."),
# 125 Plenty of cats will warm up to it in the end.
(0, 1, "room_afternoon", f"The silver tabby cat sleeps curled up in {BED} on the beige knitted throw."),
# 126 The third reason is warmth.
(0, 1, "room_afternoon", "The silver tabby cat basks in a warm patch of sunlight on the floorboards."),
# 127 Cats like to be a good deal warmer than we do.
(1, 1, "room_afternoon", "The Geek sits in a t-shirt fanning himself, while the silver tabby cat lies snug in the sunbeam beside him."),
# 128 Scientists talk about something called the thermoneutral zone.
(0, 0, "plain", "A simple drawing of a thermometer with a soft green band marked in the middle of it. No labels, numbers or text."),
# 129 That's the range of temperatures where an animal doesn't have
(0, 0, "plain", "A thermometer drawing with a calm green middle band, a blue cold area below and a red hot area above. No labels, numbers or text."),
# 130 to burn any energy to warm up or cool down.
(0, 0, "plain", "A small cat silhouette resting comfortably beside a thermometer with its level sitting in the green band. No labels, numbers or text."),
# 131 For people that zone sits somewhere around room temperature.
(1, 0, "room_afternoon", "The Geek sits comfortably on the brown sofa in his hoodie, relaxed."),
# 132 For cats it sits a lot higher.
(0, 0, "plain", "Two thermometer drawings side by side: a person icon by one with a middle green band, and a cat icon by the other with its green band much higher. No labels, numbers or text."),
# 133 It's roughly thirty to thirty six degrees Celsius.
(0, 0, "plain", "A thermometer drawing with its warm upper section glowing soft orange and a small cat silhouette beside it. No labels, numbers or text."),
# 134 That works out to about eighty six to ninety seven degrees Fahrenheit.
(0, 1, "room_afternoon", "The silver tabby cat lies stretched out in a hot sunbeam, eyes closed in bliss."),
# 135 Most of our homes are quite a bit cooler than that.
(0, 0, "room_evening", "Wide view of the room in the evening with faint cool blue air drawn drifting across the floor."),
# 136 So a cat lounging
(0, 1, "room_evening", "The silver tabby cat lies on the beige rug curled up tightly."),
# 137 in an ordinary living room is often a little bit chilly.
(0, 1, "room_close_evening", "The silver tabby cat curled tight with its tail wrapped over its nose, fluffed up against the cool."),
# 138 That's why cats follow sunny patches across the floor all day long.
(0, 1, "room_afternoon", "The silver tabby cat moves to follow a patch of sunlight across the floorboards, dotted paw prints showing its path."),
# 139 It's why they sleep on top of warm laptops
(1, 1, "office_afternoon", "The silver tabby cat sleeps on top of the warm silver laptop on the desk while the Geek stares at it with a deadpan look."),
# 140 and pressed up against radiators.
(0, 1, "room_evening", "The silver tabby cat sleeps pressed up against a white radiator under the window."),
# 141 And it's one more reason they love boxes.
(0, 1, "room_afternoon", f"The silver tabby cat curls up inside {BOX}."),
# 142 Cardboard turns out to be a surprisingly good insulator.
(0, 0, "plain", "A cross-section drawing of a piece of corrugated cardboard showing its wavy inner layer trapping small pockets of warm air. No labels or text."),
# 143 It traps the warmth of the cat's body inside the box.
(0, 0, "plain", "A simple drawing of a cardboard box with a small cat curled inside and soft orange warmth glowing inside the walls. No labels or text."),
# 144 A small box holds that heat even better
(0, 1, "room_close_afternoon", f"The silver tabby cat squeezed tightly into {SMALL_BOX}, a soft warm glow around it."),
# 145 because there's less air to warm up.
(0, 0, "plain", "Two box drawings side by side: a big box with a little warm glow spread thin, and a small box with a strong warm glow. No labels or text."),
# 146 So when your cat squeezes into a box
(0, 1, "room_afternoon", f"The silver tabby cat squeezes into {SMALL_BOX}, its body spilling over the edges."),
# 147 that looks way too small it might know exactly what it's doing.
(1, 1, "room_afternoon", f"The Geek raises an eyebrow at the silver tabby cat crammed in {SMALL_BOX}, and the cat looks back calmly."),
# 148 It has found itself a cozy little heater.
(0, 1, "room_close_afternoon", f"The silver tabby cat dozes blissfully in {SMALL_BOX} with a soft warm glow around it."),
# 149 The fourth reason is that boxes are new and interesting.
(0, 1, "room_afternoon", f"The silver tabby cat approaches a newly arrived {PARCEL} with its ears forward."),
# 150 An indoor cat lives in a pretty small world.
(0, 1, "room_afternoon", "Wide view of the room from above, the silver tabby cat small in the middle of it."),
# 151 It knows every corner of your home and every smell in it.
(0, 1, "room_afternoon", "The silver tabby cat sniffs along the bottom of the bookshelf."),
# 152 So when a box arrives it's a genuinely big event.
(1, 1, "room_afternoon", "The Geek carries in a closed plain brown cardboard box while the silver tabby cat runs toward it excitedly."),
# 153 It has come from somewhere far away.
(0, 0, "plain", "A simple illustration of a cardboard box traveling on a little delivery truck along a winding road past hills and a warehouse. No labels or text."),
# 154 It smells of trucks and warehouses and all the people who handled it.
(0, 0, "plain", "A cardboard box with faint swirly scent lines rising from it in different colours. No labels or text."),
# 155 A curious cat simply has to go and investigate.
(0, 1, "room_close_afternoon", "The silver tabby cat sniffs all along the edge of a closed plain brown cardboard box with no writing."),
# 156 And once it has investigated the cat often wants to claim the thing.
(0, 1, "room_afternoon", f"The silver tabby cat stands with its front paws on the edge of {BOX}, looking proud."),
# 157 Cats have scent glands on their cheeks and on their chins.
(0, 0, "plain", "A side-view drawing of a cat's head with small softly glowing spots on its cheek and chin. No labels or text."),
# 158 When a cat rubs its face along
(0, 1, "room_close_afternoon", f"The silver tabby cat rubs its cheek along the corner of {BOX}."),
# 159 the edge of a box it's leaving its smell behind.
(0, 1, "room_close_afternoon", f"The silver tabby cat rubs its chin on the edge of {BOX}, faint scent lines left on the cardboard."),
# 160 It's quietly stamping the box as its own property.
(0, 1, "room_afternoon", f"The silver tabby cat sits proudly inside {BOX} like a little king on a throne."),
# 161 Plenty of cats also love to scratch and chew the cardboard.
(0, 1, "room_afternoon", f"The silver tabby cat chews on a flap of {BOX}."),
# 162 Scratching leaves even more scent from glands in their paws.
(0, 1, "room_close_afternoon", f"The silver tabby cat scratches the side of {BOX} with its claws, little bits of cardboard flying."),
# 163 It also feels wonderful on their claws.
(0, 1, "room_close_afternoon", "Close-up of the silver tabby cat's claws sinking into cardboard, its eyes half closed in pleasure."),
# 164 So a cardboard box is a hiding spot
(0, 1, "room_afternoon", f"The silver tabby cat hides in {BOX}."),
# 165 and a scratching post and a chew toy rolled into one.
(0, 1, "room_afternoon", "The silver tabby cat sits among shredded bits of a cardboard box, looking delighted."),
# 166 Now here's the strangest part of the whole story.
(1, 0, "room_afternoon", "The Geek leans forward with a mysterious deadpan face, holding a roll of blue painter's tape."),
# 167 Cats don't even need a real box.
(1, 0, "room_afternoon", "The Geek kneels on the floorboards pulling off a strip of blue painter's tape."),
# 168 You may have seen a trend online
(1, 0, "office_afternoon", "The Geek watches a video on the silver laptop showing a cat sitting in a tape square, the screen with no text."),
# 169 where people stick a square of tape on the floor.
(1, 0, "room_afternoon", f"The Geek finishes sticking {TAPE_SQUARE} onto the honey-brown floorboards."),
# 170 It's just four lines of tape making an empty square.
(0, 0, "room_close_afternoon", f"Top-down close view of {TAPE_SQUARE} on the floorboards."),
# 171 And very often the cat strolls over
(0, 1, "room_afternoon", f"The silver tabby cat strolls toward {TAPE_SQUARE}."),
# 172 and sits right in the middle of it.
(0, 1, "room_afternoon", f"The silver tabby cat sits perfectly in the middle of {TAPE_SQUARE}, looking content."),
# 173 It's as if the cat has decided
(1, 1, "room_afternoon", f"The Geek stares in disbelief at the silver tabby cat sitting inside {TAPE_SQUARE}."),
# 174 that the square counts as a box.
(0, 1, "room_close_afternoon", f"The silver tabby cat curls up inside {TAPE_SQUARE} as if inside a box."),
# 175 In 2021 a researcher named Gabriella Smith decided to test this properly.
(0, 0, "research_office", f"{cap(RESEARCHER)} sits at the desk with the laptop, looking thoughtful."),
# 176 She ran a study
(0, 0, "research_office", f"{cap(RESEARCHER)} smiles at the laptop screen, which shows a cat sitting on a floor and no text."),
# 177 with the help of cat owners in their own homes.
(0, 0, "cat_home", f"{cap(OWNER)} sets up a phone on a small stand to film the floor, while {TUXEDO} watches."),
# 178 The owners laid out shapes on the floor
(0, 0, "cat_home", f"{cap(OWNER)} kneels sticking blue tape shapes onto the wooden floor."),
# 179 and noted what their cats did.
(0, 0, "cat_home", f"{cap(OWNER)} watches from the cream sofa with a notebook as {TUXEDO} approaches the tape shapes."),
# 180 One of those shapes was a real square made of tape.
(0, 0, "cat_home", f"Top-down view of {TAPE_SQUARE} on the wooden floor."),
# 181 Another was a famous optical illusion called the Kanizsa square.
(0, 0, "plain", f"A clean drawing of {KANIZSA}. No labels or text."),
# 182 The Kanizsa square doesn't actually have any sides at all.
(0, 0, "plain", f"A close drawing of {KANIZSA}, with empty space where the sides of the square would be. No labels or text."),
# 183 It's just four shapes that look like little round pac men.
(0, 0, "plain", "Four black circles each with a quarter wedge cut out, arranged in a loose row like little round pac men. No labels or text."),
# 184 They sit in the four corners with their open mouths pointing inward.
(0, 0, "plain", f"A drawing of {KANIZSA}, with small arrows showing each wedge pointing inward. No labels or text."),
# 185 Your brain fills in the missing lines
(0, 0, "plain", f"A drawing of {KANIZSA}, with faint dotted lines softly appearing where the square's edges would be. No labels or text."),
# 186 and you see a square that isn't really there.
(0, 0, "plain", f"A drawing of {KANIZSA}, the illusory white square appearing slightly brighter than the background. No labels or text."),
# 187 The cats in the study sat
(0, 0, "cat_home", f"{cap(TUXEDO)} walks toward {KANIZSA.replace('four black circles', 'four black paper circles on the wooden floor')}."),
# 188 in that illusion square about as often as the real one.
(0, 0, "cat_home", f"{cap(TUXEDO)} sits right in the middle of {KANIZSA.replace('four black circles', 'four black paper circles on the wooden floor')}, looking content."),
# 189 That hints that cats might fall for the same illusion that we do.
(0, 0, "plain", f"A cat silhouette and a person silhouette both looking at {KANIZSA}. No labels or text."),
# 190 Their brains seem to fill in the missing edges too. It also means
(0, 0, "plain", "A side-view outline drawing of a cat's head with a softly glowing brain and a faint glowing square shape above it. No labels or text."),
# 191 that even the idea of a box can be enough for a cat.
(0, 1, "room_afternoon", f"The silver tabby cat sits contentedly inside {TAPE_SQUARE}."),
# 192 The internet already had a name for all of this.
(1, 1, "room_afternoon", f"The Geek laughs quietly at his phone while the silver tabby cat sits in {TAPE_SQUARE} nearby."),
# 193 If it fits then I sits.
(0, 1, "room_afternoon", f"The silver tabby cat sits smugly crammed into {SMALL_BOX}, chest puffed out."),
# 194 Big cats love boxes too by the way. Sanctuaries that look after lions
(0, 0, "sanctuary", f"{cap(LION)} sniffs at a giant plain brown cardboard box with no writing on the grass."),
# 195 and tigers have filmed them playing with giant cardboard boxes.
(0, 0, "sanctuary", f"{cap(TIGER)} pounces on a giant plain brown cardboard box with no writing, squashing it."),
# 196 The huge cats pounce on them
(0, 0, "sanctuary", f"{cap(LION)} leaps onto a giant plain brown cardboard box with no writing."),
# 197 and squeeze into them and rip them to shreds.
(0, 0, "sanctuary", f"{cap(TIGER)} sits squeezed into a giant torn cardboard box surrounded by shredded cardboard."),
# 198 They do it exactly like a house cat would.
(0, 0, "plain", f"Side by side: {TIGER} sitting in a giant cardboard box on the left and {ORANGE} sitting in a small cardboard box on the right, in matching poses. No labels or text."),
# 199 That instinct runs right through the whole cat family.
(0, 0, "plain", "A row of cat-family animals each sitting in its own cardboard box, from small to large: a black house cat, a lynx with ear tufts, a puma, a lion and a tiger. No labels or text."),
# 200 So should you give your cat boxes?
(1, 1, "room_afternoon", f"The Geek holds up {BOX} toward the silver tabby cat with a questioning deadpan look."),
# 201 You absolutely should if you can.
(1, 1, "room_afternoon", f"The Geek sets {BOX} down and the silver tabby cat jumps straight in."),
# 202 A cardboard box is one of the cheapest
(0, 0, "room_close_afternoon", f"{cap(BOX)} sitting on the beige rug like a gift, with a small red bow on one flap."),
# 203 and best presents you can give a cat.
(0, 1, "room_afternoon", f"The silver tabby cat sits delighted inside {BOX} with a small red bow on its flap."),
# 204 Just give it a quick check first.
(1, 0, "room_afternoon", f"The Geek inspects the inside of {BOX} closely."),
# 205 Pull out any staples and long strips of packing tape.
(1, 0, "room_close_afternoon", f"The Geek pulls a long strip of clear packing tape and a staple off {BOX}."),
# 206 Take out any plastic bags or loose ties. And cut off any handles
(1, 0, "room_afternoon", f"The Geek pulls a plastic bag out of {BOX} and cuts off a rope handle with scissors."),
# 207 that a cat could get its head stuck in.
(1, 0, "room_close_afternoon", f"Close-up of the Geek's hands holding up a removed rope handle beside {BOX}."),
# 208 If your cat seems stressed it helps
(0, 1, "room_evening", "The silver tabby cat crouches nervously by the bookshelf."),
# 209 to offer more than one hiding spot around the house. A box
(1, 0, "room_evening", f"The Geek places {BOX} in a quiet corner beside the tall plant pot."),
# 210 in a quiet corner can do a nervous cat a world of good.
(0, 1, "room_evening", f"The silver tabby cat relaxes inside {BOX} in the quiet corner."),
# 211 That's especially true after a move or when you've got guests over.
(1, 1, "room_evening", f"{cap(GUESTS)} chat around the Geek, while the silver tabby cat rests calmly in a box in the corner."),
# 212 You can even cut a little doorway
(1, 0, "room_afternoon", f"The Geek cuts a small arched doorway into the side of {PARCEL} with scissors."),
# 213 in the side of a box and put a soft blanket inside.
(1, 0, "room_afternoon", "The Geek tucks the beige knitted throw inside a cardboard box through its small arched doorway."),
# 214 Some people stack a pile of boxes into a whole cardboard castle.
(0, 1, "room_afternoon", "The silver tabby cat peeks out of a window of a cardboard castle made of stacked boxes with little towers, on the beige rug."),
# 215 There's one thing worth watching for though.
(1, 0, "room_evening", "The Geek raises one finger with a serious deadpan face."),
# 216 Hiding is perfectly normal but a big change in hiding is worth noticing.
(0, 1, "room_evening", "The silver tabby cat hides deep under the brown sofa, only its eyes visible."),
# 217 If your cat suddenly hides all the time
(1, 1, "room_evening", "The Geek kneels and peers under the brown sofa with a worried face, the silver tabby cat's eyes glowing in the dark."),
# 218 and stops eating it may be unwell.
(0, 1, "kitchen_afternoon", "The silver tabby cat's white bowl sits full and untouched on the checkered tiles, the cat lying listlessly beside it."),
# 219 The same goes if it stops using its litter box.
(0, 0, "bathroom", "A clean, unused grey litter tray sits on the white tiled floor of the bathroom."),
# 220 Cats often hide away when they're sick or in pain.
(0, 1, "room_evening", "The silver tabby cat lies curled behind the tall plant pot looking unwell, eyes half closed."),
# 221 So if the hiding comes
(1, 1, "room_evening", "The Geek gently lifts the silver tabby cat into a pet carrier."),
# 222 with other changes it's a good idea to call your vet.
(1, 1, "clinic", f"{cap(VET)} examines the silver tabby cat on the stainless-steel table while the Geek watches."),
# 223 So why do cats love boxes so much?
(1, 1, "room_afternoon", f"The Geek sits on the beige rug beside the silver tabby cat inside {BOX}, both looking content."),
# 224 Because they come from small wild cats
(0, 0, "rocks", f"{cap(WILDCAT)} peers from its rocky hollow."),
# 225 that needed safe hiding spots to survive.
(0, 0, "rocks", f"{cap(WILDCAT)} curls up safe in the dark gap between the boulders."),
# 226 Because a box is the perfect place
(0, 1, "room_afternoon", f"The silver tabby cat crouches in {BOX}, eyes peeking out."),
# 227 for an ambush hunter to lie in wait.
(0, 1, "room_afternoon", f"The silver tabby cat pounces out of {BOX} at a toy mouse."),
# 228 Because walls on every side make an anxious cat feel safe.
(0, 1, "room_close_afternoon", f"The silver tabby cat relaxes deep inside {BOX}, walls all around."),
# 229 Because cardboard keeps a cat warm in a home
(0, 1, "room_close_evening", f"The silver tabby cat dozes in {SMALL_BOX} with a warm glow around it."),
# 230 that feels a bit chilly to them.
(0, 1, "room_evening", "The silver tabby cat curls up tight on the beige rug in the cool evening."),
# 231 Because a new box is full of strange smells
(0, 1, "room_close_afternoon", f"The silver tabby cat sniffs {BOX}, scent lines rising."),
# 232 and fresh cardboard to scratch.
(0, 1, "room_close_afternoon", f"The silver tabby cat scratches the side of {BOX} happily."),
# 233 And because a cat's brain loves the idea of a box
(0, 1, "room_afternoon", f"The silver tabby cat sits inside {TAPE_SQUARE}."),
# 234 so much that a square of tape will do.
(1, 1, "room_afternoon", f"The Geek shakes his head with a small smile at the silver tabby cat sitting in {TAPE_SQUARE}."),
# 235 So the next time a parcel arrives leave the box out
(1, 0, "room_afternoon", f"The Geek sets {BOX} down on the beige rug and steps back."),
# 236 for a while.
(1, 1, "room_afternoon", f"The Geek watches from the brown sofa as the silver tabby cat approaches {BOX}."),
# 237 Watch your cat climb in and turn around and settle down.
(0, 1, "room_afternoon", f"The silver tabby cat turns in a circle inside {BOX}, settling down."),
# 238 It looks a bit silly to us.
(1, 1, "room_afternoon", f"The Geek chuckles with a deadpan smirk at the silver tabby cat in {BOX}."),
# 239 But to your cat that box is a hunting hide
(0, 1, "room_close_afternoon", f"The silver tabby cat peeks out of {BOX} like a hunter in a hide."),
# 240 and a safe room and a warm bed all at once.
(0, 1, "room_close_afternoon", f"The silver tabby cat sleeps peacefully curled inside {BOX}."),
# 241 And honestly that's a much better present than whatever came inside it.
(1, 1, "room_afternoon", f"Wide view: {CAT_TREE} stands unused in the corner while the silver tabby cat sleeps in {BOX} and the Geek reads beside it on the brown sofa."),
]
