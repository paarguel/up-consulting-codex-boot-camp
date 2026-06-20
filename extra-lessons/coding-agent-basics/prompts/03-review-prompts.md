# Review Prompts

## Diff review

```text
Review the current git diff. Look for:
1. Accidental changes
2. Unrelated edits
3. Missing tests
4. Security or privacy risks
5. Simpler alternatives
```

## Beginner explanation

```text
Explain this diff line by line in plain English.
```

## Commit message

```text
Write a clear commit message for this change using the format:
type: short summary

- What changed
- Why it changed
- How it was tested
```

## Safety review

```text
Before I commit, check whether this diff includes secrets, personal data, generated junk, or files outside the exercise.
```
