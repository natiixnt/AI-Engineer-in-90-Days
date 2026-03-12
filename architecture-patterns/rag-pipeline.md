# RAG Pipeline Pattern

## When to Use It
Use this pattern when answers must be grounded in changing or private knowledge (docs, internal wikis, policies, product manuals).

## Architecture Overview
- Ingest documents and split into chunks.
- Generate embeddings and index chunks in vector store.
- Retrieve top-k chunks for each query.
- Assemble grounded prompt with citations.
- Generate answer and return with evidence.

## Pros and Cons
**Pros**
- Better factual grounding.
- Works with private/up-to-date data.
- Easier to audit with citations.

**Cons**
- More moving parts and operational overhead.
- Retrieval quality can bottleneck final answer quality.
- Requires ongoing indexing and evaluation discipline.

## Common Failure Modes
- Irrelevant retrieval due to poor chunking/embedding choices.
- Correct chunks retrieved but prompt fails to enforce grounding.
- Stale indexes causing outdated answers.

## Implementation Notes
- Measure retrieval and generation separately.
- Keep chunk IDs and source metadata in traces.
- Start simple (`k` small, deterministic prompt), then add reranking.
