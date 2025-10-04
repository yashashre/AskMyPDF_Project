from pdf_load import extract_text, chunk_text
from vectordb import add_chunks
from rag_pipeline import ask_rag

PDF_PATH = r"C:\Users\Admin\PycharmProjects\pythonProject\AskMyPDF_Project\bajaj_finserv_amc_factsheet_september_2025.pdf"

# Step 1: Load and chunk PDF
print("📄 Extracting text from PDF...")
pdf_text = extract_text(PDF_PATH)
chunks = chunk_text(pdf_text)

# Step 2: Add chunks to vector DB
print("🔍 Creating embeddings and storing chunks...")
add_chunks(chunks)

# Step 3: Start chatbot loop
print("✅ PDF loaded! You can now ask questions.")
while True:
    q = input("\nAsk a question (or type 'exit'): ")
    if q.lower() == "exit":
        print("👋 Exiting chatbot...")
        break
    print("Answer:", ask_rag(q))