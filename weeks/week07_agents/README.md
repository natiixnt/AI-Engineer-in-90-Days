# week07_agents: agents

## Concept
Agents combine planning, tool usage, and an action-observation loop. This week is about building a simple but explicit control loop instead of a single prompt call.

## Key Ideas
- Agents break tasks into steps.
- Tools provide capabilities (search, math, APIs).
- Observations from tools update the next action.
- Stop conditions prevent infinite loops.

## Minimal Code Example
```python
"""Simple tool-calling agent loop.
Run: python3 agent_loop_demo.py
"""

from __future__ import annotations


def search_docs(topic: str) -> str:
    docs = {
        "rag": "RAG = retrieval plus grounded generation.",
        "eval": "Evaluation tracks relevance, faithfulness, and latency.",
    }
    return docs.get(topic, "No document found.")


def calculator(expression: str) -> str:
    allowed = set("0123456789+-*/(). ")
    if any(ch not in allowed for ch in expression):
        return "Unsafe expression"
    return str(eval(expression, {"__builtins__": {}}, {}))


def choose_action(task: str, step: int) -> tuple[str, str]:
    plan = [("search_docs", "rag"), ("calculator", "2+2"), ("finish", "")]
    return plan[min(step - 1, len(plan) - 1)]


def run_agent(task: str, max_steps: int = 3) -> str:
    observations: list[str] = []
    for step in range(1, max_steps + 1):
        action, payload = choose_action(task, step)
        if action == "finish":
            break
        if action == "search_docs":
            observations.append(search_docs(payload))
        if action == "calculator":
            observations.append(calculator(payload))
    return "\n".join(observations)


def main() -> None:
    task = "Explain RAG and calculate 2+2"
    print(run_agent(task))


if __name__ == "__main__":
    main()
```

## Exercise
Add one more tool (for example `summarize_text`) and update planning logic to use it when needed.

## Extra Challenge
Make planning dynamic by using an LLM call to decide the next tool based on observations.
