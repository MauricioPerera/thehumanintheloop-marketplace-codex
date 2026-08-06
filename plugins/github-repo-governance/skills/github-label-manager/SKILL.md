---
name: github-label-manager
description: "Design and maintain GitHub label taxonomies with gh CLI. Use to audit labels, propose naming and color consistency, prepare bulk changes, and apply them only after explicit confirmation."
---

# GitHub Label Manager

1. Inspect current labels and their usage before proposing changes.
2. Define a taxonomy with name, purpose, color, description, owner, and migration mapping.
3. Show create, edit, merge, or delete commands and affected Issues/PRs. Deleting or renaming labels requires confirmation.
4. Avoid labels that encode secrets, personal data, or unreviewed severity claims.
5. Validate the taxonomy:

```text
python plugins/github-repo-governance/skills/github-label-manager/scripts/validate_label_plan.py --input labels.md --json labels-report.json
```
