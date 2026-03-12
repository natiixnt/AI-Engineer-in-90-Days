# Tool-Calling Assistant Pattern

## When to Use It
Use this pattern when the assistant needs external capabilities such as search, calculations, database reads, or API actions.

## Architecture Overview
- LLM receives user request and tool schemas.
- Model selects tool call with structured arguments.
- Tool executor validates arguments and runs tool.
- Tool result is appended to context.
- LLM returns final user-facing response.

## Pros and Cons
**Pros**
- Better factuality via real-time tool outputs.
- Structured, inspectable action path.
- Extensible by adding new tools.

**Cons**
- Added latency from tool round trips.
- Argument/schema mismatch risks.
- Security risk if tools are over-permissioned.

## Common Failure Modes
- Invalid tool arguments.
- Wrong tool selected for task.
- Tool timeout or dependency outage.

## Implementation Notes
- Enforce strict JSON schemas before execution.
- Set per-tool timeout/retry/fallback policy.
- Require approval for high-risk tools (write, execute, external side effects).
