---
name: supabase-backup-manager
description: Planifica, verifica y ejecuta backups y recuperaciones de PostgreSQL en Supabase self-hosted por SSH con retención, cifrado, prueba y rollback.
---

# Supabase Backup Manager

Usa esta skill para conocer el estado de backups, crear un plan de respaldo, verificar archivos y preparar una recuperación.

## Seguridad y flujo

1. Identifica base, destino, ventana, retención y responsable.
2. Verifica espacio, permisos, cifrado y disponibilidad del destino sin leer datos.
3. Para backup: define formato, compresión, checksum, retención y prueba de restauración.
4. Para restore: detalla snapshot, impacto, downtime, backup previo y rollback; exige confirmación inmediata.
5. No subas backups a servicios externos ni los muestres en la conversación.

Nunca borres backups, volúmenes o snapshots desde esta skill sin autorización separada. Valida planes con `python scripts/validate_backup_plan.py --plan <archivo>`.
