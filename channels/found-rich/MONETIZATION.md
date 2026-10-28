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

Not yet confirmed (check first, section 5): whether the channel has to be **accepted** by 2027-02-01 or only
**eligible/applied**; the subscriber count under the new rules. YouTube's review can take weeks, so the
working target is **eligible by mid-January 2027**.

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
4. **Every Monday**, the LEARNINGS.md weekly read also covers the long videos (views/day, average watch,
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

## 7. What is applied vs pending (2026-10-28)

- Applied: this file; pointers in HANDOFF.md section 5, `channels/UPLOADING.md`, `RULES.md`.
- **Pending (do not apply until development starts):** 3 Shorts/day in UPLOADING.md (still 2), long-video
  template, Related-video links, first long video.

## 8. Progress log (one line per week)

| Date | Subs | Long-video watch hours | Shorts views (90 d) | Note |
|---|---|---|---|---|
| 2026-10-28 | 10 | 0 | ~3,770 | Plan agreed. 5 Shorts public, 2/day. |

## Sources

- YouTube Blog, YPP changes for 2027: https://blog.youtube/news-and-events/youtube-partner-program-updates-2027-new-opportunities-earn/
- YouTube Blog, qualified watch hours and Shorts views: https://blog.youtube/news-and-events/youtube-monetization-qualified-watch-hours-shorts-views/
- Relevant Audience, thresholds double Feb 2027: https://www.relevantaudience.com/youtube/youtube-partner-program-thresholds-double-february-2027/
- AIR, YPP requirements 2026: https://air.io/en/monetization/youtube-partner-program-requirements-2026-the-complete-guide
- Metricool, YouTube AI content rules: https://metricool.com/youtube-ai-content-rules-monetization/
