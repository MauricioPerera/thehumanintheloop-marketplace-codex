---
name: vps-log-retention-auditor
description: Audita retención y crecimiento de logs de un VPS (journald y logging de Docker) en modo lectura sin borrar, truncar, rotar, reiniciar servicios ni cambiar configuración.
---

# VPS Log Retention Auditor

Usa esta skill cuando el usuario quiera revisar la **retención** y el **crecimiento** de los logs de un VPS autorizado, incluyendo `journald` y la configuración de logging de Docker. Confirma host, alcance, baseline de logs y ventana de auditoría antes de inspeccionar. Toda la auditoría es **read-only**: no elimina, trunca, rota, reinicia servicios ni modifica configuración.

## Alcance

Cubre tres actividades, siempre en modo lectura:

1. **journald**: uso de disco del journal, rango de boots, antigüedad y tamaño de los registros presentes, y configuración de retención vigente (`/etc/systemd/journald.conf` y drop-ins).
2. **Crecimiento de archivos de log**: tamaño y edad de `/var/log`, `/var/log/journal`, logs de contenedores en `/var/lib/docker/containers` y otros destinos, con `du`, `df`, `ls`, `stat` y `find` (metadatos, sin editar contenido).
3. **Logging de Docker**: driver de logging del daemon y por contenedor, y políticas de rotación (`max-size`, `max-file`, `max-buffer-size`) leídas de `docker info`, `docker inspect` y `/etc/docker/daemon.json`.

## Reglas de seguridad

- No ejecutes `journalctl --vacuum-size`, `--vacuum-time`, `--vacuum-files`, `--vacuum`, `--rotate`, `--flush` ni `--sync`: mutan el journal.
- No borres ni trunques archivos: sin `rm`, `truncate`, `>`, `>>` sobre logs ni configuración.
- No fuerces rotación: sin `logrotate`, `logrotate -f` ni equivalentes. Leer `/etc/logrotate.d/*` está permitido (es configuración, read-only).
- No reinicies ni recargues servicios: sin `systemctl restart`, `systemctl reload`, `systemctl stop`, `systemctl start`, `systemctl daemon-reload`, `systemctl enable/disable/mask/unmask`. Usa `systemctl status/show/list/cat/is-active/is-enabled` solo para inspeccionar.
- No mutes Docker: sin `docker prune` (system/container/image/volume/network/builder), `docker restart`, `docker exec`, `docker stop`, `docker start`, `docker rm`, `docker kill`, `docker run`, `docker create`, `docker rmi`, `docker image/volume/network rm` ni `docker compose up/down/restart/stop/start/rm/pull/build`.
- No cambies configuración: sin `sed -i`, `tee`, `echo >`, `chmod`, `chown` sobre `/etc/systemd/journald.conf`, `/etc/docker/daemon.json`, `/etc/logrotate.d/*` ni units. Lee con `cat /etc/...`, `grep`, `awk` o `sed -n`.
- No leas credenciales: sin `docker login`, `cat .env`, `cat ~/.docker/config.json`, `/root/.docker/config*`, `/etc/shadow`, `/etc/gshadow`, ni `password=`/`token=`/`api_key=`/`secret=`/`Authorization`/`Bearer`. Reporta la presencia de un archivo de credenciales por su nombre, nunca su contenido.
- Toda evidencia se captura por stdout (SSH) al lado del auditor; no escribes reportes ni rediriges `>`/`>>` a archivos del VPS.

## Flujo

