# Evaluation Tools Comparison

Concise engineering comparison for LLM/RAG evaluation tooling.

## Promptfoo
- **What it is good for:** Prompt and model regression testing in CI.
- **Strengths:** Config-driven tests, quick diffing across prompts/models.
- **Weaknesses:** Less specialized for deep retrieval-specific diagnostics.
- **When to choose it:** Teams wanting automated prompt/model checks in release pipelines.

## Ragas
- **What it is good for:** RAG-focused evaluation (retrieval + answer quality).
- **Strengths:** RAG metrics support (relevance, faithfulness, context quality).
- **Weaknesses:** Metric interpretation still requires manual failure analysis.
- **When to choose it:** RAG products needing dedicated retrieval/grounding quality tracking.

## DeepEval
- **What it is good for:** LLM app testing with structured test-case style workflows.
- **Strengths:** Practical test abstractions and fast local experimentation.
- **Weaknesses:** May require custom adaptation for complex enterprise pipelines.
- **When to choose it:** Teams building repeatable LLM tests beyond ad-hoc scripts.

## Custom Eval Harness
- **What it is good for:** Domain-specific metrics and strict product acceptance criteria.
- **Strengths:** Full control over scoring logic, datasets, and release gates.
- **Weaknesses:** Higher implementation and maintenance cost.
- **When to choose it:** Mature systems with unique business metrics and compliance constraints.
