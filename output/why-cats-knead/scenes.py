"""One image per segment in segments.json, in order: (geek in shot, silver tabby cat in shot, scene).

Each scene is standalone. Never refer to another image ("same room", "again", "earlier").
Other cats are never silver or grey tabbies, so they can't be mistaken for the Geek's cat.
"""
LIVING = ("A cozy small apartment living room in the evening, lit by one warm floor lamp: a worn brown sofa with a knitted "
          "throw, a low coffee table, a bookshelf, a houseplant and a rug.")

SCENES = [
# 1 You finally drop onto the couch.
(1, 0, LIVING + " The Geek flops down heavily onto the sofa cushions, arms loose, head tipped back, a tired deadpan expression, his canvas sneakers kicked off on the rug."),
# 2 Long day, sore feet, remote in hand.
(1, 0, LIVING + " The Geek slumps on the sofa in socks, feet up on the coffee table, a TV remote held limply in one hand pointed at a television just out of frame, eyes heavy."),
# 3 And before you've even found something to watch,
(1, 0, "Over-the-shoulder view from behind the Geek sitting on a worn brown sofa at night, holding a TV remote up toward a wall-mounted television that glows with a plain blue menu screen with no writing. Warm lamp light on one side of the room, a bookshelf and a plant."),
# 4 there's a weight on your lap. The cat.
(1, 1, LIVING + " The silver tabby cat has just stepped up onto the Geek's lap as he sits on the sofa, its white front paws planted on his thighs, looking at him. He holds the remote up and away, looking down at the cat with a flat, resigned expression."),
# 5 It turns around once. Then twice.
(1, 1, "Close view of the Geek's lap on a worn brown sofa in warm lamp light: the silver tabby cat is mid-turn on his charcoal-grey jeans, body curved in a circle, tail sweeping across his hoodie, while he holds his arms up out of the way."),
# 6 Then it gets to work.
(1, 1, LIVING + " The silver tabby cat stands squarely on the Geek's lap facing forward, front legs braced, ears up, focused like a worker clocking in. The Geek sits very still on the sofa, watching it with a deadpan look."),
# 7 Left paw, right paw. Left paw, right paw.
(1, 1, "Close-up on the Geek's thighs in charcoal-grey jeans as the silver tabby cat kneads them: one white front paw pressed down into the fabric, the other lifted mid-step. Warm evening lamp light, the edge of his green hoodie and a knitted throw visible."),
# 8 Slow, steady pushes into your thighs,
(1, 1, "Side view on a worn brown sofa in warm lamp light: the silver tabby cat stands on the Geek's lap, rhythmically pushing its white front paws into his legs, shoulders rolling with each push. The Geek sits back, hands raised slightly, watching."),
# 9 like a tiny baker who's got a lot of dough
(0, 0, "A warm old-fashioned bakery kitchen at dawn: a short round baker with a white apron and a flour-dusted bald head kneads a huge mound of bread dough on a wooden table, sleeves rolled up, flour everywhere, trays of loaves behind him."),
# 10 to get through before morning.
(0, 0, "A small bakery workbench at night lit by a single hanging bulb: a long row of unbaked bread dough balls waits on floured wooden boards, a rolling pin and a sack of flour beside them, a dark window showing the night sky with a thin moon."),
# 11 The eyes go half shut.
(0, 1, "Close-up portrait of the silver tabby cat in warm evening lamp light, resting on a person's green hoodie, its pale greenish-yellow eyes half shut and dreamy, ears relaxed, whiskers soft."),
# 12 The purring kicks in, loud as a little outboard motor.
(0, 1, "The silver tabby cat sits contentedly on a lap on a brown sofa, eyes closed, chest puffed, throat relaxed, soft curved lines rippling out from its body suggesting a deep rumbling purr. Warm evening lamp light, no text."),
# 13 And then, every so often,
(1, 1, LIVING + " The Geek sits stiffly upright on the sofa with the silver tabby cat kneading his lap, his eyes widening a little behind his glasses, bracing as if he knows something is coming."),
# 14 a claw goes right through your jeans
(1, 1, "Extreme close-up of the silver tabby cat's white paw pressing into charcoal-grey denim, one sharp curved claw poking clean through the fabric of the jeans. Warm lamp light, the weave of the denim visible."),
# 15 and you say something you wouldn't say
(1, 1, LIVING + " The Geek jolts on the sofa, mouth open mid-yelp, shoulders up, glasses slightly askew, while the silver tabby cat on his lap keeps kneading calmly with its eyes half closed."),
# 16 in front of your grandmother.
(0, 0, "A tidy old-fashioned sitting room: a kind elderly grandmother with white hair in a bun and a lilac cardigan sits in a floral armchair holding a teacup, one eyebrow raised in mild disapproval. Lace doilies, a ticking clock, a plate of biscuits on a side table."),
# 17 Kneading, people call it.
(0, 1, "Top-down view of the silver tabby cat kneading a thick cream knitted blanket on a sofa, both white front paws pressing into the wool, eyes half closed. Warm evening light."),
# 18 Online it's got a much better name. Making biscuits.
(0, 1, "A playful split image: on the left, the silver tabby cat kneading a soft blanket with its white front paws; on the right, a baking tray of golden fluffy round biscuits fresh from the oven. Warm cozy kitchen colors, no text."),
# 19 If you live with a cat,
(1, 1, "A cozy apartment hallway at the front door in the evening: the Geek comes home with a grocery bag and the silver tabby cat trots to meet him, tail up. Coat hooks, a shoe rack and warm lamp light."),
# 20 you've almost certainly been the biscuit.
(1, 1, "The Geek lies on his back on a living room rug in warm lamp light, arms at his sides, staring at the ceiling with a deadpan look, while the silver tabby cat stands on his chest kneading his green hoodie with both white front paws."),
# 21 But have you ever stopped to wonder why?
(1, 1, LIVING + " The Geek sits on the sofa with the silver tabby cat kneading his lap, and he tilts his head, chin on one hand, studying the cat with a thoughtful, puzzled look."),
# 22 Why would a grown animal, a predator,
(0, 1, "The silver tabby cat crouches low in tall garden grass at dusk in a stalking pose, body flat, eyes locked forward, ears pricked, every muscle tense like a small hunter. Hedges and a fence in the background."),
# 23 built to stalk and pounce,
(0, 1, "The silver tabby cat leaps through the air in a garden at dusk, front white paws stretched out and claws spread, pouncing on a fluttering moth above the grass. Dynamic action, hedges and flowers behind."),
# 24 climb onto a person and start kneading them like bread?
(1, 1, LIVING + " The silver tabby cat stands on the Geek's lap kneading his stomach like dough while he sits on the sofa holding a bread roll in one hand, looking from the roll to the cat with a flat expression."),
# 25 It goes back a long way. All the way back
(0, 0, "A gentle dreamy scene of a spiral of soft warm light leading back through time, with small drifting images of a cat's life getting smaller along it: an adult cat, a young cat, a kitten, and at the far end a tiny newborn kitten. Soft golden tones, no text."),
# 26 to the first day of a cat's life, actually.
(0, 0, "A soft blanket in a warm cardboard birthing box: a ginger-and-white mother cat lies on her side, and one tiny newborn ginger kitten, eyes sealed shut, damp fur, curls against her belly. Soft warm light."),
# 27 And the answer isn't one neat thing.
(1, 0, "The Geek stands at a cork board in a small home office, looking at four pinned drawings with strings between them: a kitten, a paw print, a pile of grass and a sleeping cat. He scratches his head with a deadpan, puzzled look. No text on the board."),
# 28 It's a baby habit, a comfort thing,
(0, 0, "Two side-by-side vignettes: on the left a tiny ginger kitten nursing against its ginger-and-white mother; on the right an adult cream cat curled on a fluffy blanket, eyes closed, perfectly comfortable. Soft warm light, no text."),
# 29 a kind of signature,
(0, 0, "Close-up of a single cat paw print pressed into soft fresh flour on a dark wooden table, like a signature, with a faint glowing trail rising from it. Warm kitchen light."),
# 30 and maybe a leftover from the wild too,
(0, 0, "A sandy-brown African wildcat with faint stripes stands in tall dry grassland at sunset, looking out across the savanna, an acacia tree in the distance."),
# 31 all tangled up together. So let's untangle it.
(0, 1, "The silver tabby cat sits in the middle of a living room rug wrapped in a big tangle of red wool yarn, looking up with wide eyes, a knitting basket tipped over beside it. Warm light."),
# 32 First, the first day.
(0, 0, "A quiet warm laundry room corner at night: a cardboard box lined with towels where a ginger-and-white mother cat lies curled protectively around a small litter of newborn kittens. A soft night light glows."),
# 33 A kitten comes into the world blind and deaf.
(0, 0, "Close-up of a single tiny newborn cream kitten on a soft towel, eyes sealed shut, small folded-down ears, tiny pink nose, wobbly head raised. Warm gentle light."),
# 34 Its eyes stay sealed shut
(0, 0, "Extreme close-up of a sleeping newborn ginger kitten's face, its eyes tightly sealed shut, a tiny pink nose and fine whiskers, nestled in soft fur. Warm light."),
# 35 for roughly the first week or two.
(0, 0, "A small litter of three-week-old kittens, ginger, black and calico, on a fleece blanket in a box, their eyes freshly opened and blue, blinking at the world for the first time. Warm indoor light."),
# 36 It can't walk properly. It can't keep itself warm.
(0, 0, "A tiny newborn tortoiseshell kitten wobbles on a blanket, legs splayed out, belly dragging, trying to crawl, shivering slightly beside a warm water bottle wrapped in a towel. Soft light."),
# 37 Honestly, it can't do much of anything,
(0, 0, "A tiny newborn black kitten lies flat on its belly on a towel, legs spread out like a starfish, eyes shut, completely helpless and sleepy. Warm indoor light."),
# 38 except find its mother and eat.
(0, 0, "A litter of newborn kittens, ginger, cream and calico, eyes shut, crawl toward and nurse along the belly of a ginger-and-white mother cat lying on her side in a towel-lined box. Warm light."),
# 39 And that's where kneading starts. When a newborn kitten nurses,
(0, 0, "Close-up of a tiny newborn ginger kitten nursing at its ginger-and-white mother's belly, eyes shut, both tiny front paws pressed into her soft fur. Warm gentle light."),
# 40 it pushes against its mother's belly with its front paws,
(0, 0, "Very close view of two tiny kitten front paws, pink toe pads spread, pushing into the soft cream fur of a mother cat's belly. Warm light."),
# 41 one after the other. Push, push, push.
(0, 0, "A row of three newborn kittens, ginger, cream and calico, nursing side by side at a ginger-and-white mother cat's belly, each pushing with alternating little front paws in rhythm. Warm cozy light."),
# 42 That pressure on the milk glands helps get the milk flowing.
(0, 0, "A gentle simple educational cross-section style illustration of a mother cat's belly, with soft glowing warm lines showing milk flowing toward a nursing kitten whose paws press against her. Clean diagram look, warm colors, no labels or text."),
# 43 More pushing, more milk. Simple deal.
(0, 0, "A plump content newborn ginger kitten with a round full belly lies asleep on its back against its mother's soft cream fur, a tiny drop of milk at the corner of its mouth. Warm light."),
# 44 Kittens start doing it in their very first days,
(0, 0, "A tiny newborn calico kitten, umbilical stump still visible, eyes shut, kneading its mother's belly with little front paws in a towel-lined box. Soft warm light."),
# 45 long before they can even see what they're pushing on.
(0, 0, "Close-up of a newborn black kitten with its eyes sealed shut, kneading and nursing blindly against the fluffy ginger fur of its mother. Warm dim light."),
# 46 Nobody shows them how.
(0, 0, "A ginger-and-white mother cat sleeps with her eyes closed while her small newborn kittens knead and nurse on their own, all by instinct. Quiet warm nest in a box."),
# 47 It's just there, wired in from the start.
(0, 0, "A soft glowing outline drawing of a tiny kitten curled up, with a gentle warm light pulsing from its little front paws, like instinct shining from inside. Calm dark blue background, no text."),
# 48 So picture what kneading means
(1, 0, "The Geek sits on a living room rug with eyes closed and a calm expression, as if imagining, with a soft dreamy cloud above his head showing a mother cat nursing a litter of kittens. Warm light, no text."),
# 49 to a kitten in those first few weeks.
(0, 0, "A two-week-old cream kitten with freshly opened blue eyes nestles against its ginger-and-white mother in a warm towel-lined box. Soft afternoon light."),
# 50 It means warmth. Food. A big purring mother.
(0, 0, "A large fluffy ginger-and-white mother cat lies on her side, eyes closed, purring contentedly, a litter of kittens nursing along her belly, all tucked under a warm lamp glow in a towel-lined box."),
# 51 A heap of brothers and sisters all squashed together.
(0, 0, "A cozy heap of five sleeping kittens, ginger, black, calico, cream and tortoiseshell, piled on top of each other in a soft fleece bed, paws and tails tangled together."),
# 52 Pretty much everything good
(0, 0, "A warm glowing nest box: a ginger-and-white mother cat curled around her sleeping kittens, a soft blanket, gentle golden light, a full feeling of safety and comfort."),
# 53 in its whole little world happens while those paws are going.
(0, 0, "Close-up of a nursing ginger kitten's tiny front paws kneading its mother's soft belly fur, its eyes closed in bliss, surrounded by warm golden light."),
# 54 Then the kitten grows up,
(0, 0, "A playful side-by-side: a tiny newborn ginger kitten on the left and the same breed of ginger kitten at eight weeks on the right, bigger, eyes open, tail up, standing confidently. Plain warm background, no text."),
# 55 the way kittens do, which is fast.
(0, 0, "A lively living room floor where three young kittens, ginger, black and calico, tumble and chase each other at full speed across a rug, a toy ball rolling away."),
# 56 Somewhere around eight weeks or so, it's weaned.
(0, 0, "A young ginger kitten about eight weeks old eats from a small shallow dish of wet kitten food on a kitchen floor, its ginger-and-white mother sitting calmly nearby."),
# 57 Solid food now. It's off exploring, wrestling its siblings,
(0, 0, "Two young kittens, a ginger one and a black one, wrestle and roll together on a living room rug, paws batting, mouths open in play. Sunny afternoon light."),
# 58 ambushing its first toy mouse.
(0, 0, "A young ginger kitten pounces from behind a sofa leg onto a small grey felt toy mouse on a wooden floor, ears forward, eyes wide."),
# 59 The milk is long gone.
(0, 0, "A grown ginger cat sits beside its empty food bowl in a sunny kitchen, looking alert and independent, no mother cat or kittens around."),
# 60 The kneading, though? That stays.
(0, 1, "The silver tabby cat, fully grown, kneads a soft fleece blanket on a sofa, eyes half closed, both white front paws pressing down. Warm evening lamp light."),
# 61 And that's the first big reason your cat kneads you.
(1, 1, LIVING + " The silver tabby cat kneads the Geek's lap while he sits on the sofa, and he looks down at it with a soft, understanding expression."),
# 62 It's kitten behavior that never got switched off.
(0, 1, "The silver tabby cat kneads a cushion on a sofa, while above it a soft glowing ghost-like outline of a tiny kitten does the exact matching kneading motion, showing the kitten inside the adult. Warm light, no text."),
# 63 A surprising amount of what house cats
(0, 1, "The silver tabby cat sits on a windowsill in a bright living room, gazing out, a calm grown-up house cat. Plants on the sill, sunlight."),
# 64 do as grownups is really baby stuff that just stuck around.
(0, 1, "The silver tabby cat, fully grown, lies on its back on a rug playing with a dangling feather toy like a kitten, all four white paws in the air. Sunlit living room."),
# 65 They meow at us,
(1, 1, "A small kitchen in morning light: the silver tabby cat sits on the floor looking up at the Geek with its mouth open in a meow, while he stands holding a coffee mug, looking down with a deadpan expression."),
# 66 even though adult cats hardly ever meow at each other.
(0, 0, "Two adult cats, a ginger cat and a black cat, sit facing each other on a garden wall, communicating silently with tails and ears, their mouths closed. Calm afternoon light."),
# 67 They trot up to us with their tails held straight up,
(1, 1, "An apartment hallway in warm afternoon light: the silver tabby cat trots happily toward the Geek with its tail held straight up like a flag, a little hook at the tip, while he crouches with one hand out."),
# 68 the way a kitten greets its mother.
(0, 0, "A small cream kitten trots toward its ginger-and-white mother cat across a sunny barn floor, its tiny tail held straight up in greeting, the mother leaning down to sniff it."),
# 69 And they knead.
(0, 1, "Close-up of the silver tabby cat's white front paws kneading a soft knitted blanket, one paw pressing, one lifted. Warm cozy light."),
# 70 Think about when your cat actually does it.
(1, 1, "The Geek sits at a kitchen table with a notepad, tapping his chin with a pencil, watching the silver tabby cat across the room curled on a sofa. Warm afternoon light, no writing visible."),
# 71 Usually it's relaxed. Sprawled on a soft blanket,
(0, 1, "The silver tabby cat sprawls on its side across a soft fluffy cream blanket on a bed, totally relaxed, legs stretched out, eyes half closed. Warm sunlight from a window."),
# 72 settled on a warm lap, drifting toward a nap.
(1, 1, "Close view of the Geek's lap on a sofa in warm lamp light: the silver tabby cat curled up in a loaf shape on his green hoodie and jeans, eyes slowly closing, while his hand rests gently on its back."),
# 73 Its whole body is saying, this feels like being a kitten
(0, 1, "The silver tabby cat lies completely relaxed on a fluffy blanket, paws tucked, eyes closed, a faint glowing kitten-shaped outline curled up around it like a warm memory. Soft golden light, no text."),
# 74 again. Safe. Warm. Fed.
(0, 1, "The silver tabby cat curled up asleep beside a warm radiator on a soft cushion, an empty licked-clean food bowl nearby, cozy evening light, a feeling of complete safety."),
# 75 And the paws just go back to the thing they used
(0, 1, "Close-up of the silver tabby cat's white front paws starting to knead a soft fleece throw, toes spreading, as the cat's half-closed eyes are visible above. Warm light."),
# 76 to do when life felt exactly like this.
(0, 0, "A tiny newborn ginger kitten kneading and nursing at its mother's warm belly in a soft towel-lined box, glowing warm light all around, a calm and peaceful feeling."),
# 77 Look closely and you'll often catch other kitten signs tagging along.
(1, 1, "The Geek leans in close with a magnifying glass, peering at the silver tabby cat kneading a blanket on the sofa, with a curious deadpan expression. Warm lamp light."),
# 78 The purring, for one. Kittens purr while they nurse,
(0, 0, "A litter of kittens, ginger, calico and cream, nursing contentedly at their ginger-and-white mother's belly, eyes closed, throats relaxed, soft gentle curved lines in the air suggesting a quiet purr. Warm light, no text."),
# 79 and the mother purrs right back at them.
(0, 0, "A ginger-and-white mother cat with half-closed eyes, curled around her nursing kittens, her chin resting on one of them, soft gentle curved lines around her throat suggesting a purr. Cozy box, warm light, no text."),
# 80 Some cats drool while they knead, which is a bit gross,
(0, 0, "A plump orange cat kneads a fleece blanket with half-closed blissful eyes, a small shiny drop of drool hanging from its chin. Warm lamp light."),
# 81 I'll admit, and a bit baffling
(1, 0, "The Geek sits on a sofa holding up his sleeve and looking at a small damp drool spot on his green hoodie with a deadpan, mildly disgusted expression. Warm lamp light."),
# 82 until you remember what kneading used to bring. A drooling,
(0, 0, "A small dreamy thought bubble picture of a newborn kitten happily nursing, floating above a plump orange cat that kneads a blanket with a little drool on its chin. Warm light, no text."),
# 83 kneading cat is, more or less, remembering milk.
(0, 0, "A plump orange cat kneading a cushion with eyes closed in bliss, and a soft glowing image of a small saucer of milk floating gently above its head like a memory. Warm cozy light, no text."),
# 84 And some cats take it one step further
(0, 0, "A black-and-white tuxedo cat lies on a bed holding the corner of a fleece blanket in its front paws, eyes half closed, about to put the blanket corner into its mouth. Warm bedroom light."),
# 85 and suck on a blanket, or your sleeve,
(1, 0, "The Geek sits on a sofa with a deadpan expression while a black-and-white tuxedo cat on his lap gently sucks on the cuff of his green hoodie sleeve, kneading his arm. Warm lamp light."),
# 86 or a soft toy, kneading away the whole time.
(0, 0, "A black-and-white tuxedo cat curls around a plush teddy bear on a bed, sucking on the bear's ear while kneading its soft belly with both front paws. Cozy bedroom light."),
# 87 Nursing on fleece, basically.
(0, 0, "Close-up of a black-and-white tuxedo cat with eyes closed, softly sucking a corner of a fuzzy fleece blanket like a kitten nursing, front paws kneading. Warm light."),
# 88 So when your cat climbs aboard and starts making biscuits,
(1, 1, LIVING + " The silver tabby cat climbs onto the Geek's lap from the sofa arm, one white paw already on his thigh, as he lowers his book to make room."),
# 89 there's a real sense in which it's
(1, 1, "The Geek sits on a sofa with the silver tabby cat kneading his lap, and behind him on the wall a soft glowing picture of a mother cat with her kitten appears like a thought. Warm lamp light, no text."),
# 90 treating you a little bit like its mom.
(1, 1, "The silver tabby cat kneads the Geek's chest as he lies back on the sofa, while in a soft dreamy thought bubble above the cat a mother cat nurses her kittens. Warm light, no text."),
# 91 You're warm, you're soft, you're safe, and, crucially,
(1, 1, "The Geek wrapped in a fluffy blanket on a sofa like a warm burrito, the silver tabby cat curled up contentedly on top of him. Soft warm lamp light, cozy and safe."),
# 92 you're the one who fills the food bowl.
(1, 1, "A small kitchen: the Geek crouches and pours dry cat food from a bag into a bowl on the floor, while the silver tabby cat watches eagerly beside it, tail up."),
# 93 From where the cat's sitting, which is on you,
(1, 1, "A low view from the silver tabby cat's point of view: the cat sits on the Geek's chest as he lies on a sofa, looking down at his face with round glasses and a deadpan expression. Warm lamp light."),
# 94 that's a pretty good job description for a mother.
(1, 1, "The Geek sits on a sofa with the silver tabby cat in his arms like a baby, its white belly up, its paws relaxed, and he looks down at it with a calm, fond deadpan expression."),
# 95 Comfort isn't the whole story though.
(1, 1, LIVING + " The Geek sits on the sofa with the silver tabby cat kneading his lap, holding up one finger as if remembering something."),
# 96 There's something else going on under those paws.
(0, 1, "Close-up low view of the silver tabby cat's white paw pressing down onto a blanket, with soft glowing dots of light rising from between its toe pads. Warm light, no text."),
# 97 Cats have scent glands all over the place.
(0, 1, "The silver tabby cat stands side-on against a plain warm background, with small soft glowing circles marking its cheeks, chin, the base of its tail and its paws. Clean educational look, no labels, no text."),
# 98 On their cheeks. Their chin.
(0, 1, "Close-up of the silver tabby cat rubbing its cheek and chin against the corner of a wooden table leg, eyes half closed. Warm indoor light."),
# 99 The base of the tail. And on their feet,
(0, 1, "The silver tabby cat walks past, brushing the base of its tail along a doorframe, its white paws visible stepping on a wooden floor. Warm afternoon light."),
# 100 in the pads and in between the toes.
(0, 1, "Extreme close-up of the underside of the silver tabby cat's white paw held up, showing soft pink toe pads and fur between the toes. Gentle warm light."),
# 101 Every step a cat takes leaves
(0, 1, "The silver tabby cat walks across a wooden floor, and each white paw step leaves a faint softly glowing paw print behind it. Warm evening light, no text."),
# 102 a faint trace of its smell behind it.
(0, 0, "A trail of faintly glowing cat paw prints running along a hallway floor and fading into the distance, soft wisps of light rising from them. Dim warm light."),
# 103 You'll never notice. Another cat definitely will.
(1, 0, "A hallway: the Geek walks right past a glowing trail of paw prints without noticing, reading his phone, while a ginger cat in the foreground sniffs the floor with great interest."),
# 104 It's part of why cats scratch things, by the way.
(0, 1, "The silver tabby cat stands stretched up on its hind legs against a sisal scratching post, front claws dug in, scratching. Living room in warm afternoon light."),
# 105 When your cat drags its claws down
(0, 1, "Close-up of the silver tabby cat's white front paws with claws out dragging down the fabric side of a brown sofa, threads pulling loose."),
# 106 the side of the sofa you paid good money for,
(1, 1, "A living room: the Geek stands frozen with a deadpan horrified look holding a receipt, staring at the silver tabby cat scratching the side of a brand-new brown sofa, shredded threads hanging down. No writing visible on the receipt."),
# 107 yes, it's sharpening, and yes, it's stretching.
(0, 1, "The silver tabby cat stretches its whole body long against a scratching post, front legs high, back arched, claws gripping the sisal rope. Warm afternoon light."),
# 108 But it's also leaving a scent mark.
(0, 1, "The silver tabby cat scratches a scratching post, and a soft faint glow of light rises from where its paws touch the sisal, showing its scent being left behind. Warm light, no text."),
# 109 And a visible one.
(0, 0, "Close-up of the scratched side of a brown sofa covered in long claw marks and frayed threads, sunlight from a window catching the damage."),
# 110 Right there, at eye level, for everybody to see.
(0, 0, "A ginger cat stands in a living room looking at shredded claw marks on the side of a sofa at its own eye level, inspecting them like a notice board. Warm light."),
# 111 Kneading does the same job, only softer.
(0, 1, "The silver tabby cat gently kneads a fluffy cushion on a sofa, white paws pressing softly, eyes half closed. Soft warm evening light."),
# 112 Each push of the paw presses a little of that scent
(0, 1, "Close-up of the silver tabby cat's white paw pressing down into a soft blanket, with a gentle faint glow spreading into the fabric under the paw. Warm light, no text."),
# 113 into whatever's underneath. The blanket. The pillow.
(0, 1, "The silver tabby cat kneads a pillow on a bed beside a folded fluffy blanket, both softly glowing faintly where its paws have touched them. Cozy bedroom light."),
# 114 Your lap. So when your cat kneads you,
(1, 1, LIVING + " The silver tabby cat kneads the Geek's lap on the sofa, and a faint soft glow spreads across his jeans under its white paws."),
# 115 it might also be quietly labeling you. Mine.
(1, 1, "The Geek sits on a sofa with a deadpan expression while the silver tabby cat kneads his lap, and a faint glowing paw-print shape rests on his green hoodie like a stamp of ownership. Warm light, no text."),
# 116 This one is mine.
(1, 1, "The silver tabby cat sits proudly on the Geek's chest as he lies on a sofa, one white paw placed firmly on him, looking straight out with calm confidence."),
# 117 Bit possessive? Sure. Very.
(1, 1, "A small kitchen: the silver tabby cat sits on the Geek's feet as he tries to walk to the fridge, pinning him in place, while he looks down with a deadpan expression."),
# 118 But from a cat's point of view
(0, 1, "A low view from the floor at cat eye level: the silver tabby cat's ears and the back of its head in the foreground, looking across a cozy living room at a sofa and a warm lamp."),
# 119 it's also kind of a compliment.
(1, 1, "The Geek sits on a sofa looking pleasantly surprised behind his glasses as the silver tabby cat rubs its cheek against his chin. Warm lamp light."),
# 120 Cats only bother spreading their scent
(0, 1, "The silver tabby cat rubs its cheek along the corner of its own cushioned cat bed, eyes half closed, purring. Warm afternoon light."),
# 121 on things they feel good about. Their bed.
(0, 1, "The silver tabby cat curled up contentedly in a round fluffy cat bed beside a radiator, eyes closed. Soft warm light."),
# 122 Their favorite sunny spot. Their people.
(1, 1, "A living room in golden afternoon light: the silver tabby cat stretches out in a warm patch of sunlight on the rug right beside the Geek, who sits reading on the floor."),
# 123 You won't catch them marking the vacuum cleaner.
(0, 1, "A living room: the silver tabby cat sits well away from an upright vacuum cleaner standing in the corner, ears back, eyes narrowed, giving it a cold suspicious stare."),
# 124 Now, there's one more theory,
(1, 0, "The Geek stands beside a cork board in a home office and pins up one more drawing, a picture of tall wild grass, with a thoughtful deadpan look. No writing on the board."),
# 125 and this one goes all the way back to the wild.
(0, 0, "A wide view of an open African savanna at golden hour, tall dry grass waving in the wind, a lone acacia tree and distant hills."),
# 126 Before sofas, before fleece throws,
(0, 0, "A wild open grassland at dusk with no buildings anywhere, tall golden grass, a few rocks and bushes, a big orange sky."),
# 127 there was long grass and heaps of dry leaves.
(0, 0, "Close view of a patch of tall, dry golden grass beside a heap of crunchy brown fallen leaves under a bush, in soft evening light."),
# 128 Wild cats, including the wildcats our house cats came from,
(0, 0, "A sandy-brown African wildcat with faint stripes and long legs stands alert at the edge of tall dry grass in warm evening light."),
# 129 had to sleep wherever they could find a decent spot.
(0, 0, "A sandy-brown African wildcat with faint stripes looks around beneath a thorny bush at dusk, searching for a place to rest, tall grass all around."),
# 130 And a patch of long grass isn't a bed
(0, 0, "Close view of a patch of tall uneven wild grass, stems sticking up in every direction, a few twigs poking out. Soft evening light."),
# 131 until somebody flattens it.
(0, 0, "A neatly flattened round circle of pressed-down grass in the middle of tall wild grass, like a little nest, in warm evening light."),
# 132 So the idea goes like this.
(1, 0, "The Geek stands in front of a simple wooden easel showing a drawing of a wild cat in grass, holding a pointer stick, with a deadpan teacher pose. No writing."),
# 133 A wild cat would trample
(0, 0, "A sandy-brown African wildcat with faint stripes stands in tall grass, treading down the stems with its front paws, pressing them flat. Golden evening light."),
# 134 and pat down its spot before lying in it.
(0, 0, "A sandy-brown African wildcat with faint stripes pats down a round patch of grass with its front paws, turning in a circle, preparing to lie down. Dusk light."),
# 135 Press the grass flat.
(0, 0, "Close-up of a wild cat's sandy-brown front paws pressing tall green-gold grass stems flat against the ground. Warm low sunlight."),
# 136 Make sure there's nothing sharp in there,
(0, 0, "A sandy-brown African wildcat with faint stripes sniffs carefully at the flattened grass, nudging a sharp thorny twig out of the way with its nose. Evening light."),
# 137 nothing alive, nothing nasty hiding underneath.
(0, 0, "A sandy-brown African wildcat with faint stripes peers down into the grass as a small beetle scuttles away from the flattened patch. Warm dusk light."),
# 138 Then curl up. If that's right,
(0, 0, "A sandy-brown African wildcat with faint stripes curled up asleep in a neat flattened nest of grass, tail wrapped around its nose, under a deep orange dusk sky."),
# 139 then when your cat kneads the duvet before bed,
(0, 1, "A cozy bedroom at night with a soft bedside lamp: the silver tabby cat kneads a puffy white duvet on the bed, both white front paws pressing in."),
# 140 turning in a circle and pushing the covers down,
(0, 1, "Top-down view of a bed at night: the silver tabby cat turns in a circle on a puffy duvet, pressing a round hollow into the covers. Warm lamp light."),
# 141 it's doing the exact same old job.
(0, 0, "A split image: on the left a sandy-brown African wildcat flattening a nest in tall grass at dusk; on the right a cozy bedroom where a pet cat presses a hollow into a duvet. Warm colors, no text."),
# 142 Making the bed. Even though, let's be honest,
(0, 1, "The silver tabby cat stands in the middle of a perfectly smooth, neatly made bed, kneading a big rumpled dent into the duvet. Bright morning bedroom light."),
# 143 the bed was already made.
(0, 0, "A perfectly made bed in a sunny bedroom, crisp white duvet tucked in neatly, pillows plumped and lined up, everything tidy."),
# 144 You made it. This morning.
(1, 0, "A bright bedroom in the morning: the Geek proudly smooths a crisp white duvet on his neatly made bed, holding a pillow, with a quietly satisfied deadpan look."),
# 145 To be fair, nobody's proven this one. It's tricky
(1, 0, "The Geek stands at a cork board in a home office and shrugs, holding a question-mark shaped piece of string. No writing visible."),
# 146 to test what wild cats were thinking thousands of years ago,
(0, 0, "An ancient landscape at dusk with a sandy-brown wild cat sitting on a rock, looking mysterious, beneath a sky full of early stars, no people or buildings."),
# 147 and they're not around to ask. But it does fit
(1, 0, "The Geek stands in tall grass holding a notebook and pen, looking around an empty savanna with a deadpan expression, no animals anywhere. Golden light, no writing visible."),
# 148 with how often cats knead right before they lie down.
(0, 1, "The silver tabby cat kneads a soft cushion, then begins to lower its body down onto it, eyes heavy, about to curl up for a nap. Warm evening light."),
# 149 And dogs do something similar, don't they?
(0, 0, "A cozy living room: a friendly brown-and-white beagle stands on a round dog bed, mid-way through turning in a circle, tail wagging."),
# 150 That whole spinning-in-circles routine before they finally flop over.
(0, 0, "A brown-and-white beagle flops over onto its side in a round dog bed with a happy sigh, legs splayed, eyes closing. Warm living room light."),
# 151 Kneading might also just feel nice.
(0, 1, "The silver tabby cat kneads a fluffy blanket with a blissful expression, eyes nearly closed, whiskers relaxed. Warm afternoon sunlight."),
# 152 Watch a cat wake up from a nap.
(0, 1, "The silver tabby cat lifts its head sleepily from a sunny cushion, one eye opening, ears turning, just waking up. Warm afternoon light."),
# 153 Out go the front legs, long and stiff.
(0, 1, "The silver tabby cat in a big long stretch on a rug, front legs pushed far out in front, back end raised, eyes squeezed shut. Sunny room."),
# 154 The toes spread. The claws flex.
(0, 1, "Close-up of the silver tabby cat's white front paws stretched out, toes spread wide apart and claws flexing out. Warm light."),
# 155 Kneading works those same muscles. Push, release.
(0, 1, "The silver tabby cat kneads a cushion, its shoulders and front legs working, one white paw pressing down and the other lifting. Warm light."),
# 156 Push, release. A slow,
(0, 1, "Close-up of the silver tabby cat's white paws on a fleece blanket, one pressing down slowly while the other relaxes and lifts. Soft cozy light."),
# 157 rhythmic stretch for the shoulders, the legs, the paws.
(0, 1, "Side view of the silver tabby cat kneading a blanket, front legs extended, shoulder blades rolling, toes spreading with each slow push. Warm evening light."),
# 158 If you've ever had a really good stretch
(1, 0, "A bright bedroom in the morning: the Geek sits up in bed doing a huge stretch, arms high above his head, eyes squeezed shut, glasses on the nightstand beside him."),
# 159 in bed first thing in the morning,
(1, 0, "Early morning sunlight streams through bedroom curtains onto the Geek lying in bed, stretching his legs and arms out under the duvet with a sleepy, contented look."),
# 160 you already know the feeling.
(1, 1, "A sunny bedroom: the Geek and the silver tabby cat both stretch at the very same moment on the bed, the Geek's arms raised and the cat's front legs pushed out long."),
# 161 And then there's the calming side. Rhythm is soothing.
(0, 1, "The silver tabby cat kneads a soft blanket slowly and steadily, eyes calm and half closed, in a quiet dim room lit by a warm lamp."),
# 162 It is for us, anyway.
(1, 0, "The Geek sits on a sofa with eyes closed, calmly tapping his fingers on his knee in a steady rhythm, headphones around his neck. Warm lamp light."),
# 163 Think of rocking in a chair,
(0, 0, "An elderly man with a white beard and a brown cardigan rocks gently in a wooden rocking chair on a porch at sunset, eyes closed peacefully."),
# 164 or jiggling your foot under the desk
(1, 0, "A view under a wooden desk: the Geek's leg in charcoal-grey jeans bounces nervously, his canvas sneaker tapping the floor, while above the desk his hands rest on a laptop."),
# 165 when you're waiting on something.
(1, 0, "The Geek sits at his desk staring at a laptop showing a plain loading circle, chin on hand, foot tapping, with a bored deadpan look. No text on the screen."),
# 166 It seems to work for cats too.
(0, 1, "The silver tabby cat kneads a cushion in a slow steady rhythm, its body visibly relaxing, ears soft. Gentle warm light."),
# 167 Plenty of cats knead when they're happy.
(0, 1, "The silver tabby cat kneads a fluffy blanket in a sunny window spot, eyes closed contentedly, tail curled. Warm, happy atmosphere."),
# 168 But some knead when they're a little rattled.
(0, 1, "The silver tabby cat crouches on a blanket in a corner, ears slightly back, eyes wide, kneading nervously with its white front paws. Dim, slightly uneasy light."),
# 169 After a move. After a trip to the vet.
(0, 1, "The silver tabby cat sits in an empty room full of stacked cardboard moving boxes, beside an open cat carrier, looking around uneasily."),
# 170 When the house is loud and full of strangers.
(0, 1, "A busy noisy house party in a living room full of chatting people, while the silver tabby cat hides under a side table, ears flattened, eyes wide."),
# 171 It's a way to settle.
(0, 1, "The silver tabby cat sits on a soft blanket in a quiet back bedroom, kneading slowly, its ears coming back up, beginning to relax. Calm dim light."),
# 172 The cat is, in its own way, comforting itself.
(0, 1, "The silver tabby cat curled up on a soft blanket, eyes closing, one white paw still resting on the fabric after kneading, peaceful and calm. Warm soft light."),
# 173 Female cats sometimes knead more at certain times, too.
(0, 0, "A tortoiseshell female cat kneads a cushion on a sofa with half-closed eyes, in a calm sunny living room."),
# 174 A cat in heat often gets extra cuddly,
(0, 0, "A tortoiseshell female cat rubs affectionately against a person's legs in a kitchen, tail high, body curving around their ankles."),
# 175 rolling around on the floor, rubbing on everything in sight,
(0, 0, "A tortoiseshell female cat rolls on its back on a wooden floor, twisting playfully, beside a chair leg it has just rubbed against. Sunny room."),
# 176 and yes, kneading. And a mother cat getting close
(0, 0, "A tortoiseshell cat kneads a rug with eyes half closed. Beside it, a heavily pregnant calico cat with a round belly walks slowly across the room."),
# 177 to giving birth will often knead and paw at blankets,
(0, 0, "A heavily pregnant calico cat with a round belly paws and kneads at a pile of soft blankets inside a closet. Warm dim light."),
# 178 fussing over them,
(0, 0, "A heavily pregnant calico cat tugs and rearranges the folds of a blanket with her paws, carefully shaping it. Warm closet light."),
# 179 getting a nest ready for the kittens on the way.
(0, 0, "A heavily pregnant calico cat lies down in a cozy round nest she has made of soft blankets in a quiet closet corner, settled and waiting. Warm dim light."),
# 180 So no, not every cat kneads for the same reason.
(0, 0, "A row of four different cats, a ginger, a black, a calico and a cream, each kneading a different thing: a blanket, a pillow, a lap of jeans and a fleece. Warm light, no text."),
# 181 And the same cat might knead for one reason
(0, 1, "The silver tabby cat kneads a blanket on a sunny morning, eyes bright and happy. A bright cheerful living room."),
# 182 on Tuesday and a totally different one on Friday.
(0, 1, "The silver tabby cat kneads a blanket at night during a thunderstorm, ears slightly back, a flash of lightning in the dark window behind it."),
# 183 Here's something else that surprises people.
(1, 0, "The Geek sits on a sofa raising his eyebrows above his glasses in mild surprise, holding a mug halfway to his mouth. Warm lamp light."),
# 184 Not every cat does it at all.
(0, 0, "A black cat lies on a blanket simply resting, paws still and tucked neatly beneath it, not kneading, looking calm. Warm light."),
# 185 Some cats knead every single evening, like clockwork.
(0, 0, "A cozy living room with a round wall clock without numbers above a sofa, where an orange cat kneads a blanket in warm evening lamp light."),
# 186 Some do it once in a blue moon.
(0, 0, "A night window with a big glowing blue full moon outside, a calico cat on the windowsill kneading a cushion in the moonlight."),
# 187 And some never seem to do it,
(0, 0, "A dignified fluffy black cat sits upright on a cushion like a statue, paws together, perfectly still. Calm warm light."),
# 188 at least not where you can see.
(0, 0, "Under a bed in a dim bedroom, an orange cat secretly kneads a soft sweater on the floor, only partly visible in the shadow."),
# 189 That's completely normal. A cat that doesn't knead isn't unhappy,
(0, 0, "A black cat lying happily in a sunny window, eyes half closed, purring and content, not kneading."),
# 190 and it doesn't love you any less.
(0, 0, "A black cat curled on a woman's lap, her hand resting on its back, both content and calm. A cozy armchair, warm lamp light."),
# 191 It just isn't its thing. And the styles!
(0, 0, "A playful gallery of three cats in a row on a long sofa: a ginger cat, a calico cat and a cream cat, each kneading in its own funny way. Warm light, no text."),
# 192 They're all over the place.
(0, 0, "A busy cozy living room with several cats kneading on different surfaces: one on the sofa, one on a rug, one on a bed in the background. Warm afternoon light."),
# 193 Some cats only use the front paws.
(0, 0, "A cream cat kneads a cushion using only its front paws, its back legs folded neatly beneath it. Warm light."),
# 194 Some throw the back paws in as well
(0, 0, "A ginger cat stands on a fluffy blanket kneading with its front paws while its back paws also tread up and down. Warm light."),
# 195 and sort of march on the spot.
(0, 0, "A ginger cat marches in place on a soft blanket, all four paws stepping up and down in turn, tail up. Warm cozy light."),
# 196 Some knead slow and dreamy,
(0, 0, "A calico cat kneads a blanket very slowly with half-closed sleepy eyes, in soft golden evening light."),
# 197 some like they're running late for something.
(0, 0, "A black cat kneads a cushion at a frantic pace, paws a blur, eyes wide, small motion lines around its paws. Warm light."),
# 198 Some keep their claws tucked away politely.
(0, 0, "Close-up of a cream cat's soft paws kneading a velvet cushion with claws neatly tucked away, gentle and polite."),
# 199 Others go full claws, every single one.
(0, 0, "Close-up of a ginger cat's paws kneading a wool blanket with every sharp claw extended, hooking into the fabric."),
# 200 And then there are the cats that knead nothing at all,
(0, 0, "A ginger cat lies on its back on a sofa, front paws raised in the air above it, kneading empty space. Warm lamp light."),
# 201 just paws pumping away in empty air, eyes half closed,
(0, 0, "Close-up of a ginger cat lying on its back, eyes half closed in bliss, both front paws in the air pressing at nothing in a kneading motion."),
# 202 off somewhere in their own head.
(0, 0, "A ginger cat lies on its back kneading the air with a dreamy far-away look, a soft dreamy cloud above it with drifting fluffy biscuits. No text."),
# 203 People call that making air biscuits,
(0, 0, "A ginger cat on its back kneading the air, with a few small golden round biscuits floating playfully in the air above its paws. Warm cozy light, no text."),
# 204 which might be the best phrase on the entire internet.
(1, 0, "The Geek sits at a desk looking at a laptop with a rare small satisfied smile, nodding approvingly. Warm lamp light, no text on screen."),
# 205 It isn't only a house cat thing, either.
(0, 0, "A large spacious animal sanctuary enclosure with grass, wooden platforms and trees, a big cat bed made of straw in the shade. Bright daylight."),
# 206 Big cats do it too. Lions, tigers
(0, 0, "A male lion with a golden mane and a striped orange tiger lie on grassy ground in a sanctuary, relaxed in the sun."),
# 207 and other big cats have been filmed kneading blankets and bedding,
(0, 0, "A large striped orange tiger lies on a big blanket in a sanctuary, kneading it with its huge front paws, eyes half closed."),
# 208 purring away like a very large,
(0, 0, "A large lion lounges on a pile of straw bedding, eyes closed in contentment, kneading slowly with enormous paws."),
# 209 very heavy version of the one
(0, 0, "A huge tiger lying on a blanket that is visibly squashed flat under its enormous heavy body, paws pressing down. Warm sunlight."),
# 210 on your couch. Okay.
(1, 1, LIVING + " The silver tabby cat kneads the Geek's lap on the sofa while he holds a phone showing a plain photo of a tiger, glancing between the two with a deadpan look."),
# 211 Let's talk about the part that actually hurts.
(1, 1, LIVING + " The Geek winces on the sofa, teeth clenched, as the silver tabby cat kneads his legs with claws out."),
# 212 The claws. When a cat pushes down with its paw,
(0, 1, "Close-up of the silver tabby cat's white front paw pressing down onto a soft blanket, sharp claw tips just starting to show. Warm light."),
# 213 it spreads its toes. And when it spreads its toes,
(0, 1, "Extreme close-up of the silver tabby cat's white paw with toes spreading wide apart against a blanket. Warm light."),
# 214 the claws tend to slide right out with them.
(0, 1, "Extreme close-up of the silver tabby cat's white paw, toes spread wide, curved sharp claws sliding out from between them. Warm light."),
# 215 So a blissed-out cat kneading your lap can turn
(1, 1, LIVING + " The silver tabby cat kneads the Geek's lap with eyes closed in pure bliss, while the Geek sits stiffly on the sofa with a worried look."),
# 216 into a little set of needles going
(0, 0, "Close-up of a row of tiny sewing needles poking up through a pincushion made of charcoal-grey denim. Warm lamp light."),
# 217 in and out of your legs,
(1, 1, "Close-up on the Geek's thighs in charcoal-grey jeans as the silver tabby cat's claws hook in and out of the denim with each kneading push. Warm lamp light."),
# 218 one paw at a time.
(1, 1, "Close-up of the silver tabby cat's white paws on the Geek's jeans, one lifted with claws out, the other pressing in. Warm lamp light."),
# 219 It's not doing it on purpose.
(1, 1, LIVING + " The silver tabby cat kneads the Geek's lap with a totally innocent, peaceful face, eyes closed, while he grimaces."),
# 220 It's not attacking you.
(0, 1, "The silver tabby cat lies peacefully on a blanket with soft relaxed ears and closed eyes, nothing aggressive about it at all. Warm light."),
# 221 In that moment it's so relaxed it isn't really keeping
(0, 1, "The silver tabby cat completely limp and blissful on a lap, eyes shut, whiskers soft, body melted into the blanket. Warm lamp light."),
# 222 track of what its claws are up to.
(1, 1, "Close-up of the silver tabby cat's blissful sleepy face at the top of the frame while its white paws knead the Geek's jeans with claws out below. Warm light."),
# 223 So what do you do about it?
(1, 1, LIVING + " The Geek sits on the sofa with the silver tabby cat on his lap, arms out, looking at the viewer with a helpless deadpan shrug."),
# 224 Well, first, don't punish it.
(1, 1, LIVING + " The Geek sits on the sofa with the silver tabby cat on his lap, holding up one calm open hand, keeping his cool."),
# 225 Don't yell, and don't shove the cat off.
(1, 1, LIVING + " The Geek sits still on the sofa, lips pressed together, resisting the urge to move, while the silver tabby cat stays on his lap."),
# 226 From the cat's side,
(0, 1, "A low view at cat eye level: the silver tabby cat in the foreground looking up at a person's face on a sofa with soft trusting eyes. Warm light."),
# 227 it was showing you about as much trust
(1, 1, "The silver tabby cat lies on its back in the Geek's lap, white belly fully exposed, paws relaxed, as he sits on a sofa. Warm lamp light."),
# 228 and affection as a cat knows how to show.
(1, 1, "The silver tabby cat gently headbutts the Geek's chin as he sits on a sofa, eyes closed, while he looks touched. Warm lamp light."),
# 229 Tell it off for that,
(0, 0, "A woman with short brown hair in a red sweater points sternly at a ginger cat that sits on a sofa, its ears flattening. Living room light."),
# 230 and it may decide your lap isn't such a safe place
(0, 0, "A ginger cat sits on the floor a few steps away from a woman on a sofa, staring warily at her empty lap, ears slightly back."),
# 231 after all.
(0, 0, "A ginger cat walks away down a hallway with its tail held low, leaving an empty sofa behind it. Dim evening light."),
# 232 Which is the last thing you want, really.
(1, 0, "The Geek sits alone on an empty sofa holding a blanket with a sad, deadpan expression, an empty spot on his lap. Dim lamp light."),
# 233 There are much easier fixes.
(1, 1, LIVING + " The Geek sits upright on the sofa with a bright idea look, one finger raised, the silver tabby cat beside him."),
# 234 Keep the claws trimmed. Just the sharp tips,
(1, 1, "The Geek gently holds the silver tabby cat on his lap and carefully trims the very tip of one claw with small cat nail clippers. Bright living room light."),
# 235 carefully, and if you're not sure how,
(1, 1, "Close-up of the Geek's hands holding the silver tabby cat's white paw, gently pressing the pad so a claw shows, clippers ready but hesitating."),
# 236 ask your vet to show you.
(1, 1, "A bright clean vet clinic room: a friendly female vet with dark curly hair in a blue scrub top shows the Geek how to trim the silver tabby cat's claws on an exam table."),
# 237 Throw a thick blanket or a folded towel over your lap
(1, 0, LIVING + " The Geek drapes a thick folded fleece blanket across his lap on the sofa, smoothing it flat."),
# 238 before the cat climbs on.
(1, 1, LIVING + " The silver tabby cat steps from the sofa arm onto a thick folded blanket on the Geek's lap."),
# 239 Then it can knead to its heart's content
(1, 1, LIVING + " The silver tabby cat happily kneads a thick fleece blanket on the Geek's lap, eyes half closed."),
# 240 and the claws hit fabric instead of you.
(1, 1, "Close-up of the silver tabby cat's claws sinking harmlessly into a thick fleece blanket on the Geek's lap, while the Geek's relaxed hand rests nearby. Warm light."),
# 241 You can also gently move its paws,
(1, 1, "Close-up of the Geek's hand gently lifting the silver tabby cat's white paw off his jeans. Warm lamp light."),
# 242 or shift the cat over a bit,
(1, 1, LIVING + " The Geek gently slides the silver tabby cat a little to one side on the sofa with both hands, moving it onto a cushion."),
# 243 so it's kneading the blanket beside you instead.
(1, 1, LIVING + " The silver tabby cat kneads a fluffy blanket on the sofa cushion right next to the Geek, who sits relaxed beside it."),
# 244 And some people find that stroking the cat's back
(1, 1, LIVING + " The Geek gently strokes the silver tabby cat's back with one hand as it kneads on his lap."),
# 245 while it kneads calms it down enough
(1, 1, LIVING + " The silver tabby cat's kneading slows and its eyes close as the Geek strokes its back softly."),
# 246 that it settles and lies down sooner.
(1, 1, LIVING + " The silver tabby cat lies down curled up on the Geek's lap, settled and asleep, while his hand rests on it."),
# 247 One thing you should never do is have a cat declawed
(0, 1, "The silver tabby cat sits upright with one white front paw raised, claws gently showing, looking calm and natural. Plain soft warm background."),
# 248 to stop it. Declawing isn't some heavy-duty nail trim.
(0, 0, "A simple pair of small cat nail clippers lies on a clean white towel beside a single tiny trimmed claw tip. Bright clean light."),
# 249 It removes the last bone of each toe.
(0, 0, "A clean simple educational diagram of a cat's paw shown side-on, with the small bones of the toes drawn in soft lines and the last bone of one toe highlighted in soft red. Plain light background, no labels or text."),
# 250 It's banned in a lot of countries,
(0, 0, "A soft simple world globe on a plain background with many countries gently shaded in calm green. No text, no labels."),
# 251 and vets and cat welfare groups widely oppose it.
(0, 0, "A group of three vets in scrubs and two animal welfare volunteers stand together in a bright clinic, arms crossed, serious and united."),
# 252 Kneading is normal cat behavior.
(0, 1, "The silver tabby cat kneads a cozy blanket peacefully in warm lamp light, a picture of normal, happy cat life."),
# 253 The answer is a blanket. Not surgery.
(1, 1, LIVING + " The Geek holds up a thick fluffy blanket proudly, while the silver tabby cat sits beside him looking at it with approval."),
# 254 Is kneading ever something to worry about?
(1, 1, LIVING + " The Geek sits on the sofa with a slightly worried frown, watching the silver tabby cat knead a cushion."),
# 255 Mostly, no.
(1, 1, LIVING + " The Geek relaxes back into the sofa with a calm deadpan face while the silver tabby cat kneads happily nearby."),
# 256 It's about as normal as cat behavior gets.
(0, 1, "The silver tabby cat kneads a blanket on a sunny windowsill, completely ordinary and calm. Warm daylight."),
# 257 But there are a couple of things
(1, 0, "The Geek holds up two fingers, looking thoughtful, standing in a cozy living room. Warm light."),
# 258 worth keeping an eye on. Sucking is one.
(0, 0, "A black-and-white tuxedo cat on a bed with the corner of a blanket in its mouth, sucking it gently, kneading with its front paws."),
# 259 A cat that sucks on a blanket now and then
(0, 0, "A black-and-white tuxedo cat curled up on a fleece blanket, briefly sucking its corner, eyes half closed. Calm bedroom light."),
# 260 while it kneads is generally fine.
(0, 0, "A black-and-white tuxedo cat kneads a fleece blanket and then curls up peacefully on it, content and healthy. Warm light."),
# 261 Some cats go further, though.
(0, 0, "A cream-colored Siamese cat with dark brown points on its face, ears, paws and tail stares intently at a wool sweater lying on a bed."),
# 262 They suck and chew on wool, on fabric,
(0, 0, "A cream-colored Siamese cat with dark brown points chews on the sleeve of a woollen sweater, a small hole forming in the knit."),
# 263 even on plastic, and sometimes they swallow bits of it.
(0, 0, "A cream-colored Siamese cat with dark brown points chews on a plastic shopping bag on a kitchen floor, a few torn pieces scattered around."),
# 264 That's sometimes called wool sucking,
(0, 0, "Close-up of a cream-colored Siamese cat with dark brown points sucking on a ball of wool yarn. Warm light."),
# 265 and it shows up more in certain breeds,
(0, 0, "Two elegant cats sit side by side on a cushion: a cream-colored Siamese with dark brown points and blue eyes, and a sleek solid brown Burmese with golden eyes."),
# 266 like Siamese and Burmese.
(0, 0, "Portrait of a sleek solid brown Burmese cat with golden eyes beside a cream-colored Siamese with dark brown points and blue eyes. Plain warm background."),
# 267 In some cats it's also thought to be linked
(0, 0, "A small cream-colored Siamese kitten with dark points sits alone in a box with a blanket. Soft, slightly lonely light."),
# 268 to being taken away from their mother too early.
(0, 0, "A tiny kitten is gently lifted away by a person's hands from its ginger-and-white mother cat, who watches from a towel-lined box. Soft light."),
# 269 If your cat is actually eating fabric,
(0, 0, "A cream-colored Siamese cat with dark brown points swallowing a strip of fabric torn from a blanket, the blanket frayed beside it."),
# 270 have a chat with your vet,
(0, 0, "A friendly vet with dark curly hair in a blue scrub top examines a cream-colored Siamese cat on a clinic table while its owner, a young woman, listens."),
# 271 because swallowed cloth can block the gut.
(0, 0, "A simple clean educational illustration of a cat's side silhouette with a soft view of its stomach and gut, a small knot of cloth shown stuck inside. No labels or text."),
# 272 The other thing is change.
(1, 1, LIVING + " The Geek sits on the sofa looking carefully at the silver tabby cat, attentive and watchful."),
# 273 If a cat that's always kneaded
(0, 1, "The silver tabby cat kneading a blanket calmly in warm evening light, ordinary and relaxed."),
# 274 a little suddenly starts kneading all the time,
(0, 1, "The silver tabby cat kneading a blanket intensely with wide eyes, while a clock without numbers on the wall shows the hands moving and the window shows night. Uneasy dim light."),
# 275 obsessively, or alongside other changes, like hiding,
(0, 1, "The silver tabby cat hides under a bed in a dim bedroom, only its eyes and white paws visible in the shadow."),
# 276 crying, or going off its food,
(0, 1, "The silver tabby cat sits beside a full untouched food bowl in a kitchen, mouth open in a sad meow, ears low."),
# 277 that can mean something's bothering it.
(0, 1, "The silver tabby cat curled tightly in a corner of a dim room, ears slightly flattened, looking unsettled."),
# 278 Stress, maybe. Or something physical.
(0, 1, "The silver tabby cat sits hunched on a blanket, eyes squinted, looking unwell and tense. Soft muted light."),
# 279 Any time a cat's behavior shifts out of nowhere,
(1, 1, LIVING + " The Geek kneels on the floor looking closely and with concern at the silver tabby cat, which is crouched quietly under the coffee table."),
# 280 a vet check is a smart idea.
(1, 1, "A bright vet clinic: a friendly vet with dark curly hair in a blue scrub top listens to the silver tabby cat with a stethoscope on an exam table while the Geek watches."),
# 281 Most of the time, though?
(1, 1, LIVING + " The Geek sits back on the sofa with a relieved, calm look as the silver tabby cat walks along the cushion toward him."),
# 282 A kneading cat is a happy cat.
(0, 1, "The silver tabby cat kneads a soft blanket with eyes closed and a contented look, warm golden lamp light."),
# 283 Or at the very least,
(1, 1, LIVING + " The Geek tilts his head with a wry deadpan look, watching the silver tabby cat kneading on his lap."),
# 284 an extremely comfortable one. So.
(0, 1, "The silver tabby cat completely melted into a fluffy blanket in front of a cozy fireplace, belly up, eyes closed, deeply comfortable."),
# 285 Why do cats knead you?
(1, 1, LIVING + " The Geek sits on the sofa, the silver tabby cat kneading his lap, and he looks out at the viewer with a thoughtful deadpan expression."),
# 286 Because it's the very first thing they ever learned,
(0, 0, "A tiny newborn ginger kitten with sealed eyes kneading and nursing against its ginger-and-white mother in a warm towel-lined box."),
# 287 on their very first day,
(0, 0, "A peaceful warm nest box at dawn: a ginger-and-white mother cat with her litter of newborn kittens all nestled together, soft morning light."),
# 288 pressing into their mother for milk and warmth.
(0, 0, "Close-up of tiny kitten front paws pressing into the soft warm fur of a mother cat's belly while the kitten nurses. Golden light."),
# 289 Because that feeling of being small
(0, 0, "A tiny cream kitten curled up asleep in the curve of its mother's body, looking very small and safe. Warm light."),
# 290 and safe never quite leaves them.
(0, 1, "The silver tabby cat, fully grown, curled up asleep on a soft blanket in the warm glow of a lamp, peaceful and safe."),
# 291 Because their paws carry their scent,
(0, 1, "Close-up of the silver tabby cat's white paw pressing into a blanket with a soft faint glow under the pads. Warm light, no text."),
# 292 and you're something they'd like to mark as theirs.
(1, 1, "The silver tabby cat rubs its cheek along the Geek's arm as he sits on a sofa, marking him as its own. Warm lamp light."),
# 293 Because it might be an old
(0, 0, "A sandy-brown African wildcat with faint stripes stands in tall dry grass under a golden sunset sky."),
# 294 wild habit of making a bed.
(0, 0, "A sandy-brown African wildcat with faint stripes curling up in a flattened round nest of grass at dusk."),
# 295 Because it's a good stretch.
(0, 1, "The silver tabby cat stretching long on a rug, front legs reaching far forward, toes spread, back end raised. Sunny room."),
# 296 And because, quite simply, it calms them down.
(0, 1, "The silver tabby cat kneading slowly on a soft blanket with eyes closing in calm contentment. Quiet, warm, dim light."),
# 297 But mostly, I think, because you feel safe.
(1, 1, LIVING + " The silver tabby cat sleeps curled on the Geek's lap while he sits on the sofa, his hand resting on its back, both peaceful."),
# 298 A cat doesn't make biscuits for just anyone.
(0, 1, "The silver tabby cat sits on a sofa ignoring a stranger in a grey suit who pats his own lap invitingly, the cat looking away."),
# 299 It saves that for the warm, soft places
(0, 1, "The silver tabby cat kneading a thick fluffy blanket beside a warm fireplace in a cozy room, golden glow all around."),
# 300 where it can let its guard all the way down.
(0, 1, "The silver tabby cat lying on its back on a fluffy blanket, white belly up, paws curled, sound asleep, totally unguarded. Warm light."),
# 301 So the next time the cat climbs onto your lap,
(1, 1, LIVING + " The silver tabby cat climbs up onto the Geek's lap as he sits on the sofa, one white paw stepping onto his knee."),
# 302 turns around twice, and starts that slow left paw,
(1, 1, LIVING + " The silver tabby cat turns in a circle on the Geek's lap and begins kneading slowly with its left front paw."),
# 303 right paw, maybe grab a blanket.
(1, 1, LIVING + " The Geek reaches over and pulls a fluffy fleece blanket from the sofa arm as the silver tabby cat kneads his lap."),
# 304 Maybe trim those claws this weekend.
(1, 1, "A sunny weekend morning living room: the Geek sits on the floor with small cat nail clippers in hand and the silver tabby cat on his lap, looking calm."),
# 305 And take it as the compliment it is.
(1, 1, LIVING + " The Geek sits on the sofa with a small, rare content smile, watching the silver tabby cat knead a blanket on his lap."),
# 306 That's a grown predator telling you,
(1, 1, LIVING + " Close view of the silver tabby cat on the Geek's lap, looking up at his face with soft trusting half-closed eyes."),
# 307 in the oldest language it knows,
(1, 1, LIVING + " The silver tabby cat slow-blinks up at the Geek while kneading his lap, and he slow-blinks back."),
# 308 that you feel like home.
(1, 1, "A wide cozy view of a small apartment living room at night, the window showing city lights, the Geek asleep on the sofa with the silver tabby cat curled on his chest, a warm lamp glowing."),
]
