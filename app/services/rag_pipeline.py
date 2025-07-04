"""
This module implements a retrieval-augmented generation (RAG) pipeline for an AI chat support system.
It combines user-specific health information with relevant medical knowledge from a vector store to
generate context for answering user queries.

"""

from app.services.vector_store import search_similar_docs
from app.services.get_user_context import get_user_context
from app.services.generator import call_llm


def build_combined_context(user_id: str, query: str, top_k: int = 3) -> str:
    """
    Builds a combined context for retrieval-augmented generation (RAG) by merging user context and relevant documents.

    Args:
        user_id (str): The ID of the user.
        query (str): The query string to search for.
        top_k (int): Number of top results to return from the vector store.

    Returns:
        str: Combined context string.
    """
    user_context = get_user_context(user_id)
    knowledge_results = search_similar_docs(query, top_k)

    formatted_knowledge = "".join(f"- {doc}\n" for doc in knowledge_results)
    context = (
        "You are a helpful AI assistant. Use the following context to answer the user's question. \n"
        f"User health information: \n{user_context}\n\n"
        f"relevant medical knowledge: \n{formatted_knowledge}\n"
        f"User question:\n {query}\n\n"
        "Answer the question based on the above context. If you don't know the answer, say 'I don't know'."
    )
    return context


def generate_answer(
    user_id: str, query: str, history: list = None, top_k: int = 3
) -> str:
    """
    Generates an answer to the user's query by combining user context and relevant medical knowledge.
    """
    if history is None:
        history = []

    user_context = get_user_context(user_id)
    knowledge_results = search_similar_docs(query, top_k)

    formatted_knowledge = "".join(f"- {doc}\n" for doc in knowledge_results)

    system_prompt = (
        "You are a helpful medical assistant.\n"
        f"User health info: {user_context}\n\n"
        f"Relevant medical knowledge:\n{formatted_knowledge}\n"
    )

    messages = (
        [{"role": "system", "content": system_prompt}]
        + history
        + [{"role": "user", "content": query}]
    )
    return call_llm(messages)
