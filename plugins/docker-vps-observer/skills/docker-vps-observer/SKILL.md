---
name: docker-vps-observer
description: Observa Docker en un VPS remoto por SSH con comandos de solo lectura, healthchecks, recursos y exposición. Úsala para inventario o diagnóstico inicial.
---

# Docker VPS Observer

Actúa como observador remoto de Docker. Usa SSH nativo y la configuración de conexión que el usuario proporcione; nunca dependas de LazySSH ni inventes hosts, claves o puertos.

## Flujo

1. Confirma host, usuario, puerto y huella conocida antes de conectar.
2. Ejecuta únicamente preflight de lectura: `docker version`, `docker info`, `docker ps`, `docker stats --no-stream`, `docker system df` y healthchecks.
3. Identifica contenedores unhealthy, reinicios, puertos publicados, daemon detenido y presión de disco.
4. Devuelve comandos ejecutados, evidencia, severidad, límites y siguiente acción. No expongas variables de entorno, tokens, claves ni contenido de volúmenes.

No reinicies, elimines, actualices ni hagas prune. Deriva acciones a `docker-service-manager` o `docker-image-manager` y exige confirmación explícita.
