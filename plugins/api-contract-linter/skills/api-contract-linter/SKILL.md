---
name: api-contract-linter
description: Audita contratos OpenAPI y documentación de APIs para detectar rutas incompletas, esquemas inconsistentes, respuestas sin ejemplos y cambios incompatibles.
---
# API Contract Linter

Valida el contrato declarado; no sustituye pruebas de integración contra un servidor real.

## Flujo
1. Localiza `openapi.yaml`, `openapi.json` o contratos equivalentes.
2. Ejecuta `python plugins/api-contract-linter/scripts/check_openapi.py contrato.json`.
3. Comprueba versión, paths, operations, responses, schemas y ejemplos.
4. Marca cambios breaking y confirma compatibilidad con clientes documentados.

## Salida
Entrega regla, ruta, método, evidencia, severidad y corrección propuesta.
