# week04_llms: llms

## Concept
This week covers practical prompt design with system prompts, user prompts, and function calling. The goal is to structure model behavior and consume outputs safely.

## Key Ideas
- Use system prompts to define strict behavior boundaries.
- Keep user prompts focused and explicit.
- Use function calling for structured tool inputs.
- Treat model output as data that needs validation.

## Minimal Code Example
```python
"""Call an LLM with system prompt and simple function calling.
Install: pip install openai
Set: export OPENAI_API_KEY=...
Run: python3 llm_function_call.py
"""

from __future__ import annotations

import json
import os

from openai import OpenAI


client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])


def main() -> None:
    tools = [
        {
            "type": "function",
            "function": {
                "name": "get_weather",
                "description": "Return weather summary for a city",
                "parameters": {
                    "type": "object",
                    "properties": {"city": {"type": "string"}},
                    "required": ["city"],
                },
            },
        }
    ]

    messages = [
        {"role": "system", "content": "You are a concise assistant. Use tools when needed."},
        {"role": "user", "content": "What is the weather in Warsaw?"},
    ]

    first = client.chat.completions.create(model="gpt-4o-mini", messages=messages, tools=tools)
    message = first.choices[0].message

    if message.tool_calls:
        call = message.tool_calls[0]
        args = json.loads(call.function.arguments)
        tool_result = f"Weather in {args['city']}: 15C, clear sky."

        messages.append(message)
        messages.append({"role": "tool", "tool_call_id": call.id, "content": tool_result})

        second = client.chat.completions.create(model="gpt-4o-mini", messages=messages)
        print(second.choices[0].message.content)
    else:
        print(message.content)


if __name__ == "__main__":
    main()
```

## Exercise
Add one more tool (for example `convert_currency`) and let the model choose which tool to call.

## Extra Challenge
Validate tool arguments against a strict schema before executing the function.
