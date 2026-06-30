# ============================================================
# brain/voice.py — Voice Input + Output
# ============================================================
# Phase 7
#
# Whisper: converts your speech to text (STT)
# Edge-TTS: converts JARVIS responses to speech (TTS)
#
# Dependencies (uncomment in requirements.txt):
#   openai-whisper
#   edge-tts
#   pyaudio
#   SpeechRecognition
# ============================================================

# import whisper
# import edge_tts
# import asyncio
# import speech_recognition as sr


# ── TTS ──────────────────────────────────────────────────────

JARVIS_VOICE = "en-US-GuyNeural"   # Edge-TTS voice ID


import pyttsx3
import threading

def _speak_sync(text: str) -> None:
    try:
        engine = pyttsx3.init()
        
        # Set speaking rate to 160 (polite, elegant, and deliberate, like JARVIS in the movies)
        engine.setProperty('rate', 160)
        engine.setProperty('volume', 1.0)
        
        # Select David voice (male English US Desktop)
        voices = engine.getProperty('voices')
        for voice in voices:
            if "david" in voice.name.lower() or "david" in voice.id.lower():
                engine.setProperty('voice', voice.id)
                break
                
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        print(f"TTS Error: {e}")

def speak(text: str) -> None:
    print(f"Speaking: {text}")
    threading.Thread(target=_speak_sync, args=(text,), daemon=True).start()



# ── STT ──────────────────────────────────────────────────────

def listen() -> str:
    """
    Listen for speech via the microphone and return
    transcribed text using Whisper.

    Returns:
        str: Transcribed text from the user's speech.
             Returns empty string on failure.
    """

    # ── Phase 7: uncomment when whisper + pyaudio installed ─
    # recognizer = sr.Recognizer()
    # model = whisper.load_model("base")
    # with sr.Microphone() as source:
    #     print("Listening...")
    #     audio = recognizer.listen(source, timeout=5)
    #     audio_data = audio.get_wav_data()
    #     with open("temp_input.wav", "wb") as f:
    #         f.write(audio_data)
    #     result = model.transcribe("temp_input.wav")
    #     return result["text"].strip()
    # ────────────────────────────────────────────────────────

    return ""


def detect_wake_word(phrase: str, wake_word: str = "hey jarvis") -> bool:
    """
    Check if the wake word appears in an audio transcript.

    Args:
        phrase (str): Transcribed text from continuous listening.
        wake_word (str): The trigger phrase. Default: "hey jarvis".

    Returns:
        bool: True if wake word detected.
    """
    return wake_word.lower() in phrase.lower()
