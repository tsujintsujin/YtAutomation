"""Image prompts for ships-oakum-then-now, written as one story (channels/SHORTS_RULES.md "How image prompts are
written"; worked example: ../tooth-key-then-now/scenes.py). Checks every line against script.md; this file approves the
script (no approval step) and writes scene + full prompt for every line into script.json.
usage: python channels/what-happens-now/videos/ships-oakum-then-now/scenes.py"""
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
# back then (the eighteen hundreds)
SHIP = ("an old wooden sailing ship from the eighteen hundreds (a curved wooden hull made of long horizontal planks, "
        "three tall masts with square sails, rope rigging)")
HULL_GAPS = ("the side of an old wooden ship's hull seen up close: long horizontal wooden planks with wood-grain lines, "
             "and a thin dark gap running between every two planks")
SEA = "a wide open sea with small waves, a few seagulls and a cloudy sky"
PRISON_OUT = ("an old stone prison from the eighteen hundreds: high grey stone walls, small barred windows in rows, "
              "a heavy arched wooden gate with iron studs")
PRISON_IN = ("a bare room in an old prison in the eighteen hundreds: grey stone block walls, one small high window "
             "with iron bars, a stone floor, long plain wooden benches")
PRISONERS = ("prisoners from the eighteen hundreds (stick-figure men with short cropped hair in plain loose smocks "
             "and baggy trousers) sitting on the wooden benches")
PRISONER = ("a prisoner from the eighteen hundreds (a stick-figure man with short cropped hair in a plain loose "
            "smock and baggy trousers) sitting on a wooden bench")
GUARD = ("a prison guard from the eighteen hundreds (a stick-figure man in a long buttoned coat, a peaked cap and a "
         "big ring of keys on his belt)")
OLD_ROPE = ("old thick ship rope (twisted rope with dark tar stains, cut into short pieces about as long as an arm)")
OAKUM = "oakum (a soft fluffy heap of loose, tangled rope fibres)"
SCALES = ("old hanging scales (a short iron bar with a hook, and a flat metal pan hanging from it on three chains)")
SHIPYARD_OLD = ("an old shipyard by a river in the eighteen hundreds: an unfinished wooden ship hull of long "
                "horizontal planks resting upright on big wooden supports, wooden scaffolding planks along its side, "
                "piles of timber, a wooden shed and the river behind")
CAULKER = ("a caulker from the eighteen hundreds (a stick-figure man with his sleeves rolled up, a flat cap and a "
           "leather apron)")
CAULKERS = ("caulkers from the eighteen hundreds (stick-figure men with their sleeves rolled up, flat caps and "
            "leather aprons)")
MALLET = "a caulking mallet (a wooden hammer with a long round wooden head)"
IRON = "a caulking iron (a flat iron chisel with a wide blunt tip, held against the gap)"
PITCH_POT = ("a round iron pot of black pitch hanging over a small wood fire on a tripod of iron legs, the pitch "
             "bubbling with steam curling up")
LADLE = "a long-handled iron ladle"
# now
DRYDOCK = ("a modern shipyard dry dock: a huge deep concrete basin, a giant modern steel ship hull standing on blocks "
           "in it, tall yellow-armed cranes (drawn as black lines) towering above, steel walkways and ladders")
HULL_STEEL = ("the side of a giant modern steel ship hull seen up close: big flat steel plates joined edge to edge "
              "by smooth raised weld lines, with no gaps")
WELDER = ("a welder (a stick-figure worker in thick overalls, heavy gloves and a welding helmet with a dark flat "
          "visor)")
WELD_TORCH = "a welding torch (a handheld gun on a thick cable)"
BLASTER = ("a blaster (a stick-figure worker in a full-body suit and a big hood with a clear face window, holding a "
           "thick blasting hose with a short metal nozzle)")
PAINTER = ("a painter (a stick-figure worker in white overalls, a face mask and goggles, holding a spray gun on a long "
           "hose)")
LIFT = "a lift platform (a small railed basket raised on a tall folding metal arm)"
SHIP_STEEL = ("a giant modern steel cargo ship (a long smooth steel hull, a tall white block of cabins at the back, "
              "stacks of boxes on deck)")
