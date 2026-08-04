---
name: vps-deployment-readiness-auditor
description: Audita la preparación y recuperabilidad de un despliegue Docker Compose en un VPS sin actualizar, reiniciar ni eliminar servicios.
---
# VPS Deployment Readiness Auditor

Evalúa un despliegue autorizado antes de cambiarlo. Confirma host, usuario, proyecto, rama o versión objetivo y ventana de mantenimiento antes de inspeccionar.

## Procedimiento

1. Identifica el proyecto Compose y registra servicios, imágenes, versiones, puertos, redes, volúmenes, dependencias y healthchecks sin mostrar variables secretas.
2. Ejecuta validaciones de sintaxis y configuración (`docker compose config --quiet` o equivalente) sin levantar contenedores.
3. Comprueba que los servicios críticos tengan healthcheck, política de reinicio, límites razonables, dependencias explícitas y puertos intencionales.
4. Compara la versión objetivo con el estado activo; separa cambios de imagen, configuración, esquema y datos. No descargues imágenes ni ejecutes migraciones durante la auditoría.
5. Verifica la existencia documentada de backup reciente, procedimiento de rollback, tags inmutables y comandos de recuperación; marca como `NO-VERIFICABLE` lo que no tenga evidencia.
6. Produce un plan por fases: preflight, cambio, healthcheck, observación, rollback y criterio de abortar.

## Salida y límites

Incluye timestamp UTC, proyecto, evidencia acotada, riesgos, bloqueadores y comandos propuestos con impacto y rollback. No ejecuta `pull`, `up`, `down`, `restart`, `rm`, `prune`, migraciones, cambios de `.env`, DNS, proxy o firewall sin confirmación explícita.
