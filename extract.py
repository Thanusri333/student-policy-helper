"""Extract text from uploaded PDF files."""

import pdfplumber


def extract_text_from_pdfs(uploaded_files):
    """Extract and combine text from multiple uploaded PDFs."""
    all_text = ""

    for uploaded_file in uploaded_files:
        with pdfplumber.open(uploaded_file) as pdf:
            for page in pdf.pages:
                text = page.extract_text()
                if text:
                    all_text += text + "\n"

    return all_text