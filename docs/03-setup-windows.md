# 03 - Windows Setup

## Goal

Get the learner to the point where they can open an empty folder in Codex, clone this boot camp repo into that folder, and start the labs.

## Prerequisites

Recommended:

- Windows 11
- PowerShell
- Git for Windows
- Codex app for Windows
- A ChatGPT or OpenAI account with Codex access

Optional:

- Python, only for the coding addendum
- GitHub CLI, only for people who want deeper GitHub workflows

## Step 1 - Install Codex

Use the official OpenAI Codex setup path from:

```text
docs/08-official-codex-sources.md
```

The instructor should screen share the official source and explain what is being downloaded before the learner clicks.

## Step 2 - Install Git

Git is the tool that lets the learner copy this repo and track file changes.

Use the official Git for Windows download path:

```text
https://git-scm.com/downloads/win
```

After install, reopen PowerShell and check:

```powershell
git --version
```

## Step 3 - Create an empty project folder

Example:

```powershell
mkdir $env:USERPROFILE\Documents\codex-boot-camp
```

Then open that empty folder in Codex.

## Step 4 - Clone this repo into the current folder

In Codex, paste:

```text
I am in an empty training folder.

Clone this GitHub repo into the current folder, not a nested folder:
https://github.com/paarguel/up-consulting-codex-boot-camp.git

Before running anything, explain in beginner-friendly language what git clone will do and why the final dot matters.

If the current folder is not empty, stop and tell me.

After cloning, read README.md and AGENTS.md and explain what this boot camp is for. Do not edit files yet.
```

Expected command:

```powershell
git clone https://github.com/paarguel/up-consulting-codex-boot-camp.git .
```

The final dot means "put the repo contents here."

## If the folder is not empty

Use the safer nested-folder command:

```powershell
git clone https://github.com/paarguel/up-consulting-codex-boot-camp.git
```

Then open the created `up-consulting-codex-boot-camp` folder in Codex.

## Step 5 - Run setup check

From the repo root:

```powershell
.\scripts\setup-check.ps1
```

The script checks the basics and reminds the learner of the first prompt.

## Instructor tip

Do not spend the whole session debugging setup. If setup gets stuck, keep the learner involved by screen sharing from the instructor machine and having them practice the prompts out loud.
