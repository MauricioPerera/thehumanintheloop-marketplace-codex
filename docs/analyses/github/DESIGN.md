---
name: github-homepage-analysis
version: 1.0.0
description: Análisis externo y reproducible del homepage público de GitHub; no es un sistema oficial de GitHub.
source: https://github.com/
colors: documented-in-design-system-json
typography: system-ui-and-github-monospace
rounded: 6px-controls-999px-pills
spacing: 4px-base-scale
components: header-navigation-hero-cards-callouts-footer
---

# GitHub Homepage — Design System Analysis

## Overview

Este documento describe el sistema visual observable en el homepage público de GitHub el 2 de agosto de 2026. Es un análisis externo para reconstrucción, auditoría y experimentación; no representa una especificación oficial ni incluye activos propietarios, marcas registradas o código de GitHub.

La página observada combina navegación global, propuesta de valor, registro por correo, llamadas a GitHub Copilot y bloques de producto para código, automatización, seguridad y colaboración. La fuente de verdad de los valores medibles está en `design-system.json`; este documento conserva también las decisiones de composición, comportamiento y validación.

## Contrato duro

Estos valores son medibles y deben permanecer estables al implementar una reproducción del análisis:

- El lienzo principal usa `{colors.canvasDefault}` y las superficies secundarias usan `{colors.canvasSubtle}` o `{colors.canvasInset}`.
- El texto principal usa `{colors.fgDefault}`; el texto secundario usa `{colors.fgMuted}`.
- El color de acción principal es `{colors.accent}`; un CTA oscuro puede usar `{colors.neutralEmphasis}` con texto `{colors.fgOnEmphasis}`.
- El borde por defecto usa `{colors.borderDefault}` y el estado positivo usa `{colors.success}`.
- La familia tipográfica de interfaz es `-apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif`; el texto de código usa `ui-monospace, SFMono-Regular, Menlo, Consolas, monospace`.
- Los controles y tarjetas usan `6px`; los elementos tipo píldora usan `999px`; los avatares son circulares.
- La escala de espaciado parte de 4px: 4, 8, 12, 16, 24, 32 y 48px.
- El contenedor de contenido no supera 1280px y mantiene gutters de 16px en viewport estrecho.
- Debe existir una jerarquía de un encabezado global, una zona hero, bloques de producto y un footer con enlaces.
- La interfaz debe ser usable desde 320px y cambiar de navegación horizontal a navegación compacta por debajo de 768px.

## Soft contract

Estas decisiones son inferencias visuales y pueden variar por locale, sesión, experimento, tema o fecha:

- El hero prioriza una frase declarativa grande, un párrafo corto y dos acciones primarias; el orden exacto puede cambiar.
- Las secciones de producto se presentan como bloques alternos de texto y visualización, con tarjetas de apoyo y superficies sutiles.
- Los nombres de tokens siguen la semántica de Primer para hacer el análisis interoperable, pero no implican que este documento sea la fuente oficial de Primer.
- El tono editorial es técnico, directo y orientado a resultados; los claims comerciales deben conservar su fuente y fecha al reutilizarse.
- El modo oscuro y las variantes regionales deben derivarse de tokens semánticos, no de valores de color copiados directamente a cada componente.

## Colors

| Token | Valor | Uso |
|---|---|---|
| `colors.canvasDefault` | `#FFFFFF` | Lienzo principal |
| `colors.canvasSubtle` | `#F6F8FA` | Banda o sección secundaria |
| `colors.canvasInset` | `#F6F8FA` | Paneles internos |
| `colors.fgDefault` | `#1F2328` | Texto principal |
| `colors.fgMuted` | `#59636E` | Texto de apoyo |
| `colors.fgOnEmphasis` | `#FFFFFF` | Texto sobre acción sólida |
| `colors.accent` | `#0969DA` | Enlaces y CTA de acción |
| `colors.accentMuted` | `#54AEFF` | Acento en fondos oscuros |
| `colors.neutralEmphasis` | `#24292F` | Acción de alto contraste |
| `colors.borderDefault` | `#D1D9E0` | Bordes y divisores |
| `colors.success` | `#1A7F37` | Confirmación y éxito |
| `colors.danger` | `#D1242F` | Error o riesgo |
| `colors.attention` | `#9A6700` | Advertencia |
| `colors.done` | `#8250DF` | Estado completado |
| `colors.sponsor` | `#BF3989` | Sponsorship |

