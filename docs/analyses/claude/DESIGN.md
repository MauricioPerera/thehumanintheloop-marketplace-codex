---
name: claude-homepage-analysis
version: 1.0.0
description: Análisis externo y reproducible del homepage público de Claude; no es un sistema oficial de Anthropic.
source: https://claude.com/
colors: documented-in-design-system-json
typography: warm-product-sans
rounded: 4px-controls-12px-cards
spacing: 4px-base-scale
components: product-nav-hero-auth-entry-plan-switcher-plan-card-faq-footer
---

# Claude Homepage — Design System Analysis

## Overview

Este documento analiza el homepage público de Claude observado el 2 de agosto de 2026. La experiencia combina navegación de Platform, Solutions, Pricing y Resources con login, Contact sales y Try Claude; un hero de adquisición, autenticación, descarga desktop, planes Free/Pro/Max, FAQ y navegación de productos. Es un análisis externo, no una especificación oficial.

La oferta, precios, modelos, límites y nombres de funciones pueden cambiar por región, fecha y cuenta. No se redistribuyen logo, imágenes, fuentes, ilustraciones ni textos completos de Anthropic/Claude.

## Contrato duro

- El lienzo usa `{colors.canvas}` y las cards usan `{colors.surface}` o `{colors.surfaceRaised}`.
- Texto principal usa `{colors.ink}`; metadata y copy auxiliar usan `{colors.muted}`.
- El CTA de producto usa `{colors.brand}`; enlaces y foco usan `{colors.accent}`.
- La navegación separa Platform, Solutions, Pricing y Resources, con Login, Contact sales y Try Claude.
- El hero comunica productividad y construcción rápida, con una entrada de autenticación por Google, email y SSO.
- Plan switcher distingue Individual de Team and Enterprise.
- Plan cards muestran tier, precio, frecuencia, CTA, beneficios y notas de límites o impuestos.
- FAQ usa preguntas expandibles y debe anunciar estados `collapsed`/`expanded`.
- Controles usan radio 4px; cards hasta 12px; pills usan 999px; touch targets mínimos 44px.

## Soft contract

Las siguientes decisiones son `inferido` a partir de la composición observable:

- El fondo cálido y la tipografía editorial suavizan una experiencia de pricing y producto (`inferido`).
- “Think fast, build faster” traduce la capacidad del modelo a una promesa de productividad (`inferido`).
- La autenticación aparece antes de la comparación de planes para reducir el tiempo a valor (`inferido`).
- La separación Individual/Team and Enterprise adapta el mismo producto a dos decisiones de compra (`inferido`).
- El footer denso convierte features, modelos, soluciones y plataforma en un mapa de ecosistema (`inferido`).

## Colors

| Token | Valor | Uso |
|---|---|---|
| `colors.canvas` | `#F7F5F0` | Fondo cálido |
| `colors.surface` | `#EDEAE3` | Bandas y cards |
| `colors.surfaceRaised` | `#FFFFFF` | Card activa o elevada |
| `colors.ink` | `#171716` | Texto principal |
| `colors.muted` | `#686761` | Texto auxiliar |
| `colors.brand` | `#D97757` | CTA cálido |
| `colors.accent` | `#285C4D` | Enlace y foco |
| `colors.border` | `#D8D4CB` | Bordes |
| `colors.success` | `#397A54` | Confirmación |
| `colors.error` | `#B43D36` | Error |

Los colores son un snapshot analítico y deben verificarse contra CSS computado antes de producción. Medir contraste de CTA, precios y estados en cada variante.

## Typography

| Rol | Familia | Tamaño | Peso | Line-height |
|---|---|---:|---:|---:|
| Hero heading | Sans/editorial display | 56px | 500 | 1.05 |
| Plan heading | Sans/editorial display | 32px | 500 | 1.15 |
| Card heading | Sans-serif interface | 20px | 600 | 1.3 |
| Body | Sans-serif interface | 17px | 400 | 1.55 |
| Price / label | Sans-serif interface | 14px | 600 | 1.4 |
| Code / reference | ui-monospace, monospace | 13px | 400 | 1.45 |

