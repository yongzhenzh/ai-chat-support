"""
vector_store.py

Handles vector similarity search using FAISS.

- Loads precomputed document embeddings and FAISS index
- Encodes incoming queries using SentenceTransformer
- Performs top-k similarity search on FAISS index
- Returns relevant document texts as context for retrieval-augmented generation (RAG)

"""

import faiss
import pickle
import numpy as np
from sentence_transformers import SentenceTransformer
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
INDEX_PATH = os.path.join(BASE_DIR, "data", "faiss_index.bin")
DOCS_PATH = os.path.join(BASE_DIR, "data", "docs.pkl")


model = SentenceTransformer("BAAI/bge-small-en")
index = faiss.read_index(INDEX_PATH)
with open("data/docs.pkl", "rb") as f:
    docs = pickle.load(f)


def search_similar_docs(query: str, top_k: int = 3):
    """
    Perform vector similarity search on the FAISS index.

    Args:
        query (str): The query string to search for.
        top_k (int): Number of top results to return.

    Returns:
        list: List of relevant document texts.
    """
    # Check if the query is empty
    if not query.strip():
        return []
    # format the query for BGE model
    formatted_query = f"Represent this sentence for retrieval: {query}"

    # Encode the query
    query_embedding = model.encode([formatted_query], show_progress_bar=True)
    query_embedding = np.array(
        query_embedding.astype(np.float32)
    )  # Convert to float32 for FAISS compatibility

    # Perform search
    distances, indices = index.search(query_embedding, top_k)

    # Retrieve corresponding documents
    results = [docs[i] for i in indices[0]]

    return results
