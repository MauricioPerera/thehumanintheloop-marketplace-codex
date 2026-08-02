---
name: web-performance-auditor
description: Audita rendimiento web, recursos bloqueantes, Core Web Vitals y riesgos de carga. Úsala al revisar sitios publicados o cambios frontend.
---
# Web Performance Auditor

Combina métricas reales y análisis estático; no inventes valores de laboratorio.

## Flujo
1. Ejecuta `python plugins/web-performance-auditor/scripts/check_assets.py ruta`.
2. Cuando haya navegador disponible, mide LCP, INP, CLS, FCP y TBT.
3. Identifica imágenes grandes, scripts bloqueantes, fuentes, dependencias y cambios de layout.
4. Separa mediciones de recomendaciones.

## Salida
Entrega métrica, valor, umbral, evidencia, impacto y corrección priorizada.
