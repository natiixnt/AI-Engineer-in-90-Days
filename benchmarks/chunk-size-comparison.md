# Chunk Size Comparison Benchmark

## Experiment Goal
Measure how chunk size affects retrieval quality and response cost/latency in a simple RAG setup.

## Setup
- Use one small document corpus (10-50 docs).
- Test multiple chunk sizes (for example: 60, 120, 240 words).
- Keep embedding model and retriever fixed.
- Use a small labeled query set (`query -> relevant doc/chunk`).

## Example Script
```python
from __future__ import annotations


def chunks(words: list[str], size: int) -> list[str]:
    return [" ".join(words[i:i + size]) for i in range(0, len(words), size)]


def recall_at_k(retrieved: list[str], relevant: set[str], k: int = 3) -> float:
    return len(set(retrieved[:k]) & relevant) / max(1, len(relevant))


def run_experiment(text: str, query_set: list[tuple[str, set[str]]], sizes: list[int]) -> None:
    words = text.split()
    for size in sizes:
        _chunks = chunks(words, size)
        # Replace with your real retriever scoring.
        avg_recall = 0.0
        for _, relevant_ids in query_set:
            retrieved_ids = [f"chunk-{i}" for i in range(min(3, len(_chunks)))]
            avg_recall += recall_at_k(retrieved_ids, relevant_ids, k=3)
        avg_recall /= max(1, len(query_set))
        print(f"chunk_size={size} avg_recall@3={avg_recall:.3f} num_chunks={len(_chunks)}")
```

## How to Interpret Results
- Smaller chunks often improve precision but can lose context continuity.
- Larger chunks can improve context completeness but hurt retrieval precision and token cost.
- Pick the smallest chunk size that keeps `Recall@k` acceptable and latency/cost within budget.
