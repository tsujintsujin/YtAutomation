"""Text -> WAV with Kokoro-82M (ONNX, CPU).

usage: python speak.py script.txt out.wav [--voice am_liam] [--speed 1.0]
       python speak.py --list-voices
"""
import argparse
from pathlib import Path

import soundfile as sf
from kokoro_onnx import Kokoro

MODELS = Path(__file__).parent / "models"

p = argparse.ArgumentParser()
p.add_argument("text_file", nargs="?")
p.add_argument("out", nargs="?", default="out.wav")
p.add_argument("--voice", default="am_liam")
p.add_argument("--speed", type=float, default=1.0)
p.add_argument("--lang", default="en-us")
p.add_argument("--list-voices", action="store_true")
a = p.parse_args()

kokoro = Kokoro(str(MODELS / "kokoro-v1.0.onnx"), str(MODELS / "voices-v1.0.bin"))
if a.list_voices:
    print("\n".join(kokoro.get_voices()))
    raise SystemExit

if not a.text_file:
    p.error("text_file is required")
text = Path(a.text_file).read_text(encoding="utf-8")
samples, sr = kokoro.create(text, voice=a.voice, speed=a.speed, lang=a.lang)
sf.write(a.out, samples, sr)
print(f"{a.out}: {len(samples) / sr:.1f}s audio")
