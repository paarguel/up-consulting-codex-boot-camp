# 07 - Instructor Checklist

## Before the session

- [ ] Confirm learner has a ChatGPT/OpenAI account with Codex access.
- [ ] Confirm learner has Git installed.
- [ ] Confirm learner has Python installed.
- [ ] Confirm learner can join Zoom and screen share.
- [ ] Send the repo link or zip.
- [ ] Keep a backup copy of the repo ready.
- [ ] Decide whether you are teaching the 90-minute or 3-hour version.

## During setup

- [ ] Have learner open PowerShell.
- [ ] Have learner clone or unzip the repo.
- [ ] Run `.\scripts\setup-check.ps1`.
- [ ] Open Codex from the repo root.
- [ ] Paste the first safe prompt.

## During exercises

- [ ] Learner asks Codex to inspect before editing.
- [ ] Learner asks for a plan before editing.
- [ ] Learner approves a small change.
- [ ] Learner runs tests.
- [ ] Learner reviews the diff.
- [ ] Learner explains the change back to you.

## Watch for

- Prompting too vaguely
- Letting Codex rewrite too much
- Not reading diffs
- Skipping tests
- Treating Codex as always right
- Getting stuck in setup instead of learning the loop

## End of session

Have learner answer:

1. What is Codex?
2. What makes a good prompt?
3. What should Codex ask permission for?
4. What is the inspect-plan-edit-test-review workflow?
5. What would you use this for next?
