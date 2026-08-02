---
name: mercado-libre-mexico-homepage-analysis
version: 1.0.0
description: Design System Analysis del homepage público de Mercado Libre México; análisis externo, no sistema oficial.
source: https://www.mercadolibre.com.mx/
colors:
  primary: "#FFE600"
  surface: "#FFFFFF"
  pageBackground: "#EBEBEB"
  text: "#333333"
  textStrong: "#000000"
  textMuted: "#666666"
  line: "#E6E6E6"
  blue: "#3483FA"
  blueFocus: "#2968C8"
  blueText: "#1259C3"
  green: "#00A650"
  red: "#F23D4F"
  orange: "#FF7733"
  softGray: "#F5F5F5"
  softBlue: "#E5F0FF"
  softYellow: "#FFF1CB"
typography:
  body: {fontFamily: "Proxima Nova, -apple-system, Roboto, Arial, sans-serif", fontSize: "16px", fontWeight: 400, lineHeight: 1.4}
  label: {fontFamily: "Proxima Nova, -apple-system, Roboto, Arial, sans-serif", fontSize: "14px", fontWeight: 400, lineHeight: 1.25}
  labelStrong: {fontFamily: "Proxima Nova, -apple-system, Roboto, Arial, sans-serif", fontSize: "14px", fontWeight: 600, lineHeight: 1.25}
  cardTitle: {fontFamily: "Proxima Nova, -apple-system, Roboto, Arial, sans-serif", fontSize: "16px", fontWeight: 600, lineHeight: "22px"}
  price: {fontFamily: "Proxima Nova, -apple-system, Roboto, Arial, sans-serif", fontSize: "24px", fontWeight: 400, lineHeight: 1.1}
  small: {fontFamily: "Proxima Nova, -apple-system, Roboto, Arial, sans-serif", fontSize: "12px", fontWeight: 400, lineHeight: "15px"}
rounded: {input: "2px", message: "3px", card: "4px", control: "6px", tag: "8px", circle: "999px"}
spacing: {xxs: "2px", xs: "4px", sm: "8px", md: "12px", lg: "16px", xl: "20px", section: "24px", carouselGap: "20px", navHorizontal: "10px", contentMax: "1200px"}
components:
  site-header: {backgroundColor: "{colors.primary}", height: "100px", padding: "8px 10px", width: "100%"}
  search-input: {backgroundColor: "{colors.surface}", textColor: "{colors.textStrong}", borderColor: "{colors.blue}", rounded: "{rounded.input}", height: "40px", padding: "10px 60px 10px 15px", typography: "{typography.body}"}
  primary-button: {backgroundColor: "{colors.blue}", textColor: "{colors.surface}", rounded: "{rounded.control}", padding: "10px 16px", typography: "{typography.labelStrong}"}
  product-card: {backgroundColor: "{colors.surface}", textColor: "{colors.text}", borderColor: "{colors.line}", rounded: "{rounded.card}", padding: "16px"}
  benefit-card: {backgroundColor: "{colors.surface}", textColor: "{colors.textStrong}", rounded: "{rounded.card}", padding: "16px"}
  status-tag: {backgroundColor: "{colors.green}", textColor: "{colors.surface}", rounded: "{rounded.tag}", padding: "2px 4px", typography: "{typography.small}"}
---

# Mercado Libre México — Design System Analysis

## 1. Overview

Análisis del homepage público observado el 2 de agosto de 2026 en desktop y mobile. La página articula descubrimiento comercial, acceso a cuenta, búsqueda, promociones, categorías, recomendaciones y beneficios ecosistémicos dentro de una superficie gris clara con header amarillo.

### Provenance and scope

- Fuente: https://www.mercadolibre.com.mx/
- País/locale observado: México, `es-MX`, sitio `MLM`.
- Evidencia: HTML server-rendered, CSS público de navegación/home/recommendations y render visual de la URL.
- Módulos de home declarados por la propia página: 11.
- Límite: el contenido promocional, inventario, precios, campañas, banners e imágenes cambian dinámicamente. Se documenta el sistema visual, no el contenido comercial actual.
- Propiedad intelectual: esto es un análisis externo. No es el sistema oficial de Mercado Libre ni autoriza reutilizar marca, logo, fuentes propietarias, campañas o imágenes.

