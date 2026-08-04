---
name: supabase-upgrade-manager
description: Evalúa y prepara upgrades de Supabase self-hosted por SSH con matriz de versiones, compatibilidad, backup, ventana y rollback antes de tocar Docker Compose.
---

# Supabase Upgrade Manager

Usa esta skill para evaluar versiones de imágenes, cambios de Compose y riesgos antes de actualizar Supabase self-hosted.

## Flujo obligatorio

1. Inventaría versiones actuales y destino sin hacer `pull`.
2. Revisa changelog/release notes y dependencias internas: Postgres, Auth, Realtime, Storage, Kong, Supavisor, Studio y Edge Runtime.
3. Comprueba backup reciente, espacio, healthchecks, compatibilidad y ventana de mantenimiento.
4. Genera plan con orden de actualización, comandos exactos, downtime, observabilidad y rollback.
5. Pide confirmación antes de `pull`, cambios de Compose, migraciones o reinicios.
6. Verifica healthchecks, logs acotados, endpoints y versión final; reporta cualquier degradación.

No hagas upgrades parciales improvisados, no borres imágenes antiguas automáticamente y no modifiques `.env` sin una revisión de configuración. Valida el plan con `python scripts/validate_upgrade_plan.py --plan <archivo>`.
