# Tilltown: the look (art reference: Ricks Clips, Justin 2026-11-08)

Justin set the art reference to **Ricks Clips** (YouTube `UC_VeFWlNnRIg558hAeIpJ4w`, ~156K subscribers, Shorts only;
24 Shorts in ~26 days to 2026-11-02 for ~185M views, many at 5-32M). Not Crayon Capital, not Kaz's dark stick figures.
Characters are white (Justin 2026-11-08).

## What Ricks Clips looks like (checked 2026-11-08 in Chrome, 15 frames from 3 Shorts)
Shorts looked at: "This Shape Saved Roller Coasters" (newest), "Why Perfect Railroads Don't Work" (26M),
"The Ancient Jar That Warned an Empire" (32M, older style).
- **Characters:** flat 2D cartoon cut-outs with a dark outline (slightly hand-drawn line). A big round head, about a third
  of the figure's height, white (a villain had a purple head). Strong simple faces: thick angled brows, small dot or
  half-lidded eyes, small mouths, clear expressions (smirk, angry, worried with teeth). A hair patch (brown or grey).
  **A hat tells the role** (bowler, top hat, conductor cap, striped engineer cap, emperor's hat, helmet). Small torso in
  clothes with a few details (buttons, gold watch chain, tie, vest), thin dark stick arms and legs, small white round
  hands, small feet.
- **World (current style):** a bright, saturated, stylised **3D world**: real perspective, soft sun shadows, textured
  materials (gravel, planks, grass, rock, cobbles), blue skies with soft clouds; night scenes too (moon, stars, string
  lights). The older style (the jar Short) used detailed 2D painted backgrounds with outlines.
- **Characters live in the world:** they cast shadows, foreground objects pass in front (often blurred), the camera
  moves through the space (slow pushes, fast whips with motion blur).
- **Framing:** many close shots with the head big in frame; wides with small figures to set a place.
- **Captions:** 1-2 words at a time, white bold sans with a black outline, lowercase as spoken with punctuation, centred
  about 70% down the frame.
- **Props carry text** the viewer reads (a newspaper headline, a chalkboard diagram, a banner). Cartoon 2D effects sit in
  the 3D world (steam puffs, motion lines).

## How we make it (free, all code)
- Kaz's plugin engine renders it (`growkaz-stickman-studio/`): its Three.js kit builds the 3D world (sky, sun, soft
  shadows, textures drawn in code), the plugin renders and mixes as before.
- The characters: our own 2D toon renderer (outline, white round head, faces, hats, clothes, stick limbs), drawn to a
  canvas and placed in the 3D scene as a cut-out that faces the camera, so it casts a shadow and sits in the world.
- Reusable worlds and characters live in `growkaz-stickman-studio/library/`, one folder per category (`README.md` lists them,
  `CATALOG.png` shows them). Build new places from it and add new pieces to it.
- Captions: the engine's captions set to 1-2 words, white, black outline, as spoken.
- Voice: Mark (unchanged). Format: 16:9 long videos, 9:16 Shorts from the same scenes.

## Status
- 2026-11-08: 5-second test clip made (project `look-ricks`, 16:9). Next: the opening is rebuilt in this look, from a script with
  scene direction (`ANIMATION.md`). Its 34-shot list was made one shot per line, so it gets regrouped into scenes.
- Known gaps against Ricks Clips: world detail (flat facades, faceted trees; theirs have textured rock, gravel, grass),
  no hand-drawn wobble in the outlines, no motion blur on fast moves.
- Render: always add `--gl gpu --format jpeg --workers 2`. Without `--gl gpu` headless Chromium draws the 3D on the CPU
  (SwiftShader) instead of the GTX 1660 Ti: the 5-second test took 3m32s-4m07s that way and 24 s with the options
  (measured 2026-11-08, same scene).
- Trap: never lay a huge ground quad under nearer ground. It pokes through for a few frames (seen at 3.2 s in the test).
