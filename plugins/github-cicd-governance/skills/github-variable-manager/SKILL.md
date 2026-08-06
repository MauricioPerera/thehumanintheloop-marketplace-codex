---
name: github-variable-manager
description: "Audit GitHub Actions variable names, scopes, and references with gh CLI. Use for repository, environment, and organization variable reviews; never read, print, or infer secret values and require confirmation before changes."
---

# GitHub Variable Manager

1. Inventory variable names and scopes only; treat secret values as inaccessible.
2. Detect duplicate names, wrong scope, missing references, unsafe naming, and secrets placed in plain variables.
3. Show proposed create/edit/delete commands without values in logs or reports.
4. Require confirmation before changing variables or secrets.
5. Validate the audit:

```text
python plugins/github-cicd-governance/skills/github-variable-manager/scripts/validate_variable_audit.py --input variables.md --json variables-report.json
```
