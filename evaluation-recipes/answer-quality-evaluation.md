# Answer Quality Evaluation Recipe

## Goal
Evaluate whether generated answers are useful, correct, and complete for user tasks.

## Metric Ideas
- task success rate
- completeness score (all required points included)
- answer clarity/readability
- user-rated helpfulness

## Sample Workflow
1. Define expected outcomes per test query.
2. Generate answers using a fixed pipeline version.
3. Score each answer with rules or human review.
4. Analyze failures by missing content vs wrong content.
5. Add regression tests for repeated failure patterns.

## Simple Python Example
```python
def keyword_coverage(answer: str, required_keywords: list[str]) -> float:
    text = answer.lower()
    hits = sum(1 for kw in required_keywords if kw.lower() in text)
    return hits / max(1, len(required_keywords))


def exact_match_ratio(predictions: list[str], expected: list[str]) -> float:
    hits = sum(1 for p, e in zip(predictions, expected) if e.lower() in p.lower())
    return hits / max(1, len(expected))
```