La familia exacta de Claude no se afirma como verificada ni redistribuible. Una implementación independiente debe usar una fuente con licencia compatible.

## Components

### Product navigation

Header con Platform, Solutions, Pricing, Resources, Login, Contact sales y Try Claude. Estados: `default`, `hover`, `focus-visible`, `menu-open`, `compact`.

### Hero auth entry

Hero de productividad con Google, email, SSO, aviso de privacidad y descarga desktop. Estados: `empty`, `focus`, `loading`, `error`, `success`, `disabled`.

### Plan switcher

Tabs Individual / Team and Enterprise. Estados: `selected`, `hover`, `focus-visible`, `loading`.

### Plan card

Free, Pro y Max con precio, frecuencia, CTA, benefits y disclaimers. Estados: `default`, `recommended`, `selected`, `disabled`, `error`.

### FAQ disclosure

Preguntas sobre Claude, usos, precios y planes. Estados: `collapsed`, `expanded`, `focus-visible`, `loading`.

### Footer ecosystem groups

Products, Features, Models, Solutions, Claude Platform, Resources, Company, Programs, Help and security y políticas. Estados: `default`, `hover`, `focus-visible`, `stacked-mobile`.

## Layout and spacing

- Header: padding lateral 24px desktop y 16px mobile.
- Hero: copy centrado o de ancho limitado, con auth entry y CTAs próximos.
- Plan grid: tres cards en desktop, una columna en mobile; gap de 16px.
- Card: padding 20px, borde o superficie suave y metadata separada por 8px.
- FAQ: max-width de 900px, disclosures con separación de 8px.
- Footer: grupos con gap de 32px desktop y 8px entre enlaces.

## Responsive

| Rango | Comportamiento |
|---|---|
| 320–543px | Header compacto, hero vertical, auth apilada, plan cards y footer en una columna |
| 544–767px | Plan cards de dos columnas si caben y navegación flexible |
| 768–1011px | Hero de dos zonas y plan grid adaptable |
| 1012–1279px | Plan grid de hasta tres columnas, FAQ limitada y footer en grupos |
| 1280px+ | Mayor aire exterior sin estirar indefinidamente cards o copy |

Probar 320px, 768px y 1280px, además de teclado, zoom, reduced motion, contraste, validación de email y estados de SSO.

## Do's and Don'ts

- Do: distinguir individual, team y enterprise sin depender únicamente del color.
- Do: mostrar precio, frecuencia, impuestos, límites y condiciones como contenido accesible.
- Do: mantener beneficios comparables entre cards y anunciar plan seleccionado.
- Don't: presentar precios, modelos o features dinámicos como tokens permanentes.
- Don't: copiar logo, ilustraciones, fuentes o textos de Claude sin autorización.
- Don't: ocultar legal, privacidad, límites de uso o condiciones de renovación.

## Provenance

- Fuente observada: [Claude homepage](https://claude.com/).
- Fecha de observación: 2026-08-02.
- Evidencia visible: navegación, hero, auth Google/email/SSO, desktop app, plan switcher, Free/Pro/Max, FAQ, productos, features, modelos, soluciones, plataforma y footer.
- Límite: precios, planes, modelos, disponibilidad y mensajes cambian por región, cuenta y fecha.

## Validation Contract

### PASSED

- El documento separa contrato duro, contrato blando, componentes, estados, responsive y procedencia.
- `design-system.json` contiene tokens, breakpoints y componentes derivados del contrato.
- El preview muestra hero, auth, plan switcher, plan cards, FAQ, footer, tokens y validación.
- Se contemplan accesibilidad de tabs/disclosures, touch targets, SSO y reduced motion.

### WARNING

- Precios, límites y features son dinámicos y deben revalidarse antes de publicar una adaptación.
- Los colores son snapshot analítico y requieren medición CSS computada.
- Este no es un sistema oficial de Claude/Anthropic ni una autorización para redistribuir activos.

### Criterios de aceptación

Una implementación pasa cuando conserva la ruta hero → auth → planes → FAQ, comparación transparente, navegación accesible, tokens y responsive behavior; los assets de marca deben sustituirse por recursos autorizados.
