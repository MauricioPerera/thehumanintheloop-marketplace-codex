---
name: supabase-selfhosted-observer
description: Inspecciona una instancia Supabase self-hosted por SSH mediante Docker, servicios, salud, versiones y recursos sin exponer secretos ni mutar el VPS.
---

# Supabase Self-hosted Observer

Usa esta skill cuando el usuario quiera saber si una instancia Supabase self-hosted está activa, qué servicios contiene o qué componente presenta problemas.

## Flujo

1. Verifica el alias SSH, usuario, cliente `ssh`, clave y `known_hosts` mediante el plugin VPS SSH Manager.
2. Ejecuta solo lecturas: `docker ps`, `docker compose ps`, estado de contenedores, imágenes, healthchecks, uptime y uso de disco/memoria.
3. Identifica componentes por nombre o imagen: Postgres, GoTrue/Auth, PostgREST, Realtime, Storage, Studio, Kong, Supavisor, Edge Runtime e Imgproxy.
4. Resume estado, versión de imagen, edad del contenedor y anomalías. No muestres environment, labels con secretos, volúmenes privados ni logs completos.
5. Si un contenedor está unhealthy, reiniciando o ausente, propone el siguiente diagnóstico de solo lectura antes de sugerir una mutación.

## Comandos permitidos

```text
docker ps --format '{{.Names}}\t{{.Image}}\t{{.Status}}'
docker compose ps
docker inspect --format '{{.Name}} {{.State.Status}} {{.State.Health.Status}}' <contenedor>
docker stats --no-stream --format '{{.Name}}\t{{.CPUPerc}}\t{{.MemUsage}}'
df -h
free -h
uptime
```

No ejecutes `docker exec` contra PostgreSQL, no leas `.env`, no uses `docker inspect` sin un formato que excluya configuración sensible y no reinicies servicios desde esta skill.

## Validación

Ejecuta `python scripts/validate_observer_scope.py --command-file <archivo>` cuando se prepare una lista de comandos. Debe terminar con `PASSED`; cualquier comando fuera de la allowlist queda bloqueado.
