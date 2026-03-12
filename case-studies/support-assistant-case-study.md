# Support Assistant Case Study

## Problem
Support teams spend too much time answering repeated questions, triaging tickets, and searching for the latest policy updates. Response quality varies across agents and shifts.

## System Design
A support assistant should combine retrieval over help center content with ticket metadata and policy rules.

- Ingest FAQ, docs, policy pages, and historical resolved tickets.
- Retrieve relevant context for each incoming support question.
- Generate a draft answer with citations and suggested next action.
- Route high-risk cases to human agents.

## Architecture Choices
- Retrieval: hybrid search (keyword + vector) to improve recall for exact product terms.
- Generation: grounded prompt requiring citations and confidence level.
- Workflow: deterministic routing first, optional agent tools for escalation and ticket updates.
- Data: tenant-aware indexing and strict ACL filtering for private support content.

## Common Trade-offs
- Faster responses vs stricter human review for risky issues.
- Broad context retrieval vs prompt length and latency.
- Fully automated responses vs assisted-agent draft mode.
- General model quality vs cost per ticket.

## Suggested Implementation Path
1. Start with draft-only answers for support agents (no auto-send).
2. Build evaluation set from real tickets with expected answer quality.
3. Add citation requirements and policy guardrails.
4. Enable limited auto-response only for low-risk categories.
5. Add monitoring for hallucination rate, CSAT, and escalation rate.
