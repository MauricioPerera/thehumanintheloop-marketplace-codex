---
name: github-milestone-manager
description: "Plan and track GitHub milestones with gh CLI. Use to define measurable goals, dates, owners, linked Issues, progress, risks, and release evidence; require confirmation before creating, editing, or closing milestones."
---

# GitHub Milestone Manager

1. Verify repository, milestone, owner, target date, and linked Issue scope.
2. Inspect current milestones and Issue state before drafting a plan.
3. Define outcome, measurable exit criteria, owner, date, dependencies, risks, and evidence.
4. Show exact create/edit/close commands and require confirmation before mutation.
5. Validate the plan:

```text
python plugins/github-repo-governance/skills/github-milestone-manager/scripts/validate_milestone_plan.py --input milestone.md --json milestone-report.json
```
