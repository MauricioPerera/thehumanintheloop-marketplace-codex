---
name: openai-homepage-analysis
version: 1.0.0
description: Análisis externo y reproducible del homepage público de OpenAI; no es un sistema oficial de OpenAI.
source: https://openai.com/
colors: documented-in-design-system-json
typography: neutral-sans-serif-editorial
rounded: 4px-controls-12px-cards
spacing: 4px-base-scale
components: global-nav-prompt-hero-content-rail-footer
---

# OpenAI Homepage — Design System Analysis

## Overview

Este documento analiza el homepage público de OpenAI observado el 2 de agosto de 2026. La experiencia combina navegación de Research, Products, Business, Developers y Company con una llamada a ChatGPT, contenido editorial, noticias recientes, stories, research, business stories y footer de producto/soporte. Es un análisis externo para auditoría y reconstrucción; no es una especificación oficial de OpenAI.

La página es editorial y de producto a la vez: ofrece una entrada conversacional, tarjetas de contenido y navegación profunda por el ecosistema. El contenido, los productos y las campañas cambian rápidamente; no se redistribuyen logos, imágenes, fuentes propietarias ni textos completos.

## Contrato duro

- El lienzo principal usa `{colors.canvas}` y las superficies suaves usan `{colors.surface}`.
- El texto principal usa `{colors.ink}`; el texto auxiliar usa `{colors.muted}`.
- El color de acción usa `{colors.accent}` y el borde usa `{colors.border}`.
- La navegación global agrupa Research, Products, Business, Developers y Company, con accesos a Foundation, ChatGPT y Login.
- La entrada conversacional contiene un prompt visible y acciones de destino como Talk with ChatGPT, Research, API Platform y Stories.
- Las secciones editoriales usan headings cortos, metadata de tipo/fecha/tiempo y tarjetas enlazables.
- Controles y enlaces deben mantener foco visible y objetivos táctiles mínimos de 44px.
- Controles usan radio 4px; cards editoriales pueden usar hasta 12px; superficies no dependen solo de sombra para separarse.
- Spacing base de 4px, gutters de 16px mobile y 24px desktop; los grupos de footer se reorganizan en mobile.

## Soft contract

Las siguientes decisiones son `inferido` a partir de la estructura observable:

- La interfaz comunica inteligencia aplicada con una estética editorial sobria (`inferido`).
- La frase “What can I help with?” convierte la home corporativa en punto de entrada conversacional (`inferido`).
- La repetición de productos, research, stories y business crea una arquitectura de confianza y evidencia (`inferido`).
- La navegación extensa está pensada para múltiples audiencias: usuarios, investigadores, desarrolladores, empresas y prensa (`inferido`).
- La escasez de ornamento permite que titulares, metadata y relaciones entre enlaces sean la identidad principal (`inferido`).

## Colors

| Token | Valor | Uso |
|---|---|---|
| `colors.canvas` | `#FFFFFF` | Lienzo principal |
| `colors.surface` | `#F7F7F5` | Paneles y bandas suaves |
| `colors.ink` | `#0D0D0D` | Texto y navegación |
| `colors.muted` | `#5D5D5D` | Metadata y copy auxiliar |
| `colors.accent` | `#10A37F` | Acción y foco de producto |
| `colors.border` | `#D9D9D4` | Bordes y divisores |
| `colors.hoverSurface` | `#ECECE7` | Hover y selección |
| `colors.success` | `#16825D` | Confirmación |
| `colors.error` | `#C0392B` | Error |

Contraste de referencia: `{colors.ink}` sobre `{colors.canvas}` supera 19:1; `{colors.muted}` sobre `{colors.canvas}` supera 6:1; el acento debe medirse por tamaño y contexto antes de usarse como texto pequeño.

## Typography

| Rol | Familia | Tamaño | Peso | Line-height |
|---|---|---:|---:|---:|
| Hero / prompt | Sans-serif editorial | 48px | 600 | 1.1 |
| Section heading | Sans-serif editorial | 32px | 600 | 1.2 |
| Card heading | Sans-serif editorial | 20px | 600 | 1.3 |
| Body | Sans-serif editorial | 16px | 400 | 1.5 |
| Metadata | Sans-serif editorial | 13px | 500 | 1.4 |
| Code / reference | ui-monospace, monospace | 13px | 400 | 1.45 |

