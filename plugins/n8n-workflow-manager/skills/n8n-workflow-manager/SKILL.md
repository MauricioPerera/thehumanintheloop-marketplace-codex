---
name: n8n-workflow-manager
description: 'Gestiona el ciclo de vida de workflows de n8n vía REST API: crear, activar, desactivar, archivar/desarchivar, transferir, editar (con diff obligatorio) y borrar (con confirmación por nombre exacto). Todo en modo dry-run por defecto, sin mutar hasta que el usuario confirme el plan exacto. Úsala cuando el usuario pida crear, activar, desactivar, archivar, transferir, editar, actualizar o borrar un workflow de n8n.'
---

# N8N Workflow Manager

Administra workflows de n8n sin ejecutar ninguna mutación hasta que el usuario confirme el plan exacto en el chat. Mismo principio que `docker-service-manager`: capturar estado previo, mostrar el plan/diff, confirmar, recién ahí mutar, verificar resultado.

## Alcance

Cubre `create`, `activate`, `deactivate`, `archive`, `unarchive`, `transfer`, `update` y `delete` sobre `/api/v1/workflows` de la REST API pública de n8n. Para auditar o inventariar sin mutar nada, usa `n8n-workflow-auditor`, no esta skill.

## Requisitos previos

Pide al usuario, antes de ejecutar nada:
1. URL base de n8n.
2. Una API key con permisos de escritura sobre workflows (`workflow:create`, `workflow:update`, `workflow:delete`, `workflow:activate`, `workflow:deactivate`). Instruye a pasarla por `N8N_API_KEY`, nunca pegada en el chat ni versionada.

Nunca imprimas, repitas ni guardes el valor de la API key.

## Mecanismo de seguridad (no es opcional, está en el script)

- **Dry-run por defecto**: ningún subcomando muta nada salvo que se pase `--apply`. Sin `--apply`, el script solo imprime el plan (o el diff, en `update`) y termina.
- **`update` nunca acepta un JSON parcial directo**: `PUT /workflows/{id}` en n8n es reemplazo completo, no parche — mandar un objeto incompleto puede borrar nodos/conexiones que no se querían tocar. El script siempre hace `GET` del estado actual, mergea el patch encima, y muestra el diff completo antes de aplicar.
- **`delete` exige `--confirm-name`** con el nombre EXACTO del workflow, verificado contra el nombre real que devuelve la API (no lo que el usuario cree que es el nombre). Si no coincide, falla sin borrar nada.
- Como agente, **nunca corras un comando con `--apply` sin que el usuario haya visto el plan/diff y dicho que sí explícitamente**, aunque el script ya tenga sus propias barreras. Doble capa: el script protege contra errores mecánicos, vos protegés contra hacer algo que el usuario no pidió.

## Flujo por operación

### Crear (`create`)

El usuario (o vos, en su nombre) describe el workflow. Construís el JSON completo (`name`, `nodes`, `connections`, `settings` son obligatorios) y lo escribís a un archivo. Para armar `nodes`/`connections` válidos, lo más confiable es partir de un workflow real exportado con `n8n-workflow-auditor --export-dir` y adaptarlo, en vez de inventar la estructura de nodos desde cero.

```powershell
$env:N8N_API_KEY = "<api-key-del-usuario>"
python "scripts/manage_n8n_workflows.py" create --url "https://n8n.midominio.com" --file nuevo-workflow.json
python "scripts/manage_n8n_workflows.py" create --url "https://n8n.midominio.com" --file nuevo-workflow.json --apply
```

Solo estos campos son válidos en el archivo: `name`, `nodes`, `connections`, `settings`, `staticData`, `pinData`, `nodeGroups`, `projectId`. Cualquier otro (id, active, createdAt, etc.) se ignora — son de solo lectura.

### Activar / desactivar (`activate` / `deactivate`)

```powershell
python "scripts/manage_n8n_workflows.py" activate --url "https://n8n.midominio.com" --workflow-id <id> --apply
```

n8n exige al menos un trigger automático (webhook, cron/schedule, polling) para poder activar — un workflow que solo tiene un Manual Trigger no se puede activar vía API, y el error de n8n lo dice explícito. Es idempotente: si ya está en el estado pedido, el script lo dice y no llama a la API.

### Archivar / desarchivar (`archive` / `unarchive`)

