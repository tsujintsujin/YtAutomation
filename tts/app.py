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

kokoro = Kokoro(str(HERE / "models" / "kokoro-v1.0.onnx"), str(HERE / "models" / "voices-v1.0.bin"))
VOICES = {"Liam": "am_liam", "Santa": "am_santa"}


def speak(text, voice, speed):
    text = text.strip()
    if not text:
        raise gr.Error("Paste a script first.")
    samples, sr = kokoro.create(text, voice=VOICES[voice], speed=speed, lang="en-us")
    path = OUT / f"{time.strftime('%Y%m%d-%H%M%S')}_{voice.lower()}.wav"
    sf.write(path, samples, sr)
    return str(path), f"Saved {len(samples) / sr:.1f}s of audio to {path}"


with gr.Blocks(title="Voiceover") as ui:
    gr.Markdown("# Voiceover")
    text = gr.Textbox(label="Script", lines=12, placeholder="Paste your narration here...")
    with gr.Row():
        voice = gr.Radio(list(VOICES), value="Liam", label="Voice")
        speed = gr.Slider(0.7, 1.3, value=1.0, step=0.05, label="Speed")
    go = gr.Button("Generate", variant="primary")
    audio = gr.Audio(label="Result", type="filepath")
    status = gr.Markdown()
    go.click(speak, [text, voice, speed], [audio, status])

ui.launch(server_name="127.0.0.1", server_port=7860, allowed_paths=[str(OUT)])
