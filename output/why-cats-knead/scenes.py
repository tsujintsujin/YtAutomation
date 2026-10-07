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

# Characters other than the Geek and his cat, written out in full wherever they appear.
MOTHER = "a ginger-and-white mother cat with an orange tabby head and back, a white chest, belly and paws, and amber eyes"
WILDCAT = ("a sandy-brown African wildcat with faint darker stripes on its legs, long legs, a slim ringed tail with a black "
           "tip and amber eyes")
TUXEDO = "a black-and-white tuxedo cat with a white chest, white paws, a white chin and green eyes"
SIAMESE = "a slim cream-colored Siamese cat with dark brown points on its face, ears, paws and tail, and bright blue eyes"
BURMESE = "a sleek solid brown Burmese cat with golden eyes"
TORTIE = "a tortoiseshell cat with a mottled black-and-orange coat and amber eyes"
CALICO_MOM = "a heavily pregnant calico cat with patches of white, black and orange and a round belly"
ORANGE = "a plump orange tabby cat with amber eyes"
GINGER = "a slim ginger tabby cat with amber eyes"
BLACK = "a sleek black cat with yellow-green eyes"
CREAM = "a fluffy cream-colored cat with blue eyes"
CALICO = "a calico cat with patches of white, black and orange"
VET = "a friendly female vet with dark curly hair tied back, wearing a blue scrub top"
BEAGLE = "a friendly brown-and-white beagle"
WOMAN = "a woman with short brown hair in a red sweater"
FLEECE = "a thick folded moss-green fleece blanket"

# This video's own places. False = not the attached room.
CAT_HOME = ("A cozy cottage living room with pale yellow walls, a cream two-seat sofa with green cushions, a wooden floor "
            "with a round braided rug, a window with white curtains, and a small wooden side table with a lamp with a red "
            "shade.")
PLACES = dict(HOME, **{
    "kitten_box": (False, "A quiet laundry-room corner at night, lit only by a small plug-in night light with a warm amber "
                   "glow: a low open cardboard box lined with soft cream towels stands on grey floor tiles beside a white "
                   "washing machine."),
    "kitten_box_close": (False, "A close-up inside a low open cardboard box lined with soft cream towels, in the warm dim "
                         "amber glow of a small night light."),
    "bakery": (False, "An old-fashioned bakery kitchen with whitewashed brick walls, a big arched brick bread oven, a long "
               "flour-dusted dark wooden worktable, wooden racks of bread loaves, a sack of flour and a small window."),
    "grandma": (False, "A tidy old-fashioned sitting room with pale floral wallpaper, a floral armchair, lace doilies, a white "
                "fireplace with a wooden mantel clock, and a small round side table. Soft daylight."),
    "garden": (False, "A back garden at dusk: tall uncut green grass, dark green hedges, a weathered wooden fence with purple "
               "flowers along it, and a deep blue evening sky."),
    "garden_wall": (False, "A garden on a calm afternoon: a low grey stone wall covered in ivy, flower beds along it, a green "
                    "lawn and a brick house wall behind."),
    "savanna": (False, "Open African grassland at dusk: tall dry golden grass, a few rocks and thorny bushes, a lone "
                "flat-topped acacia tree in the distance, low hills on the horizon and an orange evening sky. No buildings, "
                "roads or fences anywhere."),
    "savanna_close": (False, "A close-up at ground level in open African grassland at dusk: tall dry golden grass stems and "
                      "dry earth in warm low orange light, the grassland softly out of focus behind. No buildings, roads or "
                      "fences."),
    "barn": (False, "An old wooden barn on a sunny day: weathered plank walls, straw on the floor, and a shaft of sunlight "
             "from a high window."),
    "cat_home": (False, CAT_HOME + " Afternoon daylight through the window."),
    "cat_home_evening": (False, CAT_HOME + " Evening: the window is dark and the red-shaded side lamp is on, casting a warm glow."),
    "cat_home_kitchen": (False, "A cottage kitchen with pale yellow walls, white cabinets, a white stove, a wooden floor and a "
                         "window with white curtains. Sunny daylight."),
    "cat_home_bedroom": (False, "A cottage bedroom with pale yellow walls, a wooden bed with a patchwork quilt and a denim-blue "
                         "fleece blanket, a wooden nightstand with a small lamp with a red shade, and a wooden floor. Warm "
                         "lamp light."),
    "closet": (False, "Inside a wooden walk-in closet with pale yellow walls: shelves of folded towels, and a heap of soft "
               "blankets in green, mustard and cream on the wooden floor. Warm dim light."),
    "sanctuary": (False, "A big-cat sanctuary enclosure in sunny daylight: green grass with patches of dry earth, tall leafy "
                  "trees, wooden platforms, beds of straw, and a high wire fence at the back."),
    "clinic": (False, "A bright clean vet clinic exam room: white walls, a stainless-steel exam table, pale blue cabinets and "
               "a sink."),
    "porch": (False, "A wooden farmhouse porch with a railing at sunset, looking out over fields under an orange sky."),
    "moving_room": (False, "A bare, newly moved-into apartment room with plain off-white walls, a grey carpet, and stacks of "
                    "closed cardboard moving boxes with no writing. Flat daylight."),
    "plain_dark": (False, "There is no room and no landscape: a plain calm dark-blue background fills the frame."),
})

