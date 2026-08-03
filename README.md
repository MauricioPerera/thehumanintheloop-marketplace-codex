# TheHumanInTheLoop Marketplace

Marketplace público de plugins, skills y Design System Analyses para Claude Code y Codex, creado por Mauricio Perera.

Catálogo actual: **16 plugins**, distribuido en dos manifests compatibles y una [GitHub Page navegable](https://mauricioperera.github.io/thehumanintheloop-marketplace-codex/). También puedes conocer el proyecto en el [canal The Human in the Loop](https://www.youtube.com/@Rckflr).

## Plugins disponibles

- `Auditor SEO/GEO 2026` (`linter-seo-geo-2026`): validador de contenido para buscadores y motores generativos.
- `Marketplace Validator` (`marketplace-validator`): valida manifests y sincronización Claude Code/Codex.
- `Design System Auditor` (`design-system-auditor`): genera contratos `DESIGN.md`, tokens y validadores.
- `Content Fact Checker` (`content-fact-checker`): exige fuentes, fechas y evidencia para afirmaciones.
- `Repo Quality Gate` (`repo-quality-gate`): revisa repositorios antes de commit, PR o release.
- `Technical Docs Linter` (`technical-docs-linter`): valida documentación, ejemplos, comandos y enlaces.
- `Accessibility Auditor` (`accessibility-auditor`): audita HTML, ARIA, formularios y teclado.
- `Privacy Risk Auditor` (`privacy-risk-auditor`): detecta PII, secretos y credenciales.
- `Release Readiness` (`release-readiness`): valida si el repositorio está listo para publicar.
- `Prompt Contract Linter` (`prompt-contract-linter`): valida prompts como contratos ejecutables.
- `Research Evidence Builder` (`research-evidence-builder`): construye matrices de evidencia.
- `Brand Voice Validator` (`brand-voice-validator`): valida tono y consistencia editorial.
- `API Contract Linter` (`api-contract-linter`): audita contratos OpenAPI y ejemplos.
- `Web Performance Auditor` (`web-performance-auditor`): audita carga y Core Web Vitals.
- `Dependency Risk Auditor` (`dependency-risk-auditor`): revisa dependencias y lockfiles.
- `Test Coverage Gate` (`test-coverage-gate`): valida evidencia de tests y cobertura.

## Categorías

El catálogo usa una taxonomía común en Claude Code, Codex y la GitHub Page:

- Content & Editorial
- Design Systems
- Marketplace & Quality
- Developer Tools
- Accessibility & UX
- Security & Privacy
- Research & Evidence
- AI & Prompt Engineering

La GitHub Page permite filtrar por categoría, buscar por nombre o capacidad, copiar instrucciones de instalación y abrir el código fuente de cada plugin.

## Estructura

- `.claude-plugin/marketplace.json`: catálogo compatible con Claude Code.
- `.agents/plugins/marketplace.json`: catálogo compatible con Codex.
- `plugins/`: un directorio por plugin.
- Cada plugin puede contener `.claude-plugin/plugin.json` y `.codex-plugin/plugin.json`; ambos reutilizan las mismas skills bajo `skills/`.
- `docs/analyses/`: resultados publicados de análisis visuales; cada entrada contiene `DESIGN.md`, `design-system.json`, `validation-report.json` y un preview navegable.
- `CONTRIBUTING.md`: flujo para proponer plugins y Design System Analyses.
- `CHANGELOG.md`: historial de capacidades publicadas.
- `SECURITY.md`: alcance y procedimiento para reportar vulnerabilidades.
- `CODE_OF_CONDUCT.md`: reglas de participación de la comunidad.

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

Antes de publicar, comprueba que la entrada exista en ambos manifests, que la ruta `source` apunte al directorio correcto y que la ficha visible esté actualizada en `docs/catalog.json`. El workflow [Marketplace Validation](https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex/actions/workflows/marketplace-validation.yml) ejecuta estas comprobaciones automáticamente.

## Validación local

Desde la raíz del repositorio:

```powershell
python plugins/marketplace-validator/scripts/validate_marketplace.py .
python scripts/validate_catalog_metadata.py
python scripts/validate_analysis_metadata.py
node --check docs/app.js
git diff --check
```

No publiques un plugin si la validación devuelve `[FAILED]` o si la ficha de catálogo no coincide con los manifests.

## Instalación

En Claude Code:

```text
claude plugin marketplace add MauricioPerera/thehumanintheloop-marketplace-codex
claude plugin install linter-seo-geo-2026@thehumanintheloop-marketplace-claude
```

En Claude Desktop, usa `+ → Plugins → Add plugin`; los comandos `/plugin` solo funcionan dentro de la interfaz interactiva de Claude Code.

En Codex, registra el marketplace desde Plugins y busca `linter-seo-geo-2026`, o usa el botón de instalación de la [GitHub Page](https://mauricioperera.github.io/thehumanintheloop-marketplace-codex/).

Para instalar otro plugin, reemplaza `linter-seo-geo-2026` por cualquiera de los nombres disponibles en la sección [Plugins disponibles](#plugins-disponibles). En la página, el botón **Pedir a Codex** prepara una conversación con el nombre exacto del plugin y **Claude** ofrece la instrucción equivalente para Claude Code.

## Design System Analyses publicados

Los análisis visuales se publican como resultados reutilizables, no como plugins generadores. Cada análisis incluye el contrato `DESIGN.md`, tokens estructurados, reporte de validación y un preview HTML integrado en el catálogo. Actualmente están disponibles desde la sección de diseños de la [GitHub Page](https://mauricioperera.github.io/thehumanintheloop-marketplace-codex/).

Este repositorio se distribuye bajo la [licencia MIT](LICENSE). Los análisis de terceros y las marcas o activos de sus respectivos sitios conservan sus derechos y condiciones de uso.
