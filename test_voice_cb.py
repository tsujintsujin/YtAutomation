"""Check voice_cb.cuts: where each segment starts inside a take. Run: chatterbox/.venv/Scripts/python test_voice_cb.py"""
from voice_cb import cuts, words

group = [{"text": "You set it down on the coffee table"}, {"text": "and turn away for maybe one second."}]
# Whisper heard every word: the cut sits in the middle of the gap after "table" (1.80) and before "and" (2.00)
heard = [(w, i * 0.2, i * 0.2 + 0.15) for i, w in enumerate(words("you set it down on the coffee table"))]
heard += [(w, 2.0 + i * 0.2, 2.15 + i * 0.2) for i, w in enumerate(words("and turn away for maybe one second"))]
assert abs(cuts(group, heard, 3.5)[1] - (1.55 + 2.0) / 2) < 1e-9, cuts(group, heard, 3.5)

# Whisper misheard "table" and dropped "and": the nearest matched words either side are used
heard2 = [h for h in heard if h[0] != "and"]
heard2 = [("cable", s, e) if w == "table" else (w, s, e) for w, s, e in heard2]
assert abs(cuts(group, heard2, 3.5)[1] - (1.35 + 2.2) / 2) < 1e-9, cuts(group, heard2, 3.5)

assert words("It's — a cat’s box, 1872!") == ["it's", "a", "cat's", "box", "1872"]
print("ok")
