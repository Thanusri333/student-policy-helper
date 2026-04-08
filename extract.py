import pdfplumber

def extract_text_from_pdfs(data):
    all_text = ""

    for uploaded_file in data:
        with pdfplumber.open(uploaded_file) as pdf:
            for page in pdf.pages:
                text = page.extract_text()
                if text:
                    all_text += text + "\n"

    return all_text