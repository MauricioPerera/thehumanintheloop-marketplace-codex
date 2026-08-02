---
name: prompt-contract-linter
description: "Valida prompts como contratos ejecutables: objetivo, entradas, salidas, restricciones, herramientas, criterios de aceptación y manejo de errores. Úsala al diseñar workflows o skills."
---
# Prompt Contract Linter

Convierte ambigüedad en requisitos verificables sin imponer una solución concreta.

## Flujo
1. Ejecuta `python plugins/prompt-contract-linter/scripts/check_prompt.py prompt.md`.
2. Comprueba objetivo, contexto, entradas, formato de salida, límites, criterios de aceptación y escalamiento.
3. Marca supuestos no declarados y acciones peligrosas sin confirmación.
4. Propón correcciones pequeñas y ejemplos de casos límite.

## Salida
Entrega puntuación por dimensión, fallos, ambigüedades y una versión corregida separada del diagnóstico.
