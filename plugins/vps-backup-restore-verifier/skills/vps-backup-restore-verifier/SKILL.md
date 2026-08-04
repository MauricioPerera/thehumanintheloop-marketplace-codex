---
name: vps-backup-restore-verifier
description: Verifica integridad y recuperabilidad de backups de un VPS por SSH sin restaurar sobre producción ni exponer datos.
---
# VPS Backup Restore Verifier

Audita artefactos de backup de un VPS autorizado y separa existencia de recuperabilidad demostrada. Confirma host, usuario, destino, alcance y política de retención antes de inspeccionar.

## Procedimiento

1. Inventaría backups mediante nombres, tamaños, timestamps, permisos, checksums y manifiestos; no imprime contenido ni secretos.
2. Comprueba edad, cobertura declarada de bases de datos, volúmenes, Compose, Nginx, systemd y configuración necesaria para reconstruir servicios.
3. Verifica espacio disponible y compatibilidad de herramientas para un ensayo aislado; marca `NO-VERIFICABLE` si solo existe un archivo sin checksum, manifiesto o procedimiento.
4. Comprueba que el procedimiento documente backup previo, aislamiento, validación de datos, criterio de éxito, limpieza y rollback. No monta, sobrescribe ni elimina producción.
5. Genera un plan de restore rehearsal con destino temporal, ventana, responsable, evidencia esperada y aprobación explícita; no ejecuta la restauración automáticamente.

## Salida y límites

Incluye timestamp UTC, artefacto, edad, integridad, cobertura, RPO/RTO declarado, evidencia, limitaciones y acciones priorizadas. No muestra datos del backup, no lo copia fuera del host, no borra snapshots y no ejecuta `restore`, `drop`, `prune` o reemplazos sin autorización separada.
