---
name: github-environment-manager
description: "Audit and plan GitHub deployment environments, reviewers, branch rules, and gates with gh API. Use for deployment safety reviews; never expose environment secrets or mutate protection without explicit confirmation."
---

# GitHub Environment Manager

1. Verify repository, environment, deployment branches, reviewers, and permissions.
2. Inspect protection rules without printing secret names or values unnecessarily.
3. Produce current/proposed values, impact, rollback, and verification steps.
4. Require confirmation before changing reviewers, branches, gates, or environment settings.
5. Validate the plan:

```text
python plugins/github-cicd-governance/skills/github-environment-manager/scripts/validate_environment_plan.py --input environment.md --json environment-report.json
```
