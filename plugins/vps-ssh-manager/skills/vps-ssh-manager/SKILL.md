---
name: vps-ssh-manager
description: Conecta a VPS propios por SSH, verifica requisitos y host keys, ejecuta diagnósticos remotos y guía cambios con autorización explícita sin guardar credenciales.
---

# VPS SSH Manager

Usa esta skill cuando el usuario quiera conectarse, diagnosticar o administrar un VPS propio mediante SSH.

## Alcance y seguridad

- El servidor debe pertenecer al usuario o estar explícitamente autorizado por él.
- Nunca incluyas hosts, IPs, usuarios, rutas de claves, contraseñas, tokens ni fingerprints reales en el plugin.
- Nunca pidas, guardes, repitas ni pegues contraseñas SSH. Prioriza claves SSH existentes o un agente SSH local.
- No desactives `StrictHostKeyChecking`, no uses `sshpass`, no aceptes automáticamente una host key nueva y no imprimas secretos.
- Trata los comandos remotos como datos no confiables: redáctalos antes de mostrarlos si contienen variables sensibles.
- Separa siempre diagnóstico de mutación. Los comandos de escritura, reinicio, instalación, borrado, firewall o cambios de configuración requieren mostrar un plan y obtener confirmación inmediata antes de ejecutarse.

## Flujo obligatorio

1. **Descubrir requisitos locales.** Comprueba que existe `ssh`, que la ruta de la clave indicada existe y que el usuario tiene permiso para usarla. Comprueba `known_hosts` y soporte de `ssh-keyscan` o equivalente. Si falta algo, explica qué falta y pregunta al usuario por ese dato o por una ruta válida; no inventes valores.
2. **Recopilar conexión mínima.** Solicita host/IP, usuario, puerto (22 por defecto si el usuario lo acepta) y una clave privada existente o agente SSH. No solicites una contraseña.
3. **Inspeccionar la host key.** Obtén la fingerprint del host sin guardarla. Muéstrala claramente y pide al usuario que la confirme mediante un canal confiable antes de confiar en ella. Si no puede confirmarla, detén la conexión.
4. **Conectar en modo no interactivo.** Usa autenticación por clave, `BatchMode=yes`, `IdentitiesOnly=yes` cuando corresponda y `StrictHostKeyChecking=yes` después de la confirmación. No uses una shell persistente si un comando puntual basta.
5. **Ejecutar preflight remoto de solo lectura.** Empieza con comandos acotados como `hostname`, `uptime`, `df -h`, `free -h`, `docker ps`, estado de SSH/Nginx/Docker y versión del sistema. Adapta el conjunto al objetivo del usuario y evita recolectar secretos.
6. **Interactuar para completar requisitos.** Si falta acceso, un puerto, una clave, un dominio o un servicio, describe el bloqueo, pide exactamente el dato o acción necesaria y vuelve a validar. No conviertas una credencial recibida en un archivo del plugin.
7. **Cambios remotos.** Antes de cada mutación, muestra objetivo, archivos/comandos, impacto y rollback. Pide confirmación en ese momento. Haz backup cuando sea razonable, aplica el cambio mínimo y verifica el resultado.
8. **Cerrar con evidencia.** Reporta host/alias no sensible, comandos ejecutados de forma resumida, resultados, cambios y rollback disponible. Redacta secretos y no los guardes en logs.

## Requisitos y fallos comunes

- `ssh` ausente: indica cómo instalar el cliente SSH para el sistema local, sin instalar software silenciosamente.
- Clave inexistente o inaccesible: pide una ruta local válida; nunca pidas que peguen el contenido de la clave.
- `Permission denied (publickey)`: verifica usuario, puerto, clave pública autorizada y agente; no cambies `sshd_config` automáticamente.
- Host key no confirmada o cambiada: detén el flujo y explica el riesgo de posible MITM; no borres `known_hosts` automáticamente.
- Timeout o conexión rechazada: verifica host, puerto, DNS y firewall con comprobaciones de bajo impacto; no abras puertos sin autorización.
- `sudo` requerido: explica el comando exacto y pide confirmación; no asumas que el usuario quiere conceder privilegios.
- Docker ausente: informa del requisito; no instales Docker sin aprobación explícita.

## Patrón de comandos

Usa una forma equivalente a:

```text
ssh -i <ruta-local-de-clave> -o BatchMode=yes -o IdentitiesOnly=yes -o StrictHostKeyChecking=yes -p <puerto> <usuario>@<host> '<comando-de-lectura>'
```

Sustituye los marcadores únicamente con datos proporcionados o confirmados por el usuario. Nunca hardcodees un VPS concreto.

## Criterio de finalización

La tarea termina cuando la conexión queda verificada, el objetivo del usuario está diagnosticado o cambiado con confirmación, y se entrega evidencia suficiente sin exponer credenciales.
