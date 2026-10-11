# Law: Yes or No? (2 parts) — rules

Everyday situations where the law gets complicated. Part 1 asks the audience, Part 2 gives the answer.

## What a pair is
- Two videos about the same situation, made together: `videos/<slug>-part1/` and `videos/<slug>-part2/`.
  `settings.json` has `"parts": 2`.
- **Part 1 (the question):** set up one everyday situation with stick figures (a neighbour, a found wallet, a tree
  over the fence...). Give just the facts needed to decide, with no hint at the answer. End with a yes or no
  question, said plainly, and ask people to comment YES or NO. Part 1 never gives the answer.
- **Part 2 (the answer):** first line repeats the question in one sentence (people may see Part 2 first). Then the
  answer (yes, no, or "it depends on X", said plainly), then why, in plain words, then the one detail that would
  flip it.
- Pick situations where most people would guess wrong or be split. Law that is obvious makes a dull question.
- Same as US Laws: laws differ between states; say which state or "in most states".

## Same for every short channel

- **Length:** 60-120 s of narration (roughly 150-300 words; the voice step's `timings.json` is the real measure).
- **Format:** vertical 1080x1920 (9:16) for YouTube Shorts, TikTok and Reels.
- **No intro, no outro.** The first line is the hook, the last line ends the video.
- **Speak simple.** Basic everyday English, short sentences, one idea per sentence. No technical words, no legal
  words, no big words. If a word like that can't be avoided, say what it means in plain words right after it.
  Write it the way you'd explain it to a friend.
- **Hook first:** the first 2-3 seconds say what the video is about, as a question or a surprising line.
- **Images:** stick figures, black ink, plain paper background, like `channels/stickman-style.png`. The full style
  text is `image_style` in `settings.json` and goes into every prompt in full (every prompt stands on its own).
- **Segments:** 2-4 s each, one image per segment, never a one-word segment.
- **Flow:** same as Jin. Claude writes the script, runs it through `/humanize`, Justin approves it, it is saved as
  `videos/<slug>/script.md`; then the setup (`script.json`, prompts) and the pipeline make the video.
- **Facts are checked.** Every name, number, date and outcome must be real and checked; list the sources in
  `videos/<slug>/sources.md`. Never make a fact up to make the story better.
