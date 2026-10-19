# Shorts — rules for every short channel

These apply to every channel whose `settings.json` has `"pipeline": "shorts"` (found-rich, what-happens-now, and any new one). Each channel's own `RULES.md` holds only what is special to that channel. This is the one copy: change a shared rule here, never in a channel file.

- **Length:** 60-120 s of narration (roughly 150-300 words; the voice step's `timings.json` is the real measure).
- **Format:** vertical 1080x1920 (9:16) for YouTube Shorts, TikTok and Reels.
- **No intro, no outro.** The first line is the hook, the last line ends the video.
- **Speak simple.** Basic everyday English, short sentences, one idea per sentence. No technical words, no legal
  words, no big words. If a word like that can't be avoided, say what it means in plain words right after it.
  Write it the way you'd explain it to a friend.
- **Numbers in the narration are written in words, the way they are said** (Justin, 2026-10-18): the voice reads
  "1700s" as "one thousand seven hundreds". So "seventeen hundreds", not "1700s"; "eighteen forty-four", not "1844";
  "two thousand twenty-one", not "2021"; "four dollars", not "$4". Digits are only for the pictures.
- **Hook first:** the first 2-3 seconds say what the video is about, as a question or a surprising line.
- **Images:** stick figures, black ink, plain paper background, like `channels/stickman-style.png`. The full style
  text is `image_style` in `settings.json` and goes into every prompt in full (every prompt stands on its own).
- **Segments:** fast pace, 1-3 s each (Justin, 2026-10-18): most lines are cut in two, each half with its own
  image; lines under about 2 s stay one image. One image per segment, never a one-word segment.
- **Never "this"** for an item: no real picture is shown, so it is always "a" ("A four-dollar painting ...").
- **Flow:** same as Jin. Claude writes the script, runs it through `/humanize`, Justin approves it, it is saved as
  `videos/<slug>/script.md`; then the setup (`script.json`, prompts) and the pipeline make the video.
- **Image prompts:** written exactly as in "How image prompts are written" below. Every short channel, every video.
- **Facts are checked.** Every name, number, date and outcome must be real and checked; list the sources in
  `videos/<slug>/sources.md`. Never make a fact up to make the story better.

## How image prompts are written

Set by Justin 2026-10-18, after the found-rich video "A $4 painting was hiding $8 million" took many rounds because
the prompts were wrong. Writing the prompts is Claude's job in the pipeline. **Gemini draws exactly what the prompt
says**: every wrong picture in that video came from the prompt, not from Gemini. Every rule below comes from a
picture that went wrong, named after "Why:".

The worked example to copy is `channels/found-rich/videos/nail-sandwich-nugget-declaration/scenes.py`.

### The steps, in this order
1. **Read the whole script and `sources.md` first, and plan the video as one story.** Write down, before any prompt:
   - every person (one fixed description each: what makes them recognisable, e.g. a backwards cap and a lanyard),
   - every key object (one fixed description each, including how it changes: the sandwich gets a bite, then a face),
   - every place (one fixed description each),
   - which lines are two halves of one sentence: they are one moment, two pictures in a row.
   Why: prompts written one subtitle line at a time gave an empty floor for "On the floor / he spotted something
   small and shiny" (the worker vanished for a beat), a plain faceless sandwich right after "saw a face in the
   toast", and the ponytail woman losing her ponytail.
2. **For every line, answer three questions, then draw only that:**
   - What is happening in the story at this exact moment (script + `sources.md`)?
   - What does this line add to the picture before it?
   - Is anything in my picture something the story doesn't say? If so, take it out.
   Why: invented things told a different story than the voice: a money thought bubble for "did even better with
   her lunch" (she never thought about money), the casino man swapping cash in her kitchen (the casino bought it
   in an online auction), a museum pedestal for the nugget, the frame man visiting a museum and sitting in the
   auction's front row, "puzzled" faces nobody mentioned.
