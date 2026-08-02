# TheHumanInTheLoop Marketplace Codex

Marketplace público de plugins, skills y Design System Analyses para Codex creados por Mauricio Perera.

## Plugins disponibles

- `linter-seo-geo-2026`: auditor estático de artículos para SEO híbrido y GEO.

## Estructura

- `.agents/plugins/marketplace.json`: catálogo del marketplace.
- `plugins/`: un directorio por plugin.
- Cada plugin contiene `.codex-plugin/plugin.json` y sus skills bajo `skills/`.
- `docs/analyses/`: resultados publicados de análisis visuales; cada entrada contiene `DESIGN.md`, `design-system.json`, `validation-report.json` y un preview navegable.

## Design System Analyses

El marketplace publica resultados, no el plugin privado que los generó. Cada análisis debe incluir:

1. `DESIGN.md` como fuente de verdad con contrato duro, contrato blando y `Validation Contract`.
2. `design-system.json` derivado del `DESIGN.md`.
3. `validation-report.json` con estado, errores y advertencias.
4. `index.html` como preview navegable enlazado desde el catálogo.

Los análisis de terceros se presentan como análisis externos, no como sistemas oficiales de sus respectivas marcas.

## Añadir un plugin

1. Crear un directorio dentro de `plugins/`.
2. Añadir su manifiesto `.codex-plugin/plugin.json`.
3. Añadir una entrada en `.agents/plugins/marketplace.json`.
4. Validar el plugin antes de publicar cambios.

Este repositorio no incluye todavía una licencia. Añade una licencia explícita antes de autorizar la reutilización comercial o redistribución por terceros.
