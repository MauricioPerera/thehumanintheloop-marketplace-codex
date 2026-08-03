---
name: github-repository-manager
description: "Inspect and configure GitHub repositories with gh CLI. Use for repository metadata, visibility, features, branch settings, archival, transfer, or creation workflows; distinguish read-only inspection from high-impact mutations and require confirmation."
---

# GitHub Repository Manager

1. Verify owner, repository, authentication, current remote, and requested operation.
2. Inspect metadata and current settings before proposing a change.
3. Produce a plan with property, current value, proposed value, impact, rollback, and exact command.
4. Require confirmation before creating, archiving, transferring, changing visibility, changing branch protection, or deleting a repository.
5. Validate the plan:

```text
python plugins/github-repository-manager/scripts/validate_repository_plan.py --input repository-plan.md --json repository-report.json
```

Never print tokens or infer authorization from repository ownership alone.
