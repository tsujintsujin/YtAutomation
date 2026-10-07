"""Shared image-prompt builder for every video. Each video's scenes.py gives (geek, cat, place, action) per segment.

Rules (HANDOFF.md "Rules for the setup"):
- Every prompt stands alone: Gemini sees each one in a fresh chat with exactly 3 attached images, always in this
  order (bridge.py refs()): 1 the room (refs/style-ref.jpg), 2 the Geek sheet, 3 the cat sheet. Those 3 are the only
  things a prompt may point to. Everything else is described in full inside the prompt.
- Every scene has a place, and a place is described in full, with fixed colours, every time it is used.
- "the Geek" may only be named when the Geek block is in the prompt, "the silver tabby" only with the cat block.
"""
import re

STYLE = ("Generate one image. 16:9 landscape, full-bleed: the artwork fills the entire canvas edge to edge, like a single "
         "full-screen frame from an animated documentary on YouTube. Look: digital 2D animation background art, clean confident "
         "outlines of varying weight, cel shading with two tones of shadow, muted earthy natural palette, natural proportions, "
         "calm informative documentary mood, the scene continues past every edge of the frame. Match the art style of the first "
         "attached image exactly: its line weight, its flat two-tone cel shading, its muted earthy palette and its level of "
         "background detail. Every person and every animal is drawn in this 2D illustrated style, never photographic, never 3D "
         "rendered.")

GEEK = ("The Geek appears in this shot and must match the second attached image, his character sheet, exactly: a skinny young "
        "man with messy short dark-brown hair, large round thin black-framed glasses over simple black dot eyes, a few freckles "
        "across his cheeks, peach skin, an oversized forest-green hoodie with two dangling drawstrings and a front pouch pocket "
        "over a grey t-shirt, charcoal-grey jeans, black-and-white canvas sneakers. He is drawn in flat 2D comic style with thick "
        "black outlines and flat color, so he stands out against the detailed, textured environment. His humor comes from "
        "deadpan posture, not exaggerated faces. He carries no backpack, bag or anything on his back.")

CAT = ("A silver tabby cat appears in this shot and must match the third attached image, its character sheet, exactly: a "
       "medium-sized adult domestic short-haired cat with a pale silver-white coat covered in bold black swirling marbled tabby "
       "markings, a black bullseye swirl on each side of the body, black stripes down the spine, thin black lines on the "
       "forehead and cheeks, a black and silver ringed tail with a black tip, a clean white chest bib, a white muzzle and chin, "
       "four white paws, a pink nose, pale greenish-yellow eyes with vertical pupils, and medium triangular ears with pink "
       "insides. Natural cat anatomy and proportions, drawn in flat 2D comic style with thick black outlines and flat color like "
       "the attached sheet. It shows feeling only through ears, tail, eyes and posture, never a human-like smile or cartoon "
       "face. It is the only silver tabby cat in the image.")

NO_GEEK = ("The second attached image, the character sheet of a young man with round glasses and a green hoodie, is not used "
           "in this shot: he does not appear in this image.")
NO_CAT = ("The third attached image, the character sheet of a silver tabby cat with black swirling markings, is not used in "
          "this shot: that cat does not appear in this image; the only animals are the ones described below.")

NEGATIVE = ("Do not include: any border, margin, frame, panel outline, comic panel border, rounded corners, vignette, paper "
            "texture, text, letters, numbers, labels, captions, signs with writing, speech bubbles, watermarks, human-like faces "
            "on animals, chibi proportions, blush cheeks, photographic or 3D-rendered elements.")

# The room in the first attached image, written out too so the words and the picture agree.
ROOM = ("a small apartment living room with pale sage-green walls, an off-white ceiling and honey-brown wooden floorboards; "
        "against the back wall a worn brown fabric two-seat sofa with rolled arms, a beige knitted throw with a fringe draped "
        "over the middle of its backrest and an olive-green cushion in each corner; left of the sofa a tall leafy plant in a "
        "terracotta pot beside a white-framed window with cream curtains; right of the sofa a floor lamp with a cream fabric "
        "shade on a thin stand, then a tall dark-wood bookshelf full of books in muted greens, browns and creams; in front of "
        "the sofa a low rectangular wooden coffee table on a faded beige rug with a patterned border; in the right wall an open "
        "doorway into a small kitchen with dark-wood cabinets")
ROOM_IS = "This scene takes place in the room shown in the first attached image: " + ROOM + "."
ROOM_CLOSE = ("This is a close-up inside the room shown in the first attached image (" + ROOM + "). Only a small part of the "
              "room shows, softly out of focus behind the subject.")
NOT_ROOM = ("The first attached image is used for its art style only: this scene does not take place in the living room shown "
            "in it, so draw none of its walls, sofa, lamp, bookshelf or furniture. The place is described below.")

EVENING = (" It is evening: the window glass is dark blue with night outside, and the floor lamp is switched on and is the only "
           "light, filling the room with a warm golden glow and soft shadows.")
AFTERNOON = (" It is a sunny afternoon: warm sunlight comes through the window and falls in bright patches across the wall "
             "and the floor, and the floor lamp is switched off.")
MORNING = " It is early morning: soft pale sunlight comes through the window, and the floor lamp is switched off."

HOME_KITCHEN = ("A small apartment kitchen with pale sage-green walls, dark-wood cabinets above and below a beige countertop "
                "with a white electric kettle and a coffee maker, a white fridge, a window above the sink with cream curtains, "
                "a floor of cream-and-grey checkered tiles, and a small round wooden table with two wooden chairs.")
