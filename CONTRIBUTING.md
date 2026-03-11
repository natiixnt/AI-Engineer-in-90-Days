# Contributing Guidelines

Thank you for contributing to `ai-engineer-in-90-days`.

## How to Contribute

1. Fork the repository.
2. Create a branch: `git checkout -b feat/your-change`.
3. Make focused changes with clear commit messages.
4. Run examples and checks before opening a pull request.
5. Open a PR with:
   - what changed
   - why it changed
   - how to test it

## Contribution Areas

- Improve weekly learning content (`weeks/`)
- Add practical projects (`projects/`)
- Add runnable Python examples (`examples/`)
- Improve diagrams and architecture docs (`diagrams/`)
- Extend curated resources (`resources/`)

## Good First Issues

If you are looking for a small starter contribution, these are great entry points:

- Add more RAG examples in `examples/` (multi-query retrieval, reranking, citation formatting)
- Improve the embeddings tutorial in `weeks/week03_embeddings/README.md` with more practical use cases
- Add new agent patterns in `examples/agent_loop.py` (planner-worker or tool-selection variants)
- Add deployment guides in `weeks/week10_deploy_ai/README.md` (Docker, simple cloud deploy, API monitoring)

## Style Rules

- Keep explanations simple and practical.
- Prefer small, incremental pull requests.
- Include code snippets when useful.
- Use clear Markdown headings and short sections.

## Reporting Issues

When opening an issue, include:
- expected behavior
- actual behavior
- reproduction steps
- environment details
