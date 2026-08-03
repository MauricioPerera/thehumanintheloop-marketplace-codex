---
name: qwen-homepage-analysis
version: 1.0.0
description: Análisis externo y reproducible del homepage público de Qwen; no es un sistema oficial de Qwen.
source: https://qwen.ai/
colors: documented-in-design-system-json
typography: modern-ai-product-sans
rounded: 8px-controls-16px-cards
spacing: 4px-base-scale
components: ai-nav-hero-studio-card-api-card-feature-rail-model-card-footer
---

# Qwen Homepage — Design System Analysis

## Overview

Este documento analiza la experiencia pública de Qwen observada el 2 de agosto de 2026. La arquitectura visible en la fuente y páginas públicas relacionadas combina Qwen Studio, API Platform, Download, product features, modelos multimodales, generación de imagen/audio, Deep Research y recursos de comunidad. Es un análisis externo, no una especificación oficial de Qwen.

La página directa tiene contenido altamente dinámico y la inspección pública HTML fue limitada; por eso los hallazgos de color y composición se marcan como snapshot o inferencia. Modelos, capacidades, precios, enlaces y disponibilidad cambian rápidamente.

## Contrato duro

- El lienzo, superficies, texto, borde y acento se declaran en `design-system.json`; los valores de color son snapshot analítico cuando no se pudo verificar CSS computado.
- La navegación debe ofrecer rutas a Studio, API Platform y Download.
- El hero debe comunicar el acceso a modelos Qwen y ofrecer una acción de uso inmediato.
- Cards principales separan Studio, API Platform y Download antes de presentar features.
- Model cards exponen entradas, salidas, modalidad y contexto cuando el dato está disponible.
- API cards distinguen Chat Completions, Realtime y Batch.
- Feature cards pueden representar Image Generation, Web Search y Function Call.
- Controles usan radio 8px; cards 16px; chips de estado 999px; touch targets mínimos 44px.

## Soft contract

Las siguientes decisiones son `inferido` a partir de la estructura pública encontrada:

- Qwen presenta un ecosistema multimodal, no un único chatbot (`inferido`).
- La secuencia Studio → API → Download permite pasar de exploración a construcción y despliegue (`inferido`).
- Model cards con inputs/outputs/contexto convierten capacidades técnicas en criterios de selección (`inferido`).
- La compatibilidad OpenAI-like reduce el costo mental de adopción para desarrolladores (`inferido`).
- La mezcla de modelos abiertos, API y productos de consumo busca una audiencia amplia (`inferido`).

## Colors

| Token | Valor | Uso |
|---|---|---|
| `colors.canvas` | `#FFFFFF` | Fondo principal |
| `colors.surface` | `#F7F8FC` | Cards y bandas |
| `colors.surfaceRaised` | `#FFFFFF` | Card activa |
| `colors.ink` | `#171923` | Texto principal |
| `colors.muted` | `#697386` | Metadata |
| `colors.brand` | `#5B5BD6` | CTA y acento AI |
| `colors.accent` | `#1E88E5` | Links y foco |
| `colors.border` | `#DDE2EC` | Bordes |
| `colors.success` | `#2E9B62` | Estado disponible |
| `colors.error` | `#C5443A` | Error |

Los valores son un snapshot analítico y deben medirse contra CSS computado antes de producción. Verificar contraste de brand/accent en texto pequeño.

## Typography

| Rol | Familia | Tamaño | Peso | Line-height |
|---|---|---:|---:|---:|
| Hero heading | Sans-serif display | 52px | 600 | 1.08 |
| Section heading | Sans-serif display | 32px | 600 | 1.2 |
| Card heading | Sans-serif interface | 20px | 600 | 1.3 |
| Body | Sans-serif interface | 16px | 400 | 1.5 |
| Model metadata | ui-monospace, monospace | 13px | 500 | 1.4 |

