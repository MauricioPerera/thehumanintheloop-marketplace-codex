---
name: ephemeral-agent-delegator
description: 'Delega tareas de implementación a agentes efímeros por terminal (Ollama con `ollama launch claude`, o `pool exec` de poolside.ai), con la mecánica de lanzamiento headless sin colgarse, verificación independiente del resultado, y manejo de fallos transitorios/cuota. No sabe de la tarea en sí ni de contratos: solo de cómo lanzar y verificar. Úsala cuando el usuario pida delegar una implementación a un modelo/agente efímero por CLI, o mencione Ollama, pool/poolside, o "agente efímero".'
---

# Ephemeral Agent Delegator

Mecánica pura de lanzamiento y verificación para dos backends de agentes efímeros por terminal. Esta skill **no sabe qué tarea estás delegando** ni de contratos/tests — eso lo definís vos (o una skill de orquestación como un flujo PM/CCDD). Tu rol acá es: escribir el prompt/contrato, delegar, y **verificar el resultado vos mismo, nunca confiar en el resumen o el exit code del agente efímero**.

## Los dos backends

| | Ollama (`ollama launch claude`) | pool (`pool exec`, poolside.ai) |
|---|---|---|
| Requiere | `ollama signin` + acceso a modelos cloud | CLI `pool` instalado + cuenta poolside.ai |
| Riesgo principal | Lanzamiento sale vacío sin `< /dev/null`; hereda flota MCP global sin `--strict-mcp-config` | Nada se cuelga esperando aprobación — el costo real es el tiempo de razonamiento ANTES de la acción rechazada |
| Sonda de vida barata | Sí (`probe --backend ollama`) | No — no hay forma barata de "probar primero"; lanzá directo en un dir descartable |
| Concurrencia | ~3 modelos cloud simultáneos (cap de cuenta) | Sin límite documentado, pero colisión de archivos exige secuencial |
| Fallos conocidos | "Could not verify your plan" transitorio (relanzar); degradación por cuota a respuestas vacías o "LISTO" falso | Exit 4 = fallo explícito; heredocs POSIX fallan en Windows (reintenta solo, no bloqueante) |
| Logs/auditoría | Log del `-p` (se escribe al final); transcript en `~/.claude/projects/<cwd>/*.jsonl` | `pool config` imprime rutas reales: `%LOCALAPPDATA%\poolside\logs\pool-<run_id>.log` y `...\trajectories\trajectory-standalone_<run_id>.ndjson` |

Elegí el backend según qué tenga configurado el usuario — no asumas cuál. Si no sabés, preguntá.

## Filosofía compartida (no negociable)

El agente efímero es un implementador, no un par de confianza:
1. Vos redactás la tarea (contrato, tests, o instrucción clara con criterio de éxito verificable).
2. Delegás la implementación.
3. **Verificás el resultado vos mismo** — corriendo los tests/comandos reales, no leyendo el resumen que imprimió el agente efímero. Un "LISTO" o un exit 0 no son evidencia; el archivo/test/diff en disco sí.
4. Si el repo tiene un gate de verificación determinista (ej. CCDD), no le des esas tools al implementador — el veredicto lo corrés vos, aparte, con el gate en modo lectura sobre el resultado.

## Uso del script

`scripts/build_delegation_command.py` arma el comando exacto — **nunca lo ejecuta**. Vos corrés el comando resultante con tu propia tool de Bash, `run_in_background: true`, como su propio task. Nunca lo encadenes con `&` detrás de otro comando (queda huérfano, jamás llega la notificación de fin) y nunca dejes que este script u otro wrapper lo lance en background por vos.

