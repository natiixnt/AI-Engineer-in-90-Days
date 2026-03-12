# AI Engineering Glossary

Practical, beginner-friendly definitions of common AI engineering terms.

## Embeddings
Numerical vectors that represent text (or other data) so similar meaning is close in vector space. In practice, embeddings are used for search, retrieval, clustering, and recommendations.

## Chunking
Splitting a large document into smaller pieces before indexing or prompting. Good chunking improves retrieval quality and helps fit context limits.

## Reranking
A second-pass sorting step that reorders retrieved results with a stronger relevance model. It usually improves top results but adds some latency.

## Context Window
The maximum amount of tokens a model can process in one request (input + output). If your prompt exceeds this limit, content is truncated or rejected.

## Hallucination
When a model generates incorrect or unsupported information with high confidence. This is reduced by grounding, verification, and better prompts.

## Tool Calling
A mechanism where the model requests structured function/tool execution (for example search, calculator, API). It improves reliability for tasks that need external data or actions.

## Vector Database
A storage and query system optimized for vector similarity search. It is commonly used to retrieve relevant chunks in RAG systems.

## Tracing
Capturing end-to-end runtime details for each request (prompt, retrieved context, tool calls, output, latency). Traces are essential for debugging and regressions.

## Eval Set
A curated dataset of test inputs and expected outcomes used to measure system quality consistently. It helps compare prompt/model changes objectively.

## Guardrails
Rules and checks that constrain model behavior for safety and reliability. Examples include input filters, output validators, policy prompts, and tool permission controls.
