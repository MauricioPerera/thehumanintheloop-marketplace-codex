---
name: plugin-authoring
description: Diseña y prepara plugins para este marketplace creando la estructura, manifests, skills, catálogo sincronizado y validaciones necesarias. Úsala cuando el usuario quiera crear, actualizar o publicar un plugin para Claude Code y Codex.
---

# Plugin Authoring

Ayuda a convertir una idea en un plugin instalable y verificable para este marketplace.

## Reglas del repositorio

- Usa `plugins/<nombre-en-minusculas-con-guiones>/`.
- Mantén `.claude-plugin/plugin.json` y `.codex-plugin/plugin.json` sincronizados.
- Coloca las instrucciones compartidas en `skills/<nombre-de-skill>/SKILL.md`.
- El `name` de cada skill debe coincidir con el nombre de su carpeta.
- Usa una categoría existente: `Content & Editorial`, `Design Systems`, `Marketplace & Quality`, `Developer Tools`, `Accessibility & UX`, `Security & Privacy`, `Research & Evidence` o `AI & Prompt Engineering`.
- No inventes integraciones, fuentes, enlaces, capacidades ni resultados.
- No introduzcas secretos, credenciales, artefactos de build ni dependencias innecesarias.

## Flujo

1. Inspecciona el repositorio y confirma si el plugin es nuevo o una actualización.
2. Define el identificador, nombre visible, propósito, categoría, versión y límites.
3. Crea la estructura del plugin y una skill con frontmatter válido.
4. Si el plugin necesita scripts, añade validadores deterministas y documenta sus comandos.
5. Registra la misma entrada en `.claude-plugin/marketplace.json` y `.agents/plugins/marketplace.json`.
6. Actualiza la ficha en `docs/app.js`, el JSON-LD de `docs/index.html` y los conteos del `README.md` cuando corresponda.
7. Corre `python scripts/generate_plugin_pages.py` para regenerar la página estática compartible del plugin (`docs/plugins/<nombre>/`) y su entrada en `docs/sitemap.xml`.
8. Ejecuta la suite completa de validación.
9. Revisa `git diff`, `git status` y los cambios de autoría o licencia antes de publicar.

## Manifests mínimos

Claude debe declarar `name`, `displayName`, `version`, `description` y autor.

Codex debe declarar además `skills: "./skills/"` e `interface` con `displayName`, descripciones, desarrollador, categoría, capacidades y prompt inicial.

El nombre y la versión deben ser iguales en ambos manifests. El `displayName` de Claude debe coincidir con `interface.displayName` de Codex.

## Validación

Desde la raíz del repositorio ejecuta:

```powershell
python scripts/validate_all.py
```

Si necesitas aislar un problema:

```powershell
python plugins/marketplace-validator/scripts/validate_marketplace.py .
python scripts/validate_catalog_metadata.py
python scripts/validate_plugin_pages.py
python scripts/validate_analysis_metadata.py
python scripts/validate_llms_catalog.py
node --check docs/app.js
git diff --check
```

No declares el plugin listo si alguna comprobación devuelve `[FAILED]` o si los catálogos no están sincronizados.

## Formato de entrega

Entrega un resumen con:

- identificador, versión y categoría;
- archivos creados o modificados;
- capacidades y límites reales;
- comandos de validación ejecutados y resultado;
- advertencias, dependencias o autorización pendiente.
