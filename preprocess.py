"""Clean and split extracted document text into chunks."""

import re


def clean_text(text):
    """Normalize whitespace in extracted text."""
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def chunk_text(text, chunk_size=500, chunk_overlap=50):
    """Split text into overlapping word-based chunks."""
    words = text.split()
    chunks = []
    step = chunk_size - chunk_overlap

    for i in range(0, len(words), step):
        chunk = " ".join(words[i:i + chunk_size])
        if chunk.strip():
            chunks.append(chunk)

    return chunks