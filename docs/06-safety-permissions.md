# 06 - Safety and Permissions

## The core safety idea

Codex is most useful when it has enough access to help but not so much access that mistakes become expensive.

## Things to protect

- API keys
- Passwords
- Personal files
- Production systems
- Real customer data
- Bank or billing systems
- Anything outside the exercise folder

## Beginner safety defaults

Use this posture:

```text
Work inside the project folder.
Ask before changing anything outside it.
Ask before using the internet.
Ask before installing dependencies.
Ask before deleting files.
Ask before pushing to GitHub.
```

## Approval checklist

Before approving a Codex action, ask:

1. Do I understand what it wants to do?
2. Is it working in the right folder?
3. Could this affect secrets or personal files?
4. Is the change reversible?
5. Is there a test or visible way to verify it?
6. Is this the smallest reasonable step?

## Good safety prompt

```text
Stay inside this exercise folder. Do not access secrets, credentials, or files outside the repo. Before editing, explain your plan and wait for approval.
```

## Git safety

Before committing:

```powershell
git status
git diff
```

Ask Codex:

```text
Review this diff for accidental changes, secrets, unrelated edits, and missing tests.
```

## Instructor tip

Teach this line early:

> The goal is not maximum autonomy. The goal is useful autonomy with receipts.
