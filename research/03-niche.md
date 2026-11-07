# 3. What content: which niche

Researched 2026-11-07. Tags as in `01-monetization.md`. Data: `data/niches-2026-11-07.md` (YouTube search, last 30
days, 8 niches, ~550 videos) and `data/channels-2026-11-07.md` (full upload lists of 16 channels).

## The short version
- **Recommended: money and business stories, explained simply** ("how Rockefeller got rich", "why the Great
  Depression happened", "what happened to Labubu", "who America owes $40 trillion"). Proven demand, small new channels
  breaking out right now, the best-paying viewers on YouTube, and it fits code-made animation (charts, numbers,
  timelines, simple figures) and our money-channel experience.
- **Second choice: everyday history** ("the worst jobs in history", "what life was really like in a medieval castle").
- **What-if stories** have the biggest views today but are being cloned fast and pay less. **Found fortunes** is weak.
- **Every niche is hit-driven.** Most small channels have 1-3 big hits and most videos under 10K. The plan must survive
  many flops (`07-running-it.md`).

## 3.1 How niches were compared
For each niche, 4-6 YouTube searches, uploads of the last 30 days sorted by views, long videos only (4+ min). Then the
upload lists of the channels that broke out. Criteria:
1. **Demand:** do videos uploaded this month get big views?
2. **Room for a new channel:** do channels under ~20K subscribers get hits (not only big names)?
3. **Pay:** what kind of viewer and advertiser (`01-monetization.md` 1.2).
4. **Fit:** can our pipeline make it (illustrated or code-animated, narrated, faceless), long and Short?
5. **Durability:** evergreen topics, or a fad being cloned?

**Limits [mine]:** search shows the winners first, so the medians are medians of the top results, not of the niche.
One month of data. Compare niches with each other, not with real-life averages.

## 3.2 The niches, with the numbers

| Niche | Small-channel hits this month | Channels that show what's possible | Pay [mine, from 1.2] | Fit | Verdict |
|---|---|---|---|---|---|
| **Money & business explained** | Fortune & Fall (5.7K subs) 2.1M; PENNY (6.8K) 1.1M; "Explained Like You're 5" (3.5K) 102K | Crayon Capital: 33 videos, **median 292K**, 298K subs; Capital Case (copy, 11K subs): median 53K | High (finance/education, US) | Charts, numbers, timelines, simple figures | **Best** |
| POV money stories | 11 of the top 12 on small channels: Nate's Money Map (1.1K) 300K x3, POV Wealth (5.5K) 668K | POV Finance median 27K; Nate median 4.4K | Mid-high (older US men) | Proven in our pipeline | Hits, but clones flood it and "same situation, same outcome" is a policy risk (01, 1.3) |
| What-if stories | Minute Zero (22K) 2.3M; Kian Odyssey (5K) 1.8M; ConChaser (18K) 1.3M; Iflord (11K) 1.1M | Ifverse median 106K; ConChaser median 129K | Lower (young, worldwide) [mine] | Stick figures, fits | Biggest views now, but fading fast on repeats: Minute Zero's 5 newest (7-12 days old, same "couldn't stop" premise) at 5-21K after 2.3M; Iflord's 9-11-day-old uploads at 35-52K after 1.1M |
| Everyday history | quack doc's 699K; Runic (13K) 539K; Zeno (4K) 230K | quack doc: 137 videos, median 202K | Mid (education) | Long (20-35 min) = many pictures | **Good second** |
| Luck / survival / worst | 1 small hit (Paint Simples 310K, a Simple Paint copy) | Simple Paint median 212K, Paint Explainer 383K | Mid | Our LuckySticks look | Held by big paint channels and reaction channels |
| Psychology explained | Unclear: search filled by big creators and podcasts | | Mid | | Not enough signal |
| Personal finance explained | Weak in search (156 median) | | High | | Covered better by "money & business explained" |
| Found fortunes | None: best 46K | | Mid | Our LuckySticks topic | **Drop** for long videos |

## 3.3 Why money & business explained
- **Demand is proven and recent:** Crayon Capital's newest videos still do 181K-915K ("The Rise of Anthropic Explained
  Like You're 5", 915K in 3 weeks). Its formula is "big money story + explained like you're 5", 13-21 minutes.
- **New channels get in:** two channels under 7K subscribers (Fortune & Fall, PENNY) had a video over 1M in the last
  30 days; a third (Explained Like You're 5, 3.5K) had 102K in 6 days.
- **Topics never run out:** company rises and falls, famous fortunes, crashes and bubbles, and today's money news.
  Evergreen videos keep earning watch hours; news videos catch spikes.
- **Best-paying viewers [report/mine]:** finance and education are at the top of every RPM list; the one measured
  study put education highest ($10.22 median). US-centred topics pull US viewers.
- **Shorts fit naturally:** each video has 3-4 jaw-drop facts ("$500 every second since Jesus still isn't enough")
  that stand alone as Shorts.
- **Animation fits:** the Claude-animation video (`06-production.md`) made exactly this: charts, counters, simple
  figures. Our Paperback Millionaire research (money books, real numbers) carries over.
- **Value is obvious:** every video teaches something true, which is what YouTube's inauthentic-content review looks
  for (01, 1.3).

**Risks:** it's a research-heavy niche (wrong numbers kill trust; the Claude-animation demo itself showed a wrong
number); copies are appearing (Capital Case copies Crayon Capital's title shape); news topics age fast.
**How we differ:** see `04-script.md` (story-first structure) and `06-production.md` (our own look).

## 3.4 What this means for our current channels [mine]
- **Found fortunes** (LuckySticks topic) shows no long-video demand this month. Keep it as Shorts only, or stop.
- **POV money** (Paperback Millionaire) can keep going, but each premise must be truly different (policy).
- A **new channel** for money & business explained is cleaner than turning an existing one around: YouTube reviews
  the whole channel's theme, and the old channels' audiences are elsewhere (LuckySticks 49% Philippines).

## 3.5 Decisions this part asks for
1. Niche: money & business explained (recommended) or everyday history.
2. New channel, or one of the existing three.
3. Re-run `tools/nichescan.py` before launch and monthly (the niche moves).

## Sources
- `data/niches-2026-11-07.md`, `data/channels-2026-11-07.md` (YouTube, read 2026-11-07)
- Channels: https://www.youtube.com/@Crayon_Capital, https://www.youtube.com/@Capital_Case,
  https://www.youtube.com/@pennyexplainsfinance, https://www.youtube.com/@FortuneFall-c4u,
  https://www.youtube.com/@IfverseTales, https://www.youtube.com/@ConChaser, https://www.youtube.com/@quackdoc,
  https://www.youtube.com/@MoneyMapWithNate
- RPM: see `01-monetization.md` 1.2
