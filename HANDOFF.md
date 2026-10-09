# YtAutomation — handoff

**Written:** 2026-10-05, end of the session that built the n8n-driven image steps and finished the first full video.
**Owner:** Justin. **Folder:** `D:\AIO Freelance\YtAutomation\` (+ the workflow builder in `D:\AIO Freelance\n8n\`).
**Read this whole file before touching anything.** Then read "How Justin works" again.

---

## 1. What this project is

Faceless, narrated YouTube videos about cats (illustrated style, a recurring "Geek" human character and a
silver tabby cat). One video = a ~12-13 min story read by Chatterbox copying the voice "Mark" over one AI image per segment.

**Justin pays for nothing.** No paid APIs, no billing, no "the paid tier would fix this". Images come from the
free Gemini web app driven through his own Chrome; voice is local Chatterbox (Kokoro before 2026-10-09); editing is a local OpenCut.

### Who does what (Justin set this; do not change it)
1. **Justin** gives a topic.
2. **Claude (in a session)** writes the story (~12 min of narration) and runs it through `/humanize`.
3. **Justin** reviews and approves it. Save it as `output/<slug>/script.md` (opening question first): the dashboard
   lists any folder with a `script.md` and no `script.json` under "Story to approve" (Justin, 2026-10-08).
4. **Claude** builds the setup in `output/<slug>/`: segments, one standalone image prompt per segment,
   character reference sheets in `refs/`, `script.json`, and 5 thumbnail ideas (`thumb-ideas.json` ->
   `python thumbnails.py output/<slug>` -> `thumbnails.json`).
5. **n8n** does everything else unattended: voice -> thumbnails -> images -> resize -> subtitles -> OpenCut -> MP4.
6. **Justin** watches the MP4. Upload goes to the Jin channel (@jinthegeek) in YouTube Studio: title,
   humanized description with chapters, tags, 3 thumbnails in Test & Compare, the .srt as English subtitles,
   playlist "Cat Behavior, Explained". First video done this way 2026-10-07 by Claude in Justin's Chrome; the
   copy and settings are in `JinTheGeek/channel-copy.md`. The MP4 is >10 MB, so Chrome's file_upload tool can't
   take it: serve the folder on 127.0.0.1 (CORS for studio.youtube.com) and set the file input from the page.
   **Which 3 thumbnails** (Justin, 2026-10-07): the ones he ticked on the dashboard's Thumbnails card, saved in
   `output/<slug>/thumbs-approved.json` (list of ids, max 3; the dashboard refuses a 4th). None ticked (or no file) =
   pick 3 of the made `thumbs/thumb-N.jpg` at random. 1 or 2 ticked: ask him, he didn't say.

No AI model inside n8n without asking Justin first. The writing stays with Claude where Justin can review it.

### Rules for the story text (step 2)
**No comma rules** (Justin, 2026-10-09: "no more rules for commas"). The voice is Chatterbox copying Mark
(`voice_cb.py`), which pauses at every comma (240-560 ms, tested 2026-10-09). The old rules (max one comma per
sentence, no phrase of 3 words or less, 2026-10-08) existed only because Kokoro ignores commas; they are gone.

### Rules for the setup (step 4)
- **Segments: 2-4 seconds each, 4 s max** (Justin, 2026-10-05, after watching the first video: 4-6 s per image
  "really is long"). The first video used 3-6 s; do not copy that. Cut per phrase / punctuation; never a
  one-word segment. Shorter segments = more images (~250 for a 13 min video) = more Gemini quota.
- **Every image prompt is fully standalone**: full style + negatives + character descriptions in every prompt,
  never "same as before" / "as above". Gemini sees each prompt in a fresh chat.
- **Prompts are built by `prompt_kit.py`** (this folder), never by hand and never by a per-video copy of the style
  text. Each video's `scenes.py` gives `(geek, cat, place, action)` per segment plus its own `PLACES` and side
  characters; `build_script.py` calls `prompt_kit.build`. Rules (Justin, 2026-10-07, after why-cats-knead came out
  with a different sofa, bedroom, kitchen and blanket in almost every shot, kittens in roadside fields, and the
  style ref's backpack leaking in):
  - **The only things a prompt may point to are the 3 attached images**, always attached in this order: 1 the room
    (`style-ref.jpg`, the Geek's living room), 2 the Geek sheet, 3 the cat sheet. Every prompt says what each of
    the 3 is for in that shot ("not used in this shot" when the Geek or cat is absent). Everything else, every
    place, prop and side character, is described in full inside the prompt. No "same", "again", "the Geek's
    home", no name without its description in that prompt; `prompt_kit.check` fails the build otherwise.
  - **Every scene has a place.** Places are written once, with fixed colours, layout and light, and pasted in
    full every time: the Geek's home (living room = the attached room, kitchen, bedroom, hallway, office) lives in
    `prompt_kit.HOME`; each video adds its own (kitten box, savanna, other people's homes...). A scene with no
    place fails the build. Close-ups use the close-up version of their place (what the subject is on + what shows
    behind). Shots of one moment stay in one place unless the narration moves. Diagrams use `plain`.
  - **Side characters and props are written once** in `scenes.py` (`MOTHER`, `WILDCAT`, `FLEECE`...) and used
    through f-strings, so the mother cat or the blanket can't change colour between shots.
  - **Place test before the full run**: one image per place, checked on a contact sheet, before the rest.
  - **Check by looking**: contact sheets of each batch, comparing each background with the shots beside it.
- Reference sheets live in `output/<slug>/refs/`: `style-ref.jpg` (the room), `geek-sheet.jpg`, `cat-sheet.jpg`
  (all 3 attached to every prompt, in that order). The prompt text format is fixed (see `bridge.py` `prompt_text`):
  `Generate 1 separate images, one for each numbered prompt below. Each prompt is complete on its own.\n\n1. (image NNN) <prompt>`
  The `(image NNN)` tag matters: step 3 uses it to tell a new answer from an old one.
- `script.json` = `{"title", "voice": "am_liam", "segments": [{"id", "text", "geek", "cat", "scene", "prompt"}]}`.
  The cat video's `build_script.py`, `scenes.py`, `seg_rule.py` show how it was produced; reuse the approach,
  but with the 2-4 s rule.
- **Every video OPENS with the question** (Justin, 2026-10-07: "the intro of the whole video should have the
  questions, intro vid, resume main content"). The first seconds of narration are the question itself (2-3 short
  segments), then the intro clip, then the story. Not a question found a minute in: the first biscuits render put the
  intro at 1:08 and that was wrong. why-cats-knead: `opening.py` puts segments 309-311 in front (new ids, so the
  story keeps its ids and images; re-run it after build_script.py). New videos: write the opening into script.md.
- **Channel intro + outro in every video** (Justin, 2026-10-07): the video opens with the story's question, then
  the intro clip with the voice line "We'll talk more about that in this video", then the story goes on; the outro
  plays after the last segment. Write `output/<slug>/intro.json` (NOT in script.json, same reason as thumbnails):
  `{"after_segment": N, "intro": "intro-outro/final/jin-intro.mp4", "intro_voice": "intro-outro/final/intro-voice-mark.wav",
  "intro_voice_text": "We'll talk more about that in this video.", "intro_voice_at": 0.6, "outro": "intro-outro/final/jin-outro.mp4"}`
  where N = the segment that ends the opening question. The voice line is a separate file because other channels
  may use another voice (this channel: Chatterbox copying Mark, `intro-voice-mark.wav`; videos up to purr used Kokoro
  am_liam, `intro-voice-am_liam.wav`). `render-folder.mjs` and `make_srt.py` read it
  (n8n's "Make the video" needs nothing else): narration and images after N move later by the intro's length, one
  soundtrack is built with ffmpeg in `output/<slug>/edit/`. The clips are HyperFrames projects in
  `intro-outro/intro` and `intro-outro/outro` (4 s each, Geek + JIN on the channel orange; `cutout_geek.py` cut the
  Geek out of `JinTheGeek/ProfileImage.jpg`); renders copied to `intro-outro/final/`. Preview them with
  `npx hyperframes preview <dir> --background --port=3010` (never the default 3002: that is the OpenCut controller).
- **Thumbnails: 5 different ideas per video** (Justin, 2026-10-07: "you write 5 different ideas, you have it image
  generated, i choose"). Write `output/<slug>/thumb-ideas.json` = `{"thumbnails": [{"text", "scene"}]}`: `text` is
  a question in capitals that **always starts with "WHY"** (Justin, 2026-10-07: "all thumbnails should be WHY xxxxxx";
  "NOT EVEN THE BATHROOM?" was "far from being good"), short, no apostrophes (Gemini misspells less);
  `thumbnails.py` refuses any other title. `scene` shows the Geek and the cat. Then
  `python thumbnails.py output/<slug>` wraps each in the fixed template (style, Geek, cat, title on the left third,
  same negatives) -> `thumbnails.json`, every prompt standalone. **Not in script.json**: a script.json newer than
  voice.wav makes voice.py redo the voice. Saved by n8n as `thumbs/thumb-1.jpg` ... `thumb-5.jpg`.

---

## 2. Current state (2026-10-05, 18:10)

**First full video is DONE:** `output/why-cats-follow-owners/why-cats-follow-owners.mp4`
- 1920x1080, 30 fps, 13:00 long, voice Kokoro `am_liam` at **speed 0.9**, 181 images, 3-6 s segments.
- `why-cats-follow-owners.srt` next to it (181 subtitles), to upload with the video.
- Justin decided to **leave this video as it is** (0.9 voice, 3-6 s segments). Do not re-render it.
- Made by two n8n runs: run 384 (14:00-14:44, 86 images, then stopped on "image input not found"),
  run 387 (16:32-17:02, last 45 images + voice skip + resize + srt + OpenCut).
- Its images are mixed sizes: 41 at 1376x768 (Gemini's own download button, free accounts), 4 at 2752x1536
  (same button on the Plus account justin.masiga.94: 016, 021, 024, 031), the rest 1024x572 (on-page preview,
  the current method). All get resized to 1920x1080 for the edit.

**Settings now in n8n for the NEXT video:** voice speed **1.0** (Justin moved it back from 0.9 after watching).

**Measured speeds (real numbers from this video):**
- Voice: ~14 min for 181 segments.
- Images: **~3.4 images/min** (a round of 3 every ~53 s) while accounts have quota.
- Resize + subtitles + OpenCut export of a 13 min video: ~11 min (srt 16:51:58 -> MP4 17:02:36).
- One full video without hitting account limits: ~1.5 h. Account limits are the big unknown: how many images
  each account gets per day has NOT been measured yet. In run 384 justin.masiga.94 hit its limit and was
  switched to tsujin.giamas.p.

---

## 3. The pieces and how they talk

```
 n8n (127.0.0.1:5678)  ──HTTP──>  bridge.py (127.0.0.1:8766)  <──long-poll──  Chrome extension "runner" tab
 workflow "YouTube Render"         passes orders, writes img/                  carries out orders in Gemini windows
        │
        ├─ runs voice_cb.py (Chatterbox)   -> audio/NNN.wav, voice.wav, timings.json, voice-settings.json
        ├─ runs voice.py --images-only     -> img_clean/NNN.jpg (1920x1080)
        ├─ runs make_srt.py                -> <slug>.srt
        └─ runs start_opencut.cmd + opencut-controller/scripts/render-folder.mjs + stop_opencut.cmd -> <slug>.mp4
