# UP Consulting Codex Boot Camp

AI workflows for office, parish, nonprofit, and knowledge workers.

This boot camp teaches Codex as a practical workbench for everyday knowledge work. The goal is not to turn beginners into programmers. The goal is to help them gather messy work into a folder, give Codex clear context, ask for a useful artifact, review it safely, and save the workflow so they can repeat it next week.

## Core promise

By the end of the workshop, the learner should be able to say:

> I can put a messy pile of office materials into a folder, explain the outcome I need, have Codex produce a reviewable draft, check it safely, and save the prompt as a reusable workflow.

## Who this is for

This repo is designed for people who do practical office and coordination work:

- Parish office staff
- Ministry leaders
- Youth ministers
- Nonprofit administrators
- Office managers
- Executive assistants
- Small business operators
- Communications staff
- Volunteer coordinators
- Go-getter staff members who already solve problems informally

No coding background is required for the core boot camp.

## Teaching model

Teach Codex as a teammate, not a magic button.

Use the five-part Codex Work Loop:

```text
collect -> contextualize -> produce -> review -> compound
```

1. Collect the relevant files and notes in one project folder.
2. Contextualize the task, audience, constraints, and definition of done.
3. Produce a concrete artifact such as a brief, tracker, email, report, or checklist.
4. Review the result for accuracy, privacy, tone, judgment, dates, names, money, and commitments.
5. Compound the workflow by saving the prompt and checklist for future use.

The simple mental model is:

```text
messy inputs -> clear output -> repeatable workflow
```

## First live flow

The intended live flow is:

1. Instructor introduces the workshop over Zoom or in person.
2. Instructor opens the teacher notes and gives a whiteboard overview of AI, ChatGPT, custom GPTs, plugins/connectors, and Codex as an evolution toward agentic work.
3. Learner opens the official OpenAI/Codex download path and installs Codex.
4. Instructor tours the Codex sidebar, toolbar, composer, terminal, diff/review panel, permissions, and project folders.
5. Learner creates an empty project folder.
6. Learner opens that empty folder in Codex.
7. Learner asks Codex to clone this repo into the current folder.
8. Learner asks Codex to inspect the repo before doing any lab.
9. Learner completes knowledge-worker labs using fake but realistic work packs.

### First clone prompt

Use this prompt only after the learner has opened an empty folder in Codex:

```text
I am in an empty training folder.

Clone this GitHub repo into the current folder, not a nested folder:
https://github.com/paarguel/up-consulting-codex-boot-camp.git

Before running anything, explain in beginner-friendly language what git clone will do and why the final dot matters.

If the current folder is not empty, stop and tell me.

After cloning, read README.md and AGENTS.md and explain what this boot camp is for. Do not edit files yet.
```

The final dot in the clone command tells Git to place the repo contents directly in the current empty folder:

```powershell
git clone https://github.com/paarguel/up-consulting-codex-boot-camp.git .
```

If the folder is not empty, use the safer nested-folder command instead and reopen the cloned folder in Codex:

```powershell
git clone https://github.com/paarguel/up-consulting-codex-boot-camp.git
```

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
  teacher-notes/
    01-whiteboard-ai-history.md
    02-codex-install-and-app-tour.md
    03-first-project-folder-and-clone.md
    04-problem-imagination-board.md
  sample-work-packs/
    parish-event-planning/
    meeting-to-action-items/
    messy-roster-cleanup/
    announcement-rewrites/
    weekly-reporting/
    vendor-comparison/
    sop-builder/
  prompt-recipes/
  review-checklists/
  handouts/
  workbench-template/
  extra-lessons/
    coding-agent-basics/
```

## Main labs

The core boot camp is built around realistic sample work packs:

1. Turn messy parish event notes into an event command center.
2. Turn meeting notes into minutes, decisions, and action items.
3. Clean a messy roster and flag duplicate or missing information.
4. Rewrite one announcement for bulletin, email, pulpit, website, and social media.
5. Create a weekly leadership report from scattered notes.
6. Compare vendors or options against decision criteria.
7. Turn an informal process into a standard operating procedure.

All sample data is fake. The point is to practice the workflow safely before using Codex on real work.

## Safety rule

Use Codex for drafting, organizing, checking, and workflow support.

Use human judgment for:

- Private information
- Children or vulnerable people
- Money
- Personnel issues
- Commitments
- External sending
- Final decisions

## Addendum: coding-agent basics

The original coding-focused lessons still exist under:

```text
extra-lessons/coding-agent-basics/
```

Use them after the main knowledge-worker boot camp if the learner wants to understand coding-agent habits like tests, diffs, refactors, and Git commits.
