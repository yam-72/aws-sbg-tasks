
from src.rag_pipeline import generate_answer


question = "What are the main characteristics of RISC processors?"

print("\nUser Question:")
print(question)

print("\nGenerating answer...\n")

answer = generate_answer(question)

print("RAG Chatbot Answer:")
print(answer)
