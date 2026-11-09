
from src.embeddings import embed_text

sentence = "A processor executes instructions and controls computer operations."

# Generate embedding
vector = embed_text(sentence)

print("Embedding generated successfully!")
print("Vector dimensions:", len(vector))
print("First 10 values:", vector[:10])
