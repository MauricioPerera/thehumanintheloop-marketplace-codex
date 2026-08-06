---
name: github-archive-manager
description: Evalúa si un repositorio debe archivarse o restaurarse usando actividad, consumidores, dependencias, retención y riesgos. Úsala para decisiones de ciclo de vida con recuperación verificable.
---

# GitHub Archive Manager

Archivar es una decisión de ciclo de vida, no una limpieza automática. Revisa dependencias y consumidores, comunica el impacto y solicita confirmación antes de archivar o restaurar.

## Flujo

1. Define repositorio, propietario y criterio de inactividad.
2. Revisa actividad, Issues, PRs, releases, paquetes, Actions y consumidores.
3. Detecta integraciones, dependencias, enlaces públicos y requisitos de retención.
4. Prepara decisión con impacto, comunicación, validación y rollback.
5. Valida:

```bash
python plugins/github-org-lifecycle/skills/github-archive-manager/scripts/validate_archive_plan.py --input archive.md --json archive-report.json
```
