---
name: github-checks-manager
description: Analiza checks de GitHub, conclusiones, annotations, tiempos y fallos repetidos para diagnosticar CI con evidencia. Úsala para resumir ejecuciones y preparar remediaciones sin alterar workflows automáticamente.
---

# GitHub Checks Manager

Inspecciona check runs y resultados asociados a commits o Pull Requests usando `gh`. Mantén el diagnóstico separado de la remediación, cita URLs o identificadores de ejecución y solicita confirmación antes de editar workflows, rerun jobs o cancelar ejecuciones.

## Flujo

1. Define repositorio, PR o SHA y ventana temporal.
2. Agrupa checks por estado, conclusión, job, duración y annotation.
3. Distingue fallos de código, infraestructura, permisos y flaky tests.
4. Propón remediación priorizada con evidencia, impacto, owner y verificación.
5. Valida el informe con:

```bash
python plugins/github-cicd-governance/skills/github-checks-manager/scripts/validate_checks_report.py --input checks.md --json checks-report.json
```

No inventes conclusiones cuando faltan logs; declara los datos no observables.
