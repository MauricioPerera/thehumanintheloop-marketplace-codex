---
name: github-codeowners-manager
description: "Design and validate GitHub CODEOWNERS mappings. Use to inspect ownership coverage, map paths to users or teams, detect invalid patterns, and prepare reviewable changes without changing approval rules automatically."
---

# GitHub CODEOWNERS Manager

1. Inspect CODEOWNERS in supported locations and identify the active file.
2. Map critical paths to verified users or teams; mark unknown owners as open items.
3. Check ordering, wildcard behavior, missing coverage, invalid handles, and sensitive paths.
4. Produce a diff and validation report. Require confirmation before writing CODEOWNERS or changing branch protections.
5. Validate the mapping:

```text
python plugins/github-codeowners-manager/scripts/validate_codeowners.py --input CODEOWNERS --json codeowners-report.json
```
