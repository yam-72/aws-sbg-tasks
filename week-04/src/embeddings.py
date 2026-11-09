
import os

from dotenv import load_dotenv
from google import genai
from google.genai import types


# Load environment variables from .env
load_dotenv()

# Read the Gemini API key
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY was not found in .env")

# Create Gemini client
client = genai.Client(api_key=api_key)


def embed_text(
    text: str,
    task_type: str = "RETRIEVAL_DOCUMENT"
) -> list[float]:
    """
    Convert text into a numerical embedding vector.
    """

    if not text or not text.strip():
        raise ValueError("Text cannot be empty.")

    response = client.models.embed_content(
        model="gemini-embedding-001",
        contents=text,
        config=types.EmbedContentConfig(
            task_type=task_type,
            output_dimensionality=768
        )
    )

    return response.embeddings[0].values

def embed_texts(
    texts: list[str],
    task_type: str = "RETRIEVAL_DOCUMENT"
) -> list[list[float]]:
    """
    Convert multiple text chunks into embedding vectors.
    """

    if not texts:
        return []

    if any(not text or not text.strip() for text in texts):
        raise ValueError("All texts must contain non-empty content.")

    response = client.models.embed_content(
        model="gemini-embedding-001",
        contents=texts,
        config=types.EmbedContentConfig(
            task_type=task_type,
            output_dimensionality=768
        )
    )

    return [
        embedding.values
        for embedding in response.embeddings
    ]
