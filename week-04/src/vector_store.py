
from pathlib import Path

import chromadb

from src.embeddings import embed_texts


# Store the database inside the week-04 directory
DB_PATH = Path(__file__).resolve().parent.parent / "chroma_db"

# Create a persistent ChromaDB client
client = chromadb.PersistentClient(path=str(DB_PATH))

# Create or access our document collection
collection = client.get_or_create_collection(
    name="rag_documents",
    metadata={"hnsw:space": "cosine"}
)


def store_chunks(
    chunks: list[str],
    source: str = "sample.pdf"
) -> int:
    """
    Generate embeddings and store text chunks in ChromaDB.
    """

    if not chunks:
        return 0

    # Generate embeddings for all chunks
    embeddings = embed_texts(chunks)

    # Create unique IDs for each chunk
    ids = [
        f"{source}_chunk_{i}"
        for i in range(len(chunks))
    ]

    # Store source information and chunk indexes
    metadatas = [
        {
            "source": source,
            "chunk_index": i
        }
        for i in range(len(chunks))
    ]

    # Insert or update records
    collection.upsert(
        ids=ids,
        embeddings=embeddings,
        documents=chunks,
        metadatas=metadatas
    )

    return len(chunks)
