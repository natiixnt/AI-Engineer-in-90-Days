# week03_embeddings: embeddings

## Concept
Embeddings convert text into vectors so you can compare meaning numerically. This week focuses on creating vector representations and ranking documents by cosine similarity.

## Key Ideas
- Text similarity becomes vector math.
- Good tokenization choices affect retrieval quality.
- Cosine similarity is a practical default for ranking.
- Embeddings power search, clustering, and RAG retrieval.

## Minimal Code Example
```python
"""Generate simple embeddings and compute cosine similarity.
Run: python3 embeddings_similarity.py
"""

from __future__ import annotations

import math
import re
from collections import Counter


def tokenize(text: str) -> list[str]:
    return re.findall(r"[a-zA-Z0-9]+", text.lower())


def embed(text: str, vocab: list[str]) -> list[float]:
    counts = Counter(tokenize(text))
    return [float(counts[token]) for token in vocab]


def cosine_similarity(a: list[float], b: list[float]) -> float:
    dot = sum(x * y for x, y in zip(a, b))
    norm_a = math.sqrt(sum(x * x for x in a))
    norm_b = math.sqrt(sum(y * y for y in b))
    if norm_a == 0 or norm_b == 0:
        return 0.0
    return dot / (norm_a * norm_b)


def main() -> None:
    docs = [
        "RAG combines retrieval with generation.",
        "Vector databases index embeddings for search.",
        "Agents plan, act, and observe.",
    ]
    query = "embedding based retrieval"

    vocab = sorted(set(token for text in docs + [query] for token in tokenize(text)))
    query_vec = embed(query, vocab)

    scored = [(doc, cosine_similarity(query_vec, embed(doc, vocab))) for doc in docs]
    scored.sort(key=lambda pair: pair[1], reverse=True)

    for doc, score in scored:
        print(f"{score:.3f} :: {doc}")


if __name__ == "__main__":
    main()
```

## Exercise
Add two more documents and test whether your retrieval ranking still matches intuition.

## Extra Challenge
Normalize vectors and compare cosine similarity with plain dot-product ranking.
