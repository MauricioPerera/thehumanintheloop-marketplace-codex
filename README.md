# TheHumanInTheLoop Marketplace

Marketplace público de plugins, skills y Design System Analyses para Claude Code y Codex, creado por Mauricio Perera.

## Plugins disponibles

- `Auditor SEO/GEO 2026` (`linter-seo-geo-2026`): validador de contenido para buscadores y motores generativos.
- `Marketplace Validator` (`marketplace-validator`): valida manifests y sincronización Claude Code/Codex.
- `Design System Auditor` (`design-system-auditor`): genera contratos `DESIGN.md`, tokens y validadores.
- `Content Fact Checker` (`content-fact-checker`): exige fuentes, fechas y evidencia para afirmaciones.
- `Repo Quality Gate` (`repo-quality-gate`): revisa repositorios antes de commit, PR o release.
- `Technical Docs Linter` (`technical-docs-linter`): valida documentación, ejemplos, comandos y enlaces.
- `Accessibility Auditor` (`accessibility-auditor`): audita HTML, ARIA, formularios y teclado.

## Estructura

- `.claude-plugin/marketplace.json`: catálogo compatible con Claude Code.
- `.agents/plugins/marketplace.json`: catálogo compatible con Codex.
- `plugins/`: un directorio por plugin.
- Cada plugin puede contener `.claude-plugin/plugin.json` y `.codex-plugin/plugin.json`; ambos reutilizan las mismas skills bajo `skills/`.
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
2. Añadir los manifiestos `.claude-plugin/plugin.json` y `.codex-plugin/plugin.json` cuando el plugin deba funcionar en ambas plataformas.
3. Añadir una entrada en `.claude-plugin/marketplace.json` y `.agents/plugins/marketplace.json`.
4. Mantener las skills compartidas en `skills/` y validar ambos formatos antes de publicar cambios.

## Instalación

En Claude Code:

```text
claude plugin marketplace add MauricioPerera/thehumanintheloop-marketplace-codex
claude plugin install linter-seo-geo-2026@thehumanintheloop-marketplace-claude
```

En Claude Desktop, usa `+ → Plugins → Add plugin`; los comandos `/plugin` solo funcionan dentro de la interfaz interactiva de Claude Code.

En Codex, registra el marketplace desde Plugins y busca `linter-seo-geo-2026`, o usa el botón de instalación de la [GitHub Page](https://mauricioperera.github.io/thehumanintheloop-marketplace-codex/).

Este repositorio se distribuye bajo la [licencia MIT](LICENSE). Los análisis de terceros y las marcas o activos de sus respectivos sitios conservan sus derechos y condiciones de uso.
