# ============================================================
# brain/ai.py — Ollama LLM Integration
# ============================================================
# Phase 3
#
# Handles all communication with the local Ollama server.
# Ollama runs a local LLM (e.g. llama3, mistral) and
# exposes a REST API on http://localhost:11434
#
# Setup:
#   1. Download Ollama: https://ollama.ai
#   2. Pull a model:    ollama pull llama3
#   3. Ollama runs automatically in the background
#
# Uncomment and use once Ollama is installed.
# ============================================================

# import requests
# import json

OLLAMA_URL = "http://localhost:11434/api/generate"
DEFAULT_MODEL = "llama3"

SYSTEM_PROMPT = """
You are JARVIS, a personal AI assistant and second brain.
You are helpful, smart, and loyal. You call the user "Bro".
Keep responses concise and direct. If you don't know
something, say so honestly. Remember facts the user tells
you and use them naturally in future conversations.
"""


def get_response(prompt: str, model: str = DEFAULT_MODEL) -> str:
    """
    Send a prompt to the local Ollama instance and return
    the model's response as a plain string.

    Args:
        prompt (str): The user's message.
        model (str): The Ollama model to use. Default: llama3.

    Returns:
        str: The model's response text.
    """

    # ── Phase 3: uncomment when Ollama is installed ─────────
    # payload = {
    #     "model": model,
    #     "prompt": f"{SYSTEM_PROMPT}\n\nUser: {prompt}\nJARVIS:",
    #     "stream": False,
    # }
    # try:
    #     response = requests.post(OLLAMA_URL, json=payload, timeout=30)
    #     response.raise_for_status()
    #     data = response.json()
    #     return data.get("response", "No response received, Bro.")
    # except requests.exceptions.ConnectionError:
    #     return "Can't reach Ollama, Bro. Is it running?"
    # except Exception as e:
    #     return f"Something went wrong, Bro: {str(e)}"
    # ────────────────────────────────────────────────────────

    return "Ollama not connected yet, Bro. Phase 3 incoming."


def is_ollama_running() -> bool:
    """
    Quick health check — returns True if Ollama
    is reachable on localhost.
    """

    # ── Phase 3: uncomment ──────────────────────────────────
    # try:
    #     r = requests.get("http://localhost:11434", timeout=3)
    #     return r.status_code == 200
    # except Exception:
    #     return False
    # ────────────────────────────────────────────────────────

    return False
