---
name: crunchyroll-homepage-analysis
version: 1.0.0
description: Análisis externo y reproducible del homepage público de Crunchyroll; no es un sistema oficial de Crunchyroll.
source: https://www.crunchyroll.com/
colors: documented-in-design-system-json
typography: sans-serif-streaming-ui
rounded: 4px-controls-8px-cards
spacing: 4px-base-scale
components: streaming-header-hero-content-rail-plan-card-footer
---

# Crunchyroll Homepage — Design System Analysis

## Overview

Este documento analiza la experiencia pública de Crunchyroll observada el 2 de agosto de 2026. La página combina descubrimiento de anime, promoción de contenido, planes Premium, acciones de reproducción y navegación secundaria. Es un análisis externo para auditoría y reconstrucción; no es una especificación oficial de Crunchyroll.

La fuente es dinámica y depende de país, idioma, cookies, dispositivo, sesión y catálogo disponible. El análisis no reutiliza logotipos, key art, fotografías, tipografías propietarias, nombres de personajes ni textos completos de la fuente.

## Contrato duro

- El lienzo principal es oscuro y usa `{colors.canvas}`; el texto principal usa `{colors.ink}` y el texto auxiliar `{colors.muted}`.
- El color de acción de marca usa `{colors.brand}`; los estados positivos usan `{colors.success}` y los errores `{colors.error}`.
- La navegación superior debe separar descubrimiento, acceso y suscripción; en mobile debe compactarse sin overflow horizontal.
- El hero combina una imagen o gradiente de alto impacto con título, metadato de contenido y CTA; la imagen real no forma parte de este contrato redistribuible.
- Las rails de contenido usan tarjetas de proporción controlada y gaps constantes; el título y las acciones deben conservar foco visible.
- Las cards de planes distinguen precio, frecuencia, beneficio y acción sin depender solo de color.
- Los controles usan radio 4px; las cards y superficies de contenido usan 8px; los chips pueden usar 999px.
- La base de spacing es 4px con gutters de 16px en mobile y 24px en desktop.
- El layout debe soportar una columna de contenido en mobile, rails desplazables con indicador accesible y varias columnas en desktop.

## Soft contract

Las siguientes decisiones son `inferido` a partir de la composición observable:

- La interfaz busca una sensación de entretenimiento inmersivo y descubrimiento continuo (`inferido`).
- El fondo oscuro permite que el arte de contenido y los CTAs sean el foco visual (`inferido`).
- Las rails y etiquetas sub/dub reducen la distancia entre catálogo y decisión de reproducción (`inferido`).
- El bloque Premium alterna conversión y explicación de beneficios (`inferido`).
- El uso de una navegación extensa responde a una plataforma que incluye anime, juegos, tienda, noticias y eventos (`inferido`).

## Colors

| Token | Valor | Uso |
|---|---|---|
| `colors.canvas` | `#000000` | Fondo de experiencia de streaming |
| `colors.surface` | `#23252B` | Cards y paneles |
| `colors.surfaceRaised` | `#34363D` | Hover y elevación |
| `colors.ink` | `#FFFFFF` | Texto principal |
| `colors.muted` | `#A0A0A0` | Metadatos y texto auxiliar |
| `colors.brand` | `#F47521` | CTA y acento naranja |
| `colors.accent` | `#FAB818` | Destacado y promoción |
| `colors.border` | `#4A4C52` | Bordes y divisores |
| `colors.success` | `#2EBD59` | Confirmación |
| `colors.error` | `#E5484D` | Error |

Contraste de referencia: `{colors.ink}` sobre `{colors.canvas}` supera 20:1; `{colors.muted}` sobre `{colors.canvas}` debe verificarse por tamaño y peso; `{colors.brand}` sobre `{colors.canvas}` debe medirse antes de usarlo como texto pequeño.

## Typography

| Rol | Familia | Tamaño | Peso | Line-height |
|---|---|---:|---:|---:|
| Hero heading | Sans-serif de interfaz | 40px | 700 | 1.1 |
| Section heading | Sans-serif de interfaz | 24px | 700 | 1.25 |
| Card title | Sans-serif de interfaz | 16px | 600 | 1.3 |
| Body | Sans-serif de interfaz | 16px | 400 | 1.5 |
| Metadata / labels | Sans-serif de interfaz | 13px | 600 | 1.4 |
| Code / reference | ui-monospace, monospace | 13px | 400 | 1.45 |

