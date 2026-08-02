---
name: technical-docs-linter
description: Audita README, documentación API y ejemplos para detectar secciones faltantes, enlaces rotos y comandos inconsistentes. Úsala antes de publicar documentación técnica.
---
# Technical Docs Linter

Valida documentación contra el código y reporta contradicciones; no inventes APIs ni ejemplos.

## Flujo
1. Localiza README, docs, contratos y archivos de ejemplo.
2. Ejecuta `python plugins/technical-docs-linter/scripts/check_docs.py .`.
3. Comprueba comandos, rutas, variables de entorno, enlaces y nombres de archivos.
4. Marca como `NEEDS_REVIEW` lo que requiera ejecutar código o consultar un servicio externo.

## Salida
Entrega una tabla con archivo, regla, estado, evidencia y corrección propuesta.
