"""One image per segment in segments.json, in order: (geek in shot, silver tabby cat in shot, scene).

Each scene is standalone. Never refer to another image ("same room", "again", "earlier").
Other cats are never silver or grey tabbies, so they can't be mistaken for the Geek's cat.
"""
SCENES = [
# 1 You get up for a glass of water. That's it, nothing dramatic.
(1, 0, "A cozy small apartment living room at night lit by one warm floor lamp. The Geek has just stood up from a worn brown sofa and holds an empty tall drinking glass, looking toward an open kitchen doorway with a calm, sleepy deadpan expression. A knitted throw on the sofa, a low coffee table with a book, a houseplant, a bookshelf and a rug."),
# 2 But before you've made it halfway to the kitchen there's a soft thump somewhere behind you,
(1, 1, "A low, floor-level shot in a warm, dim apartment hallway at night: in the foreground The Geek's legs in charcoal-grey jeans and black-and-white canvas sneakers mid-stride, walking away toward a lit kitchen doorway, an empty tall glass in his hand. Just behind him the silver tabby cat lands softly on the wooden floor after jumping down from a sofa arm, all four white paws touching down. Runner rug, skirting boards."),
# 3 and you already know what it is. The cat's up too.
(1, 1, "An apartment hallway in warm night lamp light. The Geek has stopped and glances back over his shoulder with a flat, knowing deadpan look, holding an empty glass. A few steps behind him the silver tabby cat sits upright on the floor, looking straight back at him, tail curled around its white paws. Doors, a coat rack and a lamp along the hall."),
# 4 You head to the bathroom and a paw slides under the door,
(0, 1, "A low, floor-level view in a narrow hallway at night: a closed white bathroom door with a thin strip of warm light glowing through the gap underneath. The silver tabby cat lies flat on the wooden hallway floor in front of the closed door, one white front paw stretched all the way under the gap, ears forward, concentrating. A runner rug, a skirting board and a dim night light further down the hall."),
# 5 feeling around like it's lost something. You move from the couch to the desk,
(0, 1, "Inside a small bathroom, a low view across white floor tiles toward the closed bathroom door: a single white cat paw pokes in through the narrow gap under the door from the dark hallway outside, patting around on the tiles as if feeling for something. Only the white paw is visible. A bath mat, the edge of a bathtub and soft bathroom light."),
# 6 and ten seconds later, guess who's moved from the couch to the desk. It isn't hungry.
(1, 1, "A home office corner beside a window in afternoon light. The Geek sits at a wooden desk in front of an open laptop, looking sideways with a deadpan expression at the silver tabby cat, which sits upright on the desk right next to the laptop, staring at him from very close. Behind them, a sofa shows a round cat-shaped dent in one cushion. Pens in a cup, a desk lamp, a stack of notebooks."),
# 7 It doesn't want to play. It just wants to be wherever you happen to be.
(1, 1, "A small kitchen in daylight. The Geek stands at the counter making a sandwich. On the floor a full food bowl sits untouched and a small toy mouse lies ignored. The silver tabby cat sits pressed against his ankle, looking calmly up at him. Tiled backsplash, a kettle, a fruit bowl, a window over the sink."),
# 8 Which is a bit odd, honestly. Cats are meant to be the independent ones.
(1, 1, "The middle of a living room in daylight. The Geek stands still, looking down with a puzzled deadpan expression at the silver tabby cat, which is sitting directly on top of one of his sneakers, gazing up at him. Sofa, rug, bookshelf and a window behind them."),
# 9 Dogs follow you around, that's their whole deal.
(0, 0, "A sunlit suburban living room: a happy golden retriever trots eagerly right behind a woman with short brown hair in a yellow sweater as she walks across the room carrying a mug, the dog's tongue out and tail wagging, eyes fixed on her. Sofa, rug, potted plants, framed pictures without writing."),
# 10 Cats, or so the story goes, barely register that you exist until the bowl runs empty.
(0, 0, "A sunlit living room: a sleek solid black cat lounges on a high windowsill with its back turned to the room, tail hanging down, gazing out the window and completely ignoring a woman with short brown hair in a yellow sweater who waves at it from the sofa. On the floor below the windowsill sits an empty food bowl. Plants, a rug, soft daylight."),
# 11 So why does an animal famous for not caring trail after you like a small,
(1, 1, "A long apartment hallway lit by one low warm lamp. The Geek walks along carrying a plastic laundry basket full of towels, and the silver tabby cat trots right at his heels, tail up, matching his pace. Doors along the hallway, a coat rack, a runner rug."),
# 12 furry shadow with opinions? The answer, as far as anyone can tell, is a mix of things.
(1, 1, "A hallway wall lit from the side by a low lamp: two shadows stretch across the wall, the tall shadow of The Geek carrying a basket and a small cat shadow following right behind him. In the lower corner of the frame, The Geek's sneakers and the silver tabby cat walking along the floor. Warm, slightly playful mood."),
# 13 Some ancient history. Some baby behavior that never quite switched off. A surprising amount of brainpower.
(1, 1, "The Geek sits cross-legged on a living room rug surrounded by open old hardback books, the open pages showing pictures of ancient clay pots, kittens and a drawing of a brain, with no readable writing. The silver tabby cat lies stretched across the biggest open book right in the middle of the page, looking at him. Warm afternoon window light, a mug of tea on the floor."),
# 14 And a handful of very practical, very cat reasons. Let's get into it.
(0, 1, "The silver tabby cat sits upright on top of a tall wooden bookshelf, looking down at a living room with sharp, intelligent greenish-yellow eyes, ears pricked forward, tail curled over its white front paws. Below: a sofa, a sunny patch on the floor, a radiator and a kitchen doorway with a food bowl visible. Slightly low camera angle looking up."),
# 15 Start with the reputation, because that's where the confusion comes from.
(0, 0, "A cozy armchair beside a fireplace in a quiet old-fashioned living room. A tuxedo cat, black with a white chest and white paws, sits on the armchair with its back half-turned, chin raised, eyes half-closed, looking aloof and dignified, ignoring a ball of yarn on the floor. Warm firelight."),
# 16 The idea of the aloof, solitary cat really comes from the way cats hunt.
(0, 0, "A lone brown mackerel-tabby farm cat walks alone along the top of an old wooden fence at dusk, silhouetted against a dusky orange-pink sky, a wide empty field below. Natural cat anatomy, calm and solitary mood."),
# 17 A cat hunts alone. It stalks, it waits, it pounces, and it does not share.
(0, 0, "A lone brown mackerel-tabby farm cat crouches low in tall golden meadow grass at dusk, body flattened, eyes locked forward, tail straight behind it, stalking a small field mouse half-hidden in the grass ahead. A fence line, a distant farmhouse and a dusky orange-pink sky behind. Natural cat anatomy."),
# 18 Lions are the exception, but nearly every other wild cat species lives and hunts on its own.
(0, 0, "An African savanna at golden hour: in the background a pride of lions rests together under a flat-topped acacia tree; in the foreground a lone leopard lies along the thick branch of a different tree, alone, watching the plain. Dry golden grass, distant hills, a warm hazy sky. Natural animal anatomy."),
# 19 So people looked at the little one on the sofa and assumed, fair enough,
(1, 1, "A living room in the evening. The Geek sits at one end of a long sofa looking at the silver tabby cat, which is curled into a tight ball at the far other end, eyes half shut, back turned toward him, looking completely aloof. A wide empty gap of cushion between them. Lamp light, a rug, a window with a dark blue sky."),
# 20 it must be a loner too. Here's the thing though.
(0, 1, "Close shot of the silver tabby cat sitting alone on a windowsill at dusk, its silhouette against a soft purple sky, looking out at the street lights, tail hanging down. A quiet, slightly lonely mood. A potted plant beside it."),
# 21 Hunting alone and living alone aren't the same.
(0, 0, "The wooden porch of an old farmhouse at golden hour. Three cats doze together on a weathered bench, pressed side by side: a black-and-white cat, a calico cat and a ginger cat, one resting its chin on another's back. Flower pots, a screen door and fields beyond the porch rail."),
# 22 And the story of how cats ended up in our houses suggests
(0, 0, "A warm illustrated scene of a small stone cottage at sunset with lit windows; on the doorstep a ginger cat sits looking at the open front door, where warm light spills out. A garden path, a low stone wall and rolling fields behind."),
# 23 they were never quite as solitary as we gave them credit for.
(0, 0, "A back alley behind a row of brick houses in the morning: five cats of different coats, ginger, calico, black, tuxedo and tortoiseshell, sit and lie together around a shared food dish beside some crates, calm and relaxed with each other. Washing lines overhead, potted plants by the back doors."),
# 24 Roughly ten thousand years ago, people in the Near East started farming. Farming meant storing grain.
(0, 0, "A wide view of a Neolithic farming village in a fertile Near Eastern river valley about ten thousand years ago: flat-roofed mudbrick houses, people in simple woven tunics harvesting wheat with flint sickles, and large clay grain storage jars and a mudbrick granary in the foreground. Dry hills and a pale blue sky."),
# 25 Stored grain meant mice, and I mean a lot of mice.
(0, 0, "Close view inside an ancient mudbrick granary about ten thousand years ago: large clay storage jars overflowing with wheat grain, spilled grain on the dirt floor, and dozens of small brown mice scurrying over the jars, nibbling the grain and running along the walls. Shafts of dusty light through a small window."),
# 26 And the mice, naturally, brought in the local wildcats,
(0, 0, "Dusk at the edge of an ancient Near Eastern mudbrick village: an African wildcat, sandy-grey-brown with faint dark stripes, long legs, tufted ears and a black-ringed tail, creeps out of the dry scrub toward the village walls, eyes fixed ahead. Warm last light on the walls, smoke rising from a cooking fire."),
# 27 who figured out pretty quickly that human villages were the best hunting grounds for miles.
(0, 0, "An ancient mudbrick village about ten thousand years ago: a sandy-brown African wildcat with faint stripes and a ringed tail crouches on top of a low mudbrick wall, eyes fixed on brown mice running between clay grain jars below. Flat-roofed houses and a dry valley behind, warm evening light."),
# 28 Nobody actually tamed those cats. They more or less tamed themselves.
(0, 0, "Daytime in an ancient mudbrick village: a woman in a woven tunic kneels grinding grain on a stone quern, and a sandy-brown African wildcat with faint stripes sits calmly just a few meters away in the shade of a wall, watching but relaxed. Neither pays much attention to the other. Clay pots, baskets and drying herbs around them."),
# 29 The bolder, calmer ones, the ones that could put up with people, got the most food,
(0, 0, "An ancient mudbrick village lane: a calm sandy-brown striped wildcat eats a fish scrap tossed by an old man in a woven tunic sitting on a doorstep, while a second, more nervous wildcat watches warily from far away behind a clay jar. Warm sunlight, goats and grain jars in the background."),
# 30 raised the most kittens, and over a long, long time turned into a new kind of animal.
(0, 0, "In the shade of an ancient mudbrick wall, a sandy-brown striped wildcat mother lies resting with four small striped kittens tumbling around her, while village children in woven tunics play with a wooden toy in the sunlit lane nearby. Goats, grain jars and flat-roofed houses behind."),
# 31 By about nine and a half thousand years ago, things were already pretty close.
(0, 0, "Inside a simple ancient stone house about nine and a half thousand years ago, lit by a small hearth fire: a family in woven tunics sits around the fire sharing food, and a sandy-brown striped cat sleeps curled up on a woven reed mat right beside a child. Clay pots, hanging herbs and stone walls."),
# 32 On the island of Cyprus, archaeologists dug up a cat buried right beside a human.
(0, 0, "A modern archaeological excavation on a sunny Mediterranean hillside on the island of Cyprus: a square trench marked with string grid lines, two archaeologists in sun hats kneeling with brushes and trowels, carefully uncovering an ancient human skeleton lying on its side and, right beside it, the small complete skeleton of a cat. Sieves, buckets, a wheelbarrow and the blue sea on the horizon."),
# 33 Now, cats aren't native to Cyprus. Somebody brought that cat over by boat.
(0, 0, "An ancient small wooden dugout boat crossing a calm turquoise sea toward a rocky island coastline about nine and a half thousand years ago. A man in a simple tunic paddles at the back; at the front a sandy-brown striped cat sits upright in a woven reed basket, looking toward the island. Clear sky, gentle waves, seabirds."),
# 34 And somebody cared enough to bury it with a person.
(0, 0, "A close, respectful view into an ancient grave pit in pale earth: a human skeleton lying on its side with a small cat skeleton laid carefully right beside it, a few seashells and a polished stone axe placed with them. Soft warm light, archaeologist's brush and trowel resting at the edge of the pit."),
# 35 So we go back a long way, us and cats.
(1, 1, "The Geek sits on the back steps of a small house at sunset, elbows on knees, with the silver tabby cat sitting beside him on the step, both looking out at the garden and the orange sky. A fence, a washing line and a quiet, warm mood."),
# 36 And when cats have enough to eat, it turns out they don't stay solitary at all.
(0, 0, "A farmyard in the morning: a farmer's wife in an apron pours milk into a wide shallow dish, and six farm cats of different coats, ginger, calico, black, tuxedo, tortoiseshell and brown tabby, gather around it together peacefully. A red barn, chickens and hay bales behind."),
# 37 Look at a feral colony, the groups you see hanging around farms and docks and back alleys.
(0, 0, "A small fishing harbor dock in the morning: wooden fishing boats moored, stacked crates and coiled nets, and a colony of about eight cats with varied coats, ginger, calico, black, tuxedo and tortoiseshell, lounging on the crates, washing themselves and sitting together. Seagulls, a stone harbor wall and a hazy sea."),
# 38 At the heart of most of them there's a cluster of related females. Mothers, daughters, sisters, aunts.
(0, 0, "Inside an old barn: four calico and tortoiseshell female cats with similar patches sit close together on a low hay bale, clearly a family of different ages, an older mother cat in the middle and younger ones around her. Dusty light through gaps in the wooden walls."),
# 39 They groom each other. They sleep piled together in one warm heap.
(0, 0, "Close shot inside an old barn: on a pile of loose hay, four female cats, calicos and tortoiseshells, are tangled together. Two of them groom each other's heads, the other two sleep piled on top of one another in one warm heap. Shafts of dusty light from a gap in the wooden wall."),
# 40 They rub against each other when they meet, and they'll even help raise each other's kittens.
(0, 0, "A straw nest in a barn corner: a calico mother cat and a tortoiseshell mother cat lie side by side, both nursing one mixed litter of seven small kittens of different colors, while a third adult ginger cat rubs its head against one of the mothers in greeting. Soft warm light, wooden beams, a feed sack."),
# 41 The lone hunter, once it clocks off, is actually a fairly social creature.
(0, 0, "A sunny farmyard wall in the late afternoon: a brown mackerel-tabby cat that has just finished hunting lies relaxed and belly-up in the sun, pressed against two calico cats who doze beside it on the warm stone. A barn and fields behind, a calm lazy mood."),
# 42 Which brings us to the biggest reason your cat follows you around.
(1, 1, "The Geek walks from the kitchen into the living room carrying a mug, and the silver tabby cat follows right behind him, tail up, eyes fixed on him. Seen from a slightly high angle, warm afternoon light across the wooden floor."),
# 43 From where it's standing, you're not really an owner. You're something much closer to a parent.
(1, 1, "The Geek sits on a living room rug leaning back against the sofa, and the silver tabby cat is curled up asleep in his lap like a kitten, white paws tucked in. He rests one hand gently on its back, looking down at it with a calm, soft expression. Warm late-afternoon window light, a blanket, a plant."),
# 44 Kittens have this short window, somewhere between two and seven weeks old,
(0, 0, "A cardboard box lined with a soft fleece blanket holding five tiny kittens of different colors, ginger, black, calico, tuxedo and cream, eyes just open, one wobbling toward the edge on unsteady legs and peering out curiously. Shot from just above the rim of the box, warm indoor light."),
# 45 when they work out who's safe and who counts as family.
(0, 0, "A tiny ginger kitten stands at the edge of a fleece blanket, looking up curiously at a large gentle human hand held out flat on the floor in front of it, sniffing the fingertips. Soft warm indoor light, a cozy home floor."),
# 46 A kitten that gets handled by people during
(0, 0, "A bright animal shelter room: a young woman volunteer with curly black hair in a blue apron sits on a low stool and gently holds a small cream-and-white kitten against her chest, the kitten relaxed and nuzzling her collar. Cat beds, a scratching post and shelves of supplies in the background."),
# 47 that stretch grows up treating humans as part of its social world.
(0, 0, "A sunny family living room: a grown cream-and-white cat lies relaxed on the sofa between a mother and a young boy reading a picture book, the cat's head resting on the boy's leg, completely at ease with the people. Cushions, a lamp, a window."),
# 48 And an awful lot of what your adult cat does every day is kitten behavior
(0, 1, "The silver tabby cat, fully grown, lies on its back on a living room rug batting at a dangling ribbon with all four white paws like a playful kitten, belly showing, eyes wide. A sofa edge and sunlit floorboards around it."),
# 49 that simply never got turned off. Take kneading. That rhythmic pushing with the front paws?
(0, 1, "Close-up of the silver tabby cat's white front paws kneading a soft fleece blanket, one paw pressed down and the other lifted, claws slightly out, the cat's half-closed eyes visible at the top of the frame. Warm cozy light."),
# 50 That's what kittens do against their mother's belly to get the milk flowing.
(0, 0, "Close shot of a calico mother cat lying on her side on a blanket while three small kittens nurse, their tiny front paws pressing rhythmically against her soft belly. The mother's eyes are half closed, peaceful. Warm soft light."),
# 51 Your cat does it on your lap. Or take meowing.
(1, 1, "The Geek sits on the sofa with a fleece blanket over his lap. The silver tabby cat stands on the blanket kneading it with its white front paws, eyes half closed in bliss. The Geek looks down with a deadpan, slightly pained expression. Lamp light, cushions."),
# 52 Adult cats hardly ever meow at each other. They talk with scent, with body language, with touch.
(0, 0, "Two adult cats, a black cat and a ginger cat, meet on a garden path and gently touch noses, both with tails raised, silent and calm. Flower beds, a wooden fence and soft morning light."),
# 53 Kittens meow at their mother when they're cold or hungry.
(0, 0, "A small black kitten sits on a blanket with its mouth open in a tiny meow, looking up at its large black-and-white tuxedo mother cat, who leans down toward it attentively. A cozy basket and warm light."),
# 54 Grown cats keep meowing at exactly one species, and it's us. Then there's the tail.
(1, 1, "A kitchen in the morning. The Geek stands holding a coffee mug, looking down. The silver tabby cat sits on the floor in front of him with its mouth open mid-meow, looking straight up at him. Morning light through the window, cupboards, an empty food bowl near the wall."),
# 55 When your cat trots toward you with its tail straight up,
(1, 1, "An apartment entrance hall. The Geek steps in through the front door carrying a paper grocery bag. The silver tabby cat trots happily toward him across the floor with its ringed tail held straight up. Shoe rack, coat hooks, a doormat, daylight from the open door."),
# 56 maybe with a little hook at the very tip, that's a greeting.
(0, 1, "A close side view of the silver tabby cat walking, its black-and-silver ringed tail held straight up with the black tip curled over into a small hook, like a question mark. Soft daylight, a plain wooden floor and wall behind."),
# 57 Kittens hold their tails like that when they walk up to their mother.
(0, 0, "A sunny farmyard: two small ginger kittens trot eagerly toward their ginger mother cat with their little tails held straight up like flags. Chickens, a barn wall and a hay bale behind."),
# 58 In cat colonies, researchers found that the tail-up signal usually goes from lower-ranking cats to higher-ranking ones.
(0, 0, "A colony of cats on a sunny stone wall by a farm: a young slim calico cat approaches a large, sturdy older black cat with its tail held straight up, while two researchers with binoculars and a notebook watch quietly from a distance behind a fence. Fields and a barn behind."),
# 59 So it's a friendly hello, but with a little bit of respect baked in.
(0, 0, "Close shot of a young calico cat with its tail up gently bumping heads with a large older black cat on a sunny stone wall, the older cat sitting tall and calm, accepting the greeting. Soft warm light."),
# 60 When your cat follows you down the hallway, tail high like a flag,
(1, 1, "The Geek walks down a wooden staircase in his home, and the silver tabby cat follows one step behind him with its ringed tail held high like a flag. Framed pictures without writing on the wall, a banister and soft daylight from a window at the bottom of the stairs."),
# 61 it's treating you like the senior member of the family.
(1, 1, "The Geek sits in a big armchair like a king on a throne, with a deadpan expression, and the silver tabby cat sits upright on the rug in front of him looking up at him respectfully. Warm lamp light, a bookshelf behind."),
# 62 For a long time, though, nobody took any of this very seriously.
(0, 0, "A cluttered old university office with stacks of papers and books: a bored-looking male scientist in a tweed jacket leans back in his chair, ignoring a ginger cat sitting politely on his desk. A window with rain outside, a desk lamp, no readable writing anywhere."),
# 63 Dogs got all the attachment studies. Cats were filed under "in it for the food."
(0, 0, "A university animal behavior lab: a researcher in a white lab coat crouches with a clipboard, smiling at a happy beagle who sits on a mat. In the background, a black cat peers out of an open travel carrier next to a food bowl, ignored by everyone. Cameras on tripods, plain walls, a window."),
# 64 Then, in twenty nineteen, a team of researchers in the United States decided
(0, 0, "A modern university campus in the United States on a sunny autumn day: red-brick buildings, trees with orange leaves, and three young researchers walking along a path carrying a cat carrier, a laptop bag and a camera tripod."),
# 65 to test cats the same way scientists test human babies, and dogs.
(0, 0, "A bright test room divided into three side-by-side sections: on the left a mother with a baby on a play mat, in the middle a young man with a beagle, on the right a young woman with a black-and-white tuxedo cat, each pair sitting on the floor in a plain room with a camera on a tripod watching them."),
# 66 The test is called the secure base test, and it's simple.
(0, 0, "A bare, unfamiliar test room with a single wooden chair in the middle, a few scattered cat toys on the floor and a video camera on a tripod in the corner. An empty, calm room, soft even light, a closed door on one side."),
# 67 A cat and its owner go into an unfamiliar room together for two minutes.
(0, 0, "A bare test room with a single chair, a few toys on the floor and a camera in the corner. A young woman with a ponytail in a red sweater sits on the chair, and her young black-and-white tuxedo cat cautiously sniffs around the floor near her feet."),
# 68 Then the owner leaves, and the cat sits alone for two minutes. Then the owner comes back.
(0, 0, "A bare test room with an empty chair: a young black-and-white tuxedo cat sits alone in the middle of the floor, staring at the closed door, ears turned toward it, looking uncertain. A few toys on the floor, a camera in the corner."),
# 69 The bit that matters is the reunion. A securely attached cat greets its person, calms down,
(0, 0, "A bare test room: a young woman with a ponytail in a red sweater has just come back through the door and sits on the chair, and her black-and-white tuxedo cat rubs against her legs with its tail up, relaxed and happy. A camera in the corner."),
# 70 and then wanders off to explore the room again,
(0, 0, "A bare test room: a young black-and-white tuxedo cat walks away from a young woman in a red sweater seated on a chair, confidently sniffing a toy ball on the floor, while she watches it calmly. A camera in the corner, soft light."),
# 71 using that person as a sort of safe home base. An insecurely attached cat does something else.
(0, 0, "A bare test room seen from above: a young woman in a red sweater sits on a chair in the middle, and a young black-and-white tuxedo cat plays with a toy a short distance away, glancing back at her, like a little explorer checking in with base camp. A camera in the corner."),
# 72 It clings and can't settle, or it ignores the owner completely, or it bolts and hides.
(0, 0, "A bare test room with a different pair: a bearded man in a blue shirt stands awkwardly by the chair, while his ginger cat hides under the chair with wide eyes and flattened ears, refusing to come out. Toys on the floor, a camera in the corner."),
# 73 About sixty-four percent of the kittens in that study were securely attached to their owners.
(0, 0, "A cozy living room rug: a young woman sits cross-legged and a young black-and-white tuxedo cat curls contentedly against her knee, purring, while she strokes it. Soft warm light, toys scattered on the rug."),
# 74 That's almost exactly the same as human babies, where it's around sixty-five percent.
(0, 0, "A cozy living room rug: a mother sits with her baby, who crawls happily back toward her lap after exploring a few toys. Soft warm light, a play mat, a teddy bear and building blocks without letters."),
# 75 And it's very close to what's been found in dogs. So the aloof cat?
(0, 0, "A cozy living room: a young man sits on the floor and a happy beagle leans against his side with its head on his knee. On the sofa behind them, a ginger cat sits looking at the viewer with a calm, unbothered expression. Soft lamp light."),
# 76 Mostly a myth, it seems. A study from twenty seventeen pushed it even further.
(1, 1, "The Geek sits on the living room floor with the silver tabby cat pressed affectionately against his side, head-butting his arm, eyes closed. The Geek looks straight ahead with a deadpan expression. Sofa, rug and lamp behind."),
# 77 Researchers gave cats a choice between four kinds of things.
(0, 0, "A simple test room seen from above at an angle: four stations spaced around the floor, a bowl of food, a feather toy, a small cloth carrying a scent, and a researcher kneeling with an open hand. A calico cat stands in the middle of the room, looking between them, deciding."),
# 78 Food, toys, interesting smells, and a person who'd interact with them.
(0, 0, "Four small close-up panels flowing into one wide image without borders: a bowl of cat food, a colorful feather toy, a small folded cloth with faint scent wisps drawn around it, and a researcher's open, gentle hand, all laid out on a plain floor in a row."),
# 79 Each cat had already gone a few hours without food beforehand.
(0, 0, "A calico cat sits beside an empty food bowl on a tiled floor next to a large analog wall clock, looking hungry, ears slightly back. Plain test room walls, soft light."),
# 80 And still, half the cats picked the human over everything else. Food included. Food came second.
(0, 0, "A simple test room: a calico cat has walked past a full food bowl and is rubbing its cheek against a kneeling researcher's hand, eyes closed with contentment, while the food bowl, a feather toy and a scent cloth sit ignored on the floor."),
# 81 So a big part of the answer really is that simple.
(1, 1, "The Geek sits on the sofa reading, and the silver tabby cat lies stretched along the backrest right behind his head, eyes closed, one white paw resting on his shoulder. Calm evening lamp light."),
# 82 Plenty of cats follow you because they like you, and being near you feels safe.
(1, 1, "The Geek reclines in a worn armchair reading a book, and the silver tabby cat lies asleep on his chest, paws tucked in. A reading lamp glows, rain streaks a window behind them, a mug sits on the side table."),
# 83 But they're also keeping tabs on you. And they're weirdly good at it.
(0, 1, "The silver tabby cat peeks around the edge of a door frame, only its head and one white paw visible, greenish-yellow eyes wide and watchful, ears forward, watching someone in the next room. Hallway shadows, warm light from the room beyond."),
# 84 In twenty nineteen, researchers in Japan showed that cats can recognize their own names.
(0, 0, "A Japanese home with tatami mats and sliding paper screens: a young Japanese woman researcher kneels beside a small speaker and a video camera, and a cream-colored cat sits on a flat floor cushion in front of them. Soft daylight, a low table, a potted bonsai."),
# 85 Even with the name tucked into a list of similar-sounding words, the cats picked it out,
(0, 0, "A cream-colored cat sits on a floor cushion on tatami mats, looking calm and uninterested, while a small speaker beside it plays sound, drawn as faint curved sound-wave lines with no letters. A paper screen softly behind."),
# 86 moving their ears, turning their heads. Then in twenty twenty-one another Japanese team tried something stranger.
(0, 0, "Close-up of a cream-colored cat's head on a floor cushion, ears swiveled sharply toward a small speaker beside it and head just turning in that direction, eyes alert. Tatami mats and a paper screen softly behind."),
# 87 They played a cat its owner's voice from one side of a room, and then,
(0, 0, "A plain room in a Japanese home with two small speakers placed at opposite ends of the floor. A black cat sits in the middle, its head turned toward the left speaker, listening. A camera on a tripod in the corner, sliding doors, soft daylight."),
# 88 a moment later, from a speaker in a totally different spot.
(0, 0, "A plain room in a Japanese home with two small speakers at opposite ends of the floor: the right-hand speaker now gives off faint curved sound-wave lines, while a black cat in the middle of the room is still facing the silent left-hand speaker. Sliding doors, soft daylight."),
# 89 The cats looked surprised. Like, wait, how did you get over there?
(0, 0, "Close shot of a black cat that has snapped its head toward a speaker on the right, eyes wide, ears pricked fully forward, body frozen mid-turn, plainly startled. Tatami mats and a sliding door behind."),
# 90 Which suggests a cat carries around a kind of mental map of
(0, 1, "The silver tabby cat sits on a living room rug with its eyes closed in concentration, and above its head floats a simple dreamy thought-cloud showing a tiny floor plan of a house with rooms and a small dot marking a person. Soft warm light."),
# 91 where you are in the house, even when it can't see you.
(1, 1, "A cutaway cross-section of a small two-storey house, like a dollhouse with the front wall removed. Upstairs in a bedroom, The Geek sits at a desk typing. Downstairs in the living room, the silver tabby cat sits on the sofa staring up at the ceiling at exactly the spot where he is. Stairs, kitchen and rooms visible in each section."),
# 92 Following you is how it keeps that map up to date.
(1, 1, "The Geek walks from the living room into the kitchen, and the silver tabby cat follows a few steps behind, glancing around each room as it passes through the doorway, ears up. Warm evening light, an open-plan apartment."),
# 93 When you vanish into another room, you've dropped off the map.
(1, 1, "The Geek is halfway through a doorway into a dim room, only his back and one sneaker still visible as he disappears. In the bright hallway behind, the silver tabby cat stands alert watching the doorway, one white front paw raised. Doors, a rug and a lamp."),
# 94 And the cat wants to know where you went. And that leads to territory.
(0, 1, "The silver tabby cat trots quickly down an empty hallway toward a half-open door, ears forward, tail up, in a hurry to find someone. Warm light from the open door, a runner rug, framed pictures without writing."),
# 95 Cats are deeply territorial, and your home is their territory. You're part of it.
(0, 1, "The silver tabby cat sits on the top platform of a tall cat tree beside a big window, looking down over the whole living room like a lookout surveying its kingdom. Below: sofa, rug, coffee table, kitchen doorway. Bright daylight from the window."),
# 96 A cat spends a good chunk of its day patrolling,
(0, 1, "The silver tabby cat walks carefully along the edge of a kitchen counter, tail up, between a kettle and a bread bin, looking around alertly. Morning light, cupboards, a window over the sink."),
# 97 checking that everything's where it ought to be.
(0, 1, "Close shot of the silver tabby cat sniffing a potted herb plant on a windowsill, whiskers forward, inspecting it carefully. Soft daylight, a kitchen window with a view of rooftops."),
# 98 So when you get up and walk into a room,
(1, 0, "The Geek stands up from his desk chair and walks toward the door of a small laundry room, carrying an empty basket, the light switch on the wall just beside him. Soft daylight, a calm ordinary moment."),
# 99 the cat comes along to see what's going on in that corner of its little kingdom.
(1, 1, "The Geek walks into a small laundry room carrying a basket, and the silver tabby cat walks in right behind him, already sniffing the washing machine and looking around. Shelves with plain unlabelled bottles, a drying rack."),
# 100 It's also why cats can't stand closed doors.
(0, 1, "The silver tabby cat sits on the hallway floor directly in front of a closed wooden bedroom door, staring up at the door handle with intense focus, tail wrapped around its white paws. Dim hallway light."),
# 101 A closed door means a piece of the territory has suddenly gone out of reach.
(0, 1, "The silver tabby cat stands on its hind legs against a closed wooden bedroom door, one white front paw scratching at the wood just below the handle, ears forward. Hallway rug, warm light."),
# 102 The cat doesn't necessarily want to be in that room. It wants to know it could be.
(0, 1, "A low view from inside a bedroom toward the closed bedroom door: the shadow of the silver tabby cat's ears and paws is visible in the strip of light under the door, waiting on the other side. An unmade bed and a lamp in the foreground."),
# 103 Which is why, the second you open the door, it'll often just peek in, look satisfied,
(1, 1, "The Geek holds a bedroom door open, looking down, and the silver tabby cat stands on the threshold poking only its head into the room, glancing around with a satisfied look. Bedroom with an unmade bed behind him."),
# 104 and stroll off again. Cats mark their territory with scent, too.
(1, 1, "The Geek stands holding the bedroom door wide open with a deadpan expression, while the silver tabby cat strolls away down the hallway in the opposite direction, tail up, not even looking back."),
# 105 They've got glands on their cheeks, their chin, and the base of the tail.
(0, 1, "Close-up of the silver tabby cat rubbing its cheek and chin firmly against the corner of a wooden bookshelf, eyes half closed, whiskers pushed back. Books and a small plant on the shelves, soft light."),
# 106 So when your cat rubs its face along your legs while it follows you,
(1, 1, "A low, floor-level shot in a kitchen: The Geek's legs in charcoal-grey jeans and black-and-white canvas sneakers, with the silver tabby cat rubbing the side of its face along his shin and its ringed tail wrapped around his leg. Tiled floor, cupboard doors."),
# 107 it's leaving its scent on you. Mixing its smell with yours,
(1, 1, "The Geek crouches down in the kitchen, and the silver tabby cat pushes its forehead and cheek firmly into his hand, eyes closed, with faint soft scent wisps drawn in the air around them. Warm light."),
# 108 the same way colony cats rub against each other to build one shared group smell.
(0, 0, "Two colony cats, a calico and a ginger cat, rub their heads and bodies against each other along the top of a sunny stone farm wall, tails entwined. Ivy on the wall, a barn and fields behind."),
# 109 In other words, you're being labeled. Now for the less romantic reasons. Cats are extremely practical animals.
(0, 1, "The silver tabby cat sits upright beside an empty food bowl on a kitchen floor, staring directly at the viewer with a flat, unimpressed, businesslike look. Cupboards, a tiled floor, plain daylight."),
# 110 First, food. You're the one who opens the cans.
(1, 1, "The Geek stands at the kitchen counter opening a small can of cat food with a pull tab. The silver tabby cat stands on its hind legs with both white front paws on the cupboard door below the counter, stretching up toward the can, eyes wide. Evening kitchen light."),
# 111 A cat doesn't need to be a genius to notice
(0, 1, "The silver tabby cat sits on a kitchen chair with a thoughtful expression, looking at the closed cupboard where the cat food is kept, ears forward, as if working out a plan. Evening kitchen light."),
# 112 that good things tend to happen when you walk into the kitchen.
(1, 1, "The Geek walks into the kitchen in the evening and switches on the light, and the silver tabby cat, already sitting next to its bowl, perks up instantly, eyes wide, tail up. Cupboards, a fridge, a tiled floor."),
# 113 So it tags along, just in case. Lots of cats learn exactly which footsteps mean dinner.
(1, 1, "An apartment hallway in the evening: The Geek walks toward the kitchen in socks, and the silver tabby cat sprints ahead of him toward the kitchen doorway and its food bowl, ears back with speed, tail up. Warm light from the kitchen."),
# 114 Second, routine. Cats adore routine. They learn the whole shape of your day.
(1, 1, "Early morning in a bedroom with pale blue dawn light: The Geek lies asleep in bed under a duvet, his glasses on the nightstand beside an analog alarm clock, and the silver tabby cat sits squarely on his chest staring at his sleeping face, waiting."),
# 115 When you wake up, when you eat, when you finally sit down in the evening.
(1, 1, "The Geek sits down on the sofa in the evening with a bowl of noodles, and the silver tabby cat is already sitting on the cushion beside him as if it knew exactly when he would arrive. Warm lamp light, the TV glow."),
# 116 Following you is partly a way of staying in sync.
(1, 1, "A side view of The Geek and the silver tabby cat walking down a hallway together in step, his sneaker and its white front paw lifted at the same moment. Warm afternoon light, a runner rug."),
# 117 Ever noticed how a cat can be dead asleep
(0, 1, "The silver tabby cat lies deeply asleep on its back on a sofa cushion, legs in the air, white paws curled, mouth slightly open. Evening lamp light, a blanket, a peaceful mood."),
# 118 and still turn up the moment you start your bedtime routine?
(1, 1, "A small bathroom at night: The Geek stands at the sink brushing his teeth, and the silver tabby cat already sits on the counter right beside the sink, watching him. A mirror, a towel on a rail, a toothbrush cup."),
# 119 It's been paying attention the whole time. Third, warmth.
(0, 1, "Close-up of the silver tabby cat lying curled up on a sofa with its eyes just slightly open, one greenish-yellow eye watching the room, pretending to be asleep. Soft evening lamp light."),
# 120 A cat is comfortable at somewhere around thirty to thirty-eight degrees Celsius,
(0, 1, "The silver tabby cat lies stretched out long in a bright rectangle of sunlight on a wooden floor beside a warm radiator, eyes closed, belly up, white paws curled. Dust motes in the light, a window frame casting shadows."),
# 121 which is a lot warmer than most of us keep our homes.
(1, 0, "A cool, blue-toned living room in winter: The Geek sits comfortably on the sofa in his hoodie reading, a thermostat on the wall and frost on the window behind him. A calm ordinary evening."),
# 122 And you're a warm body. Your lap is warm. Your laptop is warm.
(1, 1, "The Geek sits at his desk, hands raised and frozen above an open laptop, because the silver tabby cat is lying flat across the warm laptop keyboard with its eyes closed. The Geek's expression is deadpan. Desk lamp, mug, notebook."),
# 123 The spot on the bed you just got out of is warm.
(1, 1, "Morning in a bedroom: The Geek, just out of bed and standing beside it, looks down at the silver tabby cat, which has curled up in the warm hollow he left in the rumpled sheets. Soft morning light through curtains."),
# 124 The cat follows the heat, and very often the heat is you. Fourth, boredom.
(1, 1, "The Geek sits on the sofa under a blanket, and the silver tabby cat is pressed tightly against his side under the edge of the blanket, only its head poking out, eyes closed. Cozy warm lamp light, a cold rainy window behind."),
# 125 Most house cats live indoors these days. That keeps them safe,
(0, 1, "The silver tabby cat sits on an inside windowsill behind a closed window, watching a busy street below with cars and people, safe inside a cozy apartment. Daylight, a plant pot beside it."),
# 126 sure, but it also means the most interesting thing in their entire world is often you.
(0, 1, "The silver tabby cat lies on the floor of a quiet, tidy living room with nothing happening, chin on its white paws, looking bored, eyes half open. A grey rainy day outside the window."),
# 127 You move stuff. You make noises. You open doors.
(1, 1, "The Geek drags a large cardboard box across the living room floor, and the silver tabby cat watches from the top of the sofa with wide, fascinated eyes and ears forward. Daylight, a few moving boxes."),
# 128 For an indoor cat, following you around is basically the evening's entertainment. And then, the bathroom.
(1, 1, "The Geek sits on the living room floor assembling a flat-pack bookshelf, surrounded by wooden panels, screws and a screwdriver. The silver tabby cat sits inside the empty cardboard box, only its head poking out, watching every move with total fascination."),
# 129 Almost every cat owner has had the cat sit there and stare at them,
(0, 1, "Inside a small tiled bathroom, the silver tabby cat sits upright on the bath mat staring straight up at the viewer with an unblinking, intense look. Shower curtain, sink and a towel rail behind it."),
# 130 or yell outside the door like something terrible is happening.
(0, 1, "The silver tabby cat sits in a hallway directly in front of a closed bathroom door with a strip of light under it, mouth wide open mid-yowl, head tilted up toward the door. Dim hallway light."),
# 131 From the cat's side, it kind of makes sense.
(0, 1, "A low floor-level view from behind the silver tabby cat, looking past its ears down a hallway toward a closed bathroom door with light glowing under it. The cat's ears are pointed forward, intensely focused on the door."),
# 132 The bathroom is a small room with a door, and closed doors are suspicious.
(0, 1, "Close-up of the silver tabby cat's face in a dim hallway, eyes narrowed suspiciously, ears turned sideways, staring at a closed door just out of frame. Moody low light."),
# 133 Once you're in there, you're sitting still, at roughly cat eye level, with nowhere to go.
(1, 1, "Inside a small bathroom: The Geek, fully clothed, sits on the edge of the bathtub with his hands on his knees and a deadpan expression, while the silver tabby cat sits on the bath mat directly in front of him, staring up into his face. Tiles, a sink, a towel rail."),
# 134 A captive audience, pretty much. Some cats also just love the tap, the sink, the cool tiles.
(0, 1, "The silver tabby cat sits curled inside a white bathroom sink, pawing with one white paw at a thin trickle of water from the tap, fascinated. Cool white and pale blue tiles, a mirror edge, a soap dish."),
# 135 And there's one more theory floating around. Cats are vulnerable when they use the litter box,
(0, 0, "A tidy corner of a laundry room: a ginger cat crouches in a covered litter box with its head poking out of the opening, looking around warily, ears turned back. Soft light, a plain tiled floor."),
# 136 so some people think your cat might be standing guard while you're in the same, well, position.
(0, 1, "The silver tabby cat sits upright and alert in front of a closed bathroom door like a little sentry on duty, chest out, ears swiveling, facing away from the door toward the hallway as if guarding it. Dim hallway, a night light."),
# 137 Nobody's proven that one. It's a nice idea, though.
(1, 1, "The Geek opens the bathroom door and finds the silver tabby cat sitting right outside facing the hallway like a guard; he looks down at it with a deadpan, faintly touched expression. Warm hallway light."),
# 138 Not every cat follows people around to the same degree, of course.
(0, 0, "A living room with three different cats: a fluffy ginger cat sleeps alone on a high shelf ignoring everyone, a black cat sits by the window, and a tuxedo cat follows a woman closely across the room. Soft daylight."),
# 139 Some breeds are known for being properly clingy.
(1, 1, "The Geek sits at his desk trying to type, with the silver tabby cat draped across his shoulders like a scarf, its ringed tail hanging down his chest. His expression is deadpan. Desk lamp, laptop, window."),
# 140 Siamese, Burmese, Abyssinians, Ragdolls and Sphynx cats all have a reputation as velcro cats.
(0, 0, "Five cats sit in a row along the back of a sofa, each drawn accurately to its breed: a cream Siamese with dark brown points and blue eyes, a sleek sable-brown Burmese with gold eyes, a ruddy ticked Abyssinian with large ears, a fluffy blue-eyed Ragdoll with a pale coat and dark points, and a hairless wrinkled pinkish Sphynx. Living room behind, soft light."),
# 141 A cat's own history matters too. Kittens that were bottle-raised by people,
(0, 0, "A close shot of a woman's hands bottle-feeding a tiny newborn ginger kitten wrapped in a small towel, the kitten sucking hungrily on the little bottle. A warm lamp, a heating pad and a soft blanket nearby."),
# 142 or taken from their mother very early, often grow up extra attached to humans.
(0, 0, "A young adult ginger cat follows a woman closely around her kitchen, pressed against her ankles, looking up at her constantly while she cooks. Warm kitchen light, cupboards and a stove."),
# 143 And a cat that lives alone with one person usually bonds much more strongly
(1, 1, "A small studio apartment at night: The Geek eats a bowl of noodles at a small table, and the silver tabby cat sits on the chair right beside him at the table, keeping him company. One warm pendant lamp, a dark window with city lights."),
# 144 to that person than a cat in a busy, noisy household.
(0, 0, "A busy, noisy family living room: three children running around with toys, a parent on the phone, a barking puppy, and a tuxedo cat hiding on top of a tall bookshelf looking down at the chaos. Bright daylight, a cluttered room."),
# 145 So, most of the time, a cat that follows you everywhere is a good sign.
(1, 1, "The Geek walks through a sunny park-like back garden, and the silver tabby cat walks happily beside him along the path, tail up. Flowers, a fence and a bright, cheerful afternoon."),
# 146 There are moments, though, when it's worth paying closer attention.
(1, 1, "The Geek kneels on the living room floor, leaning close and looking carefully and with concern at the silver tabby cat, which sits in front of him. Soft daylight, sofa and rug behind."),
# 147 In twenty twenty, researchers in Brazil surveyed the owners of more than two hundred cats.
(0, 0, "A university office in Brazil: three researchers sit around a table covered with paper questionnaires and laptops, sorting forms and comparing notes. A window shows a sunny tropical city with palm trees and hills. No readable writing on any paper or screen."),
# 148 About thirteen and a half percent of those cats showed signs of what's called separation-related problems.
(0, 0, "A row of many cats of different coats, ginger, black, calico, tuxedo, cream and brown tabby, sitting in a long line, most calm and relaxed, while a small group of them on one end look anxious with flattened ears and wide eyes. Plain soft background."),
# 149 These cats didn't just follow their owners around. They got genuinely distressed when the owner left.
(0, 0, "An empty apartment hallway just after the front door has closed: a ginger cat sits facing the shut door, ears flattened back, eyes wide and anxious. Daylight, a shoe rack, a coat hook."),
# 150 The signs included peeing or pooping outside the litter box, destroying things,
(0, 0, "A messy living room: a shredded sofa cushion with stuffing pulled out, a knocked-over potted plant with soil on the floor, and a ginger cat sitting in the middle of the mess looking anxious. Daylight, an otherwise empty room."),
# 151 crying or yowling for long stretches, and over-grooming until patches of fur came away.
(0, 0, "A ginger cat sits alone in an empty room, licking a small bald patch on its front leg, a few tufts of loose fur on the floor around it. Pale lonely daylight from a window."),
# 152 The study also found these problems turned up more in homes with no other pets,
(0, 0, "A bare, minimal apartment living room with almost no furniture: a ginger cat sits alone on an empty floor, with no other animals anywhere, looking small in the large empty space. Pale daylight from a window."),
# 153 and in homes where the cat had no toys.
(0, 0, "Close view of an empty wicker toy basket lying on its side on a bare wooden floor, and a ginger cat sniffing into it, finding nothing. Plain walls, soft light."),
# 154 The other thing to keep an eye on is sudden change.
(0, 0, "A senior black-and-white cat with a greying muzzle sits on a kitchen floor, looking at the viewer with tired, slightly cloudy eyes. Warm kitchen light, cupboards behind."),
# 155 If a fairly independent cat abruptly starts following you everywhere, especially an older cat,
(0, 0, "A kitchen: an elderly woman with grey hair in a cardigan walks across the room, and a senior black-and-white cat, slightly bony with a greying muzzle, follows closely at her feet. Warm kitchen light, cupboards, a kettle."),
# 156 that can be a sign something's off. Pain, an overactive thyroid, losing its sight or its hearing,
(0, 0, "Close-up of a senior black-and-white cat with a greying muzzle and slightly cloudy eyes, sitting hunched with its ears drooping, looking unwell. Soft dim light."),
# 157 or a kind of age-related confusion a lot like dementia,
(0, 0, "Night in a dim hallway: a senior black-and-white cat with a greying muzzle sits alone in the middle of the hallway, looking confused and lost, staring at a blank wall. A soft night light."),
# 158 any of those can make a cat suddenly clingy. A cat that feels unwell,
(0, 0, "An elderly woman with grey hair sits in an armchair, and a senior black-and-white cat presses itself tightly into her lap, eyes half closed, clinging to her. Warm lamp light."),
# 159 or unsure of its surroundings, will often stick close to the one thing that still feels safe.
(0, 0, "A senior black-and-white cat curled up tightly against an elderly woman's slippered feet beside her armchair, looking up at her. Warm, protective lamp light, a cozy living room."),
# 160 If the change comes out of nowhere, a trip to the vet is a good idea.
(0, 0, "A bright veterinary clinic exam room: a veterinarian in green scrubs gently checks a senior black-and-white cat on a steel exam table with a stethoscope, while an elderly woman owner stands beside it with her hand on the cat's back. Cabinets and a window."),
# 161 And if your cat's shadowing is healthy but, let's say, a bit much?
(1, 1, "The Geek sits at his desk trying to work, but the silver tabby cat sits squarely on top of his paperwork, directly between him and his laptop, staring at him. The Geek's expression is deadpan. Desk lamp, scattered papers without readable writing."),
# 162 There are easy fixes. Play with it properly, with a wand toy,
(1, 1, "The Geek sits on the living room floor holding a feather wand toy, and the silver tabby cat crouches in front of it, eyes locked on the feathers, rear end wiggling, about to pounce. Evening lamp light."),
# 163 for ten or fifteen minutes before you leave the house or head to bed,
(1, 1, "In the living room, The Geek swings a feather wand toy through the air, and the silver tabby cat leaps high off the floor mid-pounce, white front paws outstretched toward the feathers. Furniture pushed aside, energetic evening light."),
# 164 so it gets to hunt, catch, and then rest.
(0, 1, "The silver tabby cat lies stretched out asleep on a cushion, deeply content, with a feather wand toy lying beside it on the floor. Soft dim evening light, a peaceful mood."),
# 165 Use puzzle feeders, so food takes a bit of work.
(0, 1, "The silver tabby cat pokes a white paw into the hole of a colorful plastic puzzle feeder on the kitchen floor, fishing out a piece of kibble, concentrating hard. Daylight, a tiled floor."),
# 166 Put a perch by a window so there's something to watch other than you.
(0, 1, "The silver tabby cat lies on a padded window perch attached to a sunny window, watching small birds at a bird feeder outside, ears forward. Daylight, a plant."),
# 167 Keep a steady routine. And please don't punish a cat for following you.
(1, 1, "The Geek crouches down in the hallway and gently holds out his hand, and the silver tabby cat walks up and presses its head into his palm, tail up. Warm evening light, a calm, gentle mood."),
# 168 It isn't misbehaving. It's just looking for you.
(0, 1, "The silver tabby cat stands in the doorway of a dark room, looking in with wide searching eyes, as if looking for someone. Light from the hallway behind it, a gentle mood."),
# 169 If you want to give something back, try the slow blink. In twenty twenty,
(1, 1, "A close two-shot at eye level: The Geek lies on his stomach on the living room rug, face to face with the silver tabby cat, both of them with eyes half closed in a slow, peaceful blink. Soft warm light."),
# 170 scientists at the University of Sussex found that when people slowly narrowed their eyes at a cat,
(0, 0, "A British living room during a home study: a female researcher with short blonde hair sits on the floor slowly narrowing her eyes at a tuxedo cat on the sofa. A video camera on a tripod records nearby, rain outside the window."),
# 171 the cat was much more likely to slowly blink right back.
(0, 0, "Close-up of a tuxedo cat on a sofa with its eyes half closed in a slow, relaxed blink, looking calm and trusting. Soft rainy daylight from a window."),
# 172 Cats were also more likely to walk up to a stranger who'd slow blinked at them first.
(0, 0, "A ginger cat walks calmly toward a young man stranger in a denim jacket who crouches on a living room floor with his hand held out and eyes softly half closed. The cat's tail is up and relaxed. Soft daylight."),
# 173 It's about as close as we get to smiling at a cat in its own language. So.
(1, 1, "Close-up of The Geek's face with his eyes softly half closed behind his round glasses, and in the foreground the silver tabby cat's face with its eyes half closed too, a quiet, warm, trusting moment. Soft golden light."),
# 174 Why do cats follow their owners everywhere? Because for ten thousand years,
(1, 1, "The Geek stands still in the middle of his hallway, looking down, and the silver tabby cat sits at his feet looking up at him. They regard each other quietly. Warm lamp light, a long hallway behind."),
# 175 they've been choosing to live alongside us. Because to them you're part parent, part family,
(0, 0, "Sunset over an ancient Near Eastern mudbrick village: a sandy-brown striped wildcat sits on a flat rooftop beside a family in woven tunics sharing a meal around a small fire, the valley glowing orange behind them."),
# 176 and part territory. Because they like you more than most people assume, often more than food.
(1, 1, "The Geek sits on the sofa and the silver tabby cat lies contentedly in his lap, while across the room in the kitchen doorway a full food bowl sits untouched. Warm evening lamp light."),
# 177 Because they want to know where you are. And sometimes, honestly, because you're warm, you're interesting,
(1, 1, "The Geek sits wrapped in a blanket on the sofa, reading a book, and the silver tabby cat is curled up right against his side, one eye open, watching the pages. Warm lamp light, a cozy mood."),
# 178 and you might just be heading to the kitchen. So next time you get up for
(1, 1, "The Geek walks toward the kitchen in the evening, and the silver tabby cat trots eagerly just ahead of him, glancing back over its shoulder at him, tail up. Kitchen light glowing ahead."),
# 179 that glass of water and hear the soft thump behind you,
(1, 1, "A kitchen at night lit only by an under-cabinet light: The Geek fills a tall glass of water at the tap, and the silver tabby cat sits right beside his sneakers on the floor, looking up at him. Dark window, quiet mood."),
# 180 you'll know what it means. It's not just a nosy cat.
(1, 1, "The Geek, holding a glass of water, looks down at the silver tabby cat at his feet in a dark kitchen and gives it a small, warm, knowing look. The cat looks back up at him, tail curled around its white paws. Soft under-cabinet light."),
# 181 It's a small animal that's decided, for its own reasons, that you're worth following.
(1, 1, "A wide, warm shot of a moonlit apartment hallway: The Geek walks back toward the bedroom holding his glass of water, and the silver tabby cat follows a step behind him with its ringed tail held high. Moonlight through a window, a soft lamp at the end of the hall."),
]
