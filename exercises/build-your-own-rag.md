# Build Your Own RAG

Build a minimal Retrieval-Augmented Generation pipeline that answers questions using retrieved context instead of relying on model memory alone. This is one of the most practical patterns in AI engineering for grounded answers.

## Concepts Practiced
- chunking
- retrieval pipelines
- embeddings
- context assembly
- prompt design

## System Overview
You will build a 4-stage RAG pipeline:

1. **Document processing**: chunk source text into retrievable pieces.
2. **Retrieval**: embed question and retrieve relevant chunks.
3. **Prompt assembly**: build a prompt with strict context boundaries.
4. **Generation**: produce an answer grounded in retrieved context.

## Implementation Steps
1. Load a small set of documents.
2. Split each document into chunks and keep source metadata.
3. Generate embeddings for chunks and build a search index.
4. Create a `retrieve(question, k)` function.
5. Build a prompt template that includes only retrieved chunks.
6. Call an LLM with the assembled prompt.
7. Return answer plus cited chunk IDs.
8. Evaluate whether answers remain faithful to retrieved context.

## Starter Code
```python
from __future__ import annotations


def build_prompt(question: str, chunks: list[dict]) -> str:
    context_block = "\n".join(
        f"[{chunk['id']}] {chunk['text']}" for chunk in chunks
    )
    return (
        "You are a grounded assistant.\n"
        "Answer only from the context.\n"
        "If context is missing, say you are unsure.\n\n"
        f"Question: {question}\n\n"
        f"Context:\n{context_block}\n\n"
        "Answer:"
    )


def rag_answer(question: str) -> dict:
    # TODO: retrieve top-k chunks with your vector index
    retrieved_chunks = [
        {"id": "chunk-1", "text": "Replace this with retrieved context."},
        {"id": "chunk-2", "text": "Use your own retrieval pipeline."},
    ]
    prompt = build_prompt(question, retrieved_chunks)

    # TODO: call your LLM client here
    answer = "Replace with model output"

    return {
        "question": question,
        "answer": answer,
        "citations": [chunk["id"] for chunk in retrieved_chunks],
    }
```

## Hints
- Include chunk IDs in context so citations are easy.
- Keep prompts short; too much context can reduce precision.
- Always inspect retrieved chunks before debugging generation.

## Extension Ideas
- Add query rewriting before retrieval.
- Add reranking after initial retrieval.
- Add a faithfulness check comparing answer claims to context.
- Support multi-document answers with grouped citations.
