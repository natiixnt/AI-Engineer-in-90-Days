# RAG Interview Questions

Practical interview questions about Retrieval-Augmented Generation design, quality, and scaling.

## 1) What Is RAG?

**Question**
What is Retrieval-Augmented Generation (RAG)?

**Why It Matters**
RAG is one of the most common production patterns for grounded AI applications.

**Short Answer**
RAG combines retrieval and generation in one pipeline. The system first retrieves relevant external context, then asks the LLM to answer using that context. This improves factuality and keeps answers tied to known sources. It is especially useful when knowledge changes frequently.

**Deep Dive (Optional)**
A full RAG stack usually includes ingestion, chunking, embeddings, indexing, retrieval, prompt assembly, and evaluation.

**Example Code (when relevant)**
```python
chunks = retrieve("How to evaluate RAG?")
answer = generate_answer("How to evaluate RAG?", chunks)
```

## 2) Why Use RAG?

**Question**
Why is RAG often preferred over relying only on model memory?

**Why It Matters**
This is a core architectural decision in most enterprise AI products.

**Short Answer**
Model memory is static and can be outdated or incomplete for your domain. RAG allows the model to use current, private, and source-controlled knowledge at runtime. It also improves auditability because you can inspect retrieved chunks. In many cases it is cheaper and faster to update data than to retrain or fine-tune.

**Deep Dive (Optional)**
RAG does not solve everything; poor retrieval quality can still cause bad answers. You must evaluate retrieval and generation together.

**Example Code (when relevant)**
Not required for this question.

## 3) Chunking Strategies

**Question**
How do chunking strategies affect RAG performance?

**Why It Matters**
Chunking is a top source of retrieval failures in real systems.

**Short Answer**
Small chunks can improve precision but may lose context. Large chunks keep context but can dilute relevance and increase token usage. Overlap helps preserve continuity across boundaries. The right choice depends on document type, query style, and model context budget.

**Deep Dive (Optional)**
Evaluate chunk size and overlap empirically using retrieval metrics and task success, not intuition alone.

**Example Code (when relevant)**
```python
def chunk(words: list[str], size: int = 120, overlap: int = 20) -> list[str]:
    step = max(1, size - overlap)
    return [" ".join(words[i:i + size]) for i in range(0, len(words), step)]
```

## 4) Retrieval Evaluation

**Question**
How do you evaluate retrieval quality in a RAG system?

**Why It Matters**
If retrieval is weak, generation quality will be unstable regardless of prompt quality.

**Short Answer**
Use a labeled query-to-relevant-chunk dataset and measure metrics like Recall@k and Precision@k. Track these metrics by query type, not only globally. Inspect failure cases manually to diagnose indexing, chunking, or embedding problems. Retrieval metrics should be monitored continuously after data updates.

**Deep Dive (Optional)**
Also track MRR (Mean Reciprocal Rank) when ranking order matters for downstream generation.

**Example Code (when relevant)**
```python
def recall_at_k(retrieved_ids: list[str], relevant_ids: set[str], k: int) -> float:
    top_k = set(retrieved_ids[:k])
    return len(top_k & relevant_ids) / max(1, len(relevant_ids))
```

## 5) Reranking

**Question**
What is reranking in RAG and when should you use it?

**Why It Matters**
Initial vector retrieval may return roughly relevant chunks but miss the best ordering.

**Short Answer**
Reranking is a second pass that reorders retrieved candidates with a stronger relevance model. It is useful when top-k quality is inconsistent or context windows are tight. A common pattern is retrieve 20 chunks, rerank, and keep the best 3-5. This often improves final answer quality with moderate latency cost.

**Deep Dive (Optional)**
You can rerank with cross-encoders or LLM-based scoring depending on latency and budget constraints.

**Example Code (when relevant)**
```python
candidates = vector_index.search(query_vec, k=20)
reranked = sorted(candidates, key=lambda c: rerank_score(query, c["text"]), reverse=True)
final_context = reranked[:4]
```

## 6) Context Window Limits

**Question**
How do context window limits impact RAG design?

**Why It Matters**
Token limits drive both quality and cost in production.

**Short Answer**
Even large-context models have practical limits due to latency and attention dilution. Passing too much context can reduce answer precision and increase cost. Good RAG systems budget tokens across system prompt, user question, and retrieved chunks. They also prioritize or compress context before generation.

**Deep Dive (Optional)**
Use dynamic context assembly: select high-confidence chunks first, then add extra context only when needed.

**Example Code (when relevant)**
```python
def fit_context(chunks: list[str], max_tokens: int = 1200) -> list[str]:
    kept, used = [], 0
    for text in chunks:
        est = max(1, len(text.split()) // 0.75)  # rough estimate
        if used + est > max_tokens:
            break
        kept.append(text)
        used += est
    return kept
```
