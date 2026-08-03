---
name: rfp-response-builder
description: Responds to RFPs, tenders, RFIs, and formal questionnaires from user-provided requirements and evidence. Use it to build a traceable response, a compliance matrix, open-item tracking, and to avoid invented capabilities, figures, or commitments.
---

# RFP Response Builder

Build a commercial or technical response that sales, legal, and delivery teams can review.

## Workflow

1. Receive the requirements document and, separately, the organization's capabilities, references, constraints, prices, and authorized policies.
2. Extract every mandatory and optional requirement with its original identifier. If no identifier exists, assign `REQ-001`, `REQ-002`, and so on without losing the original text.
3. For each requirement, write a direct answer and link it to available evidence. Classify it as `Compliant`, `Partial`, `Non-compliant`, or `Open item`.
4. Separate what the client requests from what the organization can prove. Mark any item that needs human confirmation as open.
5. Do not invent clients, certifications, metrics, dates, prices, integrations, staff, SLAs, or case studies. Do not turn a future intention into a current capability.
6. Deliver, in this order:
   - executive response and scope;
   - compliance matrix with ID, requirement, response, evidence, status, and exception;
   - implementation approach and deliverables, only with authorized commitments;
   - assumptions, exclusions, risks, and open questions;
   - bid/no-bid recommendation when there are critical gaps or dependencies.
7. Run the validator before delivery:

```text
python plugins/rfp-response-builder/scripts/validate_rfp_response.py --rfp rfp.md --source capabilities.md --output response.md --json rfp-report.json
```

Fix every `[FAILED]` error. Keep warnings visible for human review. A `PASSED` report means that structure and basic traceability are consistent; it does not mean that the offer has legal or commercial approval.

## Writing rules

- Preserve the requirement language and lead with the verifiable status.
- Cite the internal source or evidence fragment supporting each claim.
- Use `[CONFIRM]` for missing data and `[EXCEPTION]` for accepted deviations.
- Do not guarantee outcomes or use absolutes such as "no risk", "100%", or "guaranteed" without explicit documentary authorization.
- Do not include credentials, secrets, unnecessary personal data, or confidential information that is not needed for the response.
