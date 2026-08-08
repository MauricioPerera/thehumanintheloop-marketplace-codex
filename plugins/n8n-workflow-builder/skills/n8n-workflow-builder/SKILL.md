---
name: n8n-workflow-builder
description: 'Cliente genérico para el MCP oficial de n8n (distinto de su REST API): descubre nodos, valida workflows/nodos antes de crearlos, construye y actualiza vía el n8n Workflow SDK con operaciones atómicas (no reemplazo completo), prueba con datos simulados, y consulta/restaura historial de versiones. Úsala cuando el usuario pida construir, validar, editar de forma segura, probar sin tocar servicios reales, o ver el historial de un workflow de n8n — especialmente si menciona el MCP de n8n.'
---

# N8N Workflow Builder

Cliente genérico (`list-tools` / `call`) para el servidor MCP oficial de n8n. No reimplementa lógica de negocio — el servidor MCP ya valida, aplica operaciones atómicas y genera datos de prueba; tu trabajo es armar los argumentos correctos, mostrar el plan antes de mutar, y no adivinar sintaxis del SDK.

## Esto NO es la REST API

Este plugin habla con `/mcp-server/http` (protocolo MCP, JSON-RPC), un servicio completamente distinto de `/api/v1/...` (REST) que usan `n8n-workflow-auditor`, `n8n-workflow-manager`, `n8n-credential-manager` y `n8n-community-package-manager`. Tiene su **propio Bearer token** (variable `N8N_MCP_TOKEN`, JWT con audiencia `mcp-server-api`) — es distinto de `N8N_API_KEY` (audiencia `public-api`) y no son intercambiables. Pedile al usuario el que corresponda según qué vayas a usar.

El MCP construye workflows con el **n8n Workflow SDK** (código TypeScript/JavaScript que se compone y valida), no con el JSON crudo de nodos/conexiones que arma `n8n-workflow-manager`. Para construir o editar workflows de forma robusta, preferí este plugin sobre el REST API — tiene validación real y operaciones atómicas de update en vez de un reemplazo completo.

## Requisitos previos

Pide al usuario, antes de ejecutar nada:
1. URL del endpoint MCP (ej. `https://n8n.midominio.com/mcp-server/http`).
2. El Bearer token del MCP server (`N8N_MCP_TOKEN`) — no la API key de la REST API.

Nunca imprimas, repitas ni guardes el valor del token.

## Cómo funciona el script

Dos subcomandos únicamente:

- `list-tools`: lista las 33 tools disponibles (solo lectura, siempre segura).
- `call --tool <nombre> --args-file <archivo.json> [--apply]`: invoca cualquier tool. Las de solo lectura corren directo; las mutantes muestran el plan y paran salvo que pases `--apply`.

Clasificación de mutantes (hardcodeada en el script, no confíes en el nombre de la tool para adivinar):

```
create_workflow_from_code, update_workflow, execute_workflow, publish_workflow,
unpublish_workflow, archive_workflow, restore_workflow_version, test_workflow,
create_data_table, rename_data_table, add_data_table_column,
delete_data_table_column, rename_data_table_column, add_data_table_rows
```

**`test_workflow` es mutante aunque el nombre suene inofensivo**: según la propia descripción de la tool, los nodos con credenciales, HTTP o triggers se simulan (pin data), pero `Execute Command` y lectura/escritura de archivos **corren de verdad**. No lo trates como un dry-run gratis. Un nombre de tool nuevo que el script no conoce (versión futura de n8n) se trata como mutante por defecto — el criterio conservador gana.

## Flujo recomendado para construir un workflow

Seguí el orden que el propio servidor MCP indica en sus `instructions` (no lo inventes vos):

1. `get_sdk_reference` (con `sections: ["guidelines"]` o `["design"]`) — leelo ANTES de escribir código. No adivines la sintaxis del SDK.
2. `get_workflow_best_practices` con la técnica relevante (`"chatbot"`, `"scheduling"`, etc.), o `technique: "list"` si no sabés cuál aplica.
3. `search_nodes` con las queries de los servicios/nodos que necesitás.
4. `get_node_types` con TODOS los node IDs que vas a usar (incluidos discriminadores de `search_nodes`) — te da los parámetros exactos. No adivines nombres de parámetros.
5. `explore_node_resources` para cualquier parámetro con selector dinámico (canal de Slack, hoja de Google Sheets, etc.), usando un `credentialId` real de `list_credentials`.
6. Escribí el código del SDK.
7. `validate_node_config` por nodo a medida que lo armás (señal más limpia que esperar al validate completo).
8. `validate_workflow` con el código completo. Arreglá errores y revalidá hasta que sea válido.
9. `create_workflow_from_code` (mutante, `--apply` tras confirmación) con una `description` corta (1-2 frases, máx 255 caracteres).
10. Para cambios posteriores, `update_workflow` con operaciones atómicas (`addNode`, `updateNodeParameters`, `setNodeParameter`, `renameNode` — usa `oldName`/`newName`, no `nodeName`, error real que encontré probando —, `addConnection`, `removeConnection`, `setNodeCredential`, `setNodeSettings`, `setWorkflowSettings`, etc.). Todo el batch es atómico: si una operación falla, no se aplica ninguna. Para modificar un nodo existente usá `updateNodeParameters`/`setNodeParameter`, nunca `removeNode` + `addNode` del mismo nodo — desconecta sub-nodos (modelo LLM, memoria, tools) que no se re-conectan solos.
11. `publish_workflow` cuando esté listo para producción.

## Manejo de errores en el workflow que construís

Dos capas, según las instrucciones del propio MCP: (1) por nodo, `setNodeSettings` con `onError`/`retryOnFail`/`maxTries`; (2) notificación de fallos vía un nodo Error Trigger — apuntando `settings.errorWorkflow` (con `setWorkflowSettings`) a un workflow separado ya **publicado** con un Error Trigger como primer nodo, o agregando un Error Trigger directo en el mismo workflow. No actives manejo de errores en silencio: explicá ambos patrones y preguntá cuál prefiere el usuario.

## Reporte

Mostrá siempre el plan (tool + argumentos) antes de `--apply`. Si una tool devuelve `isError: true` o un error de validación, mostralo tal cual — no lo reinterpretes ni asumas que el script está roto (ej. `renameNode` pide `oldName`, no `nodeName`; si te equivocás en un nombre de campo, la API lo dice claro).

## Recurso incluido

`scripts/manage_n8n_mcp.py` es un cliente JSON-RPC sin dependencias externas. El protocolo es **stateless**: cada request es un POST independiente, no hace falta `initialize` antes de `tools/call` (verificado). Fuerza salida UTF-8 (bug real encontrado: en Windows, `stdout` es `cp1252` por defecto y crashea con los caracteres Unicode que trae la referencia del SDK). Verificado end-to-end contra una instancia real: `list-tools`, `search_nodes`, `get_sdk_reference`, `validate_workflow` (código válido confirmado), `create_workflow_from_code` (workflow creado de verdad), `update_workflow` con `renameNode` (primero falló por el nombre de campo incorrecto, mensaje de error real propagado correctamente, corregido y confirmado), `get_workflow_history` (2 versiones reales devueltas). El workflow de prueba se borró al final vía `n8n-workflow-manager` (REST API) — este MCP no tiene una tool de borrado definitivo, solo `archive_workflow` (soft-delete).
