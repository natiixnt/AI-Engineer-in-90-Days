# Retrieval Strategy Comparison Benchmark

## Experiment Goal
Compare retrieval strategies (keyword, vector, hybrid) to find the best balance of precision and recall.

## Setup
- Keep corpus and query set fixed.
- Implement three strategies:
  - keyword-only
  - vector-only
  - hybrid (weighted merge)
- Evaluate with the same metrics and top-k.

## Example Script
```python
from __future__ import annotations


def precision_at_k(retrieved: list[str], relevant: set[str], k: int = 3) -> float:
    top_k = retrieved[:k]
    if not top_k:
        return 0.0
    return sum(1 for rid in top_k if rid in relevant) / len(top_k)


def evaluate_strategy(name: str, query_set: list[tuple[str, set[str]]]) -> dict:
    total = 0.0
    for query, relevant_ids in query_set:
        # Replace with real retrieval strategy logic.
        if name == "keyword":
            retrieved = ["doc-1", "doc-4", "doc-5"]
        elif name == "vector":
            retrieved = ["doc-2", "doc-1", "doc-6"]
        else:  # hybrid
            retrieved = ["doc-1", "doc-2", "doc-4"]
        total += precision_at_k(retrieved, relevant_ids, k=3)

    return {"strategy": name, "avg_precision@3": round(total / max(1, len(query_set)), 4)}


queries = [("rag quality", {"doc-1"}), ("agent planning", {"doc-2"})]
for s in ["keyword", "vector", "hybrid"]:
    print(evaluate_strategy(s, queries))
```

## How to Interpret Results
- Keyword retrieval usually wins on exact terms and IDs.
- Vector retrieval usually wins on semantic paraphrases.
- Hybrid often gives the most stable overall quality in production.
- Choose strategy by query mix: exact-match heavy vs semantic heavy.
