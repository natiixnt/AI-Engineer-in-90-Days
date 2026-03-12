# Prompt Comparison Recipe

## Goal
Compare prompt versions objectively and pick the best one for production.

## Metric Ideas
- task success rate
- format validity rate
- refusal correctness rate
- latency and token cost deltas

## Sample Workflow
1. Freeze an evaluation set with representative queries.
2. Run Prompt A and Prompt B on the same set.
3. Score outputs with the same rubric/validator.
4. Compare quality, cost, and latency side by side.
5. Promote only if thresholds improve without regressions.

## Simple Python Example
```python
def compare_prompt_runs(scores_a: list[float], scores_b: list[float]) -> dict:
    avg_a = sum(scores_a) / max(1, len(scores_a))
    avg_b = sum(scores_b) / max(1, len(scores_b))
    return {
        "avg_a": round(avg_a, 4),
        "avg_b": round(avg_b, 4),
        "delta": round(avg_b - avg_a, 4),
        "winner": "B" if avg_b > avg_a else "A",
    }
```
