# Common Failure Modes in AI Systems

Practical failure patterns you will see in production AI systems, with fast mitigation playbooks.

## RAG Systems

### 1) Irrelevant Retrieval Results
- **What goes wrong:** Retrieved chunks are weakly related to the query, so answers drift or become generic.
- **Why it happens:** Poor chunking, weak embeddings, or missing query normalization reduce similarity quality.
- **How to mitigate it:** Tune chunk size/overlap, test better embedding models, and add query rewriting before retrieval.

### 2) Correct Retrieval, Wrong Final Answer
- **What goes wrong:** The right chunks are retrieved, but the model still answers incorrectly.
- **Why it happens:** Prompt does not enforce grounding, or context is too long/noisy.
- **How to mitigate it:** Use strict grounded prompts, limit context to top-k relevant chunks, and require citations.

### 3) Missing Critical Context
- **What goes wrong:** Key facts are absent from context, causing partial or wrong answers.
- **Why it happens:** Incomplete indexing pipeline, stale data, or metadata filters that are too restrictive.
- **How to mitigate it:** Add ingestion checks, track index freshness, and audit filter logic with recall tests.

## LLM Applications

### 1) Hallucinated Facts
- **What goes wrong:** Model outputs confident but incorrect claims.
- **Why it happens:** Open-ended prompts and no grounding or post-check stage.
- **How to mitigate it:** Add retrieval/tool checks, force uncertainty responses when evidence is missing, and add fact-check steps.

### 2) Prompt Injection Through User Input
- **What goes wrong:** User text overrides instructions or attempts to exfiltrate hidden context.
- **Why it happens:** System and user instructions are mixed without clear boundaries.
- **How to mitigate it:** Separate system policy from user content, sanitize untrusted text, and constrain tool access.

### 3) High Latency and Cost Spikes
- **What goes wrong:** Response times and token bills grow quickly under load.
- **Why it happens:** Overlong prompts, unnecessary large models, and no caching.
- **How to mitigate it:** Reduce prompt size, route by task complexity, cache repeated calls, and monitor token usage by endpoint.

## AI Agents

### 1) Infinite or Unproductive Tool Loops
- **What goes wrong:** Agent repeatedly calls tools without progressing.
- **Why it happens:** Weak stop criteria and no explicit success conditions.
- **How to mitigate it:** Add max-step limits, termination checks, and state-based progress scoring.

### 2) Wrong Tool Selection
- **What goes wrong:** Agent picks an inappropriate tool or malformed tool arguments.
- **Why it happens:** Ambiguous tool descriptions and missing schema validation.
- **How to mitigate it:** Improve tool specs, validate arguments against strict schemas, and add fallback handling.

### 3) Unsafe Tool Execution
- **What goes wrong:** Agent triggers risky actions (shell, network, code execution) from untrusted prompts.
- **Why it happens:** No sandboxing or permission model around tool calls.
- **How to mitigate it:** Run tools in restricted environments, add allowlists, and require human approval for sensitive actions.

## Evaluation Pipelines

### 1) Metrics Do Not Match Real User Quality
- **What goes wrong:** Offline scores look good, but users report poor answers.
- **Why it happens:** Evaluation set is narrow or not representative of production traffic.
- **How to mitigate it:** Build realistic eval datasets from real queries and track segment-level performance.

### 2) Faithfulness Is Not Measured
- **What goes wrong:** System appears accurate but often invents unsupported statements.
- **Why it happens:** Pipeline tracks only relevance/helpfulness and ignores grounding.
- **How to mitigate it:** Add faithfulness metrics, citation checks, and automated contradiction detection.

### 3) Regressions Go Unnoticed
- **What goes wrong:** Model or prompt changes silently reduce quality.
- **Why it happens:** No continuous eval gates in CI/CD.
- **How to mitigate it:** Run regression suites on each change, define pass/fail thresholds, and alert on metric drift.
