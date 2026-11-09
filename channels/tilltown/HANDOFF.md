# Tilltown: full handoff

**A new session starts here.** Last updated 2026-11-09. Read this file, then `RULES.md` and `LOOK.md` in this folder, then
`growkaz-stickman-studio/library/README.md`. `research/README.md` is the research the channel is built on.

Master copy: `channels/tilltown/HANDOFF.md` in git. A copy sits at `growkaz-stickman-studio/HANDOFF.md` so it can be opened
from the shared folder. If you change one, copy it over the other.

**Claude runs this channel end to end** (Justin, 2026-11-07: "i need you to fully handle this channel", "if there's a
blocker that needs me, work on something else and note it"). Justin does only what needs his own Google account or his
decision. Those steps are listed below.

## Where everything is
| What | Folder or file |
|---|---|
| **The studio** (renders everything; local only, git-ignored) | `D:\AIO Freelance\YtAutomation\growkaz-stickman-studio\` |
| **Library of reusable worlds and characters, by category** | `...\growkaz-stickman-studio\library\` (`README.md`, `CATALOG.png`) |
| Library preview project (one view per category) | `...\growkaz-stickman-studio\projects\library-preview\` |
| 5-second look test | `...\growkaz-stickman-studio\projects\look-ricks\out\Tilltown_look_test.mp4` |
| Video 1 project | `...\growkaz-stickman-studio\projects\eiffel-tower\` |
| Channel documents | `channels/tilltown/` in git: this file, `RULES.md`, `LOOK.md`, `TOPICS.md`, `settings.json` |
| Git backup of the studio work | `channels/tilltown/studio/`: `library/`, `projects/`, `engine.patch`, `studio.cmd` |
| Video 1 script, sources, Mark's voice | `channels/tilltown/videos/eiffel-tower/` (`voice.wav` and `audio/` are git-ignored; the studio project has its own copy of the voice in `input/voiceover.wav`) |
| Kaz's plugin as downloaded | `C:\Users\justi\Downloads\GrowKaz_Stickman.plugin` |
| Kaz's skills and the clean kit | `C:\Users\justi\.claude\skills\` (`make-2d-video`, `new-video`, `video-styles`, `render-video`, `video-sound`); clean kit in `make-2d-video\kit\` |
| Research | `research/` in git (`06-production.md` section 6.2 says "we don't need his plugin": out of date, ignore that line) |
| Reviewer agent (read-only check of plans and outputs) | `C:\Users\justi\.claude\agents\reviewer.md` |

## State on 2026-11-09
**Done**
- Channel created. Research done. Topics chosen (first five in `TOPICS.md`).
- Video 1 opening: script (263 words), sources checked, Mark's voice (83.6 s), word timestamps, story bible, a 34-shot list
  timed against the voice.
- Art reference set to Ricks Clips; look spec written (`LOOK.md`).
- Toon character renderer; a 3D Paris world; a 5-second test clip with voice, captions, music and ambience. Sent to Justin,
  who replied "sounds good" and asked to reuse the world.
- Render speed fixed: 24-26 s for those 5 seconds instead of about 4 minutes.
- Library in 10 categories, tested: the clip builds from it unchanged, and the same world gives different views.
- A full 40-second 9:16 test (2026-11-09): LuckySticks' posted "struck by lightning seven times" Short remade in this look with its existing voice. Sent to Justin, private, not uploaded: `growkaz-stickman-studio/projects/sullivan-lightning/out/`. It rendered in 2m09s to 2m50s. One earlier run crashed and did not repeat; the error text was lost.

**Not done**
- The 34-shot opening in the new look. Only the test shot exists.
- The rest of video 1: the script is the opening only. A full video is 12-16 minutes.
- Nobody has listened to the test clip's sound on Claude's side. Claude can check that audio exists, not how it sounds.
- Channel art, thumbnails, Shorts, uploads, analytics.

## The channel
- **Tilltown**, handle **@Tilltown**, channel ID `UCqZM2RVq6Fo56mV6pFONLZw` (created by Justin 2026-11-07, a Brand Account like
  The Paperback Millionaire). Studio: https://studio.youtube.com/channel/UCqZM2RVq6Fo56mV6pFONLZw
- No picture, banner or videos yet. Standard features on. Intermediate features (custom thumbnails, videos over 15 min) show
  "Eligible", so the channel is **not phone-verified yet**.
- **Voice: Mark** (Justin 2026-11-07: "keep mark"), through Chatterbox, so every upload has **"Altered content: Yes"**. Justin
  picks any other voice for characters; never add one without asking him.

## Waiting on Justin
| # | What | Why only him | Blocks |
|---|---|---|---|
| 1 | **Phone-verify** Tilltown: Studio → Settings → Channel → Feature eligibility → "Intermediate features" → verify | His phone | Custom thumbnails, videos over 15 min |
| 2 | **Character voices**, if the cast speaks: Claude proposes 2-3 to pick from | He asked to choose them | Dialogue with its own voices (the narrator reads them until then) |
| 3 | Watch the first finished MP4 before it goes public | He asked for this on every channel | Video 1 going public |
| 4 | At eligibility: AdSense for YouTube, 2-Step Verification, the Partner Program application | His accounts | Monetization |

Done by Justin: channel created (2026-11-07); narration voice decided (2026-11-07); art reference chosen (2026-11-08).

YouTube's rules say a terminated channel can mean losing all of that person's channels. This channel is kept clean
(`RULES.md`: facts, copyright, no repeats), but the risk exists for any channel under the same owner.

## What Tilltown is
- **Money and business stories, explained simply**: famous fortunes, company rises and falls, scams, crashes and bubbles.
  Chosen from 8 niches on the month's YouTube numbers (`research/03-niche.md`).
- **Long videos first** (12-16 min, ~2,300-2,900 words at our voice's ~187 words a minute). **2-4 Shorts per long video**, each
  a complete fact, each linking to its long video (`research/02-long-and-shorts.md`).
- Money mechanisms get acted out in **Tilltown**, a little town with a recurring cast.
- **Target:** the Partner Program bar for new channels from 2027-02-01: **1,000 subscribers + 8,000 long-video watch hours in
  12 months** (`research/01-monetization.md`). Apply earlier only if a video breaks out.

## The look
Full spec: `LOOK.md`. In short: **Ricks Clips** (Justin 2026-11-08, "use ricksclips as art reference"): flat 2D toon characters
with **white** round heads, standing in a bright, saturated 3D world, with 1-2 word white captions.

That reference is for **art only**. Scripts follow `RULES.md`. Ricks Clips is Shorts only, so 16:9 long videos are our own
adaptation of the look.

What was tried and rejected, so nobody repeats it:
| Look | Why it's out |
|---|---|
| Self-made "cut paper" and a Crayon/PENNY-style frame | Invented without a real reference (2026-11-07) |
| HyperFrames scenes | Discarded test. Videos run on Kaz's engine, as Justin told us to |
| Kaz's dark stick figures with a self-made indigo-and-amber palette | The palette had no research behind it. Replaced by Ricks Clips |
| **Crayon Capital as an art reference** | Justin: "stop fucking using the crayon channel as art reference". Money channels are references for topics and packaging only |

## How a video is made
Run from `growkaz-stickman-studio\`. Everything is free and local. In bash on this PC, wrap studio commands as
`cmd //c ".\\studio.cmd node render.mjs ..."`.

1. **Script and facts** per `RULES.md`, every claim in `sources.md`, in `channels/tilltown/videos/<slug>/`.
2. **Voice:** from the repo root, `chatterbox/.venv/Scripts/python voice_cb.py channels/tilltown/videos/<slug>` (Chatterbox copying
   Mark; reads `script.json`, writes `voice.wav` and `timings.json`). Book videos have first claim on the PC.
3. **Project:**
   `.venv/Scripts/python.exe tools/new_project.py --name <slug> --voice <path> --script <path> --aspect 16:9 --resolution 1080p --title "<title>" --captions --style tilltown`
4. **Timestamps:** `.venv/Scripts/python.exe tools/transcribe.py --project projects/<slug> --script input/script.txt`
5. **Config** (`config.json`), as in `projects/look-ricks/config.json`: `"bars": "none"`,
   `"captionStyle": {"max": 2, "phrase": true, "upper": false, "hi": "#ffffff", "font": "Montserrat", "weight": 900, "y": 800, "size": 72}`.
6. **Story:** `story/bible.md` and `story/shots.json`, per Kaz's `make-2d-video/references/story-breakdown.md`. Each shot starts
   0.1-0.2 s before its phrase, median 2-3.5 s.
7. **Build shots** in `scenes/shots/*.js`, importing from `/library/...`. New places go in the library first.
   `projects/look-ricks/scenes/shots/01_test.js` is the working example.
8. **Check batches on a contact sheet:** `.\studio.cmd node render.mjs --project projects\<slug> --sheet --gl gpu --format jpeg`,
   then look at it against Kaz's `references/render-qc.md`.
9. **Preview a range:** `.\studio.cmd node render.mjs --project projects\<slug> --from 0 --to 5 --gl gpu --format jpeg --workers 2`
   (writes `build/preview.mp4`).
10. **Full render:** the same without `--from/--to`. **Anything long runs in n8n or its own window, never as a background task
    of a Claude session.**
11. **Sound and final MP4:** `.\studio.cmd python audio\mix.py --project projects\<slug>` (writes `out/<title>.mp4`). Music, SFX
    and ambience come from `story/shots.json`, per Kaz's `references/sound-design.md`.
12. **Check the real MP4:** frames from it, including mid-gesture and every shot change, then send Justin the first one.

### Render speed (measured 2026-11-08 on the 5-second test)
**Always use `--gl gpu --format jpeg --workers 2`.** Without `--gl gpu`, headless Chromium draws the 3D on the CPU (SwiftShader)
instead of the GTX 1660 Ti.
| | CPU (default) | GPU + JPEG |
|---|---|---|
| Drawing a frame | 2,056 ms | 154 ms |
| Capturing a frame | 1,208 ms (PNG) | 72 ms |
| The 5-second clip | 3m32s to 4m07s | 24-26 s (one run took 61 s, cause not looked into) |

Estimates from that, if other shots are about as heavy: ~7 minutes for the 85-second opening, ~1 hour for a 14-minute video.

## The library
`growkaz-stickman-studio/library/`, importable from any project as `/library/...`.

| Category | In it now |
|---|---|
| `worlds/` | `paris-street`, `blue-ridge` |
| `sky/` | `dayStage`, `stormStage`, `clouds`, `stormClouds` |
| `ground/` | `road`, `sidewalks`, `grass`, `avenue`, `meadow`, `tufts`, `dirtRoad` |
| `buildings/` | `haussmannRow`, `block`, `facadeTex`, `farSkyline`, `lookoutTower`, `cabin` |
| `nature/` | `tree`, `pine`, `forest`, `ridges`, `pond` |
| `street-props/` | `lamp`, `morrisColumn`, `awning`, `cafeTables`, `woodSign` |
| `vehicles/` | `pickup` |
| `landmarks/` | `eiffel` |
| `characters/` | `drawToon`, `toonCard`, 8 expressions, `LUSTIG`, `RANGER`, `PASSERSBY`, `drawBear`, `drawFish`, `drawCat`, `drawClover` |
| `effects/` | `bolt`, `flash`, `smoke`, `flame`, `sparks`, `dizzy`, `project`, `hit`, `blurBack` |

- Limits: day and storm only; fedora and ranger hats only; `paris-street` works looking down the street or from above, with nothing behind
  z = +18; café windows need an interior for close-ups.
- **Reuse pieces, not finished shots.** Same shots across videos look mass-produced (`research/06-production.md`, "Template
  feel"; `RULES.md` section 6). Vary `seed`, layout, camera and action.
- After adding to it: add a view to `projects/library-preview/scenes/shots/preview.js`, render the sheet, and copy
  `build/sheets/sheet_01.png` over `library/CATALOG.png`.

## Our changes to Kaz's kit
The studio is outside git, so a fresh install loses these. `channels/tilltown/studio/engine.patch` has all of them, tested
against the clean kit (2026-11-08). Apply from the studio folder with `git apply --whitespace=nowarn -p1 <path to engine.patch>`,
then run `npm install` for the font.
- `engine/styles.js`: the `tilltown` style (bright clean grade, a saturated `day` mood; night, dusk and interior moods are left
  over from the old look and still need checking for this one).
- `engine/ui2d.js`: captions take `upper`, `font`, `weight`, `phrase` (`phrase` breaks after punctuation).
- `engine/player.js`: loads Montserrat. `package.json`: `@fontsource/montserrat`.
- `tools/verify_kit.py` reports these 4 files as MISMATCH (25/29 verified): expected. Do not follow its advice to copy them again.

**Keep git in step.** After changing the library or a project, copy it into `channels/tilltown/studio/` and commit. To remake the
patch: `diff -u --label a/<file> --label b/<file> <kit file> <studio file>` for each of those four files.

## Video 1: The Man Who Sold the Eiffel Tower
Project: `growkaz-stickman-studio/projects/eiffel-tower/`.

**Keep:** the voice, `timeline/`, and the timing, lines and sound cues of `story/shots.json` (34 shots, 85.14 s, median 2.52 s).
**Change when rebuilding:**
- `config.json`: `captions` on with the Tilltown caption style, `"bars": "none"`.
- `story/shots.json`: each `scene` text was written for the dark look. Remove the `scope`/`none` bars. Most scenes become daylight.
- `story/bible.md`: story, roles, places and motifs stand. Its look section is marked out of date.
- `scenes/` (`cast.js`, `sets/paris.js`, `shots/01_open.js`): old look. Replace.

**Places the shot list needs** (only Paris street exists):
| Shots | Place |
|---|---|
| s001, s004, s009, s025, s026 | Paris street (have it) |
| s002, s010 | Close on the tower's iron; tower with a giant price tag |
| s003, s005, s011 | Poisson's scrapyard with a platform scale |
| s006, s007 | Police station front in the rain (needs night) |
| s008 | Railway platform with a departing train |
| s012, s016 | Table top with three gold cards (the three tricks) |
| s013-s015, s017 | 2025 living room, a phone, the $920 million data card |
| s018-s024 | Tilltown: main street, clock tower, junk shop inside |
| s027 | 1920s printing press |
| s028, s029 | Hôtel de Crillon front; Place de la Concorde |
| s030, s032-s034 | Hotel suite and meeting room |
| s031 | Diagram: invitations going out |

**Characters needed:** Poisson (yellow cap), "you" (blue hoodie), the junk dealer (green beanie), more hats and body types,
close-up heads, hands holding things.

**Script notes:** only the opening exists. The "Trick one: look official" heading was not voiced. Whisper heard "Crillon" as
"clion": listen for a mispronunciation.

**Facts already checked for the later parts** (claims and links for the opening are in `videos/eiffel-tower/sources.md`):
- Smithsonian (Jeff Maysh, 2016, citing Secret Service agent James Johnson's memoir): arrested 10 May 1935, escaped 1 Sep 1935
  (bedsheet rope, posed as a window cleaner), recaptured 28 Sep 1935 in Pittsburgh; 20 years, Alcatraz from April 1936; died
  11 March 1947 in Springfield, Missouri (pneumonia); death certificate: "Apprentice salesman".
  https://www.smithsonianmag.com/history/man-who-sold-eiffel-tower-twice-180958370/
- The tower operator's page says he died at Alcatraz. The death certificate says Springfield: use Springfield.
- Contested, keep out of the script: the price paid, "a month" vs "six months" before the second attempt, whether the other
  bidders were real dealers or accomplices.
- The three tricks: look official; a reason to act fast and quietly; money the victim can't chase (a bribe = shame = no police;
  today: gift cards, crypto).

## Next steps, in order
1. Close the look gaps from `LOOK.md` while building: more world detail, slight hand-drawn line wobble, motion blur and fast
   whips, more hats and body types.
2. Add `sky/night.js` and the missing places to the library, in batches, each checked on the preview sheet.
3. Rebuild the 34-shot opening. Contact sheet after each batch, then a preview, then frames from the real MP4.
4. Send Justin the finished opening.
5. Write the full script (12-16 min) per `RULES.md`, fact-check it, voice it, build it.
6. Thumbnails and channel art. Plan: same engine, not tested yet.
7. Shorts at 9:16 from the same worlds. Not tested yet; compositions will need re-framing.
8. Upload per `RULES.md` section 7. Set up monitoring below.

## The plan
Each phase: plan → small test → real run. Nothing is called done without looking at the real output.
- **Phase 1, look:** done pending the finished opening. Test clip made, library built.
- **Phase 2, pipeline:** steps above, proven on the opening, then on one full 12-16 min video that passes a frame-by-frame look.
  Long renders in n8n or their own window. Book videos keep first claim on the PC (voice, GPU).
- **Phase 3, launch:** channel art; title and thumbnail first for each video; 3 scripts written ahead; video 1 and its Shorts;
  Test & Compare on; Justin watches video 1; then public.
- **Phase 4, running:** 1-2 long videos and 4-8 Shorts a week to start, set by measured capacity in the first two weeks. Daily
  read, one change at a time, a format judged after ~10 videos.

## How Justin wants this run
Learned the hard way on 2026-11-07 and 08. Each of these cost him real time.
- **Decide channel matters yourself and act.** Content, look details, process. He asked "why are you asking me?" Only the
  "Waiting on Justin" list goes to him.
- **A reference he gives is the spec.** Study it before building: open it, read real frames, listen to what is said. He once had
  to analyse Kaz's video himself. Never build without a reference.
- **Check that a reference is current.** He caught a year-old reference being used.
- **No guessing.** Measure, look, or say you don't know. "Is that from the research?" needs a checked answer. The palette guess
  was exactly this failure.
- **No shortcuts.** Global Rule Zero. Understand first, then build.
- **Test small first, then look.** One frame or a 5-second clip before a batch. Look at frames, including mid-motion. The green
  road glitch only showed up on three frames.
- **If he corrects something, fix the thing.** "so modify? maybe? why do i even have to tell you this?"
- **No background agents without saying the token cost first.** He had one stopped for burning tokens.
- **Justin pays for nothing.** No paid APIs or plugins.
- Close Chrome tabs after checking videos. Never leave a video playing. Never play our own videos from analytics checks.
- Scratch work on D: only.

## Traps found
| Trap | What to do |
|---|---|
| Render on CPU by default | Always `--gl gpu --format jpeg --workers 2` |
| Huge ground sheet under nearer ground pokes through for a few frames | Keep ground pieces from overlapping (`library/ground/ground.js`) |
| `studio.cmd` "not recognized" | This PC needs `.\studio.cmd` |
| `cmd //c` breaks quoted titles | Run `new_project.py` with the venv's Python from bash |
| `--out` is relative to the studio folder, and its folder must exist | Leave it off; previews go to `build/preview.mp4` |
| Long bash heredocs can break under the command hook | Write a script file with the Write tool and run it |
| Chrome can't open `file://` pages through the extension | Open real URLs |
| First Chrome screenshot after loading can time out | Take it again |
| A character in a dark building shadow casts no visible shadow | Place characters in the sun |
| `ffmpeg` filter paths with `D:` break on the colon | Use a relative path |
| A prop past the edge of a toon image is cut off flat | Pass a wider `W` to `toonCard` |
| An effect placed with `project` lands in the frame corner | The position was NaN: the card has no `ground` height set |
| The film-grade colour step runs in JS per pixel | Fine at 154 ms a frame; look here first if renders slow down |

## Bad scenarios and what we do
| Scenario | What we do |
|---|---|
| Videos barely shown (0-4 views in 24 h) | Read impressions, click rate, traffic sources at 24 h and 72 h. Under ~100 impressions: check restrictions, "made for kids", policy notices, whether the exact title shows in YouTube search. Impressions but CTR < 2%: change title/thumbnail at 48-72 h. Never delete or re-upload, never buy views. |
| 5 videos in a row barely shown | Stop before video 6 and diagnose. All 5 under-shown and not in search = the channel is held back: change what may be flagged or start over. Shown but not clicked = redo the packaging style. Clicked but not watched = change topic family. |
| Shorts probe | Shorts from day one. Shorts get views but long videos don't = the long videos' topics/packaging; nothing gets views = the channel. |
| First 5 videos have no floor | First 5 long videos on well-known, searched subjects. |
| Rejected as mass-produced | Each video a different story with real facts and its own scenes; library pieces varied, never the same shots; opinion labelled as ours; honest titles. |
| Nobody clicks | Title + thumbnail before the script; topic dropped without a strong pair; Test & Compare on every video. |
| Most videos miss | Expected (hit game). Judge after ~10, one change at a time, notes in `LEARNINGS.md`. |
| Niche gets crowded or fades | Monthly niche scan (`research/tools/nichescan.py`); never repeat a premise. |
| Shorts bring viewers who never watch long videos | Long first; every Short links its long video; drop Shorts if they bring nothing. |
| Low-paying viewers | US-centred money topics. |
| Copyright claims | Only our own animation and art; no film or TV clips; see the music item under Open items. |
| Legal trouble about real people/companies | Every claim backed by a named source or court record; opinion said as opinion; nothing alleged that isn't on record. |
| Wrong facts | Fact-check pass before voice; every number/date/claim in `sources.md`. |
| A strike reaching other channels | The rules above; any notice reported to Justin the same day. |
| The PC is the only factory | 3 scripts ahead; capacity measured, pace set from it. The studio work is backed up in git. |
| Sessions lose track | This file and the daily log are kept current; every session starts here. |
| Waiting on Justin | Listed above; other work goes on. |
| "This is AI" comments | Comments read daily; change what triggers it if it recurs. |
| Studio page changes break uploads | Every upload checked in Studio; manual fallback with Justin. |
| YouTube changes the rules | Monetization and AI-label pages re-read monthly. |
| Views but no subscribers | Read subscribers per 1,000 views; recurring cast, a thread to the next video. |

## Monitoring (starts with the first video)
The morning analytics task (`channels/ANALYTICS.md`) gets a Tilltown section. Read-only, Claude in Chrome, never plays our videos.
| When | Long videos | Shorts |
|---|---|---|
| 24 h | Impressions, CTR, views, traffic sources | Views, stayed to watch % |
| 72 h | CTR vs our others, % still watching at 30 s, retention drops, subscribers | Stayed %, average % watched, subscribers |
| 7 days, then weekly | Views/day, watch hours, subs per 1,000 views, Test & Compare result, clicks from Shorts | Clicks to the linked long video |
| Daily | Channel totals: subscribers, 12-month watch hours vs the goal line | |

Health checks daily: Studio notifications (claims, policy, limited ads), each new upload searched by exact title, comments.
Justin hears only about steps he must do, strikes/claims, and milestones.

**Goal line:** 8,000 h in 12 months = ~22 h/day = ~1,315 min/day ≈ 220-330 long-video views/day at 4-6 min average watch.

## Where the data lives
```
channels/tilltown/
  HANDOFF.md            this file
  RULES.md              how a video is written, checked and posted
  LOOK.md               the art reference and how it is made
  TOPICS.md             candidate topics with their YouTube check
  settings.json         channel id, voice, upload settings
  studio/               git backup of the library, projects and our engine changes
  LEARNINGS.md          what worked, what didn't (from the first readings)
  analytics/raw/<date>.json, analytics/<date>.md   the morning read
  videos/<slug>/        script.md, sources.md, title/thumbnail ideas, posted.json
```
Plus a **Tilltown** tab in the Google Sheet "Shorts - Posts and Analytics" (justin.masiga.94's Drive), filled each morning. GitHub
weekly: analytics, learnings and video records in one pull request a week.

Justin sees it on the dashboard (http://127.0.0.1:8770, Tilltown tab and Analytics page; desktop only), the sheet, and these files.

## Open items
1. **Music.** `RULES.md` says YouTube's Audio Library only. The plugin generates its own music in code, used in the test clip.
   Generated music is our own, so copyright is fine, but its quality hasn't been judged by ear. Settle it with the first finished
   opening.
2. **Dashboard: long-video analytics and goal line.** The Analytics page only knows Shorts. Waiting on another session's
   uncommitted `dashboard.py` / `dashboard.html` edits on branch `claude/whn-sources`.
3. **Google Sheet tab "Tilltown":** add with the first reading.
4. **A way to run long renders outside a Claude session** (n8n workflow or a double-click script started through `explorer.exe`).
5. **Thumbnail method:** planned from the same engine; `RULES.md` section 2 applies. Not tested.
6. `channels/book-stories/niche_scan.py` reads "1mo ago" as 1 minute. Fixed in `research/tools/nichescan.py`; the book-stories copy
   was left alone because it is uncommitted on another session's branch.
7. Ricks Clips scripts and sound were not studied; Justin's reference was art. A third-party video summarises their script as hook,
   "Luckily/Unluckily", "You see", callback. Unchecked.

## Decisions
- 2026-11-07 (Justin): Claude makes and fully runs a new channel to monetization. Blockers go in "Waiting on Justin".
- 2026-11-07 (Claude): money and business stories explained simply; long first + Shorts; name **Tilltown** (@Tilltown was free).
- 2026-11-07 (Justin): narration voice Mark.
- 2026-11-07 (Justin): use Kaz's plugin, not a self-built kit. It remains the render engine.
- 2026-11-08 (Justin): art reference Ricks Clips; characters white; Crayon Capital is not an art reference.
- 2026-11-08 (Claude): 3D worlds with Kaz's Three.js kit, characters as flat cut-outs inside them; captions on (2 words, white,
  Montserrat); render on the GPU.
- 2026-11-08 (Justin): reusable worlds, sorted into categories.

## Daily log
| Date | What happened |
|---|---|
| 2026-11-07 | Research done (`research/`), plan agreed, channel files written, name picked, topics written. |
| 2026-11-08 | Kaz's plugin installed. Opening voiced, timed, bible and 34-shot list written. Dark look dropped for Ricks Clips. Toon characters, 3D Paris, 5-second test clip. Render on GPU (about 10x faster). Library in 8 categories. |
| 2026-11-09 | This handoff; library and project sources backed up in git. LuckySticks lightning Short remade as a 9:16 test; storm, mountains, tower, cabin, truck, pond, bear and effects added to the library. |

## Pick up here
Next steps, item 1: look gaps and the missing places, then rebuild the 34-shot opening.
