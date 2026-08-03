---
name: github-team-manager
description: Audita equipos de GitHub, membresías, roles, equipos anidados y repositorios asignados. Úsala para revisar permisos y preparar cambios de acceso con mínimo privilegio y confirmación explícita.
---

# GitHub Team Manager

Inspecciona equipos y accesos con `gh` o `gh api` en modo lectura. No agregues, retires ni cambies miembros o permisos sin mostrar el diff, propietario, impacto y confirmación expresa.

## Flujo

1. Define organización, equipo, repositorios y ventana de revisión.
2. Lista miembros, roles, equipos anidados, repositorios y permisos efectivos.
3. Detecta accesos excesivos, cuentas inactivas, duplicación y excepciones.
4. Propón ajuste de mínimo privilegio con owner, impacto, validación y rollback.
5. Valida el informe:

```bash
python plugins/github-team-manager/scripts/validate_team_access.py --input team-audit.md --json team-report.json
```
