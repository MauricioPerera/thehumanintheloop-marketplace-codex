---
name: notebooklm-homepage-analysis
version: 1.0.0
description: Análisis externo y reproducible del homepage público de NotebookLM/Gemini Notebook; no es un sistema oficial de Google.
source: https://notebooklm.google/
colors: documented-in-design-system-json
typography: google-product-sans-ui
rounded: 8px-controls-16px-cards
spacing: 4px-base-scale
components: product-nav-hero-source-upload-insight-card-output-rail-public-notebook-faq-footer
---

# NotebookLM / Gemini Notebook — Design System Analysis

## Overview

Este documento analiza el homepage público de NotebookLM, cuya página observada presenta también el naming Gemini Notebook, el 2 de agosto de 2026. La experiencia comunica un compañero de investigación basado en fuentes: carga de PDFs, sitios, YouTube, audio, Google Docs y Slides; preguntas y conexiones; citas; Audio Overviews; formatos de salida; notebooks públicos y FAQ. Es un análisis externo, no una especificación oficial de Google.

La página directa carga contenido dinámico dentro de un iframe; el análisis combina la fuente pública y sus variantes indexadas de idioma. No se redistribuyen logo, ilustraciones, audio, imágenes, fuentes ni textos completos.

## Contrato duro

- El lienzo usa `{colors.canvas}` y las superficies de notebook usan `{colors.surface}`.
- El texto principal usa `{colors.ink}`; el auxiliar usa `{colors.muted}`.
- La acción primaria usa `{colors.brand}`; los estados de fuente/validación usan colores semánticos.
- El hero debe comunicar comprensión basada en fuentes y ofrecer Try Notebook/Get the app.
- El flujo principal separa Upload sources, Instant insights y See the source/citations.
- Output cards distinguen Audio Overviews, Mind Maps, Reports, Flashcards, Quizzes, Video Overviews, Data Tables, Infographics y Slide Decks.
- Public notebooks presentan nombre, número de fuentes y acción de exploración.
- FAQ usa disclosure con estados collapsed/expanded y foco visible.
- Controles usan radio 8px; cards 16px; chips 999px; touch targets mínimos 44px.

## Soft contract

Las siguientes decisiones son `inferido` a partir de la estructura pública:

- La fuente no es solo input: es la frontera de confianza del producto (`inferido`).
- Citas y “see the source” convierten la trazabilidad en parte de la interfaz, no en una nota legal (`inferido`).
- Audio, mapas, flashcards y slides transforman la misma base documental para distintos modos de aprendizaje (`inferido`).
- Public notebooks reducen la barrera de entrada mostrando ejemplos antes de crear uno (`inferido`).
- La paleta multicolor sugiere una familia de capacidades alrededor de una superficie de investigación (`inferido`).

## Colors

| Token | Valor | Uso |
|---|---|---|
| `colors.canvas` | `#FFFFFF` | Fondo principal |
| `colors.surface` | `#F6F8FC` | Notebook y cards |
| `colors.surfaceRaised` | `#FFFFFF` | Card activa |
| `colors.ink` | `#202124` | Texto principal |
| `colors.muted` | `#5F6368` | Texto auxiliar |
| `colors.brand` | `#1A73E8` | CTA y enlaces |
| `colors.source` | `#34A853` | Fuentes/citas |
| `colors.audio` | `#A142F4` | Audio Overviews |
| `colors.warning` | `#F9AB00` | Aviso |
| `colors.border` | `#DADCE0` | Bordes |
| `colors.error` | `#D93025` | Error |

Los colores son un snapshot analítico y deben medirse contra CSS computado antes de producción. Verificar contraste de estados multicolor y no depender del color como único indicador.

## Typography

| Rol | Familia | Tamaño | Peso | Line-height |
|---|---|---:|---:|---:|
| Hero heading | Product Sans / sans-serif | 52px | 500 | 1.08 |
| Section heading | Product Sans / sans-serif | 32px | 500 | 1.2 |
| Card heading | Sans-serif interface | 20px | 600 | 1.3 |
| Body | Sans-serif interface | 16px | 400 | 1.5 |
| Metadata | Sans-serif interface | 13px | 500 | 1.4 |
| Code / reference | ui-monospace, monospace | 13px | 400 | 1.45 |

