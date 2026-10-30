from pathlib import Path

import chromadb
import pandas as pd


# Project paths
BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "faqs.csv"
DB_DIR = BASE_DIR / "chroma_db"


def load_faqs():
    """Load and validate FAQs from the CSV file."""
    if not DATA_FILE.exists():
        raise FileNotFoundError(f"Dataset not found: {DATA_FILE}")

    df = pd.read_csv(DATA_FILE)

    required_columns = {"id", "question", "answer", "category"}

    if not required_columns.issubset(df.columns):
        missing = required_columns - set(df.columns)
        raise ValueError(f"Missing required columns: {missing}")

    # Remove rows with missing required values.
    df = df.dropna(subset=["question", "answer", "category"]).copy()

    # Clean whitespace from text columns.
    for column in ["question", "answer", "category"]:
        df[column] = df[column].astype(str).str.strip()

    # Remove rows with empty questions or answers.
    df = df[
        (df["question"] != "")
        & (df["answer"] != "")
        & (df["category"] != "")
    ]

    # Remove duplicate questions.
    df = df.drop_duplicates(subset=["question"])

    if df.empty:
        raise ValueError("No valid FAQs were found in the dataset.")

    df["id"] = df["id"].astype(str)

    print(f"Loaded {len(df)} valid FAQs.")
    return df


def create_search_collection(df):
    """Store FAQ documents and their embeddings in ChromaDB."""
    client = chromadb.PersistentClient(path=str(DB_DIR))

    # Rebuild the collection so it always reflects the current CSV.
    collection = client.get_or_create_collection(
        name="faq_collection"
    )

    existing_count = collection.count()

    if existing_count > 0:
        existing_ids = collection.get()["ids"]
        collection.delete(ids=existing_ids)

    documents = (
        "Question: " + df["question"]
        + "\nAnswer: " + df["answer"]
    ).tolist()

    metadatas = [
        {
            "question": row["question"],
            "answer": row["answer"],
            "category": row["category"],
        }
        for _, row in df.iterrows()
    ]

    collection.add(
        ids=df["id"].tolist(),
        documents=documents,
        metadatas=metadatas,
    )

    print(f"Stored {collection.count()} FAQs in ChromaDB.")
    return collection


def search_faqs(collection, query):
    """Find the three most relevant FAQs for a query."""
    query = query.strip()

    if not query:
        print("Please enter a search question.")
        return

    results = collection.query(
        query_texts=[query],
        n_results=min(3, collection.count()),
        include=["metadatas", "distances"],
    )

    print(f"\nSearch results for: {query}")
    print("=" * 60)

    if not results["ids"] or not results["ids"][0]:
        print("No matching FAQs found.")
        return

    for rank, metadata in enumerate(results["metadatas"][0], start=1):
        distance = results["distances"][0][rank - 1]

        print(f"\nResult {rank}")
        print(f"Category: {metadata['category']}")
        print(f"Question: {metadata['question']}")
        print(f"Answer: {metadata['answer']}")
        print(f"Distance: {distance:.4f}")


def main():
    """Run the FAQ semantic search application."""
    try:
        faqs = load_faqs()
        collection = create_search_collection(faqs)

        print("\nMini Semantic Search")
        print("Type 'exit' to quit.")

        while True:
            query = input("\nEnter your question: ")

            if query.strip().lower() in {"exit", "quit"}:
                print("Goodbye!")
                break

            search_faqs(collection, query)

    except (FileNotFoundError, ValueError) as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
