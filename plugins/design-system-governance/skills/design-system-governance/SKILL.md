---
name: design-system-governance
description: Mantiene y valida un Design System existente después de su auditoría. Úsala cuando el usuario pida contratos evolutivos, tokens, componentes, drift entre diseño y código, reglas de contribución, accesibilidad o criterios de aceptación para cambios visuales.
---

# Design System Governance

Mantén un sistema de diseño como un contrato vivo, trazable y revisable. Este skill complementa `design-system-auditor`: el auditor descubre y documenta; este skill gobierna cambios posteriores y detecta desviaciones.

## Principios

- Declara la fuente, fecha observada, viewport, alcance y limitaciones.
- Separa hechos observados, inferencias, decisiones aprobadas y recomendaciones.
- No presentes un análisis externo como el sistema oficial de una marca.
- No inventes tokens, componentes, estados, reglas de accesibilidad ni decisiones de diseño.
- Prefiere cambios pequeños, reversibles y verificables.
- Marca como desconocido lo que no pueda comprobarse en la fuente disponible.

## Flujo

1. Define el alcance: producto, rutas, componentes, repositorio y fuente de diseño.
2. Lee el contrato existente (`DESIGN.md`, `design-system.json`, tokens, documentación y tests) antes de proponer cambios.
3. Registra procedencia, fecha, viewport, herramientas usadas y evidencia disponible.
4. Compara la implementación actual con el contrato en tokens, tipografía, espaciado, color, radios, sombras, motion, layout y responsive behavior.
5. Revisa componentes y estados: default, hover, focus-visible, active, disabled, loading, error, empty y responsive cuando apliquen.
6. Evalúa accesibilidad observable: contraste, foco, teclado, nombres accesibles, targets táctiles, idioma y movimiento reducido.
7. Clasifica cada hallazgo como `match`, `drift`, `missing`, `unknown` o `needs-decision`.
8. Propón el cambio mínimo con evidencia, impacto, riesgo, archivos afectados y criterio de aceptación.
9. Actualiza el contrato solo cuando la decisión esté respaldada por la fuente o aprobada explícitamente.
10. Ejecuta validadores deterministas y reporta fallos, advertencias y limitaciones.

## Contrato mínimo

Cuando se cree o actualice un contrato, conserva como mínimo:

- `source`: URL o ruta, fecha observada y procedencia.
- `tokens`: color, tipografía, spacing, radius, shadow, motion y z-index cuando existan.
- `components`: variantes, estados, contenido mínimo, anatomía y reglas responsive.
- `governance`: propietario, regla de cambio, compatibilidad y versión.
- `validation`: checks deterministas, comandos y resultado.
- `warnings`: incertidumbres, áreas no observadas y decisiones pendientes.

## Formato de revisión

Entrega una tabla o lista con:

- ID del hallazgo.
- Evidencia y fuente.
- Estado (`match`, `drift`, `missing`, `unknown`, `needs-decision`).
- Severidad y alcance.
- Recomendación reversible.
- Criterio de aceptación verificable.

No conviertas automáticamente una recomendación en cambio de código. Si el usuario pide implementación, separa primero el contrato aprobado de los cambios derivados.

## Gates antes de publicar

- Ambos manifests son válidos y tienen el mismo nombre y versión.
- Los tokens usados por ejemplos o previews existen en el contrato.
- Cada componente nuevo declara variantes y estados relevantes.
- Las reglas responsive no contradicen el comportamiento observado.
- Los hallazgos `unknown` no se presentan como conformidad.
- Los enlaces de procedencia funcionan o se documentan como no verificables.
- Los validadores pasan y el reporte conserva advertencias.

## No hacer

- No rediseñar por preferencia estética.
- No asumir que una captura representa todos los breakpoints.
- No declarar conformidad WCAG completa a partir de una inspección parcial.
- No borrar tokens o componentes sin evidencia de obsolescencia y confirmación.
- No publicar un sistema de terceros como oficial.

## Salida recomendada

Entrega `DESIGN.md` actualizado, el contrato estructurado, un reporte de drift y una lista priorizada de cambios. Incluye comandos de validación, evidencia, incertidumbres y decisiones pendientes.
