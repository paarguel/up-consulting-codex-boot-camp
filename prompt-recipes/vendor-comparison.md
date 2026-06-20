# Prompt Recipe - Vendor Comparison

Use with:

```text
sample-work-packs/vendor-comparison/
```

## Prompt

```text
Use the work pack at sample-work-packs/vendor-comparison/.

Read everything in sample-work-packs/vendor-comparison/inputs/.

Create a vendor comparison packet with:
1. comparison table against the stated criteria
2. strengths and weaknesses for each option
3. missing information to ask each vendor
4. risk list
5. recommendation section that clearly separates facts from judgment

Rules:
- Use only the provided vendor notes and requirements.
- Do not invent pricing, contract terms, features, or availability.
- Flag missing information instead of guessing.
- Save the result in sample-work-packs/vendor-comparison/outputs/vendor-comparison-packet.md.

After saving, list the decision points a human should confirm.
```

## Review focus

- Pricing
- Contract terms
- Fit against requirements
- Unsupported assumptions
- Procurement or approval rules
