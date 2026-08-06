---
name: github-activity-manager
description: "Summarize GitHub repository activity with gh CLI. Use for dated reports over commits, Issues, Pull Requests, reviews, releases, and contributors; state scope, links, bots, and limitations."
---

# GitHub Activity Manager

1. Define repository, time window, event types, branch, and timezone.
2. Collect dated evidence with `gh` and git; preserve links and distinguish merged, closed, and open work.
3. Separate measurements from interpretation and disclose pagination, bots, squash merges, and unavailable data.
4. Validate the report:

```text
python plugins/github-collab-activity/skills/github-activity-manager/scripts/validate_activity_report.py --input activity.md --json activity-report.json
```
