# Teacher Notes 03 - First Project Folder and Clone

## Goal

Avoid the confusing "download ZIP, extract, open, reopen" flow by using Codex to clone the repo into an empty project folder.

## Recommended flow

1. Create an empty folder.
2. Open that empty folder in Codex.
3. Ask Codex to clone the repo into the current folder with the final dot.
4. Ask Codex to inspect `README.md` and `AGENTS.md`.

## Why the final dot matters

Without the final dot:

```powershell
git clone https://github.com/paarguel/up-consulting-codex-boot-camp.git
```

Git creates a nested folder:

```text
current-folder/
  up-consulting-codex-boot-camp/
```

Then the learner may need to reopen the nested folder in Codex.

With the final dot:

```powershell
git clone https://github.com/paarguel/up-consulting-codex-boot-camp.git .
```

Git puts the repo contents directly into the current empty folder:

```text
current-folder/
  README.md
  AGENTS.md
  docs/
  sample-work-packs/
```

## Prompt to paste

```text
I am in an empty training folder.

Clone this GitHub repo into the current folder, not a nested folder:
https://github.com/paarguel/up-consulting-codex-boot-camp.git

Before running anything, explain in beginner-friendly language what git clone will do and why the final dot matters.

If the current folder is not empty, stop and tell me.

After cloning, read README.md and AGENTS.md and explain what this boot camp is for. Do not edit files yet.
```

## If the folder is not empty

Do not force the dot clone.

Use the nested clone:

```powershell
git clone https://github.com/paarguel/up-consulting-codex-boot-camp.git
```

Then reopen the cloned folder in Codex.

## Teaching line

> The current folder is our workbench. We want Codex and Git looking at the same workbench.