HOME_BEDROOM = ("A small apartment bedroom with pale sage-green walls and honey-brown wooden floorboards: a wooden double bed "
                "with a plain wooden headboard against the back wall, made with a crisp white duvet and two white pillows; a "
                "small wooden nightstand on the right with a lamp with a cream fabric shade and a round black alarm clock; a "
                "wooden chest of drawers; a faded beige rug beside the bed; a white-framed window with cream curtains on the "
                "left.")
HOME_HALLWAY = ("A narrow apartment hallway with pale sage-green walls and honey-brown wooden floorboards: a dark-wood front "
                "door with a brass handle at the far end, a row of wall hooks holding a grey coat, a low wooden shoe rack, a "
                "small framed landscape painting, and a ceiling light with a cream shade.")
HOME_OFFICE = ("A small apartment home office with pale sage-green walls and honey-brown wooden floorboards: a large cork board "
               "on the back wall, a wooden desk under it with a silver laptop and a desk lamp with a green glass shade, a black "
               "office chair, a short dark-wood bookshelf, and a white-framed window with cream curtains.")
PLAIN = "There is no room and no landscape: a plain soft warm cream background fills the frame."

# place key -> (uses the room image?, text). A video adds its own places in scenes.py with room=False.
HOME = {
    "room_evening": (True, ROOM_IS + EVENING),
    "room_afternoon": (True, ROOM_IS + AFTERNOON),
    "room_morning": (True, ROOM_IS + MORNING),
    "room_close_evening": (True, ROOM_CLOSE + EVENING),
    "room_close_afternoon": (True, ROOM_CLOSE + AFTERNOON),
    "kitchen_morning": (False, HOME_KITCHEN + " Bright early-morning sunlight through the window."),
    "kitchen_afternoon": (False, HOME_KITCHEN + " Warm afternoon light through the window."),
    "bedroom_night": (False, HOME_BEDROOM + " Night: the window is dark blue and only the bedside lamp is on, casting a warm glow."),
    "bedroom_morning": (False, HOME_BEDROOM + " Morning: bright sunlight streams through the window onto the bed; the bedside lamp is off."),
    "bedroom_close_night": (False, "A close-up on a bed made with a crisp white duvet, in a small bedroom with pale sage-green "
                            "walls softly out of focus behind, lit by the warm glow of a bedside lamp with a cream fabric shade."),
    "hallway_evening": (False, HOME_HALLWAY + " Evening: the ceiling light is on, casting warm light."),
    "hallway_afternoon": (False, HOME_HALLWAY + " Afternoon: daylight falls in from an open doorway on the left."),
    "office_afternoon": (False, HOME_OFFICE + " Afternoon daylight through the window."),
    "office_evening": (False, HOME_OFFICE + " Evening: the window is dark and the green desk lamp is on."),
    "plain": (False, PLAIN),
}

BANNED = re.compile(r"\bsame\b|\bagain\b|earlier|previous|as before|from before|other images|last (image|shot)|"
                    r"every (image|shot|frame)|\bhis (home|room|apartment|flat|house)\b|Geek's (home|room|apartment|flat|house)", re.I)


def check(i, geek, cat, place, action, places):
    """Fails the build on any scene that points outside its own prompt."""
    keys = place if isinstance(place, tuple) else (place,)
    for k in keys:
        assert k in places, f"scene {i}: unknown place '{k}'"
    hit = BANNED.search(action)
    assert not hit, f"scene {i}: points outside itself: '{hit.group(0)}'"
    if not geek:
        assert "Geek" not in action, f"scene {i}: names the Geek but he is not in the shot"
    if not cat:
        assert "silver tabby" not in action, f"scene {i}: names the silver tabby but it is not in the shot"


def place_text(place, places):
    if isinstance(place, tuple):                       # split image: (left, right)
        (_, a), (_, b) = places[place[0]], places[place[1]]
        return NOT_ROOM + " This is a split image with two halves. Left half: " + a + " Right half: " + b
    room, text = places[place]
    return text if room else NOT_ROOM + " Place: " + text


def full_prompt(geek, cat, place, action, places):
    parts = [STYLE, place_text(place, places)]
    parts.append(GEEK if geek else NO_GEEK)
    parts.append(CAT if cat else NO_CAT)
    return " ".join(parts + ["Scene: " + action, NEGATIVE])


def build(scenes, places):
    """scenes: list of (geek, cat, place, action). Returns [(geek, cat, scene_text, prompt)]."""
    out = []
    for i, (g, c, p, a) in enumerate(scenes, 1):
        check(i, g, c, p, a, places)
        out.append((bool(g), bool(c), a, full_prompt(g, c, p, a, places)))
    return out


if __name__ == "__main__":                            # self-check
    P = dict(HOME)
    assert "first attached image" in full_prompt(1, 1, "room_evening", "The Geek sits.", P)
    assert "does not take place" in full_prompt(0, 0, "plain", "A diagram.", P)
    for bad in [(0, 0, "plain", "The Geek waves."), (0, 0, "plain", "the silver tabby naps"),
                (1, 0, "room_evening", "the same sofa"), (1, 0, "nowhere", "x")]:
        try:
            check(0, *bad, P)
        except AssertionError:
            continue
        raise SystemExit(f"check let through {bad}")
    print("prompt_kit ok")
