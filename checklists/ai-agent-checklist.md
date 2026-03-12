# AI Agent Production Checklist

Practical production checklist for deploying AI agents with tools and multi-step behavior.

## Reliability

- [ ] Agent has explicit max-step and timeout limits.
- [ ] Tool failures do not crash the full workflow.
- [ ] Stop conditions are deterministic and tested.
- [ ] Fallback path exists when planning fails.

## Latency

- [ ] Per-step latency budget is defined and enforced.
- [ ] Tool calls have strict timeouts and retry strategy.
- [ ] Long agent runs support cancellation and partial results.
- [ ] Expensive tools are gated by confidence or decision thresholds.

## Observability

- [ ] Full action log is captured (`plan -> action -> observation -> decision`).
- [ ] Each tool call logs input, output, latency, and status.
- [ ] Repeated-action and loop-detection metrics are tracked.
- [ ] Traces link final answer to intermediate steps and tools used.

## Evaluation

- [ ] Task-level success criteria are defined per agent use case.
- [ ] Eval set includes multi-step and adversarial scenarios.
- [ ] Metrics include completion rate, tool accuracy, and forced-stop rate.
- [ ] Regression tests run after planner/prompt/tool updates.

## Safety

- [ ] Tool permissions are least-privilege and scoped by task.
- [ ] High-risk tools require explicit approval or human-in-the-loop.
- [ ] Untrusted inputs are sanitized before tool execution.
- [ ] Sandbox boundaries are enforced for shell/code execution tools.

## API Design

- [ ] API exposes task status (`queued`, `running`, `completed`, `failed`).
- [ ] Response includes step summary, tool usage, and trace ID.
- [ ] Idempotency key support exists for retried task submissions.
- [ ] Async endpoint is available for long-running agent tasks.

## Deployment Considerations

- [ ] Queueing/backpressure strategy exists for burst traffic.
- [ ] Background workers are monitored and autoscaled.
- [ ] Feature flags allow gradual agent capability rollout.
- [ ] Incident runbook includes tool outage and loop-storm scenarios.
