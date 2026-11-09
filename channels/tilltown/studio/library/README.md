# Tilltown library: reusable 3D worlds and characters

Everything here is code, so any project can use it. In a shot file:

```js
import { parisStreet } from '/library/worlds/paris-street.js';
import { drawToon, toonCard } from '/library/characters/toon.js';
```

`CATALOG.png` shows every category. Each file's header comment lists its options.

## Categories
| Folder | What it holds | In it now |
|---|---|---|
| `worlds/` | A whole place, ready to film: add a camera and characters | `paris-street`, `blue-ridge` (day or storm, optional road and pond) |
| `sky/` | Light, sky, clouds. Every world starts here | `day.js`: `dayStage`, `clouds`; `storm.js`: `stormStage`, `stormClouds` |
| `ground/` | What people stand on | `ground.js`: `road`, `sidewalks`, `grass`, `avenue` (and the `cobbles`, `slabs` textures); `terrain.js`: `meadow`, `tufts`, `dirtRoad` |
| `buildings/` | Facades and whole buildings | `haussmann.js`: `haussmannRow`, `block`, `facadeTex`, `farSkyline`; `park.js`: `lookoutTower`, `cabin` |
| `nature/` | Plants, mountains, water | `trees.js`: `tree`, `pine`, `forest`; `mountains.js`: `ridges`; `water.js`: `pond` |
| `street-props/` | Objects placed in a scene | `paris.js`: `lamp`, `morrisColumn`, `awning`, `cafeTables`; `park.js`: `woodSign` |
| `vehicles/` | Things that drive | `truck.js`: `pickup` |
| `landmarks/` | One-off famous structures | `eiffel.js`: `eiffel` |
| `characters/` | The toon renderer, recurring outfits, animals | `toon.js`: `drawToon`, `toonCard`, 8 expressions, fedora and ranger hats; `cast.js`: `LUSTIG`, `RANGER`, `PASSERSBY`; `animals.js`: `drawBear`, `drawFish`, `drawClover` |
| `effects/` | Cartoon effects drawn over a shot | `toon-fx.js`: `bolt`, `flash`, `smoke`, `flame`, `sparks`, `dizzy`, `project`, `hit`, `blurBack` |

A new place (scrapyard, hotel room, Tilltown) goes in `worlds/`, built from the other categories. New pieces it needs go in
their category, so the next world can use them. A new kind of thing gets a new folder and a row here.

## Rules
- **Parts are reusable, finished shots are not.** Use the pieces freely and the same world within a story, with a new camera
  and action. Don't repeat the same shots across videos: it looks mass-produced (`research/06-production.md`, "Template feel";
  `channels/tilltown/RULES.md` section 6). For a new look of a world, change `seed`, `cafeAt` and the camera.
- **Views:** `paris-street` is built to be seen looking down the street toward -z, or from above. Behind z = +18 there is
  nothing. Up close, the café windows are plain amber and need an interior.
- **Ground:** never lay a huge sheet under nearer ground (see `ground/ground.js`). `road` and `sidewalks` are a strip: use
  them between buildings or the sides show empty sky.
- **Hats:** `fedora` and `campaign` (ranger) so far.
- **Day and storm only.** Night needs a `sky/night.js`.
- **Cut-outs:** anything past the edge of a `toonCard` image is clipped; pass a wider `W` for long props. To place effects on a card with `project`, know its ground height.

## After adding something
Add a view to `projects/library-preview/scenes/shots/preview.js`, then:

```
studio.cmd node render.mjs --project projects\library-preview --sheet --gl gpu --format jpeg
```

Copy `projects/library-preview/build/sheets/sheet_01.png` over `CATALOG.png`.

This folder is inside the git-ignored studio, so it has to be copied into git (`channels/tilltown/library/`) to be backed up.
