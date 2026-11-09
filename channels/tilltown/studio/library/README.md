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
| `worlds/` | A whole place, ready to film: add a camera and characters | `paris-street` |
| `sky/` | Light, sky, clouds. Every world starts here | `day.js`: `dayStage`, `clouds` |
| `ground/` | What people stand on | `ground.js`: `road`, `sidewalks`, `grass`, `avenue` (and the `cobbles`, `slabs` textures) |
| `buildings/` | Facades and rows of blocks | `haussmann.js`: `haussmannRow`, `block`, `facadeTex`, `farSkyline` |
| `nature/` | Plants, later rocks and water | `trees.js`: `tree` |
| `street-props/` | Objects placed in a street | `paris.js`: `lamp`, `morrisColumn`, `awning`, `cafeTables` |
| `landmarks/` | One-off famous structures | `eiffel.js`: `eiffel` |
| `characters/` | The toon renderer and recurring outfits | `toon.js`: `drawToon`, `toonCard`, 7 expressions; `cast.js`: `LUSTIG`, `PASSERSBY` |

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
- **Hats:** only `fedora` is drawn so far.
- **Daylight only so far.** Night needs a `sky/night.js`.

## After adding something
Add a view to `projects/library-preview/scenes/shots/preview.js`, then:

```
studio.cmd node render.mjs --project projects\library-preview --sheet --gl gpu --format jpeg
```

Copy `projects/library-preview/build/sheets/sheet_01.png` over `CATALOG.png`.

This folder is inside the git-ignored studio, so it has to be copied into git (`channels/tilltown/library/`) to be backed up.