```powershell
python "scripts/manage_n8n_workflows.py" archive --url "https://n8n.midominio.com" --workflow-id <id> --apply
```

Soft-delete idempotente: archivar saca el workflow de la vista activa pero se puede restaurar con `unarchive`, a diferencia de `delete`. Mismo patrón que `activate`/`deactivate`: si ya está en el estado pedido, no llama a la API.

### Transferir a otro proyecto (`transfer`)

```powershell
python "scripts/manage_n8n_workflows.py" transfer --url "https://n8n.midominio.com" --workflow-id <id> --destination-project-id <id> --apply
```

**Requiere que la instancia tenga proyectos de equipo habilitados.** Confirmado vía el MCP oficial de n8n (`search_projects` devuelve `teamProjectsEnabled: false` con un hint explícito cuando no lo están): no es un tema de permisos de tu API key, es un flag a nivel instancia. Con `teamProjectsEnabled: false` solo existe el proyecto personal — no hay a dónde transferir, y ni siquiera se puede crear un segundo proyecto (`POST /projects` también queda bloqueado). Si el usuario no sabe el `--destination-project-id`, no lo inventes: si tenés acceso al MCP builder (`n8n-workflow-builder`), llamá `search_projects` para confirmar si hay más de un proyecto antes de intentarlo; si no, pedile que lo consiga desde la UI de n8n (Settings → Projects).

### Editar (`update`)

**Si el usuario tiene token del MCP oficial de n8n (`N8N_MCP_TOKEN`), preferí `n8n-workflow-builder` para editar workflows en vez de este comando.** Su `update_workflow` aplica operaciones atómicas por nodo (`addNode`, `updateNodeParameters`, `renameNode`, etc.); este `update` de acá sigue mergeando a nivel de campo top-level porque el `PUT` de la REST API es reemplazo completo — funciona, pero es más rudimentario. Usá este comando cuando el usuario solo tenga la API key REST, no el token MCP.

Escribí un archivo JSON con **solo los campos que cambian** (nunca el objeto completo). Campos editables: `name`, `description`, `nodes`, `connections`, `nodeGroups`, `settings`, `staticData`, `pinData`. Si el patch toca `nodes` o `connections`, tiene que traer el arreglo/objeto completo deseado, no un delta — el merge es a nivel de campo top-level, no dentro de `nodes`.

```powershell
python "scripts/manage_n8n_workflows.py" update --url "https://n8n.midominio.com" --workflow-id <id> --patch cambio.json
```

Sin `--apply` muestra el diff completo (formato `unified_diff`) y para ahí. Mostrale ese diff al usuario tal cual antes de pedir confirmación — no lo resumas ni lo reinterpretes.

### Borrar (`delete`)

Irreversible. Conseguí el nombre exacto del workflow (vía `n8n-workflow-auditor --summary` si hace falta) y pasalo en `--confirm-name`.

```powershell
python "scripts/manage_n8n_workflows.py" delete --url "https://n8n.midominio.com" --workflow-id <id> --confirm-name "Nombre exacto" --apply
```

## Reporte

Después de cada operación, resumí: qué se planeó, si se aplicó o quedó en dry-run, y el resultado (`[OK]` o el error tal cual lo devolvió n8n — nunca lo suavices ni inventes una causa distinta a la que dice el mensaje).

## Recurso incluido

`scripts/manage_n8n_workflows.py` es un cliente sin dependencias externas con 8 subcomandos (`create`, `activate`, `deactivate`, `archive`, `unarchive`, `transfer`, `update`, `delete`). Verificado end-to-end contra una instancia n8n real: create/activate/update/deactivate/archive/unarchive/delete completos, incluyendo dos comportamientos reales de la API que no estaban documentados igual en el OpenAPI — `PUT` rechaza cualquier campo fuera de un allowlist estricto (la respuesta de `GET` trae campos internos como `sourceWorkflowId`/`activeVersionId`/`versionCounter` que rompen el `PUT` si se reenvían tal cual) y rechaza `description: null` aunque el propio `GET` lo devuelva así. El script ya filtra ambos casos. `transfer` está verificado en formato de request y manejo de error (404 ante proyecto inexistente), no en una transferencia exitosa real: la instancia de prueba tiene `teamProjectsEnabled: false` (confirmado vía `search_projects` del MCP oficial) y no admite crear un segundo proyecto para probarlo — limitación de configuración de la instancia, no del script.
