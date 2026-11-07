# Research: a YouTube channel with long videos and Shorts that gets monetized

Asked by Justin 2026-11-07: how to make and run a YouTube channel efficiently and get it monetized: what content,
how to make it, script and structure included, for one channel with both long videos and Shorts. Researched the same
day by Claude. Nothing in the channels was changed by this research; everything below is a proposal.

**How to read it:** this page is the summary and the decisions. Each part has its own file with the evidence.
Tags in every file: **[YouTube]** YouTube's own pages or data; **[report]** press or third-party study;
**[creator]** one creator's claim; **[mine]** my reading, not a fact.

| Part | File | Question |
|---|---|---|
| 1 | `01-monetization.md` | What does YouTube require and pay for, and what won't it pay for? |
| 2 | `02-long-and-shorts.md` | Do long videos and Shorts help or hurt each other on one channel? |
| 3 | `03-niche.md` | Which niche? (8 niches compared on this month's YouTube numbers) |
| 4 | `04-script.md` | Structure, story, conflict, resolution, wording (9 videos studied in full) |
| 5 | `05-packaging.md` | Titles, thumbnails, the click |
| 6 | `06-production.md` | How to make it efficiently (incl. Claude-made animation) |
| 7 | `07-running-it.md` | Cadence, what to read and when, how to change things |
| | `data/` | Channel numbers, niche scan, replay data, all read 2026-11-07 |
| | `tools/` | `chstats.py` (a channel's long/Shorts numbers), `nichescan.py` (compare niches) |

## What I found, in ten lines
1. **The bar doubles on 2027-02-01** and a pending application isn't protected. A new channel should plan for
   1,000 subscribers + **8,000 long-video watch hours in 12 months**: ~80-120K long-video views in a year, or one hit.
2. **Long videos are the money.** Shorts views never count as watch hours, Shorts pay 3-14% of long-video RPM, and
   from 2027 a channel needs 10M Shorts views per 90 days to be paid for Shorts at all.
3. **In our style, Shorts are a side dish.** Every mixed narrated/illustrated channel checked gets far more on long
   videos (Ifverse: 106K vs 20K median); the biggest ones post no Shorts.
4. **YouTube won't pay for "same situation, same outcome" videos** or anything that looks mass-produced. Each video
   must be clearly different and teach or tell something real. Cartoon/animated pictures need no AI label; the
   narration voice question is open.
5. **Best niche: money and business stories, explained simply.** Two channels under 7K subscribers had a 1M+ video
   this month; Crayon Capital holds a 292K median; education viewers pay the most in the one measured study, and
   finance tops every estimate.
6. **The topic and the first 30 seconds decide most of it.** Same channel, same format: Labubu 2.1M vs Tencent 1.2K,
   "$40 Trillion" 1.1M vs "Where Money Comes From" 8.1K. The hits open on an extreme concrete fact, a reversal and a
   stake for the viewer.
7. **A script needs one central question, a turn (decision, conflict, low point, comeback) and a payoff** that answers
   the question; mechanisms explained through a tiny world with recurring characters; concrete numbers, names, dates.
8. **Titles that hit name something known or a giant number and open a gap** ("...Explained Like You're 5", "WTF
   Happened to...?"). Our Ep. 1 got 0.6% CTR: packaging is our weakest link today.
9. **Claude-made animation (HyperFrames, already installed) can replace most Gemini pictures:** no quota, no account
   risk, consistent characters, real motion, and it suits money explainers. Look and speed are unproven until tested.
10. **It's a hit game:** most videos of small channels get little; plan for ~10 videos before judging, change one
    thing at a time.

## Decisions for Justin
| # | Decision | Recommended | Detail |
|---|---|---|---|
| 1 | Niche | Money & business stories explained simply (2nd: everyday history) | 03 |
| 2 | New channel or an existing one | New channel | 03, 3.4 |
| 3 | Format mix | Long videos first (12-16 min), 2-4 Shorts per long video, each linking to it | 02 |
| 4 | Target | 2027 bar: 1,000 subs + 8,000 h; Feb 2027 only if a video breaks out | 01 |
| 5 | Production | Hybrid: code animation + ~20-40 Gemini pictures per video, after a 60-90 s side-by-side test | 06 |
| 6 | Script rules | Template + checklist from 04 into the new channel's `RULES.md` | 04 |
| 7 | Packaging | Title and thumbnail written before the script; Test & Compare on every video | 05 |
| 8 | Voice | Find out whose voice the "Mark" sample is; label it or switch voice | 01, 1.4 |
| 9 | Cadence | 1-2 long videos + 4-8 Shorts a week to start | 07 |
| 10 | Affiliate income | Amazon Associates for the books/products mentioned (Justin's account) | 01, 1.5 |

## What this research did not settle
- How code-made animation looks and how long it takes on this PC (the test in 06, 6.6).
- Whether pending applications on 2027-02-01 keep the old bar (YouTube doesn't say).
- RPM for our exact niche and audience: only measurable once the channel earns.
- Shorts → long-video click rate for us: only measurable once we post.
- Search-based niche numbers show the winners first; one month of data.
