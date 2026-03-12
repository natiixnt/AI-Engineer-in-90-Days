# From Prototype to Production

A practical path for turning a notebook or script into a production-ready AI application.

## 1) Refactor Into Modules

### Goal
Move from one-file logic to clear, testable components.

### What to Do
- Split code into modules: `ingestion`, `retrieval`, `generation`, `api`, `evaluation`.
- Extract configuration to environment variables and typed settings.
- Replace ad-hoc notebook cells with callable functions and CLI entry points.

### Minimal Target Structure
```text
app/
  config.py
  retrieval.py
  generation.py
  service.py
  api.py
tests/
```

### Practical Tip
If a function depends on global state, refactor it first. Global state causes most production regressions.

## 2) Add an API Layer

### Goal
Expose your AI workflow as a stable service interface.

### What to Do
- Add REST endpoints (`/health`, `/ask`, `/metrics`).
- Define request/response schemas with validation.
- Return trace IDs and stable error codes.

### Practical Tip
Start with synchronous endpoints for simplicity, then add async jobs only if task duration requires it.

## 3) Add Logging and Tracing

### Goal
Make failures explainable and reproducible.

### What to Do
- Log request metadata, prompt version, retrieved chunk IDs, tool calls, latency.
- Use structured JSON logs for easy querying.
- Assign one trace ID per request and pass it through all stages.

### Practical Tip
Log enough to debug, but avoid logging sensitive content in plaintext.

## 4) Add Evaluation

### Goal
Prevent quality regressions before deployment.

### What to Do
- Build a small eval set from real representative tasks.
- Add baseline metrics: retrieval quality, answer quality, faithfulness, latency.
- Run eval in CI for every prompt/model change.

### Practical Tip
Start with 20-50 high-value test cases before scaling dataset size.

## 5) Add Monitoring

### Goal
Detect production issues quickly.

### What to Do
- Track p50/p95 latency, error rate, token/cost usage, and quality proxy signals.
- Add alert thresholds for spikes and sudden regressions.
- Segment metrics by route, tenant, and model version.

### Practical Tip
Dashboards should answer: "what broke, where, and since when?"

## 6) Prepare Deployment

### Goal
Ship changes safely and roll back quickly.

### What to Do
- Containerize service (Docker) and pin runtime dependencies.
- Use staged environments (`dev`, `staging`, `prod`).
- Deploy with canary or blue/green strategy.
- Document rollback and incident response steps.

### Practical Tip
If rollback is not rehearsed, deployment is not production-ready.

## 7) Implement Failure Handling

### Goal
Fail gracefully instead of crashing or returning misleading answers.

### What to Do
- Add timeouts and retries for model/tool/network calls.
- Add fallback responses for retrieval/model failures.
- Enforce max steps for agents and max token budgets for prompts.
- Surface meaningful user-safe errors.

### Practical Tip
Handle failures per stage (retrieval, tools, generation) with distinct error codes.

## Production Readiness Checklist

Use this quick gate before launch:

- [ ] Modular code with tests for core paths
- [ ] Stable API contracts and validation
- [ ] Structured logs + end-to-end trace IDs
- [ ] Regression eval pipeline with pass thresholds
- [ ] Monitoring dashboard and alerts
- [ ] Safe deployment strategy and tested rollback
- [ ] Failure handling and graceful degradation

## Suggested Rollout Path

1. notebook/script proof of concept
2. modular service with tests
3. API + logging + eval
4. staging soak test with synthetic and real traffic
5. limited production canary
6. full rollout with active monitoring

This sequence minimizes risk while keeping delivery velocity high.