# ---- the one coloured thing per picture (settings.json "colour_subject") ----
C_SHIP = "the ship's wooden hull: flat warm brown"
C_WATER = "the water squirting through the gaps: flat bright blue"
C_ROPE = "the rope and rope fibres: flat light tan, with darker brown tar stains"
C_PRISON = "the prison's stone walls: flat grey"
C_GUARD = "the guard's coat and cap: flat dark blue"
C_SCALES = "the old hanging scales: flat dark iron grey"
C_SHIPYARD = "the unfinished wooden ship hull: flat warm brown"
C_CAULKER = "the caulker's leather apron: flat brown"
C_TOOLS = "the mallet flat warm brown and the caulking iron flat dark iron grey"
C_PITCH = "the bubbling pitch: flat glossy black, with flat orange fire and flat light grey steam"
C_PITCH_HOT = "the hot pitch pouring from the ladle: flat glossy black, with flat orange heat lines"
C_PITCH_HARD = "the hard pitch line along the seam: flat glossy black"
C_SPLASH = "the sea water splashing against the hull: flat bright blue"
C_SAILS = "the ship's sails: flat cream white, and the sea flat blue"
C_STEEL = "the giant steel ship hull: flat dark red below and flat dark grey above"
C_SPARKS = "the welding sparks: flat bright orange and yellow"
C_WELD = "the smooth weld line: flat shiny silver grey"
C_GRIT = "the spray of grit: flat sandy brown"
C_PAINT = "the fresh paint being sprayed on the hull: flat dark grey"
C_LAYERS = "the paint layers: from the steel outward, flat grey, flat white and flat dark grey; the rust spot flat orange-brown with a flat red X over it"
C_REDPAINT = "the special paint on the bottom of the hull: flat dark red"
C_GROWTH = "the sea weed flat green and the shells flat sandy brown"
C_SHIP_NEW = "the steel ship's hull: flat dark red below the water line and flat dark grey above, and the sea flat blue"
C_SPLIT = ("on the left the rope fibres flat light tan, and on the right the hot pitch flat glossy black")
C_WELDER = "the welder's overalls: flat orange"
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
 shot(1, "A wooden ship had a gap",
      f"{SHIP} sails on the sea, seen from the side, its long planks clearly drawn along the hull.",
      SEA,
      "the old wooden sailing ship with its hull of long planks",
      "a modern ship, any engine or funnel, any flag with letters",
      colour=C_SHIP),
 shot(2, "between every plank.",
      f"{HULL_GAPS}. Thin jets of sea water squirt in through the gaps between the planks, with small drops flying.",
      "the side of an old wooden ship's hull at sea; the close view fills the whole frame, with a strip of sea "
      "at the bottom",
      "the thin gaps between the planks with water squirting through them",
      "any people, any rope yet",
      colour=C_WATER),
 shot(3, "So they stuffed every gap with old rope.",
      f"{HULL_GAPS}. A stick-figure hand pushes a long twist of loose rope fibres into one of the gaps; the gaps "
      "above it are already stuffed with rope fibres.",
      "the side of an old wooden ship's hull; the close view fills the whole frame",
      "the rope fibres being stuffed into the gap between two planks",
      "nails, glue, any modern tool",
      colour=C_ROPE),
 shot(4, "Back in the eighteen hundreds,",
      "Wide view of the old prison standing alone on a grey street of the eighteen hundreds, cobblestones in front, "
      "nobody outside.",
      PRISON_OUT,
      "the old stone prison of the eighteen hundreds",
      "any modern thing, any letters on the gate",
      colour=C_PRISON),
 shot(5, "the rope came from prisons.",
      f"Inside the bare prison room: a big heap of {OLD_ROPE} lies on the stone floor in the middle, and {PRISONERS} "
      "look at it.",
      PRISON_IN,
      "a heap of old ship rope inside the prison",
      "a ship, any modern thing",
      colour=C_ROPE),
 shot(6, "Prisoners got piles of old tarry ship rope.",
      f"{GUARD} drops an armful of {OLD_ROPE} onto the floor in front of {PRISONERS}; each prisoner already has a "
      "small pile of the old rope at his feet.",
      PRISON_IN,
      "the guard handing out piles of old tarry rope to the prisoners",
      "chains on the prisoners, any weapon",
      colour=C_GUARD),
 shot(7, "They picked it apart with their fingers,",
      f"{PRISONER} holds a short piece of {OLD_ROPE} in his lap and pulls its twisted strands apart with his "
      "fingers, frowning in concentration; a pile of loose fibres grows beside him.",
      PRISON_IN,
      "the prisoner pulling the rope apart with his bare fingers",
      "scissors, knives, any tool",
      colour=C_ROPE),
 shot(8, "strand by strand.",
      "Close view of two stick-figure hands: one holds the end of a twisted old rope, the other pulls one thin "
      "strand loose from it, and the strand splits into fine fluffy fibres.",
      PRISON_IN + "; the close view of the hands fills most of the frame",
      "fingers pulling one single strand loose from the rope",
      "any tool",
      colour=C_ROPE),
 shot(9, "Some had to pick two pounds of it a day.",
      f"{GUARD} weighs a heap of picked rope fibres on {SCALES}, holding the scales up by the hook; {PRISONER} "
      "waits beside him, tired, rubbing his sore fingers.",
      PRISON_IN,
      "the guard weighing the prisoner's day of picked fibres on the hanging scales",
      "any numbers or letters, modern digital scales",
      colour=C_SCALES),
 shot(10, "The loose fibers were called oakum.",
      f"{OAKUM} sits on the stone floor in the middle of the room, big and soft, a few fibres floating up from it.",
      PRISON_IN,
      "the soft fluffy heap of loose rope fibres",
      "any people, any letters",
      colour=C_ROPE),
 shot(11, "At the shipyard, workers called caulkers",
      f"Wide view of the old shipyard: {CAULKER} walks along the scaffolding planks beside the unfinished wooden ship "
      "hull, carrying a bundle of oakum (a soft fluffy heap of loose, tangled rope fibres) under one arm.",
      SHIPYARD_OLD,
      "the caulker arriving at the unfinished wooden ship in the shipyard",
      "a steel ship, any crane, any modern machine",
      colour=C_SHIPYARD),
 shot(12, "rolled the oakum into long strings.",
      f"{CAULKER} sits on the scaffolding plank and rolls a handful of oakum (loose, tangled rope fibres) against "
      "his thigh with his palm, making one long thin twisted string that hangs down beside him.",
      SHIPYARD_OLD,
      "the caulker rolling the loose fibres into a long string",
      "a machine, a spinning wheel",
      colour=C_ROPE),
 shot(13, "They pushed one into a gap between two planks.",
      f"{CAULKER} stands on the scaffolding and presses the long twisted string of oakum into a thin gap between two "
      "long horizontal planks of the ship's hull with his thumbs.",
      SHIPYARD_OLD,
      "the string of rope fibres being pressed into the gap in the hull",
      "nails, glue, any modern tool",
      colour=C_ROPE),
 shot(14, "Then they hammered it in deep,",
      f"{CAULKER} holds {IRON} against the stuffed gap in the hull with one hand and swings {MALLET} at it with the "
      "other; short bang lines burst where they meet.",
      SHIPYARD_OLD,
      "the caulker hammering the rope fibres deep into the gap",
      "a metal claw hammer, nails",
      colour=C_CAULKER),
 shot(15, "with a mallet and a flat iron chisel.",
      f"Close view: {MALLET} strikes the end of {IRON}, whose wide blunt tip presses the rope fibres into the gap "
      "between two planks; bang lines around the hit.",
      "the side of an old wooden ship's hull; the close view fills the whole frame",
      "the wooden mallet hitting the flat iron chisel in the gap",
      "a metal hammer, nails, a power tool",
      colour=C_TOOLS),
 shot(16, "Gap after gap, all over the ship.",
      f"Wide view: many {CAULKERS} stand on the scaffolding planks all along the unfinished wooden ship hull, top to "
      "bottom, each hammering a different gap; bang lines everywhere.",
      SHIPYARD_OLD,
      "many caulkers working on gap after gap along the whole hull",
      "any modern machine",
      colour=C_SHIPYARD),
 shot(17, "Next, a pot of black pitch bubbled over a fire.",
      f"{PITCH_POT}, on the ground beside the ship; {CAULKER} stirs it with a long stick.",
      SHIPYARD_OLD,
      "the iron pot of black pitch bubbling over the fire",
      "a modern stove, a gas burner",
      colour=C_PITCH),
 shot(18, "They poured the hot pitch over each stuffed gap.",
      f"{CAULKER} on the scaffolding pours hot black pitch from {LADLE} along a stuffed gap between two planks of the "
      "hull, the pitch running along the seam in a thin line.",
      SHIPYARD_OLD,
      "the hot pitch being poured along the stuffed gap",
      "a paint brush, a spray can",
      colour=C_PITCH_HOT),
 shot(19, "As it cooled, it set hard",
      "Close view of the side of the ship's hull: long horizontal planks, and between two of them a smooth, shiny, "
      "hardened line of pitch fills the gap completely; a few small shine marks on it.",
      "the side of an old wooden ship's hull; the close view fills the whole frame",
      "the hard shiny line of pitch sealing the seam",
      "any people, any gap left open",
      colour=C_PITCH_HARD),
 shot(20, "and sealed the gap shut.",
      "The side of the finished wooden ship's hull in the water: a wave splashes against the planks, and every "
      "seam is sealed with a black line of pitch; small drops bounce off and not one drop goes through.",
      "the side of an old wooden ship's hull at the edge of a river; the close view fills the frame, with water "
      "at the bottom",
      "sea water splashing on the sealed hull and none getting in",
      "any leak, any water squirting in",
      colour=C_SPLASH),
 shot(21, "Only then could the ship go out to sea.",
      f"{SHIP}, finished, sails out of the river mouth onto the open sea, its sails full of wind.",
      SEA,
      "the finished wooden ship sailing out to sea",
      "a modern ship, any engine",
      colour=C_SAILS),
 shot(22, "Today, most big ships are made of steel.",
      "Wide view of the dry dock: the giant modern steel ship hull towers over tiny stick-figure workers below.",
      DRYDOCK,
      "the giant steel ship hull in the modern dry dock",
      "any wooden planks, any letters or names on the hull",
      colour=C_STEEL),
 shot(23, "Huge steel plates are welded together,",
      f"{WELDER} kneels where two big flat steel plates meet edge to edge and runs {WELD_TORCH} along the join; a "
      "bright burst of sparks flies from the torch tip.",
      DRYDOCK,
      "the welder joining two big steel plates with sparks flying",
      "rope, pitch, any hammer",
      colour=C_SPARKS),
 shot(24, "so there are no gaps at all.",
      f"{HULL_STEEL}. A big tick mark beside one smooth weld line.",
      "the side of a giant modern steel ship hull in a dry dock; the close view fills the whole frame",
      "the smooth weld line with no gap at all",
      "any planks, any rope fibres",
      colour=C_WELD),
 shot(25, "Workers blast the steel clean",
      f"{BLASTER} stands on a steel walkway and points the thick blasting hose at the side of the giant steel hull; "
      "a wide cloud of spray hits the steel.",
      DRYDOCK,
      "the worker in a hood blasting the steel hull clean",
      "a broom, a sponge",
      colour=C_GRIT),
 shot(26, "with tiny bits of grit.",
      "Close view: the short metal nozzle of a thick blasting hose shoots a cone of tiny grit grains at flat steel; "
      "where it hits, the dull rough steel turns clean and shiny.",
      "the side of a giant modern steel ship hull; the close view fills the whole frame",
      "the tiny grit grains hitting the steel and cleaning it",
      "water, soap bubbles",
      colour=C_GRIT),
 shot(27, "Then the hull is sprayed with paint,",
      f"{PAINTER} stands in {LIFT} beside the giant steel hull and sprays a wide fan of paint onto it.",
      DRYDOCK,
      "the painter spraying paint onto the steel hull from the lift",
      "a paint brush, any letters",
      colour=C_PAINT),
 shot(28, "coat after coat, to stop rust.",
      "Cut-away close view of the edge of a steel plate showing three thin paint layers stacked on top of it like "
      "the layers of a cake; beside it, a small rusty patch drawn on a bare piece of steel is crossed out.",
      "the side of a giant modern steel ship hull; the close view fills the whole frame",
      "several layers of paint on the steel, and rust crossed out",
      "any letters or numbers",
      colour=C_LAYERS),
 shot(29, "The bottom gets a special paint,",
      f"Two painters (stick-figure workers in white overalls, face masks and goggles, each holding a spray gun on a "
      "long hose) stand under the curved bottom of the giant steel hull and spray it.",
      DRYDOCK,
      "the painters spraying special paint on the bottom of the hull",
      "any letters",
      colour=C_REDPAINT),
 shot(30, "so sea plants and shells can't grow on it.",
      "Under the sea: the smooth painted bottom of the steel ship's hull; strands of sea weed and small cone-shaped "
      "barnacle shells drift near it and slide off, with small arrows pointing away from the hull.",
      "under the sea beside the bottom of a giant steel ship: blue-black water lines, a few small fish, bubbles",
      "sea weed and shells sliding off the painted hull and not sticking",
      "a diver, any letters",
      colour=C_GROWTH),
 shot(31, "Then it's ready for the ocean.",
      f"{SHIP_STEEL} sails out across the sea, a white wake behind it.",
      SEA,
      "the finished steel ship sailing out to sea",
      "any sails, any letters or names on the hull",
      colour=C_SHIP_NEW),
 shot(32, "Back then, old rope and hot pitch.",
      f"The picture is split down the middle by a simple vertical line. Left half: in the bare prison room, "
      f"{PRISONER} pulls apart {OLD_ROPE}. Right half: in the old shipyard, {CAULKER} pours hot black pitch from "
      f"{LADLE} along a gap in the wooden hull.",
      f"left half: {PRISON_IN}; right half: {SHIPYARD_OLD}",
      "the prisoner picking rope on the left and the caulker pouring pitch on the right",
      "any modern thing",
      colour=C_SPLIT),
 shot(33, "Now? Not one gap to fill.",
      f"{WELDER}, with his visor flipped up, runs a gloved hand along the big flat steel plates of the giant hull, joined edge to edge by smooth raised weld lines with no gaps, smiling, a big tick mark beside "
      "his hand.",
      DRYDOCK,
      "the welder's hand sliding along the smooth steel hull with no gaps",
      "rope, pitch, any wooden planks",
      colour=C_WELDER),
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
