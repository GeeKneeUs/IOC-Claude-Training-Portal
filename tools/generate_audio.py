"""Regenerate src/audio/*.mp3 from the NARRATION text embedded in src/index.html.

Requires edge-tts: python -m pip install edge-tts
Usage: python tools/generate_audio.py
"""
import asyncio
import json
import re
from pathlib import Path

import edge_tts

VOICE = "en-GB-RyanNeural"
ROOT = Path(__file__).resolve().parent.parent
HTML_PATH = ROOT / "src" / "index.html"
AUDIO_DIR = ROOT / "src" / "audio"


def load_narration():
    html = HTML_PATH.read_text(encoding="utf-8")
    match = re.search(r"var NARRATION = (\{.*?\n  \});", html, re.S)
    if not match:
        raise SystemExit("Could not find the NARRATION block in src/index.html")
    # The block is JS, not JSON (string concatenation with +, single quotes).
    # Evaluate it narrowly: pull out each "id: \"...\" + \"...\"" entry by hand.
    body = match.group(1)
    entries = re.findall(r"(m\d+):\s*((?:\"(?:[^\"\\]|\\.)*\"\s*\+?\s*)+)", body)
    narration = {}
    for module_id, concat in entries:
        parts = re.findall(r"\"((?:[^\"\\]|\\.)*)\"", concat)
        text = "".join(p.encode().decode("unicode_escape") for p in parts)
        narration[module_id] = text
    return narration


async def generate_one(module_id, text):
    out_path = AUDIO_DIR / f"{module_id}.mp3"
    communicate = edge_tts.Communicate(text, VOICE)
    await communicate.save(str(out_path))
    print(f"wrote {out_path.name} ({len(text)} chars)")


async def main():
    AUDIO_DIR.mkdir(parents=True, exist_ok=True)
    narration = load_narration()
    for module_id, text in narration.items():
        await generate_one(module_id, text)


if __name__ == "__main__":
    asyncio.run(main())
