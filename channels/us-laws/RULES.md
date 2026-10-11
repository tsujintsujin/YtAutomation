# US Laws — rules

One real US law, or one surprising legal fact, explained so anyone gets it.

## What a video is
- One law or legal fact per video.
- Shape: hook (the surprising part, as a question or a "did you know") -> what the law says, in plain words -> a
  simple everyday example with stick figures -> why it exists or what happens if you break it.
- Laws differ between states. Say which state, or say "in most states" when that is the truth. Never say "it's
  illegal in the US" when it is only one state.
- No legal words. Say "the person who sues" not "plaintiff", "break the deal" not "breach of contract".
- Facts are checked against the law itself or a reliable source, listed in sources.md.

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
