# Contribuir al marketplace

## Añadir un plugin

1. Crea `plugins/<nombre-del-plugin>/` usando un nombre minúsculo con guiones.
2. Añade `.claude-plugin/plugin.json` y `.codex-plugin/plugin.json` cuando el plugin sea multiplataforma.
3. Coloca las skills compartidas en `skills/<nombre-de-la-skill>/SKILL.md`.
4. Registra el plugin en `.claude-plugin/marketplace.json` y `.agents/plugins/marketplace.json`.
5. Actualiza la ficha correspondiente en `docs/index.html` o `docs/app.js`, según el origen de datos usado por el catálogo.
6. Mantén la categoría, versión, nombre visible y descripción sincronizados.

## Añadir un Design System Analysis

Cada análisis publicado debe incluir, como mínimo:

- `DESIGN.md` como contrato principal.
- `design-system.json` con tokens y estructura derivada.
- `validation-report.json` con resultados y advertencias.
- `index.html` como preview navegable.
- canonical, Open Graph, JSON-LD y entrada en `docs/sitemap.xml`.

Declara siempre la procedencia del sitio analizado y evita presentar un análisis externo como sistema oficial de la marca.

## Validación obligatoria

Desde la raíz del repositorio:

```powershell
python plugins/marketplace-validator/scripts/validate_marketplace.py .
python scripts/validate_catalog_metadata.py
python scripts/validate_analysis_metadata.py
node --check docs/app.js
git diff --check
```

El workflow de GitHub Actions debe pasar antes de hacer merge o publicar. No incluyas secretos, credenciales, artefactos de build ni archivos generados fuera de `docs/analyses/`.

## Pull requests

Describe qué se añadió, qué fuentes se utilizaron y qué validaciones ejecutaste. Los cambios de autoría, licencia, eliminación de plugins o publicación de activos de terceros requieren revisión explícita.

Para reportar un problema o proponer una mejora, utiliza las plantillas de **Issues** del repositorio. Para cambios de código, usa la plantilla de pull request y conserva la salida de los validadores en la descripción cuando sea relevante.

Para vulnerabilidades de seguridad, sigue [`SECURITY.md`](SECURITY.md) y no publiques detalles explotables en un issue.

Las contribuciones también deben respetar [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md).
