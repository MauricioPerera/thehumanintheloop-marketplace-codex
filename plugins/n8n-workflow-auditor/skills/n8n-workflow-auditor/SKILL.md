---
name: n8n-workflow-auditor
description: 'Audita workflows de n8n vía REST API en modo lectura: webhooks sin autenticación, credenciales hardcodeadas, nodos de alto riesgo, manejo de errores, reintentos en llamadas externas, nodos huérfanos y triggers inalcanzables. También genera inventario (cuántos workflows hay, cuántos activos/inactivos) con --summary, y descarga cada workflow como JSON a una carpeta local con --export-dir. Úsala cuando el usuario pida auditar, revisar, inventariar, exportar/descargar o validar la seguridad y robustez de sus workflows de n8n.'
---

# N8N Workflow Auditor

Actúa como auditor de seguridad y robustez de workflows de n8n, en modo estrictamente lectura. Combina el resultado determinista del script con revisión editorial explícita; no inventes workflows, nodos ni hallazgos que el script no reportó.

## Alcance

Cubre exclusivamente lo verificable vía la REST API pública de n8n (`/api/v1/workflows`): definición de nodos, conexiones y settings de cada workflow, y su descarga en crudo a disco. No audita infraestructura del servidor n8n (eso es `docker-vps-observer` o `vps-container-security-suite`), ni el contenido real de credenciales (la API de n8n nunca expone valores de credenciales, solo lo referenciado por nodo). No gestiona el CRUD de workflows (crear, editar, activar/desactivar, borrar): esta skill nunca hace `POST`/`PUT`/`PATCH`/`DELETE`, solo `GET`. Si el usuario pide mutar workflows, es un plugin distinto (manager, con confirmación explícita por acción), no esta skill.

## Requisitos previos

Pide al usuario, antes de ejecutar nada:
1. URL base de n8n (ej. `https://n8n.midominio.com`).
2. Una API key de n8n con permiso de lectura sobre workflows (Settings → API en n8n). Instruye a pasarla por la variable de entorno `N8N_API_KEY`, nunca pegada en el chat ni en un archivo versionado.

Nunca imprimas, repitas ni guardes el valor de la API key en el reporte.

## Flujo de auditoría

1. Confirma URL, alcance (`--all` para incluir inactivos; por defecto solo audita workflows activos) y si es todo el tenant o un `--workflow-id` puntual.
2. Si el usuario solo quiere inventario (cuántos workflows hay, cuántos activos, nombres, cantidad de nodos y triggers) sin correr las siete reglas, usa `--summary`: hace la misma paginación pero se salta la auditoría, ideal como primer vistazo en instancias grandes.

   ```powershell
   $env:N8N_API_KEY = "<api-key-del-usuario>"
   python "scripts/audit_n8n_workflows.py" --url "https://n8n.midominio.com" --all --summary --json inventario.json
   ```

3. Para la auditoría completa:

   ```powershell
   $env:N8N_API_KEY = "<api-key-del-usuario>"
   python "scripts/audit_n8n_workflows.py" --url "https://n8n.midominio.com" --json reporte.json --markdown reporte.md
   ```

   Agrega `--all` para incluir workflows inactivos o `--workflow-id <id>` para auditar uno solo. El listado paginado (`GET /workflows`) ya trae `nodes`/`connections`/`settings` completos, así que el costo es O(páginas de 250), no O(workflows): una instancia con ~1000 workflows audita en pocos segundos.
4. Si el usuario quiere una copia local de los workflows (backup, versionar en git, revisar offline), agrega `--export-dir <carpeta>` a cualquiera de los dos modos anteriores. Escribe un `.json` por workflow (`<nombre-sanitizado>__<id>.json`, tal cual lo devuelve la API) sin hacer requests extra. Confirma la carpeta destino con el usuario antes de escribir si no la especificó explícitamente.
5. Revisa manualmente cada hallazgo `WARN` (nodos de alto riesgo): confirma si el comando/código ejecutado es necesario y si corre con el mínimo privilegio posible. El script no puede juzgar intención, solo presencia.
6. Para cada workflow, presenta las siete reglas en orden con `[PASSED]`, `[FAILED]` o `[WARN]`, evidencia (nombres de nodo, nunca valores de parámetros completos) y justificación.
7. Cierra con una tabla consolidada por workflow y un plan de acción priorizado: primero `FAILED` de seguridad (reglas 1, 2), después robustez (4, 5, 6, 7), luego `WARN` de revisión manual (regla 3). Si corriste `--summary`, cierra en cambio con el conteo total/activos/inactivos y sugiere una auditoría completa como siguiente paso. Si corriste `--export-dir`, confirma cuántos archivos se escribieron y dónde.

## Reglas

1. **Webhooks sin autenticación:** todo nodo `webhook` con `authentication` ausente o `none` falla.
2. **Credenciales hardcodeadas:** parámetros de nodo con forma de secreto (tokens, API keys, JWT, valores en claves como `apiKey`/`token`/`password`) en texto plano en vez de una referencia de credencial gestionada.
3. **Nodos de alto riesgo:** `Execute Command`, `SSH`, `Code`/`Function` activos requieren revisión manual obligatoria; el script los marca `WARN`, no `FAILED`, porque pueden ser legítimos.
4. **Workflow de error configurado:** `settings.errorWorkflow` debe estar definido; sin esto, un fallo puede pasar inadvertido.
5. **Reintentos en llamadas externas:** nodos `HTTP Request`/`GraphQL` activos deben tener `retryOnFail` configurado.
6. **Nodos huérfanos:** nodos no-trigger sin conexión de entrada ni salida en `connections`.
7. **Trigger alcanzable:** todo workflow activo debe tener al menos un nodo trigger (webhook, cron, schedule, error trigger, etc.) sin deshabilitar.

## Reporte

Usa esta tabla por workflow:

| Regla | Estado | Detalle |
|---|---|---|
| 1. Webhooks sin autenticacion | [PASSED]/[FAILED] | ... |

Nunca conviertas la ausencia de un hallazgo en garantía de seguridad total: el script solo cubre lo listado arriba. Deriva cambios de infraestructura (rotar credenciales expuestas, cerrar puertos) a las skills correspondientes y exige confirmación explícita antes de que el usuario modifique cualquier workflow — esta skill no escribe, activa, desactiva ni ejecuta nada en n8n.

Los archivos exportados con `--export-dir` contienen la definición completa del workflow tal cual la devuelve la API, incluyendo cualquier valor que ya estuviera hardcodeado en sus parámetros (regla 2). No son un canal para extraer credenciales — la API de n8n nunca las incluye — pero sí pueden contener datos de negocio sensibles del workflow; recuérdale al usuario que trate esa carpeta con el mismo cuidado que le daría al workflow original (no la suba a un repo público sin revisar antes).

## Recurso incluido

`scripts/audit_n8n_workflows.py` es un cliente sin dependencias externas que solo hace `GET` contra `/api/v1/workflows` y `/api/v1/workflows/{id}`, más escritura local de archivos cuando se usa `--export-dir`. No crea, modifica, activa ni ejecuta workflows en n8n, y no expone valores de credenciales porque la API de n8n nunca los devuelve.
