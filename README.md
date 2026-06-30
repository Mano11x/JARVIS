# JARVIS — Personal AI Assistant

> *"Not all those who wander are lost. But JARVIS always knows where you are."*

A personal AI second brain built with Python and Django. JARVIS is designed to grow phase by phase — from a chat UI today, to a fully autonomous desktop assistant with voice, memory, and internet access.

---

## Vision

JARVIS is not just a chatbot. The goal is a personal AI operating system:

```
You: Open my editor.
JARVIS: Opening VS Code, Bro.

You: Remember my favorite editor is VS Code.
JARVIS: Understood Bro. I'll remember that.

You: What is my favorite editor?
JARVIS: Your favorite editor is VS Code, Bro.
```

---

## Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python 3.13, Django 6.x |
| Database | SQLite |
| Frontend | HTML, CSS, JavaScript |
| AI Engine | Ollama (Phase 3) |
| Voice Input | Whisper STT (Phase 7) |
| Voice Output | Edge-TTS (Phase 7) |

---

## Project Structure

```
jarvis/
├── assistant/          # Django app — views, models, routes
│   ├── migrations/
│   ├── models.py       # Conversation & Memory models
│   ├── views.py        # Chat view + API endpoints
│   └── urls.py
│
├── brain/              # JARVIS intelligence modules
│   ├── __init__.py
│   ├── core.py         # Central router — dispatches all requests
│   ├── ai.py           # Ollama LLM integration (Phase 3)
│   ├── safety.py       # Input/output safety filtering
│   ├── search.py       # Web search + file search (Phase 6)
│   ├── voice.py        # Whisper STT + Edge-TTS (Phase 7)
│   └── desktop.py      # Desktop automation (Phase 5)
│
├── core/               # Django project config
│   ├── settings.py
│   └── urls.py
│
|
|
├── jarvis_frountend
|   ├── static/
│   |   ├── css/style.css   # Odysseus dark theme
│   |   └── js/chat.js      # Chat UI logic
│   |
|   ├── templates/
│       └── chat.html       # Main chat interface
│
├── manage.py
├── README.md
└── requirements.txt
```

---

## Setup

```bash
# 1. Clone and navigate
cd jarvis

# 2. Activate virtual environment (Windows)
venv\Scripts\Activate.ps1

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run migrations
python manage.py migrate

# 5. Start server
python manage.py runserver
```

Visit `http://127.0.0.1:8000`

---

## Roadmap

### Phase 1 — Chat UI (done)
- [x] Django project setup
- [x] Routing and template engine configured
- [x] Dark Odysseus-themed chat interface
- [x] Bronze star idle/thinking animation
- [x] Responsive layout

### Phase 2 — Memory & Storage (next)
- [ ] `Conversation` model — persist chat history in SQLite
- [ ] `Memory` model — store key facts about the user
- [ ] Chat history visible in sidebar
- [ ] JARVIS reads memory before each response

### Phase 3 — Local AI (Ollama)
- [ ] Install and run Ollama locally
- [ ] `brain/ai.py` — send prompts, receive responses
- [ ] Stream responses token by token
- [ ] Choose model (llama3, mistral, etc.)

### Phase 4 — Long-term Memory
- [ ] JARVIS extracts facts from conversations
- [ ] Stores preferences, names, habits
- [ ] Memory retrieval injected into context

### Phase 5 — Desktop Automation
- [ ] Open applications by name
- [ ] Open folders and files
- [ ] Search local files
- [ ] `brain/desktop.py`

### Phase 6 — Internet Access
- [ ] Web search via DuckDuckGo or SerpAPI
- [ ] Read and summarise web pages
- [ ] Draft and send emails
- [ ] `brain/search.py`

### Phase 7 — Voice
- [ ] Wake word detection
- [ ] Whisper for speech-to-text
- [ ] Edge-TTS for text-to-speech
- [ ] Fully hands-free operation
- [ ] `brain/voice.py`

---

## Design Language

The UI follows an **Odysseus / Navigator** aesthetic:

- **Void background** — near-black `#0A0D14`
- **Bronze accents** — `#C99A4B` (the guide star)
- **Cinzel serif** — for the JARVIS wordmark only
- **Manrope sans** — for all chat content
- **JetBrains Mono** — for status and metadata

The bronze star pulses slowly at idle and quickens when JARVIS is thinking.

---

## Contributing

This is a personal project. If you fork it, make it yours.

---

*Built by Mano — Chennai, India*
