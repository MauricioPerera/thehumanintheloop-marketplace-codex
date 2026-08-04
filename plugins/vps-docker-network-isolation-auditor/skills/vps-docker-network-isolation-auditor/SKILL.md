---
name: vps-docker-network-isolation-auditor
description: Audita segmentación, redes compartidas, aliases y exposición de contenedores Docker en un VPS sin aplicar cambios.
---
# VPS Docker Network Isolation Auditor

Audita la conectividad declarada y efectiva de contenedores en un VPS autorizado. Confirma host, proyectos, redes en alcance y baseline antes de inspeccionar.

## Procedimiento

1. Lista redes, drivers, subnets, gateways, endpoints y labels de proyecto sin mostrar variables ni nombres sensibles innecesarios.
2. Correlaciona cada contenedor con sus redes, aliases, `NetworkMode`, puertos publicados y proyecto Compose; trata `host`, `none` y `container:` como casos especiales.
3. Marca `CRITICAL` cuando una red de datos, administración o backend esté compartida con un servicio público no justificado; marca `HIGH` para `host` networking o aliases cruzados entre proyectos.
4. Distingue exposición host→contenedor de conectividad contenedor→contenedor; no asume que una red bridge aislada está protegida si existen puertos publicados o rutas proxy.
5. Entrega un grafo textual de proyectos y redes, controles faltantes, justificación conocida y plan de segmentación con rollback. No prueba credenciales ni enumera datos de aplicación.

## Salida y límites

Incluye timestamp UTC, red, contenedor, proyecto, exposición, evidencia redactada, severidad y remediación propuesta. No conecta shells entre contenedores, no crea/elimina redes, no desconecta endpoints y no reinicia servicios sin autorización explícita.
