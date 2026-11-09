
from src.document_loader import load_pdf
from src.text_splitter import split_text

# Load our PDF
pdf_text = load_pdf("data/documents/sample.pdf")

# Split the extracted text
chunks = split_text(
    pdf_text,
    chunk_size=1000,
    overlap=200
)

print("Document successfully split!")
print("Total characters:", len(pdf_text))
print("Total chunks:", len(chunks))

for index, chunk in enumerate(chunks[:3], start=1):
    print(f"\n--- Chunk {index} ---")
    print(chunk[:200])
