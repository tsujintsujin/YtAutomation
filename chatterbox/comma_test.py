"""Isolated Chatterbox test: does it pause at commas? Not part of the pipeline.

usage: comma_test.py [voice.wav]   no clip -> built-in voice, out/; with a clip -> that voice copied, out_<clip>/

Writes out/NN_<case>.wav (default voice, exaggeration 0.5, cfg_weight 0.5) and prints every silent gap
of 60 ms or more in each clip, so the pauses can be lined up with the commas.
"""
import sys
import time
from pathlib import Path

import numpy as np
import torch
import torchaudio as ta
from chatterbox.tts import ChatterboxTTS

HERE = Path(__file__).parent
VOICE = Path(sys.argv[1]) if len(sys.argv) > 1 else None
OUT = HERE / (f"out_{VOICE.stem}" if VOICE else "out")
OUT.mkdir(exist_ok=True)

CASES = [
    ("no_comma", "The cat waited by the kitchen door for someone to come home."),
    ("one_comma", "When the morning light reaches the kitchen window, the cat starts to wait by her bowl."),
    ("many_commas", "The cat sat by the door, waiting, listening, and hoping someone would come home."),
    ("short_intro", "Yes, she knows exactly what she is doing."),
    ("comma_vs_period", "The cat sat by the door, she waited for hours. The cat sat by the door. She waited for hours."),
]


def gaps(wav, sr, min_ms=60):
    """Silent stretches (20 ms frames quieter than -40 dB of the clip's peak), leading/trailing silence excluded."""
    frame = int(sr * 0.02)
    x = wav[: len(wav) // frame * frame].reshape(-1, frame)
    db = 20 * np.log10(np.sqrt((x ** 2).mean(1)) + 1e-9)
    quiet = db < db.max() - 40
    loud = np.flatnonzero(~quiet)
    out, start = [], None
    for i in range(loud[0], loud[-1] + 1):
        if quiet[i] and start is None:
            start = i
        elif not quiet[i] and start is not None:
            if (i - start) * 20 >= min_ms:
                out.append((round(start * 0.02, 2), (i - start) * 20))
            start = None
    return out


t0 = time.time()
model = ChatterboxTTS.from_pretrained(device="cuda" if torch.cuda.is_available() else "cpu")
print(f"model loaded in {time.time() - t0:.0f}s on {model.device}")
for n, (name, text) in enumerate(CASES, 1):
    t = time.time()
    wav = model.generate(text, audio_prompt_path=str(VOICE) if VOICE else None)   # exaggeration=0.5, cfg_weight=0.5
    path = OUT / f"{n:02d}_{name}.wav"
    ta.save(str(path), wav, model.sr)
    a = wav.squeeze().cpu().numpy()
    print(f"\n{path.name}  {len(a) / model.sr:.2f}s audio, took {time.time() - t:.1f}s")
    print(f"  text: {text}")
    print("  pauses (at s, ms): " + ", ".join(f"{s}s {ms}ms" for s, ms in gaps(a, model.sr)))
