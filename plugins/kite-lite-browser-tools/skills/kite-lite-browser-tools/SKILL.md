---
name: kite-lite-browser-tools
description: 'Registra kite-lite (motor web ligero orientado a agentes, sin JS vivo) como servidor MCP y enseña a usar bien sus 9 tools de navegación/fetch/screenshot: sesión persistente por proceso, formularios solo GET, sin ejecución de JS de la página, y detección declarativa de WebMCP. Úsala cuando el usuario pida navegar, fetchear, hacer scraping ligero, o tomar screenshots de una página sin un navegador real, o mencione kite-lite.'
---

# Kite-lite Browser Tools

Este plugin registra [kite-lite](https://github.com/MauricioPerera/kite-lite) como servidor MCP (`.mcp.json` en la raíz del plugin, `command: kite-lite`, `args: [mcp]`) — Claude Code lo levanta automáticamente al habilitar el plugin, con una sesión de navegación persistente por proceso durante toda la conversación. Este SKILL.md no reimplementa esas tools ni las envuelve en un script: te dice cómo usarlas bien, porque **no es un navegador real** y usarlo como si lo fuera produce resultados silenciosamente incorrectos.

## Requisito previo

Necesita el binario `kite-lite` instalado y en PATH:

```powershell
cargo install kite-lite
```

Corré `python scripts/verify_kite_lite.py` para confirmar que el binario responde correctamente antes de asumir que las tools van a funcionar — hace el handshake MCP real (`initialize` + `tools/list`) y confirma que las 9 tools esperadas están presentes.

**Codex**: el bundling automático vía `.mcp.json` está confirmado para Claude Code. Para Codex, no verificamos si lee el mismo archivo — confirmá el mecanismo de registro de MCP que use tu instalación antes de asumir que se auto-registra igual.

## Las 9 tools, y sus límites reales (no los ignores)

kite-lite **no tiene un DOM vivo ligado a JavaScript** — es una decisión de diseño, no una limitación temporal (ver el README del proyecto: "no hay ítem de roadmap para esto porque resolverlo significaría abandonar la decisión de diseño"). Consecuencias directas para cada tool:

- **`fetch_page(url)`** — resumen liviano `{url, title, text, links}` (más `cookies` si el sitio las setea, y `tools` si detecta formularios WebMCP declarativos). No ejecuta JS. Para SPAs o contenido cargado por `fetch` del lado cliente, **vas a ver una página vacía o incompleta** — no es un bug, es el límite del proyecto. No lo uses para sitios que dependen de JS para renderizar contenido.
- **`browser_navigate(url)`, `browser_click(selector)`, `browser_type(text, selector?)`, `browser_get_dom(selector?)`, `browser_screenshot(format?)`** — una única sesión de navegación persistente **por proceso MCP**, no multi-pestaña. Las cookies y redirecciones se mantienen entre llamadas dentro de esa sesión (útil para login → página siguiente), pero si el proceso se reinicia, se pierde todo el estado.
- **`browser_click`** no ejecuta `onclick` ni corre `<script>` de la página — simula click/foco/submit sin DOM↔JS real. Sobre un `<button>`/`submit`, arma un GET con los campos del form — **nunca POST**, no hay body de request. Si el formulario real espera POST, el submit simulado no va a reflejar el comportamiento real.
- **`eval_js(url, script)`** — corre en un contexto Boa aislado, sin red/filesystem/DOM real más allá de un snapshot reducido (`document.title`, `document.body.innerText`, `querySelector` limitado a un `h1`/`h2`/`h3`/`p`/`a`/`button`). No es un intérprete de JS de página completo.
- **`render_screenshot(url, format?)`** — PNG (base64) o SVG. Necesita fuentes instaladas en el sistema donde corre `kite-lite`; sin fuentes, sale en blanco (todo lo que dibuja es texto, no hay rectángulos/imágenes propias).
- **`browser_call_tool(name, arguments?)`** — llena y envía un formulario detectado vía [WebMCP declarativo](https://github.com/webmachinelearning/webmcp/blob/main/declarative-api-explainer.md) (atributos `toolname`/`tooldescription`/`toolparamdescription` en el HTML). Solo el subset **declarativo** está soportado — la API imperativa (`navigator.modelContext.registerTool()` en JS) no, por la misma razón de "sin DOM↔JS vivo". Mismo límite de GET-only que `browser_click`.

**Esto no habilita Playwright real.** El servidor CDP de kite-lite (fuera del alcance de este plugin, que solo cubre las tools MCP) es compatible lo suficiente para que Playwright *conecte*, pero cada acción de Playwright depende de un DOM↔JS vivo para chequear visibilidad/actionability — eso es justo lo que este proyecto evita a propósito.

## Cuándo SÍ conviene usarlo

Páginas server-rendered (HTML completo sin depender de JS para el contenido relevante), fetch/scraping liviano, screenshots rápidos sin el costo de un Chrome headless (~4-7 MiB medidos vs cientos de MB), y flujos de login→navegación simples con formularios GET. Cuando el usuario necesite interactuar con una SPA real o un formulario POST, no fuerces kite-lite — decilo y sugerí un navegador real.

## Reporte

Cuando uses estas tools, si el resultado parece vacío o incompleto, primero descartá que sea contenido dependiente de JS antes de reportarlo como un error — es la causa más común dado el diseño del proyecto.

## Recurso incluido

- `.mcp.json`: registra `kite-lite` como servidor MCP stdio, auto-levantado por Claude Code al habilitar el plugin (confirmado: mecanismo documentado de "Plugin-provided MCP servers").
- `scripts/verify_kite_lite.py`: smoke test sin dependencias externas, un solo proceso corto de solo lectura — hace el handshake `initialize`+`tools/list` contra el binario real y confirma que las 9 tools esperadas están presentes. Verificado con tres casos: binario válido (9 tools confirmadas), ruta inexistente (error claro, sin traceback), y sin argumento (auto-descubre vía PATH, encontró el binario real instalado del usuario). También verificado manualmente con una llamada `fetch_page` real contra `https://example.com`, confirmando el shape `{url, title, text, links}`.
