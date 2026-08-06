---
name: github-traffic-manager
description: "Analyze GitHub repository traffic through gh API. Use for views, clones, referrers, and popular paths; state retention windows, permissions, aggregation limits, and never infer unique users from unavailable data."
---

# GitHub Traffic Manager

1. Verify repository, owner permissions, date window, and traffic endpoint.
2. Query views, clones, referrers, and paths with explicit dates and preserve raw totals.
3. Explain retention and aggregation limits; do not present views as unique users.
4. Validate the report:

```text
python plugins/github-traffic-manager/scripts/validate_traffic_report.py --input traffic.md --json traffic-report.json
```
