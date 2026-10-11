# Illegal Ways to Get Rich (US) — rules

Real people in the US who got rich by breaking the law, and how it ended for them.

## What a video is
- One real, documented US case per video (a scheme, a scam, a fraud). Named person, real years, real amounts.
- Shape: hook (how much they made, or how wild it was) -> what they did, in plain words -> how it fell apart /
  how they got caught -> what happened to them (prison time, fines, money taken back).
- **Explain what they did, never how to do it.** No step-by-step, no tips, no "how to avoid getting caught".
  One plain sentence on how the scheme worked is enough. YouTube, TikTok and Instagram all remove videos that teach
  people to commit crimes, and strikes can end the channel.
- Always end with the consequence. The story is "it looked like a shortcut, here is the price".
- Don't present an accusation as fact: if they were never convicted, say so.

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
