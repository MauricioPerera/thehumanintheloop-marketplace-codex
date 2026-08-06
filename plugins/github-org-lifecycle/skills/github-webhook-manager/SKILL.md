---
name: github-webhook-manager
description: "Audit and plan GitHub webhooks with gh API. Use to inspect endpoints, event scope, delivery behavior, and secret handling; redact credentials and require confirmation before any webhook mutation or test delivery."
---

# GitHub Webhook Manager

1. Verify repository, endpoint owner, permissions, target URL, event scope, and delivery need.
2. Inspect current hooks without printing secrets. Check least-privilege events, HTTPS, retries, and receiver ownership.
3. Prepare a redacted create/edit/test/delete plan with rollback and verification.
4. Require explicit confirmation for every mutation or test delivery.
5. Validate the plan:

```text
python plugins/github-org-lifecycle/skills/github-webhook-manager/scripts/validate_webhook_plan.py --input webhook.md --json webhook-report.json
```
