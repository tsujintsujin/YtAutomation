# 7. Running the channel

Researched 2026-11-07. Tags as in `01-monetization.md`. Builds on `channels/ANALYTICS.md` (the daily Studio read
that already runs for the Shorts channels).

## The short version
- **It's a hit game.** Small channels in every niche checked had 1-3 big hits and most videos far lower (Fortune &
  Fall: one 2.1M video, median 1,150; Nate's Money Map: three ~300K videos, median 4,450). Plan for many misses.
- **Quality and topic over volume.** The channels that hold a high median post about once a week or less, not daily.
- **Read the numbers at 24 h, 72 h and 7 days, change one thing at a time, judge a format after ~10 videos.**

## 7.1 The goal line
8,000 watch hours in 12 months (01, 1.1) = ~22 hours a day = ~1,315 minutes a day.

| Average view duration | Long-video views needed per day |
|---|---|
| 4 min | ~330 |
| 6 min | ~220 |
| 8 min | ~165 |

Plus 1,000 subscribers. Track both daily in the same sheet as the Shorts.

## 7.2 Cadence
- **Long videos: 1-2 a week to start.** Crayon Capital has 33 videos in 13+ months (its 4.3M video is from October
  2025), under one a week, and 298K subscribers; ConChaser has 15 videos and a 129K median. Raise the pace only when
  the pipeline makes them without lowering the script work.
- **Shorts: 2-4 per long video**, spread over the days between long videos, each linking to its long video (02).
- **[creator, to test]** Jack Craig: on a new channel, let each upload settle (until it drops under ~100 views an hour
  for 12 hours) before the next. Test it on the Shorts first.
- **Never post repeats:** Minute Zero's repeats of one premise fell from 2.3M to 5-21K within weeks (03).

## 7.3 What to read, and when
| When | Long video | Short |
|---|---|---|
| 24 h | Impressions, CTR (don't judge before), first viewers' average view duration | Views, stayed to watch % |
| 72 h | CTR vs our other videos; retention graph: % at 30 s, where the big drops are; traffic sources (browse, suggested, search, Shorts) | Stayed to watch %, average % viewed, subscribers |
| 7 days | Views/day trend; subscribers per 1,000 views; Test & Compare result | Clicks to the linked long video |

**Benchmarks to aim for:**
- **[report]** CTR: half of channels sit at 2-10%; below 2% means the title/thumbnail is the problem.
- **[creator]** Shorts "stayed to watch": ~80% is good, 60% is weak (Jack Craig).
- **[YouTube]** The 30-second intro number: if it's low, change the open or make the title/thumbnail match.

## 7.4 How to change things
- **One change at a time**, on one lever: topic, title, thumbnail, cold open, length, Shorts timing.
- **Write each change and its result** in the channel's `LEARNINGS.md` (the LuckySticks daily routine already does
  this).
- **Judge a format after ~10 long videos**, not 2: one hit in ~10-30 is the pattern.
- **Stop rule:** after 10 long videos with no video over ~10K views and CTR under 2%, the topic choice or packaging is
  wrong, not the luck: re-run the niche scan and change the topic family.
- **Copy what hits, inside our own channel:** when one of ours hits, make the next 2-3 on neighbouring topics with the
  same title shape (not the same premise).

## 7.5 Topic pipeline
- Monthly: `python research/tools/nichescan.py <out.json>` (edit the niche queries first); look for small channels'
  hits.
- Weekly: a list of 10 candidate topics, each checked against 04, 4.9 (number, reversal, conflict, stake) and 05, 5.1
  (known subject or giant number + gap). Search YouTube for each: if big channels did it recently, find a new angle or
  drop it.
- Always 2-3 scripts ahead, so a run never waits for writing.

## 7.6 Decisions this part asks for
1. Cadence: 1-2 long videos + 4-8 Shorts a week to start.
2. The 24 h / 72 h / 7 d read and the stop rule above, added to `channels/ANALYTICS.md` for the new channel.

## Sources
- `data/channels-2026-11-07.md`; `channels/ANALYTICS.md`; `channels/book-stories/STRATEGY.md`
- Jack Craig: https://www.youtube.com/watch?v=1r0eyM7suUg
- YouTube Help, retention: https://support.google.com/youtube/answer/9314415
