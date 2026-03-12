# Build Your Own Agent

Build a small AI agent that selects tools, executes actions, and updates its plan based on observations. This matters because many real AI systems need multi-step reasoning and external tool usage.

## Concepts Practiced
- agents
- tool usage
- planning
- observation-action loops
- task decomposition

## System Overview
You will implement an agent loop with clear control flow:

1. **Planner**: decide the next action from task + state.
2. **Tool layer**: execute capabilities (search, calculator, API call).
3. **Memory/state**: store observations from each step.
4. **Stop condition**: finish when task is solved or max steps reached.

## Implementation Steps
1. Define a task input format.
2. Implement 2-3 tools with strict input/output schemas.
3. Create `choose_action(state)` to pick the next tool.
4. Run an action-observation loop for a fixed number of steps.
5. Append each tool result to state memory.
6. Generate a final response from accumulated observations.
7. Add simple safety checks for unsafe tool inputs.

## Starter Code
```python
from __future__ import annotations


def search_docs(query: str) -> str:
    docs = {
        "rag": "RAG combines retrieval and generation.",
        "eval": "Evaluation uses precision, relevance, and faithfulness.",
    }
    return docs.get(query.lower(), "No result")


def calculator(expression: str) -> str:
    allowed = set("0123456789+-*/(). ")
    if any(ch not in allowed for ch in expression):
        return "Unsafe expression"
    return str(eval(expression, {"__builtins__": {}}, {}))


def choose_action(task: str, history: list[str]) -> tuple[str, str]:
    # TODO: replace with dynamic planning logic
    if not history:
        return ("search_docs", "rag")
    if len(history) == 1:
        return ("calculator", "2+2")
    return ("finish", "")


# TODO:
# 1) implement run_agent(task, max_steps)
# 2) execute tools based on choose_action
# 3) collect observations and return final answer
```

## Hints
- Store action, input, and output for each step to make debugging easy.
- Add a max step limit to avoid infinite loops.
- Keep tool outputs short and structured.

## Extension Ideas
- Add long-term memory between runs.
- Let an LLM generate the plan dynamically.
- Add a browser/search API tool.
- Add tool confidence scoring and fallback logic.
