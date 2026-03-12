# Simple LLM App Pattern

## When to Use It
Use this pattern for single-turn or light multi-turn assistants where the main value is fast, direct generation without retrieval or complex tool orchestration.

## Architecture Overview
- API/UI receives user prompt.
- Prompt template adds system instructions.
- LLM generates response.
- Optional output validator checks format/safety.
- Logs store prompt, output, latency, token usage.

## Pros and Cons
**Pros**
- Fastest pattern to ship.
- Minimal infrastructure.
- Easy to iterate prompt behavior.

**Cons**
- Limited factual grounding.
- More hallucination risk.
- Harder to answer domain-specific questions without context.

## Common Failure Modes
- Inconsistent output format.
- Hallucinated claims for factual tasks.
- Cost spikes from oversized prompts.

## Implementation Notes
- Start with strict system prompt and output schema.
- Add token limits and latency budgets early.
- Version prompts and run regression tests before release.
