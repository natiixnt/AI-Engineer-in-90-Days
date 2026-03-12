# week09_build_projects: build projects

## Concept
This week is about combining previous concepts into complete AI systems. You move from isolated demos to integrated workflows that include retrieval, generation, tools, evaluation, and interfaces.

## Key Ideas
- Production systems are compositions of small components.
- Clear interfaces between modules reduce complexity.
- Build vertical slices early: input -> pipeline -> output.
- Add logging and evaluation before scaling features.

## Minimal Code Example
```python
"""Combine retrieval, agent step, and response assembly.
Run: python3 build_project_slice.py
"""

from __future__ import annotations


def retrieve_context(question: str) -> list[str]:
    kb = [
        "RAG needs retrieval precision and faithfulness checks.",
        "Agents can call tools to gather missing information.",
        "Monitoring tracks latency and output quality.",
    ]
    return [chunk for chunk in kb if any(word in chunk.lower() for word in question.lower().split())][:2]


def run_agent_step(question: str) -> str:
    if "metric" in question.lower() or "evaluate" in question.lower():
        return "Tool result: recommend precision, recall, and faithfulness metrics."
    return "Tool result: no extra tool needed."


def generate_answer(question: str, context: list[str], tool_result: str) -> str:
    merged = " ".join(context)
    return f"Q: {question}\nContext: {merged}\n{tool_result}"


def main() -> None:
    question = "How do I evaluate a RAG assistant in production?"
    context = retrieve_context(question)
    tool_result = run_agent_step(question)
    answer = generate_answer(question, context, tool_result)
    print(answer)


if __name__ == "__main__":
    main()
```

## Exercise
Pick one project in `projects/` and define a minimal v1 with 3 modules: retrieval, generation, and evaluation.

## Extra Challenge
Add a CLI command that runs an end-to-end smoke test and prints pass/fail checks.
