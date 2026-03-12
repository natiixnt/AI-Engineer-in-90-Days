# Build Your Own Embedding Search

Build a small semantic search system that finds the most relevant text chunks for a user query. This is a core building block for modern AI products because retrieval quality directly affects answer quality.

## Concepts Practiced
- embeddings
- vector representations
- similarity search
- ranking
- lightweight evaluation

## System Overview
You will build a minimal embedding search pipeline with three parts:

1. **Indexer**: convert each document chunk into a vector and store it.
2. **Retriever**: embed a user query and compare it with stored vectors.
3. **Ranker**: sort results by cosine similarity and return top matches.

## Implementation Steps
1. Load a small dataset of short documents (10-30 lines is enough).
2. Normalize and chunk each document into smaller pieces.
3. Generate an embedding for each chunk.
4. Store chunk text, chunk id, and vector in an in-memory index.
5. Implement cosine similarity.
6. Embed the query and compute similarity against all chunks.
7. Return top-k chunks and print scores.
8. Test with 3-5 different queries and inspect results.

## Starter Code
```python
from __future__ import annotations

import math


def cosine_similarity(a: list[float], b: list[float]) -> float:
    dot = sum(x * y for x, y in zip(a, b))
    norm_a = math.sqrt(sum(x * x for x in a))
    norm_b = math.sqrt(sum(y * y for y in b))
    if norm_a == 0 or norm_b == 0:
        return 0.0
    return dot / (norm_a * norm_b)


class EmbeddingIndex:
    def __init__(self) -> None:
        self.rows: list[dict] = []

    def add(self, chunk_id: str, text: str, vector: list[float]) -> None:
        self.rows.append({"id": chunk_id, "text": text, "vector": vector})

    def search(self, query_vector: list[float], k: int = 3) -> list[tuple[str, float]]:
        scored = []
        for row in self.rows:
            score = cosine_similarity(query_vector, row["vector"])
            scored.append((row["id"], score))
        scored.sort(key=lambda pair: pair[1], reverse=True)
        return scored[:k]


# TODO:
# 1) implement embed_text(text) -> list[float]
# 2) load dataset and add chunks to EmbeddingIndex
# 3) run search for a query and print top-k matches
```

## Hints
- Start with a deterministic embedding method first (even bag-of-words) before using an external API.
- Keep chunk IDs stable so you can trace retrieval errors.
- If all scores are near zero, inspect tokenization and normalization.

## Extension Ideas
- Try overlapping chunks instead of fixed non-overlapping chunks.
- Add metadata filters (topic, source, date).
- Add reranking with a cross-encoder or an LLM.
- Add offline evaluation with expected chunk labels.
