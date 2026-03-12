# AI System Design Interview Questions

Practical system design prompts for AI engineering interviews, focused on architecture and tradeoffs.

## 1) Design a RAG Chatbot

**Question**
How would you design a production RAG chatbot for internal knowledge?

**Why It Matters**
This is a common real-world use case in enterprise AI adoption.

**Short Answer**
Start with an ingestion pipeline that chunks documents, generates embeddings, and indexes them with metadata. At runtime, retrieve top-k chunks, rerank if needed, and build a grounded prompt for generation. Add citation output, latency budgets, caching, and fallback behavior for low-confidence retrieval. Instrument the system with trace IDs and quality metrics.

**Deep Dive (Optional)**
Design for freshness: incremental re-indexing, source-of-truth checks, and rollback for bad ingestions.

**Example Code (when relevant)**
```python
pipeline = {
    "ingestion": ["parse", "chunk", "embed", "index"],
    "runtime": ["retrieve", "rerank", "generate", "cite"],
    "ops": ["log", "evaluate", "alert"],
}
```

## 2) Design a Document Search Assistant

**Question**
How would you design an assistant focused on high-precision document search?

**Why It Matters**
Many users want retrieval-first workflows before any generation.

**Short Answer**
Prioritize retrieval quality with clean metadata, hybrid search (keyword + vector), and robust filtering. Return ranked snippets with source location and confidence, then optionally offer summarization. Include query rewriting and reranking for better precision. Evaluate with Recall@k and click-through quality.

**Deep Dive (Optional)**
Treat summarization as a separate stage so retrieval can be debugged independently.

**Example Code (when relevant)**
Not required for this question.

## 3) Design an AI Coding Assistant

**Question**
How would you design an AI coding assistant for a large codebase?

**Why It Matters**
Code assistants must be accurate, context-aware, and safe with tool usage.

**Short Answer**
Use code-aware indexing by file path, symbols, and repository metadata. Retrieve relevant files/chunks based on task intent and include strict constraints in prompts. Add tool calls for search, linting, tests, and diff generation with sandboxed execution. Log every action and require confirmation for risky operations.

**Deep Dive (Optional)**
Add repository-specific style rules and eval suites to prevent regressions in generated changes.

**Example Code (when relevant)**
```python
assistant_tools = ["code_search", "run_tests", "apply_patch", "create_diff"]
```

## 4) Scaling an LLM Application

**Question**
How do you scale an LLM application from prototype to production traffic?

**Why It Matters**
Scaling failures quickly become latency, cost, and reliability incidents.

**Short Answer**
Introduce caching, async processing, and model routing by task complexity. Add concurrency controls, queueing, retries, and timeouts for external dependencies. Track p50/p95 latency, token usage, and error rates by endpoint. Define SLOs and graceful degradation strategies.

**Deep Dive (Optional)**
Use canary releases for prompt/model changes and compare online metrics before full rollout.

**Example Code (when relevant)**
```python
def choose_model(task: str) -> str:
    return "small-model" if len(task) < 200 else "large-model"
```

## 5) Monitoring AI Systems

**Question**
What should you monitor in a production AI system?

**Why It Matters**
Without monitoring, quality regressions are detected too late.

**Short Answer**
Monitor four groups: quality (task success, faithfulness), reliability (errors, retries), performance (latency), and cost (tokens, spend). Track these by segment such as query type, language, and customer tier. Add alert thresholds and investigate drift over time. Include both offline evaluation dashboards and online user feedback signals.

**Deep Dive (Optional)**
A useful baseline is to connect each user request to a trace that stores prompt, context, model output, and evaluation metadata.

**Example Code (when relevant)**
```python
metrics = {
    "faithfulness": 0.91,
    "p95_latency_ms": 1840,
    "cost_per_1k_requests_usd": 12.4,
    "error_rate": 0.007,
}
```
