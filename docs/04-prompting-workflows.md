# 04 - Prompting and Workflows

## Goal

Teach learners how to turn vague office frustration into a clear Codex task.

## The beginner mistake

Most beginners ask:

```text
Can you help with this?
```

That gives Codex too much freedom and too little context.

## Better pattern

Use this shape:

```text
Context:
- I work in a parish office.
- I am preparing a youth night.
- The files in inputs/ are messy notes, volunteer availability, and budget details.

Task:
- Read the inputs folder.
- Create an event command center.
- Put unclear details in Questions.

Constraints:
- Do not invent missing names, dates, costs, or assignments.
- Keep the tone warm and organized.
- Use only the files in this folder.

Definition of done:
- Save the result in outputs/event-command-center.md.
- Include what I should review before sending anything.
```

## The Codex Work Loop

```text
collect -> contextualize -> produce -> review -> compound
```

### 1. Collect

Put the relevant files in one folder.

Example:

```text
inputs/
  messy-event-notes.md
  volunteer-availability.csv
  budget.csv
  room-and-supplies.md
```

### 2. Contextualize

Tell Codex:

- What the job is
- Who the audience is
- What tone matters
- What the output should include
- What it must not invent
- What "done" means

### 3. Produce

Ask for a real artifact, not just advice.

Examples:

```text
outputs/event-command-center.md
outputs/follow-up-email.md
outputs/action-tracker.csv
outputs/vendor-comparison-table.md
```

### 4. Review

Check:

- Names
- Dates and times
- Money
- Private information
- Commitments
- Tone
- Missing facts
- Anything that will be sent or published

### 5. Compound

Save the prompt and checklist so the learner can repeat the workflow next week.

Example:

```text
workflows/event-command-center-workflow.md
```

## Prompt ladder

### Level 1 - Inspect

```text
Read this folder and explain what files are here, what the task appears to be, and what you would need to clarify. Do not edit anything yet.
```

### Level 2 - Draft

```text
Create the requested draft artifact from the files in inputs/. Put unclear or missing details in a Questions section. Save the result in outputs/.
```

### Level 3 - Review

```text
Review the draft for names, dates, privacy, tone, missing information, and anything that should not be sent yet. Do not rewrite it unless I ask.
```

### Level 4 - Revise

```text
Revise the draft using the review notes. Keep the same structure. Do not add facts that are not in the source files.
```

### Level 5 - Save workflow

```text
Turn this successful prompt into a reusable workflow I can use next time. Save it as workflow.md with inputs needed, prompt, review checklist, and final-send reminders.
```

## Bad prompts and safer rewrites

| Vague prompt | Safer version |
|---|---|
| Make this good. | Read the inputs and create a draft with a Questions section for unclear details. |
| Write the email. | Draft the email, then list what I must verify before sending. |
| Clean this spreadsheet. | Identify duplicates, missing fields, and suspicious rows. Save a review list before changing data. |
| Summarize this meeting. | Create minutes, decisions, action items, open questions, and follow-up email. |
| Automate this. | First map the repeated workflow: inputs, output, review risk, and reusable prompt. |
| Search the internet and decide. | List sources, compare options against criteria, and separate facts from recommendations. |

## Instructor tip

Have the learner say this out loud:

> Inspect first. Draft second. Review third. Send never without a human.