```powershell
# Sonda de vida (antes de una delegación real, solo Ollama tiene una barata)
python scripts/build_delegation_command.py probe --backend ollama --model glm-5.2:cloud

# Armar el lanzamiento real
python scripts/build_delegation_command.py build --backend ollama --dir <repo> \
  --prompt-file prompt.txt --prompt-text "<instrucción completa>" \
  --model glm-5.2:cloud --log delegation.log

# Modo /goal (Ollama): el agente sigue trabajando hasta cumplir una condición verificable,
# con reintentos automáticos dentro de la misma invocación
python scripts/build_delegation_command.py build --backend ollama --dir <repo> \
  --goal "Los tests de test_x.py pasan en verde. Parar tras 6 turnos si no se cumple." \
  --model glm-5.2:cloud --log delegation.log

# pool
python scripts/build_delegation_command.py build --backend pool --dir <repo> \
  --prompt-file prompt.txt --prompt-text "<instrucción completa>" --log delegation.log
```

El script imprime el comando y los recordatorios de por qué cada flag es obligatoria — leelos, no los saltees. Para Ollama con gate CCDD, pasá `--mcp-config-file` con un JSON que tenga **solo** la entrada del servidor MCP del gate (copiada de la config real del usuario) — el script no la inventa ni asume una.

## Reglas anti-cuelgue (aplican a ambos backends salvo que se aclare)

- **Ningún proceso en foreground que no termine solo.** Un server bloqueante cuelga el lanzamiento para siempre. Instruí explícito en el prompt: todo proceso de servidor va en background y se mata al final.
- **Un lanzamiento = un background task tuyo**, nunca `&` encadenado tras otro comando.
- **CLIs que funcionan headless**: `claude` vía `ollama launch claude`, y `pool exec`. `agy` (Antigravity) y `codex` se cuelgan en no-interactivo (esperan TTY) — no los uses para esto.
- **En Windows, lanzá desde Bash (Git Bash), nunca PowerShell**: `< /dev/null` (obligatorio para Ollama) no tiene equivalente directo en PowerShell y el comando falla al instante con un error de parseo.
- **Log vacío no significa colgado**: en modo `-p`/headless el log se escribe recién al final. Para saber si sigue vivo, mirá el `mtime` de los entregables esperados en disco (o del trajectory de pool), no el log.
- **Un tope de turnos (modo `/goal`) no protege un loop DENTRO de un turno**: si el agente queda reintentando una tool sin parar, el evaluador nunca corre porque el turno nunca termina, y el timeout del task tampoco lo mata. Único guardián real: monitorear si el transcript/trajectory crece sin avanzar, y matar el proceso vos.

## Verificación independiente (obligatoria, sin atajos)

1. Si hay tests/contrato congelados: hasheá el archivo de tests ANTES de delegar, compará después — debe ser idéntico (el implementador no debería tocarlo).
2. Corré el comando de test/verificación vos mismo. No leas el resumen del agente efímero como si fuera el resultado.
3. Si hay un gate determinista en el repo, corrélo vos, aparte, sobre el resultado final.
4. Confirmá que el agente efímero no tocó nada fuera del alcance declarado (diff o listado del directorio).
5. Ante una muerte del host/proceso a mitad de tarea: auditá disco primero (`git status`, entregables esperados, transcript/log con su `mtime`) antes de asumir que se perdió el trabajo o de relanzar — los lanzamientos son efímeros e idempotentes sobre la misma especificación, relanzar de más solo gasta cuota.

## Reporte

Después de delegar, contale al usuario: qué backend, qué comando se lanzó (sin exponer secretos si el prompt los tuviera), y el resultado de tu verificación independiente — nunca el resumen del agente efímero tal cual, sin haberlo comprobado vos.

## Recurso incluido

`scripts/build_delegation_command.py` es un generador de comandos sin dependencias externas ni ejecución de subprocesos — su única salida es texto (el comando a correr) y, opcionalmente, el archivo de prompt si se lo pediste con `--prompt-text`. Probado: `probe` y `build` para ambos backends, modo `--goal`, `--mcp-config-file` válido e inválido (error claro, sin traceback), y el caso de `--prompt-file` inexistente sin `--prompt-text` (falla claro, salvo en modo `--goal` donde no hace falta — bug real encontrado y corregido durante las pruebas).
