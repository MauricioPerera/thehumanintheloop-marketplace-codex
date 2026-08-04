---
name: vps-dependency-topology-auditor
description: Mapea dependencias y blast radius entre Nginx, systemd, Docker, redes y bases de datos de un VPS sin aplicar cambios.
---
# VPS Dependency Topology Auditor

Construye un mapa de dependencias observable de un VPS autorizado. Confirma host, alcance, dominios y proyectos incluidos antes de inspeccionar.

## Procedimiento

1. Extrae únicamente metadatos de `nginx -T`, `systemctl`, `docker ps`, Compose config, puertos, redes, healthchecks y nombres de servicios.
2. Modela relaciones dominio→proxy, proxy→upstream, servicio→red, servicio→volumen, servicio→dependencia y aplicación→base de datos sin consultar datos de aplicación.
3. Identifica puntos únicos de fallo, dependencias implícitas, ciclos, dependencias sin healthcheck y recursos compartidos entre proyectos.
4. Calcula blast radius por nodo: dominios afectados, servicios downstream, backups o jobs relacionados y evidencia disponible. Marca inferencias como `INFERRED`.
5. Produce grafo textual o Mermaid, matriz de impacto y recomendaciones con prioridad, prueba, rollback y responsable.

## Salida y límites

Incluye timestamp UTC, alcance, fuentes, grafo, supuestos, limitaciones y severidades. Redacta secretos y rutas sensibles; no accede a bases de datos, no ejecuta requests autenticadas, no reinicia servicios ni cambia Docker, Nginx, DNS o firewall.
