---
name: github-fork-manager
description: Audita forks, propietarios, visibilidad, sincronización y políticas de redes de código. Úsala para gobernar forks y preparar cambios de forking con evidencia, mínimo privilegio y rollback.
---

# GitHub Fork Manager

Inspecciona la red de forks y sus relaciones con `gh`. No crees, elimines, transfieras ni cambies visibilidad de forks sin explicar alcance, impacto, dependencias y recuperación.

## Flujo

1. Define repositorio origen, forks objetivo y visibilidad esperada.
2. Revisa propietario, permisos, sincronización, ramas protegidas y consumidores.
3. Detecta forks huérfanos, divergencia, exposición involuntaria y accesos excesivos.
4. Propón política con owner, impacto, validación y rollback.
5. Valida el plan:

```bash
python plugins/github-fork-manager/scripts/validate_fork_plan.py --input forks.md --json forks-report.json
```
