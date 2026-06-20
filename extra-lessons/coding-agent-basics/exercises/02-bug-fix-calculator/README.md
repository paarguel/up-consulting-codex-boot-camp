# Exercise 02 - Bug Fix Calculator

## Goal

Use tests to find and fix bugs.

## What to do

The calculator has several simple functions. Some are wrong.

Your job is to ask Codex to:

1. Run the tests.
2. Focus on the first failure.
3. Explain the cause.
4. Make the smallest fix.
5. Repeat until tests pass.

## Run tests

From this folder:

```powershell
python -m unittest discover -s tests
```

## Codex prompt

```text
Run the tests and focus only on the first failure. Explain the failure before editing. Then make the smallest fix.
```

## Definition of done

- Tests pass
- Codex explains each bug in plain language
- The final diff is small
