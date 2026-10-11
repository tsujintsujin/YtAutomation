# Legal but Questionable Ways to Get Rich (US) — rules

Ways people get rich in the US that are completely legal, but that many people think are wrong.

## What every way must be (Justin, 2026-10-11)
1. **It works today.** Something a person can still do now, not a story from years ago.
2. **It is completely legal.** Legal in the US, nothing illegal anywhere in it.
3. **It starts with no money, or very little.** A normal viewer could do it, not only a company with millions.
4. **It is very morally questionable, but no one is going to die from it.** (So no medicine price hikes.)

## What a video is
- One way to get rich per video (not one person's life story). A real person or company can be the example.
- Shape: hook (the money, or the "wait, that's legal?") -> what the way is, in plain words -> why it makes so much
  money -> why it is legal -> who pays the price, or why people think it's wrong.
- **Check that it really is legal** before writing, and say so in the video. A way that is illegal anywhere in the
  US, or only legal in some situations, is not a topic for this channel.
- **Show both sides fairly.** Say why people think it's wrong, and why the people doing it say it's fine. The viewer
  decides; the video doesn't call anyone a criminal.
- **Real names only with checked facts.** Anything said about a real person or company must come from a reliable
  source listed in sources.md. Never accuse anyone of a crime they weren't convicted of.

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
