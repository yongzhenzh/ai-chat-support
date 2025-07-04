"""
Test cases for the RAG pipeline in the AI Chat Support application.
This module contains unit tests for the functions that build context and generate answers using the RAG pipeline.
It uses pytest and monkeypatching to mock external dependencies like the LLM call.
"""

from _pytest.monkeypatch import MonkeyPatch
from app.services.rag_pipeline import build_combined_context, generate_answer


def test_build_combined_context():
    """
    Test the RAG pipeline by building a combined context from user data and query.
    """
    user_id = "u001"
    query = "What are the risks of high blood pressure?"

    context = build_combined_context(user_id, query)

    assert "high blood pressure" in context.lower()
    assert "User health information" in context
    assert "relevant medical knowledge" in context
    assert "User question" in context
    assert query in context


def test_generate_answer(monkeypatch: MonkeyPatch):
    """
    Test the RAG pipeline by generating an answer using a mocked LLM call.
    """

    def mock_llm_call(messages: list) -> str:
        user_msg = next(
            (m["content"] for m in messages if m["role"] == "user"), "No user message"
        )
        return "Mocked answer based on the provided context: " + user_msg

    # Mock the call_local_llm function to return a fixed response
    # This avoids making an actual HTTP request to the LLM API during testing
    monkeypatch.setattr("app.services.rag_pipeline.call_llm", mock_llm_call)

    query = "What are the risks of high blood pressure?"
    user_id = "u001"
    answer = generate_answer(user_id, query)

    assert "Mocked answer based on the provided context" in answer
