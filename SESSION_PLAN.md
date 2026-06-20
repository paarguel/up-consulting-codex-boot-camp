# Session Plan: UP Consulting Codex Boot Camp

## Session promise

By the end of this session, the learner will have Codex installed, will understand the basic mental model, and will have completed practical knowledge-worker workflows using fake but realistic work materials.

The learner should leave knowing how to:

- Open Codex around a project folder.
- Ask Codex to inspect before acting.
- Turn messy inputs into a clear artifact.
- Review the artifact for accuracy, privacy, tone, and judgment.
- Save a useful prompt so the workflow can be repeated.

## 2-hour live workshop

### 0:00-0:10 - Welcome and frame

Explain:

- Codex is not magic.
- Codex is a workbench for files, folders, prompts, tools, and outputs.
- The core skill is supervision: context, boundaries, review, and reuse.

Whiteboard:

```text
messy inputs -> clear output -> repeatable workflow
```

### 0:10-0:25 - AI history and mental model

Use `teacher-notes/01-whiteboard-ai-history.md`.

Cover:

- AI as pattern prediction and tool use, not human judgment.
- ChatGPT as conversation.
- Custom GPTs and plugins/connectors as specialized context and connected tools.
- Codex as an agentic workbench that can operate on a project folder.

### 0:25-0:40 - Install and app tour

Use `teacher-notes/02-codex-install-and-app-tour.md`.

Do together:

- Open the official Codex download path.
- Install or open Codex.
- Sign in.
- Tour the sidebar, toolbar, composer, terminal, diff/review panel, permissions selector, and project picker.

### 0:40-0:55 - Create project folder and clone repo

Use `teacher-notes/03-first-project-folder-and-clone.md`.

Do together:

- Create an empty folder for the learner's boot camp workbench.
- Open that folder in Codex.
- Prompt Codex to clone this repo into the current folder using `git clone ... .`.
- Ask Codex to read `README.md` and `AGENTS.md` before doing work.

### 0:55-1:10 - Teach the Codex Work Loop

Use `docs/04-prompting-workflows.md`.

Teach:

```text
collect -> contextualize -> produce -> review -> compound
```

Make the learner say the review rule out loud:

> Codex can draft and organize. I still review names, dates, money, privacy, commitments, and final sending.

### 1:10-1:35 - Lab 1: Parish event command center

Use:

```text
sample-work-packs/parish-event-planning/
prompt-recipes/event-command-center.md
review-checklists/final-send-review.md
```

Goal:

- Read messy notes and supporting files.
- Produce `outputs/event-command-center.md`.
- Include summary, timeline, volunteer assignments, supplies, parent email draft, questions, and risks.
- Do not invent missing details.

### 1:35-1:55 - Problem imagination board

Use `teacher-notes/04-problem-imagination-board.md` and `handouts/from-office-pain-to-codex-prompt.md`.

Ask:

> Where does your work get messy?

Map one real frustration into:

```text
Input -> Desired Output -> Review Risk -> Codex Workflow
```

### 1:55-2:00 - Wrap

Ask:

- What output did Codex produce?
- What did you have to review?
- What would you trust it with next?
- What would you not trust it with yet?
- Which workflow should you try this week?

## Optional 3-hour version

Use the same opening, then add two more labs:

1. Meeting notes to action tracker.
2. Announcement rewrite across channels.

End with a learner-specific workflow canvas:

```text
workbench-template/
  inputs/
  outputs/
  workflows/
```

## Addendum path

After the knowledge-worker workshop, learners who want to understand coding-agent habits can use:

```text
extra-lessons/coding-agent-basics/
```

That addendum teaches tests, diffs, small code changes, refactors, and Git commits.
