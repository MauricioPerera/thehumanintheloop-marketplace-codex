---
name: vps-configuration-drift-auditor
description: Detecta drift entre configuración declarada y estado activo de Docker, systemd y Nginx en un VPS sin aplicar cambios.
---
# VPS Configuration Drift Auditor

Compara la intención documentada con el estado observado de un VPS autorizado. Confirma host, usuario, alcance, baseline y fecha de referencia antes de auditar.

## Procedimiento

1. Identifica archivos Compose, unidades systemd, sitios Nginx, jobs cron, imágenes, puertos, redes y servicios habilitados sin mostrar sus contenidos completos.
2. Calcula metadatos y hashes de archivos autorizados; excluye `.env`, claves, certificados privados, tokens y valores secretos del reporte.
3. Compara configuración declarada con `docker ps`, `docker inspect` limitado, `systemctl`, `ss` y `nginx -T` acotado a nombres, destinos y listeners.
4. Clasifica diferencias como `EXPECTED`, `UN-DOCUMENTED`, `STALE`, `CONFLICT` o `NO-VERIFIABLE`, indicando baseline, evidencia y fecha.
5. Separa drift funcional —imagen, puerto, volumen, proxy, unidad o job— de drift cosmético. No normalices archivos ni actualices servicios durante la auditoría.

## Salida y límites

Incluye timestamp UTC, baseline, tabla de diferencias, riesgo, impacto, evidencia redactada y plan de reconciliación con rollback. No imprime secretos, no cambia archivos, no reinicia servicios y no ejecuta `compose up`, `systemctl daemon-reload`, reload de Nginx o despliegues sin confirmación explícita.
