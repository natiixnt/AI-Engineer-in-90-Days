# LLM Frameworks Comparison

Concise engineering comparison for orchestration approaches.

## Plain Python
- **What it is good for:** Explicit, maintainable production control paths.
- **Strengths:** Low abstraction, easier debugging, minimal dependency churn.
- **Weaknesses:** More boilerplate and slower initial prototyping.
- **When to choose it:** Core production workflows where reliability and clarity are priorities.

## LangChain
- **What it is good for:** Rapid prototyping across many integrations.
- **Strengths:** Large ecosystem, many connectors, fast POC velocity.
- **Weaknesses:** Abstraction overhead and version-churn risk in long-lived systems.
- **When to choose it:** Early product exploration and integration-heavy experimentation.

## LlamaIndex
- **What it is good for:** Retrieval-centric applications and document workflows.
- **Strengths:** Strong ingestion/retrieval utilities, document-first patterns.
- **Weaknesses:** Can hide retrieval internals if used as a black box.
- **When to choose it:** Teams building document-heavy RAG and wanting faster retrieval setup.

## DSPy
- **What it is good for:** Optimization and programmatic prompt/pipeline tuning.
- **Strengths:** Structured optimization workflows and evaluation-driven design.
- **Weaknesses:** Higher learning curve and less straightforward for simple apps.
- **When to choose it:** Teams with mature eval loops optimizing quality systematically.
