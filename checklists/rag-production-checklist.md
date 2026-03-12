# RAG Production Checklist

Practical production checklist for shipping and operating a Retrieval-Augmented Generation system.

## Reliability

- [ ] Ingestion pipeline has retries and dead-letter handling for failed documents.
- [ ] Index freshness SLA is defined (for example: updates visible within 15 minutes).
- [ ] Fallback exists when retrieval fails (safe response or cached answer).
- [ ] Retrieval and generation stages have independent timeout settings.

## Latency

- [ ] End-to-end p95 latency target is defined and monitored.
- [ ] Retrieval p95 and generation p95 are measured separately.
- [ ] Context size is token-budgeted (top-k limits + truncation policy).
- [ ] Hot queries use caching or precomputed retrieval where possible.

## Observability

- [ ] Each request has a trace ID linking query, retrieved chunks, and final output.
- [ ] Retrieval logs include chunk IDs, scores, and source metadata.
- [ ] Error logs distinguish ingestion, retrieval, and generation failures.
- [ ] Dashboard shows quality, latency, cost, and error trends by endpoint.

## Evaluation

- [ ] Labeled eval set exists with expected relevant chunks and answers.
- [ ] Retrieval metrics tracked: `Recall@k`, `Precision@k`, `MRR` (if ranking matters).
- [ ] Generation metrics tracked: faithfulness, answer correctness, completeness.
- [ ] Regression tests run before each prompt/model/index change.

## Safety

- [ ] Prompt requires grounded answers and explicit uncertainty when evidence is missing.
- [ ] Sensitive sources are filtered by ACL/tenant permissions before retrieval.
- [ ] Output checks prevent unsupported high-risk claims.
- [ ] Prompt injection tests exist for untrusted user content.

## API Design

- [ ] API returns citations (`chunk_id` / source) with each answer.
- [ ] Request schema includes query and optional retrieval constraints.
- [ ] Response schema includes answer, citations, confidence, and trace ID.
- [ ] Error contract is explicit (`timeout`, `retrieval_unavailable`, `validation_error`).

## Deployment Considerations

- [ ] Blue/green or canary rollout strategy exists for prompt/model/index changes.
- [ ] Rollback procedure is documented and tested.
- [ ] Compute and storage capacity planning is done for expected index growth.
- [ ] Secrets and API keys are managed via secure secret store, not in code.
