---
name: github-api-manager
description: "Run safe, reproducible GitHub REST or GraphQL queries through gh CLI. Use for endpoints not covered by specialized plugins; default to GET, allowlist methods and fields, redact credentials, and require explicit approval for mutations."
---

# GitHub API Manager

1. Verify repository, endpoint, API version, authentication, and requested fields.
2. Prefer `gh api` GET queries with explicit `--repo`, `--method GET`, `--jq`, or GraphQL variables.
3. Reject destructive methods or ambiguous endpoints by default. Show the exact request before any POST, PATCH, PUT, or DELETE.
4. Return status, endpoint, query, selected fields, pagination, evidence links, and limitations.
5. Validate the query plan:

```text
python plugins/github-org-lifecycle/skills/github-api-manager/scripts/validate_api_query.py --input api-query.md --json api-report.json
```

Never print tokens, headers, or private response fields unnecessarily.
