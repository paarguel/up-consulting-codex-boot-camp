# 02 - What Is Codex?

## Simple explanation

Codex is an AI coding agent. It can work with a project folder, read files, suggest changes, edit files, run commands, and help you understand code.

A good way to describe it to a beginner:

> Codex is like a very fast junior developer sitting next to you. It can help, but you still need to give context, check the work, and decide what gets committed.

## What Codex is good for

- Explaining unfamiliar code
- Finding where a bug might live
- Writing small functions
- Adding tests
- Refactoring messy code
- Generating documentation
- Reviewing a diff
- Creating a plan before implementation

## What Codex is not good for blindly

- Handling secrets without care
- Making large architecture changes without review
- Touching production systems casually
- Guessing business rules
- Rewriting a whole codebase because the prompt was vague
- Making irreversible changes without approval

## Beginner workflow

```text
1. Open the project folder.
2. Ask Codex to inspect the README and files.
3. Ask for a plan before editing.
4. Approve a small change.
5. Run tests.
6. Review the diff.
7. Ask Codex to explain the result.
8. Commit only when you understand it.
```

## Useful instructor phrase

> Codex is powerful when the project has rails: a clear folder, a clear task, a test, and a human reviewing the result.
