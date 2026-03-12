# week06_vector_databases: vector databases

## Concept
This week focuses on indexing vectors, running nearest-neighbor search, and filtering by metadata. The objective is to understand how vector stores power semantic retrieval in production.

## Key Ideas
- Index embeddings once, search many times.
- Similarity search returns nearest semantic matches.
- Metadata filters narrow results to relevant subsets.
- Vector stores are retrieval infrastructure for RAG.

## Minimal Code Example
```python
"""Tiny in-memory vector store with metadata filtering.
Run: python3 vector_store_demo.py
"""

from __future__ import annotations

import math


def cosine_similarity(a: list[float], b: list[float]) -> float:
    dot = sum(x * y for x, y in zip(a, b))
    norm_a = math.sqrt(sum(x * x for x in a))
    norm_b = math.sqrt(sum(y * y for y in b))
    if norm_a == 0 or norm_b == 0:
        return 0.0
    return dot / (norm_a * norm_b)


class VectorStore:
    def __init__(self) -> None:
        self.items: list[dict] = []

    def add(self, item_id: str, vector: list[float], category: str) -> None:
        self.items.append({"id": item_id, "vector": vector, "category": category})

    def search(self, query: list[float], k: int = 3, category: str | None = None) -> list[tuple[str, float]]:
        candidates = [item for item in self.items if category is None or item["category"] == category]
        scored = [(item["id"], cosine_similarity(query, item["vector"])) for item in candidates]
        scored.sort(key=lambda pair: pair[1], reverse=True)
        return scored[:k]


def main() -> None:
    store = VectorStore()
    store.add("doc-1", [0.9, 0.1, 0.0], category="rag")
    store.add("doc-2", [0.1, 0.8, 0.2], category="agents")
    store.add("doc-3", [0.8, 0.2, 0.1], category="rag")

    query = [1.0, 0.0, 0.0]
    print(store.search(query, k=2, category="rag"))


if __name__ == "__main__":
    main()
```

## Exercise
Add a second metadata field (for example `source`) and support filtering by both category and source.

## Extra Challenge
Persist vectors to disk (JSON or SQLite) and reload them at startup.
