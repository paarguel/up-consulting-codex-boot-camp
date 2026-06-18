# 05 - Agents, Skills, and Workflows

## Agent

An agent is an AI system that can take multiple steps using tools.

A simple agent loop:

```text
understand goal -> inspect context -> choose action -> use tool -> observe result -> continue or stop
```

## Skill

A skill is a repeatable capability or procedure.

Examples:

- Debug a failing test
- Summarize a codebase
- Create a README
- Add a feature behind a flag
- Review a Git diff

## Workflow

A workflow is a repeatable sequence of skills.

Example debugging workflow:

```text
1. Reproduce the bug.
2. Read the failing test or error.
3. Identify likely cause.
4. Make the smallest change.
5. Run the test again.
6. Summarize the fix.
```

## Why workflows matter

Without a workflow, Codex may do too much.

With a workflow, Codex becomes easier to steer.

## Teaching analogy

Do not say:

> "AI, do my work."

Say:

> "AI, follow this workflow with me."

## Beginner workflows to practice

### Explain a folder

```text
Read this folder and explain:
1. What each file does
2. What the entry point is
3. What I should run first
4. What looks risky or confusing
```

### Debug a test

```text
Run the tests. Pick the first failure. Explain the failure, then make the smallest fix.
```

### Add a feature

```text
Before editing, propose:
1. Files likely affected
2. Tests to add or update
3. Risks
4. Smallest implementation plan
```

### Review before commit

```text
Review the current diff as if you are a cautious teammate. Call out bugs, unnecessary changes, and missing tests.
```
