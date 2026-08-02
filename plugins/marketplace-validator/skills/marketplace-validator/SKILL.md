---
name: marketplace-validator
description: Valida la estructura, manifests y sincronización de marketplaces para Claude Code y Codex. Úsala antes de publicar, añadir plugins, cambiar rutas o revisar un repositorio de marketplace.
---

# Marketplace Validator

Audita un repositorio dual sin modificarlo. Ejecuta el validador determinista y después revisa cualquier diferencia entre `.claude-plugin/marketplace.json`, `.agents/plugins/marketplace.json`, los directorios de plugins y `docs/catalog.json`.

## Flujo

1. Identifica la raíz del repositorio y no confíes en archivos generados como única fuente.
2. Ejecuta `python plugins/marketplace-validator/scripts/validate_marketplace.py .`.
3. Comprueba que cada plugin tenga ambos manifests cuando sea multiplataforma:
   - `plugins/<name>/.claude-plugin/plugin.json`
   - `plugins/<name>/.codex-plugin/plugin.json`
4. Comprueba que las skills compartidas estén bajo `plugins/<name>/skills/`.
5. Compara nombres, descripciones, versiones y categorías con `docs/catalog.json`.
6. Reporta `[PASSED]` o `[FAILED]`, archivos afectados y cambios exactos. No publiques ni instales nada sin confirmación.

## Reglas

- Las rutas Claude usan `source: "./plugins/<name>"`.
- Las rutas Codex usan el objeto `source.local.path` relativo.
- No incluyas secretos, tokens ni credenciales.
- Si un plugin solo soporta una plataforma, decláralo explícitamente en el informe.
- Un error de manifest o de ruta bloquea la publicación.

## Salida

Entrega el JSON del script, un resumen humano y un plan de corrección ordenado por severidad.
