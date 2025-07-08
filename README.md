# Medical AI Chat Support System (RAG)

A full-stack AI-powered chatbot built using:
- FastAPI backend with dual-path Retrieval-Augmented Generation (RAG)
- [Ollama](https://ollama.com/) to run LLaMA3 locally or run it online using online LLM API (default Deepseek-chat)
- Vite-based frontend (Vue)
- FAISS + BGE Embeddings for semantic search
- Mock user health data + medical knowledge base for personalized responses

✅ This project includes automated testing with `pytest`, code linting with `flake8`, and formatting checks using `black`, integrated via GitHub Actions CI.

---

## 1. Prerequisites

make sure to copy .env.example to the created .env file before running docker:

```bash
cp .env.example .env
```

.env.example:

USE_ONLINE_LLM=true

LLM_URL=http://ollama:11434/api/chat

LLM_API_KEY=your_api_key_here


if wanting to host the LLM locally, change USE_ONLINE_LLM to false. The program will serve llama3 locally with Ollama.

if wanting to host the LLM online, change "your_api_key_here" with your online LLM API (currently only supports DeepSeek-chat API)



Make sure the following are installed:

- [Docker](https://docs.docker.com/get-docker/)
- [Ollama](https://ollama.com/download) (only if serving the LLM locally)

And make sure you run this to build the FAISS index:

build-index:

	python scripts/populate_embeddings.py

with:
```bash
make build-index
```

---

## 2. Configuration (Switch between Local and Online LLM)

This project supports two LLM inference modes:
 1. Local mode: runs llama3 model via Ollama locally. Default (USE_ONLINE_LLM=false).
 2. Online mode: uses online API (deepseek by default), to enable, Set USE_ONLINE_LLM=true.
---


1. Pull or Run LLaMA3 Model with Ollama

Before launching the full stack, ensure the model is pulled:

```bash
ollama pull llama3
# or to launch immediately:
ollama run llama3
```
Or
2. Update the .env or docker-compose.yml:

USE_ONLINE_LLM=true
DEEPSEEK_API_KEY=your-api-key-here

to switch to online mode by setting USE_ONLINE_LLM=true.

## 3. Build and Launch Full Stack via Docker Compose
From the root of the project:

```bash
docker-compose up --build
```

Once launched, access the services at:

 Frontend: http://localhost:5173

 Backend API: http://localhost:8000

 Ollama API: http://localhost:11435

---
## 4. Test the Chat API
Test the /ask endpoint:

```bash
curl -X POST http://localhost:8000/ask \
  -H "Content-Type: application/json" \
  -d '{
    "user_id": "test_user",
    "query": "What is hypertension?",
    "history": []
  }'
```

Expected Response:
```bash
{
  "answer": "Hypertension, also known as high blood pressure, is..."
}
```

---

## 5. Development: Serve Components Individually

If you want to run backend and frontend separately for development:

Backend (FastAPI):

```bash
uvicorn app.main:app --reload
```
Access at: http://localhost:8000



Frontend (Vite):
```bash
cd frontend
npm install
npm run dev
```

Access at: http://localhost:5173

---

## 6. Deployment

Currently configured for local use.


## 7. Author
Yongzhen "Michael" Zhang, MSCS student at Northeastern University

Personal Email: zhangyongzhen99@gmail.com

GitHub: https://github.com/yongzhenzh

LinkedIn: https://www.linkedin.com/in/yongzhen-zhang-291557239/

---

## 8. Testing & Code Quality

Includes full test coverage with **Pytest**, and code linting using **Flake8** and **Black** for consistent style and quality.

To run tests:

```bash
pytest
```

To check linting:

```bash
flake8 .
black --check .
```

To auto-format with Black:

```bash
black .
```