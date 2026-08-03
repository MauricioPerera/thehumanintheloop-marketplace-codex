## Qué cambia

Describe el plugin, análisis, validador o documentación modificada.

## Fuentes y procedencia

- Plugin o análisis afectado:
- Fuentes utilizadas:
- ¿Incluye activos de terceros? Sí / No

## Checklist

- [ ] Actualicé ambos manifests cuando corresponde.
- [ ] Sincronicé la ficha del catálogo y las categorías.
- [ ] Ejecuté `python plugins/marketplace-validator/scripts/validate_marketplace.py .`.
- [ ] Ejecuté `python scripts/validate_catalog_metadata.py`.
- [ ] Ejecuté `python scripts/validate_analysis_metadata.py` si modifiqué un análisis.
- [ ] Ejecuté `node --check docs/app.js`.
- [ ] No incluí secretos, credenciales ni archivos generados fuera de las rutas permitidas.
