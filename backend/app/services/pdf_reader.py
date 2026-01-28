from PyPDF2 import PdfReader

def extract_text_from_pdf(file) -> str:
    reader = PdfReader(file)
    text_chunks = []

    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text_chunks.append(page_text)

    extracted_text = "\n".join(text_chunks).strip()

    if not extracted_text:
        raise ValueError("No readable text found in PDF")

    return extracted_text
