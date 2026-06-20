# Debugging Prompts

## Find the first failure

```text
Run the tests and focus only on the first failure. Explain what the failure means before editing.
```

## Reason from tests

```text
Read the tests as the source of truth. What behavior do they expect, and how does the current code differ?
```

## Smallest fix

```text
Make the smallest code change that should satisfy the failing test. Avoid broad refactors.
```

## Verify

```text
Run the test again. If it fails, explain the new failure and your next smallest step.
```

## Review

```text
Review the final diff for unrelated changes, overengineering, or missing edge cases.
```
