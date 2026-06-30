# ============================================================
# brain/core.py â€” JARVIS Central Router
# ============================================================
from brain.voice import speak
from brain.desktop import open_app
from brain.ai import get_response, is_ollama_running
from brain.safety import is_safe

def handle_message(user_input: str, user=None) -> str:
    cleaned_input = user_input.strip().lower()

    if not is_safe(user_input):
        response = "I can't help with that, Sir. Safety check failed."
        speak(response)
        return response

    if cleaned_input.startswith("open "):
        app_name = user_input[5:].strip()
        response = open_app(app_name)
        speak(response)
        return response

    if cleaned_input in ["hi", "hello", "hey", "wakeup", "wake up", "jarvis wakeup", "jarvis wake up"]:
        response = "Online and ready, Sir. How can I help you today?"
        speak(response)
        return response
    elif cleaned_input in ["who are you", "what is your name"]:
        response = "I am JARVIS, your personal strategic intelligence system, Sir."
        speak(response)
        return response
    elif cleaned_input in ["how are you", "how's it going"]:
        response = "All systems are operational and nominal, Sir. Ready for input."
        speak(response)
        return response

    try:
        import requests
        r = requests.get("http://localhost:11434", timeout=3)
        if r.status_code == 200:
            payload = {
                "model": "llama3.2:1b",
                "prompt": f"You are JARVIS, a helpful personal AI assistant. Call the user Sir. Keep responses direct and concise.\n\nUser: {user_input}\nJARVIS:",
                "stream": False,
            }
            res = requests.post("http://localhost:11434/api/generate", json=payload, timeout=30)
            response = res.json().get("response", "No response received, Sir.")
        else:
            response = "Ollama is running but returned unexpected status, Sir."
    except Exception as _e:
        print(f"OLLAMA ERROR: {_e}")
        response = f"I'm not wired to a local AI brain yet, Sir. To connect my AI, make sure Ollama is installed and running, then pull a model (like 'ollama pull llama3')."

    speak(response)
    return response
