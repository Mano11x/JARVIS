# ============================================================
# brain/voice.py — Voice Input + Output
# ============================================================
JARVIS_VOICE = "en-US-GuyNeural"   # Edge-TTS voice ID

import pyttsx3
import threading

_tts_lock = threading.Lock()

def _speak_sync(text: str) -> None:
    with _tts_lock:
        try:
            engine = pyttsx3.init()
            engine.setProperty('rate', 160)
            engine.setProperty('volume', 1.0)
            voices = engine.getProperty('voices')
            for voice in voices:
                if "david" in voice.name.lower() or "david" in voice.id.lower():
                    engine.setProperty('voice', voice.id)
                    break
            engine.say(text)
            engine.runAndWait()
            engine.stop()
        except Exception as e:
            print(f"TTS Error: {e}")

def speak(text: str) -> None:
    print(f"Speaking: {text}")
    threading.Thread(target=_speak_sync, args=(text,), daemon=True).start()

def listen() -> str:
    return ""

def detect_wake_word(phrase: str, wake_word: str = "hey jarvis") -> bool:
    return wake_word.lower() in phrase.lower()
