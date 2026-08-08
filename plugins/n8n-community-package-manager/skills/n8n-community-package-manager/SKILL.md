---
name: n8n-community-package-manager
description: 'Instala, actualiza y desinstala paquetes de nodos de comunidad en n8n vía REST API, con verificación contra la lista vetada de n8n activa por defecto y confirmación explícita antes de cada mutación. Úsala cuando el usuario pida instalar, actualizar o desinstalar un paquete/nodo de comunidad de n8n.'
---

# N8N Community Package Manager

Administra paquetes npm de nodos de comunidad sin ejecutar ninguna mutación hasta que el usuario confirme el plan en el chat.

## Por qué esto es distinto a los otros managers de n8n

`n8n-workflow-manager` y `n8n-credential-manager` mutan un objeto aislado (un workflow, una credencial). Instalar un paquete de comunidad corre **código de terceros dentro de la instancia entera** y afecta a todos los workflows que corran ahí, no solo a uno. Tratalo con más cuidado: confirmá con el usuario el nombre exacto del paquete, explicá qué hace si no es obvio, y nunca uses `--allow-unverified` sin que el usuario lo haya pedido explícitamente sabiendo que implica saltarse la lista vetada de n8n.

## Alcance

Cubre `list` (solo lectura), `install`, `update` y `uninstall` sobre `/api/v1/community-packages`.

## Requisitos previos

Pide al usuario, antes de ejecutar nada:
1. URL base de n8n.
2. Una API key con los scopes correspondientes (`communityPackage:list`, `communityPackage:install`, `communityPackage:update`, `communityPackage:uninstall`).
3. El nombre npm exacto del paquete a instalar (debe empezar con `n8n-nodes-`, o `n8n-nodes-` después del scope si es un paquete con scope como `@usuario/n8n-nodes-ejemplo`). **No inventes ni asumas que un paquete existe** — antes de instalar, confirmá que existe de verdad (ej. consultando `https://registry.npmjs.org/<nombre>`) para no gastar un intento contra la API de n8n con un nombre que no existe.

## Flujo por operación

### Ver instalados (`list`, solo lectura)

```powershell
python "scripts/manage_n8n_packages.py" list --url "https://n8n.midominio.com"
```

### Instalar (`install`)

```powershell
$env:N8N_API_KEY = "<api-key-del-usuario>"
python "scripts/manage_n8n_packages.py" install --url "https://n8n.midominio.com" --name n8n-nodes-ejemplo --apply
```

Por defecto, n8n verifica el paquete contra su lista vetada y rechaza cualquiera que no esté ahí (`HTTP 400: Package ... is not vetted for installation`) — es la barrera de seguridad principal contra supply-chain, y funciona: no la rodees por comodidad. Si el usuario quiere instalar algo fuera de esa lista, agregá `--allow-unverified` solo después de que lo haya pedido explícitamente sabiendo lo que implica.

### Actualizar (`update`)

```powershell
python "scripts/manage_n8n_packages.py" update --url "https://n8n.midominio.com" --name n8n-nodes-ejemplo --apply
```

Agrega `--version <semver>` para una versión específica en vez de la última.

### Desinstalar (`uninstall`)

```powershell
python "scripts/manage_n8n_packages.py" uninstall --url "https://n8n.midominio.com" --name n8n-nodes-ejemplo --confirm-name n8n-nodes-ejemplo --apply
```

Advertí siempre que los workflows que usen nodos de ese paquete van a dejar de poder ejecutarlos — si no sabés si algún workflow lo usa, sugerí revisar antes (los nodos instalados por un paquete se ven en `list`, y se pueden buscar por `type` en `n8n-workflow-auditor --summary`/`--export-dir`).

## Reporte

Después de cada operación, resumí qué se planeó, si se aplicó, y el resultado tal cual lo devolvió n8n. Si `install` falla por "not vetted", explicá esa barrera en vez de sugerir saltarla como primer paso.

## Recurso incluido

`scripts/manage_n8n_packages.py` es un cliente sin dependencias externas con 4 subcomandos. Verificado end-to-end contra una instancia n8n real (sandbox): `list` sobre los paquetes reales instalados; `install` sin `--allow-unverified` bloqueado correctamente por la lista vetada de n8n (confirma que la barrera funciona); ciclo completo `install --allow-unverified` → `list` (confirma que aparece) → `uninstall` con gate de `--confirm-name` → `list` (confirma que la instancia queda exactamente como antes), usando un paquete real y públicamente verificable (`n8n-nodes-serpapi`).
