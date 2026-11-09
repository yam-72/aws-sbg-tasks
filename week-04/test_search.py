from src.vector_store import search_documents

question = "What are the main characteristics of RISC processors?"

results = search_documents(question, n_results=3)

print("\nUser Question:")
print(question)

print("\nRetrieved Documents:")

for i, document in enumerate(results["documents"][0], start=1):
    print(f"\n--- Result {i} ---")
    print(document)

    print("\nMetadata:")
    print(results["metadatas"][0][i - 1])

    print("\nDistance:")
    print(results["distances"][0][i - 1])