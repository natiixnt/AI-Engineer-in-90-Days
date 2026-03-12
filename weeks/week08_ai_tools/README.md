# week08_ai_tools: evaluation and monitoring

## Concept
This week focuses on measuring output quality and capturing runtime traces. You should treat every prompt, output, and latency value as data for debugging and improvement.

## Key Ideas
- Evaluation should be explicit and repeatable.
- Log prompts, outputs, and timing for every request.
- Trace IDs help connect multi-step workflows.
- Monitoring makes regressions visible early.

## Minimal Code Example
```python
"""Log prompts, outputs, scores, and traces.
Run: python3 eval_monitoring_demo.py
"""

from __future__ import annotations

import json
import time
import uuid
from pathlib import Path


def ask_model(prompt: str) -> str:
    return f"Draft answer for: {prompt}"


def evaluate(answer: str) -> float:
    return 1.0 if "answer" in answer.lower() else 0.0


def log_trace(path: Path, trace: dict) -> None:
    with path.open("a", encoding="utf-8") as f:
        f.write(json.dumps(trace) + "\n")


def main() -> None:
    prompt = "How do I monitor a RAG system?"
    trace_id = str(uuid.uuid4())
    start = time.perf_counter()
    output = ask_model(prompt)
    latency_ms = (time.perf_counter() - start) * 1000

    trace = {
        "trace_id": trace_id,
        "prompt": prompt,
        "output": output,
        "score": evaluate(output),
        "latency_ms": round(latency_ms, 2),
    }

    log_trace(Path("traces.jsonl"), trace)
    print(trace)


if __name__ == "__main__":
    main()
```

## Exercise
Log at least 20 traces and compute average score and p95 latency from the JSONL file.

## Extra Challenge
Create a small dashboard script that groups metrics by prompt type.
