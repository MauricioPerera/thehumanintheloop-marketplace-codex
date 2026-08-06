---
name: github-contributor-manager
description: "Analyze GitHub contributor activity with gh CLI and prepare evidence-based ownership or reviewer plans. Use for contribution summaries, bus-factor signals, and reviewer suggestions; do not assign people or infer authority automatically."
---

# GitHub Contributor Manager

1. Define repository, time window, contribution types, and privacy scope.
2. Inspect commits, merged PRs, reviews, Issues, and paths; preserve links and dates.
3. Separate measured activity from inferred expertise and state limitations such as squash merges or bots.
4. Propose owners or reviewers with evidence, confidence, and opt-out/open questions. Require confirmation before assignment.
5. Validate the report:

```text
python plugins/github-contributor-manager/scripts/validate_contributor_report.py --input contributors.md --json contributors-report.json
```
