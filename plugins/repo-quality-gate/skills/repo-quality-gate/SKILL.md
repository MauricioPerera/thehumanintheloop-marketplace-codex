---
name: repo-quality-gate
description: Ejecuta una revisión de calidad previa a publicación sobre repositorios de código. Úsala antes de commit, release, PR o despliegue.
---
# Repo Quality Gate

Inspecciona el repositorio y reporta riesgos sin afirmar que una revisión sustituye CI o aprobación humana.

## Flujo
1. Revisa `git status`, cambios, tests, lint, secretos y archivos de configuración.
2. Ejecuta `python plugins/repo-quality-gate/scripts/check_repo.py .`.
3. Ejecuta las pruebas y validadores disponibles, sin inventar comandos.
4. Clasifica bloqueantes, advertencias y comprobaciones pendientes.
5. No hagas push, releases ni acciones destructivas sin autorización.

## Salida
Entrega `[PASSED]`, `[FAILED]` o `[NEEDS REVIEW]`, evidencias y acciones exactas antes de publicar.
