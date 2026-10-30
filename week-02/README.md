# Week 02: Mini Semantic Search

## Overview

Mini Semantic Search is a Python application that searches a Frequently Asked Questions (FAQ) dataset using semantic similarity.

Unlike traditional keyword search, semantic search uses text embeddings to find documents related to the meaning of a user's question, even when the wording differs.

## Objectives

- Load FAQ data from CSV using Pandas.
- Clean and validate the dataset.
- Convert FAQ questions and answers into embeddings.
- Store documents and embeddings in ChromaDB.
- Retrieve the three most relevant FAQs for a user query.

## Project Structure

```text
week-02/
├── faqs.csv
├── mini_semantic_search.py
├── mini_semantic_search.ipynb
├── README.md
└── requirements.txt
```

## Technologies

- Python
- Pandas
- ChromaDB
- NumPy
- Google Colab

ChromaDB uses the `all-MiniLM-L6-v2` embedding model by default to generate text embeddings.

## Installation

Activate the virtual environment from the repository root:

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
python -m pip install -r week-02/requirements.txt
```

## Run the Application

From the repository root:

```bash
python week-02/mini_semantic_search.py
```

Enter a question when prompted. The application returns up to three relevant FAQs, including their categories, questions, answers, and distance values.

Type `exit` or `quit` to close the application.

## Example Queries

```text
My payment failed. What should I do?
I forgot my login password.
When will my package arrive?
I want my money back.
```

## Dataset

The `faqs.csv` file contains ten sample FAQs covering:

- Account
- Payment
- Delivery
- Orders
- Support

Each record includes an ID, question, answer, and category.

## How Semantic Search Works

1. Load FAQ records from the CSV file.
2. Remove invalid records and clean text values.
3. Combine each question and answer into a document.
4. Generate embeddings and store documents in ChromaDB.
5. Convert the user's query into an embedding.
6. Retrieve the three closest matching documents.
7. Display the matching FAQ information.
