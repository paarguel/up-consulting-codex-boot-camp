# 04 - Prompting and Workflows

## The beginner mistake

Most beginners ask:

```text
Can you fix this?
```

That gives Codex too much freedom and too little context.

## Better pattern

Use this shape:

```text
Context:
- I am in exercise 02.
- The tests are failing.
- I want the smallest fix.

Task:
- Read the README and tests.
- Explain what is failing.
- Propose a plan.
- Do not edit yet.

Definition of done:
- Tests pass.
- The diff is small.
- You explain the change.
```

## Core workflow

```text
clarify -> inspect -> plan -> edit -> test -> review -> commit
```

## Prompt ladder

### Level 1 - Explain

```text
Read this folder and explain what the code is supposed to do. Do not edit anything.
```

### Level 2 - Diagnose

```text
Run the relevant tests. Explain the first failure and the likely cause before changing files.
```

### Level 3 - Small fix

```text
Make the smallest change that should pass the failing test. Do not refactor unrelated code.
```

### Level 4 - Review

```text
Show me the diff and explain it line by line in beginner language.
```

### Level 5 - Improve

```text
Suggest one improvement that would make this easier to maintain, but do not implement it yet.
```

## Bad prompts and safer rewrites

| Vague prompt | Safer version |
|---|---|
| Fix everything. | Find the first failing test and make the smallest fix. |
| Make this better. | Suggest 3 improvements, then wait. |
| Rewrite this app. | Identify the riskiest part of the code and propose a refactor plan. |
| Add AI. | Explain where AI would help and where it would be overkill. |
| Push this to GitHub. | Show me the diff and ask before any Git write operation. |

## Instructor tip

Have the learner say the workflow out loud:

> "Inspect first. Plan second. Edit third. Test fourth. Review fifth."
