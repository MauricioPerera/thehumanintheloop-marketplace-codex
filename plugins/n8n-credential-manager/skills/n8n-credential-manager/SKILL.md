---
name: n8n-credential-manager
description: 'Gestiona credenciales de n8n vía REST API: crear, renombrar, rotar el secreto, borrar (con confirmación por nombre exacto), probar y transferir. El valor del secreto se lee de un archivo local aportado por el usuario y nunca se imprime ni se registra. Úsala cuando el usuario pida crear, rotar, renombrar, borrar, probar o transferir una credencial de n8n.'
---

# N8N Credential Manager

Administra credenciales de n8n sin ejecutar ninguna mutación hasta que el usuario confirme el plan en el chat, y sin que el valor de ningún secreto pase por vos ni quede en ningún log.

## Alcance

Cubre `create`, `rename`, `rotate`, `delete`, `test` y `transfer` sobre `/api/v1/credentials`. Para inventariar credenciales sin mutar nada (tipo, con qué proyecto están compartidas, cuáles no se usan), usa `n8n-workflow-auditor --credentials` o `--native-audit`, no esta skill.

## Regla innegociable: el secreto nunca pasa por el chat

`create` y `rotate` necesitan el valor real del secreto (`data`: `accessToken`, `password`, lo que sea según el tipo). Ese valor **siempre** se lee de un archivo JSON local que el usuario prepara de antemano — nunca lo pidas por chat, nunca lo escribas vos en un archivo a partir de algo que el usuario te dictó en la conversación, y nunca lo repitas de vuelta. El script solo imprime los **nombres** de los campos que va a mandar, jamás sus valores. n8n tampoco ayuda a romper esto: la API nunca devuelve `data` en ningún `GET`, así que no hay forma de que este flujo filtre un secreto existente aunque quisiera.

Antes de `create`, usa `schema --type <tipo>` para saber qué campos necesita ese tipo de credencial (ej. `githubApi` → `accessToken`) y decirle al usuario exactamente qué debe poner en su archivo.

## Requisitos previos

Pide al usuario, antes de ejecutar nada:
1. URL base de n8n.
2. Una API key con los scopes que correspondan a la operación (`credential:create`, `credential:update`, `credential:delete`, `credential:read`, `credential:move`). Instruye a pasarla por `N8N_API_KEY`.
3. Para `create`/`rotate`: que prepare un archivo JSON local con los campos del secreto (mostrale primero la salida de `schema` para que sepa qué poner).

Nunca imprimas, repitas ni guardes el valor de la API key ni del contenido de ese archivo.

## Flujo por operación

### Ver el schema de un tipo (`schema`, solo lectura)

```powershell
python "scripts/manage_n8n_credentials.py" schema --url "https://n8n.midominio.com" --type githubApi
```

### Crear (`create`)

```powershell
$env:N8N_API_KEY = "<api-key-del-usuario>"
python "scripts/manage_n8n_credentials.py" create --url "https://n8n.midominio.com" --name "Mi Credencial" --type githubApi --data-file secreto.json --apply
```

Sin `--apply` es dry-run: muestra el nombre de la credencial, el tipo, y los **nombres** de los campos del secreto (nunca los valores). Recordale al usuario que borre `secreto.json` después de usarlo.

### Renombrar (`rename`) — no toca el secreto

```powershell
python "scripts/manage_n8n_credentials.py" rename --url "https://n8n.midominio.com" --credential-id <id> --name "Nombre nuevo" --apply
```

### Rotar el secreto (`rotate`)

```powershell
python "scripts/manage_n8n_credentials.py" rotate --url "https://n8n.midominio.com" --credential-id <id> --data-file nuevo-secreto.json --apply
```

Por defecto reemplaza el secreto completo. Con `--partial`, n8n desredacta el secreto existente y lo mergea con lo que mandes (útil para cambiar un solo campo sin conocer los demás) — usalo solo si el usuario lo pide explícitamente, el reemplazo completo es más predecible.

### Borrar (`delete`)

Irreversible. Conseguí el nombre exacto (vía `n8n-workflow-auditor --credentials` si hace falta).

```powershell
python "scripts/manage_n8n_credentials.py" delete --url "https://n8n.midominio.com" --credential-id <id> --confirm-name "Nombre exacto" --apply
```

### Probar (`test`) — no muta nada

```powershell
python "scripts/manage_n8n_credentials.py" test --url "https://n8n.midominio.com" --credential-id <id>
```

n8n prueba la credencial ya guardada contra su servicio real. **Caveat verificado**: en instancias reales, `test` puede fallar con un error interno de n8n (`Unrecognized node type: ...`) según el tipo de credencial y qué nodos tenga disponibles esa instancia — es un comportamiento del lado de n8n, no del script. Mostrá el error tal cual lo devuelve la API, no lo reinterpretes ni asumas que es un bug propio.

### Transferir (`transfer`)

```powershell
python "scripts/manage_n8n_credentials.py" transfer --url "https://n8n.midominio.com" --credential-id <id> --destination-project-id <id> --apply
```

**Caveat verificado**: requiere una licencia de n8n con soporte multi-proyecto (`feat:projectRole:admin`). En instancias Community/single-project, `GET /projects` y `POST /projects` fallan con un error de licencia — no hay proyecto destino real al que transferir. El comando está implementado y verificado en formato de request y manejo de errores (404 correcto ante un proyecto inexistente), pero no se pudo verificar una transferencia exitosa real por esta limitación de licencia, no del script.

## Reporte

Después de cada operación, resumí qué se planeó, si se aplicó, y el resultado — sin repetir nunca el contenido de `data`. Si `test` o `transfer` fallan por las razones documentadas arriba, decilo explícito en vez de sugerir que el script está roto.

## Recurso incluido

`scripts/manage_n8n_credentials.py` es un cliente sin dependencias externas con 7 subcomandos. Verificado end-to-end contra una instancia n8n real (sandbox): create/rename/rotate/delete completos sobre una credencial descartable, incluyendo el gate de `--confirm-name`; `schema` y `test` verificados en su formato de request/respuesta; `transfer` verificado en formato y manejo de error, no en una transferencia exitosa (limitación de licencia de la instancia de prueba, documentada arriba).
