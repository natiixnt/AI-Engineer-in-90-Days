"""Tiny in-memory vector search example."""

from __future__ import annotations

import math


class VectorIndex:
    def __init__(self) -> None:
        self.items: list[tuple[str, list[float]]] = []

    def add(self, item_id: str, vector: list[float]) -> None:
        self.items.append((item_id, vector))

    def search(self, query: list[float], k: int = 3) -> list[tuple[str, float]]:
        scored = [(item_id, cosine_similarity(query, vec)) for item_id, vec in self.items]
        scored.sort(key=lambda pair: pair[1], reverse=True)
        return scored[:k]


def cosine_similarity(a: list[float], b: list[float]) -> float:
    dot = sum(x * y for x, y in zip(a, b))
    norm_a = math.sqrt(sum(x * x for x in a))
    norm_b = math.sqrt(sum(y * y for y in b))
    if norm_a == 0 or norm_b == 0:
        return 0.0
    return dot / (norm_a * norm_b)


def main() -> None:
    index = VectorIndex()
    index.add("doc-1", [1.0, 0.0, 0.0])
    index.add("doc-2", [0.7, 0.7, 0.0])
    index.add("doc-3", [0.0, 0.1, 1.0])

    query = [0.8, 0.2, 0.0]
    print("Query:", query)
    print("Nearest vectors:")
    for item_id, score in index.search(query, k=3):
        print(f"- {item_id}: {score:.3f}")


if __name__ == "__main__":
    main()
