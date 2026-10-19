# n8n "YouTube Render" — changes agreed, not done yet

Justin's instruction: note them, don't apply until he says.

1. Window loops: each Gemini window runs on its own (own timers, never waits for the others). Agreed
   2026-10-05. Shared lists in bridge.py written + checked offline; runner.js concurrency + closeWindows and the
   two n8n workflows not written yet. Deploy only when no run is going (needs bridge restart + extension reload).
   Full plan: HANDOFF.md section 5.
2. **DONE 2026-10-09** (Justin: "modify the workflow to include the chatterbox, just on standard and base settings"):
   `voice_cb.py`, n8n voice node, `intro-voice-mark.wav`; see HANDOFF step 2.
   Voice: Chatterbox instead of Kokoro, copying **Mark** (`tts/samples/voices/29_mark.mp3`, 18 s) — "this is what
   we'll be using for the jinthegeek channel" (Justin, 2026-10-09). Chatterbox gives no word timings, so voice.py
   needs Whisper word times for the image cuts inside a sentence; the intro voice line must be redone in Mark too.
   Chatterbox page (`chatterbox/app.py`, :7861) is for trying it out; plan and test before touching n8n.
3. **DONE 2026-10-09** ("no more rules for commas"; HANDOFF story rules updated).
4. **Shorts pipeline for `found-rich`** (agreed 2026-10-18; Justin says "go" before each build step).
   Who does what: **n8n** finds sources, transcribes, renders. **Justin** says when the week's sources are in (no script
   approval since 2026-10-19: running a video's scenes.py approves it). **Claude** only writes the scripts (with segments + one stickman image prompt per segment)
   and uploads the finished videos (YouTube Shorts, TikTok, Reels; one batch a week, confirmed with Justin before posting).
   - Workflow A "Shorts: weekly sources" (new): Monday 06:00 timer + manual start; stops if this week's batch exists.
     `find_shorts.py found-rich` (yt-dlp): Shorts from known format channels (Law By Mike first) + topic searches;
     keep <= 3 min, >= 1M views, on topic, never used before; top 28 by views (fewer = note "only N found", no retry).
     Rows to a Google Sheet (existing n8n Google Sheets login): week, link, title, channel, views, status. Then per
     row: download audio, Whisper, transcript into the row (a failure is marked and skipped). Also writes
     `channels/found-rich/weeks/<date>/sources.json` for Claude. ~30-45 min a week.
   - Claude: pull the finds from the 28 transcripts, check each against a real source (drop unconfirmed), write 14
     scripts, each mixing 3-5 finds from different source videos, in our own words (never the sources' wording),
     /humanize, keep a used-finds list so weeks don't repeat. Saved as `videos/<slug>/script.md` for approval.
   - Workflow B "Shorts Render": copy of YouTube Render; reads `channels/found-rich/videos/`, 1080x1920, no
     intro/outro, stickman style ref instead of the character refs, no thumbnails. ~30-40 images per Short = ~500
     Gemini images a week; measure on the first video.
   - Build order, each checked by looking: 1 find_shorts.py, Justin reviews the list; 2 Workflow A limited to 2
     Shorts, check sheet + transcripts; 3 one full week (28); 4 first scripts for approval; 5 Workflow B, render ONE
     Short and watch it before the rest.
   - **Step 1 done 2026-10-18** (PR #36): `find_sources.py`, settings in `channels/found-rich/sources.json`.
   - **Step 2 done 2026-10-18**: `weekly_sources.py` (finder + yt-dlp + Whisper via ffmpeg samples; 3 failures in a
     row stop it) and n8n "Shorts: weekly sources" (id cCAzjZb6dVHPG6PF, built by `n8n/build_shorts_sources.py`,
     active: Monday 06:00 + POST /webhook/shorts-sources {"channel","want","test"}). Sheet "YtAutomation -
     found-rich sources" (id in sources.json, tab Sources). Tested by hand with want 2 / test: 2 rows in the sheet,
     music-only clips skipped as "no narration". Progress log: `channels/found-rich/weeks/run.log`.
   Story rules: **drop the comma rules** (max one comma, 4+ words each side, no phrase of 3 words or less) once
   Chatterbox voices the videos (Justin, 2026-10-09: "in effect of using chatterbox, we will omit the rules on the
   comma usage"). Chatterbox pauses at every comma (240-560 ms, tested 2026-10-09). Until then Kokoro still voices
   the videos and the rules still matter.

Discussed, not agreed (do not build without asking): full-size image download, Real-ESRGAN upscaler,
segmentation inside n8n, replacing the 5-hour timer with a wait inside the run, slow pan across images
(only segments over 6 s, or every image; OpenCut keyframe export not yet checked).

Done:
- 2026-10-08: Gemini account order: justin.masiga.sub, zaframelanie0524, theoj5442, soypremium050,
  justin.masiga.1994 first (first three open the windows). Story text rules: max one comma per sentence (4+ words
  each side), no phrase of 3 words or less (Kokoro ignores commas; nine voice fixes failed). voice.py: no cut-in
  silence (rejected as glitchy), one recording per sentence.
- 2026-10-07: voice.py speaks whole sentences (timestamped Kokoro places the image cuts); replaces the 10-06
  per-piece split below, which sounded choppy. Opening question first, then the channel intro (intro.json), outro last.
- 2026-10-07: thumbnails: 5 per video (thumb-ideas.json -> thumbnails.py -> thumbnails.json), n8n group
  "3b. Thumbnails" makes them in one separate Gemini window before the images -> thumbs/thumb-N.jpg. First real run
  (why-cats-knead, run 413): 5/5 in 09:57-10:14 (thumbnail 3 needed a second try), then the image steps started.
  Dashboard: thumbnails in each video row + a Thumbnails card (click = full size, download); Delete is a trash icon on
  the right; the robot-check notice has a delete button (hides that run's notice in this browser).
- 2026-10-06: dashboard (dashboard.py / dashboard.html / start_dashboard.cmd, http://127.0.0.1:8770) with Start, Stop
  (also closes the Gemini windows), Hold, Make again, Delete; bridge.py writes usage.jsonl (images per account,
  limit replies, robot checks) and answers GET /status. See HANDOFF section 3.
- 2026-10-05: removed "Skip images?" and the `skip_images` option.
- 2026-10-05: step 8 goes straight to a new chat (no separate refresh).
- 2026-10-05: step 3 checks every 5 s from the start (no 30 s wait).
- 2026-10-05: each window acts on its own random 1-3 s timer for actions that reach Google (open window, prompt,
  switch account, new chat); random 1-3 s pause after steps 2, 4, 6, 7; random 10-30 s pause between rounds.
- 2026-10-05: Google's robot check in any window stops the run at once (no notification).
- 2026-10-06: voice.py splits each segment after every punctuation mark and pauses after each piece (mid-segment
  too): `, ; :` 0.22 s, `. !` 0.45 s, `?` 0.5 s, no mark 0.2 s (old values +0.1). Fixes narration running on past a
  period inside a segment. Split checked on text; audio not yet heard (first 3 segments of the next video).
- 2026-10-05: subtitles: make_srt.py writes output/<video>/<video>.srt next to the MP4, for upload to YouTube.
