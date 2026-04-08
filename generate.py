"""Generate final answers for the Student Policy Helper using OpenAI."""

import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def generate_answer(question, relevant_chunks):
    """Generate an answer using retrieved document chunks as context."""
    context = "\n\n".join(relevant_chunks)

    prompt = f"""
You are a university policy assistant.
Answer the question only using the context below.
If the answer is not in the context, say:
"I could not find that information in the uploaded documents."

Context:
{context}

Question:
{question}
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": (
                    "You answer questions using university "
                    "policy documents only."
                ),
            },
            {"role": "user", "content": prompt},
        ],
        temperature=0,
    )

    return response.choices[0].message.content