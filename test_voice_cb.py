"""Checks for voice_cb: cut placement, word matching, splitting. Run: chatterbox/.venv/Scripts/python test_voice_cb.py"""
from voice_cb import MAX_WORDS, cuts, parts, score, words

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

# A group longer than MAX_WORDS is split at segment boundaries; a single segment is never split
long = [{"text": " ".join(["word"] * 20)} for _ in range(4)]
assert all(sum(len(x["text"].split()) for x in p) <= MAX_WORDS for p in parts(long)) and sum(map(len, parts(long))) == 4
assert parts([{"text": " ".join(["word"] * 80)}]) == [[{"text": " ".join(["word"] * 80)}]]
print("ok")
