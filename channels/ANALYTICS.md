# Shorts analytics — the daily Studio read

Set by Justin 2026-10-25: "a routine to monitor the short performances so you can improve the creation of the
shorts, document the analytics per day in a file". Read from YouTube Studio in Claude in Chrome (no API: Justin
dropped it the same day). A scheduled Claude task runs this every morning; it can also be run by hand.

## What it writes (per channel)
- `channels/<key>/analytics/raw/<YYYY-MM-DD>.json`: the numbers as read from Studio (format below).
- `channels/<key>/analytics/<YYYY-MM-DD>.md`: made from the raw file by `python analytics_report.py <key> <date>`
  (run in `YtAutomation\`): one row per public Short with the change since the last reading.
- On **Mondays** also `channels/<key>/LEARNINGS.md` (see "Weekly learnings").

## Rules
- **Read only.** Never change anything in Studio, never press Download/Export, never play or open the video itself
  (Justin: never watch our own videos; the analytics pages don't play it).
- Never make a number up. A number Studio doesn't show is `null`, and why goes in `note`.
- One reading per channel per day. A raw file for today already there = that channel is done, skip it.
- Never edit scripts, RULES.md or SHORTS_RULES.md from this task. Findings go in LEARNINGS.md; a rule change is
  proposed in `PENDING_CHANGES.md` for Justin.

## Channels
Same table as `UPLOADING.md` (found-rich = LuckySticks `UCdAwc7fcFUSyyGjRdO6rOxw`, what-happens-now =
OldSticksNewSticks `UCG8zeGkCD4_hrLPIQYkSezQ`). A new channel there = read here too.

## Steps (per channel)
1. **Switch channel:** `https://www.youtube.com/channel_switcher`, click the channel. Studio refuses another
   channel's pages ("you don't have permission") until this is done. Right after switching it can still say
   that once: load the page again.
2. **Public Shorts:** `https://studio.youtube.com/channel/<id>/videos/short`, page text. Keep the rows whose
   visibility is **Public**: title, length (e.g. 1:29), date. Match each to its folder by `video_id` in
   `videos/*/posted.json` (that's the `slug`; a Short with no posted.json gets `slug: null`).
3. **Full table** (Studio's own numbers, complete to about 2 days ago). Open, wait ~10 s:
   ```
   https://studio.youtube.com/channel/<id>/analytics/tab-overview/period-default/explore?entity_type=CHANNEL&entity_id=<id>&time_period=lifetime&explore_type=TABLE_AND_CHART&metric=EXTERNAL_VIEWS&granularity=DAY&t_metrics=EXTERNAL_VIEWS&t_metrics=ENGAGED_VIEWS&t_metrics=SHORTS_FEED_IMPRESSIONS_VTR&t_metrics=AVERAGE_WATCH_TIME&t_metrics=AVERAGE_WATCH_PERCENTAGE&t_metrics=RATINGS_LIKES&t_metrics=COMMENTS&t_metrics=SHARINGS&t_metrics=SUBSCRIBERS_NET_CHANGE&dimension=VIDEO&o_column=EXTERNAL_VIEWS&o_direction=ANALYTICS_ORDER_DIRECTION_DESC
   ```
   It opens as Advanced mode (an overlay: `get_page_text` reads the page under it, so read the table with
   `read_page`/`find` or a screenshot). The date under Controls ("Oct 23, 2026 / Lifetime") is
   `table_complete_to`. Columns: Views, Engaged views, Stayed to watch, Average view duration, Average percentage
   viewed, Likes, Comments added, Shares, Subscribers. Every public Short with a row here: `source: "table"`.
4. **Live pages** for each public Short the table doesn't have yet (published after `table_complete_to`):
   - `https://studio.youtube.com/video/<video_id>/analytics/tab-overview/period-default`: Views, Subscribers,
     Top traffic sources.
   - Then click the **Engagement** tab (its address is `tab-interest_viewers`; typing other tab names gives a blank
     page): Engaged views, Watch time, Average view duration, "How viewers engaged" Stayed to watch %.
   - Likes, comments, shares, average % are not on these pages: `null`. `source: "live"`.
   - Audience retention, once processed, says something useful (key moments): put it in `note`.
5. **Raw file** `channels/<key>/analytics/raw/<date>.json` (date = today, Philippines time):
   ```json
   {"channel": "found-rich", "channel_name": "LuckySticks", "date": "2026-10-25",
    "read_at": "2026-10-25 09:05 PHT", "table_complete_to": "2026-10-23",
    "shorts": [{"video_id": "bccF3ZLa2hY", "slug": "nail-sandwich-nugget-declaration",
                "title": "A $4 painting was hiding $8 million", "published": "2026-10-24", "length_s": 89,
                "source": "live", "views": 734, "engaged_views": 233, "stayed_pct": 30.2,
                "avg_view_duration_s": 47, "avg_pct_viewed": null, "likes": null, "comments": 0,
                "shares": null, "subs_net": 4, "watch_hours": 3.3,
                "traffic": {"Shorts feed": 97.0, "YouTube search": 2.7}, "note": null}]}
   ```
   `comments` can always come from the Shorts list (step 2). Percentages as numbers (30.2, not "30.2%").
   Subscribers shown as "—" = 0. `read_at` is the real clock time (`date "+%Y-%m-%d %H:%M"`: the PC runs on UTC+8; `TZ=Asia/Manila` in Git Bash wrongly gives GMT), never estimated.
6. `python analytics_report.py <key> <date>`, then open the `.md` it wrote and check it against what Studio showed.

## Weekly learnings (Mondays, after the daily read)
Read the channel's last 7 daily files plus each Short's `script.md`, and rewrite `channels/<key>/LEARNINGS.md`:
- What the best and worst Shorts did differently (hook, title promise, length, order of items, ending), with the
  numbers that show it: stayed to watch %, average % viewed, subscribers, comments.
- Only what the numbers support; a Short under ~200 views is too early to judge, say so.
- At most 5 points, each one a concrete thing to do in the next scripts.
- If a point means changing a rule, add it to `PENDING_CHANGES.md` for Justin. Never change the rules here.

Writing a new script for a channel: read its `LEARNINGS.md` first (SHORTS_RULES.md says so).
