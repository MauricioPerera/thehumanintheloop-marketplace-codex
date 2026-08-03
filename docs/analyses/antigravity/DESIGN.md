---
name: google-antigravity-homepage-analysis
version: 1.0.0
description: Análisis externo y reproducible de antigravity.google; no es un sistema oficial de Google Antigravity.
source: https://antigravity.google/
colors: documented-in-design-system-json
typography: dark-product-editorial-sans
rounded: 4px-controls-16px-cards
spacing: 4px-base-scale
components: product-nav-hero-product-selector-use-case-story-download-footer
---

# Google Antigravity — Design System Analysis

## Overview

Este documento analiza `antigravity.google` observado el 2 de agosto de 2026. La página presenta Google Antigravity como plataforma de desarrollo agentic, con productos 2.0, CLI, SDK e IDE; casos de uso para desarrolladores; descarga; contenido de blog y enlaces de producto, docs y changelog. Es un análisis externo, no una especificación oficial.

La experiencia combina landing de producto, documentación de ecosistema y adquisición de software. Los mensajes, modelos, versiones, screenshots, logo y assets de Google quedan fuera de este entregable.

## Contrato duro

- La página usa un lienzo oscuro con texto claro, superficies de producto y un acento de acción luminoso; los valores reproducibles están en `design-system.json`.
- La navegación agrupa Product, Press/Guidelines, Download y menú; el footer repite Product y Resources.
- El hero debe declarar la propuesta de valor, ofrecer Download y Explore use cases, y conservar una composición de alto impacto.
- El selector de productos distingue Antigravity 2.0, CLI, SDK e IDE mediante título, descripción, visual y enlace.
- Los casos de uso separan Full stack developer, Enterprise developer y Frontend developer.
- Las tarjetas editoriales exponen categoría, fecha, título y acción de lectura.
- Controles usan radio 4px; cards y paneles usan 16px; chips de estado usan 999px.
- El spacing parte de 4px; touch targets mínimos de 44px; la navegación no debe producir overflow horizontal.

## Soft contract

Las siguientes decisiones son `inferido` a partir de la composición observable:

- El nombre, el lenguaje de liftoff y el fondo oscuro construyen una metáfora de despegue tecnológico (`inferido`).
- El movimiento y las demostraciones son parte de la narrativa de confianza del producto (`inferido`).
- El producto se presenta como una familia de superficies: command center, CLI, SDK e IDE (`inferido`).
- La separación por tipo de desarrollador reduce la distancia entre capacidades técnicas y casos reales (`inferido`).
- La mezcla de descarga, docs, changelog y blog sugiere una experiencia orientada a adopción continua (`inferido`).

## Colors

| Token | Valor | Uso |
|---|---|---|
| `colors.canvas` | `#0B0B0F` | Fondo oscuro |
| `colors.surface` | `#15161C` | Cards y navegación |
| `colors.surfaceRaised` | `#242631` | Hover y panel elevado |
| `colors.ink` | `#FFFFFF` | Texto principal |
| `colors.muted` | `#A8AAB5` | Copy auxiliar y metadata |
| `colors.brand` | `#B8F34A` | CTA y acento experimental |
| `colors.accent` | `#8AB4F8` | Enlaces y foco |
| `colors.border` | `#3A3D4A` | Bordes y divisores |
| `colors.success` | `#71D99A` | Confirmación |
| `colors.error` | `#F28B82` | Error |

Los colores exactos se consideran snapshot analítico cuando la fuente no expone CSS computado; deben medirse de nuevo antes de implementación. Verificar contraste de acentos en texto pequeño.

## Typography

| Rol | Familia | Tamaño | Peso | Line-height |
|---|---|---:|---:|---:|
| Hero heading | Sans-serif display | 56px | 600 | 1.05 |
| Section heading | Sans-serif display | 36px | 600 | 1.15 |
| Card heading | Sans-serif interface | 22px | 600 | 1.25 |
| Body | Sans-serif interface | 16px | 400 | 1.5 |
| Metadata | Sans-serif interface | 13px | 500 | 1.4 |
| Code / reference | ui-monospace, monospace | 13px | 400 | 1.45 |

