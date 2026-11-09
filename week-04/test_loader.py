
from src.document_loader import load_pdf

pdf_path = "data/documents/sample.pdf"

text = load_pdf(pdf_path)

print("PDF loaded successfully!")
print("Extracted characters:", len(text))
print("\nFirst 500 characters:\n")
print(text[:500])
