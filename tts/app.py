"""Local voiceover UI: paste a script, pick a voice, get a WAV.

Run: Voiceover.bat (or .venv/Scripts/python app.py) -> http://127.0.0.1:7860
Every render is also saved to ../output/voiceovers/.
"""
import time
from pathlib import Path

import gradio as gr
import soundfile as sf
from kokoro_onnx import Kokoro

HERE = Path(__file__).parent
OUT = HERE.parent / "output" / "voiceovers"
OUT.mkdir(parents=True, exist_ok=True)

kokoro = Kokoro(str(HERE / "models" / "kokoro-v1.0.onnx"), str(HERE / "models" / "voices-v1.0-full.bin"))
# Every voice with a sample in samples/voices (NN_<id>.wav), in that order. a = US, b = British; f/m = female/male.
KIND = {"af": "US, female", "am": "US, male", "bf": "UK, female", "bm": "UK, male"}
VOICES = {}
for f in sorted((HERE / "samples" / "voices").glob("*.wav")):
    vid = f.stem.split("_", 1)[1]
    VOICES[f"{vid.split('_', 1)[1].title()} ({KIND[vid[:2]]})"] = vid


def speak(text, voice, speed):
    text = text.strip()
    if not text:
        raise gr.Error("Paste a script first.")
    vid = VOICES[voice]
    samples, sr = kokoro.create(text, voice=vid, speed=speed, lang="en-gb" if vid[0] == "b" else "en-us")
    path = OUT / f"{time.strftime('%Y%m%d-%H%M%S')}_{vid}.wav"
    sf.write(path, samples, sr)
    return str(path), f"Saved {len(samples) / sr:.1f}s of audio to {path}"


with gr.Blocks(title="Voiceover") as ui:
    gr.Markdown("# Voiceover")
    text = gr.Textbox(label="Script", lines=12, placeholder="Paste your narration here...")
    with gr.Row():
        voice = gr.Radio(list(VOICES), value="Liam (US, male)", label="Voice")
        speed = gr.Slider(0.7, 1.3, value=1.0, step=0.05, label="Speed")
    go = gr.Button("Generate", variant="primary")
    audio = gr.Audio(label="Result", type="filepath")
    status = gr.Markdown()
    go.click(speak, [text, voice, speed], [audio, status])

ui.launch(server_name="127.0.0.1", server_port=7860, allowed_paths=[str(OUT)])
