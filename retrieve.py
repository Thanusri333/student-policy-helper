import os
from dotenv import load_dotenv

from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS

load_dotenv()

def build_faiss_index(chunks, save_path="faiss_index"):
    embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
    vector_store = FAISS.from_texts(chunks, embedding=embeddings)
    vector_store.save_local(save_path)
    return vector_store

def load_faiss_index(save_path="faiss_index"):
    embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
    vector_store = FAISS.load_local(
        save_path,
        embeddings,
        allow_dangerous_deserialization=True
    )
    return vector_store

def retrieve_relevant_chunks(query, vector_store, top_k=3):
    docs = vector_store.similarity_search(query, k=top_k)
    return [doc.page_content for doc in docs]