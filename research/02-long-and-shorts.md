# 2. Long videos and Shorts on one channel

Researched 2026-11-07. Tags as in `01-monetization.md`. Channel numbers were read from YouTube that day with yt-dlp
(`tools/chstats.py` in the session scratchpad; the raw numbers are in `data/channels-2026-11-07.md`).

## The short version
- **YouTube says Shorts don't hurt long videos**: separate recommendation systems for each format.
- **In our kind of channel (narrated, illustrated stories and explainers), Shorts barely work.** On every mixed channel
  checked, Shorts got a small fraction of the long videos' views. The big channels in this style post long videos only.
- **The Shorts that do work are made as Shorts** (one quick idea, built for the feed), not trailers of a long video.
- **So: long videos first.** Shorts are a cheap side channel to test ideas and pick up viewers, made from the long
  video's own pictures and script, and they link to it.

## 2.1 What YouTube says
**[YouTube]** Blog, 2025-05-06, "Debunking common myths about YouTube Shorts": "we haven't seen evidence of Shorts
negatively impacting long-form performance"; Shorts and long videos have "separate recommendation systems optimized for
each", which still "understand cross-format viewing". Shorts can "drive traffic to your long-form content". No numbers
are given; it is a marketing post.

**[report]** Independent checks mostly agree on average (one study of 22 channels around the time they started Shorts:
long-video performance unchanged). The risk they name is **audience mismatch**: Shorts can bring subscribers who never
watch long videos, so subscriber count rises without watch hours.

## 2.2 What mixed channels in our style actually get
Median views of the newest ~20 uploads of each kind, read 2026-11-07:

| Channel | Subs | Long videos (count, median) | Shorts (count, median) |
|---|---|---|---|
| Ifverse (what-if, stick figures) | 60K | 18, **106,000** | 14, 20,500 |
| Iflord (what-if) | 11K | 11, 52,000 | 2, 5,700 |
| Minute Zero (what-if) | 22K | 15, 48,000 | 1, 228,000 (one Short) |
| PENNY (money explained) | 6.8K | 9, 13,000 | 3, 1,000 |
| History Meets Finance | 149K | 129, 13,500 | 32, 625 |
| Kian Odyssey (space what-if) | 5K | 24, 2,550 | 11, 226 |

(The newest uploads include some only days old, so these medians run a little low; the gap between long videos and
Shorts is far bigger than that.)

Long-only channels in the same style, for scale: The Paint Explainer 2.0M subs (median 383K), Simple Paint 546K (212K),
Crayon Capital 298K (292K), quack doc 187K (202K), ConChaser 18K (129K). None post Shorts.

Shorts-only channels are a different business: Zack D. Films (29.6M subs, 4,143 Shorts, newest Shorts ~5M each) makes
one quick 3D "what happens if" idea per Short, built for the feed.

**[mine]** Shorts that are a slice of a long story underperform. A Short has to be a complete idea on its own.

## 2.3 Linking Shorts to long videos
**[YouTube]** A Short can carry one "Related video" link to any video on the same channel (set in Studio).
**[report]/[creator]** No platform numbers exist. Reports range from ~0.05% of Short viewers clicking to ~10% in one
creator's well-matched test. Our own number is the one that counts: read the long video's traffic source "Shorts" in
Studio.

## 2.4 Posting rhythm
**[creator]** Jack Craig (Shorts): on a new channel, space the first 5 uploads at least 48 h apart, and post the next
one only when the last one drops below ~100 views/hour for 12 hours; he says rushing a 4th Short killed it while the
3rd was still climbing. **One creator's claim**, but it contradicts what LuckySticks does (3 a day), so it is worth a
test on our own numbers.
**[YouTube]** No official guidance on frequency in the myths post.

## 2.5 Decisions this part asks for
1. The channel is a long-video channel first: 1-3 long videos a week.
2. Each long video yields 2-4 Shorts, each a complete idea (the most surprising fact or moment), written as a Short,
   using the long video's pictures, each linking to the long video.
3. Read Shorts → long-video clicks in Studio from the first month, and drop Shorts if they bring nothing.

## Sources
- YouTube Blog, Shorts myths (2025-05-06): https://blog.youtube/creator-and-artist-stories/debunking-common-myths-about-youtube-shorts/
- Independent analysis of Shorts and long-form: https://www.overseeros.com/blog/do-youtube-shorts-hurt-long-form-views
- Related video link: https://tubefilter.com/2023/09/01/youtube-related-links-multi-format-creators-shorts-live-long-form/
- Jack Craig, "I BLEW UP a YouTube Channel in 7 Days with AI": https://www.youtube.com/watch?v=1r0eyM7suUg
- Channel numbers: YouTube channel pages read with yt-dlp, 2026-11-07 (`data/channels-2026-11-07.md`).
