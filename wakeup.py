import os
import sys
import time
import subprocess
import webbrowser
import speech_recognition as sr
import pyttsx3
import urllib.request

def speak(text):
    print(f"JARVIS: {text}")
    try:
        engine = pyttsx3.init()
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
        print(f"Speech error: {e}")

def is_server_running():
    try:
        urllib.request.urlopen("http://127.0.0.1:8000/assistant/", timeout=1)
        return True
    except Exception:
        return False

def start_server():
    if is_server_running():
        speak("Server is already running, Sir.")
        return
    
    speak("Starting the server, Sir.")
    # Locate virtual environment python
    python_exe = os.path.join(".venv", "Scripts", "python.exe")
    if not os.path.exists(python_exe):
        python_exe = os.path.join("venv", "Scripts", "python.exe")
    if not os.path.exists(python_exe):
        python_exe = sys.executable  # fallback
    
    # Start the django process in the background
    subprocess.Popen([python_exe, "manage.py", "runserver"])
    
    # Wait for the server to spin up
    for _ in range(5):
        time.sleep(1)
        if is_server_running():
            break

def main():
    recognizer = sr.Recognizer()
    try:
        microphone = sr.Microphone()
    except Exception as e:
        speak("No microphone detected, Sir. Please plug in a microphone.")
        return

    speak("Voice wakeup system is online, Sir. Say 'JARVIS WAKEUP' to start the server.")

    while True:
        with microphone as source:
            recognizer.adjust_for_ambient_noise(source, duration=1)
            print("Listening for wake word...")
            try:
                audio = recognizer.listen(source, timeout=3, phrase_time_limit=3)
            except sr.WaitTimeoutError:
                continue
            except Exception as e:
                print(f"Error listening: {e}")
                continue

        try:
            phrase = recognizer.recognize_google(audio).lower()
            print(f"Heard: {phrase}")
            if "wakeup" in phrase or "wake up" in phrase or "jarvis" in phrase:
                speak("Awaiting your command, Sir. Opening the chat page.")
                start_server()
                webbrowser.open("http://127.0.0.1:8000/assistant/")
                break
        except sr.UnknownValueError:
            pass
        except sr.RequestError as e:
            print(f"Could not request results from speech service; {e}")

if __name__ == "__main__":
    main()
