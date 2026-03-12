# Build vs Buy Decisions in AI Engineering

Practical trade-offs for choosing architecture and tooling in real AI products.

## How to Use This Guide

For each decision, evaluate these dimensions first:

- required reliability and SLA
- team size and skills
- expected scale (QPS, data size, monthly traffic)
- security/compliance constraints
- total cost over 6-12 months (not only month 1)

## 1) Local Vector Search vs Managed Vector Database

### Local Vector Search (Build)
Use local or self-hosted indexing when:

- you are prototyping and need fast iteration
- dataset is small/medium and team can operate infrastructure
- strict data residency or offline requirements exist

### Managed Vector DB (Buy)
Use managed infrastructure when:

- you need high uptime, backups, and multi-tenant reliability
- traffic and index size grow quickly
- your team should focus on product logic, not infra operations

### Practical Trade-off
Local search is cheaper initially but operational overhead increases with scale (monitoring, failover, compaction, indexing jobs). Managed DBs reduce ops risk and accelerate delivery, but lock-in and long-term cost can be higher.

### Default Recommendation
Start local for early validation, migrate to managed once uptime and scaling requirements become business-critical.

## 2) Framework vs Plain Python

### Framework (Buy)
Frameworks (LangChain, LlamaIndex, etc.) help when:

- you need many integrations quickly
- team is new to AI orchestration patterns
- speed of experimentation matters more than fine-grained control

### Plain Python (Build)
Prefer plain Python when:

- system behavior must be explicit and debuggable
- latency/cost tuning requires tight control
- you want minimal abstraction and easier long-term maintenance

### Practical Trade-off
Frameworks reduce time-to-first-demo but can hide complexity and add version churn. Plain Python takes longer at first, but often gives clearer control paths and easier debugging in production.

### Default Recommendation
Prototype with lightweight abstractions, then keep core production path in explicit Python modules.

## 3) RAG vs Fine-Tuning

### RAG (Build Data Layer)
Use RAG when:

- you need up-to-date or private knowledge
- source citations and auditability matter
- content changes frequently

### Fine-Tuning (Buy/Train Model Behavior)
Use fine-tuning when:

- you need consistent behavior/style across many requests
- prompt-only approaches cannot achieve required reliability
- you have a high-quality labeled dataset

### Practical Trade-off
RAG solves knowledge access; fine-tuning changes model behavior. Fine-tuning without good data can degrade quality. RAG usually has lower risk and faster iteration for knowledge-heavy tasks.

### Default Recommendation
Start with RAG + prompt engineering + evaluation. Fine-tune only after measuring persistent behavior gaps.

## 4) Agents vs Deterministic Workflows

### Deterministic Workflow (Build Fixed Flow)
Prefer deterministic flows when:

- task steps are known and stable
- compliance requires predictable behavior
- failure recovery must be explicit

### Agents (Buy Flexibility)
Use agents when:

- tasks are open-ended and require adaptive planning
- tool selection varies by query
- users value flexibility over strict determinism

### Practical Trade-off
Deterministic workflows are easier to test, cheaper, and more reliable. Agents are more flexible but can loop, choose wrong tools, and increase latency/cost without strong guardrails.

### Default Recommendation
Ship deterministic first. Introduce agentic behavior only for clearly non-deterministic use cases.

## 5) API Model vs Open-Weight Model

### API Model (Buy)
Use hosted API models when:

- you need fastest time-to-market
- quality and model upgrades matter more than deep customization
- your team cannot run model serving infrastructure yet

### Open-Weight Model (Build/Host)
Use open-weight models when:

- data governance requires self-hosting
- you need deep customization or model-level control
- workload is large enough that hosting economics are favorable

### Practical Trade-off
APIs reduce operational burden and often provide strong baseline quality. Open-weight hosting provides control and potential cost savings at scale but requires MLOps, serving, and performance tuning capability.

### Default Recommendation
Start with APIs for speed. Move to open-weight only when compliance, customization, or long-term cost justify operational complexity.

## Practical Decision Scorecard

Use a simple scorecard before committing:

```python
criteria = {
    "time_to_market": 5,
    "reliability": 5,
    "cost_12_month": 4,
    "team_operational_capacity": 3,
    "compliance": 5,
}

# Score each option (1-5) and pick highest weighted total.
```

## Common Mistakes

- optimizing for demo speed and ignoring maintenance cost
- choosing agents where deterministic workflows are enough
- fine-tuning too early before retrieval/evaluation is stable
- adopting many frameworks before defining clear ownership boundaries

## Final Rule of Thumb

Choose the simplest option that meets current product and reliability requirements. Re-evaluate every quarter as traffic, team, and constraints change.
