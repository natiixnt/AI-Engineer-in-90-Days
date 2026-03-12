# Vector Databases Comparison

Concise engineering comparison for common vector storage options.

## FAISS
- **What it is good for:** Local prototypes, offline batch retrieval, single-host indexing.
- **Strengths:** Fast ANN search, no external service required, highly flexible.
- **Weaknesses:** No built-in multi-tenant API/service layer, more manual ops for production.
- **When to choose it:** Early-stage prototypes or embedded retrieval inside one service.

## Chroma
- **What it is good for:** Lightweight developer workflows and quick RAG experiments.
- **Strengths:** Simple API, easy local usage, low setup overhead.
- **Weaknesses:** Not ideal for high-scale production workloads without extra engineering.
- **When to choose it:** MVP phase when speed of iteration matters most.

## Qdrant
- **What it is good for:** Production vector search with filtering and scalable deployment.
- **Strengths:** Strong metadata filtering, good performance, self-host or managed options.
- **Weaknesses:** More infrastructure complexity than local-only options.
- **When to choose it:** Production RAG systems needing filter-heavy retrieval and reliable APIs.

## Pinecone
- **What it is good for:** Managed vector infrastructure with minimal operational burden.
- **Strengths:** Fast time-to-production, managed scaling, reduced ops workload.
- **Weaknesses:** Vendor lock-in risk and potentially higher long-term cost.
- **When to choose it:** Teams prioritizing delivery speed over owning vector infra.

## Weaviate
- **What it is good for:** Vector + structured/hybrid search with rich schema support.
- **Strengths:** Flexible query model, hybrid retrieval, self-host or managed deployments.
- **Weaknesses:** More setup and operational learning curve.
- **When to choose it:** Applications needing hybrid search and richer data modeling.
