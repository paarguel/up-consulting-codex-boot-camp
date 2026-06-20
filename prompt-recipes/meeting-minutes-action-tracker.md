# Prompt Recipe - Meeting Minutes and Action Tracker

Use with:

```text
sample-work-packs/meeting-to-action-items/
```

## Prompt

```text
Use the work pack at sample-work-packs/meeting-to-action-items/.

Read everything in sample-work-packs/meeting-to-action-items/inputs/.

Create a meeting follow-up package with:
1. short meeting summary
2. decisions made
3. action tracker table with owner, task, due date, and status
4. open questions
5. follow-up email draft

Rules:
- Do not invent owners or due dates.
- If the notes imply an action but do not name an owner, put "Unassigned" and flag it.
- If a date is unclear, put it in Open Questions.
- Keep the tone concise and professional.
- Save the result in sample-work-packs/meeting-to-action-items/outputs/meeting-follow-up-package.md.

After saving, list the items that need human review.
```

## Review focus

- Owners
- Due dates
- Decisions versus suggestions
- Sensitive or internal details
- Follow-up email recipients
