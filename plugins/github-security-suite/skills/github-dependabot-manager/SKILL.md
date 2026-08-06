---
name: github-dependabot-manager
description: "Review GitHub Dependabot alerts and dependency updates with gh CLI. Use to group alerts, assess severity and breaking-change risk, propose upgrade order, and prepare evidence before applying updates."
---

# GitHub Dependabot Manager

1. Verify repository, package ecosystem, lockfile source, and alert scope.
2. Inspect Dependabot alerts and related PRs. Capture package, vulnerable range, fixed version, severity, manifest, and evidence URL.
3. Group compatible upgrades and identify breaking changes, runtime constraints, and required tests.
4. Produce an ordered upgrade plan with owner, command, validation, rollback, and open decisions.
5. Require confirmation before merging Dependabot PRs, changing update configuration, or applying dependency changes.
6. Validate the plan:

```text
python plugins/github-security-suite/skills/github-dependabot-manager/scripts/validate_dependabot_plan.py --input dependabot-plan.md --json dependabot-report.json
```

Never claim an alert is fixed without a current alert or CI result proving it.
