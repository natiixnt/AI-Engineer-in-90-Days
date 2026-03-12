# Retrieval Evaluation Recipe

## Goal
Measure whether your retriever returns the right context chunks for real user queries.

## Metric Ideas
- `Recall@k`
- `Precision@k`
- `MRR` (mean reciprocal rank)
- query coverage by domain/topic

## Sample Workflow
1. Build a small labeled dataset: query -> relevant chunk IDs.
2. Run retrieval for each query with fixed `k`.
3. Compute retrieval metrics per query and aggregate.
4. Segment failures by query type (short, long, ambiguous).
5. Tune chunking/indexing/embedding model and re-run.

## Simple Python Example
```python
def recall_at_k(retrieved_ids: list[str], relevant_ids: set[str], k: int) -> float:
    top_k = set(retrieved_ids[:k])
    return len(top_k & relevant_ids) / max(1, len(relevant_ids))


def precision_at_k(retrieved_ids: list[str], relevant_ids: set[str], k: int) -> float:
    top_k = retrieved_ids[:k]
    if not top_k:
        return 0.0
    hits = sum(1 for rid in top_k if rid in relevant_ids)
    return hits / len(top_k)
```
