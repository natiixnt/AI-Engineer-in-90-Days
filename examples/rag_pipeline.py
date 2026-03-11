"""Very small RAG pipeline using keyword overlap retrieval."""

from __future__ import annotations

import re

KNOWLEDGE_BASE = [
    "RAG improves factuality by grounding generation in retrieved documents.",
    "Evaluation should track relevance, faithfulness, and answer correctness.",
    "Vector databases speed up semantic retrieval over large corpora.",
    "Chunking strategy strongly affects retrieval quality.",
]


def tokenize(text: str) -> set[str]:
    return set(re.findall(r"[a-zA-Z0-9]+", text.lower()))


def retrieve(query: str, k: int = 2) -> list[str]:
    query_tokens = tokenize(query)
    scored: list[tuple[str, int]] = []
    for chunk in KNOWLEDGE_BASE:
        overlap = len(query_tokens & tokenize(chunk))
        scored.append((chunk, overlap))

    scored.sort(key=lambda pair: pair[1], reverse=True)
    return [chunk for chunk, _ in scored[:k]]


def generate_answer(question: str, context_chunks: list[str]) -> str:
    context = " ".join(context_chunks)
    return f"Question: {question}\nAnswer (grounded): {context}"


def main() -> None:
    question = "How can I evaluate a RAG system?"
    chunks = retrieve(question)
    answer = generate_answer(question, chunks)

    print("Retrieved context:")
    for chunk in chunks:
        print(f"- {chunk}")
    print("\n" + answer)


if __name__ == "__main__":
    main()