## Typography

La escala mantiene lectura cómoda y contraste entre display, headings, cuerpo, labels y código:

| Rol | Tamaño | Peso | Line-height |
|---|---:|---:|---:|
| Display / hero | 48px | 700 | 1.1 |
| H2 de sección | 32px | 600 | 1.25 |
| H3 de componente | 24px | 600 | 1.3 |
| Body | 16px | 400 | 1.5 |
| Label | 14px | 600 | 1.4 |
| Code | 13px | 400 | 1.45 |

En viewport estrecho el display baja a 36px y los headings se ajustan a 24px sin modificar el orden semántico.

## Components

### Global header

Barra superior con identidad, navegación de producto/soluciones/recursos, búsqueda y acciones de autenticación. Estados mínimos: `default`, `expanded`, `compact`, `focus-visible`.

### Hero and primary CTA

Bloque de entrada con un heading de alto impacto, explicación breve, campo de email y botones de registro/producto. El campo debe conservar label accesible, estado `focus`, `invalid` y `disabled`.

### Feature section

Sección de producto con eyebrow, heading, body copy, enlace semántico y una visualización o tarjeta. Estados: `default`, `hover-link`, `loading`, `reduced-motion`.

### Product card and status callout

Tarjetas sobre `{colors.canvasSubtle}` con borde, icono, título, descripción y enlace. Los callouts de seguridad y automatización deben distinguir `info`, `success`, `attention` y `danger` sin depender solo del color.

### Footer

Bloque final de registro y navegación secundaria agrupada. En mobile, las columnas se apilan y los grupos mantienen headings navegables.

Los nombres anteriores son un inventario analítico. No se afirma que correspondan uno a uno con componentes internos de GitHub.

## Responsive

| Rango | Comportamiento |
|---|---|
| 320–543px | Header compacto, navegación colapsada, una columna, display 36px, CTAs apilados |
| 544–767px | Grilla flexible, tarjetas de dos columnas cuando el contenido lo permite |
| 768–1011px | Header regular, secciones de dos zonas y navegación horizontal |
| 1012–1279px | Contenedor amplio con gutters regulares y composición editorial completa |
| 1280–1399px | Contenedor máximo de 1280px y mayor aire entre bloques |
| 1400px+ | Variante wide con espacio exterior adicional, sin estirar el contenido |

El análisis adopta los rangos de layout documentados por Primer: narrow por debajo de 768px, regular desde 768px y wide desde 1400px. Deben respetarse `prefers-reduced-motion`, contraste suficiente, zoom del navegador y orientación vertical/horizontal.

## Provenance

- Fuente observada: [GitHub homepage](https://github.com/).
- Referencia de layout: [Primer responsive foundations](https://primer.style/product/getting-started/foundations/responsive) y [Primer layout foundations](https://primer.style/product/getting-started/foundations/layout/).
- Referencia de color semántico: [Primer color primitives](https://www.primer.style/product/primitives/color/).
- Fecha de observación: 2026-08-02.
- Los valores son una síntesis analítica; el sitio fuente es dinámico y puede variar por región, tema, experimento o autenticación.

## Validation Contract

### PASSED

- Todos los colores hardcoded del contrato tienen formato hexadecimal válido.
- `design-system.json` contiene tokens, componentes, breakpoints y procedencia.
- El preview expone colores, tipografía, componentes, estados, responsive behavior y fuentes.
- Existe un único H1 en el documento y la estructura separa contrato duro, contrato blando y validación.

### WARNING

- No se valida la identidad visual oficial de GitHub ni se redistribuyen sus activos.
- Los claims, copy, iconos y layout del homepage pueden cambiar; deben revalidarse antes de una implementación productiva.
- La validación no sustituye pruebas de accesibilidad, contraste, rendimiento ni revisión legal de marca.

### Criterios de aceptación

Una implementación pasa este contrato cuando conserva los tokens medibles, la jerarquía de componentes, los rangos responsive, estados accesibles y la procedencia declarada; cualquier desviación debe registrarse como decisión explícita.
