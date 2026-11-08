# Tilltown: handoff

**A new session starts here.** Read this file, then `RULES.md`, then `research/README.md` (the research this channel is
built on). Started 2026-11-07. **Claude runs this channel end to end** (Justin, 2026-11-07: "i need you to fully handle
this channel", "if there's a blocker that needs me, work on something else and note it"). Justin does only what needs
his own Google account or his decision; those steps are listed first, below.

## The channel
- **Tilltown**, handle **@Tilltown**, channel ID `UCqZM2RVq6Fo56mV6pFONLZw` (created by Justin 2026-11-07, a Brand
  Account like The Paperback Millionaire). Studio: https://studio.youtube.com/channel/UCqZM2RVq6Fo56mV6pFONLZw
- State 2026-11-07: no picture, no banner, no videos. Standard features enabled; intermediate features (custom
  thumbnails, videos over 15 min) "Eligible", i.e. **not phone-verified yet**.
- **Voice: Mark** (Justin 2026-11-07: "keep mark"), so every upload has **"Altered content: Yes"**. Other voices for
  characters: Justin wants to be asked before any is used.

## How the videos are made: Kaz's plugin (installed 2026-11-08)
Justin's reference for the animation is Grow With Kaz, "I Made VIRAL Animation Videos Using Claude Code"
(https://www.youtube.com/watch?v=3tpaWHaiLQ8, uploaded 2026-11-04): Claude animates every frame in code with his free
plugin. **Use the plugin; do not build a style or a kit from scratch, and do not invent a look** (2026-11-07: a
self-made "cut paper" look and a Crayon/PENNY-style frame were both wrong and are discarded; the old LOOK.md was removed).
- **Plugin:** GrowKaz Stickman Studio v1.1.0. Justin downloaded it (`C:\Users\justi\Downloads\GrowKaz_Stickman.plugin`,
  from the Drive folder linked in the video's description). Every file was read or scanned before install: it only
  serves files to a headless Chromium on localhost, runs ffmpeg, writes inside its own project folders; no outside
  network, no keys, no hooks.
- **Skills** (in `C:\Users\justi\.claude\skills\`): `make-2d-video` (the full pipeline; read its SKILL.md and
  `references/style-bible.md` before any shot), `new-video`, `video-styles`, `render-video`, `video-sound`.
- **Studio:** `D:\AIO Freelance\YtAutomation\growkaz-stickman-studio\` (kept out of git by its own `.gitignore`).
  Its Chromium (build 1194) and Python venv live inside it, on D:. **Always run through `.\studio.cmd <command>`** from
  that folder (cmd on this PC needs the `.\`), e.g. `.\studio.cmd node render.mjs --project projects\<slug> --sheet --scale 0.5`.
- Checked 2026-11-08: `verify_kit.py` 29/29, `doctor.py` all OK, self-test (the example "reaction-time" project) rendered
  14 shots with no errors, looked at.
- The master prompt (`2D Niche Prompt for Claude.pdf`) is 3-4 minute scripts for self-improvement / psychology / what-if /
  science / history niches; our scripts follow `RULES.md`, so it is reference only.
- Next: run the pipeline on the opening of video 1 (`videos/eiffel-tower/`, voice already made: 83.6 s), stage 5 renders
  the shots in the plugin's 5 styles and **Justin picks the style**.

## Waiting on Justin (do these when you're back)
| # | What | Why only you | Blocks |
|---|---|---|---|
| 1 | **Phone-verify** Tilltown: Studio → Settings → Channel → Feature eligibility → "Intermediate features" → verify | Your phone | Custom thumbnails, videos over 15 min |
| 2 | **Character voices**, if the cast speaks: Claude proposes 2-3 voices to pick from | You asked to choose them | Dialogue lines with their own voices (narrator reads them until then) |
| 3 | Watch the first finished MP4 before it goes public | You asked for this on every channel | Video 1 going public |
| 4 | Later, at eligibility: AdSense for YouTube + 2-Step Verification + the Partner Program application | Your accounts | Monetization |
| 5 | Robot checks (`google.com/sorry`) when Gemini hits one | Only you can solve them | Gemini pictures (caricatures, thumbnails) |

Done by Justin: channel created (2026-11-07); narration voice decided (Mark + "Altered content: Yes", 2026-11-07).

A note on ownership: YouTube's rules say a terminated channel can mean losing all of that person's channels. This
channel is kept clean (`RULES.md`: facts, copyright, no repeats), but the risk exists for any channel under the same
owner.

## What Tilltown is
- **Money and business stories, explained simply**: famous fortunes, company rises and falls, scams, crashes and
  bubbles, the money news everyone is talking about. Chosen from 8 niches on this month's YouTube numbers
  (`research/03-niche.md`): proven demand (Crayon Capital, median 292K views), small new channels breaking out (two
  channels under 7K subscribers with 1M+ videos in October), the best-paying viewers.
- **Long videos first** (12-16 min, ~2,300-2,900 words at our voice's ~187 words a minute). **2-4 Shorts per long
  video**, each a complete fact, each linking to its long video (`research/02-long-and-shorts.md`).
- **The look:** animated scenes Claude builds in code (HyperFrames) with a small recurring cast living in **Tilltown**,
  a little town where every money mechanism gets acted out; plus ~20-40 Gemini-drawn caricatures per video for real
  people and big moments; captions of 2-4 words. Not a copy of PENNY's village or Crayon Capital's crayon style.
  To be proven by the side-by-side test (phase 1).
- **Target:** the Partner Program bar for new channels from 2027-02-01: **1,000 subscribers + 8,000 long-video watch
  hours in 12 months** (`research/01-monetization.md`). Apply earlier only if a video breaks out.

## The plan
Each phase: plan → small test → real run; nothing called done without looking at the real output.

**Phase 1: look and production test**
1. Channel files (this file, `RULES.md`, `settings.json`). **Done 2026-11-07.**
2. First topic list, each topic checked on YouTube (`TOPICS.md`).
3. A 60-90 s test section of a real script, fact-checked, with `sources.md`.
4. The same section made two ways: HyperFrames scenes, and Gemini pictures with slow zoom (the Paperback Millionaire
   way). Compared frame by frame, also against Crayon Capital and PENNY frames; Claude time and render time measured.
5. Shown to Justin; then the look is fixed: palette, cast, Tilltown itself, caption style, thumbnail template.
Done means: Justin has seen both versions and the look is decided.

**Phase 2: pipeline**
Script → fact check → voice (Chatterbox) → scenes (Claude writes HyperFrames code per section) → render → captions →
MP4 + 9:16 Shorts. Long renders run in n8n or their own window, never as a background task of a Claude session.
Tested on one short piece before the first full video. The book videos keep first claim on the PC (voice, GPU,
Gemini); Tilltown runs fit around them.
Done means: a full 12-16 min video comes out of the pipeline and passes a frame-by-frame look.

**Phase 3: launch**
Channel art (profile, banner, description) once the channel exists; title + thumbnail written first for each video;
3 scripts written ahead; video 1 + its Shorts; Test & Compare on; Justin watches video 1; then public.
Done means: video 1 and its Shorts are public and the first 72 h read is written down.

**Phase 4: running**
1-2 long videos + 4-8 Shorts a week to start, set by measured capacity in the first two weeks. Daily read, one change
at a time, a format judged after ~10 videos; the stop rule below for videos that are barely shown.

## Bad scenarios and what we do
| Scenario | What we do |
|---|---|
| Videos barely shown (0-4 views in 24 h) | Read impressions, click rate, traffic sources at 24 h and 72 h. Under ~100 impressions: check restrictions, "made for kids", policy notices, whether the exact title shows in YouTube search. Impressions but CTR < 2%: change title/thumbnail at 48-72 h. Never delete or re-upload, never buy views. |
| 5 videos in a row barely shown | Stop before video 6 and diagnose. All 5 under-shown and not in search = the channel is held back: change what may be flagged or start over. Shown but not clicked = redo the packaging style. Clicked but not watched = change topic family. |
| Shorts probe | Shorts from day one: Shorts get shown even on new channels. Shorts get views but long videos don't = the long videos' topics/packaging; nothing gets views = the channel. |
| First 5 videos have no floor | First 5 long videos on well-known, searched subjects (search sends a few viewers to any channel). |
| Rejected as mass-produced | Each video a different story with real facts and its own scenes; never "same situation, same outcome"; opinion labelled as ours; honest titles. |
| Nobody clicks | Title + thumbnail before the script; topic dropped without a strong pair; Test & Compare on every video. |
| Most videos miss | Expected (hit game). Judge after ~10, one change at a time, notes in `LEARNINGS.md`. |
| Gemini limits / flagged accounts / robot checks | Code animation carries the video; Gemini only ~20-40 pictures. |
| Niche gets crowded or fades | Monthly niche scan (`research/tools/nichescan.py`); never repeat a premise. |
| Shorts bring viewers who never watch long videos | Long first; every Short links its long video; drop Shorts if they bring nothing. |
| Low-paying viewers | US-centred money topics. |
| Copyright claims | Only our own drawings/animation; no film or TV clips; music only from YouTube's Audio Library. |
| Legal trouble about real people/companies | Every claim backed by a named source or court record; opinion said as opinion; nothing alleged that isn't on record. |
| Wrong facts | Fact-check pass before voice; every number/date/claim in `sources.md`. |
| A strike reaching other channels | The rules above; any notice reported to Justin the same day. |
| The PC is the only factory | 3 scripts ahead; capacity measured, pace set from it. |
| Sessions lose track | This file and the daily log are kept current; every session starts here. |
| Waiting on Justin | Listed at the top of this file; other work goes on. |
| "This is AI" comments | Comments read daily; change what triggers it if it recurs. |
| Studio page changes break uploads | Every upload checked in Studio; manual fallback with Justin. |
| YouTube changes the rules | Monetization and AI-label pages re-read monthly. |
| Views but no subscribers | Read subscribers per 1,000 views; recurring cast, a thread to the next video. |

## Monitoring
The morning analytics task (`channels/ANALYTICS.md`) gets a Tilltown section once the channel has videos. Read-only,
Claude in Chrome, never plays our videos.
| When | Long videos | Shorts |
|---|---|---|
| 24 h | Impressions, CTR, views, traffic sources | Views, stayed to watch % |
| 72 h | CTR vs our others, % still watching at 30 s, retention drops, subscribers | Stayed %, average % watched, subscribers |
| 7 days, then weekly | Views/day, watch hours, subs per 1,000 views, Test & Compare result, clicks from Shorts | Clicks to the linked long video |
| Daily | Channel totals: subscribers, 12-month watch hours vs the goal line | |
Health checks daily: Studio notifications (claims, policy, limited ads), each new upload searched by exact title,
comments. Triggers and actions: table above. Justin hears only about steps he must do, strikes/claims, and milestones.

**Goal line:** 8,000 h in 12 months = ~22 h/day = ~1,315 min/day ≈ 220-330 long-video views/day at 4-6 min average
watch.

## Where the data lives
```
channels/tilltown/
  HANDOFF.md            this file: state, plan, goal line, decisions
  RULES.md              how a video is written, checked and posted
  TOPICS.md             candidate topics with their YouTube check
  LEARNINGS.md          what worked, what didn't, the change being tested (from the first readings)
  analytics/raw/<date>.json, analytics/<date>.md   the morning read
  videos/<slug>/        script.md, sources.md, title/thumbnail ideas, scenes, posted.json
```
Plus a **Tilltown** tab in the Google Sheet "Shorts - Posts and Analytics" (justin.masiga.94's Drive), filled each
morning, readable on a phone. **GitHub weekly**: analytics, learnings and video records go up in one pull request a
week (LuckySticks' daily files were found mostly uncommitted on 2026-11-07; not repeated here).

**Justin sees it:** the dashboard (http://127.0.0.1:8770 → Tilltown tab and the Analytics page; desktop only), the
sheet (anywhere), these files.

## Open items
1. **Dashboard: long-video analytics + goal line.** The Analytics page only knows Shorts. To add: a long-video table
   (impressions, CTR, average view duration, watch hours) and the progress to 1,000 subs + 8,000 h. **Waiting:** the
   shared folder's `dashboard.py` / `dashboard.html` have another session's uncommitted edits (branch
   `claude/whn-sources`); building on main now would collide with them. Do it after those are committed.
2. **Google Sheet tab "Tilltown"**: add with the first reading.
3. **n8n workflow for the HyperFrames render**: phase 2.

## Decisions
- 2026-11-07 (Justin): Claude makes and fully runs a new channel to monetization, on the research in `research/`;
  blockers go in "Waiting on Justin" and other work continues.
- 2026-11-07 (Claude): niche money & business stories explained simply; long first + Shorts; hybrid production after a
  side-by-side test; name **Tilltown** (@Tilltown free; "Ledger Lane" taken by several money channels, "How It Cashed
  Out" collides with songs and channels named "Cashed Out").

## Daily log
| Date | What happened |
|---|---|
| 2026-11-07 | Research done (`research/`), plan agreed, channel files written, name picked and checked. `TOPICS.md` written (first five: Lustig/Eiffel Tower, John Law, tulip mania, Kodak, Toys"R"Us). Facts for the test section gathered (see "Next step"). Stopped here: usage limit. |

## Next step (pick up here)
Phase 1, step 3: write `videos/eiffel-tower/script-test.md` (cold open + promise + "trick one: look official" with a
Tilltown beat, ~270 words = ~85 s) and its `sources.md`. Facts already checked on 2026-11-07:
- Smithsonian (Jeff Maysh, 2016, citing Secret Service agent James Johnson's memoir), read in Chrome: Lustig in Paris
  May 1925; stationery with the French government seal; the Hôtel de Crillon; wrote to the top scrap-metal dealers;
  reportedly said the tower must come down for "political problems I cannot discuss"; arrested 10 May 1935, escaped
  1 Sep 1935 (bedsheet rope, posed as a window cleaner), recaptured 28 Sep 1935 Pittsburgh; 20 years, Alcatraz from
  April 1936; died 11 March 1947 in Springfield, Missouri (pneumonia); death certificate: "Apprentice salesman".
  https://www.smithsonianmag.com/history/man-who-sold-eiffel-tower-twice-180958370/
- Eiffel Tower operator's page, read in Chrome: the buyer André Poisson; **7,300 tons of iron**; price "an unknown
  sum"; too embarrassed to press charges; Lustig fled to Austria; "some time later" tried again, less luck.
  (It says he died at Alcatraz; the death certificate says Springfield: use Springfield.)
  https://www.toureiffel.paris/en/news/history-and-culture/who-sold-eiffel-tower
- FTC press release June 2026: people reported losing about **$920 million to government impersonators** in 2025
  ($3.5B to all imposter scams). FTC advice page: impostors give an "employee ID number" to sound official, give a
  reason to pay immediately, insist on gift cards/wire/crypto because the money is hard to get back.
  https://www.ftc.gov/news-events/news/press-releases/2026/06/ftc-data-show-people-reported-losing-3-point-5-billion-imposter-scams-2025
  https://consumer.ftc.gov/articles/how-avoid-government-impersonator-scam
- Contested, keep out of the script: the price paid, "a month" vs "six months" before the second attempt, whether the
  other bidders were real dealers or accomplices.
- The three tricks: look official; a reason to act fast and quietly; money the victim can't chase (a bribe = shame =
  no police; today: gift cards, crypto).
Then: voice the section (Chatterbox, Mark until Justin decides; n8n and the dashboard were off on 2026-11-07, no run
going), build the HyperFrames version, then the Gemini version, then compare (phase 1 steps 4-5).

Also found: `channels/book-stories/niche_scan.py` reads "1mo ago" as 1 minute (the "m" alternative comes before "mo").
Fixed in `research/tools/nichescan.py`; the book-stories copy still has it (uncommitted file on another session's
branch, so not touched here).