La disponibilidad y licencia de Product Sans no se consideran parte de este entregable. Una adaptación debe usar una fuente con licencia compatible.

## Components

### Product navigation

Navegación de Notebook, Try, Get the app, ayuda y acceso. Estados: `default`, `hover`, `focus-visible`, `menu-open`, `compact`.

### Source upload hero

Hero con CTA para cargar fuentes y formatos admitidos. Estados: `empty`, `drag-over`, `uploading`, `success`, `error`, `unsupported`.

### Insight card

Bloque de instant insights, preguntas, conexiones y respuestas grounded. Estados: `default`, `loading`, `citation-visible`, `error`, `empty`.

### Output format card

Audio, mind map, report, flashcard, quiz, video, data table, infographic y slide deck. Estados: `default`, `generating`, `ready`, `failed`, `downloadable`.

### Public notebook card

Notebook destacado con nombre, cantidad de fuentes y acción. Estados: `default`, `hover`, `focus-visible`, `featured`, `loading`.

### FAQ disclosure/footer

FAQ y navegación de producto, ayuda, privacidad y recursos. Estados: `collapsed`, `expanded`, `focus-visible`, `stacked-mobile`.

## Layout and spacing

- Header: padding lateral 24px desktop y 16px mobile.
- Hero: copy centrado, CTA de fuente y visual de notebook separado.
- Source upload: panel destacado con icono y formatos explícitos; gap de 16px.
- Output rail: grid o rail horizontal con gap de 12px y tarjetas de formato.
- Public notebooks: cards de dos o cuatro columnas según viewport.
- FAQ/footer: max-width de lectura y grupos de enlaces con gap de 24px.

## Responsive

| Rango | Comportamiento |
|---|---|
| 320–543px | Header compacto, upload vertical, output cards apiladas y FAQ en una columna |
| 544–767px | Grid flexible de dos columnas y rail de outputs navegable |
| 768–1011px | Hero de dos zonas, upload amplio y public notebooks adaptables |
| 1012–1279px | Outputs y notebooks en varias columnas; footer agrupado |
| 1280px+ | Más aire exterior sin estirar indefinidamente el panel de fuentes |

Probar 320px, 768px y 1280px, además de teclado, zoom, reduced motion, upload fallido, citas y estados de generación.

## Do's and Don'ts

- Do: dejar claro qué fuentes se incorporaron y qué respuesta las cita.
- Do: indicar formato, progreso, error y disponibilidad de cada output.
- Do: ofrecer accesibilidad equivalente para audio, video, mapas y tarjetas visuales.
- Don't: presentar respuestas como grounded si no muestran procedencia suficiente.
- Don't: copiar logo, ilustraciones, audio, fuentes o textos de Google sin autorización.
- Don't: ocultar límites de fuente, privacidad o condiciones de notebook público.

## Provenance

- Fuente observada: [NotebookLM / Gemini Notebook](https://notebooklm.google/).
- Referencias públicas: [NotebookLM Audio](https://notebooklm.google/audio?hl=es) y variantes indexadas del homepage.
- Fecha de observación: 2026-08-02.
- Límite: la página directa expone un iframe y el contenido puede variar por idioma, cuenta, disponibilidad y experimento.

## Validation Contract

### PASSED

- El documento separa contrato duro, contrato blando, componentes, estados, responsive y procedencia.
- `design-system.json` contiene tokens, breakpoints y componentes derivados del contrato.
- El preview muestra upload, insights, citations, outputs, notebooks públicos, tokens y validación.
- Se contemplan estados de carga, error, generación, citación, audio y formatos alternativos.

### WARNING

- La inspección directa del homepage estuvo limitada por contenido dinámico/iframe.
- Funciones, formatos, límites y nomenclatura pueden cambiar por región, cuenta y fecha.
- Este no es un sistema oficial de Google ni una autorización para redistribuir activos.

### Criterios de aceptación

Una implementación pasa cuando conserva la ruta fuentes → insights → citas → outputs, transparencia de procedencia, estados accesibles, tokens y responsive behavior.
