# UP Consulting Codex Boot Camp

A beginner-friendly boot camp for learning how to use Codex as a safe coding partner.

## Goal

By the end of the session, the learner should be able to:

1. Explain what Codex is in plain language.
2. Open a project folder and ask Codex to inspect it.
3. Ask Codex to make a small change.
4. Run tests and review the result.
5. Use better prompts instead of vague prompts.
6. Understand permissions, sandboxing, and what not to let an agent do blindly.
7. Leave with a repeatable workflow: **inspect -> plan -> change -> test -> review -> commit**.

## Audience

This is for someone who is new to AI coding agents but comfortable enough to download tools, open a folder, and follow guided exercises.

They do **not** need to already be a professional developer.

## Recommended format

- 2 to 3 hours on Zoom
- Screen share by instructor first
- Then learner screen share during setup and exercises
- Keep exercises small and confidence-building
- Pause after every exercise for reflection

## Repo structure

```text
up-consulting-codex-boot-camp/
  README.md
  SESSION_PLAN.md
  AGENTS.md
  docs/
    01-ai-basics.md
    02-what-is-codex.md
    03-setup-windows.md
    04-prompting-workflows.md
    05-agents-skills-workflows.md
    06-safety-permissions.md
    07-instructor-checklist.md
    08-official-codex-sources.md
  prompts/
    00-first-session-prompts.md
    01-debugging-prompts.md
    02-refactor-prompts.md
    03-review-prompts.md
  exercises/
    README.md
    01-hello-codex/
    02-bug-fix-calculator/
    03-refactor-notes/
    04-add-feature-todo-cli/
  rubrics/
    skill-check.md
  scripts/
    setup-check.ps1
    create-public-github-repo.ps1
```

## Suggested teaching philosophy

Do not teach Codex as "magic."

Teach it as:

> A junior teammate who is fast, patient, and useful, but needs context, boundaries, tests, and review.

The learner should not walk away thinking, "AI will do everything for me."

They should walk away thinking:

> I can use Codex to understand code, make careful changes, learn faster, and stay in control.

## First commands

From inside this repo:

```powershell
# Windows PowerShell
.\scripts\setup-check.ps1
```

Then open Codex from the project folder:

```powershell
codex
```

## Exercise rhythm

For each exercise:

1. Read the exercise README.
2. Ask Codex to explain the goal.
3. Ask Codex to inspect files before editing.
4. Ask Codex for a plan.
5. Approve one small change.
6. Run tests.
7. Review the diff.
8. Commit only after you understand the change.

## Instructor note

Whiteboard and visual tool evaluations are intentionally **not** in this learning repo. Keep the repo focused on teaching materials, prompts, exercises, and repeatable practice.
