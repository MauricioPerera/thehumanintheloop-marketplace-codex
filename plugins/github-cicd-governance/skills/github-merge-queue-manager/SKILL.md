---
name: github-merge-queue-manager
description: Analiza merge queues, pull requests en espera, checks, grupos de merge y tiempos de integración. Úsala para diagnosticar colas y preparar cambios de configuración sin ejecutar merges automáticamente.
---

# GitHub Merge Queue Manager

Usa `gh` para revisar estado, checks y políticas de integración. Distingue una PR bloqueada por código, política, capacidad o conflicto. Hacer merge, habilitar la cola o cambiar reglas requiere confirmación explícita.

## Flujo

1. Define repositorio, rama objetivo y ventana temporal.
2. Relaciona PR, grupo de merge, checks, reviewers, estado y tiempo en cola.
3. Identifica cuellos de botella y causas repetidas con evidencia.
4. Prepara plan con prioridad, impacto, owner y verificación posterior.
5. Valida el informe:

```bash
python plugins/github-cicd-governance/skills/github-merge-queue-manager/scripts/validate_merge_queue.py --input queue.md --json queue-report.json
```
