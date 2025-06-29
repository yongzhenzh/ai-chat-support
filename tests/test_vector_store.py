"""
ai-chat-support/tests/test_vector_store.py
This module contains unit tests for the vector store search functionality.
It tests the search_similar_docs function to ensure it returns relevant results based on user queries
and handles edge cases like empty queries.
"""

from app.services.vector_store import search_similar_docs


def test_search_similar_docs_basic_query():
    query = "What are the symptoms of diabetes?"
    top_k = 3
    results = search_similar_docs(query, top_k)

    assert len(results) <= top_k
    assert isinstance(results, list)
    assert all(isinstance(doc, str) for doc in results)
    assert "diabetes" in results[0].lower()


def test_search_similar_docs_empty_query():
    query = ""
    results = search_similar_docs(query, top_k=3)

    assert len(results) == 0  # No results expected for empty query
    assert isinstance(results, list)
    assert all(isinstance(doc, str) for doc in results)
