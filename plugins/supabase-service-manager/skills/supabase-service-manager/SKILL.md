---
name: supabase-service-manager
description: Opera servicios Supabase self-hosted en Docker Compose por SSH con diagnóstico, logs acotados, reinicios controlados y rollback explícito.
---

# Supabase Service Manager

Usa esta skill para diagnosticar o cambiar el estado de los servicios Docker que componen Supabase self-hosted.

## Flujo seguro

1. Localiza el directorio Compose sin leer `.env` ni imprimir secretos.
2. Ejecuta `docker compose ps`, `config --services` y logs acotados por servicio y tiempo.
3. Distingue fallo de aplicación, dependencia, red, volumen, healthcheck y capacidad del host.
4. Antes de `restart`, `up`, `pull`, `stop` o cambios de Compose, presenta servicio, comando, impacto, ventana, backup y rollback.
5. Requiere confirmación justo antes de mutar. Después verifica healthcheck, puertos y dependencias.

## Límites

Nunca ejecutes `docker compose down`, `docker system prune`, borres volúmenes, cambies firewall o edites `.env` desde esta skill sin un plan específico y una confirmación separada. Los logs deben limitarse por cantidad y redactarse antes de mostrarlos.

Valida un plan con `python scripts/validate_service_plan.py --plan <archivo>`.
