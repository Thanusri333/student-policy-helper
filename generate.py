"""Generate concise answers from retrieved document chunks."""

import re


def generate_answer(question, relevant_chunks):
    """Return a short answer based on the most relevant retrieved text."""
    if not relevant_chunks:
        return "I could not find that information in the uploaded documents."

    best_chunk = relevant_chunks[0]
    sentences = re.split(r"(?<=[.!?])\s+", best_chunk)
    question_words = [
        word.lower() for word in question.split()
        if len(word) > 3
    ]

    matched_sentences = []
    for sentence in sentences:
        sentence_lower = sentence.lower()
        if any(word in sentence_lower for word in question_words):
            matched_sentences.append(sentence.strip())

    if matched_sentences:
        return " ".join(matched_sentences[:2])

    return " ".join(sentences[:2]).strip()
