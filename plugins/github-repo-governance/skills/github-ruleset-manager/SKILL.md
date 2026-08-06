---
name: github-ruleset-manager
description: Audita y diseña reglasets de GitHub para ramas, tags y workflows. Úsala para revisar condiciones, bypass actors, checks requeridos y planes de protección reproducibles antes de mutar repositorios.
---

# GitHub Ruleset Manager

Convierte la política de protección en evidencia y un plan aplicable. Usa `gh api` o `gh` en modo lectura para inspeccionar reglasets; cualquier creación, actualización o eliminación requiere mostrar el diff y confirmación explícita.

## Flujo

1. Define repositorio, patrones objetivo, actores con bypass y nivel de enforcement.
2. Audita reglas de branch/tag, pull requests, revisiones, status checks, firmas y workflows.
3. Detecta conflictos, excepciones excesivas y reglas sin cobertura.
4. Genera un plan con impacto, orden de aplicación, validación posterior y rollback.
5. Valida el plan con:

```bash
python plugins/github-repo-governance/skills/github-ruleset-manager/scripts/validate_ruleset_plan.py --input ruleset-plan.md --json ruleset-report.json
```

Nunca habilites enforcement sobre producción sin confirmar propietarios, bypass de emergencia y procedimiento de recuperación.
