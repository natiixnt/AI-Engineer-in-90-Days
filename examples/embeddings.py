"""Minimal embedding demo with bag-of-words vectors."""

from __future__ import annotations

import math
import re
from collections import Counter


def tokenize(text: str) -> list[str]:
    return re.findall(r"[a-zA-Z0-9]+", text.lower())


def build_vocab(texts: list[str]) -> list[str]:
    vocab = set()
    for text in texts:
        vocab.update(tokenize(text))
    return sorted(vocab)


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
    documents = [
        "RAG combines retrieval with generation.",
        "Vector databases store embeddings for semantic search.",
        "Agents can call tools and iterate over multiple steps.",
    ]
    query = "semantic retrieval with vectors"

    vocab = build_vocab(documents + [query])
    query_vector = embed(query, vocab)

    print("Query:", query)
    print("Top matches:")
    for doc in documents:
        score = cosine_similarity(query_vector, embed(doc, vocab))
        print(f"- {score:.3f} :: {doc}")


if __name__ == "__main__":
    main()
