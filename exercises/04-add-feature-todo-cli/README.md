# Exercise 04 - Add Feature to Todo CLI

## Goal

Add a small feature with a plan and tests.

## Current behavior

The todo module can:

- Add a task
- Mark a task complete
- List tasks

## New feature

Add a function named `list_open_tasks(tasks)` that returns only tasks where `done` is `False`.

## Run tests

From this folder:

```powershell
python -m unittest discover -s tests
```

## Codex prompt

```text
Read the README, starter/todo.py, and tests. Add the missing list_open_tasks function with the smallest change. Then run tests.
```

## Definition of done

- Tests pass
- The new function is simple
- Existing behavior is unchanged
