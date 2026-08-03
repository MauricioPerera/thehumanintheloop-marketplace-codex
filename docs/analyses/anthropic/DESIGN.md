---
name: anthropic-homepage-analysis
version: 1.0.0
description: Análisis externo y reproducible del homepage público de Anthropic; no es un sistema oficial de Anthropic.
source: https://www.anthropic.com/
colors: documented-in-design-system-json
typography: warm-editorial-sans
rounded: 4px-controls-12px-cards
spacing: 4px-base-scale
components: global-nav-hero-research-card-product-groups-footer
---

# Anthropic Homepage — Design System Analysis

## Overview

Este documento analiza el homepage público de Anthropic observado el 2 de agosto de 2026. La experiencia comunica investigación y productos de IA orientados a seguridad, y organiza productos Claude, modelos, soluciones, plataforma, recursos, programas y políticas. Es un análisis externo para auditoría y reconstrucción; no es una especificación oficial de Anthropic.

El lenguaje y los enlaces cambian con la evolución de productos y políticas. No se redistribuyen logos, imágenes, fuentes, ilustraciones ni textos completos de Anthropic.

## Contrato duro

- El lienzo usa `{colors.canvas}` y las superficies suaves usan `{colors.surface}`.
- El texto principal usa `{colors.ink}`; el auxiliar y metadata usan `{colors.muted}`.
- Las acciones usan `{colors.brand}` y el foco usa `{colors.accent}`.
- La navegación global separa Research, Products, Business, Developers y Company, con CTA a Claude/Login.
- El hero combina headline de seguridad/IA, párrafo de propósito y enlaces hacia research y products.
- La sección de hard questions usa copy explicativo y acción Learn more.
- Latest releases usa tarjetas con categoría, título y enlace editorial.
- El footer agrupa Products, Models, Solutions, Claude Platform, Resources, Programs, Help and security, Company y políticas.
- Controles usan radio 4px; cards editoriales hasta 12px; touch targets mínimos de 44px.

## Soft contract

Las siguientes decisiones son `inferido` a partir de la estructura observable:

- La paleta cálida y el tono editorial buscan transmitir calma y responsabilidad frente a la velocidad del sector (`inferido`).
- La seguridad aparece como promesa estructural, no como módulo añadido al final (`inferido`).
- La taxonomía de enlaces convierte la página corporativa en un mapa de ecosistema (`inferido`).
- Research, policy, economic impacts y releases construyen evidencia antes de la conversión de producto (`inferido`).
- “Hard questions” funciona como marco narrativo para problemáticas técnicas y sociales (`inferido`).

## Colors

| Token | Valor | Uso |
|---|---|---|
| `colors.canvas` | `#F7F5F0` | Fondo editorial cálido |
| `colors.surface` | `#EDEAE3` | Bandas y cards suaves |
| `colors.surfaceRaised` | `#FFFFFF` | Cards elevadas |
| `colors.ink` | `#171716` | Texto principal |
| `colors.muted` | `#686761` | Texto auxiliar |
| `colors.brand` | `#C45A3C` | CTA y acento cálido |
| `colors.accent` | `#285C4D` | Enlaces y foco |
| `colors.border` | `#D8D4CB` | Divisores |
| `colors.success` | `#397A54` | Confirmación |
| `colors.error` | `#B43D36` | Error |

Los valores cromáticos son un snapshot analítico y deben verificarse contra CSS computado antes de producción. Medir contraste de CTA y enlaces en cada estado.

## Typography

| Rol | Familia | Tamaño | Peso | Line-height |
|---|---|---:|---:|---:|
| Hero heading | Sans/editorial display | 56px | 500 | 1.05 |
| Section heading | Sans/editorial display | 36px | 500 | 1.15 |
| Card heading | Sans-serif interface | 20px | 600 | 1.3 |
| Body | Sans-serif interface | 17px | 400 | 1.55 |
| Metadata | Sans-serif interface | 13px | 500 | 1.4 |
| Code / reference | ui-monospace, monospace | 13px | 400 | 1.45 |

