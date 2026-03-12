# Agent Evaluation Recipe

## Goal
Measure whether an agent completes multi-step tasks correctly, safely, and efficiently.

## Metric Ideas
- task completion rate
- average steps per successful task
- tool argument accuracy
- forced-stop / loop rate

## Sample Workflow
1. Build task set with expected outcomes and allowed tools.
2. Run agent with full step traces enabled.
3. Score task success and validate tool-call correctness.
4. Detect loops, repeated actions, and unsafe tool attempts.
5. Improve planner/tool policies and re-run regression suite.

## Simple Python Example
```python
def completion_rate(results: list[dict]) -> float:
    completed = sum(1 for r in results if r.get("status") == "completed")
    return completed / max(1, len(results))


def loop_rate(results: list[dict]) -> float:
    loops = sum(1 for r in results if r.get("loop_detected", False))
    return loops / max(1, len(results))


def avg_steps(results: list[dict]) -> float:
    steps = [r.get("steps", 0) for r in results]
    return sum(steps) / max(1, len(steps))
```
