
from types import SimpleNamespace

import pytest
import src.rag_pipeline as rag_pipeline


def test_empty_question():
    with pytest.raises(ValueError, match="Question cannot be empty"):
        rag_pipeline.generate_answer("")


def test_no_relevant_documents(monkeypatch):
    def fake_search(query, n_results):
        return {"documents": [[]]}

    monkeypatch.setattr(
        rag_pipeline,
        "search_documents",
        fake_search
    )

    answer = rag_pipeline.generate_answer("What is RISC?")

    assert "couldn't find relevant information" in answer


def test_generate_answer_with_context(monkeypatch):
    def fake_search(query, n_results):
        return {
            "documents": [
                ["RISC processors use a small and simple instruction set."]
            ]
        }

    def fake_generate_content(model, contents):
        assert "RISC processors" in contents
        assert "What is RISC?" in contents
        return SimpleNamespace(
            text="RISC processors use a small instruction set."
        )

    monkeypatch.setattr(
        rag_pipeline,
        "search_documents",
        fake_search
    )

    monkeypatch.setattr(
        rag_pipeline.client.models,
        "generate_content",
        fake_generate_content
    )

    answer = rag_pipeline.generate_answer("What is RISC?")

    assert answer == "RISC processors use a small instruction set."


def test_empty_gemini_response(monkeypatch):
    monkeypatch.setattr(
        rag_pipeline,
        "search_documents",
        lambda query, n_results: {
            "documents": [["Some document content"]]
        }
    )

    monkeypatch.setattr(
        rag_pipeline.client.models,
        "generate_content",
        lambda model, contents: SimpleNamespace(text=None)
    )

    answer = rag_pipeline.generate_answer("Explain RISC")

    assert answer == "Gemini did not return a text answer."
