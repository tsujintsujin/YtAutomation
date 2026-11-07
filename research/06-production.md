# 6. How to make it efficiently

Researched 2026-11-07. Tags as in `01-monetization.md`. Our own numbers come from `HANDOFF.md`,
`channels/found-rich/MONETIZATION.md` and `channels/book-stories/HANDOFF.md`.

## The short version
- **Pictures are the bottleneck.** Gemini makes ~3.4 pictures a minute and ~180-480 a day across all accounts; a
  long video needs 190-260; two accounts were flagged by Google on 2026-10-21. Every extra video is paid for in
  Gemini quota and account risk.
- **Code-made animation removes that bottleneck.** Claude writes the scenes as code and they render on the PC: no
  quota, no Google accounts, characters identical in every scene, real motion. We already have the tool (HyperFrames,
  which made our intro and outro). It fits money explainers best: charts, counters, maps, timelines, a small cast.
- **Recommended: a hybrid.** Code animation carries the video; Gemini draws only the few things code draws badly
  (caricatures of real people, thumbnails): ~20-40 Gemini pictures per video instead of ~250.
- **Shorts come almost free** with code animation: the same scenes re-laid out at 9:16.
- **Not proven yet:** look quality, render time and Claude time per video. One small test answers all three.

## 6.1 Today's pipeline, in numbers
- Voice: Chatterbox copying "Mark", ~187 words a minute, ~1 h 45 for a 14-minute video (Ep. 1). Local and free.
- Pictures: Gemini web app through Justin's Chrome, ~3.4 a minute while accounts have quota, 180-480 a day (615
  best); a 12-15 min long video is 190-260 pictures; LuckySticks Shorts ~35 each. Two accounts flagged by Google
  (2026-10-21), robot checks now and then (only Justin can clear them).
- MP4: `finish.py`, slow zoom per picture + captions, ~25 minutes.
- Record: 6+ long videos made fine; the system works. Its limit is how many pictures Google allows.

## 6.2 The Claude-animation method (Grow With Kaz, studied 2026-11-07)
**[creator]** Claude writes Three.js (3D drawing) + Remotion (captions, audio, render) code per part of the voice
track; a "style plugin" made from screenshots of reference channels sets the look; ~45 minutes for a 6-minute video
(his number). His result (frames checked): dark green motion graphics, animated charts and counters, flat stick
figures, a simple office set, each line shown (paper flying out of a printer for "arguing with a printer").
Not shown: any view numbers for his own video; one on-screen number disagreed with the narration.
**[report]** Remotion is free for individuals and teams of up to 3, commercial use included; Three.js is free (MIT).
**[mine] We don't need his plugin:** HyperFrames is installed in this workspace with skills for animation (GSAP,
Three.js, Lottie), captions, audio and rendering, and it already made `intro-outro/`.

**What it fixes:**
- No Gemini quota, no account bans, no robot checks for the video itself.
- Consistency by construction: a character is code, so it can't change face or colour between scenes (the problem
  `prompt_kit.py` and the "places" rules fight today).
- Motion instead of a zoom on a still: numbers count up, charts draw, figures walk.
- Charts, maps, timelines and big numbers are exactly what money explainers need, and they come out sharp and right.
- 9:16 Shorts from the same scenes.

**What it risks:**
- **Look:** simple shapes can read as cheap next to Crayon Capital's hand-drawn caricatures. A designed style (our
  own palette, character, texture) is needed, not defaults.
- **Template feel:** if every video uses the same scenes, it looks mass-produced (01, 1.3). Each video needs its own
  scenes and its own tiny world.
- **Time:** Claude session time per video and render time on this PC are unknown.

## 6.3 Local image models (instead of Gemini)
**[report]** On a 6 GB card like the GTX 1660 Ti: SDXL Lightning at 512-768 px or a compressed Flux Schnell, roughly
30 seconds to 4 minutes per picture (2024 user reports, no 1660 Ti benchmark found). 250 pictures = 2-16 hours, on the
same GPU the voice needs. **[mine]** A fallback for a few pictures, not a replacement.

## 6.4 The recommended split [mine]
| Layer | Made by | Per video |
|---|---|---|
| Voice | Chatterbox (as now) | 1 |
| Explainer scenes: charts, numbers, maps, timelines, the tiny world and its cast | HyperFrames (Claude writes the scenes) | most of the video |
| Real people as caricatures, key dramatic moments | Gemini (as now) | ~20-40 |
| Thumbnails | Gemini art + text by code (as `thumbnails.py --final`) | 3 |
| Captions | `finish.py` style (2-4 words, one key word coloured) | |
| Shorts | Same scenes at 9:16 + the Short's own script | 2-4 |

## 6.5 Uploading
**[YouTube developer docs, via report]** Videos uploaded through the YouTube Data API from an unverified project are
locked private, cannot be appealed, and need a compliance audit (YouTube API Services form) before uploads can be
public. Cost of the audit: not found. Today's way (Studio in Chrome, file handed to the page by script) works.
**[mine]** Keep Studio uploads; apply for the API audit only if upload time becomes the bottleneck.

## 6.6 The test that settles it (needs Justin's OK)
One 60-90 second section of a money-explainer script, made two ways: HyperFrames scenes, and Gemini pictures with
zoom. Judge frame by frame side by side, and against Crayon Capital and PENNY frames. Measure Claude time and render
time. Then decide the split in 6.4.

## 6.7 Decisions this part asks for
1. Go hybrid (code animation + few Gemini pictures), subject to the test in 6.6.
2. Design the channel's own look before the first video (palette, mascot/cast, texture), with Justin.
3. Keep Chatterbox; settle the voice question (01, 1.4).

## Sources
- Grow With Kaz, Claude animation: https://www.youtube.com/watch?v=3tpaWHaiLQ8 (transcript + frames, 2026-11-07)
- Remotion license FAQ: https://www.remotion.dev/docs/license/faq and https://github.com/remotion-dev/remotion/blob/main/LICENSE.md
- Low-VRAM image generation: https://eastondev.com/blog/en/posts/ai/20260721-comfyui-low-vram-acceleration/ and https://dev.to/jovan_chan_9500711396d4e6/flux-vs-sdxl-vs-sd-15-real-cost-per-image-across-gpus-2026-44f8
- YouTube Data API upload lock: https://developers.google.com/youtube/v3/docs/videos
- Our pipeline: `HANDOFF.md`, `channels/found-rich/MONETIZATION.md` (R4), `channels/book-stories/HANDOFF.md`
