# LLM App Production Checklist

Practical production checklist for LLM-powered applications (non-agentic or lightly agentic).

## Reliability

- [ ] Clear fallback path exists when model API fails or times out.
- [ ] Retries use backoff and idempotency-safe behavior.
- [ ] Model routing policy is defined (small vs large model by task type).
- [ ] Third-party dependency failures are isolated with circuit breakers.

## Latency

- [ ] p50/p95 latency budgets are defined per user-facing endpoint.
- [ ] Token usage limits are enforced per request.
- [ ] Prompt templates are optimized to remove unnecessary context.
- [ ] Streaming is enabled for long responses where UX benefits.

## Observability

- [ ] Prompt, model, params, and response metadata are logged with trace IDs.
- [ ] Token, cost, and error metrics are tracked by route and tenant.
- [ ] Alerts exist for sudden error-rate or latency spikes.
- [ ] Prompt/version changes are linked to production metrics.

## Evaluation

- [ ] Offline eval dataset reflects real user tasks and edge cases.
- [ ] Success metrics include quality, refusal correctness, and format validity.
- [ ] A/B evaluation exists for prompt and model changes.
- [ ] CI checks prevent release when critical quality thresholds fail.

## Safety

- [ ] Input and output safety filters are applied where required.
- [ ] System prompt includes policy boundaries and prohibited behaviors.
- [ ] Sensitive data redaction policy exists for logs and traces.
- [ ] Manual escalation path exists for high-risk requests.

## API Design

- [ ] Request schema validates task type, input limits, and optional settings.
- [ ] Response schema is stable and versioned.
- [ ] Error responses are machine-readable with stable error codes.
- [ ] Rate limiting and quota policy are documented.

## Deployment Considerations

- [ ] Environment parity exists between staging and production.
- [ ] Rollout uses progressive delivery and quick rollback path.
- [ ] Capacity planning includes peak traffic and provider outages.
- [ ] Runbook exists for incident response and provider failover.
