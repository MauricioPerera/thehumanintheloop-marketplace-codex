---
name: agent-tools-runtime-poc
description: Valida y documenta el uso de un runtime just-bash persistente para cargar comandos de plugins y conectar MCP, APIs o CLIs. Úsala cuando una skill necesite comprobar el runtime, verificar un comando o explicar cómo implementar el adaptador faltante.
---

# Agent Tools Runtime POC

Actúa como una receta de integración. No instales dependencias, no cargues comandos y no ejecutes código de implementación sin autorización explícita.

El runtime distribuido por esta POC requiere Node.js >= 20.18.1 y la dependencia
`just-bash`. Para preparar una instalación autorizada desde la raíz del plugin:

```powershell
npm install
```

## Flujo obligatorio

1. Ejecuta el validador incluido:

   ```powershell
   node scripts/runtime_probe.mjs --json
   ```

2. Interpreta el estado:

   - `READY`: Node, `just-bash`, el runtime y el comando solicitado están disponibles.
   - `IMPLEMENTABLE`: falta `just-bash`, el runtime o el comando, pero el reporte incluye contexto para implementarlo.
   - `BLOCKED`: falta una autorización, credencial o requisito que no puede inferirse.

3. Si el estado es `READY`, sigue el contrato del comando de la skill especializada.
4. Si el estado es `IMPLEMENTABLE`, explica al usuario qué falta y muestra el contexto de implementación. No lo ejecutes automáticamente.
5. Si el estado es `BLOCKED`, solicita únicamente la autorización o dato concreto que falta.

Para validar un CLI específico sin ejecutarlo, define `AGENT_TOOLS_COMMAND` y,
si corresponde, `AGENT_CLI_ALLOWLIST` antes del probe. El reporte distingue
entre que el programa exista en `PATH`, que esté permitido y que haya sido
ejecutado; el probe nunca ejecuta el CLI.

## Contrato del runtime

El runtime central mantiene una instancia de `just-bash` por conversación y un contexto aislado por sesión. Los plugins declaran comandos; las skills solo indican cuándo y cómo utilizarlos.

Comandos conceptuales del runtime:

```text
agent-tools runtime status
agent-tools command list
agent-tools load <plugin-name>
agent-tools exec <command> [json-arguments]
```

Para una POC local, el proceso persistente se inicia con:

```powershell
node runtime/agent-tools-runtime.mjs serve
```

Después de `npm install`, también puede iniciarse como comando local:

```powershell
npx agent-tools serve
```

Cuando el plugin se instala en un host compatible con `.mcp.json`, puede iniciar
automáticamente el puente MCP local. El agente seguirá viendo solo
`agent_tools_help` y `agent_tools_exec`; los adaptadores concretos se cargan con
`agent_tools_exec` según la skill activa.

En ese modo recibe una línea JSON por operación. El módulo de comandos debe
exportar `register({ bash, commands })`; la skill puede indicar qué módulo cargar,
pero no debe modificarlo ni ejecutarlo sin autorización.

Para el adaptador de n8n:

```text
agent-tools load commands/n8n-mcp.mjs
n8n-auth-status
n8n-search "validate workflow"
n8n-describe validate_workflow
n8n-call validate_workflow '{"code":"..."}'
n8n-call --confirm create_workflow_from_code '{"code":"..."}'
```

Configura `N8N_MCP_TOKEN` en el host antes de cargar el adaptador. Nunca pases el
token como argumento de `n8n-call` ni lo escribas dentro del sandbox. También
puedes reutilizar el almacén OAuth de la POC ejecutando una vez:

```text
n8n-mcp-cli auth login
```

El adaptador renovará el token mediante el refresh token cuando corresponda.

Para cualquier otro MCP, carga el adaptador genérico y configura sus credenciales
en el host. El token es opcional para MCP públicos:

```text
agent-tools load commands/generic-mcp.mjs
mcp-search "search repository"
mcp-describe search_repositories
mcp-call --confirm search_repositories '{"query":"..."}'
```

Para un MCP público basta con configurar `AGENT_MCP_URL`. Para uno protegido,
añade `AGENT_MCP_TOKEN`. El adaptador conserva automáticamente `Mcp-Session-Id`
cuando el servidor lo devuelve.

El adaptador genérico exige `--confirm` para todas las llamadas hasta que exista
una política de solo lectura específica del proveedor.

Para capacidades REST que el MCP no cubre, carga el adaptador API. Solo acepta
rutas relativas a `AGENT_API_BASE_URL`; `GET` y `HEAD` son de lectura y el resto
requiere `--confirm`:

```text
agent-tools load commands/rest-api.mjs
api-request GET /health
api-request --confirm POST /workflows '{"name":"demo"}'
```

El token opcional se configura en `AGENT_API_TOKEN` y nunca se entrega como
argumento del comando.

Para CLIs locales, carga el adaptador y declara una allowlist en el host:

```powershell
$env:AGENT_CLI_ALLOWLIST = "gh,docker,supabase"
agent-tools load commands/local-cli.mjs
cli-run --confirm gh repo view MauricioPerera/KDD
```

El adaptador usa `execFile` sin shell y rechaza programas que no estén en la
allowlist. Todas las ejecuciones requieren confirmación.

Ejemplo de sesión:

```json
{"action":"status"}
{"action":"load","module":"commands/runtime-demo.mjs"}
{"action":"list"}
{"action":"exec","command":"runtime-echo hola | tr a-z A-Z"}
```

Los adaptadores de MCP, API y CLI deben ejecutarse en el host. No introduzcas tokens OAuth, claves privadas ni credenciales dentro del filesystem o las variables del sandbox.

## Reglas de seguridad

- Usa allowlists de comandos y endpoints.
- Exige confirmación para mutaciones, publicaciones, borrados o ejecuciones remotas.
- Mantén límites de tiempo, memoria y salida.
- Devuelve respuestas JSON estructuradas con `code`, `data`, `error` y `meta`.
- No confundas que `just-bash` esté instalado con que el adaptador del plugin esté cargado.
