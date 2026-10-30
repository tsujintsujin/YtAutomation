# LuckySticks: get monetized before 2027-02-01: plan and handoff

Agreed by Justin 2026-10-28 ("record and apply this plan... you will handle the research and development of
this channel"). Development starts in a later session. **Read this whole file, then `RULES.md`,
`LEARNINGS.md`, `channels/SHORTS_RULES.md` and `channels/UPLOADING.md` before doing anything.**
HANDOFF.md section 6 (how Justin works) still applies: plan, tell him in a few lines, get his OK, test small.

Claude owns the research and development of this channel: what to make, the formats, the weekly read of the
numbers, and proposing changes. Justin still approves topics/scripts the way the pipeline already works and
does the steps only he can do (marked **Justin** below).

---

## 1. The goal and the deadline

**Get LuckySticks (@TheLuckySticks, `UCdAwc7fcFUSyyGjRdO6rOxw`) accepted into the YouTube Partner Program
(ad revenue) before 2027-02-01.**

From 2027-02-01 the bar for NEW applicants doubles (YouTube blog, announced 2026-08-10):

| | Today | New applicants from 2027-02-01 |
|---|---|---|
| Full YPP (ads) | 1,000 subs + 4,000 long-video watch hours (12 months) **or** 10M Shorts views (90 days) | 8,000 watch hours **or** 20M Shorts views |
| Lower tier (fan funding, no ads) | 500 subs + 3 uploads + 3,000 watch hours or 3M Shorts views | unchanged |

**Checked 2026-10-29 (R1, section 5): the channel must be ACCEPTED, not just applied, before 2027-02-01.**
The blog says only "This update won't impact creators already in YPP"; nothing protects a pending application.
Review is "typically in about 1 month". So the real target is **eligible and applied by 2026-12-31**
(about 63 days from 2026-10-29), not mid-January.

Also needed for YPP: 2-Step Verification on justin.masiga.94, an AdSense account linked, no Community
Guidelines strikes (**Justin**: AdSense and 2SV are his steps).

## 2. Why this route (the numbers, 2026-10-28)

Data: `analytics/2026-10-26.md`, `analytics/2026-10-28.md` (Studio readings).

- A Short gets **~800-900 views in its first 1-2 days, then ~30-40 a day** (painting +58 in 2 days, egg +82 in
  2 days). Only 2 Shorts measured over 2 days: re-check this every week.
- Subscribers: 9 from ~3,700 views, **~1 per 400 views**.
- Projection (launch 800 + 30/day tail per Short, tail assumed not to decay, so this is the high side):

| Pace | Views in 90 days | 1,000 subs reached |
|---|---|---|
| 1 Short/day | ~190K | ~5 months |
| 2 Shorts/day (today's rule) | ~385K | ~day 92, about 2027-01-28: too late |
| 3 Shorts/day | ~576K | ~day 72, about **2027-01-08** |

Math: views by day N at k Shorts/day = k × (800·N + 15·N·(N−1)). Subs = views / 400.

- **10M Shorts views in 90 days is out of reach** (576K at 3/day, 17x short) unless several Shorts break out.
  Shorts views never count toward watch hours.
- So the route is **1,000 subscribers (from Shorts) + 4,000 hours on long videos.**
  4,000 h by mid-January = ~47 watch hours/day = 2,800 min/day; at a 3-minute average watch that is
  **~900 long-video views a day**. This is a target, not a projection: there is no long-video data yet.

## 3. The plan

1. **Long videos on LuckySticks, 8-12 min, 1-2 a week.** Each tells 6-10 finds or luck stories in more depth.
   A new script every time: never Shorts glued together (see the policy risk in section 4). Same look, same
   voice, same "every fact real and checked, sources.md" rule as the Shorts. Keep under 15 min until phone
   verification is done (unverified accounts can't upload longer).
2. **Every Short links to the newest long video** with Studio's "Related video" field, so Shorts viewers turn
   into watch hours.
3. **LuckySticks goes to 3 Shorts a day**, 30-50 s each (RULES.md length rule). Fits the shared ~10 uploads/day
   limit: 3 here + 1 each on the other channels. The third slot's time is decided in step R3 below.
4. **Every day** (Justin 2026-10-29: "monitor daily, improve daily"; `channels/ANALYTICS.md` "LuckySticks: learn
   and improve EVERY day"): the 09:00 analytics run rewrites LEARNINGS.md, applies one change, and logs the goal
   line in section 8. The read covers the long videos too (views/day, average watch,
   watch hours to date vs the 47 h/day line, subs to date vs the 3-a-day line). **Stop rule:** if the first two
   long videos are each under ~300 views/day after a week, don't keep posting the same thing: change one thing
   (topic, title, length, opening) and tell Justin.
5. **Apply the day the channel is eligible** (**Justin**: the application and AdSense are his).

## 4. Risks (say these to Justin, don't hide them)

- **The long-video numbers are a guess.** Shorts-to-long-video links usually move only ~1-3% of viewers; at
  ~10K Shorts views/day that is ~100-300 views. The rest must come from search and suggested. If long videos
  don't take off, the deadline is missed.
- **YPP review is by hand, and the "inauthentic content" policy targets mass-produced, repetitive AI channels**
  (AI voice, one look, many uploads a day). What gets us accepted: checked facts, a new script in every video,
  variety of stories, long videos that are their own work, not reused Shorts. Never reupload or loop content.
- The tail of 30-40 views/day per Short is from 2 Shorts over 2 days. If it decays, subscribers arrive later
  than the table says; then 3/day is the floor, not a comfortable margin.

## 5. Research to do first (next session, before building anything)

- **R1. Confirm the rules** on YouTube's Help Center (YPP overview + eligibility) and the 2026-08-10 blog post:
  thresholds, accepted-vs-eligible by 2027-02-01, subscriber count, whether Shorts→long "Related video" works
  on this channel now.
- **R2. Long-video format.** Find 5-10 faceless long videos in this niche ("people who found fortunes",
  "luckiest people", 8-15 min) with high views on small channels. Study shape only (hook, number of stories,
  order, length, title/thumbnail style), never their words: same rule as `research.md`. Write the long-video
  template into `RULES.md`.
- **R3. Third Short slot.** Pick the time from Studio's "When your viewers are on YouTube" (Analytics →
  Audience) once it has data; until then propose one to Justin, don't guess silently.
- **R4. Pipeline check.** Confirm what the n8n "YouTube Render" workflow needs for an 8-12 min 16:9 video in
  the stick-figure look (image size/aspect, number of scenes, voice length, render time). Verify by reading the
  workflow and a test render Justin OKs, not by assuming it works because the cat videos did.

## 6. Development, in order (each step: plan → Justin's OK → small test → real run)

1. R1-R4 above; write findings into this file.
2. Long-video template in `RULES.md`; first long-video story list from `used-sources.json`-unused finds and
   luck stories (never reuse a Short's exact script).
3. First long video: script → Justin approves → render → check the real MP4 by looking → upload (UPLOADING.md
   flow; long videos are not Shorts, so no #shorts tag and a real thumbnail once phone verification allows).
4. Add the Related-video link to every public/scheduled LuckySticks Short.
5. Switch LuckySticks to 3 Shorts a day in `channels/UPLOADING.md` (pending: section 7).
6. Weekly read every Monday (step 4 of the plan) until eligible; update section 8 below.

## 5b. Research results (2026-10-29)

**R1. Rules (YouTube's own pages: blog post above, Help `answer/72851`, monetization policies `answer/1311392`).**
- Full YPP today: 1,000 subs + 4,000 qualified watch hours (12 months) or 10M qualified Shorts views (90 days).
- From 2027-02-01 new applicants need 8,000 h or 20M views; the subscriber number isn't restated. Members
  already in YPP are not affected. Accepted before 2027-02-01 is what counts (section 1).
- To apply: 2-Step Verification on, one AdSense for YouTube account linked, no strikes, "advanced features
  access". Review "typically in about 1 month". Rejected: appeal within 21 days or re-apply after 30 days.
  Channel age and phone verification are not listed as YPP requirements.
- Inauthentic content (renamed from "repetitious"): not allowed are "image slideshows, templated storylines ...
  with minimal or no narrative", and "AI-generated content made with generic or unoriginal templates giving the
  impression of mass production". Allowed: AI used to visualize your own narrative. Reviewers look at the main
  theme, most viewed, newest videos and metadata, for the channel as a whole. So: every video a real story told
  in our words, checked facts, no copy-paste structure, no reused Shorts as long videos.

**R2. Long-video format: proven in exactly our look.**
- **Simple Paint** (@SimplePaintOfficial): MS-Paint-style stick figures + narration, long videos only, started
  about a year ago, 541K subs, 136 videos. Its FIRST videos already did 142K-6M views ("The Most AVOIDABLE Cave
  Deaths Ever" 6M, "Luckiest Cave Divers Who Survived The Impossible" 2.1M). Now 13-18 min, 1 every 3-4 days,
  recent ones 12K-3M. Also 1-hour "Marathon" compilations (850K).
- **The Paint Explainer** (2.01M subs): "The Luckiest People Who Survived The Impossible", 8:09, 6.1M views.
- **Shape of these videos** (from their chapter lists): **no intro**: the first person starts at 0:00; **7-12
  people, about 60-70 s each**, one chapter per person (name as chapter title); title = "The Most/Luckiest
  <superlative> <who>". Simple Paint's luck video: 12 people in 13:35 (Joan Murray, Bugorski, Yamaguchi...).
- Older list channels (TheRichest, Top Trending) did 1-4M on "thrift store finds that made people rich" 7-8 years
  ago; few recent long videos on finds, so the luck angle is the proven one right now.
- What it means for watch hours: 4,000 h = 240,000 min. At ~4 min average watch on a 10-13 min video that is
  **~60,000 long-video views in total**. One modest hit does it; Simple Paint's first uploads all passed that.

**R3. Studio, LuckySticks Audience tab (read 2026-10-29).**
- "When your viewers are on YouTube": *not enough viewer data*. Third/fourth slot times can't be picked from
  data yet; propose times to Justin.
- Viewers: 99.8% new, 0.0% watch time from subscribers. 25-44 years old 90%, 60% female. Phone 77%.
- **Top country Philippines 48.8%** (South Africa 2.7%, Sweden 1.1%, US 0.8%). Doesn't block YPP, but PH ads pay
  far less than US ones; English titles about US/UK finds should pull more US viewers over time. Watch it.
- **"Related video" is available on our Shorts now** (seen on `wBlNzsabjoU`'s edit page, currently "None").

**R4. Pipeline.**
- The long-video n8n workflow ("YouTube Render", `n8n/build_yt_workflow.py` without `--shorts`) already makes
  1920x1080 videos; folder `output/<slug>/`, with intro.json/thumbnails.json steps (skip themselves if absent).
  The long cat videos were 11-13 min with **181-312 images** (one per ~2.5 s).
- Image capacity (bridge `usage.jsonl`): **~180-480 images on a normal run day** (615 best), with 3-8 accounts.
  A LuckySticks Short is ~35 images. 4 Shorts a day = ~140; the other two channels ~70; a 12-min long video at
  one image per ~5 s = ~150, i.e. ~40/day at 2 a week. Total ~250/day: **at the limit**. So long videos use one
  image per ~5 s (paint channels hold one drawing for several seconds), not 2.5 s.
- Not checked yet: a test render of a long stick-figure video (needs Justin's OK; section 6 step 3).

**Revised numbers for the 2026-12-31 target** (63 days, Short = 800 at launch + 30/day, 1 sub per 400 views):

| LuckySticks Shorts/day | Subs by 2026-12-31 (Shorts only) |
|---|---|
| 2 | ~555 |
| 3 | ~830 |
| **4** | **~1,100** |

Watch hours: first long video ~2026-11-08 leaves ~53 days → ~75 h/day, or ~60,000 long-video views in total.
**Proposal: 4 Shorts a day + one long video a week (two if images allow).** Long videos also bring subscribers.

**Proposed first long video (waiting for Justin's OK):** the 13 luck stories already researched for Shorts
(`*-luck` folders, every one has `sources.md`: Yamaguchi, Vulović, Koepcke, Jessop, Okene, Oliver, Sullivan,
Gage, Hodges, Packard, Alvarenga, Adams, Morgan). 10-12 of them, a NEW ~60-70 s script each (more detail than
the Short, our own words), no intro, one chapter per person, ~12 min. Each luck Short then links to it with
"Related video". Simple Paint and The Paint Explainer cover Yamaguchi/Murray-type stories too: tell ours with
our own facts, angle and wording (RULES.md).

## 7. What is applied vs pending (2026-10-28)

- Applied: this file; pointers in HANDOFF.md section 5, `channels/UPLOADING.md`, `RULES.md`.
- Applied 2026-10-30: 3 Shorts/day in UPLOADING.md; the daily run now owns growth changes (ANALYTICS.md).
- Pending: long-video template, Related-video links (once a long video is public), first long video.

## 8. Progress log (one line per week)

| Date | Subs | Long-video watch hours | Shorts views (90 d) | Note |
|---|---|---|---|---|
| 2026-10-28 | 10 | 0 | ~3,770 | Plan agreed. 5 Shorts public, 2/day. |
| 2026-10-30 | 10 | 0 | 6,017 | 6 Shorts public, no long video yet. Behind the line: 1,000 subs by 2026-12-31 needs ~16 a day, we have 10 total. |

## Sources

- YouTube Blog, YPP changes for 2027: https://blog.youtube/news-and-events/youtube-partner-program-updates-2027-new-opportunities-earn/
- YouTube Blog, qualified watch hours and Shorts views: https://blog.youtube/news-and-events/youtube-monetization-qualified-watch-hours-shorts-views/
- Relevant Audience, thresholds double Feb 2027: https://www.relevantaudience.com/youtube/youtube-partner-program-thresholds-double-february-2027/
- AIR, YPP requirements 2026: https://air.io/en/monetization/youtube-partner-program-requirements-2026-the-complete-guide
- Metricool, YouTube AI content rules: https://metricool.com/youtube-ai-content-rules-monetization/
