# 🤖 Document AI – Chat with Your PDF Documents

An AI-powered PDF question-answering application built with Python, Streamlit, ChromaDB, Sentence Transformers, and Google's Gemini API.

The application uses **Retrieval-Augmented Generation (RAG)** to retrieve relevant information from uploaded PDF documents and generate context-aware answers using a Large Language Model (LLM).

## 🚀 Features

- **PDF Document Loading:** Extract text from PDF documents.
- **Text Chunking:** Split documents into smaller chunks for efficient processing.
- **Semantic Embeddings:** Convert text chunks into numerical vector representations using Sentence Transformers.
- **Vector Database:** Store and manage embeddings using ChromaDB.
- **Semantic Search:** Retrieve relevant information based on user questions.
- **RAG Pipeline:** Combine document retrieval with AI-powered response generation.
- **Gemini Integration:** Generate natural-language answers using Google's Gemini API.
- **Streaming Responses:** Display generated answers progressively through the application interface.
- **Interactive Interface:** Upload documents and ask questions through Streamlit.

## 🛠️ Technologies Used

| Technology            | Purpose                   |
| --------------------- | ------------------------- |
| Python                | Core programming language |
| Streamlit             | Web application interface |
| ChromaDB              | Vector database           |
| Sentence Transformers | Embedding generation      |
| Google Gemini API     | Answer generation         |
| PyPDF                 | PDF text extraction       |
| Pytest                | Automated testing         |

## 🧠 RAG Architecture

The application follows a Retrieval-Augmented Generation architecture.

### How It Works

1. **Document Loading:** Extract text from PDF documents.
2. **Text Splitting:** Divide extracted text into smaller chunks.
3. **Embedding Generation:** Convert text chunks into vector embeddings.
4. **Vector Storage:** Store embeddings and document content in ChromaDB.
5. **Question Processing:** Convert the user's question into an embedding.
6. **Semantic Retrieval:** Search ChromaDB for relevant document chunks.
7. **Context Preparation:** Combine retrieved information with the user's question.
8. **Answer Generation:** Send the context and question to Gemini.
9. **Response Streaming:** Display the generated answer in the Streamlit interface.

### Architecture Overview

```text
          PDF Documents
                |
                v
        Document Loader
                |
                v
          Text Splitter
                |
                v
       Embedding Generation
                |
                v
            ChromaDB
                |
                |
        User's Question
                |
                v
        Semantic Search
                |
                v
       Retrieved Context
                |
                v
          Gemini API
                |
                v
        Generated Answer
                |
                v
        Streamlit Interface
```

## 📂 Project Structure

```text
week-04/
│
├── app.py
├── run_rag_demo.py
├── requirements.txt
├── .env
├── .env.example
├── .gitignore
├── README.md
│
├── src/
│   ├── __init__.py
│   ├── document_loader.py
│   ├── text_splitter.py
│   ├── embeddings.py
│   ├── vector_store.py
│   └── rag_pipeline.py
│
├── tests/
│   └── test_rag_pipeline.py
│
├── data/
│   └── documents/
│
└── chroma_db/
```

### Main Components

| File                   | Description                                          |
| ---------------------- | ---------------------------------------------------- |
| `app.py`               | Streamlit application interface                      |
| `run_rag_demo.py`      | Runs the RAG demonstration                           |
| `document_loader.py`   | Loads PDF documents and extracts text                |
| `text_splitter.py`     | Splits extracted text into chunks                    |
| `embeddings.py`        | Generates text embeddings                            |
| `vector_store.py`      | Manages ChromaDB storage and retrieval               |
| `rag_pipeline.py`      | Connects the components into a complete RAG workflow |
| `test_rag_pipeline.py` | Tests the RAG pipeline                               |

Additional standalone test scripts are available in the project root.

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone <your-github-repository-url>
```

### 2. Navigate to Week 04

```bash
cd aws-sbg-tasks/week-04
```

### 3. Create a virtual environment

```bash
python3 -m venv .venv
```

### 4. Activate the environment

```bash
source .venv/bin/activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Configure environment variables

Create your `.env` file using the example:

```bash
cp .env.example .env
```

Add your Gemini API key to the `.env` file using the variable name expected by the application.

Keep your API key private. Never commit your `.env` file to GitHub.

### 7. Run the application

```bash
streamlit run app.py
```

Open the local URL displayed in your terminal.

## 🧪 Testing

Run the automated RAG pipeline tests:

```bash
pytest -v
```

You can also execute the individual test scripts available in the project root.

## 🔐 Security

- Store API keys in environment variables.
- Never expose API keys in source code.
- Keep `.env` excluded from Git.
- Do not commit virtual environments or unnecessary generated files.

## 🎯 Learning Objectives

This project demonstrates practical implementation of:

- Document processing and text extraction.
- Text chunking strategies.
- Vector embeddings and semantic representations.
- Vector databases and similarity search.
- Retrieval-Augmented Generation (RAG).
- Large Language Model (LLM) integration.
- AI application development using Python.

_Part of the AWS SBG Machine Learning Learning Journey._
