# Movie Explainer — rules

One movie explained in 1-2 minutes, told with stick figures.

## What a video is
- Say the movie's name (and year) in the first line.
- Shape: hook (the strange setup or the big question of the movie) -> the story in order, only the parts needed to
  follow it -> the ending, and what it means, in plain words.
- Say "spoilers" at the start when the video gives away the ending.
- **No movie footage, stills, posters or logos.** Everything is our own stick-figure drawing. Characters are drawn
  as stick figures with one simple feature that tells them apart (a hat, glasses, long hair), written once and
  reused in every prompt for that character.
- No quoting long lines from the movie; tell it in our own words. Character names are fine.

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
