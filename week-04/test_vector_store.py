
from src.document_loader import load_pdf
from src.text_splitter import split_text
from src.vector_store import store_chunks, collection


# Step 1: Load PDF
pdf_text = load_pdf("data/documents/sample.pdf")

# Step 2: Split PDF text
chunks = split_text(
    pdf_text,
    chunk_size=1000,
    overlap=200
)

# Step 3: Store chunks and embeddings
stored = store_chunks(
    chunks,
    source="sample.pdf"
)

# Step 4: Check database
print("Chunks stored successfully!")
print("Chunks processed:", stored)
print("Total records in ChromaDB:", collection.count())

# Step 5: Inspect one stored record
result = collection.get(
    ids=["sample.pdf_chunk_0"],
    include=["documents", "metadatas"]
)

print("\nFirst stored document:")
print(result["documents"][0][:300])

print("\nMetadata:")
print(result["metadatas"][0])
