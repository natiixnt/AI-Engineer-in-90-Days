# Debugging AI Systems

A practical guide for debugging common failures in production AI applications.

## Debugging Checklist

Use this checklist before changing prompts or models:

- Reproduce the issue with a fixed input and save a `trace_id`.
- Log full pipeline state: query, retrieved context, prompt, tool calls, output, latency.
- Compare failing trace with a known-good trace.
- Isolate one stage at a time (retrieval, prompt, tools, agent loop, generation).
- Measure before/after metrics for every fix.
- Add a regression test for the failure case.

## Practical Inspection Steps

1. Capture one failing request with full artifacts.
2. Verify retrieval quality first (wrong context causes downstream failures).
3. Check prompt instructions and output constraints.
4. Inspect tool argument payloads, errors, and timeout behavior.
5. Review agent step history for loops or no-progress actions.
6. Break down latency by stage and identify the slowest component.
7. Re-run after fix and compare metrics against baseline.

## 1) Poor Retrieval Quality

### What Goes Wrong
The system retrieves weakly related chunks, so answers become generic or incorrect.

### Why It Happens
Chunking is suboptimal, embedding quality is weak, metadata filters are too strict, or query normalization is missing.

### How to Mitigate It
Tune chunk size/overlap, validate embedding model choice, improve query rewriting, and add reranking for top-k candidates.

### Metrics to Look At
- `Recall@k`
- `Precision@k`
- retrieval hit rate on labeled queries
- average similarity score of top result

### Simple Example
```python
def debug_retrieval(query: str, retriever) -> None:
    results = retriever.search(query, k=5)
    print(f"query={query}")
    for rank, row in enumerate(results, start=1):
        print(f"{rank}. score={row['score']:.3f} id={row['id']} text={row['text'][:80]}")
```

## 2) Hallucinations

### What Goes Wrong
The model returns confident claims that are not supported by available context.

### Why It Happens
Generation is not grounded strongly enough, context is incomplete, or no verification step exists.

### How to Mitigate It
Use grounded prompts with citation requirements, add evidence checks, and return uncertainty when support is missing.

### Metrics to Look At
- faithfulness score
- unsupported-claim rate
- citation coverage (claims with source)
- user correction / escalation rate

### Simple Example
```python
def has_citation(answer: str) -> bool:
    # Minimal check: expects references like [chunk-12]
    return "[chunk-" in answer
```

## 3) Weak Prompts

### What Goes Wrong
Outputs are inconsistent, off-format, or ignore important constraints.

### Why It Happens
Instructions are ambiguous, role hierarchy is unclear, or prompts are too long and noisy.

### How to Mitigate It
Use strict system prompts, short task instructions, explicit output schema, and prompt regression tests.

### Metrics to Look At
- format validity rate
- task success rate on eval set
- refusal correctness rate (for out-of-scope requests)
- output variance across repeated runs

### Simple Example
```python
def format_valid(output: dict) -> bool:
    required = {"answer", "confidence"}
    return required.issubset(output.keys())
```

## 4) Tool Failures

### What Goes Wrong
Tool calls fail, return malformed data, or timeout under load.

### Why It Happens
Arguments are invalid, schemas are weak, dependency services are unstable, or retry strategy is missing.

### How to Mitigate It
Validate tool inputs with strict schemas, add retries with backoff, set timeouts, and define fallbacks.

### Metrics to Look At
- tool success rate
- timeout rate
- invalid-argument rate
- fallback usage rate

### Simple Example
```python
def safe_tool_call(tool_fn, args: dict):
    if "city" not in args:
        return {"ok": False, "error": "missing city"}
    try:
        return {"ok": True, "data": tool_fn(**args)}
    except Exception as exc:
        return {"ok": False, "error": str(exc)}
```

## 5) Agent Loops

### What Goes Wrong
The agent repeats actions without progress or never reaches a stop condition.

### Why It Happens
Planning policy is weak, stop conditions are missing, and state tracking is incomplete.

### How to Mitigate It
Add max-step limits, no-progress detection, action deduplication, and explicit termination criteria.

### Metrics to Look At
- average steps per task
- completion rate
- repeated-action ratio
- forced-stop rate

### Simple Example
```python
def repeated_action_ratio(actions: list[str]) -> float:
    if not actions:
        return 0.0
    repeats = sum(1 for i in range(1, len(actions)) if actions[i] == actions[i - 1])
    return repeats / max(1, len(actions) - 1)
```

## 6) Latency Issues

### What Goes Wrong
Responses are slow or unstable, causing poor UX and higher infrastructure cost.

### Why It Happens
Large prompts, slow retrieval/tool dependencies, and no stage-level latency budgets.

### How to Mitigate It
Track per-stage latency, trim context, cache repeated work, and route simple tasks to smaller models.

### Metrics to Look At
- end-to-end latency (`p50`, `p95`, `p99`)
- per-stage latency (retrieval, LLM, tools)
- tokens per request
- timeout and retry counts

### Simple Example
```python
import time


def timed(label: str, fn, *args, **kwargs):
    start = time.perf_counter()
    out = fn(*args, **kwargs)
    elapsed_ms = (time.perf_counter() - start) * 1000
    print(f"{label}: {elapsed_ms:.1f}ms")
    return out
```

## Fast Triage Order

When multiple failures appear at once, debug in this order:

1. retrieval quality
2. prompt quality
3. tool correctness
4. agent loop behavior
5. generation faithfulness
6. performance and latency

This order usually finds the root cause faster than tuning prompts first.
