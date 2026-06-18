# Session Plan: UP Consulting Codex Boot Camp

## Session promise

By the end of this session, the learner will have Codex installed, will understand the basic mental model, and will have completed several small coding-agent exercises without losing control of the project.

## 90-minute version

### 0:00-0:10 - Welcome and frame

Explain:

- This is not about becoming a full developer in one day.
- This is about learning how to collaborate with an AI coding agent.
- The core skill is not "typing prompts." The core skill is giving context, setting boundaries, checking work, and iterating.

### 0:10-0:25 - AI basics

Cover:

- What a model is
- What a prompt is
- What context means
- Why AI can be useful and wrong at the same time
- Why tests and review matter

Whiteboard idea:

```text
Human intention -> Prompt -> Codex reads repo -> Plan -> Edits -> Tests -> Human review
```

### 0:25-0:45 - Setup

Do together:

- Install or open Codex
- Sign in
- Open this repo
- Run setup checks
- Confirm terminal, Git, and Python work

### 0:45-1:05 - Exercise 1: Hello Codex

Goal:

- Let Codex inspect files
- Make one tiny fix
- Run a test
- Explain the diff

### 1:05-1:25 - Exercise 2: Calculator bug fix

Goal:

- Debug a broken function
- Ask Codex to reason from tests
- Keep the change small

### 1:25-1:30 - Wrap

Ask:

- What did Codex do well?
- What felt scary or unclear?
- What would you trust it with next?
- What would you not trust it with yet?

## 3-hour version

### 0:00-0:15 - Welcome

Frame Codex as a coding teammate, not a magic button.

### 0:15-0:35 - AI basics

Explain:

- Model
- Token/context
- Prompt
- Tool use
- Agent loop
- Hallucination
- Tests as reality checks

### 0:35-1:00 - What Codex is

Explain:

- Local project awareness
- File reading
- File editing
- Terminal/test execution
- Permission prompts
- Git diffs
- Why repo hygiene matters

### 1:00-1:25 - Setup

Do:

- Install/open Codex
- Sign in
- Clone/download repo
- Run setup script
- Open Codex from the project folder

### 1:25-1:45 - Exercise 1: Hello Codex

Tiny fix, low stakes.

### 1:45-2:10 - Exercise 2: Calculator bug fix

Debug with tests.

### 2:10-2:20 - Break

### 2:20-2:45 - Exercise 3: Refactor notes

Refactor messy code while preserving behavior.

### 2:45-3:10 - Exercise 4: Add todo CLI feature

Add a small feature using a plan and tests.

### 3:10-3:30 - Philosophy, workflows, and next steps

Teach the operating loop:

```text
clarify -> constrain -> inspect -> plan -> approve -> test -> review -> commit
```

Cover:

- Good prompts
- Bad prompts
- When to use agents
- When not to use agents
- How to ask for a review
- How to use Codex for learning instead of copying
