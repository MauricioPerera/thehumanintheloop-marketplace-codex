---
name: vps-docker-resource-limits-auditor
description: Audita límites CPU, memoria, PIDs, OOM y políticas de reinicio de contenedores Docker en un VPS sin aplicar cambios.
---
# VPS Docker Resource Limits Auditor

Evalúa límites y comportamiento de recursos de contenedores en un VPS autorizado. Confirma host, proyecto y criticidad de servicios antes de inspeccionar.

## Procedimiento

1. Lista contenedores, proyecto, imagen, estado y healthcheck sin imprimir variables de entorno ni comandos sensibles.
2. Inspecciona de forma acotada `NanoCpus`, `CpuQuota`, `CpuPeriod`, `Memory`, `MemorySwap`, `PidsLimit`, `OomKillDisable`, `RestartPolicy`, reservas y límites declarados.
3. Correlaciona límites con uso observado, reinicios, OOM kills, healthchecks fallidos y capacidad disponible; no confunde límite ausente con consumo alto.
4. Marca `HIGH` para servicios públicos o bases de datos sin límite razonable, `REVIEW` para límites incompatibles con el workload y `NO-VERIFIABLE` cuando falte evidencia histórica.
5. Propone valores y ventana de prueba con rollback, sin ejecutar `docker update` ni modificar Compose.

## Salida y límites

Incluye timestamp UTC, contenedor, métrica, valor observado, límite, evidencia, severidad y acción propuesta. No cambia límites, reinicia, pausa, mata, recrea ni modifica cgroups o Compose sin confirmación explícita.