## 2. Hard Contract

Valores observados: header amarillo `#FFE600` con altura desktop de `100px`; navegación con ancho máximo de `1220px`; input de búsqueda de `40px`; fondo general `#EBEBEB`; tarjetas blancas con borde `rgba(0,0,0,.1)` y sombra `0 1px 1px 0 rgba(0,0,0,.1)`; Proxima Nova en pesos 300, 400 y 600; cards de categoría de `270px × 100px` en desktop; gap de carrusel de `20px`; y focus ring `#2968C8` con halo `rgba(65,137,230,.3)`.

## 3. Soft Contract

Inferido a partir de la repetición visual: el sistema busca reducir fricción en una misión de compra masiva. El amarillo identifica el entorno de marca; el azul indica acción y navegación; el verde comunica beneficio o estado positivo; el rojo queda reservado para error/urgencia. La jerarquía prioriza búsqueda, acceso y precio antes que ornamentación. Las tarjetas deben sentirse confiables y densas, pero separadas por espacio suficiente para escaneo rápido.

## 4. Colors

| Token | Value | Role | Evidence |
| --- | --- | --- | --- |
| `primary` | `#FFE600` | Header y superficie de marca | navigation CSS `.nav-header` |
| `blue` | `#3483FA` | Acción primaria y foco de inputs | navigation/home CSS |
| `blueFocus` | `#2968C8` | Focus ring y enlaces de alta prioridad | focus indicator CSS |
| `green` | `#00A650` | Envío gratis, beneficios y estados positivos | dynamic-access/recommendations CSS |
| `red` | `#F23D4F` | Error/alerta | home CSS |
| `pageBackground` | `#EBEBEB` | Canvas de módulos | render/home layout |
| `surface` | `#FFFFFF` | Cards, search y contenido | navigation/home CSS |
| `text` | `#333333` | Texto de producto y contenido | recommendations CSS |
| `textMuted` | `#666666` | Placeholder y metadata | navigation CSS |

Contrast is state-dependent: `#333333` sobre `#FFFFFF` is approximately `12.63:1`; `#3483FA` sobre `#FFFFFF` is approximately `3.52:1`, so blue should not carry small text as the sole contrast cue. Runtime sampling is still required for every component state.

## 5. Typography

The public CSS loads Proxima Nova in light, regular and semibold weights. Fallback is `-apple-system, Roboto, Arial, sans-serif`.

| Role | Size | Weight | Line-height | Usage |
| --- | --- | --- | --- | --- |
| Body | `16px` | 400 | `1.4` | Search and general copy |
| Label | `14px` | 400 | `1.25` | Navigation and metadata |
| Strong label | `14px` | 600 | `1.25` | CTA and card emphasis |
| Card title | `16px` | 600 | `22px` | Category/product titles |
| Price | `24px` | 400 | `1.1` | Product pricing |
| Small metadata | `12px` | 400 | `15px` | Tags and secondary info |

## 6. Navigation and search

The header is a yellow `100px` band. It contains a `134px × 34px` logo asset, a `40px` search input, location/account access, menu links and cart affordance. The navigation bounds are capped at `1220px` and use `10px` horizontal padding. The search field has `2px` radius, white background, `16px` text, `15px` left padding and a right-side `46px` search button. Focus adds a `1.5px` blue border and a white/blue/halo ring.

## 7. Components and states

### Product and recommendation cards

The homepage uses Andes card primitives with white primary surfaces, flat variants, `1px` translucent borders and restrained shadow. Product titles are `16px/22px` semibold; recommendation prices reach `24px`. Hover and focus are evidence-backed for interactive cards; bookmark and brand actions may remain visually hidden until interaction. Do not use a deep shadow or saturated background for every card.

### Benefit and ecosystem cards

