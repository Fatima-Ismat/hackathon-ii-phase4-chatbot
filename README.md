# Hackathon II – Phase 3  
## AI-Powered Todo Chatbot (Agent + MCP Tools)

This project is a **Phase-3 compliant, agent-based Todo chatbot** built for **Hackathon II**.  
It uses **FastAPI**, **OpenAI Agents SDK**, and **official MCP tools** to manage tasks via **natural language**, with **persistent conversation memory** backed by **Neon PostgreSQL**.

The backend is **Dockerized** and deployed on **Hugging Face Spaces**, while the frontend is built with **Next.js (App Router)** and deployed on **Vercel**.

---

## 🚀 Features (Phase-3 Scope)

- 🤖 **Agent-based chatbot** (NO regex / rule-based logic)
- 🧠 **OpenAI Agents SDK** for reasoning + tool orchestration
- 🧰 **Official MCP tools only** for all task operations  
  (no direct DB access from agent)
- 💬 **Natural language commands**:
  - `add <task>`
  - `list`
  - `complete <task_id>`
  - `delete <task_id>`
  - `stats`
- 🗂️ **Persistent conversation memory**
- 🔁 **conversation_id preserved** across messages
- 🗄️ **Neon PostgreSQL** for:
  - Tasks
  - Conversations
  - Messages
- 🔐 **Secure environment variables**
- 🐳 **Dockerized backend** for production
- 🎨 **Premium UI dashboard + floating AI chatbot**
- 🧩 **Custom ChatKit-style UI** (App Router compatible)

---

## 🧱 Architecture Overview

Frontend (Next.js App Router)
│
│ Floating AI Chatbot Widget
│ └── Calls /api/{user_id}/chat
│
Backend (FastAPI on Hugging Face)
│
├── OpenAI Agent (Agents SDK)
│ ├── MCP Tool: add_task
│ ├── MCP Tool: list_tasks
│ ├── MCP Tool: complete_task
│ ├── MCP Tool: delete_task
│ └── MCP Tool: stats
│
└── Neon PostgreSQL
├── tasks
├── conversations
└── messages


---

## 🖥️ Frontend

- **Framework**: Next.js (App Router)
- **UI**:
  - Sign-in welcome screen
  - Premium Todo dashboard
  - Floating **AI button** → opens chatbot
- **Auth**:
  - Demo auth via `localStorage` (`todo_user_id`)
- **Deployment**: Vercel

### Frontend Environment Variable

```env
NEXT_PUBLIC_API_BASE=https://<your-huggingface-space>.hf.space

⚙️ Backend

    Framework: FastAPI

    Agent: OpenAI Agents SDK

    Tools: MCP (Model Context Protocol)

    Database: Neon PostgreSQL

    Deployment: Hugging Face Spaces

    Container: Docker

Backend Environment Variables

OPENAI_API_KEY=sk-****
DATABASE_URL=postgresql+asyncpg://...

🧪 Example Chat Commands

add buy milk
list
complete 1
delete 2
stats

🧠 Conversation Memory (Phase-3 Requirement)

    Each chat creates or reuses a conversation_id

    The same conversation continues across messages

    Stored in Neon PostgreSQL

    Enables context-aware responses

🧑‍⚖️ For Judges (Phase-3 Checklist)

This project fully satisfies Hackathon II – Phase 3 requirements:

✅ Agent-based system (no regex, no hardcoded rules)
✅ OpenAI Agents SDK used
✅ All task actions via MCP tools only
✅ Persistent conversation memory implemented
✅ conversation_id maintained across turns
✅ Database-backed (Neon PostgreSQL)
✅ Deployed backend (Hugging Face)
✅ Deployed frontend (Vercel)
✅ Clean UI + integrated chatbot
✅ Dockerized backend for production

    ⚠️ Note on ChatKit
    Official ChatKit UI could not be used due to Next.js App Router incompatibility.
    A custom ChatKit-style UI was implemented instead, while keeping agent + MCP logic fully compliant.

📦 Repository Structure

hackathon-ii-phase3-chatbot/
│
├── backend/
│   ├── app/
│   │   ├── agents/
│   │   ├── mcp_tools/
│   │   ├── models/
│   │   ├── routers/
│   │   └── main.py
│   ├── Dockerfile
│   └── requirements.txt
│
├── frontend/
│   ├── app/
│   │   ├── page.tsx
│   │   ├── signin/
│   │   └── dashboard/
│   ├── components/
│   │   └── ChatbotWidget.tsx
│   └── lib/
│
└── README.md

🚀 Live Deployments

    Frontend (Vercel)
    👉 https://phase3-ismatfatima-ai-todo.vercel.app

    Backend (Hugging Face Spaces)
    👉 https://ismat110-hackathon-ii-phase3-chatbot.hf.space

🏁 Final Notes

This project demonstrates a production-ready, agent-driven AI system with:

    Clear separation of concerns

    Tool-only task execution

    Persistent memory

    Real deployment

It is fully aligned with Hackathon II – Phase 3 objectives.
