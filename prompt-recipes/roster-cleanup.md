# Prompt Recipe - Roster Cleanup

Use with:

```text
sample-work-packs/messy-roster-cleanup/
```

## Prompt

```text
Use the work pack at sample-work-packs/messy-roster-cleanup/.

Read the files in sample-work-packs/messy-roster-cleanup/inputs/.

Create a roster cleanup review packet.

Include:
1. suspected duplicate records
2. missing required fields
3. inconsistent formatting
4. permission or status issues
5. rows that need human review
6. a cleaned-roster.csv draft if you can safely normalize obvious formatting without inventing data

Rules:
- Do not invent missing contact details, ages, permissions, or family relationships.
- Preserve the original inputs.
- Put uncertain rows in a review list instead of silently changing them.
- Save the review packet in sample-work-packs/messy-roster-cleanup/outputs/roster-cleanup-review.md.
- If you create a cleaned CSV, save it as sample-work-packs/messy-roster-cleanup/outputs/cleaned-roster.csv.

After saving, explain the cleanup decisions and what still needs human review.
```

## Review focus

- Duplicate people
- Missing permissions
- Contact details
- Any real children or private data
- Changes made to records
