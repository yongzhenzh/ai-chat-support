"""
This script populates a FAISS index with embeddings of medical knowledge documents.
It uses the BGE model from SentenceTransformers to generate embeddings and saves the index and documents
for later retrieval.

"""


import os
from sentence_transformers import SentenceTransformer
import faiss
import pickle

DATA_DIR = "data/medical_knowledge"
INDEX_PATH = "data/faiss_index.bin"
DOCS_PATH = "data/docs.pkl"


# Load the embedding model
model = SentenceTransformer("BAAI/bge-small-en")

# Load documents
docs = []
for filename in os.listdir(DATA_DIR):
    if filename.endswith(".txt"):
        with open(os.path.join(DATA_DIR, filename), "r", encoding="utf-8") as f:
            docs.append(f.read())
# format documents for BGE model
formatted_docs = [f"Represent this sentence for retrieval: {doc}" for doc in docs]

# embedding documents
embeddings = model.encode(formatted_docs, show_progress_bar=True)
import numpy as np
embeddings = np.array(embeddings.astype(np.float32))  # Convert to float32 for FAISS compatibility

# store in FAISS index

dim = embeddings[0].shape[0]
index = faiss.IndexFlatL2(dim)
index.add(embeddings)


# save the index and documents
faiss.write_index(index, INDEX_PATH)
with open(DOCS_PATH, "wb") as f:
    pickle.dump(docs, f)

print(f"Index saved to {INDEX_PATH}")
print(f"Documents saved to {DOCS_PATH}")
print(f"Total documents processed: {len(docs)}")
print(f"Embedding dimension: {dim}")




