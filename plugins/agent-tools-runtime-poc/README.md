# Agent Tools Runtime POC

Runtime persistente basado en `just-bash` para que las skills carguen solo el
adaptador que necesitan: MCP, REST/API o CLI local. La fachada MCP mantiene un
contrato pequeño (`agent_tools_help` y `agent_tools_exec`) y la exploración de
capacidades ocurre bajo demanda.

## Requisitos

- Node.js `>=20.18.1`.
- `npm`.
- Autorización explícita antes de instalar dependencias o ejecutar comandos.

## Instalación local

Desde esta carpeta:

```powershell
npm install
npm run probe
npm test
```

El resultado `READY` del probe confirma Node, `just-bash` y el runtime. La
instalación no configura credenciales ni ejecuta adaptadores automáticamente.

Para validar además un CLI concreto sin ejecutarlo, usa sus variables de
preflight:

```powershell
$env:AGENT_TOOLS_COMMAND = "gh"
$env:AGENT_CLI_ALLOWLIST = "gh,docker,supabase"
npm run probe
```

El reporte indica si el programa existe en `PATH` y si está en la allowlist.

## Uso

Runtime JSONL persistente:

```powershell
npm run serve
```

Fachada MCP local:

```powershell
npm run mcp
```

El manifiesto Claude usa `.mcp.json` con `${CLAUDE_PLUGIN_ROOT}`. El manifiesto
Codex declara el servidor inline en `.codex-plugin/plugin.json`, con `cwd: "."`
y una ruta relativa al plugin. Así ambos clientes arrancan la misma fachada sin
depender de una ruta de manifiesto no estándar.

La fachada MCP usa npx con la versión exacta publicada
`@rckflr/agent-tools-runtime@0.1.1` y deshabilita scripts de instalación. La
copia local se conserva como fallback; para forzarla durante una prueba, define
`AGENT_TOOLS_RUNTIME_SOURCE=local`.

Cargar únicamente el adaptador requerido por la skill:

```text
load commands/generic-mcp.mjs
mcp-search "search repository"
```

Otros módulos disponibles:

- `commands/n8n-mcp.mjs`: herramientas MCP de n8n y estado OAuth host-side.
- `commands/rest-api.mjs`: requests relativos a `AGENT_API_BASE_URL`.
- `commands/local-cli.mjs`: ejecución de programas incluidos en
  `AGENT_CLI_ALLOWLIST`.

## Seguridad

Los adaptadores MCP, REST y CLI se ejecutan en el host, no dentro del sandbox
de `just-bash`. Los tokens se leen desde variables o almacenes del host y no se
aceptan como argumentos de comandos. Las mutaciones REST, las llamadas MCP
genéricas y todas las ejecuciones CLI exigen confirmación explícita. El CLI se
ejecuta con `execFile`, `shell: false`, timeout y límite de salida.

Esta es una prueba de concepto: cada skill debe declarar el adaptador, la
allowlist, los permisos y el criterio de confirmación apropiados para su caso.
