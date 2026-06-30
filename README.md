<div align="center">

# 🧠 JARVIS

### A self-hosted personal AI assistant, built from scratch.

*Inspired by Iron Man. Powered by Python, Django, and a local AI brain.*

[![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-6.0-092E20?logo=django&logoColor=white)](https://www.djangoproject.com/)
[![Ollama](https://img.shields.io/badge/AI-Ollama%20(Local)-black?logo=ollama&logoColor=white)](https://ollama.com/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Active%20Development-yellow)]()

</div>

---

## ✨ What is JARVIS?

JARVIS is a personal AI assistant that runs **entirely on your own machine** — no cloud subscriptions, no sending your conversations to a third party. It's built around a custom Django backend, a hand-designed dark-themed chat interface (codename: **Odysseus Navigator**), and a local large language model powered by [Ollama](https://ollama.com/).

This project started as a simple question: *what would it take to actually build a JARVIS?* A few weeks of late-night debugging, Git mishaps, and architecture rewrites later — it's alive, it talks back, and it's fully open source.

---

## 🚀 Features (so far)

- 🖥️ **Custom chat interface** — dark theme, smooth animations, built from scratch (no UI templates)
- 🧠 **Local AI brain** — powered by Ollama, fully private, runs offline
- 🗣️ **Voice output (TTS)** — JARVIS speaks its responses back to you
- 🛡️ **Safety layer** — input filtering before any request reaches the AI
- 🗂️ **Clean modular architecture** — AI logic, Django app, and frontend are fully decoupled
- 💾 **Conversation memory** *(in progress)* — SQLite-backed chat history

---

## 🏗️ Architecture

```
JARVIS/
├── core/                  # Django project configuration
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py / asgi.py
│
├── assistant/             # Django app — views, API routes, models
│   ├── views.py
│   ├── urls.py
│   └── migrations/
│
├── brain/                 # AI logic layer (framework-agnostic)
│   ├── core.py            # Central message router
│   ├── ai.py               # Ollama integration
│   ├── voice.py            # Text-to-speech
│   ├── desktop.py          # Desktop automation commands
│   ├── safety.py           # Input safety checks
│   └── search.py           # Web search (planned)
│
├── frontend/               # UI layer
│   ├── templates/
│   └── static/
│
├── manage.py
└── requirements.txt
```

**Why this structure?** The `brain/` package contains zero Django imports — it's pure Python, meaning the AI logic can be tested, reused, or swapped out independently of the web framework wrapped around it.

---

## 🛣️ Roadmap

JARVIS is being built in 7 phases:

| Phase | Status | Description |
|-------|--------|-------------|
| 1 | ✅ Done | Django backend + custom chat UI (Odysseus Navigator) |
| 2 | 🔄 In Progress | SQLite conversation memory |
| 3 | ✅ Done | Local AI integration via Ollama |
| 4 | ⏳ Planned | Memory-aware context injection |
| 5 | ⏳ Planned | Desktop automation commands |
| 6 | ⏳ Planned | Web search integration |
| 7 | ⏳ Planned | Voice input (Whisper) + voice wake word |

---

## ⚙️ Installation

### Prerequisites

- Python 3.11+
- [Ollama](https://ollama.com/download) installed and running
- Git

### 1. Clone the repository

```bash
git clone https://github.com/Mano11x/JARVIS.git
cd JARVIS
```

### 2. Create and activate a virtual environment

**Windows (PowerShell):**
```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

**macOS / Linux:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Pull a local AI model via Ollama

```bash
ollama pull llama3.2:1b
```

*(You can substitute any model you prefer — e.g. `mistral` for higher quality at the cost of speed. Update the model name in `brain/core.py` if you switch.)*

### 5. Run database migrations

```bash
python manage.py migrate
```

### 6. Start the server

```bash
python manage.py runserver
```

Open **http://127.0.0.1:8000/assistant/** in your browser — JARVIS should greet you.

---

## 🔑 Environment Variables

Create a `.env` file in the project root if you plan to extend JARVIS with cloud AI fallback or other API integrations:

```env
OPENAI_API_KEY=your_key_here       # optional, for cloud fallback
OPENAI_MODEL=gpt-3.5-turbo          # optional
```

> ⚠️ Never commit your `.env` file — it's already excluded via `.gitignore`.

---

## 🧰 Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Django 6.0 |
| AI Engine | Ollama (local LLM inference) |
| Text-to-Speech | pyttsx3 |
| Database | SQLite |
| Frontend | HTML / CSS / vanilla JS |
| Language | Python 3.13 |

---

## 🤝 Contributing

This is a personal learning project, but feedback, issues, and PRs are welcome. If you spot a bug or have an idea, feel free to open an issue.

---

## 📬 Contact

**Mano** — [GitHub @Mano11x](https://github.com/Mano11x) · manomaghi6@gmail.com

---

<div align="center">

*Built over 2-4 weeks of nights and weekends, one debugging session at a time.*

</div>