1. Confirma el host/alias SSH, usuario y alcance con el plugin VPS SSH Manager. Verifica qué herramientas existen con `command -v journalctl docker logrotate || true`, `which` o `whereis`; usa solo las presentes, no las instales.
2. **journald**: ejecuta `journalctl --disk-usage`, `journalctl --list-boots --no-pager`, `journalctl --header` y `journalctl --since "<ventana>" --no-pager` para medir volumen, rango y crecimiento. Lee retención vigente con `cat /etc/systemd/journald.conf` (sin comentarios) y `systemctl show systemd-journald -p FragmentPath -p DropInPaths`.
3. **Archivos de log**: ejecuta `df -h` y `df -h /var/log` para espacio libre; `du -sh /var/log /var/log/journal /var/lib/docker/containers` para tamaño por destino; `du -ah /var/log --max-depth=1 | sort -h` y `find /var/log -maxdepth 2 -type f -printf '%s %p\n' | sort -rn | head -20` para identificar los archivos que más crecen. Usa `ls -lh` y `stat` para metadatos, sin abrir contenido.
4. **Docker logging**: ejecuta `docker info --format '{{.LoggingDriver}} {{.DockerRootDir}}'`, `docker system df -v`, `docker ps --format '{{.Names}} {{.Image}}'` y, por contenedor, `docker inspect <c> --format '{{.HostConfig.LogConfig.Type}} {{.HostConfig.LogConfig.Config}}'`. Lee `cat /etc/docker/daemon.json` para la política global de logging/rotación. Usa `docker logs --tail <n> <c>` solo como evidencia de crecimiento, sin seguimiento (`-f`) prolongado.
5. Correlaciona destino→tamaño→edad→política de retención y clasifica `OK`, `GROWING`, `UNBOUNDED` (sin `max-size`/`SystemMaxUse`), `STALE` (log sin rotación prevista) o `NO-POLICY`. Estima proyección de crecimiento con la tasa observada.
6. Entrega acciones con responsable, ventana, impacto, prueba posterior y rollback. Para remediar (ajustar retención, aplicar rotación, reiniciar journald), genera un plan separado y pide confirmación explícita; no apliques cambios desde esta skill.

## Comandos permitidos (ejemplos)

```bash
command -v journalctl docker logrotate || true
which journalctl docker logrotate
journalctl --disk-usage
journalctl --list-boots --no-pager
journalctl --header
journalctl --since "1 hour ago" --no-pager
cat /etc/systemd/journald.conf
grep -v '^[[:space:]]*#' /etc/systemd/journald.conf
systemctl status systemd-journald --no-pager
systemctl show systemd-journald -p FragmentPath -p DropInPaths
cat /etc/docker/daemon.json
docker info --format '{{.LoggingDriver}} {{.DockerRootDir}}'
docker inspect webapp --format '{{.HostConfig.LogConfig.Type}} {{.HostConfig.LogConfig.Config}}'
docker system df -v
docker logs --tail 50 webapp
df -h /var/log
du -sh /var/log /var/log/journal /var/lib/docker/containers
du -ah /var/log --max-depth=1 | sort -h
find /var/log -maxdepth 2 -type f -printf '%s %p\n' | sort -rn | head -20
ls -lh /var/log
stat /var/log/journal
cat /etc/logrotate.d/syslog
```

No ejecutes `journalctl --vacuum*`, `journalctl --rotate/flush/sync`, `rm`, `truncate`, `logrotate`, `systemctl restart/reload/stop/start`, `docker prune`, `docker restart/exec/stop/start/rm`, `sed -i`, `tee` ni redirecciones `>`/`>>` sobre archivos del VPS.

## Salida y límites

Incluye timestamp UTC, destino de log, tamaño, edad, política de retención observada, tasa de crecimiento, estado y limitaciones (ej. `du` no cuenta inodos, `journalctl --disk-usage` es instantánea no acumulada). No borra, trunca, rota, reinicia ni cambia configuración; toda remediación requiere confirmación explícita fuera de esta skill.

## Validación

Ejecuta `python scripts/validate_log_retention_scope.py --command-file <archivo>` cuando se prepare una lista de comandos. Debe terminar con `PASSED`; cualquier `journalctl --vacuum*`, `--rotate/flush/sync`, `rm`, `truncate`, `logrotate`, `systemctl restart/reload/stop/start`, `docker prune`, `docker restart/exec/stop/start/rm`, `sed -i`, `tee`, lectura de credenciales o comando fuera de alcance queda bloqueado.