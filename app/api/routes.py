"""
This module defines the API routes for the AI chat support application.
It includes an endpoint for asking questions, which processes the request and generates an answer using the RAG pipeline.
"""

from fastapi import APIRouter, Request
from app.models.schemas import AskResponse
from app.services.rag_pipeline import generate_answer
from typing import List, Dict
from pydantic import BaseModel

router = APIRouter()


class AskRequest(BaseModel):
    user_id: str
    query: str
    history: List[Dict[str, str]] = []


@router.post("/ask", response_model=AskResponse)
def ask_question(request_body: AskRequest, request: Request):
    print(">>> /ask endpoint hit with:", request_body.dict())
    answer = generate_answer(
        request_body.user_id, request_body.query, request_body.history
    )
    return AskResponse(answer=answer)
