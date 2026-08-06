---
name: github-dependency-review-manager
description: Revisa dependencias nuevas en Pull Requests, lockfiles, licencias, advisories y riesgo de supply chain. Úsala antes de aprobar cambios de dependencias.
---

# GitHub Dependency Review Manager

Compara la base y el head del Pull Request con `gh`. Revisa paquete, versión, ecosistema, licencia, advisory, maintainer y lockfile. No apruebes ni cierres el PR automáticamente.

## Flujo

1. Define PR, repositorio y rama base.
2. Lista dependencias agregadas, actualizadas o retiradas.
3. Prioriza severidad, explotabilidad, licencia y procedencia.
4. Propón acción, owner, evidencia y verificación.
5. Valida:

```bash
python plugins/github-security-suite/skills/github-dependency-review-manager/scripts/validate_dependency_review.py --input review.md --json review-report.json
```
