# TheHumanInTheLoop Marketplace Codex

Marketplace público de plugins y skills para Codex creados por Mauricio Perera.

## Plugins disponibles

- `linter-seo-geo-2026`: auditor estático de artículos para SEO híbrido y GEO.

## Estructura

- `.agents/plugins/marketplace.json`: catálogo del marketplace.
- `plugins/`: un directorio por plugin.
- Cada plugin contiene `.codex-plugin/plugin.json` y sus skills bajo `skills/`.

## Añadir un plugin

1. Crear un directorio dentro de `plugins/`.
2. Añadir su manifiesto `.codex-plugin/plugin.json`.
3. Añadir una entrada en `.agents/plugins/marketplace.json`.
4. Validar el plugin antes de publicar cambios.

Este repositorio no incluye todavía una licencia. Añade una licencia explícita antes de autorizar la reutilización comercial o redistribución por terceros.
