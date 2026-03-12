# LLM Interview Questions

Practical interview questions about LLM behavior, control, and safety in applications.

## 1) Temperature

**Question**
What does temperature control in an LLM response?

**Why It Matters**
Temperature affects determinism, consistency, and downstream reliability.

**Short Answer**
Temperature controls randomness in token sampling. Lower values produce more deterministic and repeatable outputs, which is useful for structured tasks. Higher values increase creativity but can reduce consistency. In production, many workflows use low temperature and rely on prompt/tool design for quality.

**Deep Dive (Optional)**
Temperature does not replace good prompts or retrieval quality. It should be tuned per task type, not globally.

**Example Code (when relevant)**
```python
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": "Summarize this doc."}],
    temperature=0.2,
)
```

## 2) Tokens

**Question**
Why do tokens matter in LLM applications?

**Why It Matters**
Tokens directly drive model limits, latency, and cost.

**Short Answer**
LLMs process text as tokens, not raw characters. Input and output token counts affect both billing and response time. Token limits also constrain prompt size and context assembly strategies. Good systems track tokens per request and enforce budgets.

**Deep Dive (Optional)**
Token-aware routing can send short tasks to smaller models and reserve larger models for complex cases.

**Example Code (when relevant)**
```python
def rough_token_estimate(text: str) -> int:
    return int(len(text.split()) / 0.75)
```

## 3) System Prompts

**Question**
What is a system prompt and why is it important?

**Why It Matters**
System prompts define global behavior and safety boundaries.

**Short Answer**
A system prompt is a high-priority instruction that sets role, tone, and policy constraints. It helps keep behavior consistent across many user requests. In production, it should include task scope, refusal rules, and output format requirements. It should be versioned and regression-tested.

**Deep Dive (Optional)**
Treat system prompts as policy code: small changes can materially affect business outcomes.

**Example Code (when relevant)**
```python
messages = [
    {"role": "system", "content": "Answer with citations. If unsure, say so."},
    {"role": "user", "content": "How do I monitor RAG quality?"},
]
```

## 4) Tool Calling

**Question**
What is tool calling and when should you use it?

**Why It Matters**
Tool calling enables reliable access to external systems and real-time data.

**Short Answer**
Tool calling lets the model request structured function execution instead of guessing answers. It is useful for tasks requiring databases, calculators, search, or APIs. This improves factuality and controllability because tool outputs are explicit. Always validate tool arguments before execution.

**Deep Dive (Optional)**
Use strict JSON schemas and permission controls to avoid unsafe or malformed tool calls.

**Example Code (when relevant)**
```python
def get_weather(city: str) -> str:
    return f"Weather in {city}: 15C, clear"

# validate args before executing tool
args = {"city": "Warsaw"}
print(get_weather(args["city"]))
```

## 5) Guardrails

**Question**
What are guardrails in LLM systems?

**Why It Matters**
Guardrails reduce policy violations and unsafe outputs.

**Short Answer**
Guardrails are controls around model behavior, including input filtering, prompt constraints, output validation, and policy checks. They help prevent unsafe content, data leakage, and unsupported claims. Strong guardrails are layered, not single-point checks. They should be measured with targeted adversarial tests.

**Deep Dive (Optional)**
Combine model-side guardrails with system-side controls (tool permissions, sandboxing, and audit logs).

**Example Code (when relevant)**
```python
def is_allowed_output(text: str) -> bool:
    blocked = ["password", "api_key", "private token"]
    return not any(word in text.lower() for word in blocked)
```
