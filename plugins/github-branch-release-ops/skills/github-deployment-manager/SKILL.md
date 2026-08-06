---
name: github-deployment-manager
description: Analiza deployments de GitHub, estados, commits, entornos, actores, tiempos y rollback. Úsala para operaciones de promoción, cancelación o recuperación con evidencia y confirmación previa.
---

# GitHub Deployment Manager

Resume el estado operativo de despliegues con `gh` y `gh api`. No promociones, canceles ni reviertas despliegues automáticamente; primero presenta objetivo, diff operativo, impacto, validación y procedimiento de rollback.

## Flujo

1. Define repositorio, SHA, entorno y ventana temporal.
2. Relaciona deployment, status, workflow, commit, actor y URL de evidencia.
3. Distingue pendiente, activo, éxito, fallo y cancelación; no inventes estados ausentes.
4. Propón promoción o rollback con owner, precondiciones, monitoreo y recuperación.
5. Valida el plan:

```bash
python plugins/github-branch-release-ops/skills/github-deployment-manager/scripts/validate_deployment_plan.py --input deployment.md --json deployment-report.json
```
