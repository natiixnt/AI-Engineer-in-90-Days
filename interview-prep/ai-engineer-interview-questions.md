# AI Engineer Interview Questions

Practical interview questions focused on day-to-day AI engineering work in production systems.

## 1) ML Engineer vs AI Engineer

**Question**
What is the difference between an ML engineer and an AI engineer?

**Why It Matters**
Teams hire for different responsibilities. Mixing these roles can cause poor ownership and delivery gaps.

**Short Answer**
An ML engineer usually focuses on training, validating, and serving predictive models from structured data. An AI engineer focuses on building end-to-end AI applications that combine LLMs, retrieval, prompting, tools, APIs, and monitoring. In practice, AI engineers spend more time on orchestration, system behavior, and runtime reliability. ML engineers often go deeper into feature engineering, model training pipelines, and statistical performance.

**Deep Dive (Optional)**
In modern teams, the roles overlap, but the center of gravity differs: model-centric optimization versus application-centric integration. AI engineering includes product constraints like latency, cost, safety, and prompt/tool behavior.

**Example Code (when relevant)**
```python
# AI engineer style orchestration flow
question = "How do I reduce RAG latency?"
chunks = retrieve(question)
answer = llm_generate(question, chunks)
log_trace(question, chunks, answer)
```

## 2) Embeddings vs Fine-Tuning

**Question**
When should you use embeddings instead of fine-tuning?

**Why It Matters**
Choosing the wrong approach can waste weeks and budget.

**Short Answer**
Use embeddings when you need retrieval, search, clustering, or context injection from external knowledge. Use fine-tuning when model behavior itself must change consistently across many prompts, such as output format, tone, or domain-specific reasoning patterns. Most teams should start with embeddings + prompt engineering because it is faster and easier to iterate. Fine-tuning is usually a second step after baseline gaps are clearly measured.

**Deep Dive (Optional)**
Embeddings solve knowledge access; fine-tuning changes model parameters. If your issue is missing facts, retrieval usually helps more than fine-tuning.

**Example Code (when relevant)**
```python
# Embedding-first baseline
query_vec = embed("How do I evaluate a RAG system?")
top_chunks = vector_index.search(query_vec, k=3)
answer = llm_generate_with_context(top_chunks)
```

## 3) Prompt Engineering in Production

**Question**
What does prompt engineering mean in production AI systems?

**Why It Matters**
Prompt quality directly affects reliability, cost, and safety.

**Short Answer**
Prompt engineering means designing stable instructions that produce predictable model behavior under real traffic. In production, prompts are templates with strict roles, output contracts, and fallback behavior. Good prompts reduce hallucinations, improve tool usage, and simplify downstream parsing. They should be versioned and tested just like code.

**Deep Dive (Optional)**
Use prompt layers: system policy, task instructions, retrieved context, and output schema. Evaluate each version on a fixed regression set before rollout.

**Example Code (when relevant)**
```python
def build_prompt(question: str, context: str) -> str:
    return (
        "You are a grounded assistant.\n"
        "Answer only from context.\n"
        "If unsure, say: I don't know.\n\n"
        f"Question: {question}\n"
        f"Context:\n{context}\n"
        "Return JSON with keys: answer, confidence."
    )
```

## 4) Hallucination Mitigation

**Question**
How do you reduce hallucinations in LLM applications?

**Why It Matters**
Hallucinations break trust and can create serious product risk.

**Short Answer**
Start by grounding responses with retrieval or verified tools instead of pure generation. Constrain prompts to require citations or explicit uncertainty when evidence is missing. Add output checks for unsupported claims and run high-risk responses through a verifier step. Finally, monitor hallucination rates in production with labeled samples.

**Deep Dive (Optional)**
Hallucination mitigation is a system property, not a single prompt trick. Retrieval quality, prompt constraints, and evaluation gates all matter together.

**Example Code (when relevant)**
```python
def is_supported(answer: str, context: str) -> bool:
    # Simple baseline check: improve with claim-level verification later.
    return any(sentence in context for sentence in answer.split(". ")[:2])
```

## 5) Evaluating LLM Systems

**Question**
How do you evaluate an LLM system before release?

**Why It Matters**
Without structured evaluation, quality regressions go live unnoticed.

**Short Answer**
Define a representative evaluation set from real user tasks and edge cases. Measure task success, faithfulness, latency, and cost, not just one quality score. Compare prompt/model versions with the same test set and fixed thresholds. Add regression checks in CI/CD and monitor drift after deployment.

**Deep Dive (Optional)**
Combine offline evaluation with online signals (thumbs-up rate, escalation rate, task completion) for a complete picture.

**Example Code (when relevant)**
```python
def evaluate_case(pred: str, expected: str) -> float:
    return 1.0 if expected.lower() in pred.lower() else 0.0

scores = [evaluate_case(run_model(x), y) for x, y in eval_set]
print("avg_score=", sum(scores) / len(scores))
```
