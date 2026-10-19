# What Happens Now — rules

How an everyday process was done back then, and how it is done now. Stick-figure Shorts. Set by Justin 2026-10-18.

## What a video is
- One process (pulling a tooth, making ice cream, washing clothes ...): the old way step by step, then the same
  thing today step by step.
- **The "before" is the show.** That is what the hits are about (`research.md`). The "now" is researched by Claude
  and told just as plainly, but it is the payoff, not the main part.
- **Copy the structure of the hits, never their words.** The reference Shorts in `research.md` are studied for
  shape and pacing only. Our script is written from scratch, in our own words, with our own sources. Never reword
  another creator's script line by line, and never copy their jokes, lines or visuals.
- **Our own topics where possible.** When a topic is also in a reference video, tell it with our own facts, angle
  and wording.
- **Our own stickman character.** Original to this channel; it never looks like a real creator or a known character.
- **Colour (Justin, 2026-10-19):** still black-ink stick figures, but the one main object each picture is about is
  filled with flat colour (`"colour_subject"` in `settings.json`; each scene in `scenes.py` names it, same words
  every time). Everything else stays black ink.
- **Paper (Justin, 2026-10-19):** Gemini draws on pure white; the image prep step (`voice.py --images-only`) lays
  every picture on `paper.jpg` (`"paper_ref"`, copied into each video's `refs/paper.jpg`), so the background is
  always exactly that paper.
- **Every fact is real and checked.** How it was done, when, where, and how it is done now come from reliable
  sources listed in `videos/<slug>/sources.md`. When historians are not sure, say "probably" or "one idea is".

## Length (Justin, 2026-10-18)
- **Always more than 1 minute, never less.** The hits run 24-41 s; ours are 60-120 s, so the before part gets more
  steps and the now part is added.

## Template
Built from transcripts of the 6 reference Shorts in `research.md` (2026-10-18).
1. **Hook (2-3 s):** drop straight into the old way, mid-action, no intro ("They would press a sharp stone into your
   aching tooth."). Or a question about something people see every day that hides an old process.
2. **Before (about 60% of the video):** the old process in order, one step per sentence, each step a picture you can
   see. Talk to "you" ("you would feel every scrape"). Say what each step was for.
3. **Now (about 35%):** the same process today, in order, one step per sentence, as plain as the before part.
4. **End (one line):** the before and now side by side in one sentence, then stop.

## Same for every short channel
In `channels/SHORTS_RULES.md` (one copy for all short channels; the dashboard shows it under these rules).
