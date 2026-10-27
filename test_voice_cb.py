"""Checks for voice_cb: cut placement, word matching, splitting. Run: chatterbox/.venv/Scripts/python test_voice_cb.py"""
from voice_cb import MAX_WORDS, cut_tail, cuts, parts, score, sentences, words
import numpy as np

group = [{"text": "You set it down on the coffee table"}, {"text": "and turn away for maybe one second."}]
# Whisper heard every word: the cut sits in the middle of the gap after "table" (1.55) and before "and" (2.00)
heard = [(w, i * 0.2, i * 0.2 + 0.15) for i, w in enumerate(words("you set it down on the coffee table"))]
heard += [(w, 2.0 + i * 0.2, 2.15 + i * 0.2) for i, w in enumerate(words("and turn away for maybe one second"))]
assert abs(cuts(group, heard, 3.5)[1] - (1.55 + 2.0) / 2) < 1e-9, cuts(group, heard, 3.5)

# Whisper misheard "table" and dropped "and": the nearest matched words either side are used
heard2 = [h for h in heard if h[0] != "and"]
heard2 = [("cable", s, e) if w == "table" else (w, s, e) for w, s, e in heard2]
assert abs(cuts(group, heard2, 3.5)[1] - (1.35 + 2.2) / 2) < 1e-9, cuts(group, heard2, 3.5)

# Numbers count the same however they are written (run 473 died on "thirty" vs "30")
assert words("It's roughly thirty to thirty six degrees Celsius.") == words("it's roughly 30 to 36 degrees celsius")
assert words("about eighty six to ninety seven degrees") == words("about 86 to 97 degrees")
assert words("In 2014 a team") == words("In twenty fourteen a team")
assert words("It's — a cat’s box!") == ["it's", "a", "cat's", "box"]

# Good take: 90% of the words, or at most 1 word different (short sentences); a dropped half is not good
assert score(words("The cats with boxes settled in much faster."), words("the cats with boxes settled in much faster"))[0]
assert score(words("It's just four lines of tape."), words("it's just for lines of tape"))[0]         # 1 word off
assert not score(words("Some of the new arrivals were given a box to hide in."), words("some of the new arrivals"))[0]

# A word Whisper heard that is not in the script fails the take (tooth-key-then-now: an extra "you" after "now.")
assert not score(words("There were no dentists like we have now."), words("there were no dentists like we have now you"))[0]
assert not score(words("Tooth-pullers went from town to town instead."), words("you tooth pullers went from town to town instead"))[0]
assert not score(words("They picked market days, when the square was full of people."),
                 words("they picked market days uh when the square was full of people"))[0]
# ...but a mishearing in place of a script word is not extra (both from tooth-key-then-now's voice-check.json)
assert score(words("Afterward, he said it hurt less than a pin prick."), words("afterward he said it hurt less than a pinprick"))[2] == 0
assert score(words("Then pliers called forceps rock it side to side and pull it straight out."),
             words("then pliers called forceps rocket side to side and pull it straight out"))[2] == 0
assert score(words("It's just four lines of tape."), words("it's just for lines of tape"))[2] == 0

# A group longer than MAX_WORDS is split at segment boundaries; a single segment is never split
long = [{"text": " ".join(["word"] * 20)} for _ in range(4)]
assert all(sum(len(x["text"].split()) for x in p) <= MAX_WORDS for p in parts(long)) and sum(map(len, parts(long))) == 4
assert parts([{"text": " ".join(["word"] * 80)}]) == [[{"text": " ".join(["word"] * 80)}]]

# A sentence of 3 words or fewer runs on into the next ("How?" alone came out odd, 2026-10-25)
segs = [{"id": i, "text": t} for i, t in enumerate(["And they went to war.", "How?", "One grandmother.", "Queen Victoria.",
                                                     "Germany. Russia. Greece.", "Spain. Romania. Norway."], 1)]
assert [[x["id"] for x in g] for g in sentences(segs)] == [[1], [2, 3, 4], [5, 6]], sentences(segs)

# Under 5 words the 1-word allowance is gone: "How'd" for "How?" is not good
assert not score(words("How?"), words("how'd"))[0]
assert score(words("How?"), words("how"))[0]

# Extra words after the script's last word are cut off the take; extra words inside it are left
sr = 1000
heard = [("spain", 0.0, 0.4), ("romania", 0.5, 1.0), ("norway", 1.1, 1.5), ("norway", 1.9, 2.3)]
wav, h = cut_tail(words("Spain. Romania. Norway."), heard, np.ones(2400, dtype=np.float32), sr)
assert len(wav) == 1700 and wav[-1] == 0 and [x[0] for x in h] == ["spain", "romania", "norway"], (len(wav), h)
inner = [("spain", 0.0, 0.4), ("you", 0.5, 0.6), ("romania", 0.7, 1.0)]
assert len(cut_tail(words("Spain. Romania."), inner, np.ones(1100, dtype=np.float32), sr)[0]) == 1100

# shouted (clipped) and babbled (voice runs long for its syllables) takes are not good; "for forty-six years" = 5
from voice_cb import sound, syllables
assert syllables("For forty-six years.") == 5, syllables("For forty-six years.")
voice = lambda s, level: (level * np.sin(np.arange(int(s * 24000)) / 5)).astype(np.float32)
assert sound(voice(1.0, 0.5), 24000, "For forty-six years.")[0] is True  # 0.2 s a syllable: fine (a plain bool: JSON)
assert not sound(voice(1.6, 0.5), 24000, "For forty-six years.")[0]      # 0.32 s a syllable: babble
assert not sound(voice(1.0, 1.0), 24000, "For forty-six years.")[0]      # full scale: shouted
print("all good")