La fuente exacta de Anthropic no se afirma como verificada ni redistribuible. Una adaptación independiente debe usar una fuente con licencia compatible.

## Components

### Global navigation

Navegación por audiencias, Foundation, Claude, Login y submenús. Estados: `default`, `hover`, `focus-visible`, `menu-open`, `compact`.

### Hero mission block

Headline sobre research/product safety, párrafo de propósito y acciones. Estados: `default`, `hover`, `focus-visible`, `reduced-motion`.

### Hard questions section

Bloque editorial con heading, explicación y Learn more. Estados: `default`, `hover`, `focus-visible`, `loading`.

### Release card

Card de anuncio, alignment science, education o economic research con título y metadata. Estados: `default`, `hover`, `focus-visible`, `featured`.

### Product and solution groups

Listas de Claude, modelos, sectores y plataforma. Estados: `default`, `hover`, `focus-visible`, `expanded`, `stacked-mobile`.

### Policy/footer group

Políticas, seguridad, privacidad, disponibilidad, compañía y programas. Estados: `default`, `hover`, `focus-visible`, `collapsed-mobile`.

## Layout and spacing

- Header: ancho completo, padding lateral 24px desktop y 16px mobile.
- Hero: copy con max-width aproximado de 800px y amplio espacio vertical.
- Editorial cards: grid flexible con gap de 16px y metadata separada del título.
- Product groups: columnas con gap de 32px desktop y grupos verticales mobile.
- Footer: separación de 48px entre bloques principales y 8px entre enlaces.

## Responsive

| Rango | Comportamiento |
|---|---|
| 320–543px | Header compacto, hero vertical, cards apiladas y footer por grupos |
| 544–767px | Grid flexible, navegación que envuelve y cards de dos columnas si cabe |
| 768–1011px | Header regular, hero amplio y secciones de dos columnas |
| 1012–1279px | Grid editorial amplio y footer en columnas |
| 1280px+ | Mayor aire exterior sin estirar la columna de lectura |

Probar 320px, 768px y 1280px, además de teclado, zoom, reduced motion, contraste y foco en submenús.

## Do's and Don'ts

- Do: separar research, products, policy y resources con headings y metadata.
- Do: hacer visible el foco y mantener legibles los bloques editoriales.
- Do: tratar seguridad y políticas como navegación de primer nivel cuando corresponda.
- Don't: copiar logo, fotografías, ilustraciones, tipografías o textos de Anthropic sin autorización.
- Don't: presentar políticas o claims dinámicos como tokens permanentes.
- Don't: esconder grupos de footer en un acordeón sin estado anunciado.

## Provenance

- Fuente observada: [Anthropic homepage](https://www.anthropic.com/).
- Fecha de observación: 2026-08-02.
- Evidencia visible: hero de AI research/products/safety, hard questions, Latest releases, Products, Models, Solutions, Claude Platform, Resources, Programs, Help and security, Company y políticas.
- Límite: productos, modelos, enlaces, políticas y copy cambian por fecha, locale y navegación.

## Validation Contract

### PASSED

- El documento separa contrato duro, contrato blando, componentes, estados, responsive y procedencia.
- `design-system.json` contiene tokens, breakpoints y componentes derivados del contrato.
- El preview muestra hero, research, cards de releases, grupos de producto, footer, tokens y validación.
- Se contemplan accesibilidad de submenús, touch targets y reduced motion.

### WARNING

- Los colores son snapshot analítico y requieren medición CSS para producción.
- El contenido de productos y políticas cambia rápidamente.
- Este no es un sistema oficial de Anthropic ni una autorización para redistribuir sus activos.

### Criterios de aceptación

Una implementación pasa cuando conserva la jerarquía de seguridad, research, productos, releases, políticas, navegación accesible, tokens y responsive behavior; los activos de marca deben sustituirse por recursos autorizados.
