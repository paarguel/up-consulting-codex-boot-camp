# Exercise 03 - Refactor Notes

## Goal

Practice refactoring without changing behavior.

## Scenario

The file `starter/notes.py` works, but it is hard to read.

Ask Codex to:

1. Explain what the function does.
2. Identify code smells.
3. Propose a small refactor.
4. Apply only one small refactor.
5. Preserve behavior.

## Manual check

From this folder:

```powershell
python starter/notes.py sample_notes.txt
```

Expected output:

```text
Total notes: 5
Todo notes: 3
Done notes: 2
```

## Codex prompt

```text
Read starter/notes.py. Explain what it does. Then suggest a small refactor that preserves behavior. Do not edit until I approve.
```

## Definition of done

- Output stays the same
- Code is easier to read
- Codex explains what it changed
