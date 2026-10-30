# Uploading Shorts to YouTube — the flow

Set by Justin 2026-10-24, after a session uploaded 10 videos to one channel, used the whole day's upload limit
and left the other channel with none. **Read this whole file before uploading anything.**

## Rules (what NOT to do)
- **Never upload a channel's videos in one block.** Uploads are balanced: one video per channel, in turn
  (round robin), every pass. Never 9 videos in one channel while another channel has 0.
- **The daily upload limit is for the whole Google account, not per channel.** All Shorts channels are Brand
  Accounts under justin.masiga.94, so they share one limit. Unverified (as of 2026-10-24) that is about
  **10 uploads a day**. Plan the batch against it before the first upload.
- **"Start posting" means one video public now**, then the rest scheduled one per day (two for LuckySticks, see
  below). Don't schedule the first one for later.
- **LuckySticks posts three a day** (agreed 2026-10-28, applied 2026-10-30 when the monetization work started):
  9:00 AM, 12:00 PM and 6:00 PM. 9:00 AM PHT is 9 PM US Eastern, picked because Studio has no viewer-time data
  yet; the daily analytics run may move any slot once it does. Mix finds and `-luck` people across the slots.
  Every other channel stays at one a day.
- **Never play or watch our own videos** (Justin). Studio's preview is not to be started either.
- **Never upload a video that has `posted.json`** in its folder. That file means it is already on YouTube.
- **Stop at the first "Daily upload limit reached".** No retry, no waiting in a loop. Close the dialog, note what
  is left, tell Justin when the limit resets (24 h after the day's first upload) or that phone verification
  lifts it.
- Phone verification of justin.masiga.94 (Studio → Settings → Channel → Feature eligibility) is Justin's step.
  Until it is done there are also no custom thumbnails (covers can't be set).

## Plan the batch first (before any upload)
1. Ready = video folder has `<slug>.mp4` and no `posted.json`, in every channel with `"pipeline": "shorts"`.
2. Per channel, its next free slot = the slot after its latest `posted.json` `publish_at`; a channel with no
   posted video starts with **one public now**.
3. Order the uploads round robin: channel A video 1, channel B video 1, (channel C ...), then A video 2, B
   video 2, ... oldest MP4 first within a channel. LuckySticks takes two per pass (one find, one `-luck`).
   Stop the list at the day's limit (about 10).
4. Times, Philippines time (GMT+8): 6:00 PM, one per day per channel. LuckySticks: the `-luck` video at
   12:00 PM and the find at 6:00 PM; on a day only one kind is ready, that one goes at 6:00 PM.
5. Tell Justin the list (channel, video, when it goes public) in a few lines before starting.

## Channels
| Folder | YouTube channel | Channel id |
|---|---|---|
| `found-rich` | LuckySticks (@TheLuckySticks) | UCdAwc7fcFUSyyGjRdO6rOxw |
| `what-happens-now` | OldSticksNewSticks (@OldSticksNewSticks) | UCG8zeGkCD4_hrLPIQYkSezQ |
| `chaotic-lives` | TangledSticks (@TangledSticks) | UC2GpVbKcgjWSVoSnCWORdOQ |

New channel = add a row here. Copy, settings and ids are also in `channels/<key>/channel-copy.md`.

## Per video (Claude in Chrome, Studio)
- Switch Studio to the right channel first (avatar → Switch account) and check the left panel says
  "Your channel / <name>". Upload dialog: `studio.youtube.com/channel/<id>/videos/upload?d=ud`.
- MP4s are over the 10 MB limit of the file-upload tool: serve the YtAutomation folder on `127.0.0.1:8790`
  with CORS for `https://studio.youtube.com` plus `Access-Control-Allow-Private-Network: true`, `fetch` the MP4
  in the page, put it in `ytcp-uploads-file-picker input[type=file]` with a `DataTransfer`, fire `change`.
  Studio blocks `eval` (Trusted Types): paste the script into the JS tool each time. Stop the server after.
- Title = `script.json` title. Description = the script's first sentences (up to ~220 characters) + hashtags
  (LuckySticks `#shorts #treasure #luckyfinds`, OldSticksNewSticks `#shorts #history #thenandnow`).
  Set them with `execCommand('insertText')` in `#title-textarea #textbox` / `#description-textarea #textbox`.
- Audience: `tp-yt-paper-radio-button[name=VIDEO_MADE_FOR_KIDS_NOT_MFK]`. Then `#next-button` three times.
- Visibility: the first video of a channel → Public. Others → expand Schedule. The date and time must be typed
  with **real keystrokes** (click `#datepicker-trigger`, triple-click its input, type `Oct 26, 2026`, Enter;
  triple-click the time input, type `6:00 PM`, Enter): JS-set values don't stick. Read both back (normalise
  whitespace, the time has a hidden narrow space) and press Schedule only if they match.
- Video id: from the review step's `youtube.com/shorts/<id>`.
- Right after Studio accepts it, write `posted.json` in the video folder:
  `{"status": "scheduled", "platform": "YouTube Shorts", "channel", "video_id", "url", "studio", "title",
  "publish_at", "uploaded_at"}`. The dashboard then shows it as **Scheduled post** and nothing re-uploads it.
- After the batch: open each channel's Shorts list in Studio and check every video shows Scheduled/Public on
  the right date; then check the dashboard's "Scheduled post" tab.
