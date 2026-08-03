---
name: github-security-manager
description: "Audit GitHub security alerts and repository risks with gh CLI, including code scanning, secret scanning, and repository security settings. Use for evidence-based remediation plans; never close alerts or change policies without explicit approval."
---

# GitHub Security Manager

1. Verify authentication, repository, permissions, and requested alert scope.
2. Inspect code scanning, secret scanning, Dependabot, branch protection, and security policy evidence with `gh api` or supported `gh` commands.
3. Classify each finding by severity, confidence, affected path, source, owner, and remediation status. Never expose secret values.
4. Separate confirmed findings from hypotheses and document evidence links.
5. Propose remediation, rollback, and verification commands. Require confirmation before dismissing alerts, changing settings, or rotating credentials.
6. Validate the audit report:

```text
python plugins/github-security-manager/scripts/validate_security_report.py --input security-report.md --json security-report.json
```

The report must include repository, scope, findings, severity, evidence, remediation, verification, and open decisions.
