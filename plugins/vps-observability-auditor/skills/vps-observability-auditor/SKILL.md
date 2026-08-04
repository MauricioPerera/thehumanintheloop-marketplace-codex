---
name: vps-observability-auditor
description: Audita métricas, logs, healthchecks, retención y alertas de un VPS por SSH sin instalar agentes ni modificar servicios.
---
# VPS Observability Auditor

Audita un VPS autorizado y determina si existe observabilidad operativa, no solo un dashboard accesible. Confirma host, usuario, puerto y huella SSH antes de conectar.

## Procedimiento

1. Inventaría contenedores y servicios relacionados con Prometheus, Grafana, Loki, Promtail, Alertmanager, exporters, Telegraf, Vector y healthchecks.
2. Revisa `systemctl`, `docker ps`, `docker inspect` limitado a health/status y `ss` para localizar endpoints de métricas sin extraer datos de aplicación.
3. Comprueba de forma acotada `journalctl --disk-usage`, rotación de logs, errores recientes y estado de healthchecks; limita volumen y redacta rutas o valores sensibles.
4. Busca configuración declarativa de scraping, retención y alertas solo mediante nombres, rutas y claves estructurales; nunca muestra tokens, contraseñas ni URLs con credenciales.
5. Correlaciona cada servicio con señal producida, retención, dashboard, alerta y responsable. Un `server_name` de Grafana no prueba que haya métricas recolectadas.

## Salida y límites

Entrega timestamp UTC, matriz de cobertura, evidencia, huecos, impacto y plan de implementación con coste, rollback y ventana. No instala agentes, reinicia servicios, crea dashboards, cambia retención, consulta bases de datos ni envía alertas de prueba sin autorización explícita.
