---
name: design-system-auditor
description: Genera o audita Design System Analyses a partir de un sitio publicado o proyecto local. Úsala cuando el usuario pida DESIGN.md, tokens, componentes, procedencia, validadores o un preview navegable.
---

# Design System Auditor

Produce un análisis reproducible y verificable, no una copia visual superficial. Separa observaciones del sitio, decisiones inferidas y reglas duras que deben validar una implementación.

## Flujo

1. Inspecciona la fuente autorizada: URL pública, proyecto local o ambos.
2. Registra procedencia, fecha, viewport y limitaciones del análisis.
3. Extrae tokens de color, tipografía, espaciado, radios, sombras y motion.
4. Documenta layout, responsive behavior, componentes, estados y contenido estructural.
5. Genera `DESIGN.md` como fuente de verdad y `design-system.json` como contrato estructurado.
6. Incluye exactamente un H1 y las secciones `Design Tokens`, `Components` y `Validation Contract`.
7. Ejecuta `python plugins/design-system-auditor/scripts/validate_design.py DESIGN.md --json design-system.json`.
8. Genera un `validation-report.json` y, cuando se solicite, un preview navegable derivado del contrato.

## Contrato

- Distingue hechos observados, inferencias y recomendaciones.
- No presentes una marca o diseño de terceros como oficial.
- Cada componente debe declarar variantes, estados, contenido mínimo y reglas responsive.
- Cada token utilizado en el preview debe existir en el contrato.
- Los validadores deben poder fallar de forma determinista.

## Salida

Entrega `DESIGN.md`, `design-system.json`, `validation-report.json` y preview si fue solicitado. Reporta evidencia, incertidumbres y fallos antes de aplicar cambios al proyecto.
