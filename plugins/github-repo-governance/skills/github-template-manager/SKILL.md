---
name: github-template-manager
description: "Review and maintain GitHub Issue, Pull Request, and config templates. Use to improve required context, acceptance criteria, reproduction details, security guidance, and consistency; preview file changes before writing them."
---

# GitHub Template Manager

1. Inspect existing `.github/ISSUE_TEMPLATE`, `PULL_REQUEST_TEMPLATE`, and config files.
2. Identify missing context, acceptance criteria, reproduction steps, validation evidence, security warnings, and ownership.
3. Draft portable Markdown templates and show file paths plus a diff before applying changes.
4. Do not overwrite a repository's templates or remove fields without confirmation.
5. Validate the template set:

```text
python plugins/github-template-manager/scripts/validate_templates.py --input templates.md --json templates-report.json
```