Dynamic access cards explain benefits such as first-purchase shipping, account access, location, low prices, top sales, protected buying, official stores, categories and payment methods. Observed values include `16px` title text, `14px` description text, `16px`/`12px` internal padding and green/blue action treatments.

### Buttons, tags and messages

Use blue for primary actions, green for positive benefit tags and red for error messages. Tags use small type and `2px`–`8px` radii depending on component. Messages may be full-width, left-aligned and padded `24px`; success, warning, error and informational states have distinct colors. Every interactive component must expose default, hover/active, focus-visible and disabled/error behavior where the source provides evidence; otherwise mark the missing state as `WARNING`.

## 8. Data and commercial modules

The observed homepage declares 11 module positions: exhibitor, dynamic access, THB double, loyalty essential benefits, media card, partner subscriptions, billboards, discovery ads, categories and shopping information. These are content slots, not fixed visual promises: their ordering and campaigns are dynamic. Prices and promotions must never be copied into a derivative system as static claims.

## 9. Spacing and grid

The source uses a compact scale from `2px`, `4px`, `8px`, `12px`, `16px`, `20px` and `24px`, with carousels commonly using `20px` gaps. Desktop content is centered inside a `1200px`–`1220px` bound. Category card width is `270px` at wide desktop, `250px` from `1110px`, and `210px` in narrower category layouts. Cards commonly use `16px` internal spacing.

## 10. Radius and elevation

Observed radii include `2px` inputs, `3px` messages, `4px` cards, `6px` controls and `8px` tags. Circular icon/button affordances use a full-radius shape. Elevation is intentionally shallow: the common card shadow is `0 1px 1px 0 rgba(0,0,0,.1)`. Avoid modal-like shadows on ordinary product cards.

## 11. Responsive behavior

The source provides desktop, tablet and mobile home bundles. At `1200px` and `1095px`, selected nav items are hidden to protect header density. At `768px`, the navigation/content composition switches to mobile behavior. A derivative must preserve a usable search field, touch targets, readable price and card scan order on all three tiers. Exact mobile module ordering is `WARNING` unless inspected in a dedicated mobile session.

## 12. Do's and Don'ts

- Do use yellow only for the brand header/context, not as the default surface of every card.
- Do reserve blue for actions, links and focus states.
- Do keep cards white and separate them with a shallow border/shadow system.
- Do expose keyboard focus with the documented blue ring.
- Don't claim current prices, promotions or inventory from this analysis.
- Don't redistribute the Mercado Libre logo, Proxima Nova files or campaign imagery as if they were generic assets.
- Don't introduce arbitrary rounded pills, gradients or heavy shadows without new evidence.

## 13. Validation Contract

- `[PASSED] Source access`: HTTP `200`; canonical homepage and locale metadata were available.
- `[PASSED] Provenance`: URL, observation date, CSS sources and scope limits are recorded.
- `[PASSED] Hard tokens`: 16 colors, 6 typography scales, 6 radius tokens and 10 spacing tokens are represented in JSON.
- `[PASSED] Component references`: documented component references resolve to `{colors.*}`, `{rounded.*}` and `{typography.*}` tokens.
- `[PASSED] Responsive evidence`: desktop header, max-width bounds, 1200/1095 navigation reductions and 768 mobile bundle are documented.
- `[PASSED] Accessibility evidence`: skip/focus behavior is present in the navigation CSS; image `alt` attributes are present in the observed HTML.
- `[WARNING] Runtime contrast`: blue on white is approximately `3.52:1`; avoid using it for small body text without another contrast cue.
- `[WARNING] Dynamic state coverage`: campaigns, carousels, cookies, account state and mobile modules require dedicated runtime snapshots.
- `[WARNING] Proprietary assets`: logo, font and campaign images require license/trademark review before reuse.

## 14. Extractability contract

An implementation agent should read this Markdown first, use `design-system.json` as the machine projection, and preserve the distinction between brand header, commerce action, positive benefit and error. Any new token, component, campaign claim or responsive rule must be added to this document with evidence before it enters the preview.
