---
name: n8n-workflow-auditor
description: 'Audita workflows de n8n vía REST API en modo lectura: webhooks sin autenticación, credenciales hardcodeadas, nodos de alto riesgo, manejo de errores, reintentos en llamadas externas, nodos huérfanos y triggers inalcanzables. También genera inventario (cuántos workflows hay, cuántos activos/inactivos) con --summary, descarga cada workflow como JSON a una carpeta local con --export-dir, envuelve el audit nativo de n8n con --native-audit, analiza el historial real de ejecuciones (tasa de error, últimos fallos por workflow) con --executions, e inventaría credenciales (tipo, proyecto, con quién están compartidas, nunca valores) con --credentials. Úsala cuando el usuario pida auditar, revisar, inventariar, exportar/descargar, ver qué workflows están fallando o validar la seguridad y robustez de sus workflows de n8n.'
---

# N8N Workflow Auditor

Actúa como auditor de seguridad y robustez de workflows de n8n, en modo estrictamente lectura. Combina el resultado determinista del script con revisión editorial explícita; no inventes workflows, nodos ni hallazgos que el script no reportó.

## Alcance

Cubre exclusivamente lo verificable vía la REST API pública de n8n (`/api/v1/workflows`, `/api/v1/audit`, `/api/v1/executions`, `/api/v1/credentials`): definición de nodos, conexiones y settings de cada workflow, su descarga en crudo a disco, el reporte de riesgo nativo que n8n ya calcula server-side, el historial real de ejecuciones (no solo si hay `errorWorkflow` configurado, sino si el workflow efectivamente falla), y el inventario de credenciales (metadata: nombre, tipo, con qué proyecto está compartida y con qué rol). No audita infraestructura del servidor n8n (eso es `docker-vps-observer` o `vps-container-security-suite`), ni el contenido real de credenciales (la API de n8n nunca expone valores de credenciales, solo lo referenciado por nodo, ni siquiera en `/credentials`, que explícitamente excluye los secretos). No gestiona el CRUD de workflows (crear, editar, activar/desactivar, borrar): la única llamada no-`GET` que hace esta skill es `POST /api/v1/audit`, que es un generador de reporte de solo lectura (no crea, modifica ni borra nada) — nunca hace `PUT`/`PATCH`/`DELETE`, ni un `POST` que mute algo. Si el usuario pide mutar workflows, es un plugin distinto (manager, con confirmación explícita por acción), no esta skill.

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
5. Si el usuario quiere el audit nativo de n8n (credenciales sin usar, nodos riesgosos u oficiales-inseguros, webhooks sin proteger, instancia desactualizada), usa `--native-audit`: es un modo aparte, no recorre workflows, solo pide `POST /api/v1/audit` y devuelve el reporte de n8n tal cual. Requiere que la API key tenga el scope `securityAudit:generate`; si no lo tiene, n8n devuelve 403 y el script corta con el detalle del error.

   ```powershell
   $env:N8N_API_KEY = "<api-key-del-usuario>"
   python "scripts/audit_n8n_workflows.py" --url "https://n8n.midominio.com" --native-audit --json audit-nativo.json --markdown audit-nativo.md
   ```

   Filtra con `--audit-categories credentials,nodes,instance,database,filesystem` (subset de las cinco) o `--days-abandoned N` para ajustar cuándo un workflow cuenta como abandonado. Este reporte es a nivel instancia, no por workflow: complementa las siete reglas (que son por workflow), no las reemplaza.
6. Si el usuario quiere saber qué workflows están fallando de verdad (no solo si tienen `errorWorkflow` configurado, sino si realmente erroran), usa `--executions`: pagina `/api/v1/executions` y agrega por workflow total/OK/error/tasa de error/último status/último error.

   ```powershell
   $env:N8N_API_KEY = "<api-key-del-usuario>"
   python "scripts/audit_n8n_workflows.py" --url "https://n8n.midominio.com" --executions --status error --json ejecuciones.json --markdown ejecuciones.md
   ```

   `/api/v1/executions` **no tiene filtro de fecha**, solo `status`, `workflowId` y paginación por cursor — y una instancia real puede tener millones de ejecuciones históricas. Por eso el script trae como máximo `--max-executions` (default 500, subible) y **nunca** hace un crawl completo por defecto; si corta antes de agotar el cursor, marca `truncated: true` y el markdown lo dice explícito — nunca lo omitas al reportar. Usa `--status error` para ver solo fallos recientes (el caso de uso más común) o `--workflow-id <id>` para ver el historial de uno solo.
7. Si el usuario quiere inventariar credenciales (cuántas hay, de qué tipo, con qué proyecto están compartidas y con qué rol), usa `--credentials`: pagina `/api/v1/credentials`, que por diseño de n8n nunca devuelve el valor de la credencial, solo metadata. Requiere que la API key pertenezca al owner/admin de la instancia (`credential:list` scope); si no, 403.

   ```powershell
   $env:N8N_API_KEY = "<api-key-del-usuario>"
   python "scripts/audit_n8n_workflows.py" --url "https://n8n.midominio.com" --credentials --json credenciales.json --markdown credenciales.md
   ```

   No dupliques lo que ya hace `--native-audit` (que ya distingue credenciales sin usar/sin usar en activos/sin ejecutar recientemente): `--credentials` es un inventario plano, no un detector de riesgo.
8. Revisa manualmente cada hallazgo `WARN` (nodos de alto riesgo): confirma si el comando/código ejecutado es necesario y si corre con el mínimo privilegio posible. El script no puede juzgar intención, solo presencia.
9. Para cada workflow, presenta las siete reglas en orden con `[PASSED]`, `[FAILED]` o `[WARN]`, evidencia (nombres de nodo, nunca valores de parámetros completos) y justificación.
10. Cierra con una tabla consolidada por workflow y un plan de acción priorizado: primero `FAILED` de seguridad (reglas 1, 2), después robustez (4, 5, 6, 7), luego `WARN` de revisión manual (regla 3). Si corriste `--summary`, cierra en cambio con el conteo total/activos/inactivos y sugiere una auditoría completa como siguiente paso. Si corriste `--export-dir`, confirma cuántos archivos se escribieron y dónde. Si corriste `--native-audit`, presenta cada risk report (Credentials/Nodes/Instance/Database/Filesystem) con sus secciones, cantidad de hallazgos y recomendación, priorizando por cantidad de ubicaciones afectadas. Si corriste `--executions`, ordena por tasa de error y aclara siempre si la muestra fue truncada. Si corriste `--credentials`, agrupa por tipo y señala credenciales sin compartir con ningún proyecto además del propietario, si corresponde.

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

`scripts/audit_n8n_workflows.py` es un cliente sin dependencias externas. Hace `GET` contra `/api/v1/workflows`, `/api/v1/workflows/{id}`, `/api/v1/executions` y `/api/v1/credentials`, `POST /api/v1/audit` (generador de reporte de solo lectura, no muta nada), y escritura local de archivos cuando se usa `--export-dir`. No crea, modifica, activa, desactiva ni ejecuta workflows en n8n, no borra ni reintenta ejecuciones, no crea ni edita credenciales, y no expone valores de credenciales porque la API de n8n nunca los devuelve.
