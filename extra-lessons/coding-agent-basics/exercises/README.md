# Exercises

Each exercise is intentionally small.

The goal is not to prove Codex can build a huge app. The goal is to practice the control loop:

```text
inspect -> plan -> edit -> test -> review
```

## Exercise order

1. `01-hello-codex` - Tiny fix
2. `02-bug-fix-calculator` - Debug from tests
3. `03-refactor-notes` - Refactor messy code
4. `04-add-feature-todo-cli` - Add a small feature

## Standard test command

From an exercise folder:

```powershell
python -m unittest discover -s tests
```

## Standard Codex starter prompt

```text
Read this exercise README and the tests. Explain the task and likely files to edit. Do not edit yet.
```
