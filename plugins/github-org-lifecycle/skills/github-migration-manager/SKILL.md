---
name: github-migration-manager
description: Planifica migraciones de repositorios considerando código, Issues, PRs, Actions, webhooks, permisos, integraciones y rollback. Úsala antes de transferir, importar o cambiar el origen de un repositorio.
---

# GitHub Migration Manager

Construye un inventario antes de migrar. No transfieras, borres ni cambies URLs sin checklist, owner, ventana de mantenimiento, validación de consumidores y recuperación confirmada.

## Flujo

1. Define origen, destino, repositorios y restricciones.
2. Inventaría ramas, releases, Issues, PRs, Actions, secretos, webhooks y dependencias.
3. Identifica URLs, permisos, integraciones y usuarios afectados.
4. Genera fases, smoke tests, comunicación y rollback.
5. Valida:

```bash
python plugins/github-org-lifecycle/skills/github-migration-manager/scripts/validate_migration_plan.py --input migration.md --json migration-report.json
```
