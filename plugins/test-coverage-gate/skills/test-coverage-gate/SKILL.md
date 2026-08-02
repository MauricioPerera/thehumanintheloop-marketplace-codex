---
name: test-coverage-gate
description: Valida evidencia de pruebas, cobertura y criterios de calidad antes de publicar código. Úsala antes de commit final, PR, release o despliegue.
---
# Test Coverage Gate

No confunde porcentaje de cobertura con calidad completa: revisa también tests fallidos, suites ejecutadas y casos críticos.

## Flujo
1. Ejecuta `python plugins/test-coverage-gate/scripts/check_tests.py .`.
2. Localiza configuración, reportes y suites de pruebas.
3. Ejecuta los comandos existentes solo cuando sean seguros y documenta su resultado.
4. Marca como pendiente cualquier cobertura no verificable.

## Salida
Entrega suites, cobertura, fallos, evidencia, umbral y estado del gate.
