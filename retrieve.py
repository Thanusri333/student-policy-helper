"""Build and load a FAISS index using local HuggingFace embeddings."""

from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS


def get_embeddings():
    """Return the local embedding model used for FAISS indexing."""
    return HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )


def build_faiss_index(chunks, save_path="faiss_index"):
    """Create and save a FAISS index from text chunks."""
    embeddings = get_embeddings()
    vector_store = FAISS.from_texts(chunks, embedding=embeddings)
    vector_store.save_local(save_path)
    return vector_store


def load_faiss_index(save_path="faiss_index"):
    """Load an existing FAISS index from disk."""
    embeddings = get_embeddings()
    vector_store = FAISS.load_local(
        save_path,
        embeddings,
        allow_dangerous_deserialization=True,
    )
    return vector_store


def retrieve_relevant_chunks(query, vector_store, top_k=3):
    """Retrieve the most relevant chunks for a query."""
    docs = vector_store.similarity_search(query, k=top_k)
    return [doc.page_content for doc in docs]
