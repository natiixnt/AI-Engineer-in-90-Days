# Faithfulness Checking Recipe

## Goal
Detect whether answers are grounded in retrieved evidence rather than unsupported claims.

## Metric Ideas
- faithfulness score (claim supported by context)
- unsupported claim rate
- citation coverage rate
- contradiction rate vs context

## Sample Workflow
1. Collect query, retrieved context, answer, and citations.
2. Split answer into atomic claims.
3. Check each claim against context/citation evidence.
4. Mark unsupported or contradictory claims.
5. Track faithfulness trends by prompt/model version.

## Simple Python Example
```python
def citation_coverage(answer: str) -> float:
    # Simple heuristic: count sentences with citations like [chunk-12]
    sentences = [s.strip() for s in answer.split('.') if s.strip()]
    if not sentences:
        return 0.0
    cited = sum(1 for s in sentences if '[chunk-' in s)
    return cited / len(sentences)


def has_unsupported_claim(answer: str, context: str) -> bool:
    # Baseline heuristic; replace with claim-level verifier later.
    return any(claim.lower() not in context.lower() for claim in answer.split('. ')[:2] if claim)
```
