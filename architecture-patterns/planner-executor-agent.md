# Planner-Executor Agent Pattern

## When to Use It
Use this pattern for open-ended tasks that require multi-step decomposition, adaptive planning, and multiple tools.

## Architecture Overview
- Planner creates or updates step plan from task + current state.
- Executor runs one selected action/tool.
- Observer stores result and updates memory/state.
- Loop continues until goal met or termination condition reached.

## Pros and Cons
**Pros**
- Flexible for complex workflows.
- Can adapt when intermediate steps fail.
- Good fit for research/automation tasks.

**Cons**
- Harder to test and debug than deterministic flows.
- Higher latency and cost from multi-step loops.
- Greater risk of loops or unproductive actions.

## Common Failure Modes
- Repeated actions with no progress.
- Overly broad planning with unclear stop criteria.
- Unsafe tool usage from untrusted instructions.

## Implementation Notes
- Add hard limits: max steps, max runtime, tool budgets.
- Log full step traces (`plan -> action -> observation`).
- Start with deterministic planner heuristics before full LLM planning.
