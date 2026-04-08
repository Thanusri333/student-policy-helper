import os
import streamlit as st

from extract import extract_text_from_pdfs
from preprocess import clean_text, chunk_text
from retrieve import build_faiss_index, load_faiss_index, retrieve_relevant_chunks
from generate import generate_answer

st.set_page_config(page_title="Student Policy Helper")
st.title("Student Policy Helper")
st.write("Ask questions from UTA policy documents using FAISS-based retrieval.")

uploaded_files = st.file_uploader(
    "Upload PDF files",
    type=["pdf"],
    accept_multiple_files=True
)

if uploaded_files:
    if st.button("Process Documents"):
        with st.spinner("Extracting and indexing documents..."):
            raw_text = extract_text_from_pdfs(uploaded_files)
            cleaned_text = clean_text(raw_text)
            chunks = chunk_text(cleaned_text, chunk_size=500, chunk_overlap=50)
            build_faiss_index(chunks)
        st.success("Documents processed and FAISS index created.")

question = st.text_input("Enter your question")

if question:
    if os.path.exists("faiss_index"):
        vector_store = load_faiss_index()
        relevant_chunks = retrieve_relevant_chunks(question, vector_store, top_k=3)
        answer = generate_answer(question, relevant_chunks)

        st.subheader("Answer")
        st.write(answer)

        st.subheader("Retrieved Context")
        for i, chunk in enumerate(relevant_chunks, 1):
            st.write(f"**Chunk {i}:** {chunk[:700]}...")
    else:
        st.warning("Please upload and process the documents first.")