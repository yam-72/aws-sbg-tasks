
import hashlib
import tempfile
from pathlib import Path

import streamlit as st

from src.document_loader import load_pdf
from src.text_splitter import split_text
from src.vector_store import collection, store_chunks
from src.rag_pipeline import generate_answer


# --------------------------------------------------
# Page configuration
# --------------------------------------------------

st.set_page_config(
    page_title="Document AI Chatbot",
    page_icon="🤖",
    layout="centered"
)


# --------------------------------------------------
# Session state
# --------------------------------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []


# --------------------------------------------------
# Sidebar
# --------------------------------------------------

with st.sidebar:
    st.title("🤖 Document AI")
    st.write("Chat with your PDF documents.")

    st.divider()

    st.subheader("Upload a document")

    uploaded_file = st.file_uploader(
        "Choose a PDF file",
        type=["pdf"]
    )

    if st.button("Process PDF", disabled=uploaded_file is None):
        try:
            with st.spinner("Processing your PDF..."):

                # Read uploaded PDF content
                pdf_bytes = uploaded_file.getvalue()

                # Create a unique source ID based on file content
                file_hash = hashlib.sha256(pdf_bytes).hexdigest()[:12]
                filename = Path(uploaded_file.name).name
                source_id = f"{Path(filename).stem}_{file_hash}.pdf"

                # Save temporarily because load_pdf expects a file path
                with tempfile.NamedTemporaryFile(
                    suffix=".pdf",
                    delete=False
                ) as temp_file:
                    temp_file.write(pdf_bytes)
                    temp_path = Path(temp_file.name)

                try:
                    # Extract PDF text
                    text = load_pdf(temp_path)
                finally:
                    temp_path.unlink(missing_ok=True)

                if not text.strip():
                    st.error("No readable text was found in this PDF.")
                else:
                    # Split extracted text into chunks
                    chunks = split_text(text)

                    # Generate embeddings and store chunks
                    total = store_chunks(
                        chunks,
                        source=source_id
                    )

                    st.success(
                        f"Successfully processed {filename}! "
                        f"Stored {total} chunks."
                    )

        except Exception as error:
            st.error(f"PDF processing failed: {error}")

    st.divider()

    st.subheader("Knowledge base")
    st.metric("Stored document chunks", collection.count())

    if st.button("Clear chat history"):
        st.session_state.messages = []
        st.rerun()


# --------------------------------------------------
# Main application
# --------------------------------------------------

st.title("💬 Chat with Your Documents")

st.caption(
    "Ask questions and get answers based on your uploaded PDFs."
)

st.divider()


# --------------------------------------------------
# Display previous messages
# --------------------------------------------------

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# --------------------------------------------------
# Chat input and answer generation
# --------------------------------------------------

if collection.count() == 0:

    st.info(
        "Your knowledge base is empty. "
        "Upload a PDF using the sidebar to get started."
    )

else:

    question = st.chat_input("Ask something about your documents...")

    if question:
        # Display user question
        st.session_state.messages.append(
            {"role": "user", "content": question}
        )

        with st.chat_message("user"):
            st.markdown(question)

        # Generate AI response
        with st.chat_message("assistant"):
            with st.spinner("Searching documents and generating answer..."):
                try:
                    answer = generate_answer(question)

                    st.markdown(answer)

                    st.session_state.messages.append(
                        {"role": "assistant", "content": answer}
                    )

                except Exception as error:
                    st.error(f"Something went wrong: {error}")
