---
name: release-readiness
description: Comprueba si un repositorio está listo para release, publicación o despliegue. Úsala antes de crear tags, paquetes, PRs finales o despliegues.
---
# Release Readiness

Evalúa evidencia disponible y no convierte ausencia de pruebas en aprobación.

## Flujo
1. Ejecuta `python plugins/release-readiness/scripts/check_release.py .`.
2. Comprueba versión, changelog, licencia, README, tests, CI y estado del repositorio.
3. Ejecuta validadores y tests existentes; registra comandos y resultados.
4. Separa bloqueantes de pendientes y solicita confirmación antes de publicar.

## Salida
Entrega `[PASSED]`, `[FAILED]` o `[NEEDS REVIEW]`, evidencias y checklist residual.
