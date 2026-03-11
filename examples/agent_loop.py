"""Simple agent loop with deterministic tool selection."""

from __future__ import annotations


def search_docs(topic: str) -> str:
    docs = {
        "rag": "RAG = retrieval + generation grounded in external knowledge.",
        "agents": "Agents iterate: plan -> act -> observe -> refine.",
        "eval": "Evaluation uses test sets, metrics, and trace analysis.",
    }
    return docs.get(topic, "No document found for this topic.")


def calculator(expression: str) -> str:
    allowed = set("0123456789+-*/(). ")
    if any(ch not in allowed for ch in expression):
        return "Unsafe expression."
    try:
        return str(eval(expression, {"__builtins__": {}}, {}))
    except Exception as exc:  # pragma: no cover
        return f"Calculation failed: {exc}"


def choose_action(task: str, step: int) -> tuple[str, str]:
    text = task.lower()
    plan: list[tuple[str, str]] = []
    if "rag" in text:
        plan.append(("search_docs", "rag"))
    if "agent" in text:
        plan.append(("search_docs", "agents"))
    if "2+2" in text:
        plan.append(("calculator", "2+2"))

    if step <= len(plan):
        return plan[step - 1]
    return "finish", ""


def run_agent(task: str, max_steps: int = 3) -> str:
    observations: list[str] = []

    for step in range(1, max_steps + 1):
        action, payload = choose_action(task, step)
        if action == "finish":
            break

        if action == "search_docs":
            observations.append(search_docs(payload))
        elif action == "calculator":
            observations.append(calculator(payload))

    if not observations:
        return "No action was needed."

    return "\n".join(observations)


def main() -> None:
    task = "Explain RAG quickly and compute 2+2"
    print("Task:", task)
    print("Result:")
    print(run_agent(task))


if __name__ == "__main__":
    main()
