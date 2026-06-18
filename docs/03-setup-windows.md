# 03 - Windows Setup

## Goal

Get the learner to the point where they can open this repo and run Codex from the project folder.

## Prerequisites

Recommended:

- Windows 11
- PowerShell
- Git
- Python 3.11 or newer
- A ChatGPT or OpenAI account with Codex access
- Optional: GitHub CLI for publishing/forking repos

## Step 1 - Check tools

From the repo root:

```powershell
.\scripts\setup-check.ps1
```

The script checks:

- Git
- Python
- Codex command availability
- GitHub CLI availability

## Step 2 - Open Codex from the repo

```powershell
codex
```

## Step 3 - First prompt

Paste:

```text
Read the README and AGENTS.md. Then explain this repo to me like I am new to AI coding agents. Do not edit files yet.
```

## Step 4 - Run the first exercise

```text
Open exercises/01-hello-codex. Read the README and tests. Explain what is broken before editing.
```

## Setup troubleshooting

### "codex is not recognized"

Possible causes:

- Codex is not installed.
- The terminal was not restarted after install.
- The install location is not on PATH.

Use the official Codex setup docs for the latest install command.

### Python not found

Install Python from the official Python website or Microsoft Store. Then reopen PowerShell.

### Git not found

Install Git for Windows, then reopen PowerShell.

## Instructor tip

Do not spend the whole session debugging setup. If setup gets stuck, screen share from the instructor machine and let the learner still practice prompts conceptually.
