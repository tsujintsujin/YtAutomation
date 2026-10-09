"""Chatterbox page: paste a script, pick a voice clip to copy, play with every setting, get a WAV.

Run: started by the dashboard's Chatterbox button (or .venv/Scripts/python app.py) -> http://127.0.0.1:7861
Not part of the video pipeline. Every render is saved to ../output/voiceovers/.
A model loads into the GPU the first time it is used (~40 s); only one is kept loaded (6 GB card).
"""
import copy
import gc
import logging
import random
import re
import time
from pathlib import Path

import gradio as gr
import numpy as np
import soundfile as sf
import torch

HERE = Path(__file__).parent
OUT = HERE.parent / "output" / "voiceovers"
OUT.mkdir(parents=True, exist_ok=True)
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
logging.basicConfig(filename=HERE / "app.log", level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
log = logging.getLogger("chatterbox-page")

BUILTIN, CLIP = "Chatterbox built-in voice", "Clip below (upload or record)"
CHANNEL = "Mark (Jin the Geek voice)"
KIND = {"af": "US female", "am": "US male", "bf": "UK female", "bm": "UK male"}
SAMPLES = sorted(f for f in (HERE.parent / "tts" / "samples" / "voices").iterdir() if f.suffix in (".wav", ".mp3"))
VOICES = {CHANNEL: next(f for f in SAMPLES if f.stem == "29_mark")}
VOICES[BUILTIN] = None
for f in sorted((HERE / "refs").glob("*.wav")):                       # your own recordings
    VOICES[f"{f.stem.title()} (recording)"] = f
for f in SAMPLES:                                                      # the 28 Kokoro samples, NN_am_liam.wav
    parts = f.stem.split("_", 2)
    if len(parts) == 3 and parts[1] in KIND:
        VOICES[f"{parts[2].title()} (Kokoro, {KIND[parts[1]]})"] = f
VOICES[CLIP] = None

loaded = {"name": None, "model": None, "default_conds": None}


def get_model(name):
    if loaded["name"] != name:
        loaded["model"] = loaded["default_conds"] = None                # free the other model first
        gc.collect()
        torch.cuda.empty_cache()
        if name == "Turbo":
            from chatterbox.tts_turbo import ChatterboxTurboTTS
            loaded["model"] = ChatterboxTurboTTS.from_pretrained(device=DEVICE)
        else:
            from chatterbox.tts import ChatterboxTTS
            loaded["model"] = ChatterboxTTS.from_pretrained(device=DEVICE)
        loaded["default_conds"] = copy.deepcopy(loaded["model"].conds)  # the built-in voice
        loaded["name"] = name
    return loaded["model"]


def chunks(text, limit=250):
    """Sentences, grouped up to ~limit characters, so long scripts work and short ones stay one take."""
    out = []
    for s in re.split(r"(?<=[.!?])\s+", text.strip()):
        if out and len(out[-1]) + len(s) < limit:
            out[-1] += " " + s
        else:
            out.append(s)
    return out


def speak(*args, progress=gr.Progress()):
    """Generate, and put the real reason for a failure in app.log and on the page (Gradio otherwise shows 'Error')."""
    try:
        return _speak(*args, progress=progress)
    except gr.Error:
        raise
    except Exception as e:
        log.exception("generate failed; settings: %s", args[1:])
        raise gr.Error(f"{type(e).__name__}: {e}"[:500])


def _speak(text, model_name, voice, clip, exaggeration, cfg, temperature, rep_pen, min_p, top_p, top_k, seed, gap,
           progress):
    text = text.strip()
    if not text:
        raise gr.Error("Paste a script first.")
    ref = clip if voice == CLIP else VOICES[voice]
    if voice == CLIP and not clip:
        raise gr.Error("Upload or record a clip first (10-20 s of one person talking).")
    if model_name == "Turbo" and ref is None:
        raise gr.Error("Turbo has no built-in voice: pick a recording, a Kokoro sample or a clip.")
    t0 = time.time()
    progress(0, desc=f"Loading {model_name} (first time ~40 s)" if loaded["name"] != model_name else "Starting")
    m = get_model(model_name)
    if ref is None:
        m.conds = copy.deepcopy(loaded["default_conds"])
    elif model_name == "Turbo":
        m.prepare_conditionals(str(ref), norm_loudness=True)
    else:
        m.prepare_conditionals(str(ref), exaggeration=exaggeration)
    seed = int(seed) or random.randint(1, 2**31 - 1)
    random.seed(seed), np.random.seed(seed), torch.manual_seed(seed)
    parts, pieces = chunks(text), []
    for i, piece in enumerate(parts):
        progress(i / len(parts), desc=f"Part {i + 1} of {len(parts)}")
        if model_name == "Turbo":
            wav = m.generate(piece, temperature=temperature, repetition_penalty=rep_pen, top_p=top_p, top_k=int(top_k))
        else:
            wav = m.generate(piece, exaggeration=exaggeration, cfg_weight=cfg, temperature=temperature,
                             repetition_penalty=rep_pen, min_p=min_p, top_p=top_p)
        pieces += [wav.squeeze().cpu().numpy(), np.zeros(int(m.sr * gap), dtype=np.float32)]
    audio = np.concatenate(pieces[:-1])
    who = Path(ref).stem if ref else "builtin"
    tag = f"ex{exaggeration}_cfg{cfg}_" if model_name == "Standard" else ""
    path = OUT / f"{time.strftime('%Y%m%d-%H%M%S')}_cb-{model_name.lower()}_{who}_{tag}t{temperature}_seed{seed}.wav"
    sf.write(path, audio, m.sr)
    log.info("saved %s", path.name)
    return str(path), (f"Saved {len(audio) / m.sr:.1f}s of audio in {time.time() - t0:.0f}s, "
                       f"{len(parts)} part(s), seed **{seed}** (type it in Seed to get this take again).  \n`{path}`")


with gr.Blocks(title="Chatterbox") as ui:
    gr.Markdown("# Chatterbox")
    text = gr.Textbox(label="Script", lines=10, placeholder="Paste your narration here...")
    with gr.Row():
        model_name = gr.Radio(["Standard", "Turbo"], value="Standard", label="Model",
                              info="Turbo: faster, understands [laugh] [chuckle] [sigh] [cough] [gasp] in the text; needs a voice clip")
        voice = gr.Dropdown(list(VOICES), value=CHANNEL, label="Voice to copy")
    clip = gr.Audio(label="Clip (when 'Clip below' is picked): 10-20 s of one person, quiet room",
                    sources=["upload", "microphone"], type="filepath")
    with gr.Row():
        exaggeration = gr.Slider(0.25, 2.0, value=0.5, step=0.05, label="Exaggeration",
                                 info="Emotion: calm (low) to dramatic (high)")
        cfg = gr.Slider(0.0, 1.0, value=0.5, step=0.05, label="CFG / pace",
                        info="Lower = slower, more deliberate. Try 0.3 with high exaggeration")
        temperature = gr.Slider(0.05, 2.0, value=0.8, step=0.05, label="Temperature",
                                info="Low = steady and same each time, high = more varied")
    with gr.Row():
        seed = gr.Number(value=0, precision=0, label="Seed", info="0 = random. Reuse a seed to get the same take")
        gap = gr.Slider(0.0, 1.0, value=0.3, step=0.05, label="Pause between parts (s)",
                        info="Long scripts are made a few sentences at a time")
    with gr.Accordion("Advanced", open=False):
        with gr.Row():
            rep_pen = gr.Slider(1.0, 2.0, value=1.2, step=0.05, label="Repetition penalty")
            min_p = gr.Slider(0.0, 1.0, value=0.05, step=0.01, label="min_p (Standard)")
            top_p = gr.Slider(0.0, 1.0, value=1.0, step=0.01, label="top_p")
            top_k = gr.Slider(1, 2000, value=1000, step=1, label="top_k (Turbo)", visible=False)
    go = gr.Button("Generate", variant="primary")
    audio = gr.Audio(label="Result", type="filepath")
    status = gr.Markdown()

    def switch(name):                                 # Turbo ignores exaggeration, CFG and min_p; Standard has no top_k
        std = name == "Standard"
        return (gr.update(visible=std), gr.update(visible=std), gr.update(visible=std), gr.update(visible=not std),
                gr.update(value=1.0 if std else 0.95))
    model_name.change(switch, model_name, [exaggeration, cfg, min_p, top_k, top_p])
    go.click(speak, [text, model_name, voice, clip, exaggeration, cfg, temperature, rep_pen, min_p, top_p, top_k, seed,
                     gap], [audio, status])

ui.queue().launch(server_name="127.0.0.1", server_port=7861, allowed_paths=[str(OUT)])