SCENES = [
# 1 You finally drop onto the couch.
(1, 0, "room_evening", "The Geek flops down heavily onto the brown sofa, arms loose, head tipped back, a tired deadpan expression, his canvas sneakers kicked off on the rug."),
# 2 Long day, sore feet, remote in hand.
(1, 0, "room_evening", "The Geek slumps on the brown sofa in grey socks, feet up on the coffee table, a TV remote held limply in one hand pointed at a television just out of frame, eyes heavy."),
# 3 And before you've even found something to watch,
(1, 0, "room_close_evening", "Over-the-shoulder view from behind the Geek as he sits on the brown sofa, holding a TV remote up toward a television on a low stand that glows with a plain blue menu screen with no writing."),
# 4 there's a weight on your lap. The cat.
(1, 1, "room_evening", "The silver tabby cat has just stepped up onto the Geek's lap as he sits on the brown sofa, its white front paws planted on his thighs, looking at him. He holds the remote up and away, looking down at the cat with a flat, resigned expression."),
# 5 It turns around once. Then twice.
(1, 1, "room_close_evening", "Close view of the Geek's lap as he sits on the brown sofa: the silver tabby cat is mid-turn on his charcoal-grey jeans, body curved in a circle, tail sweeping across his hoodie, while he holds his arms up out of the way."),
# 6 Then it gets to work.
(1, 1, "room_evening", "The silver tabby cat stands squarely on the Geek's lap facing forward, front legs braced, ears up, focused like a worker clocking in. The Geek sits very still on the brown sofa, watching it with a deadpan look."),
# 7 Left paw, right paw. Left paw, right paw.
(1, 1, "room_close_evening", "Close-up on the Geek's thighs in charcoal-grey jeans as he sits on the brown sofa, the silver tabby cat kneading them: one white front paw pressed down into the fabric, the other lifted mid-step. The edge of his green hoodie and the beige knitted throw are visible."),
# 8 Slow, steady pushes into your thighs,
(1, 1, "room_evening", "Side view: the silver tabby cat stands on the Geek's lap on the brown sofa, rhythmically pushing its white front paws into his legs, shoulders rolling with each push. The Geek sits back, hands raised slightly, watching."),
# 9 like a tiny baker who's got a lot of dough
(0, 0, "bakery", "Dawn light through the small window. A short round baker with a white apron and a flour-dusted bald head kneads a huge mound of bread dough on the worktable, sleeves rolled up, flour everywhere, loaves on the racks behind him."),
# 10 to get through before morning.
(0, 0, "bakery", "Night: the bakery is lit by a single hanging bulb. A long row of unbaked bread dough balls waits on the floured worktable, a rolling pin and the sack of flour beside them, the small window showing the night sky with a thin moon. Nobody is there."),
# 11 The eyes go half shut.
(1, 1, "room_close_evening", "Close-up portrait of the silver tabby cat resting against the Geek's green hoodie as he sits on the brown sofa, its pale greenish-yellow eyes half shut and dreamy, ears relaxed, whiskers soft. Only his hoodie shows, not his face."),
# 12 The purring kicks in, loud as a little outboard motor.
(1, 1, "room_close_evening", "The silver tabby cat sits contentedly on the Geek's lap on the brown sofa, eyes closed, chest puffed, throat relaxed, soft curved lines rippling out from its body suggesting a deep rumbling purr. Only his charcoal-grey jeans and the hem of his green hoodie show."),
# 13 And then, every so often,
(1, 1, "room_evening", "The Geek sits stiffly upright on the brown sofa with the silver tabby cat kneading his lap, his eyes widening a little behind his glasses, bracing as if he knows something is coming."),
# 14 a claw goes right through your jeans
(1, 1, "room_close_evening", "Extreme close-up of the silver tabby cat's white paw pressing into the Geek's charcoal-grey jeans as he sits on the brown sofa, one sharp curved claw poking clean through the denim, the weave of the denim visible. Only his lap is in frame."),
# 15 and you say something you wouldn't say
(1, 1, "room_evening", "The Geek jolts on the brown sofa, mouth open mid-yelp, shoulders up, glasses slightly askew, while the silver tabby cat on his lap keeps kneading calmly with its eyes half closed."),
# 16 in front of your grandmother.
(0, 0, "grandma", "A kind elderly grandmother with white hair in a bun and a lilac cardigan sits in the floral armchair holding a teacup, one eyebrow raised in mild disapproval. A plate of biscuits on the side table."),
# 17 Kneading, people call it.
(0, 1, "room_close_evening", "Top-down view of the silver tabby cat on the brown sofa kneading the beige knitted throw, both white front paws pressing into the wool, eyes half closed."),
# 18 Online it's got a much better name. Making biscuits.
(0, 1, "plain", "A playful split image: on the left, the silver tabby cat kneading a beige knitted throw with its white front paws; on the right, a baking tray of golden fluffy round biscuits fresh from the oven."),
# 19 If you live with a cat,
(1, 1, "hallway_evening", "The Geek comes in through the front door with a brown paper grocery bag and the silver tabby cat trots along the hallway to meet him, tail up."),
# 20 you've almost certainly been the biscuit.
(1, 1, "room_evening", "The Geek lies on his back on the beige rug in front of the coffee table, arms at his sides, staring at the ceiling with a deadpan look, while the silver tabby cat stands on his chest kneading his green hoodie with both white front paws."),
# 21 But have you ever stopped to wonder why?
(1, 1, "room_evening", "The Geek sits on the brown sofa with the silver tabby cat kneading his lap, and he tilts his head, chin on one hand, studying the cat with a thoughtful, puzzled look."),
# 22 Why would a grown animal, a predator,
(0, 1, "garden", "The silver tabby cat crouches low in the tall grass in a stalking pose, body flat, eyes locked forward, ears pricked, every muscle tense like a small hunter."),
# 23 built to stalk and pounce,
(0, 1, "garden", "The silver tabby cat leaps through the air above the tall grass, white front paws stretched out and claws spread, pouncing on a fluttering moth. Dynamic action."),
# 24 climb onto a person and start kneading them like bread?
(1, 1, "room_evening", "The silver tabby cat stands on the Geek's lap kneading his stomach like dough while he sits on the brown sofa holding a bread roll in one hand, looking from the roll to the cat with a flat expression."),
# 25 It goes back a long way. All the way back
(0, 0, "plain", "A gentle dreamy spiral of soft warm golden light leading back through time, with small drifting pictures of a cat's life getting smaller along it: an adult cat, a young cat, a kitten, and at the far end a tiny newborn kitten."),
# 26 to the first day of a cat's life, actually.
(0, 0, "kitten_box", f"Inside the box, {MOTHER} lies on her side, and one tiny newborn ginger kitten, eyes sealed shut, damp fur, curls against her belly."),
# 27 And the answer isn't one neat thing.
(1, 0, "office_afternoon", "The Geek stands at the cork board looking at four pinned drawings with strings between them: a kitten, a paw print, a pile of grass and a sleeping cat. He scratches his head with a deadpan, puzzled look. No writing on the board."),
# 28 It's a baby habit, a comfort thing,
(0, 0, ("kitten_box_close", "cat_home"), f"In the left half, a tiny ginger kitten nurses against {MOTHER} on the cream towels. In the right half, {CREAM} lies curled on the cream sofa, eyes closed, perfectly comfortable."),
# 29 a kind of signature,
(0, 0, "bakery", "Close-up of a single cat paw print pressed into soft fresh flour on the dark wooden worktable, like a signature, with a faint glowing trail rising from it. Warm light."),
# 30 and maybe a leftover from the wild too,
(0, 0, "savanna", f"{cap(WILDCAT)} stands in the tall dry grass, looking out across the grassland, the acacia tree in the distance."),
# 31 all tangled up together. So let's untangle it.
(0, 1, "room_evening", "The silver tabby cat sits in the middle of the beige rug wrapped in a big tangle of red wool yarn, looking up with wide eyes, a wicker knitting basket tipped over beside it."),
# 32 First, the first day.
(0, 0, "kitten_box", f"{cap(MOTHER)} lies curled protectively around a small litter of newborn kittens inside the box."),
# 33 A kitten comes into the world blind and deaf.
(0, 0, "kitten_box_close", "A single tiny newborn cream kitten lies on the cream towels, eyes sealed shut, small folded-down ears, tiny pink nose, wobbly head raised."),
# 34 Its eyes stay sealed shut
(0, 0, "kitten_box_close", "Extreme close-up of a sleeping newborn ginger kitten's face, its eyes tightly sealed shut, a tiny pink nose and fine whiskers, nestled against its mother's soft orange fur."),
# 35 for roughly the first week or two.
(0, 0, "kitten_box_close", "Three-week-old kittens, one ginger, one black and one calico, sit on the cream towels, their eyes freshly opened and blue, blinking at the world for the first time."),
# 36 It can't walk properly. It can't keep itself warm.
(0, 0, "kitten_box_close", "A tiny newborn tortoiseshell kitten wobbles on the cream towels, legs splayed out, belly dragging, trying to crawl, shivering slightly beside a hot water bottle wrapped in a towel."),
# 37 Honestly, it can't do much of anything,
(0, 0, "kitten_box_close", "A tiny newborn black kitten lies flat on its belly on the cream towels, legs spread out like a starfish, eyes shut, completely helpless and sleepy."),
# 38 except find its mother and eat.
(0, 0, "kitten_box", f"Newborn kittens, one ginger, one cream and one calico, eyes shut, crawl toward and nurse along the belly of {MOTHER}, who lies on her side in the box."),
# 39 And that's where kneading starts. When a newborn kitten nurses,
(0, 0, "kitten_box_close", f"A tiny newborn ginger kitten nurses at the belly of {MOTHER}, eyes shut, both tiny front paws pressed into her soft white belly fur."),
# 40 it pushes against its mother's belly with its front paws,
(0, 0, "kitten_box_close", "Very close view of two tiny kitten front paws, pink toe pads spread, pushing into the soft white belly fur of a ginger-and-white mother cat."),
# 41 one after the other. Push, push, push.
(0, 0, "kitten_box", f"Three newborn kittens, one ginger, one cream and one calico, nurse side by side at the belly of {MOTHER}, each pushing with alternating little front paws in rhythm."),
# 42 That pressure on the milk glands helps get the milk flowing.
(0, 0, "plain", "A gentle simple educational cross-section illustration of a ginger-and-white mother cat's belly, with soft glowing warm lines showing milk flowing toward a nursing kitten whose paws press against her. Clean diagram look, no labels."),
# 43 More pushing, more milk. Simple deal.
(0, 0, "kitten_box_close", f"A plump content newborn ginger kitten with a round full belly lies asleep on its back against the soft white belly fur of {MOTHER}, a tiny drop of milk at the corner of its mouth."),
# 44 Kittens start doing it in their very first days,
(0, 0, "kitten_box_close", f"A tiny newborn calico kitten, eyes shut, kneads the belly of {MOTHER} with its little front paws."),
# 45 long before they can even see what they're pushing on.
(0, 0, "kitten_box_close", f"A newborn black kitten with its eyes sealed shut kneads and nurses blindly against the white belly fur of {MOTHER}."),
# 46 Nobody shows them how.
(0, 0, "kitten_box", f"{cap(MOTHER)} sleeps with her eyes closed in the box while her small newborn kittens knead and nurse on their own, all by instinct."),
# 47 It's just there, wired in from the start.
(0, 0, "plain_dark", "A soft glowing outline drawing of a tiny kitten curled up, with a gentle warm light pulsing from its little front paws, like instinct shining from inside."),
# 48 So picture what kneading means
(1, 0, "room_evening", f"The Geek sits cross-legged on the beige rug with eyes closed and a calm expression, imagining, with a soft dreamy cloud above his head showing {MOTHER} nursing a litter of kittens."),
# 49 to a kitten in those first few weeks.
(0, 0, "kitten_box", f"A two-week-old cream kitten with freshly opened blue eyes nestles against {MOTHER} in the box."),
# 50 It means warmth. Food. A big purring mother.
(0, 0, "kitten_box", f"{cap(MOTHER)} lies on her side in the box, eyes closed, purring contentedly, a litter of kittens nursing along her belly."),
# 51 A heap of brothers and sisters all squashed together.
(0, 0, "kitten_box", "A cozy heap of five sleeping kittens, one ginger, one black, one calico, one cream and one tortoiseshell, piled on top of each other on the cream towels in the box, paws and tails tangled together."),
# 52 Pretty much everything good
(0, 0, "kitten_box", f"{cap(MOTHER)} curls around her sleeping kittens in the box, a full feeling of safety and comfort."),
# 53 in its whole little world happens while those paws are going.
(0, 0, "kitten_box_close", "A nursing ginger kitten's tiny front paws knead its ginger-and-white mother's soft white belly fur, its eyes closed in bliss."),
# 54 Then the kitten grows up,
(0, 0, "plain", "A playful side-by-side: a tiny newborn ginger kitten on the left and a ginger kitten at eight weeks on the right, bigger, eyes open, tail up, standing confidently."),
# 55 the way kittens do, which is fast.
(0, 0, "cat_home", "Three young kittens, one ginger, one black and one calico, tumble and chase each other at full speed across the braided rug, a toy ball rolling away."),
# 56 Somewhere around eight weeks or so, it's weaned.
(0, 0, "cat_home_kitchen", f"A young ginger kitten about eight weeks old eats from a small shallow dish of wet kitten food on the floor, {MOTHER} sitting calmly nearby."),
# 57 Solid food now. It's off exploring, wrestling its siblings,
(0, 0, "cat_home", "Two young kittens, a ginger one and a black one, wrestle and roll together on the braided rug, paws batting, mouths open in play."),
# 58 ambushing its first toy mouse.
(0, 0, "cat_home", "A young ginger kitten pounces from behind a leg of the cream sofa onto a small grey felt toy mouse on the wooden floor, ears forward, eyes wide."),
# 59 The milk is long gone.
(0, 0, "cat_home_kitchen", f"{cap(GINGER)}, fully grown, sits beside its empty food bowl on the kitchen floor, looking alert and independent, no mother cat or kittens around."),
# 60 The kneading, though? That stays.
(0, 1, "room_close_evening", "The silver tabby cat, fully grown, kneads the beige knitted throw on the brown sofa, eyes half closed, both white front paws pressing down."),
# 61 And that's the first big reason your cat kneads you.
(1, 1, "room_evening", "The silver tabby cat kneads the Geek's lap while he sits on the brown sofa, and he looks down at it with a soft, understanding expression."),
# 62 It's kitten behavior that never got switched off.
(0, 1, "room_close_evening", "The silver tabby cat kneads an olive-green cushion on the brown sofa, while above it a soft glowing ghost-like outline of a tiny kitten does the matching kneading motion, showing the kitten inside the adult."),
# 63 A surprising amount of what house cats
(0, 1, "room_afternoon", "The silver tabby cat sits on the sill of the white-framed window, gazing out, a calm grown-up house cat, the tall leafy plant beside it."),
# 64 do as grownups is really baby stuff that just stuck around.
(0, 1, "room_afternoon", "The silver tabby cat, fully grown, lies on its back on the beige rug playing with a dangling feather toy like a kitten, all four white paws in the air."),
# 65 They meow at us,
(1, 1, "kitchen_morning", "The silver tabby cat sits on the checkered floor looking up at the Geek with its mouth open in a meow, while he stands holding a coffee mug, looking down with a deadpan expression."),
# 66 even though adult cats hardly ever meow at each other.
(0, 0, "garden_wall", f"Two adult cats, {GINGER} and {BLACK}, sit facing each other on the stone wall, communicating silently with tails and ears, their mouths closed."),
# 67 They trot up to us with their tails held straight up,
(1, 1, "hallway_afternoon", "The silver tabby cat trots happily along the hallway toward the Geek with its tail held straight up like a flag, a little hook at the tip, while he crouches with one hand out."),
# 68 the way a kitten greets its mother.
(0, 0, "barn", f"A small cream kitten trots toward {MOTHER} across the straw, its tiny tail held straight up in greeting, the mother leaning down to sniff it."),
# 69 And they knead.
(0, 1, "room_close_evening", "Close-up of the silver tabby cat's white front paws kneading the beige knitted throw on the brown sofa, one paw pressing, one lifted."),
# 70 Think about when your cat actually does it.
(1, 1, "room_afternoon", "The Geek sits on the floor by the coffee table with a notepad, tapping his chin with a pencil, watching the silver tabby cat curled up on the brown sofa. No writing visible."),
# 71 Usually it's relaxed. Sprawled on a soft blanket,
(0, 1, "bedroom_morning", "The silver tabby cat sprawls on its side across the white duvet on the bed, totally relaxed, legs stretched out, eyes half closed."),
# 72 settled on a warm lap, drifting toward a nap.
(1, 1, "room_close_evening", "Close view of the Geek's lap on the brown sofa: the silver tabby cat curled up in a loaf shape on his green hoodie and charcoal-grey jeans, eyes slowly closing, while his hand rests gently on its back."),
# 73 Its whole body is saying, this feels like being a kitten
(0, 1, "room_close_evening", "The silver tabby cat lies completely relaxed on the beige knitted throw on the brown sofa, paws tucked, eyes closed, a faint glowing kitten-shaped outline curled up around it like a warm memory."),
# 74 again. Safe. Warm. Fed.
(0, 1, "room_evening", "The silver tabby cat curled up asleep in a round cream fluffy cat bed on the rug beside the bookshelf, an empty licked-clean food bowl nearby, a feeling of complete safety."),
# 75 And the paws just go back to the thing they used
(0, 1, "room_close_evening", "Close-up of the silver tabby cat's white front paws starting to knead the beige knitted throw, toes spreading, the cat's half-closed eyes visible above."),
# 76 to do when life felt exactly like this.
(0, 0, "kitten_box_close", f"A tiny newborn ginger kitten kneads and nurses at the warm belly of {MOTHER}, a calm and peaceful feeling."),
# 77 Look closely and you'll often catch other kitten signs tagging along.
(1, 1, "room_evening", "The Geek leans in close with a magnifying glass, peering at the silver tabby cat kneading the beige knitted throw on the brown sofa, with a curious deadpan expression."),
# 78 The purring, for one. Kittens purr while they nurse,
(0, 0, "kitten_box", f"A litter of kittens, one ginger, one calico and one cream, nurse contentedly at the belly of {MOTHER}, eyes closed, soft gentle curved lines in the air suggesting a quiet purr."),
# 79 and the mother purrs right back at them.
(0, 0, "kitten_box", f"{cap(MOTHER)} with half-closed eyes, curled around her nursing kittens in the box, her chin resting on one of them, soft gentle curved lines around her throat suggesting a purr."),
# 80 Some cats drool while they knead, which is a bit gross,
(0, 0, "cat_home_evening", f"{cap(ORANGE)} kneads a grey fleece blanket on the cream sofa with half-closed blissful eyes, a small shiny drop of drool hanging from its chin."),
# 81 I'll admit, and a bit baffling
(1, 0, "room_evening", "The Geek sits on the brown sofa holding up his sleeve and looking at a small damp drool spot on his green hoodie with a deadpan, mildly disgusted expression."),
# 82 until you remember what kneading used to bring. A drooling,
(0, 0, "cat_home_evening", f"{cap(ORANGE)} kneads a grey fleece blanket on the cream sofa with a little drool on its chin, and a small dreamy thought bubble floats above it showing a newborn kitten happily nursing."),
# 83 kneading cat is, more or less, remembering milk.
(0, 0, "cat_home_evening", f"{cap(ORANGE)} kneads a grey fleece blanket on the cream sofa with eyes closed in bliss, and a soft glowing picture of a small saucer of milk floats gently above its head like a memory."),
# 84 And some cats take it one step further
(0, 0, "cat_home_bedroom", f"{cap(TUXEDO)} lies on the bed holding the corner of the denim-blue fleece blanket in its front paws, eyes half closed, about to put the corner into its mouth."),
# 85 and suck on a blanket, or your sleeve,
(1, 0, "room_evening", f"The Geek sits on the brown sofa with a deadpan expression while {TUXEDO} on his lap gently sucks on the cuff of his green hoodie sleeve, kneading his arm."),
# 86 or a soft toy, kneading away the whole time.
(0, 0, "cat_home_bedroom", f"{cap(TUXEDO)} curls around a plush teddy bear on the bed, sucking on the bear's ear while kneading its soft belly with both front paws."),
# 87 Nursing on fleece, basically.
(0, 0, "cat_home_bedroom", f"Close-up of {TUXEDO} with eyes closed, softly sucking a corner of the denim-blue fleece blanket like a kitten nursing, front paws kneading."),
# 88 So when your cat climbs aboard and starts making biscuits,
(1, 1, "room_evening", "The silver tabby cat climbs onto the Geek's lap from the arm of the brown sofa, one white paw already on his thigh, as he lowers a book to make room."),
# 89 there's a real sense in which it's
(1, 1, "room_evening", f"The Geek sits on the brown sofa with the silver tabby cat kneading his lap, and on the wall behind him a soft glowing picture of {MOTHER} with her kitten appears like a thought."),
# 90 treating you a little bit like its mom.
(1, 1, "room_evening", f"The silver tabby cat kneads the Geek's chest as he lies back along the brown sofa, while in a soft dreamy thought bubble above the cat {MOTHER} nurses her kittens."),
# 91 You're warm, you're soft, you're safe, and, crucially,
(1, 1, "room_evening", "The Geek is wrapped in the beige knitted throw on the brown sofa like a warm burrito, the silver tabby cat curled up contentedly on top of him."),
# 92 you're the one who fills the food bowl.
(1, 1, "kitchen_morning", "The Geek crouches and pours dry cat food from a plain bag with no writing into a bowl on the checkered floor, while the silver tabby cat watches eagerly beside it, tail up."),
# 93 From where the cat's sitting, which is on you,
(1, 1, "room_close_evening", "A low view from the silver tabby cat's point of view: the cat sits on the Geek's chest as he lies along the brown sofa, looking down at his face with round glasses and a deadpan expression."),
# 94 that's a pretty good job description for a mother.
(1, 1, "room_evening", "The Geek sits on the brown sofa with the silver tabby cat in his arms like a baby, its white belly up, its paws relaxed, and he looks down at it with a calm, fond deadpan expression."),
# 95 Comfort isn't the whole story though.
(1, 1, "room_evening", "The Geek sits on the brown sofa with the silver tabby cat kneading his lap, holding up one finger as if remembering something."),
# 96 There's something else going on under those paws.
(0, 1, "room_close_evening", "Close-up low view of the silver tabby cat's white paw pressing down onto the beige knitted throw on the brown sofa, with soft glowing dots of light rising from between its toe pads."),
# 97 Cats have scent glands all over the place.
(0, 1, "plain", "The silver tabby cat stands side-on, with small soft glowing circles marking its cheeks, chin, the base of its tail and its paws. Clean educational look, no labels."),
# 98 On their cheeks. Their chin.
(0, 1, "room_close_afternoon", "Close-up of the silver tabby cat rubbing its cheek and chin against a leg of the wooden coffee table, eyes half closed."),
# 99 The base of the tail. And on their feet,
(0, 1, "room_afternoon", "The silver tabby cat walks past the open kitchen doorway, brushing the base of its tail along the doorframe, its white paws stepping on the wooden floorboards."),
# 100 in the pads and in between the toes.
(0, 1, "room_close_afternoon", "Extreme close-up of the underside of the silver tabby cat's white paw held up, showing soft pink toe pads and fur between the toes."),
# 101 Every step a cat takes leaves
(0, 1, "room_afternoon", "The silver tabby cat walks across the wooden floorboards, and each white paw step leaves a faint softly glowing paw print behind it."),
# 102 a faint trace of its smell behind it.
(0, 0, "hallway_afternoon", "A trail of faintly glowing cat paw prints runs along the wooden floorboards toward the front door, soft wisps of light rising from them. Nobody is in the hallway."),
# 103 You'll never notice. Another cat definitely will.
(1, 0, "hallway_afternoon", f"The Geek walks right past a glowing trail of paw prints without noticing, reading his phone, while {GINGER} in the foreground sniffs the floor with great interest."),
# 104 It's part of why cats scratch things, by the way.
(0, 1, "room_afternoon", "The silver tabby cat stands stretched up on its hind legs against a tall sisal-rope scratching post beside the bookshelf, front claws dug in, scratching."),
# 105 When your cat drags its claws down
(0, 1, "room_close_afternoon", "Close-up of the silver tabby cat's white front paws with claws out, dragging down the brown fabric of the sofa's arm, threads pulling loose."),
# 106 the side of the sofa you paid good money for,
(1, 1, "room_afternoon", "The Geek stands frozen with a deadpan horrified look holding a receipt, staring at the silver tabby cat scratching the arm of the brown sofa, shredded threads hanging down. No writing visible on the receipt."),
# 107 yes, it's sharpening, and yes, it's stretching.
(0, 1, "room_afternoon", "The silver tabby cat stretches its whole body long against a tall sisal-rope scratching post beside the bookshelf, front legs high, back arched, claws gripping the rope."),
# 108 But it's also leaving a scent mark.
(0, 1, "room_afternoon", "The silver tabby cat scratches a tall sisal-rope scratching post beside the bookshelf, and a soft faint glow of light rises from where its paws touch the rope, showing its scent being left behind."),
# 109 And a visible one.
(0, 0, "room_close_afternoon", "Close-up of the arm of the brown sofa covered in long claw marks and frayed threads, sunlight catching the damage. No animals in frame."),
# 110 Right there, at eye level, for everybody to see.
(0, 0, "cat_home", f"{cap(GINGER)} stands looking at shredded claw marks on the side of the cream sofa at its own eye level, inspecting them like a notice board."),
# 111 Kneading does the same job, only softer.
(0, 1, "room_close_evening", "The silver tabby cat gently kneads an olive-green cushion on the brown sofa, white paws pressing softly, eyes half closed."),
# 112 Each push of the paw presses a little of that scent
(0, 1, "room_close_evening", "Close-up of the silver tabby cat's white paw pressing down into the beige knitted throw, with a gentle faint glow spreading into the wool under the paw."),
# 113 into whatever's underneath. The blanket. The pillow.
(0, 1, "bedroom_night", "The silver tabby cat kneads a white pillow on the bed beside the folded-back white duvet, both softly glowing faintly where its paws have touched them."),
# 114 Your lap. So when your cat kneads you,
(1, 1, "room_evening", "The silver tabby cat kneads the Geek's lap on the brown sofa, and a faint soft glow spreads across his jeans under its white paws."),
# 115 it might also be quietly labeling you. Mine.
(1, 1, "room_evening", "The Geek sits on the brown sofa with a deadpan expression while the silver tabby cat kneads his lap, and a faint glowing paw-print shape rests on his green hoodie like a stamp of ownership."),
# 116 This one is mine.
(1, 1, "room_evening", "The silver tabby cat sits proudly on the Geek's chest as he lies along the brown sofa, one white paw placed firmly on him, looking straight out with calm confidence."),
# 117 Bit possessive? Sure. Very.
(1, 1, "kitchen_morning", "The silver tabby cat sits on the Geek's feet as he tries to walk to the fridge, pinning him in place, while he looks down with a deadpan expression."),
# 118 But from a cat's point of view
(0, 1, "room_evening", "A low view from the floor at cat eye level: the silver tabby cat's ears and the back of its head in the foreground, looking across the room at the brown sofa and the glowing floor lamp."),
# 119 it's also kind of a compliment.
(1, 1, "room_evening", "The Geek sits on the brown sofa looking pleasantly surprised behind his glasses as the silver tabby cat rubs its cheek against his chin."),
# 120 Cats only bother spreading their scent
(0, 1, "room_afternoon", "The silver tabby cat rubs its cheek along the rim of a round cream fluffy cat bed on the rug beside the bookshelf, eyes half closed, purring."),
# 121 on things they feel good about. Their bed.
(0, 1, "room_afternoon", "The silver tabby cat curled up contentedly in a round cream fluffy cat bed on the rug beside the bookshelf, eyes closed."),
# 122 Their favorite sunny spot. Their people.
(1, 1, "room_afternoon", "The silver tabby cat stretches out in a warm patch of sunlight on the beige rug right beside the Geek, who sits reading a book on the floor."),
# 123 You won't catch them marking the vacuum cleaner.
(0, 1, "room_afternoon", "The silver tabby cat sits well away from an upright vacuum cleaner standing by the kitchen doorway, ears back, eyes narrowed, giving it a cold suspicious stare."),
# 124 Now, there's one more theory,
(1, 0, "office_afternoon", "The Geek pins one more drawing, a picture of tall wild grass, onto the cork board beside drawings of a kitten, a paw print and a sleeping cat, with a thoughtful deadpan look. No writing on the board."),
# 125 and this one goes all the way back to the wild.
(0, 0, "savanna", "A wide view across the open grassland, the tall dry grass waving in the wind. No animals."),
# 126 Before sofas, before fleece throws,
(0, 0, "savanna", "A wide view of the wild grassland under the big orange sky, rocks and thorny bushes scattered through the grass. No animals."),
# 127 there was long grass and heaps of dry leaves.
(0, 0, "savanna_close", "A patch of tall, dry golden grass beside a heap of crunchy brown fallen leaves under a thorny bush."),
# 128 Wild cats, including the wildcats our house cats came from,
(0, 0, "savanna", f"{cap(WILDCAT)} stands alert at the edge of the tall dry grass."),
# 129 had to sleep wherever they could find a decent spot.
(0, 0, "savanna", f"{cap(WILDCAT)} looks around beneath a thorny bush, searching for a place to rest, tall grass all around."),
# 130 And a patch of long grass isn't a bed
(0, 0, "savanna_close", "A patch of tall uneven wild grass, stems sticking up in every direction, a few twigs poking out."),
# 131 until somebody flattens it.
(0, 0, "savanna", "A neatly flattened round circle of pressed-down grass in the middle of the tall dry grass, like a little nest. No animals."),
# 132 So the idea goes like this.
(1, 0, "office_afternoon", f"The Geek stands in front of a simple wooden easel showing a drawing of {WILDCAT} in grass, holding a pointer stick, in a deadpan teacher pose. No writing."),
# 133 A wild cat would trample
(0, 0, "savanna", f"{cap(WILDCAT)} stands in the tall grass, treading down the stems with its front paws, pressing them flat."),
# 134 and pat down its spot before lying in it.
(0, 0, "savanna", f"{cap(WILDCAT)} pats down a round patch of grass with its front paws, turning in a circle, preparing to lie down."),
# 135 Press the grass flat.
(0, 0, "savanna_close", "The sandy-brown front paws of an African wildcat press tall golden grass stems flat against the ground."),
# 136 Make sure there's nothing sharp in there,
(0, 0, "savanna", f"{cap(WILDCAT)} sniffs carefully at the flattened grass, nudging a sharp thorny twig out of the way with its nose."),
# 137 nothing alive, nothing nasty hiding underneath.
(0, 0, "savanna", f"{cap(WILDCAT)} peers down into the grass as a small beetle scuttles away from the flattened patch."),
# 138 Then curl up. If that's right,
(0, 0, "savanna", f"{cap(WILDCAT)} lies curled up asleep in a neat flattened nest of grass, tail wrapped around its nose."),
# 139 then when your cat kneads the duvet before bed,
(0, 1, "bedroom_night", "The silver tabby cat kneads the white duvet on the bed, both white front paws pressing in."),
# 140 turning in a circle and pushing the covers down,
(0, 1, "bedroom_night", "Top-down view of the bed: the silver tabby cat turns in a circle on the white duvet, pressing a round hollow into the covers."),
# 141 it's doing the exact same old job.
(0, 0, ("savanna", "bedroom_night"), f"In the left half, {WILDCAT} flattens a nest in the tall grass. In the right half, {ORANGE} presses a round hollow into the white duvet on the bed."),
# 142 Making the bed. Even though, let's be honest,
(0, 1, "bedroom_morning", "The silver tabby cat stands in the middle of the perfectly smooth, neatly made bed, kneading a big rumpled dent into the white duvet."),
# 143 the bed was already made.
(0, 0, "bedroom_morning", "The perfectly made bed: the white duvet tucked in neatly, the two white pillows plumped and lined up, everything tidy. Nobody in the room."),
# 144 You made it. This morning.
(1, 0, "bedroom_morning", "The Geek proudly smooths the white duvet on the neatly made bed, holding a white pillow, with a quietly satisfied deadpan look."),
# 145 To be fair, nobody's proven this one. It's tricky
(1, 0, "office_afternoon", "The Geek stands at the cork board and shrugs, holding a question-mark shaped piece of red string. No writing visible."),
# 146 to test what wild cats were thinking thousands of years ago,
(0, 0, "savanna", f"Night is falling and the first stars appear. {cap(WILDCAT)} sits on a rock, looking mysterious. No people anywhere."),
# 147 and they're not around to ask. But it does fit
(1, 0, "savanna", "The Geek stands in the tall grass holding a notebook and pen, looking around the empty grassland with a deadpan expression, no animals anywhere. No writing visible."),
# 148 with how often cats knead right before they lie down.
(0, 1, "room_close_evening", "The silver tabby cat kneads an olive-green cushion on the brown sofa, then begins to lower its body down onto it, eyes heavy, about to curl up for a nap."),
# 149 And dogs do something similar, don't they?
(0, 0, "cat_home", f"{cap(BEAGLE)} stands on a round dog bed on the braided rug, mid-way through turning in a circle, tail wagging."),
# 150 That whole spinning-in-circles routine before they finally flop over.
(0, 0, "cat_home", f"{cap(BEAGLE)} flops over onto its side in a round dog bed on the braided rug with a happy sigh, legs splayed, eyes closing."),
# 151 Kneading might also just feel nice.
(0, 1, "room_close_afternoon", "The silver tabby cat kneads the beige knitted throw on the brown sofa with a blissful expression, eyes nearly closed, whiskers relaxed."),
# 152 Watch a cat wake up from a nap.
(0, 1, "room_close_afternoon", "The silver tabby cat lifts its head sleepily from an olive-green cushion on the brown sofa, one eye opening, ears turning, just waking up."),
# 153 Out go the front legs, long and stiff.
(0, 1, "room_afternoon", "The silver tabby cat in a big long stretch on the beige rug, front legs pushed far out in front, back end raised, eyes squeezed shut."),
# 154 The toes spread. The claws flex.
(0, 1, "room_close_afternoon", "Close-up of the silver tabby cat's white front paws stretched out on the beige rug, toes spread wide apart and claws flexing out."),
# 155 Kneading works those same muscles. Push, release.
(0, 1, "room_close_afternoon", "The silver tabby cat kneads the beige knitted throw on the brown sofa, its shoulders and front legs working, one white paw pressing down and the other lifting."),
# 156 Push, release. A slow,
(0, 1, "room_close_afternoon", "Close-up of the silver tabby cat's white paws on the beige knitted throw, one pressing down slowly while the other relaxes and lifts."),
# 157 rhythmic stretch for the shoulders, the legs, the paws.
(0, 1, "room_close_afternoon", "Side view of the silver tabby cat kneading the beige knitted throw on the brown sofa, front legs extended, shoulder blades rolling, toes spreading with each slow push."),
# 158 If you've ever had a really good stretch
(1, 0, "bedroom_morning", "The Geek sits up in bed doing a huge stretch, arms high above his head, eyes squeezed shut, his glasses on the nightstand beside him."),
# 159 in bed first thing in the morning,
(1, 0, "bedroom_morning", "The Geek lies in bed under the white duvet, stretching his legs and arms out with a sleepy, contented look."),
# 160 you already know the feeling.
(1, 1, "bedroom_morning", "The Geek kneels on the bed and the silver tabby cat beside him stretches at the very moment he does, his arms raised high and the cat's front legs pushed out long on the white duvet."),
# 161 And then there's the calming side. Rhythm is soothing.
(0, 1, "room_close_evening", "The silver tabby cat kneads the beige knitted throw slowly and steadily, eyes calm and half closed, the room quiet."),
# 162 It is for us, anyway.
(1, 0, "room_evening", "The Geek sits on the brown sofa with eyes closed, calmly tapping his fingers on his knee in a steady rhythm, headphones around his neck."),
# 163 Think of rocking in a chair,
(0, 0, "porch", "An elderly man with a white beard and a brown cardigan rocks gently in a wooden rocking chair, eyes closed peacefully."),
# 164 or jiggling your foot under the desk
(1, 0, "office_afternoon", "A view under the wooden desk: the Geek's leg in charcoal-grey jeans bounces nervously, his canvas sneaker tapping the floor, while above the desk his hands rest on the silver laptop."),
# 165 when you're waiting on something.
(1, 0, "office_afternoon", "The Geek sits at the desk staring at the silver laptop showing a plain loading circle, chin on hand, foot tapping, with a bored deadpan look. No text on the screen."),
# 166 It seems to work for cats too.
(0, 1, "room_close_evening", "The silver tabby cat kneads an olive-green cushion on the brown sofa in a slow steady rhythm, its body visibly relaxing, ears soft."),
# 167 Plenty of cats knead when they're happy.
(0, 1, "room_afternoon", "The silver tabby cat kneads the beige knitted throw spread on the sunny windowsill, eyes closed contentedly, tail curled."),
# 168 But some knead when they're a little rattled.
(0, 1, "room_evening", "The silver tabby cat crouches on the beige knitted throw in the corner of the brown sofa, ears slightly back, eyes wide, kneading nervously with its white front paws."),
# 169 After a move. After a trip to the vet.
(0, 1, "moving_room", "The silver tabby cat sits among the moving boxes beside an open grey plastic cat carrier, looking around uneasily."),
# 170 When the house is loud and full of strangers.
(0, 1, "room_evening", "A busy noisy house party fills the room with chatting people holding drinks, while the silver tabby cat hides under the coffee table, ears flattened, eyes wide."),
# 171 It's a way to settle.
(0, 1, "bedroom_night", "The silver tabby cat sits on the white duvet in the quiet bedroom, kneading slowly, its ears coming back up, beginning to relax."),
# 172 The cat is, in its own way, comforting itself.
(0, 1, "bedroom_close_night", "The silver tabby cat curled up on the white duvet, eyes closing, one white paw still resting on the fabric after kneading, peaceful and calm."),
# 173 Female cats sometimes knead more at certain times, too.
(0, 0, "cat_home", f"{cap(TORTIE)}, a female, kneads a green cushion on the cream sofa with half-closed eyes."),
# 174 A cat in heat often gets extra cuddly,
(0, 0, "cat_home_kitchen", f"{cap(TORTIE)} rubs affectionately against a person's legs in blue jeans, tail high, body curving around their ankles. Only the person's legs show."),
# 175 rolling around on the floor, rubbing on everything in sight,
(0, 0, "cat_home", f"{cap(TORTIE)} rolls on its back on the wooden floor, twisting playfully, beside a leg of the side table it has just rubbed against."),
# 176 and yes, kneading. And a mother cat getting close
(0, 0, "cat_home", f"{cap(TORTIE)} kneads the braided rug with eyes half closed. Beside it, {CALICO_MOM} walks slowly across the room."),
# 177 to giving birth will often knead and paw at blankets,
(0, 0, "closet", f"{cap(CALICO_MOM)} paws and kneads at the heap of soft blankets on the closet floor."),
# 178 fussing over them,
(0, 0, "closet", f"{cap(CALICO_MOM)} tugs and rearranges the folds of a green blanket with her paws, carefully shaping it."),
# 179 getting a nest ready for the kittens on the way.
(0, 0, "closet", f"{cap(CALICO_MOM)} lies down in a cozy round nest she has made of the soft blankets in the corner of the closet, settled and waiting."),
# 180 So no, not every cat kneads for the same reason.
(0, 0, "plain", f"A row of four different cats, each kneading something different: {GINGER} on a pink blanket, {BLACK} on a red pillow, {CALICO} on a lap in blue jeans, and {CREAM} on a white fleece."),
# 181 And the same cat might knead for one reason
(0, 1, "room_morning", "The silver tabby cat kneads the beige knitted throw on the brown sofa, eyes bright and happy."),
# 182 on Tuesday and a totally different one on Friday.
(0, 1, "room_evening", "A thunderstorm outside: a flash of lightning in the dark window. The silver tabby cat kneads the beige knitted throw on the brown sofa, ears slightly back."),
# 183 Here's something else that surprises people.
(1, 0, "room_evening", "The Geek sits on the brown sofa raising his eyebrows above his glasses in mild surprise, holding a mug halfway to his mouth."),
# 184 Not every cat does it at all.
(0, 0, "cat_home", f"{cap(BLACK)} lies on the cream sofa simply resting, paws still and tucked neatly beneath it, not kneading, looking calm."),
# 185 Some cats knead every single evening, like clockwork.
(0, 0, "cat_home_evening", f"A round wall clock without numbers hangs above the cream sofa, where {ORANGE} kneads a grey fleece blanket."),
# 186 Some do it once in a blue moon.
(0, 0, "cat_home_evening", f"A big glowing blue full moon shines through the window, and {CALICO} sits on the windowsill kneading a green cushion in the moonlight."),
# 187 And some never seem to do it,
(0, 0, "cat_home", "A dignified fluffy black cat with yellow-green eyes sits upright on a green cushion on the cream sofa like a statue, paws together, perfectly still."),
# 188 at least not where you can see.
(0, 0, "cat_home_bedroom", f"Under the wooden bed, in the shadow, {ORANGE} secretly kneads a soft sweater on the floor, only partly visible."),
# 189 That's completely normal. A cat that doesn't knead isn't unhappy,
(0, 0, "cat_home", f"{cap(BLACK)} lies happily on the sunny windowsill, eyes half closed, purring and content, not kneading."),
# 190 and it doesn't love you any less.
(0, 0, "cat_home_evening", f"{cap(BLACK)} lies curled on the lap of a woman with long grey hair sitting on the cream sofa, her hand resting on its back, both content and calm."),
# 191 It just isn't its thing. And the styles!
(0, 0, "cat_home", f"Three cats sit in a row on the cream sofa, {GINGER}, {CALICO} and {CREAM}, each kneading in its own funny way."),
# 192 They're all over the place.
(0, 0, "cat_home", f"Several cats knead on different surfaces around the room: {CALICO} on the cream sofa, {GINGER} on the braided rug, and {CREAM} on a green cushion on the windowsill."),
# 193 Some cats only use the front paws.
(0, 0, "cat_home", f"{cap(CREAM)} kneads a green cushion on the cream sofa using only its front paws, its back legs folded neatly beneath it."),
# 194 Some throw the back paws in as well
(0, 0, "cat_home", f"{cap(GINGER)} stands on a grey fleece blanket on the cream sofa, kneading with its front paws while its back paws also tread up and down."),
# 195 and sort of march on the spot.
(0, 0, "cat_home", f"{cap(GINGER)} marches in place on a grey fleece blanket on the cream sofa, all four paws stepping up and down in turn, tail up."),
# 196 Some knead slow and dreamy,
(0, 0, "cat_home_evening", f"{cap(CALICO)} kneads a grey fleece blanket on the cream sofa very slowly with half-closed sleepy eyes."),
# 197 some like they're running late for something.
(0, 0, "cat_home", f"{cap(BLACK)} kneads a green cushion at a frantic pace, paws a blur, eyes wide, small motion lines around its paws."),
# 198 Some keep their claws tucked away politely.
(0, 0, "cat_home", f"Close-up of the soft cream paws of {CREAM} kneading a green velvet cushion on the cream sofa, claws neatly tucked away, gentle and polite."),
# 199 Others go full claws, every single one.
(0, 0, "cat_home", f"Close-up of the paws of {GINGER} kneading a grey fleece blanket with every sharp claw extended, hooking into the fabric."),
# 200 And then there are the cats that knead nothing at all,
(0, 0, "cat_home_evening", f"{cap(GINGER)} lies on its back on the cream sofa, front paws raised in the air above it, kneading empty space."),
# 201 just paws pumping away in empty air, eyes half closed,
(0, 0, "cat_home_evening", f"Close-up of {GINGER} lying on its back on the cream sofa, eyes half closed in bliss, both front paws in the air pressing at nothing in a kneading motion."),
# 202 off somewhere in their own head.
(0, 0, "cat_home_evening", f"{cap(GINGER)} lies on its back on the cream sofa kneading the air with a dreamy far-away look, a soft dreamy cloud above it with drifting fluffy biscuits."),
# 203 People call that making air biscuits,
(0, 0, "cat_home_evening", f"{cap(GINGER)} lies on its back on the cream sofa kneading the air, a few small golden round biscuits floating playfully above its paws."),
# 204 which might be the best phrase on the entire internet.
(1, 0, "office_evening", "The Geek sits at the desk looking at the silver laptop with a rare small satisfied smile, nodding approvingly. No text on the screen."),
# 205 It isn't only a house cat thing, either.
(0, 0, "sanctuary", "A wide view of the enclosure with no animals in sight, a big straw bed in the shade of the trees."),
# 206 Big cats do it too. Lions, tigers
(0, 0, "sanctuary", "A male lion with a golden mane and a striped orange tiger lie side by side on the grass, relaxed in the sun."),
# 207 and other big cats have been filmed kneading blankets and bedding,
(0, 0, "sanctuary", "A large striped orange tiger lies on a big brown blanket on a wooden platform, kneading it with its huge front paws, eyes half closed."),
# 208 purring away like a very large,
(0, 0, "sanctuary", "A large male lion with a golden mane lounges on a bed of straw, eyes closed in contentment, kneading slowly with enormous paws."),
# 209 very heavy version of the one
(0, 0, "sanctuary", "A huge striped orange tiger lies on a big brown blanket on a wooden platform, the blanket visibly squashed flat under its enormous heavy body, paws pressing down."),
# 210 on your couch. Okay.
(1, 1, "room_evening", "The silver tabby cat kneads the Geek's lap on the brown sofa while he holds a phone showing a plain photo of a tiger, glancing between the two with a deadpan look."),
# 211 Let's talk about the part that actually hurts.
(1, 1, "room_evening", "The Geek winces on the brown sofa, teeth clenched, as the silver tabby cat kneads his legs with claws out."),
# 212 The claws. When a cat pushes down with its paw,
(1, 1, "room_close_evening", "Close-up of the silver tabby cat's white front paw pressing down onto the Geek's charcoal-grey jeans as he sits on the brown sofa, sharp claw tips just starting to show. Only his lap and legs are in frame."),
# 213 it spreads its toes. And when it spreads its toes,
(1, 1, "room_close_evening", "Extreme close-up, seen from the side, of the silver tabby cat's white paw pressing down on the Geek's charcoal-grey jeans, its toes spreading wide apart. Only his lap is in frame."),
# 214 the claws tend to slide right out with them.
(1, 1, "room_close_evening", "Extreme close-up, seen from the side, of the silver tabby cat's white paw on the Geek's charcoal-grey jeans, toes spread wide, curved sharp claws sliding out and hooking into the denim. Only his lap is in frame."),
# 215 So a blissed-out cat kneading your lap can turn
(1, 1, "room_evening", "The silver tabby cat kneads the Geek's lap with eyes closed in pure bliss, while the Geek sits stiffly on the brown sofa with a worried look."),
# 216 into a little set of needles going
(0, 0, "room_close_evening", "Close-up of a row of tiny sewing needles poking up through a pincushion made of charcoal-grey denim, lying on the wooden coffee table. No animals in frame."),
# 217 in and out of your legs,
(1, 1, "room_close_evening", "Close-up on the Geek's thighs in charcoal-grey jeans as he sits on the brown sofa, the silver tabby cat's claws hooking in and out of the denim with each kneading push. Only his lap is in frame."),
# 218 one paw at a time.
(1, 1, "room_close_evening", "Close-up of the silver tabby cat's white paws on the Geek's charcoal-grey jeans, one lifted with claws out, the other pressing in. Only his lap is in frame."),
# 219 It's not doing it on purpose.
(1, 1, "room_evening", "The silver tabby cat kneads the Geek's lap on the brown sofa with a totally innocent, peaceful face, eyes closed, while he grimaces."),
# 220 It's not attacking you.
(0, 1, "room_close_evening", "The silver tabby cat lies peacefully on the beige knitted throw on the brown sofa with soft relaxed ears and closed eyes, nothing aggressive about it at all."),
# 221 In that moment it's so relaxed it isn't really keeping
(1, 1, "room_close_evening", "The silver tabby cat lies completely limp and blissful on the Geek's lap on the brown sofa, eyes shut, whiskers soft, body melted onto his charcoal-grey jeans. Only his lap shows."),
# 222 track of what its claws are up to.
(1, 1, "room_close_evening", "Close-up of the silver tabby cat's blissful sleepy face at the top of the frame while its white paws knead the Geek's charcoal-grey jeans with claws out below. Only his lap shows."),
# 223 So what do you do about it?
(1, 1, "room_evening", "The Geek sits on the brown sofa with the silver tabby cat on his lap, arms out, looking at the viewer with a helpless deadpan shrug."),
# 224 Well, first, don't punish it.
(1, 1, "room_evening", "The Geek sits on the brown sofa with the silver tabby cat on his lap, holding up one calm open hand, keeping his cool."),
# 225 Don't yell, and don't shove the cat off.
(1, 1, "room_evening", "The Geek sits still on the brown sofa, lips pressed together, resisting the urge to move, while the silver tabby cat stays on his lap."),
# 226 From the cat's side,
(1, 1, "room_close_evening", "A low view at cat eye level: the silver tabby cat in the foreground looks up with soft trusting eyes at the Geek's face as he sits on the brown sofa."),
# 227 it was showing you about as much trust
(1, 1, "room_evening", "The silver tabby cat lies on its back in the Geek's lap, white belly fully exposed, paws relaxed, as he sits on the brown sofa."),
# 228 and affection as a cat knows how to show.
(1, 1, "room_evening", "The silver tabby cat gently headbutts the Geek's chin as he sits on the brown sofa, eyes closed, while he looks touched."),
# 229 Tell it off for that,
(0, 0, "cat_home", f"{cap(WOMAN)} points sternly at {GINGER} sitting on the cream sofa, its ears flattening."),
# 230 and it may decide your lap isn't such a safe place
(0, 0, "cat_home", f"{cap(GINGER)} sits on the floor a few steps away from {WOMAN} sitting on the cream sofa, staring warily at her empty lap, ears slightly back."),
# 231 after all.
(0, 0, "cat_home_evening", f"{cap(GINGER)} walks away across the wooden floor toward a doorway with its tail held low, leaving the empty cream sofa behind it."),
# 232 Which is the last thing you want, really.
(1, 0, "room_evening", "The Geek sits alone on the brown sofa holding the beige knitted throw with a sad, deadpan expression, an empty spot on his lap."),
# 233 There are much easier fixes.
(1, 1, "room_evening", "The Geek sits upright on the brown sofa with a bright idea look, one finger raised, the silver tabby cat beside him."),
# 234 Keep the claws trimmed. Just the sharp tips,
(1, 1, "room_afternoon", "The Geek sits on the brown sofa gently holding the silver tabby cat on his lap and carefully trims the very tip of one claw with small cat nail clippers."),
# 235 carefully, and if you're not sure how,
(1, 1, "room_close_afternoon", "Close-up of the Geek's hands holding the silver tabby cat's white paw, gently pressing the pad so a claw shows, small cat nail clippers ready but hesitating."),
# 236 ask your vet to show you.
(1, 1, "clinic", f"{cap(VET)} shows the Geek how to trim the silver tabby cat's claws on the exam table."),
# 237 Throw a thick blanket or a folded towel over your lap
(1, 0, "room_evening", f"The Geek drapes {FLEECE} across his lap on the brown sofa, smoothing it flat."),
# 238 before the cat climbs on.
(1, 1, "room_evening", f"The silver tabby cat steps from the arm of the brown sofa onto {FLEECE} on the Geek's lap."),
# 239 Then it can knead to its heart's content
(1, 1, "room_evening", f"The silver tabby cat happily kneads {FLEECE} on the Geek's lap on the brown sofa, eyes half closed."),
# 240 and the claws hit fabric instead of you.
(1, 1, "room_close_evening", f"Close-up of the silver tabby cat's claws sinking harmlessly into {FLEECE} on the Geek's lap, while his relaxed hand rests nearby."),
# 241 You can also gently move its paws,
(1, 1, "room_close_evening", "Close-up of the Geek's hand gently lifting the silver tabby cat's white paw off his charcoal-grey jeans."),
# 242 or shift the cat over a bit,
(1, 1, "room_evening", "The Geek gently slides the silver tabby cat a little to one side on the brown sofa with both hands, moving it onto an olive-green cushion."),
# 243 so it's kneading the blanket beside you instead.
(1, 1, "room_evening", f"The silver tabby cat kneads {FLEECE} spread on the brown sofa cushion right next to the Geek, who sits relaxed beside it."),
# 244 And some people find that stroking the cat's back
(1, 1, "room_evening", "The Geek gently strokes the silver tabby cat's back with one hand as it kneads his lap on the brown sofa."),
# 245 while it kneads calms it down enough
(1, 1, "room_evening", "The silver tabby cat's kneading slows and its eyes close as the Geek strokes its back softly, sitting on the brown sofa."),
# 246 that it settles and lies down sooner.
(1, 1, "room_evening", "The silver tabby cat lies down curled up on the Geek's lap on the brown sofa, settled and asleep, while his hand rests on it."),
# 247 One thing you should never do is have a cat declawed
(0, 1, "plain", "The silver tabby cat sits upright with one white front paw raised, claws gently showing, looking calm and natural."),
# 248 to stop it. Declawing isn't some heavy-duty nail trim.
(0, 0, "room_close_afternoon", "A small pair of cat nail clippers lies on a white towel on the wooden coffee table beside a single tiny trimmed claw tip. No animals in frame."),
# 249 It removes the last bone of each toe.
(0, 0, "plain", "A clean simple educational diagram of a cat's paw shown side-on, with the small bones of the toes drawn in soft lines and the last bone of one toe highlighted in soft red. No labels."),
# 250 It's banned in a lot of countries,
(0, 0, "plain", "A soft simple world globe with many countries gently shaded in calm green. No labels."),
# 251 and vets and cat welfare groups widely oppose it.
(0, 0, "clinic", "Three vets in blue scrubs and two animal welfare volunteers in green t-shirts stand together, arms crossed, serious and united."),
# 252 Kneading is normal cat behavior.
(0, 1, "room_close_evening", "The silver tabby cat kneads the beige knitted throw on the brown sofa peacefully, a picture of normal, happy cat life."),
# 253 The answer is a blanket. Not surgery.
(1, 1, "room_evening", f"The Geek holds up {FLEECE} proudly, while the silver tabby cat sits beside him on the brown sofa looking at it with approval."),
# 254 Is kneading ever something to worry about?
(1, 1, "room_evening", "The Geek sits on the brown sofa with a slightly worried frown, watching the silver tabby cat knead an olive-green cushion."),
# 255 Mostly, no.
(1, 1, "room_evening", "The Geek relaxes back into the brown sofa with a calm deadpan face while the silver tabby cat kneads happily beside him."),
# 256 It's about as normal as cat behavior gets.
(0, 1, "room_afternoon", "The silver tabby cat kneads the beige knitted throw spread on the sunny windowsill, completely ordinary and calm."),
# 257 But there are a couple of things
(1, 0, "room_afternoon", "The Geek stands on the beige rug holding up two fingers, looking thoughtful."),
# 258 worth keeping an eye on. Sucking is one.
(0, 0, "cat_home_bedroom", f"{cap(TUXEDO)} on the bed holds a corner of the denim-blue fleece blanket in its mouth, sucking it gently, kneading with its front paws."),
# 259 A cat that sucks on a blanket now and then
(0, 0, "cat_home_bedroom", f"{cap(TUXEDO)} curled up on the denim-blue fleece blanket on the bed, briefly sucking its corner, eyes half closed."),
# 260 while it kneads is generally fine.
(0, 0, "cat_home_bedroom", f"{cap(TUXEDO)} kneads the denim-blue fleece blanket on the bed and then curls up peacefully on it, content and healthy."),
# 261 Some cats go further, though.
(0, 0, "cat_home_bedroom", f"{cap(SIAMESE)} stares intently at a grey wool sweater lying on the bed."),
# 262 They suck and chew on wool, on fabric,
(0, 0, "cat_home_bedroom", f"{cap(SIAMESE)} chews on the sleeve of a grey wool sweater on the bed, a small hole forming in the knit."),
# 263 even on plastic, and sometimes they swallow bits of it.
(0, 0, "cat_home_kitchen", f"{cap(SIAMESE)} chews on a plain plastic shopping bag with no writing on the kitchen floor, a few torn pieces scattered around."),
# 264 That's sometimes called wool sucking,
(0, 0, "cat_home_bedroom", f"Close-up of {SIAMESE} sucking on a ball of grey wool yarn on the bed."),
# 265 and it shows up more in certain breeds,
(0, 0, "cat_home", f"Two elegant cats sit side by side on the cream sofa: {SIAMESE}, and {BURMESE}."),
# 266 like Siamese and Burmese.
(0, 0, "plain", f"Portrait of two cats side by side: {BURMESE}, and {SIAMESE}."),
# 267 In some cats it's also thought to be linked
(0, 0, "cat_home", "A small cream-colored Siamese kitten with dark brown points and blue eyes sits alone in an empty cardboard box on the wooden floor, looking a little lonely."),
# 268 to being taken away from their mother too early.
(0, 0, "kitten_box", f"A tiny kitten is gently lifted out of the box by a person's hands, while {MOTHER} watches from the cream towels."),
# 269 If your cat is actually eating fabric,
(0, 0, "cat_home", f"{cap(SIAMESE)} swallows a strip of fabric torn from a grey fleece blanket on the braided rug, the blanket frayed beside it."),
# 270 have a chat with your vet,
(0, 0, "clinic", f"{cap(VET)} examines {SIAMESE} on the exam table while its owner, a young woman with a dark ponytail, listens."),
# 271 because swallowed cloth can block the gut.
(0, 0, "plain", "A simple clean educational illustration of a cat's side silhouette with a soft view of its stomach and gut, a small knot of cloth shown stuck inside. No labels."),
# 272 The other thing is change.
(1, 1, "room_evening", "The Geek sits on the brown sofa looking carefully at the silver tabby cat, attentive and watchful."),
# 273 If a cat that's always kneaded
(0, 1, "room_close_evening", "The silver tabby cat kneads the beige knitted throw on the brown sofa calmly, ordinary and relaxed."),
# 274 a little suddenly starts kneading all the time,
(0, 1, "room_evening", "Late at night: the silver tabby cat kneads the beige knitted throw on the brown sofa intensely with wide eyes, a round wall clock without numbers above the sofa, the window black."),
# 275 obsessively, or alongside other changes, like hiding,
(0, 1, "bedroom_night", "The silver tabby cat hides under the bed, only its eyes and white paws visible in the shadow."),
# 276 crying, or going off its food,
(0, 1, "kitchen_morning", "The silver tabby cat sits beside a full untouched food bowl on the checkered floor, mouth open in a sad meow, ears low."),
# 277 that can mean something's bothering it.
(0, 1, "room_evening", "The silver tabby cat is curled tightly in the corner behind the floor lamp, ears slightly flattened, looking unsettled."),
# 278 Stress, maybe. Or something physical.
(0, 1, "room_close_evening", "The silver tabby cat sits hunched on the beige knitted throw, eyes squinted, looking unwell and tense."),
# 279 Any time a cat's behavior shifts out of nowhere,
(1, 1, "room_evening", "The Geek kneels on the floor looking closely and with concern at the silver tabby cat, which is crouched quietly under the coffee table."),
# 280 a vet check is a smart idea.
(1, 1, "clinic", f"{cap(VET)} listens to the silver tabby cat with a stethoscope on the exam table while the Geek watches."),
# 281 Most of the time, though?
(1, 1, "room_evening", "The Geek sits back on the brown sofa with a relieved, calm look as the silver tabby cat walks along the cushion toward him."),
# 282 A kneading cat is a happy cat.
(0, 1, "room_close_evening", "The silver tabby cat kneads the beige knitted throw with eyes closed and a contented look."),
# 283 Or at the very least,
(1, 1, "room_evening", "The Geek tilts his head with a wry deadpan look, watching the silver tabby cat kneading on his lap on the brown sofa."),
# 284 an extremely comfortable one. So.
(0, 1, "room_close_evening", "The silver tabby cat completely melted into the beige knitted throw on the brown sofa, belly up, eyes closed, deeply comfortable."),
# 285 Why do cats knead you?
(1, 1, "room_evening", "The Geek sits on the brown sofa, the silver tabby cat kneading his lap, and he looks out at the viewer with a thoughtful deadpan expression."),
# 286 Because it's the very first thing they ever learned,
(0, 0, "kitten_box_close", f"A tiny newborn ginger kitten with sealed eyes kneads and nurses against {MOTHER}."),
# 287 on their very first day,
(0, 0, "kitten_box", f"{cap(MOTHER)} and her litter of newborn kittens all nestled together in the box."),
# 288 pressing into their mother for milk and warmth.
(0, 0, "kitten_box_close", "Tiny kitten front paws press into the soft white belly fur of a ginger-and-white mother cat while the kitten nurses."),
# 289 Because that feeling of being small
(0, 0, "kitten_box_close", f"A tiny cream kitten curled up asleep in the curve of the body of {MOTHER}, looking very small and safe."),
# 290 and safe never quite leaves them.
(0, 1, "room_close_evening", "The silver tabby cat, fully grown, curled up asleep on the beige knitted throw on the brown sofa, peaceful and safe."),
# 291 Because their paws carry their scent,
(0, 1, "room_close_evening", "Close-up of the silver tabby cat's white paw pressing into the beige knitted throw with a soft faint glow under the pads."),
# 292 and you're something they'd like to mark as theirs.
(1, 1, "room_evening", "The silver tabby cat rubs its cheek along the Geek's arm as he sits on the brown sofa, marking him as its own."),
# 293 Because it might be an old
(0, 0, "savanna", f"{cap(WILDCAT)} stands in the tall dry grass under the orange sky."),
# 294 wild habit of making a bed.
(0, 0, "savanna", f"{cap(WILDCAT)} curls up in a flattened round nest of grass."),
# 295 Because it's a good stretch.
(0, 1, "room_afternoon", "The silver tabby cat stretches long on the beige rug, front legs reaching far forward, toes spread, back end raised."),
# 296 And because, quite simply, it calms them down.
(0, 1, "room_close_evening", "The silver tabby cat kneads slowly on the beige knitted throw with eyes closing in calm contentment."),
# 297 But mostly, I think, because you feel safe.
(1, 1, "room_evening", "The silver tabby cat sleeps curled on the Geek's lap while he sits on the brown sofa, his hand resting on its back, both peaceful."),
# 298 A cat doesn't make biscuits for just anyone.
(0, 1, "room_evening", "The silver tabby cat sits on the brown sofa ignoring a stranger in a grey suit who sits beside it and pats his own lap invitingly, the cat looking away."),
# 299 It saves that for the warm, soft places
(0, 1, "room_close_evening", "The silver tabby cat kneads the beige knitted throw on the brown sofa in the warm golden glow of the floor lamp."),
# 300 where it can let its guard all the way down.
(0, 1, "room_close_evening", "The silver tabby cat lies on its back on the beige knitted throw, white belly up, paws curled, sound asleep, totally unguarded."),
# 301 So the next time the cat climbs onto your lap,
(1, 1, "room_evening", "The silver tabby cat climbs up onto the Geek's lap as he sits on the brown sofa, one white paw stepping onto his knee."),
# 302 turns around twice, and starts that slow left paw,
(1, 1, "room_evening", "The silver tabby cat turns in a circle on the Geek's lap on the brown sofa and begins kneading slowly with its left front paw."),
# 303 right paw, maybe grab a blanket.
(1, 1, "room_evening", f"The Geek reaches over and pulls {FLEECE} from the arm of the brown sofa as the silver tabby cat kneads his lap."),
# 304 Maybe trim those claws this weekend.
(1, 1, "room_morning", "The Geek sits on the beige rug with small cat nail clippers in hand and the silver tabby cat on his lap, looking calm."),
# 305 And take it as the compliment it is.
(1, 1, "room_evening", "The Geek sits on the brown sofa with a small, rare content smile, watching the silver tabby cat knead the beige knitted throw on his lap."),
# 306 That's a grown predator telling you,
(1, 1, "room_close_evening", "Close view of the silver tabby cat on the Geek's lap on the brown sofa, looking up at his face with soft trusting half-closed eyes."),
# 307 in the oldest language it knows,
(1, 1, "room_evening", "The silver tabby cat slow-blinks up at the Geek while kneading his lap on the brown sofa, and he slow-blinks back."),
# 308 that you feel like home.
(1, 1, "room_evening", "A wide view of the room at night, the Geek asleep along the brown sofa with the silver tabby cat curled on his chest, the floor lamp glowing."),
]
