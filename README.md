# FRIDAY — Voice AI Assistant

A voice-controlled AI assistant inspired by Tony Stark's F.R.I.D.A.Y., built from scratch using function calling, real-time news retrieval, and speech-to-speech interaction.

> Built in public by **Dhani Baksh (Bilal)** — self-taught backend developer from Pakistan 🇵🇰

---

## 🎥 Demo

*(embed your reel/video link here)*

---

## 🧠 What it does

Talk to FRIDAY naturally — ask it who built it, ask it for the latest world news, and it responds back in voice, briefing you like a personal aide. It can also pull up a live world news dashboard on command.

- 🎤 **Voice input** — speak your command, no typing needed
- 🌍 **Live world news** — fetches and explains current headlines, not just raw text
- 🗺️ **Dashboard trigger** — opens a real-time world monitor visualization
- 🔊 **Voice output** — responds back in natural speech
- 🤖 **Function calling** — the LLM decides which tool to call based on what you ask

---

## 🛠️ Tech Stack

| Layer | Tool |
|---|---|
| Core LLM / reasoning | **Groq API** (Llama 3.3 70B) |
| Function calling | Groq's native tool-use |
| Backend | **FastAPI** |
| Speech-to-Text | **Sarvam AI** |
| Text-to-Speech | **Edge TTS** |
| News data | **NewsData.io** |
| Audio I/O | `sounddevice`, `scipy`, `soundfile` |

---

## ⚙️ How it works

```
🎤 Voice input
     │
     ▼
Sarvam STT  →  transcribes speech to text
     │
     ▼
Groq (Llama 3.3)  →  decides: reply directly, or call a tool
     │
     ├──► tell_world_news()  →  fetches headlines (NewsData.io) + opens live dashboard
     │
     ▼
Groq explains the result in natural language
     │
     ▼
Edge TTS  →  converts response to speech
     │
     ▼
🔊 Spoken back to the user
```

---

## 📂 Project Structure

```
friday-news-assistant/
├── main.py                 # FastAPI entry point
├── config.py                # Loads API keys from .env
├── requirements.txt
│
├── tools/
│   └── news_tools.py          # News fetching + dashboard trigger (the tool)
│
├── core/
│   └── agent.py                 # Groq client, function calling, system prompt
│
└── voice/
    └── voice_handler.py          # Mic recording, STT, TTS, playback
```

---

## 🚀 Setup

```bash
git clone https://github.com/<your-username>/friday-news-assistant.git
cd friday-news-assistant
pip install -r requirements.txt
```

Create a `.env` file:
```
GROQ_API_KEY=your_key_here
NEWS_DATA_API_KEY=your_key_here
SARVAM_API_KEY=your_key_here
```

Run the voice assistant:
```bash
python -m voice.voice_handler
```

Or run the text-based API:
```bash
uvicorn main:app --reload
```

---

## 🔮 What's next

- Web-based chat UI (text + browser mic input)
- Deployment with browser-native voice capture
- Additional tools (finance news, weather, reminders)
- Combined AI customer support API (in progress)

---

## 👤 About

Built by **Dhani Baksh (Bilal)**, a self-taught backend developer specializing in FastAPI, PostgreSQL, and AI integration engineering.

- GitHub: [dhanibaksh777-byte](https://github.com/dhanibaksh777-byte)
- Portfolio: *(add your portfolio link)*
