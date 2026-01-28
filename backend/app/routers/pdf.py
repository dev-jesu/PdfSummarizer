from fastapi import APIRouter, UploadFile, File, HTTPException

from app.services.pdf_reader import extract_text_from_pdf
from app.services.txt_reader import extract_text_from_txt
from app.services.summarizer import extract_concepts

router = APIRouter(
    prefix="/api",
    tags=["Summarization"]
)


@router.post("/summarize")
async def summarize_file(file: UploadFile = File(...)):
    if not file.filename:
        raise HTTPException(status_code=400, detail="No file uploaded")

    filename = file.filename.lower()

    if filename.endswith(".pdf"):
        document = extract_text_from_pdf(file.file)
    elif filename.endswith(".txt"):
        document = extract_text_from_txt(file.file)
    else:
        raise HTTPException(
            status_code=400,
            detail="Only PDF and TXT files are supported"
        )

    if not document.strip():
        raise HTTPException(
            status_code=400,
            detail="No readable content found"
        )

    result = extract_concepts(document)

    return {
        "status": "success",
        "file_name": file.filename,
        "summary": result
    }