```

| Piece | Where | Notes |
|---|---|---|
| n8n 2.37.10 | npm global; data in `D:\AIO Freelance\n8n\` (`N8N_USER_FOLDER`) | Start: `D:\AIO Freelance\n8n\start_n8n.cmd` in its own window. Owner login was reset 2026-10-05 and re-created by Justin (Claude never types it). |
| Workflow "YouTube Render" | id `ytrender00000001` | Generated by `D:\AIO Freelance\n8n\build_yt_workflow.py` -> `workflows/yt-render.json`. 77 nodes, grouped in 9 labelled boxes. |
| Deploy a workflow change | `python build_yt_workflow.py && python push_yt_workflow.py` (in `D:\AIO Freelance\n8n\`) | Pushes through the n8n API and publishes. **No restart needed**; Justin refreshes the editor to see it. API key: `D:\AIO Freelance\Credentials\n8n\api-key.txt` (listed in `Credentials/README.md`; never copy it anywhere). A running execution keeps the version it started with. |
| bridge.py | `YtAutomation\bridge.py`, port 8766 | Started by n8n's "Start bridge to extension" node via `start_bridge.cmd` (own minimised window "Gemini bridge :8766", `Start-Process`, not cmd `start`). Holds commands for the runner, answers, writes `img/NNN.jpg` (verifies it is a real image), serves `/prompt`, `/refs`, `/missing`, `/accounts`, `/claim`, `/release`. |
| Chrome extension "YtAutomation Gemini Runner" | `YtAutomation\gemini-extension\` (unpacked, MV3) | `background.js` only keeps a pinned **"Gemini runner"** tab open (reopens it if closed, not discardable). `runner.js` in that tab long-polls the bridge and carries out orders. It decides nothing and remembers nothing. **Any change to runner.js needs Justin to reload the extension at chrome://extensions** (Claude's Chrome tools cannot open chrome:// pages). Reloading kills any order in flight, so never reload during a run. |
| Gemini accounts | `YtAutomation\gemini-accounts.json` | `accounts` = first 3 windows, `pool` = 8 signed-in accounts in switch order. Since 2026-10-08 (Justin) the order is justin.masiga.sub, zaframelanie0524, theoj5442, soypremium050, justin.masiga.1994, then justjecery, thejobstash, tsujin.giamas.p; the first three open the windows (thumbnails use the first one not on limit). **justin.masiga.94 is out** (Justin, 2026-10-07): it owns the Jin YouTube channel, and a Google ban for the Gemini automation would take the channel with it. Never add it back. Opened by `?authuser=<email>`, so /u/N order doesn't matter. Justin: "just use whatever is still available/has credits". |
| Dashboard | `YtAutomation\dashboard.py` + `dashboard.html`, http://127.0.0.1:8770 | Built 2026-10-06. Start: `YtAutomation Dashboard.lnk` (pinned to Justin's taskbar; icon `dashboard.ico`) runs `start_dashboard.cmd`: starts whatever is down, each in its own minimised window (n8n via `..\n8n\start_n8n.cmd`, window "n8n :5678", not waited for; the bridge via `start_bridge.cmd`; the dashboard, window "YtAutomation dashboard :8770"), then opens the page in Chrome (the PC's default browser is Edge). Measured cold, 2026-10-07: bridge 9 s, page 12 s, n8n ~3 min until ready. n8n's `/healthz` answers while its database is still loading, so the dashboard's n8n dot and Start use `/healthz/readiness` (dot shows "starting" in between). n8n does not start by itself after a reboot: open the shortcut. The .lnk is not in git: it is `cmd.exe /c "<folder>\start_dashboard.cmd"`, window minimised, icon dashboard.ico. Not started by n8n; restarting it is safe during a run (it only reads and calls the same endpoints Justin would). Shows videos (images made / total, voice, srt, MP4, status), each video's image grid with line + prompt, MP4 player + .srt download, live run (rate, time left, windows, the runner's last orders), images per Gemini account per day, n8n runs with their failure reason. Buttons: Start (webhook), Stop (n8n stop + release claim + runner `setup` closes every Gemini window), Make again (moves img/NNN + img_clean/NNN into img/redo/; only videos without an MP4), Delete (removes the whole `output/<slug>/` permanently, after typing the name; refused during a run). Thumbnails: each video row shows them; the video page has a Thumbnails card (click = full size + Download; checkbox top-right = use on YouTube, max 3, `thumbs-approved.json`, POST `/api/thumbpick`). Delete is the trash icon at the far right of the video page. Every error message (robot-check notice, "Last run failed", "script.json problem", red pop-ups) has a trash button; a deleted notice stays hidden in that browser (localStorage `gone`: `robot:<run>`, `run:<run>`, `script:<slug>:<error>`), a new run's error shows again. Only answers 127.0.0.1/localhost; POSTs need the `X-Dash: 1` header. n8n's plain execution list leaves out running executions, so it also asks with `status=running` / `waiting`. Cache of finished runs: `dashboard-cache/runs.json`. |
| Account counts | `bridge.py` `watch()` -> `usage.jsonl` | The bridge watches the orders passing through it (openWindows / switchAccounts / newChat tell it which account is in which window) and writes one line per image saved, per limit reply and per robot check. Started 2026-10-06 23:2x; earlier videos have no counts. **The window-loop rework changes the orders**: update `watch()` then (the `/pool/limit` call gives limits directly). |
| Kokoro TTS | `YtAutomation\tts\` (venv `tts\.venv`, models `tts\models`) | `voice.py` speaks whole sentences in one call (2026-10-07; the 10-06 one-call-per-comma-piece version sounded choppy, "every pause is a period", and mispronounced short pieces like "sore feet"). Image cuts inside a sentence come from `tts/models/kokoro-v1.0-timestamped.onnx` (onnx-community export of the same Kokoro v1.0: identical audio, checked, plus per-phoneme durations); `kokoro_onnx` only supplies phonemes and voices. Pause 0.45 s after `.`/`!`, 0.5 s after `?`; comma pauses are the model's own. Measured 191 words/min at speed 1.0. Knobs: voice, speed. No pitch/intonation control. |
| OpenCut | `YtAutomation\opencut-classic\` (editor :3000) + `opencut-controller\` (MCP over HTTP :3002) | Started/stopped by the workflow. Use 127.0.0.1, not localhost (IPv6). |

### Windows quirks found (real, don't re-learn them)
- `NoDefaultCurrentDirectoryInExePath=1` on this PC: cmd needs `.\script.cmd`, not `script.cmd`.
- cmd `start` hands inherited handles to the child, which made n8n's Execute Command hang -> windows are launched
  with PowerShell `Start-Process`.
- Use `127.0.0.1`, never `localhost`.

---

## 4. The n8n workflow, start to finish

Groups as they appear in the editor (top to bottom):

1. **Start** — "Start: make a video" (webhook `POST /webhook/yt-render` `{"slug": "...", "voice": "am_liam"}`,
   answers at once). The only trigger: **no timer** (Justin had the "Every 5 hours" timer removed, 2026-10-07;
   it started runs by itself, two at once. Never add a timer back). `pending.py` is no longer used.
   Then: Video name ok? -> Start bridge to extension -> Bridge running? -> "Mark video in progress"
   (`/claim`; a second run on the same video stops at "Stop: already in progress").
2. **Voice** — `chatterbox\.venv\Scripts\python voice_cb.py output\<slug> --if-needed` (since 2026-10-09; was
   Kokoro `voice.py`). Chatterbox Standard, default settings, copying Mark (`tts/samples/voices/29_mark.mp3`), one
   take per sentence; Whisper (small.en, CPU) hears each take: the image cuts go in the word gaps, and a take with
   dropped/repeated words is made again (3 tries, then the step fails naming the segments). Closes the Chatterbox
   page (:7861) first (one model fits on the 6 GB card). ~30-60 min for a 13 min video. Skips only if
   `voice-settings.json` has the same narration text and method (a Kokoro voice is redone).
3. **Images: setup** — Accounts -> "Setup: close leftovers" (closes every other runner tab and every Gemini /
   Gemini image tab) -> "Setup: forget windows and limits" -> 3b -> Images missing -> All images in?
3b. **Thumbnails** — once per run, only if `thumbnails.json` has thumbnails not yet in `thumbs/`. One separate
   Gemini window (first account not on limit) makes them one at a time, the same way as an image: prompt (tag
   `(thumbnail N)`), pause 1-3 s, look every 5 s up to 6 min, open the image tab, pause, save to `thumbs/thumb-N.jpg`,
   close the tab, pause, on limit note the account and switch the window to the next free one, pause, new chat.
   Ends when all are saved, every account is on limit, or 3 tries in a row save nothing and note no limit
   (thumbnails skipped, the video goes on). Robot check stops the run. Then "Thumbs: close window" (runner `setup`)
   and on to Images missing. Accounts noted on limit here stay noted for the image steps. ~5-6 min per video.
4. **Steps 1-2** — decide accounts, open windows (up to 3; accounts not on limit, list order), remember windows;
   decide prompts (one missing image per window), prompt each window; pause 1-3 s.
5. **Step 3** — look in each window every **5 s** (no initial wait) until each shows its "AI generated" image
   or the limit message **under its own prompt** (matched by `(image NNN)`), max 6 min. "Robot check?" ->
   stop the run (Google's `google.com/sorry` page in any window).
6. **Steps 4-8** — open each image's link in a tab, pause, save to `img/NNN.jpg`, close tabs, pause, note
   accounts on limit + switch those windows to the next free account, pause, new chat in every window.
7. **After the 8 steps** — images still missing: pause 10-30 s, next round. "image input not found" at step 2: nothing
   extra, step 8 already reloaded that window, it gets a prompt again next round (Justin, 2026-10-07: refresh, never
   close/reopen windows for this). The runner attaches the 3 refs by dropping them on the input box (Gemini's new
   upload menu has no file input in the page, 2026-10-07). Every account on limit: release the claim, end ("Wait for next try"; Justin starts it
   again). 3 rounds with no image saved and no new limit: fail.
8. **Make the video** — Prepare images (`voice.py --images-only`) -> Make subtitles (`make_srt.py`) ->
   OpenCut assemble + export -> Stop OpenCut -> Release -> MP4 done.
9. **Failed** — Collect failure -> Release -> Mark failed (execution shows red with the reason).

State kept by n8n between steps: workflow static data `wins {account: windowId}`, `onLimit {account: time}`.

The **8 steps** are Justin's own definition (linear, nothing in between that he didn't ask for):
1 open 3 accounts in different windows, 2 prompt each with an image not yet in the folder, 3 check for the
`<img>` whose alt contains "AI generated", 4 open its src in a new tab (no image: do nothing), 5 save it,
6 close the added tabs, 7 note accounts on limit and switch those windows to an account not on limit,
8 new chat in every window.

### Runner commands (what n8n can order; `runner.js`)
`setup`, `listWindows`, `openWindows`, `prompt`, `look`, `openTabs`, `saveImages`, `closeTabs`,
`switchAccounts`, `newChat`. Each works on all its windows at once. Actions that reach Google (open window,
prompt, switch account, new chat) wait a random 1-3 s per window first. `look`/`saveImages` only read the open
page (no traffic to Google).

### Gemini page facts (observed, not guessed)
- Generated image: `<img alt=", AI generated" class="image ... loaded" src="blob:https://gemini.google.com/...">`,
  1024x572. That preview is what gets saved now (Justin: keep 1024, "the most stable").
- "Download full size image" gives 1376x768 on free accounts, 2752x1536 on the Plus account, but it comes from a
  sandboxed `blob:null` frame and Chrome blocked repeat downloads; catching the `lh3.googleusercontent.com/rd-gg/`
  link worked for a while, following a redirect to lh3.google.com broke it. Parked.
- The "Upload & tools" menu is a toggle; Escape does not close it; `input[type=file][accept="image/*"]` only
  exists while it is open. "image input not found" = that input never appeared.
- Limit reply: "I can create more images as soon as your limit resets". Gemini does not keep it after reload.
- Robot check page: `google.com/sorry`. **Only Justin solves it.** It was triggered once by 7 tabs at full speed.

---

## 5. Open items (nothing here is approved unless marked)

- **why-cats-knead (biscuits) — state 2026-10-08.** `why-cats-knead.mp4` (run 444, 11:57) has the opening question
  (segments 309-311), the intro at 0:08, the outro at the end: placement checked in the frames. Its voice is the
  sentence version Justin rejected because commas run together. The text rules (HANDOFF "Rules for the story
  text") are for NEW scripts; existing videos are not remade unless Justin says so. Comma tests:
  `output/why-cats-knead/voice-tests/`.
- **opencut-controller is not in git:** `scripts/render-folder.mjs` (intro/outro placement) exists only on this PC.

- **Window-loop rework — AGREED by Justin, half built, NOT deployed.** Justin's expectation: each window runs
  independently, its own timers, never waiting for the others (today the steps are lockstep: every step waits
  for all 3 windows, so the random timers never put them in different phases, and the slowest window sets the
  pace). Plan:
  - a sub-workflow "Gemini window" started 3 times by the main run (Execute Workflow v1.2, `source: database`,
    `waitForSubWorkflow: false`; trigger = Execute Workflow Trigger `inputSource: passthrough`). Sub-runs are
    mode "integrated" and do NOT count against `N8N_CONCURRENCY_PRODUCTION_LIMIT=2` (checked in n8n source).
  - each loop: take account -> open window -> take image -> prompt -> look every 5 s -> save -> close tab ->
    new chat -> pauses -> next image; on limit: note it, take the next free account, switch its window; ends
    on no images / no accounts / robot check / 3 rounds with nothing saved, closes its window.
  - main run polls every 30 s until all 3 loops ended, then: all images in -> make video; all out of accounts
    -> wait for timer; robot/stuck -> fail.
  - shared lists in the bridge so two loops never take the same image/account: **already written in
    `bridge.py` (`/pool/reset|account|limit|image|result|loop`, `GET /pool/status`) and checked offline**, but
    the running bridge process is older and doesn't have them (restart the bridge when no run is going).
  - **runner.js must run commands concurrently** (start each order without awaiting it, then poll again) and
    gain a `closeWindows` command. NOT written yet (Justin interrupted that edit). Backup of the lockstep runner:
    the current file. Needs an extension reload by Justin.
  - Deploy only when no run is going. Then test on the next video's first rounds.
- **Stale orders:** if the sender of an order gives up (timeout), the bridge still lets the extension carry it
  out later. Fix proposed (drop orders whose sender disconnected), not decided.
- **The 10-30 s pause between rounds** came from Claude's reading of "apply all discussed"; Justin never picked
  that number. Options offered: remove / 3-8 s / keep. Not decided.
- Discussed, NOT agreed (ask before building): full-size image download, Real-ESRGAN upscaler (Justin has a
  GTX 1660 Ti; he is testing an upscaler on `img/043.jpg`), segmentation inside n8n, slow pan across images, background music, title/thumbnail/upload,
  notifications (Justin: "for now no need to notify me").
- Account risk: automating the Gemini web app goes against Google's terms; worst realistic case is limits or
  blocks on an account (Google's terms forbid automated access and allow account termination). justin.masiga.94
  was removed from the rotation 2026-10-07 because it owns the Jin channel; the other accounts carry that risk.
- Git: `YtAutomation` is on github.com/tsujintsujin/YtAutomation (private) since 2026-10-06. `.gitignore` keeps
  media, the venv/models, `usage.jsonl` and the two OpenCut clones out; each video's scripts, prompts, timings,
  refs and .srt are in. **Not backed up:** `opencut-controller/` is a clone of JXUE0/opencut-controller with
  Justin's local changes (`src/index.ts`, `src/tools/export.ts`, `src/tools/project.ts`, `package.json`) and the
  untracked `scripts/render-folder.mjs` + `scripts/_call.mjs` the workflow depends on. The `n8n` folder is not a
  repo either. Ask Justin how he wants those kept.
- Legacy, unused: `gemini_job.py` (old job server), `gen_images.py`, `make_video.py`, `output/_test-steps/`
  (a test folder Claude made without being asked). Clean up only if Justin says.
- `PENDING_CHANGES.md` is the agreed-changes log Justin asked for: note agreed-but-not-done changes there,
  apply only when he says, then move them to "Done".

---

## 6. How Justin works (this matters more than any code)

Learned the hard way in this session; every point cost him hours.

- **Do exactly what he says and only that.** No unrequested additions: no extra timers, waits, retries,
  conditions, window sizes, tests, test folders, "safety" features. If something extra seems needed, say it in
  one line and ask. When he gives an instruction, do it; don't ask again for confirmation.
- **No shortcuts. Ever.** Think the whole behavior through first (every step, every failure, when every loop
  stops), then build.
- **Never guess.** Check the code, the page, the file, the n8n source. Say "I don't know yet" rather than
  inventing a cause.
- **Run things in the real target, not a test copy.** He asked to "run the image prompting part" and a test
  folder was used instead; it re-made images that already existed. Use the real video folder.
- **Long-running work runs in n8n**, never as a background task of a Claude session (it dies with the session).
  Claude may watch with a cheap shell loop; don't burn tokens polling.
- **Any command that takes more than 15 s when it should take seconds is broken: stop it and find out why.**
- **Verify by the real output** (the file in `img/`, the MP4's length/streams), never by "the API said ok".
  Say "built, not checked" until it has run.
- **Logic lives in n8n**, not in the extension. The extension only carries out exact orders and reports back.
- **No paid anything.** No visual inspection of images he didn't ask for (token waste). No opinions he
  didn't ask for, no "you're right" filler. Plain, short answers.
- **Before changing anything, check whether a run is going** (n8n API: `/api/v1/executions?status=running`).
  Never restart the bridge, reload the extension or restart n8n during a run.
- Commands: run them yourself; only UAC prompts and chrome:// pages need Justin.
- He uses the n8n editor to follow along: keep node names readable, keep the grouped layout
  (`GROUPS` in `build_yt_workflow.py`), and every new node must be placed in a group (the builder asserts it).

---

## 7. How to start the next video

1. Justin gives a topic -> write the story (~12 min), `/humanize` it, Justin approves.
2. Make `output/<slug>/` with `script.json` (2-4 s segments, standalone prompts, voice `am_liam`) and `refs/`.
3. Check no run is going, then start it:
   `curl -X POST http://127.0.0.1:5678/webhook/yt-render -H "Content-Type: application/json" -d '{"slug":"<slug>","voice":"am_liam"}'`
   (or the dashboard's Start button).
4. Follow it in the bridge window or n8n -> Executions. The MP4 and .srt land in `output/<slug>/`.
