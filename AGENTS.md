# Instrucciones para agentes de IA

Este repositorio es el marketplace público de TheHumanInTheLoop para Claude Code y Codex. Trabaja con cambios pequeños, verificables y reversibles.

## Fuentes de verdad

- `.claude-plugin/marketplace.json`: catálogo instalable por Claude Code.
- `.agents/plugins/marketplace.json`: catálogo instalable por Codex.
- `plugins/<plugin>/.claude-plugin/plugin.json`: manifest Claude del plugin.
- `plugins/<plugin>/.codex-plugin/plugin.json`: manifest Codex del plugin.
- `plugins/<plugin>/skills/`: skills compartidas.
- `docs/index.html` y `docs/app.js`: catálogo web y acciones de instalación.
- `docs/analyses/<analysis>/`: resultados publicados de Design System Analysis.
- `docs/sitemap.xml`, `docs/robots.txt` y `docs/llms.txt`: descubrimiento web y por IA.
- `scripts/`: validadores ejecutados por CI.

## Añadir o actualizar un plugin

1. Usa un nombre minúsculo con guiones bajo `plugins/`.
2. Mantén sincronizados ambos manifests cuando el plugin sea multiplataforma.
3. Reutiliza las skills compartidas bajo `skills/`.
4. Actualiza la entrada de ambos marketplaces y la ficha visible del catálogo.
5. Incrementa la versión cuando cambie el comportamiento o el contenido.
6. No inventes capacidades, fuentes, enlaces o integraciones.

## Añadir un análisis

Incluye `DESIGN.md`, `design-system.json`, `validation-report.json` e `index.html`. Declara la URL fuente, la fecha observada, la procedencia y las advertencias. Añade canonical, Open Graph, JSON-LD y la URL al sitemap. Un análisis externo no debe presentarse como sistema oficial de la marca analizada.

## Validación obligatoria

Desde la raíz:

```powershell
python plugins/marketplace-validator/scripts/validate_marketplace.py .
python scripts/validate_catalog_metadata.py
python scripts/validate_analysis_metadata.py
node --check docs/app.js
git diff --check
```

La CI debe pasar antes de publicar. Revisa `git diff` y `git status`; este workspace puede contener artefactos locales de demos que no deben entrar en el marketplace.

## Seguridad y autorización

No leas, publiques ni introduzcas secretos. No elimines plugins, skills, análisis o activos sin confirmación explícita. Para vulnerabilidades, sigue [`SECURITY.md`](SECURITY.md); para contribuciones, sigue [`CONTRIBUTING.md`](CONTRIBUTING.md).
