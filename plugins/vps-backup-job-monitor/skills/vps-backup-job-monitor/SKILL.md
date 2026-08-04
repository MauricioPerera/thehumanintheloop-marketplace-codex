---
name: vps-backup-job-monitor
description: Audita ejecución, frescura, fallos y cobertura de jobs cron o systemd que generan backups en un VPS sin lanzarlos.
---
# VPS Backup Job Monitor

Audita jobs de backup de un VPS autorizado y comprueba evidencia de ejecución reciente. Confirma host, servicios en alcance, RPO esperado y zona horaria antes de inspeccionar.

## Procedimiento

1. Inventaría entradas cron, unidades y timers systemd relacionados con backup sin mostrar comandos completos, credenciales ni destinos sensibles.
2. Comprueba última ejecución, próxima ejecución, exit status, duración, errores acotados y timestamps de artefactos mediante metadatos, sin leer contenido.
3. Correlaciona job→servicio→artefacto→retención y clasifica `CURRENT`, `LATE`, `FAILED`, `NO-OUTPUT` o `NO-VERIFIABLE` según el RPO declarado.
4. Detecta solapamientos, jobs deshabilitados, rutas que no existen, espacio insuficiente y falta de alertas; no ejecuta el job para “probarlo”.
5. Entrega acciones con responsable, ventana, impacto, prueba posterior y rollback. Un archivo antiguo no prueba que la última ejecución haya sido exitosa.

## Salida y límites

Incluye timestamp UTC, RPO, job, última/ próxima ejecución, estado, artefacto, edad, evidencia redactada y limitaciones. No ejecuta cron, `systemctl start`, scripts de backup, restores, uploads, prune o cambios de retención sin confirmación explícita.
