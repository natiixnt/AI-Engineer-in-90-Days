# Embedding Model Comparison Benchmark

## Experiment Goal
Compare embedding models for retrieval quality, speed, and cost on your domain queries.

## Setup
- Select 2-4 embedding models (API or local).
- Use the same corpus, chunking method, and retrieval logic.
- Evaluate on a labeled query set.
- Capture quality + runtime/cost metrics per model.

## Example Script
```python
from __future__ import annotations

import time


def recall_at_k(retrieved: list[str], relevant: set[str], k: int = 3) -> float:
    return len(set(retrieved[:k]) & relevant) / max(1, len(relevant))


def benchmark_model(model_name: str, query_set: list[tuple[str, set[str]]]) -> dict:
    start = time.perf_counter()
    total_recall = 0.0

    for query, relevant_ids in query_set:
        # Replace with real embedding + retrieval.
        retrieved_ids = ["doc-1", "doc-2", "doc-3"]
        total_recall += recall_at_k(retrieved_ids, relevant_ids, k=3)

    elapsed_ms = (time.perf_counter() - start) * 1000
    avg_recall = total_recall / max(1, len(query_set))
    return {"model": model_name, "avg_recall@3": round(avg_recall, 4), "latency_ms": round(elapsed_ms, 2)}


for model in ["embed-small", "embed-large"]:
    print(benchmark_model(model, [("rag eval", {"doc-1"}), ("agents", {"doc-2"})]))
```

## How to Interpret Results
- Prefer models with better recall on your real query distribution, not generic benchmarks.
- A slightly lower-quality model may be better if latency and cost improve significantly.
- If quality gaps are small, choose the model that scales operationally and fits budget.
