---
name: vps-container-security-auditor
description: Audita aislamiento, privilegios, capabilities, mounts y superficies de ataque de contenedores Docker en un VPS sin aplicar cambios.
---
# VPS Container Security Auditor

Audita contenedores de un VPS autorizado y clasifica riesgos de aislamiento sin alterar el runtime. Confirma host, usuario, alcance y ventana antes de inspeccionar.

## Procedimiento

1. Lista contenedores activos y sus imágenes, sin imprimir variables de entorno, labels sensibles ni comandos completos.
2. Usa `docker inspect` con campos acotados para revisar `Privileged`, `User`, `CapAdd`, `CapDrop`, `SecurityOpt`, `ReadonlyRootfs`, `NetworkMode`, `PidMode`, `IpcMode`, `Devices` y mounts.
3. Marca como `CRITICAL` Docker socket, `--privileged`, `host` network/PID/IPC, montajes de `/`, `/etc`, `/var/run` o dispositivos sin justificación documentada.
4. Marca como `HIGH` ejecución como root, capabilities excesivas, filesystem escribible, imagen sin digest, exposición pública innecesaria y ausencia de healthcheck.
5. Correlaciona cada excepción con el servicio y su justificación; no propone quitar un permiso crítico sin impacto, rollback y prueba de compatibilidad.

## Salida y límites

Incluye timestamp UTC, contenedor, control, evidencia redactada, severidad, justificación conocida y remediación propuesta. No reinicia, recrea, mata, actualiza, escanea credenciales ni cambia Compose, AppArmor, seccomp, firewall o volúmenes sin confirmación explícita.
