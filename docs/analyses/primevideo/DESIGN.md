---
name: primevideo-homepage-analysis
version: 1.0.0
description: Análisis externo y reproducible del homepage público de Prime Video; no es un sistema oficial de Amazon.
source: https://www.primevideo.com/
colors: documented-in-design-system-json
typography: sans-serif-streaming-ui
rounded: 4px-controls-8px-cards
spacing: 4px-base-scale
components: streaming-header-hero-content-rail-plan-card-footer
---

# Prime Video Homepage — Design System Analysis

## Overview

Este documento analiza la experiencia pública de Prime Video observada el 2 de agosto de 2026. La fuente combina navegación de películas, series, deportes, TV en vivo y suscripciones con un hero editorial, rails de catálogo y promociones de prueba o membresía. Es un análisis externo para auditoría y reconstrucción; no es una especificación oficial de Amazon o Prime Video.

El contenido observado incluye variaciones por país, idioma, edad, sesión, derechos de distribución y suscripción. No se redistribuyen logos, key art, imágenes, nombres de obras ni textos completos de la fuente.

## Contrato duro

- El lienzo usa `{colors.canvas}` y las superficies de navegación o cards usan `{colors.surface}` y `{colors.surfaceRaised}`.
- El texto principal usa `{colors.ink}`; el texto auxiliar y metadatos usan `{colors.muted}`.
- El CTA de marca usa `{colors.brand}`; el foco y enlaces de acción deben mantener contraste visible.
- El header separa Browse, Subscriptions, Search, idioma, cuenta y Join Prime; en mobile se convierte en menú compacto.
- El hero combina imagen o gradiente, título, metadato, clasificación, descripción y CTA; el arte real queda fuera del entregable.
- Las rails muestran tarjetas con etiquetas como nuevo, trending, top o leaving soon y deben ofrecer una alternativa de teclado.
- Los controles usan radio 4px; cards y paneles usan 8px; chips de estado usan 999px.
- Spacing base de 4px, gutters de 16px mobile y 24px desktop; CTAs con min-height de 44px.
- El layout debe sostener hero editorial, rails de catálogo y bloques de suscripción en una columna móvil y varias columnas desktop.

## Soft contract

Las siguientes decisiones son `inferido` a partir de la estructura observable:

- El azul oscuro y el negro generan una experiencia de entretenimiento premium y cinematográfica (`inferido`).
- Las etiquetas de ranking y disponibilidad reducen la fricción de elección (`inferido`).
- La coexistencia de Browse, Subscriptions y Join Prime mezcla descubrimiento con conversión (`inferido`).
- Las categorías de deportes y Live TV amplían el modelo mental más allá de películas y series (`inferido`).
- La localización visible funciona como una decisión estructural y no solo como una preferencia de usuario (`inferido`).

## Colors

| Token | Valor | Uso |
|---|---|---|
| `colors.canvas` | `#0F171E` | Fondo de streaming |
| `colors.surface` | `#1A242F` | Header y paneles |
| `colors.surfaceRaised` | `#233243` | Hover y cards elevadas |
| `colors.ink` | `#FFFFFF` | Texto principal |
| `colors.muted` | `#A8B3BF` | Metadatos y copy auxiliar |
| `colors.brand` | `#00A8E1` | CTA y marca de acción |
| `colors.accent` | `#90D4F7` | Estado activo y foco claro |
| `colors.border` | `#3A4A5A` | Bordes y separadores |
| `colors.success` | `#65C466` | Confirmación |
| `colors.error` | `#E5484D` | Error |

Contraste de referencia: `{colors.ink}` sobre `{colors.canvas}` supera 15:1; `{colors.muted}` sobre `{colors.canvas}` requiere verificación por tamaño; `{colors.brand}` se debe medir antes de usarlo como texto pequeño.

## Typography

| Rol | Familia | Tamaño | Peso | Line-height |
|---|---|---:|---:|---:|
| Hero heading | Sans-serif de interfaz | 40px | 700 | 1.1 |
| Section heading | Sans-serif de interfaz | 24px | 700 | 1.25 |
| Card title | Sans-serif de interfaz | 16px | 600 | 1.3 |
| Body | Sans-serif de interfaz | 16px | 400 | 1.5 |
| Metadata / label | Sans-serif de interfaz | 13px | 600 | 1.4 |
| Code / reference | ui-monospace, monospace | 13px | 400 | 1.45 |