La fuente exacta de marca no se considera verificada ni redistribuible; una implementación propia debe usar una sans-serif con licencia compatible.

## Components

### Streaming header

Header con navegación de catálogo, búsqueda, juegos/tienda, cuenta y Premium. Estados: `default`, `hover`, `focus-visible`, `compact`, `menu-open`.

### Hero content block

Bloque de promoción o título destacado con arte, copy, metadatos, CTA de reproducción y CTA de suscripción. Estados: `default`, `loading`, `hover`, `focus-visible`, `unavailable`.

### Content rail and card

Rail horizontal con tarjetas de anime, etiquetas de subtítulos/doblaje y acción de detalle. Estados: `default`, `hover`, `focus-visible`, `loading`, `empty`, `locked`.

### Premium plan card

Card comparativa con tier, precio, frecuencia, beneficios y acción. Estados: `default`, `recommended`, `selected`, `disabled`, `error`.

### Footer navigation

Enlaces de soporte, cuenta, dispositivos, legal, idioma y productos relacionados. Estados: `default`, `hover`, `focus-visible`, `stacked-mobile`.

## Layout and spacing

- Header: ancho completo, altura aproximada de 64px desktop y 56px mobile.
- Hero: proporción amplia; copy con max-width de 520px y gradiente para legibilidad.
- Rail: gap de 12px, card mínima de 160px en mobile y 220px en desktop cuando el contenido lo permite.
- Card: padding 16px, superficie oscura y borde o separación de 1px.
- Plan grid: tres columnas en desktop, una columna en mobile; gap de 16px.
- CTA: min-height 44px, padding horizontal 16px y radio 4px.

## Responsive

| Rango | Comportamiento |
|---|---|
| 320–543px | Header compacto, hero vertical, rails desplazables, cards estrechas y planes apilados |
| 544–767px | Rails flexibles y hero de dos zonas cuando el ancho lo permite |
| 768–1011px | Navegación regular, hero amplio y dos columnas para contenido auxiliar |
| 1012–1279px | Rails de varias tarjetas y plan grid de hasta tres columnas |
| 1280px+ | Contenedor amplio con hero limitado y mayor densidad de catálogo |

Probar 320px, 768px y 1280px, además de teclado, zoom, reduced motion, contraste alto y navegación de rails sin depender solo del gesto táctil.

## Do's and Don'ts

- Do: proporcionar título, estado y acción accesible para cada card de contenido.
- Do: anunciar el estado de suscripción, carga, error o contenido bloqueado.
- Do: ofrecer controles visibles para avanzar rails y una alternativa de teclado.
- Don't: usar key art, logotipos, personajes o tipografías de Crunchyroll sin permiso.
- Don't: hacer que el autoplay o la animación sean necesarios para entender la oferta.
- Don't: ocultar precio, periodicidad, renovación o disponibilidad regional en una card Premium.

## Provenance

- Fuente observada: [Crunchyroll homepage](https://www.crunchyroll.com/).
- Referencia complementaria pública: [Crunchyroll Premium](https://www.crunchyroll.com/premium/).
- Fecha de observación: 2026-08-02.
- Límite: la captura pública directa puede no exponer todo el contenido por carga dinámica; región, idioma, sesión y suscripción modifican catálogo y ofertas.

## Validation Contract

### PASSED

- El documento contiene contrato duro, contrato blando, componentes, estados, responsive y procedencia.
- `design-system.json` contiene tokens hex, breakpoints y componentes referenciados por el análisis.
- El preview expone rails, hero, planes, tokens y estado de validación sin reutilizar activos de la fuente.
- El contrato contempla touch targets, teclado, reduced motion y disponibilidad regional.

### WARNING

- El homepage es altamente dinámico y puede presentar contenido diferente por región, sesión o suscripción.
- La captura directa tuvo contenido HTML limitado; algunas decisiones son inferencias documentadas.
- Este no es un sistema oficial de Crunchyroll ni una autorización para redistribuir sus activos.

### Criterios de aceptación

Una implementación pasa cuando conserva la primacía del contenido audiovisual, rails navegables, planes transparentes, estados accesibles, tokens y responsive behavior; todo contenido de marca debe sustituirse por activos licenciados.
