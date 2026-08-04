---
name: vps-tls-renewal-monitor
description: Audita expiración, jobs Certbot y coherencia de certificados TLS servidos por un VPS sin renovarlos ni recargar proxies.
---
# VPS TLS Renewal Monitor

Audita la salud operativa de renovaciones TLS en un VPS autorizado. Confirma host, dominios, zona horaria y umbrales de expiración antes de inspeccionar.

## Procedimiento

1. Inventaría certificados y dominios mediante nombres, fechas, SAN y fingerprints redactados; no muestra claves privadas ni tokens ACME.
2. Revisa `certbot.timer`, cron o unidad equivalente: habilitación, última ejecución, próxima ejecución, exit status y errores acotados.
3. Compara fecha de expiración, próxima ventana esperada, certificado servido por SNI y configuración del reverse proxy; clasifica `CURRENT`, `DUE`, `FAILED`, `MISMATCH` o `NO-VERIFIABLE`.
4. Marca riesgo cuando el certificado servido difiera del archivo esperado, falte un dominio SAN, el job esté deshabilitado o la expiración quede bajo el umbral acordado.
5. Propone diagnóstico y remediación con dominio exacto, ventana, backup, prueba posterior y rollback. No trata una conexión TLS exitosa como prueba de renovación automática.

## Salida y límites

Incluye timestamp UTC, dominio, expiración, job, última/ próxima ejecución, estado, evidencia redactada y limitaciones. No ejecuta `certbot renew`, `certbot certonly`, ACME issuance, reload de Nginx, cambios DNS ni modificaciones de certificados sin confirmación explícita.