La familia exacta de Prime Video no se afirma como verificada ni redistribuible. Una implementación propia debe usar una sans-serif con licencia compatible.

## Components

### Streaming header

Navegación para Home, Movies, TV shows, Sports, Live TV, Subscriptions, búsqueda, idioma, cuenta y Join Prime. Estados: `default`, `hover`, `focus-visible`, `compact`, `menu-open`, `language-open`.

### Hero title block

Hero con artwork, título, descripción, clasificación, estado de disponibilidad y CTA. Estados: `default`, `loading`, `hover`, `focus-visible`, `subscription-required`.

### Content rail and rank card

Rail horizontal para Top 10, Top TV, trending, leaving soon y categorías. Estados: `default`, `hover`, `focus-visible`, `loading`, `empty`, `unavailable`.

### Subscription CTA

Bloque que comunica prueba, suscripción, canal o compra. Estados: `default`, `recommended`, `selected`, `disabled`, `error`.

### Footer navigation

Enlaces de ayuda, dispositivos, idioma, cuenta y legal. Estados: `default`, `hover`, `focus-visible`, `stacked-mobile`.

## Layout and spacing

- Header: altura aproximada de 64px desktop y 56px mobile.
- Hero: copy con max-width aproximado de 520px y overlay para preservar legibilidad sobre el artwork.
- Rail: gap de 12px, cards mínimas de 160px mobile y 220px desktop cuando el contenido lo permite.
- Card: superficie oscura, padding 12–16px y borde o separación visible.
- CTA: min-height 44px, padding horizontal 16px y radio 4px.
- Footer: grupos de enlaces separados por 24px y sin overflow horizontal.

## Responsive

| Rango | Comportamiento |
|---|---|
| 320–543px | Header compacto, hero vertical, rails desplazables y CTAs de ancho disponible |
| 544–767px | Rails flexibles y hero de dos zonas cuando el ancho lo permite |
| 768–1011px | Navegación regular, hero amplio y rail de varias cards |
| 1012–1279px | Mayor densidad de catálogo y bloques auxiliares en columnas |
| 1280px+ | Hero limitado, rails amplias y espacio exterior sin estirar la lectura |

Probar 320px, 768px y 1280px, además de teclado, zoom, reduced motion, alto contraste y navegación de rails sin depender solo del gesto táctil.

## Do's and Don'ts

- Do: indicar si el contenido está incluido, requiere suscripción, prueba, compra o canal.
- Do: anunciar ranking, edad, idioma, subtítulos y disponibilidad con texto accesible.
- Do: ofrecer controles de rail visibles y una alternativa de teclado.
- Don't: copiar artwork, logos, nombres o textos de Amazon/Prime Video sin permiso.
- Don't: esconder condiciones de prueba, pago, renovación o disponibilidad regional.
- Don't: usar autoplay o animación como requisito para entender un título.

## Provenance

- Fuente observada: [Prime Video](https://www.primevideo.com/).
- Fecha de observación: 2026-08-02.
- Evidencia visible: navegación Browse, Movies, TV shows, Sports, Live TV, Subscriptions, búsqueda, idioma, cuenta, Join Prime, hero, Top 10, Top TV, rails y estados de suscripción.
- Límite: catálogo, idioma, precios, derechos, clasificación y promociones cambian por país, sesión y fecha.

## Validation Contract

### PASSED

- El documento contiene contrato duro, contrato blando, componentes, estados, responsive y procedencia.
- `design-system.json` contiene tokens, breakpoints y componentes derivados del contrato.
- El preview muestra hero, rails, suscripción, tokens y estado de validación sin reutilizar assets.
- Se contemplan disponibilidad, accesibilidad de rails, touch targets y reduced motion.

### WARNING

- El contenido y las ofertas de Prime Video son dinámicos y regionales.
- La clasificación, idioma, precio y disponibilidad deben revalidarse antes de una implementación real.
- Este no es un sistema oficial de Amazon o Prime Video ni una autorización para redistribuir sus activos.

### Criterios de aceptación

Una implementación pasa cuando conserva la jerarquía de descubrimiento, hero, rails, estados de disponibilidad, suscripción transparente, accesibilidad y responsive behavior; los activos de marca deben sustituirse por recursos licenciados.