La familia exacta de Qwen no se afirma como verificada ni redistribuible. Una adaptación debe usar fuentes con licencia compatible.

## Components

### AI product navigation

Navegación a Studio, API Platform, Download, Models, Docs, Blog y comunidad. Estados: `default`, `hover`, `focus-visible`, `menu-open`, `compact`.

### Hero model CTA

Hero con claim de modelos, entrada a Studio o API y acción Download. Estados: `default`, `hover`, `focus-visible`, `loading`, `reduced-motion`.

### Studio/API/Download cards

Tres puertas de entrada con descripción, visual y CTA. Estados: `default`, `hover`, `selected`, `focus-visible`, `loading`.

### Model card

Card con nombre, inputs, outputs, contexto y Learn more. Estados: `default`, `hover`, `focus-visible`, `unavailable`, `loading`.

### API capability card

Chat Completions, Realtime y Batch con caso de uso y enlace. Estados: `default`, `hover`, `focus-visible`, `expanded`.

### Feature rail and footer

Features de imagen, búsqueda, function call, comunidad y recursos. Estados: `default`, `collapsed-mobile`, `focus-visible`.

## Layout and spacing

- Header: padding lateral 24px desktop y 16px mobile.
- Hero: copy centrado o de ancho limitado con CTA inmediato.
- Entry cards: grid de tres zonas desktop y una columna mobile; gap de 16px.
- Model cards: grid flexible con metadata agrupada y gap de 12px.
- API/features: secciones de dos o tres columnas; footer agrupado por producto y comunidad.

## Responsive

| Rango | Comportamiento |
|---|---|
| 320–543px | Header compacto, hero vertical, cards apiladas y metadata en bloques |
| 544–767px | Grid flexible de dos columnas cuando cabe y rail desplazable |
| 768–1011px | Hero de dos zonas, entry cards adaptables y model grid |
| 1012–1279px | Model/API/features en varias columnas y footer agrupado |
| 1280px+ | Mayor aire exterior sin estirar indefinidamente cards o copy |

Probar 320px, 768px y 1280px, además de teclado, zoom, reduced motion, estados de API y disponibilidad de modelos.

## Do's and Don'ts

- Do: distinguir Studio, API y Download en el primer nivel.
- Do: mostrar inputs/outputs, modalidad, contexto y disponibilidad como texto accesible.
- Do: diferenciar API síncrona, realtime y batch por caso de uso.
- Don't: presentar modelos, context windows o precios como valores permanentes.
- Don't: copiar logo, imágenes, screenshots, fuentes o textos de Qwen sin autorización.
- Don't: hacer que una animación o demo sea necesaria para entender la acción.

## Provenance

- Fuente observada: [Qwen homepage](https://qwen.ai/).
- Referencia pública: [Qwen API Platform](https://qwen.ai/apiplatform) y [Qwen home](https://qwen.ai/home/).
- Fecha de observación: 2026-08-02.
- Límite: la página directa fue parcialmente inaccesible al extractor; algunos hallazgos se basan en páginas públicas indexadas y quedan marcados como advertencias.

## Validation Contract

### PASSED

- El documento separa contrato duro, contrato blando, componentes, estados, responsive y procedencia.
- `design-system.json` contiene tokens, breakpoints y componentes derivados del contrato.
- El preview muestra Studio/API/Download, modelos, capacidades, tokens y validación sin reutilizar assets.
- Se contemplan accesibilidad de model cards, disponibilidad y reduced motion.

### WARNING

- La inspección directa del homepage fue limitada y los colores son snapshot analítico.
- Modelos, capacidades, precios y features cambian con frecuencia.
- Este no es un sistema oficial de Qwen ni una autorización para redistribuir activos.

### Criterios de aceptación

Una implementación pasa cuando conserva la ruta Studio → API → Download, selección de modelos, capacidades multimodales, estados accesibles, tokens y responsive behavior; los assets de marca deben sustituirse por recursos autorizados.
