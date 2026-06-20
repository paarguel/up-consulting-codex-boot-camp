# 07 - Instructor Checklist

Use this before and during a live session.

## Before the session

- [ ] Confirm the learner has a computer they can use on Zoom or in person.
- [ ] Confirm they can install software, or have a fallback instructor demo ready.
- [ ] Have the official Codex download page ready.
- [ ] Have the official Git for Windows download page ready.
- [ ] Have this repo URL ready.
- [ ] Open `SESSION_PLAN.md`.
- [ ] Open `teacher-notes/01-whiteboard-ai-history.md`.
- [ ] Open `teacher-notes/02-codex-install-and-app-tour.md`.
- [ ] Open `teacher-notes/03-first-project-folder-and-clone.md`.
- [ ] Open `teacher-notes/04-problem-imagination-board.md`.

## Teaching posture

Say early:

> We are not trying to make AI do everything. We are learning how to supervise it.

Keep the learner moving through small wins.

## Setup checklist

- [ ] Codex installed or instructor demo ready.
- [ ] Git installed.
- [ ] Empty project folder created.
- [ ] Folder opened in Codex.
- [ ] Repo cloned into the current folder or cloned as a nested folder and reopened.
- [ ] `README.md` and `AGENTS.md` inspected by Codex.
- [ ] `scripts/setup-check.ps1` run if time allows.

## Lab checklist

For each lab:

- [ ] Read the work-pack README or workflow.
- [ ] Ask Codex to inspect before producing.
- [ ] Ask for a named output file in `outputs/`.
- [ ] Require a Questions or Needs Human Review section.
- [ ] Review the output with the learner.
- [ ] Save or point to the reusable workflow.

## Debrief questions

Ask:

- What was the input?
- What did Codex produce?
- What did it get right?
- What still needed human review?
- What would make this workflow reusable?
- What real work task does this remind you of?

## Watch for these failure modes

- The learner wants Codex to "just do it."
- The learner skips reading the output.
- The learner wants to paste real sensitive data.
- The learner gets stuck because they cannot imagine a use case.
- The instructor over-explains setup and loses the hands-on part.

## Recovery moves

If setup fails:

- Screen share from the instructor machine.
- Let the learner practice prompt review and safety decisions.

If the learner has no ideas:

- Use `handouts/from-office-pain-to-codex-prompt.md`.
- Ask which category of work is most annoying: writing, lists, meetings, planning, reporting, follow-up, or SOPs.

If Codex produces too much:

- Ask it to create a shorter version.
- Ask it to list only what requires review.
- Ask it to save the reusable prompt, not expand the scope.
