# How a video is animated

The rulebook for every video made in the studio in the Ricks Clips look, on any channel. Set by Justin 2026-11-09, after the
LuckySticks lightning test came out with wrong and broken-up scenes.

What went wrong, so it isn't repeated: the video was built one shot per script line from a picture list written for still
images, and "checked" only meant it rendered. A thumbs-up read as a "1" on the word "one". Mountains stood in for "Virginia".
Scenes in one place were split into separate clips that jumped and reset. A fishing cast played twice. A fish was cut off. A
black cat stood for "cursed".

## The order
| Step | What | Gate |
|---|---|---|
| 1 | Script with **scene direction** (`RULES.md` section 3, format below) | Nothing is built without it |
| 2 | Read the direction as a viewer, with the rules below | Every line passes |
| 3 | Voice and timestamps | Only the spoken lines are voiced |
| 4 | Build one scene at a time from the library | Each scene looked at in motion order |
| 5 | **Viewer check** of the real MP4 (below) | Every row says yes |
| 6 | Show Justin | Only after step 5 |

## Scene direction format
Written in `script.md`, with the narration. Only the quoted lines go into `script.json`; direction is never voiced.

```
SCENE 1: open field, storm. Ranger, hat on.
Starts: he stands alone in the field.

"One man was struck by lightning"
  Camera: low, slow push in.
  Action: he looks up; bolt hits him on "struck".
"seven times."
  Camera: pulls back, same spot.
  Action: six more bolts hit him; count climbs to 7.
"And he lived through every single one."
  Camera: pushes in.
  Action: hat smoking, clear thumbs-up.

Ends: standing, hat smoking.
```

## Rules for the direction
1. **Scenes before lines.** A new scene only when the place or the time changes. Same place and same action is one continuous
   scene running across as many lines as it needs; only the camera angle changes.
2. **The picture has to say it.** For each line: what does the viewer understand from the picture alone at that word? A place
   name needs something that says that place. A pretty view that says nothing gets redirected.
3. **Continuity.** Every scene has `Starts:` and `Ends:`: who is where, what they hold, what they wear, the weather. Each scene
   starts where the last one ended, unless the script jumps in time. Never restart an action the viewer has already seen.
4. **Show what the words say.** If he is struck, the bolt hits him, not the ground near him. If it "found him", he is in the
   shot.
5. **Nothing from nowhere.** Anything the story needs arrives on screen: the fish comes up on the line, the bucket is visible.
6. **Misread check.** Look at every gesture and object on the exact word it lands on. Could it read as something else? Hands and
   small props are drawn big and unmistakable.
7. **No animals for bad luck, curses or insults.** Never tie a term like that to an animal. Symbols come from the story itself.

## What not to work from
- A one-picture-per-line list ("Lines and pictures") is a format for still-image videos. Ideas can be taken from it; it is not
  a shot list.
- Kaz's `story-breakdown.md` says to cut on phrases, 2-3.5 s a shot. That does not apply here. Cuts follow the scene.
- A reference is studied for its **editing** too, by watching it in motion: how long scenes run, how the camera moves through a
  place, what motivates a cut. Still frames only show the look.

## Building
- **One scene is one entry in `story/shots.json` and one `registerShot`:** one world built once, one character state for the
  whole scene, camera angles changed by time inside it. Not yet used on a full video; the Eiffel opening is its first use.
- Character cut-outs use a wide image (`toonCard` with `W` 1800), so anything held fits. A prop past the edge is cut off flat.
- A bolt aimed low comes in from the side, so it doesn't run through the body on its way down.
- A bug that shows up twice gets fixed at its cause, then every other place it can happen gets checked.

## Viewer check
Required before anyone else sees the video. A table in the project at `build/viewer-check.md`, one row per spoken line, filled
in from frames of the **real MP4**, looked at **in order**, at least 270 px wide: first word of the line, middle, end.

| Line | Time | What is on screen | Does the picture say it? | Follows the shot before? | Misreads? |
|---|---|---|---|---|---|

- Any "no" gets fixed and re-checked before showing.
- **"Checked" means this table is complete and clean.** A clean render is reported as "renders clean", never "checked".
- Claude can't hear the video. Sound is always reported as not heard.
