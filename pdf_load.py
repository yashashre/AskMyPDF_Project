from pypdf import PdfReader

pdf_path = r"C:\Users\Admin\PycharmProjects\pythonProject\AskMyPDF_Project\bajaj_finserv_amc_factsheet_september_2025.pdf"


def extract_text(pdf_path):
    """Extract all text from a PDF file"""
    reader = PdfReader(pdf_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
    return text

def chunk_text(text, chunk_size=1000, overlap=200):
    """Split text into overlapping chunks for embeddings"""
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start = end - overlap
    return chunks