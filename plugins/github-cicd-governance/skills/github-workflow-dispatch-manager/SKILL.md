---
name: github-workflow-dispatch-manager
description: Prepara ejecuciones manuales de workflows con ref, inputs, permisos, entorno y consecuencias. Úsala para revisar y simular dispatch antes de ejecutarlo.
---

# GitHub Workflow Dispatch Manager

Inspecciona el workflow y sus inputs antes de cualquier `gh workflow run`. Presenta comando, ref, valores no sensibles, permisos, entorno, impacto y verificación; ejecutar requiere confirmación explícita.

## Flujo

1. Define repositorio, workflow, ref e inputs.
2. Confirma que el workflow soporte `workflow_dispatch`.
3. Valida tipos, valores permitidos, secretos, entornos y efectos.
4. Prepara comando reproducible y plan de seguimiento.
5. Valida:

```bash
python plugins/github-cicd-governance/skills/github-workflow-dispatch-manager/scripts/validate_dispatch_plan.py --input dispatch.md --json dispatch-report.json
```
