# week05_rag: rag

## Concept
RAG combines retrieval and generation: chunk documents, embed/index chunks, retrieve relevant context, and assemble a prompt grounded in those chunks.

## Key Ideas
- Chunk quality strongly affects retrieval quality.
- Retrieval should be measurable and deterministic.
- Prompt assembly must include clear context boundaries.
- Generated answers should cite retrieved evidence.

## Minimal Code Example
```python
"""Minimal RAG flow: chunking -> retrieval -> answer assembly.
Run: python3 rag_minimal.py
"""

from __future__ import annotations

import re


def tokenize(text: str) -> set[str]:
    return set(re.findall(r"[a-zA-Z0-9]+", text.lower()))


def chunk_text(text: str, chunk_size: int = 12) -> list[str]:
    words = text.split()
    return [" ".join(words[i : i + chunk_size]) for i in range(0, len(words), chunk_size)]


def retrieve(query: str, chunks: list[str], k: int = 2) -> list[str]:
    q = tokenize(query)
    scored = [(chunk, len(q & tokenize(chunk))) for chunk in chunks]
    scored.sort(key=lambda pair: pair[1], reverse=True)
    return [chunk for chunk, _ in scored[:k]]


def generate_answer(question: str, context_chunks: list[str]) -> str:
    context = "\n".join(f"- {chunk}" for chunk in context_chunks)
    return f"Question: {question}\nContext:\n{context}\nAnswer: Use the retrieved context above."


def main() -> None:
    document = (
        "RAG systems rely on chunking, retrieval, and grounded generation. "
        "Evaluation should track retrieval precision, context relevance, and faithfulness."
    )
    chunks = chunk_text(document)
    question = "How should I evaluate a RAG system?"
    top_chunks = retrieve(question, chunks, k=2)
    print(generate_answer(question, top_chunks))


if __name__ == "__main__":
    main()
```

## Exercise
Change `chunk_size` and observe how retrieval results change for the same query.

## Extra Challenge
Add source IDs to each chunk and include citations in the final answer.
