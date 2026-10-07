# n8n "YouTube Render" — changes agreed, not done yet

Justin's instruction: note them, don't apply until he says.

1. Window loops: each Gemini window runs on its own (own timers, never waits for the others). Agreed
   2026-10-05. Shared lists in bridge.py written + checked offline; runner.js concurrency + closeWindows and the
   two n8n workflows not written yet. Deploy only when no run is going (needs bridge restart + extension reload).
   Full plan: HANDOFF.md section 5.

Discussed, not agreed (do not build without asking): full-size image download, Real-ESRGAN upscaler,
segmentation inside n8n, replacing the 5-hour timer with a wait inside the run, slow pan across images
(only segments over 6 s, or every image; OpenCut keyframe export not yet checked).

Done:
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
