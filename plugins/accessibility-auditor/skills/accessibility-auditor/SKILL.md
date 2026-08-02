---
name: accessibility-auditor
description: Audita HTML y CSS para detectar problemas de accesibilidad en estructura, nombres accesibles, formularios, contraste y teclado. Úsala al revisar sitios o componentes web.
---
# Accessibility Auditor

Combina análisis estático con pruebas en navegador cuando estén disponibles. No declares conformidad WCAG completa solo con heurísticas.

## Flujo
1. Ejecuta `python plugins/accessibility-auditor/scripts/check_html.py <ruta>`.
2. Revisa landmarks, headings, `alt`, labels, botones, enlaces, foco visible y atributos ARIA.
3. Comprueba contraste con herramientas visuales cuando sea posible.
4. Clasifica bloqueantes, problemas serios y recomendaciones.

## Salida
Entrega estado, criterio afectado, elemento, evidencia y corrección concreta. Indica qué necesita una prueba manual.
