---
name: github-organization-settings-manager
description: "Audita configuración y políticas de organizaciones de GitHub: permisos base, repositorios, forking, Actions, seguridad, membresías y límites. Úsala antes de cambiar políticas globales."
---

# GitHub Organization Settings Manager

Inspecciona la organización en modo lectura y separa configuración observada de recomendaciones. Toda mutación global requiere owner, impacto, diff, ventana, verificación y confirmación explícita.

## Flujo

1. Define organización, política y repositorios afectados.
2. Revisa permisos base, visibilidad, forking, Actions, seguridad y membresías.
3. Detecta excepciones, exposición y conflictos con equipos o rulesets.
4. Prepara cambio mínimo con rollback y comunicación.
5. Valida:

```bash
python plugins/github-org-lifecycle/skills/github-organization-settings-manager/scripts/validate_org_settings.py --input org.md --json org-report.json
```