La familia tipográfica exacta y los iconos de la fuente no se consideran verificables ni redistribuibles. Una adaptación debe usar recursos licenciados.

## Components

### Product navigation

Header con Product, Press Guidelines, Download, menú y footer con Docs, Changelog, Releases, Blog, Pricing y Use Cases. Estados: `default`, `hover`, `focus-visible`, `menu-open`, `compact`.

### Hero product CTA

Hero con claim, Download y Explore use cases; puede incluir animación o visual. Estados: `default`, `loading`, `hover`, `focus-visible`, `reduced-motion`.

### Product selector

Tabs o paneles para 2.0, CLI, SDK e IDE con descripción y visual. Estados: `selected`, `hover`, `focus-visible`, `loading`, `collapsed`.

### Use-case story

Casos Full stack, Enterprise y Frontend con imagen/video, label, play y View case. Estados: `default`, `playing`, `paused`, `focus-visible`, `reduced-motion`.

### Download panel

Descarga diferenciada para Apple Silicon e Intel. Estados: `default`, `hover`, `focus-visible`, `disabled`, `unavailable`.

### Blog card

Tarjeta con categoría, fecha, título y Read blog. Estados: `default`, `hover`, `focus-visible`, `loading`.

## Layout and spacing

- Header: ancho completo, padding lateral 24px desktop y 16px mobile.
- Hero: composición amplia con max-width de copy cercano a 720px y visual de producto separado.
- Product selector: grid de dos zonas en desktop, apilado en mobile.
- Use cases: cards o rail con gap de 16px; los controles de reproducción deben tener label accesible.
- Blog: grid de cards con gap de 16px y metadata separada del título.
- Footer: grupos Product y Resources separados por 32px desktop y apilados en mobile.

## Responsive

| Rango | Comportamiento |
|---|---|
| 320–543px | Menú compacto, hero vertical, producto apilado y cards de caso a una columna |
| 544–767px | Grid flexible, rail navegable y CTAs con ancho disponible |
| 768–1011px | Header regular, hero de dos zonas y product selector en dos columnas |
| 1012–1279px | Grid de casos y blog con mayor densidad |
| 1280px+ | Hero amplio con copy limitado y espacio exterior sin estirar la lectura |

Probar 320px, 768px y 1280px, además de teclado, reduced motion, zoom, contraste alto y estados de descarga sin red.

## Do's and Don'ts

- Do: distinguir claramente IDE, CLI, SDK y command center.
- Do: ofrecer alternativas textuales para video, animación y casos de uso.
- Do: explicar plataforma, arquitectura y disponibilidad antes de iniciar la descarga.
- Don't: copiar logo, screenshots, videos, iconos o textos de Google sin autorización.
- Don't: ocultar requisitos de sistema o diferenciar Apple Silicon/Intel solo con iconos.
- Don't: hacer que el movimiento sea necesario para entender el producto.

## Provenance

- Fuente observada: [Google Antigravity](https://antigravity.google/).
- Fecha de observación: 2026-08-02.
- Evidencia visible: hero, Download, Explore use cases, Antigravity 2.0, CLI, SDK, IDE, casos de uso, descarga Apple Silicon/Intel, blog, docs y changelog.
- Límite: screenshots, animaciones, claims, versiones, enlaces y disponibilidad pueden cambiar rápidamente.

## Validation Contract

### PASSED

- El documento separa contrato duro, contrato blando, componentes, estados, responsive y procedencia.
- `design-system.json` contiene tokens, breakpoints y componentes derivados del contrato.
- El preview muestra hero, productos, use cases, descarga, blog, tokens y validación sin reutilizar assets.
- Se contemplan reduced motion, teclado, touch targets y variantes de descarga.

### WARNING

- Los valores cromáticos son un snapshot analítico y requieren medición computada para producción.
- El sitio es experimental y sus productos, versiones, copy y assets pueden cambiar.
- Este no es un sistema oficial de Google Antigravity ni una autorización para redistribuir activos.

### Criterios de aceptación

Una implementación pasa cuando mantiene la narrativa de producto agentic, diferenciación de superficies, casos de uso, descarga accesible, tokens y responsive behavior; los activos de marca deben sustituirse por recursos autorizados.
