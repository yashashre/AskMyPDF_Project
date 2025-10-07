# pdf_load.py

import pytesseract
from pdf2image import convert_from_path
from PyPDF2 import PdfReader

# For OCR on scanned PDFs
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def extract_text(pdf_path):
    text = ""

    # Try extracting digital text first
    try:
        reader = PdfReader(pdf_path)
        for page in reader.pages:
            if page.extract_text():
                text += page.extract_text() + "\n"
    except:
        pass

    # If no digital text, fallback to OCR
    if not text.strip():
        print("🧠 No digital text found. Using OCR...")
        pages = convert_from_path(pdf_path, dpi=300)
        for i, page in enumerate(pages):
            text += pytesseract.image_to_string(page)
            print(f"OCR processed page {i+1}/{len(pages)}")

    return text

def chunk_text(text, chunk_size=1000, overlap=200):
    """Split text into overlapping chunks"""
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start = end - overlap
    return chunks
