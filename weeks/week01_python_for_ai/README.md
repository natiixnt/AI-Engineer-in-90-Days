# week01_python_for_ai: python for ai

## Concept
This week is about building reliable Python scripts that talk to APIs, parse JSON, and run from a clean local environment. The goal is not theory; it is to automate a small real task end-to-end.

## Key Ideas
- Keep setup reproducible with a virtual environment and `.env` values.
- Treat API responses as data contracts and validate key fields.
- Parse JSON into Python dictionaries and extract only what you need.
- Build scripts that fail clearly when network calls or keys are missing.

## Minimal Code Example
```python
"""Call a public API and process JSON output.
Run: python3 api_json_demo.py
"""

from __future__ import annotations

import json
import urllib.request


def fetch_repo(repo: str) -> dict:
    url = f"https://api.github.com/repos/{repo}"
    req = urllib.request.Request(url, headers={"Accept": "application/vnd.github+json"})
    with urllib.request.urlopen(req, timeout=10) as response:
        return json.loads(response.read().decode("utf-8"))


def main() -> None:
    repo = "natiixnt/AI-Engineer-in-90-Days"
    data = fetch_repo(repo)

    summary = {
        "name": data["full_name"],
        "stars": data["stargazers_count"],
        "open_issues": data["open_issues_count"],
        "default_branch": data["default_branch"],
    }

    print("Repository summary:")
    for key, value in summary.items():
        print(f"- {key}: {value}")


if __name__ == "__main__":
    main()
```

## Exercise
Write a script that calls two different API endpoints and saves a merged JSON report to `output.json`.

## Extra Challenge
Add retry logic with exponential backoff and graceful handling for rate limits (HTTP 429).