La familia exacta de OpenAI no se afirma como verificada ni redistribuible. Una implementación independiente debe usar una fuente compatible con su propia licencia.

## Components

### Global navigation

Menú por audiencias y productos, Foundation, ChatGPT, Login y apertura de submenús. Estados: `default`, `hover`, `focus-visible`, `menu-open`, `compact`.

### Prompt entry

Campo o panel de entrada conversacional con placeholder, submit y destinos relacionados. Estados: `empty`, `typing`, `focus`, `loading`, `error`, `disabled`.

### Editorial story card

Tarjeta con título, tipo, fecha/tiempo, visual opcional y enlace. Estados: `default`, `hover`, `focus-visible`, `loading`, `featured`.

### Content section rail

Agrupación para Recent news, Stories, Latest research y OpenAI for business. Estados: `default`, `loading`, `empty`, `collapsed`.

### Product link group

Grupos de productos, API, Business, Developers, Company, Support y políticas. Estados: `default`, `hover`, `focus-visible`, `stacked-mobile`.

## Layout and spacing

- Header: ancho completo, padding lateral 24px desktop y 16px mobile.
- Prompt: ancho limitado, zona de alto contraste y acciones relacionadas debajo.
- Secciones editoriales: grid de cards con gap de 16px y encabezado con enlace “View more”.
- Card: padding 20px, borde o superficie suave, title y metadata separados por 8px.
- Footer: grupos de enlaces con gap vertical de 8px y separación entre columnas de 32px.

## Responsive

| Rango | Comportamiento |
|---|---|
| 320–543px | Header compacto, prompt a una columna, cards apiladas y footer en grupos verticales |
| 544–767px | Grid flexible de contenido y navegación que envuelve sin overflow |
| 768–1011px | Header regular, prompt amplio y grids de dos columnas |
| 1012–1279px | Contenedor editorial amplio y grupos de footer en columnas |
| 1280px+ | Más espacio exterior sin estirar indefinidamente la columna de lectura |

Probar 320px, 768px y 1280px, además de teclado, zoom, reduced motion, contraste alto y foco dentro de menús.

## Do's and Don'ts

- Do: distinguir producto, research, news, stories y business mediante metadata y jerarquía.
- Do: proporcionar un destino claro para cada tarjeta y un foco visible.
- Do: comunicar errores del prompt con texto y estado accesible.
- Don't: presentar claims, nombres de modelos o fechas dinámicas como tokens visuales permanentes.
- Don't: copiar logo, imágenes, fuentes o textos de OpenAI sin autorización.
- Don't: esconder productos o políticas importantes en menús inaccesibles.

## Provenance

- Fuente observada: [OpenAI homepage](https://openai.com/).
- Fecha de observación: 2026-08-02.
- Evidencia visible: navegación global, ChatGPT, Login, prompt, Research, API Platform, Stories, Recent news, Latest research, OpenAI for business, Products, API, Business, Developers, Company y Support.
- Límite: titulares, productos, enlaces y campañas son dinámicos; puede variar por región, sesión y fecha.

## Validation Contract

### PASSED

- El documento separa contrato duro, contrato blando, componentes, estados, responsive y procedencia.
- `design-system.json` contiene tokens, breakpoints y componentes derivados del contrato.
- El preview muestra prompt, cards editoriales, grupos de enlaces, tokens y validación sin reutilizar activos.
- Se contemplan navegación por teclado, menús, prompt, metadata y reduced motion.

### WARNING

- El contenido de OpenAI cambia con frecuencia y los valores de color/tipografía son una síntesis analítica.
- Los estados autenticados y submenús completos requieren inspección autorizada adicional.
- Este no es un sistema oficial de OpenAI ni una autorización para redistribuir sus activos.

### Criterios de aceptación

Una implementación pasa cuando conserva la entrada conversacional, arquitectura editorial, navegación por audiencias, estados accesibles, tokens y responsive behavior; los contenidos y activos de marca deben sustituirse o licenciarse correctamente.
