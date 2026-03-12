# Model Comparison Recipe

## Goal
Choose the best model for your workload based on quality, latency, and cost.

## Metric Ideas
- quality score on eval set
- p95 latency
- token cost per request
- error/timeout rate

## Sample Workflow
1. Define acceptance thresholds (quality, p95 latency, budget).
2. Run the same eval set across candidate models.
3. Capture per-request quality, latency, and token metrics.
4. Build a scorecard for weighted decision-making.
5. Validate the winner with a canary rollout.

## Simple Python Example
```python
def weighted_model_score(quality: float, latency_ms: float, cost_usd: float) -> float:
    # Higher is better. Normalize in real systems.
    return (quality * 0.6) + ((1 / max(1.0, latency_ms)) * 200 * 0.2) + ((1 / max(0.001, cost_usd)) * 0.2)


models = {
    "model_a": {"quality": 0.88, "latency_ms": 1400, "cost_usd": 0.012},
    "model_b": {"quality": 0.84, "latency_ms": 900, "cost_usd": 0.007},
}
```
