# YtAutomation — handoff

**Written:** 2026-10-05, end of the session that built the n8n-driven image steps and finished the first full video.
**Owner:** Justin. **Folder:** `D:\AIO Freelance\YtAutomation\` (+ the workflow builder in `D:\AIO Freelance\n8n\`).
**Read this whole file before touching anything.** Then read "How Justin works" again.

---

## 1. What this project is

Faceless, narrated YouTube videos about cats (illustrated style, a recurring "Geek" human character and a
silver tabby cat). One video = a ~12-13 min story read by a Kokoro voice over one AI image per segment.

**Justin pays for nothing.** No paid APIs, no billing, no "the paid tier would fix this". Images come from the
free Gemini web app driven through his own Chrome; voice is local Kokoro; editing is a local OpenCut.

### Who does what (Justin set this; do not change it)
1. **Justin** gives a topic.
2. **Claude (in a session)** writes the story (~12 min of narration) and runs it through `/humanize`.
3. **Justin** reviews and approves it.
4. **Claude** builds the setup in `output/<slug>/`: segments, one standalone image prompt per segment,
   character reference sheets in `refs/`, and `script.json`.
5. **n8n** does everything else unattended: voice -> images -> resize -> subtitles -> OpenCut -> MP4.
6. **Justin** watches the MP4 and uploads it by hand (title/description/thumbnail/upload are not built).

No AI model inside n8n without asking Justin first. The writing stays with Claude where Justin can review it.

### Rules for the setup (step 4)
- **Segments: 2-4 seconds each, 4 s max** (Justin, 2026-10-05, after watching the first video: 4-6 s per image
  "really is long"). The first video used 3-6 s; do not copy that. Cut per phrase / punctuation; never a
  one-word segment. Shorter segments = more images (~250 for a 13 min video) = more Gemini quota.
- **Every image prompt is fully standalone**: full style + negatives + character descriptions in every prompt,
  never "same as before" / "as above". Gemini sees each prompt in a fresh chat.
- Reference sheets live in `output/<slug>/refs/`: `style-ref.jpg`, `geek-sheet.jpg`, `cat-sheet.jpg`
  (attached to every prompt). The prompt text format is fixed (see `bridge.py` `prompt_text`):
  `Generate 1 separate images, one for each numbered prompt below. Each prompt is complete on its own.\n\n1. (image NNN) <prompt>`
  The `(image NNN)` tag matters: step 3 uses it to tell a new answer from an old one.
- `script.json` = `{"title", "voice": "am_liam", "segments": [{"id", "text", "geek", "cat", "scene", "prompt"}]}`.
  The cat video's `build_script.py`, `scenes.py`, `seg_rule.py` show how it was produced; reuse the approach,
  but with the 2-4 s rule.

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
        ├─ runs voice.py (Kokoro)          -> audio/NNN.wav, voice.wav, timings.json, voice-settings.json
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
| Gemini accounts | `YtAutomation\gemini-accounts.json` | `accounts` = first 3 windows (justin.masiga.94 [Plus, Justin's main], justjecery, thejobstash), `pool` = all 9 signed-in accounts in switch order. Opened by `?authuser=<email>`, so /u/N order doesn't matter. Justin: "just use whatever is still available/has credits". |
| Kokoro TTS | `YtAutomation\tts\` (venv `tts\.venv`, models `tts\models`) | `voice.py` uses `kokoro_onnx`; only knobs: voice, speed, pauses. No pitch/intonation control (punctuation and voice blending are the only levers). |
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
   answers at once) or "Every 5 hours" -> "Find unfinished video" (`pending.py`: oldest `output/<slug>/` with
   script.json, no MP4, no `HOLD` file, not starting with `_`) -> "Pick that video".
   Then: Video name ok? -> Start bridge to extension -> Bridge running? -> "Mark video in progress"
   (`/claim`; a second run on the same video stops at "Stop: already in progress").
2. **Voice** — `voice.py output\<slug> --voice <v> --speed 1.0 --if-needed`. Skips only if voice.wav +
   timings.json are newer than script.json AND `voice-settings.json` has the same voice and speed.
3. **Images: setup** — Accounts -> "Setup: close leftovers" (closes every other runner tab and every Gemini /
   Gemini image tab) -> "Setup: forget windows and limits" -> Images missing -> All images in?
4. **Steps 1-2** — decide accounts, open windows (up to 3; accounts not on limit, list order), remember windows;
   decide prompts (one missing image per window), prompt each window; pause 1-3 s.
5. **Step 3** — look in each window every **5 s** (no initial wait) until each shows its "AI generated" image
   or the limit message **under its own prompt** (matched by `(image NNN)`), max 6 min. "Robot check?" ->
   stop the run (Google's `google.com/sorry` page in any window).
6. **Steps 4-8** — open each image's link in a tab, pause, save to `img/NNN.jpg`, close tabs, pause, note
   accounts on limit + switch those windows to the next free account, pause, new chat in every window.
7. **After the 8 steps** — images still missing: pause 10-30 s, next round. "image input not found" at step 2:
   **Restart windows** (close all, forget them, back to step 1; accounts on limit stay noted), up to 3 times in a
   row, then fail. Every account on limit: release the claim, end ("Wait for next try"; the 5-hour timer picks
   it up again). 3 rounds with no image saved and no new limit: fail.
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
  GTX 1660 Ti; he is testing an upscaler on `img/043.jpg`), segmentation inside n8n, replacing the 5-hour timer
  with a wait inside the run, slow pan across images, background music, title/thumbnail/upload,
  notifications (Justin: "for now no need to notify me").
- Account risk: automating the Gemini web app goes against Google's terms; worst realistic case is limits or
  blocks on an account. justin.masiga.94 (his main, Plus) is in the first 3 windows; Justin said keep using
  whatever has credits.
- No git: neither `YtAutomation` nor `n8n` is a git repo -> no backup. Workspace rule wants a private repo on
  github.com/tsujintsujin; ask Justin once before creating/pushing (audit for secrets first).
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
   (or let the 5-hour timer find it; add a `HOLD` file to keep a folder from being picked up).
4. Follow it in the bridge window or n8n -> Executions. The MP4 and .srt land in `output/<slug>/`.
