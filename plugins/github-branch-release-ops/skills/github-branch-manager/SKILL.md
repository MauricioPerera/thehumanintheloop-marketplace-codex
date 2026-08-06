---
name: github-branch-manager
description: "Inspect and manage Git branches with git and gh CLI. Use for branch comparison, creation, cleanup, protection planning, or remote tracking; never delete, force-push, or change protected branches without explicit confirmation."
---

# GitHub Branch Manager

1. Verify repository, current branch, worktree status, upstream, and target branch.
2. Inspect refs, divergence, commits, checks, and protection before proposing a change.
3. Produce a plan with branch, operation, impact, rollback, and exact command.
4. Require confirmation before creating remote branches, deleting branches, force-pushing, or changing protection.
5. Validate the plan:

```text
python plugins/github-branch-manager/scripts/validate_branch_plan.py --input branch.md --json branch-report.json
```
