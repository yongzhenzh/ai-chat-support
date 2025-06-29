# AI Chat Support System

A full-stack AI-powered chatbot built using:
- FastAPI backend with dual-path Retrieval-Augmented Generation (RAG)
- [Ollama](https://ollama.com/) to run LLaMA3 locally
- Vite-based frontend (React or Vue)
- FAISS + BGE Embeddings for semantic search
- Mock user health data + medical knowledge base for personalized responses

✅ This project includes automated testing with `pytest`, code linting with `flake8`, and formatting checks using `black`, integrated via GitHub Actions CI.

---

## 1. Prerequisites

Make sure the following are installed:

- [Docker](https://docs.docker.com/get-docker/)
- [Ollama](https://ollama.com/download)

And make sure you run this to build the FAISS index:

build-index:

	python scripts/populate_embeddings.py

with:
```bash
make build-index
```

---

## 2. Pull or Run LLaMA3 Model with Ollama

Before launching the full stack, ensure the model is pulled:

```bash
ollama pull llama3
# or to launch immediately:
ollama run llama3
```


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
Yongzhen Zhang

GitHub: https://github.com/yongzhenzh

LinkedIn: https://www.linkedin.com/in/yongzhen-zhang-291557239/

---

## 8. Testing & Code Quality

✅ Includes full test coverage with **Pytest**, and code linting using **Flake8** and **Black** for consistent style and quality.

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