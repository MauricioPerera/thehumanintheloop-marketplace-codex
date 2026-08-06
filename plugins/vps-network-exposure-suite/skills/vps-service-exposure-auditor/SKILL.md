---
name: vps-service-exposure-auditor
description: Audita la exposición pública de servicios en un VPS por SSH correlacionando listeners, Docker, firewall y reverse proxy sin modificar el host.
---
# VPS Service Exposure Auditor

Audita un VPS autorizado y entrega evidencia reproducible de qué servicios aceptan conexiones públicas y por qué. Confirma primero host, usuario, puerto y huella SSH.

## Procedimiento

1. Ejecuta `ss -lntup` o `ss -ltnp` y clasifica `0.0.0.0`, `[::]` y `127.0.0.1`.
2. Ejecuta `docker ps --format` para identificar mapeos `0.0.0.0:HOST->CONTAINER` y separa puertos publicados de puertos internos.
3. Lee, sin modificar, `nft list ruleset`, `iptables -S` o el firewall disponible. Reporta políticas `INPUT` y `FORWARD` y reglas que permitan el tráfico.
4. Si existe Nginx, Caddy o Traefik, extrae únicamente `listen`, `server_name` y destinos `proxy_pass`/equivalentes; no muestres secretos ni archivos completos.
5. Correlaciona cada listener con: dominio/proxy previsto, publicación Docker directa, regla de firewall y prueba HTTP/TLS acotada.
6. Clasifica `CRITICAL` para bases de datos, APIs administrativas, Ollama, n8n o paneles publicados sin autenticación visible; `HIGH` para servicios HTTP directos; `REVIEW` cuando la intención no pueda determinarse.

## Formato de salida

Incluye timestamp UTC, host, tabla de servicio/puerto/bind/origen/proxy/firewall/evidencia, limitaciones y plan de remediación con impacto y rollback. No pruebes credenciales, no enumeres datos de aplicación, no consultes modelos, no reinicies servicios y no cambies firewall, Docker, DNS o reverse proxy sin confirmación explícita.
