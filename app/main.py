"""
main.py
FastAPI application entry point for AI Chat Support.
This module initializes the FastAPI app, sets up the embedding model, and includes the API routes.

"""

from fastapi import FastAPI
from sentence_transformers import SentenceTransformer
from app.api.routes import router
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pathlib import Path


app = FastAPI(
    title="AI Chat Support",
    description="LLM powered chatbot using semantic search and RAGs",
    version="0.1.0",
)

# Add CORS middleware to allow cross-origin requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# Serve frontend
# frontend_path = Path(__file__).parent.parent / "frontend-dist"
# app.mount("/", StaticFiles(directory=frontend_path, html=True), name="static")


app.state.embedding_model = SentenceTransformer("BAAI/bge-small-en")
app.include_router(router)
