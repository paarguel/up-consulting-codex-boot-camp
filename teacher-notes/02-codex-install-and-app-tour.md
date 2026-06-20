# Teacher Notes 02 - Codex Install and App Tour

## Goal

Help the learner install or open Codex and understand the main app surfaces before doing labs.

## Before the learner clicks anything

Say:

> We use official sources for software. We want the right site, the right publisher, and a clear reason for the download.

Use:

```text
docs/08-official-codex-sources.md
```

## Install flow

1. Open the official Codex source.
2. Download or open the Codex app.
3. Sign in.
4. Keep the learner in default or bounded permissions for training.
5. Do not create API keys or secrets.

## App tour

Show these surfaces:

### Sidebar

Use it to switch projects, threads, skills, plugins, and app areas.

Teaching line:

> The sidebar is how Codex remembers and organizes work.

### Project folder

Show that Codex is attached to a folder.

Teaching line:

> Codex is strongest when the folder contains the context.

### Composer

This is where the learner writes the prompt.

Teach them to include:

- Goal
- Context
- Constraints
- Definition of done

### Terminal

The terminal is where commands run.

For this workshop, Git commands and setup checks are enough.

### Diff or review panel

Show that Codex changes can be inspected.

Teaching line:

> We do not just trust the result. We inspect what changed.

### Permissions selector

Explain:

- Default permissions keep Codex bounded.
- Approval prompts are useful.
- Full access is not the beginner default.

### New thread

Explain that each thread is a working conversation.

Teaching line:

> A new thread is like a fresh work session. Keep one thread per clear task when possible.

## First safe prompt

After the repo is cloned:

```text
Read README.md and AGENTS.md. Explain this repo to me like I am new to AI-assisted knowledge work. Do not edit files yet.
```

## Instructor warning

Do not turn the app tour into a product demo. Show only enough for the learner to start the first lab.