3. **Show what the line means, not its loose words.**
   Why: "an online casino" came out a man at a slot machine (it is a casino website); "that made people rich"
   came out objects on a shelf (it is the people getting rich); "looked like the Virgin Mary" came out a smiley
   face (it is the Virgin Mary image, a veiled woman's face, on the toast); "did even better" means more money
   than the person before.
4. **Write each prompt in full** with the frame below, then **check all of them against the story before any
   image is made**, and fix the whole set, not only the one Justin points at.
   Why: fixing only the flagged picture left the same mistake in others, and Justin had to find each one.
5. **Starting, stopping or redoing a run needs Justin's yes for that exact step.** A yes for one run is not a yes
   for the next. Why: a run was started on an old yes, and he had to stop it.

### What every scene text contains (the `shot()` frame in the example)
`This is picture N of M in one continuous picture story; draw exactly this moment.` + **what happens** (every
person and object written out in full) + `Place: ...` (written out in full) + `It MUST show: ...` (the one thing
the line is about) + `NEVER: ...` (the mistakes this picture is likely to make) + the captions line:
`The place fills the whole frame; keep the very top and very bottom of the frame calm (sky, wall or floor) for
captions. Never write any name, label or caption under or beside anyone or anything.`
`short_prompt()` in `dashboard.py` then wraps it with the 9:16 frame, the channel's full `image_style` and the
Avoid list. Every prompt stands on its own.

### Rules for the words
- **Gemini sees each prompt in a fresh chat and never sees the picture before.** Never write "the same shelf as
  the picture before" or "as above". Write every person, object and place out in full, in the same words, in
  every prompt it appears in (keep them as named text blocks in `scenes.py` and paste the block, never retype it).
  Why: picture 4 said "the same shelf as the picture before" and got a different shelf from picture 3.
- **Every scene has a fully written place.** The style text and the prompt frame must never say a place is
  drawn "only when needed" or ask for "empty paper above and below". Why: those two lines (now removed from
  `image_style` and `short_prompt`) gave bare pictures, like a laptop on a table with no room around it.
- **No capital labels in the text** ("THE STAGE WORKER: a stick-figure man ..."). Describe people in plain
  words. Why: Gemini printed "STAGE WORKER", "WOMAN", "NUGGET OWNER" as captions under the people.
- **Say "black ink lines only, no yellow, no brown, no colour" on anything that is coloured in real life**
  (toast, cheese, food, gold). Why: "darker toasting" gave a yellow and brown sandwich, although the style says
  no colour.
- **Words Gemini takes literally.** Pick words that can only mean the shape you want, and say what it must never
  look like. Why:
  - "a stiletto nail" came out a bullet standing up. Say: a thin flat fingernail shaped like a long narrow
    almond that tapers to a point; never a cone, a bullet or an object standing upright.
  - "a bump on its back like a backpack" (the nugget) came out a mug handle. Say: a rounded lump that is part of
    the same crumbly nugget; never a handle, loop or ring.
  - "a flat square shape" hidden under a cloth came out a visible sandwich. For a hidden thing, say it is fully
    covered and only a cloth lump shows.
- **Make sure a NEVER never forbids what the line needs.** Why: "never any religious figure" sat in the prompt for
  "To her, it looked like the Virgin Mary", fighting the line.
- **Hidden things stay hidden in a hook.** A teaser picture must not give away what a later picture reveals.

### Where the prompts live
- `script.md` "Lines and pictures" holds each line with a first sketch of its picture; approving builds
  `script.json` from it.
- Then the video's own `scenes.py` (next to `script.md`, like the example) holds the fixed descriptions and the
  full scene for every line, and writes `scene` + `prompt` into `script.json`. That is what Gemini gets. It checks
  that every line's id and text match `script.json`, so it can't drift from the script.
- Never edit `script.json` while a run is going; write it when no run is going, then make again only the
  pictures whose prompt changed.

### Before calling a set of prompts done
Read every prompt once more against its line and its neighbours: same people and objects described in the same
words, a full place, nothing the story doesn't say, the line's meaning shown, no capital labels, black ink only.
Then test 2-3 pictures and look at them before the rest are made.
