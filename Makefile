# Makefile for AI Chat Support System

# Run this to build the FAISS index
build-index:
	python scripts/populate_embeddings.py

# Run the backend locally
run-backend:
	uvicorn app.main:app --reload

# Run the frontend locally (assumes you're in the root dir and Vite is used)
run-frontend:
	cd frontend && npm run dev

# Launch full stack using Docker Compose
up:
	docker-compose up --build

# Stop all containers
down:
	docker-compose down

# Rebuild and restart containers
rebuild:
	docker-compose down && docker-compose up --build

# Show running containers
ps:
	docker ps

# Tail logs from backend
logs-backend:
	docker logs -f ai-chat-backend

# Tail logs from frontend
logs-frontend:
	docker logs -f ai-chat-frontend

# Tail logs from Ollama
logs-ollama:
	docker logs -f ollama
