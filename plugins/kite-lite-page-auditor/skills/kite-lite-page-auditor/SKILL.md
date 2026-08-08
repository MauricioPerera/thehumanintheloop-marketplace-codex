---
name: kite-lite-page-auditor
description: 'Corre los 4 linters de pre-publicación de kite-lite (seo-lint, a11y-lint, social-lint, webmcp-lint) contra una URL o archivo HTML y consolida los hallazgos en un solo reporte con severidad agregada. Úsala cuando el usuario pida auditar una página antes de publicarla, revisar SEO/accesibilidad/preview social/WebMCP de una URL, o mencione kite-lite.'
---

# Kite-lite Page Auditor

Envuelve los 4 linters de [kite-lite](https://github.com/MauricioPerera/kite-lite) (motor web ligero orientado a agentes, sin JS vivo) para no tener que correrlos uno por uno y reconciliar formatos distintos a mano.

## Requisito previo

Necesita el binario `kite-lite` disponible. Si no está en PATH:

```powershell
cargo install kite-lite
```

o pasá su ruta con `--kite-lite-bin`. Este plugin no lo instala ni lo descarga — solo lo invoca.

## Uso

```powershell
python scripts/audit_page.py https://mi-sitio.com/pagina --json reporte.json --markdown reporte.md
python scripts/audit_page.py ./pagina.html --kite-lite-bin C:\ruta\kite-lite.exe
```

El target puede ser una URL, un archivo `.html`, o un `page.json` de kite-lite (el mismo formato que aceptan los 4 linters nativamente).

## Qué corre y qué significa cada uno

| Linter | Qué chequea | Severidades reales |
|---|---|---|
| `seo-lint` | `<title>`, meta description, `noindex`, `<h1>`, longitud de contenido | error/warning/info |
| `a11y-lint` | `alt` en imágenes, `<html lang>`, saltos de nivel de encabezado, links sin texto | solo warning hoy (nunca falla el exit code por sí solo) |
| `social-lint` | Cadena de fallback OG → Twitter Card → meta/`<title>` que usan los bots de preview | error/warning/info, más un objeto `preview` con lo que se resolvió |
| `webmcp-lint` | Formularios `toolname="..."` (WebMCP declarativo): descripción faltante, nombres duplicados, campos sin `name` | error/warning/info |

Ninguno de los 4 es una auditoría completa (ni WCAG, ni un linter de SEO exhaustivo) — son chequeos prácticos de errores comunes antes de publicar, tal como los documenta kite-lite mismo. No los presentes como más de lo que son.

## Reporte

El script ya normaliza los dos formatos JSON distintos que devuelven los linters (3 devuelven un array plano de `{severity, message}`; `social-lint` devuelve `{findings: [...], preview: {...}}`) en una sola estructura. Mostrale al usuario la tabla consolidada por linter, y si `social-lint` resolvió un preview, mostrá también qué título/descripción/imagen verían los bots.

El exit code del script es distinto de cero si **cualquiera** de los 4 linters reportó al menos un hallazgo de severidad `error` — tratalo como gate real si el usuario quiere bloquear una publicación en un pipeline.

## Recurso incluido

`scripts/audit_page.py` es un wrapper sin dependencias externas que solo hace `subprocess` sobre los 4 subcomandos de `kite-lite --json` — no fetchea nada por su cuenta, no habla MCP. Verificado end-to-end: contra `https://example.com` (2 warnings, 1 info, exit 0) y contra un HTML local con errores deliberados (`<title>` faltante, `noindex`, sin `alt`, sin `og:title`/`twitter:title`) — 3 errores, 5 warnings, 1 info, exit 1, los 4 formatos parseados y consolidados correctamente. Se encontró y corrigió un bug real: `--kite-lite-bin` con una ruta inexistente crasheaba con traceback en vez de un error claro.
