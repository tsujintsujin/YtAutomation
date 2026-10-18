# Items People Found That Made Them Rich — rules

Real things ordinary people found (thrift stores, attics, yards, trash, old boxes) that turned out to be worth a
fortune. Stick-figure Shorts. Set by Justin 2026-10-18; replaces the four earlier short channels.

## What a video is
- A short list of real finds: who found it, where, what they paid (often nothing), what it turned out to be, what
  it sold for. The exact shape (hook, number of items, order, ending) comes from the template below.
- **Copy the structure of the hits, never their words.** The reference Shorts in `research.md` are studied for
  shape and pacing only. Our script is written from scratch, in our own words, with our own sources. Never reword
  another creator's script line by line, and never copy their jokes, lines or visuals.
- **Our own items where possible.** When a famous find is also in a reference video, tell it with our own facts,
  angle and wording.
- **Our own stickman character.** Original to this channel; it never looks like a real creator or a known character.
- **Every find is real and checked.** Names, places, prices, dates and sale amounts come from reliable sources
  listed in `videos/<slug>/sources.md`. "Could be worth" is said as "could be", never as a sale.

## Template (to fill in)
Built from transcripts of the top reference Shorts in `research.md`. Pending.

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
