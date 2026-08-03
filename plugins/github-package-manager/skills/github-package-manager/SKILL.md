---
name: github-package-manager
description: "Inspect and plan GitHub Packages operations with gh CLI or API. Use for package versions, visibility, retention, publishing, and cleanup; preview destructive actions and require confirmation before mutation."
---

# GitHub Package Manager

1. Verify package owner, ecosystem, package name, version scope, visibility, and permissions.
2. Inspect versions, consumers, tags, download evidence, and retention constraints.
3. Prepare publish, visibility, delete, or cleanup plans with rollback and verification.
4. Never delete a version without confirming consumers and the exact immutable target.
5. Validate the plan:

```text
python plugins/github-package-manager/scripts/validate_package_plan.py --input packages.md --json packages-report.json
```
