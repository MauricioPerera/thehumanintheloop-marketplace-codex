---
name: github-action-permissions-manager
description: Audita permissions de workflows, alcance de GITHUB_TOKEN, eventos, forks y acciones de terceros. Úsala para reducir privilegios antes de modificar workflows.
---

# GitHub Action Permissions Manager

Lee workflows y políticas de Actions; no los edita automáticamente. Identifica permisos explícitos, heredados, escritura innecesaria, forks y dependencias de terceros. Presenta diff y solicita confirmación.

## Flujo

1. Define repositorio, workflows y eventos.
2. Calcula scopes efectivos y permisos por job.
3. Detecta write-all, tokens heredados, pull_request_target y terceros no fijados.
4. Propón mínimo privilegio con impacto, validación y rollback.
5. Valida:

```bash
python plugins/github-action-permissions-manager/scripts/validate_action_permissions.py --input permissions.md --json permissions-report.json
```
