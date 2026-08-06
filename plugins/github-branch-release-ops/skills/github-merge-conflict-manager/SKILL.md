---
name: github-merge-conflict-manager
description: Diagnostica conflictos de Pull Requests, archivos afectados, base, head, checks y owners. Úsala para preparar una resolución revisable sin sobrescribir ramas automáticamente.
---

# GitHub Merge Conflict Manager

Inspecciona la base y el head con `gh`, identifica archivos y commits divergentes y separa conflicto textual de conflicto semántico. Resolver, hacer push o actualizar la PR requiere confirmación explícita.

## Flujo

1. Define PR, repositorio, rama base y rama head.
2. Lista archivos, commits, checks y propietarios afectados.
3. Explica opciones de resolución, riesgos y pruebas necesarias.
4. Prepara plan, owner, validación y rollback.
5. Valida:

```bash
python plugins/github-merge-conflict-manager/scripts/validate_conflict_plan.py --input conflict.md --json conflict-report.json
```
