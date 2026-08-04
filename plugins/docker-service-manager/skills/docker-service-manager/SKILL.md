---
name: docker-service-manager
description: Planifica cambios de servicios Docker Compose en un VPS por SSH con preflight, confirmación explícita, ventana de cambio y rollback.
---

# Docker Service Manager

Administra servicios Compose sin ejecutar mutaciones hasta que el usuario confirme el plan exacto.

## Flujo obligatorio

1. Localiza el proyecto Compose y valida `docker compose config` sin imprimir secretos.
2. Captura estado previo: servicios, imágenes, healthchecks, puertos, logs recientes y espacio.
3. Presenta el comando exacto, impacto, duración, backup o snapshot requerido y rollback verificable.
4. Solo tras confirmación ejecuta una mutación acotada, observa el resultado y corre smoke checks.
5. Si falla, detén la cadena, conserva evidencia y ofrece rollback; nunca hagas `down -v`, `rm -f` o `prune` implícitamente.

No inventes rutas Compose, variables ni credenciales.
