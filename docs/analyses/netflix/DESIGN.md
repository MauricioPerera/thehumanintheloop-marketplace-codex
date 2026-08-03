---
name: netflix-homepage-analysis
version: 1.0.0
description: Análisis externo y reproducible del homepage público de Netflix; no es un sistema oficial de Netflix.
source: https://www.netflix.com/
colors: documented-in-design-system-json
typography: sans-serif-streaming-ui
rounded: 4px-controls-2px-inputs
spacing: 4px-base-scale
components: brand-header-hero-email-form-promo-rail-faq-footer
---

# Netflix Homepage — Design System Analysis

## Overview

Este documento analiza el homepage público de Netflix observado el 2 de agosto de 2026. La experiencia observada combina un header mínimo, hero de adquisición, email signup, promoción de plan, ranking Trending Now, razones para unirse, FAQ y footer de soporte/legal. Es un análisis externo para auditoría y reconstrucción; no es una especificación oficial de Netflix.

La página puede variar por país, idioma, cookies, dispositivo y campaña. No se redistribuyen logotipos, artwork, fotografías, tipografías propietarias, nombres de títulos ni textos completos.

## Contrato duro

- El lienzo usa `{colors.canvas}`; el texto principal usa `{colors.ink}` y el texto auxiliar `{colors.muted}`.
- La acción de marca usa `{colors.brand}` con texto `{colors.ink}`; los estados de error usan `{colors.error}`.
- El hero debe comunicar una propuesta de entretenimiento, precio o cancelación, seguido de un formulario de email con CTA.
- El header conserva selector de idioma y Sign In; en mobile mantiene ambos sin overflow.
- El formulario usa input de aproximadamente 56px de altura, radio 2px y CTA de min-height 56px con radio 4px.
- El bloque de trending usa cards o posters numerados y debe mantener el orden y el número visible como información accesible.
- Las razones para unirse usan cards o columnas con icono/ilustración, heading y descripción; no dependen solo de la imagen.
- FAQ usa disclosure/accordion con foco visible, estado expandido y contenido navegable por teclado.
- Spacing base de 4px, gutters de 16px mobile y 48px desktop; secciones separadas por superficies o divisores.

## Soft contract

Las siguientes decisiones son `inferido` a partir de la composición observable:

- El negro y el rojo producen urgencia, contraste y reconocimiento de marca (`inferido`).
- La secuencia hero → email → prueba social → beneficios → FAQ reduce objeciones antes del registro (`inferido`).
- La numeración grande de Trending Now transforma el catálogo en una señal editorial (`inferido`).
- Repetir el email signup al final recupera usuarios que no convirtieron al inicio (`inferido`).
- El footer denso combina soporte, confianza, legal y descubrimiento corporativo (`inferido`).

## Colors

| Token | Valor | Uso |
|---|---|---|
| `colors.canvas` | `#141414` | Fondo principal |
| `colors.surface` | `#232323` | Cards y paneles |
| `colors.surfaceRaised` | `#333333` | Hover y estados elevados |
| `colors.ink` | `#FFFFFF` | Texto principal y CTA sobre rojo |
| `colors.muted` | `#B3B3B3` | Texto auxiliar |
| `colors.brand` | `#E50914` | CTA y acento de marca |
| `colors.border` | `#5C5C5C` | Bordes de inputs y divisores |
| `colors.success` | `#46D369` | Confirmación |
| `colors.error` | `#EB3942` | Error de formulario |

Contraste de referencia: `{colors.ink}` sobre `{colors.canvas}` supera 15:1; `{colors.muted}` sobre `{colors.canvas}` supera 7:1; `{colors.ink}` sobre `{colors.brand}` debe medirse por tamaño y peso antes de usarlo en texto pequeño.

## Typography

| Rol | Familia | Tamaño | Peso | Line-height |
|---|---|---:|---:|---:|
| Hero heading | Sans-serif de interfaz | 48px | 700 | 1.1 |
| Section heading | Sans-serif de interfaz | 32px | 700 | 1.2 |
| Card heading | Sans-serif de interfaz | 20px | 600 | 1.3 |
| Body | Sans-serif de interfaz | 16px | 400 | 1.5 |
| Label / footer | Sans-serif de interfaz | 13px | 400 | 1.4 |
| Code / reference | ui-monospace, monospace | 13px | 400 | 1.45 |

La fuente exacta de Netflix no se afirma como verificada ni redistribuible. Una implementación propia debe usar una sans-serif con licencia compatible.

## Components

### Brand header

Logo o identidad, selector de idioma y Sign In. Estados: `default`, `hover`, `focus-visible`, `language-open`, `compact`.

### Hero and email form

Propuesta de valor, precio/cancelación, email input y CTA Get Started. Estados: `empty`, `focus`, `invalid`, `loading`, `success`, `disabled`.

### Promo card

Banda de plan accesible con beneficio, copy y Learn More. Estados: `default`, `hover`, `focus-visible`, `dismissed`.

### Trending rail

Cards numeradas con poster, título y metadata. Estados: `default`, `hover`, `focus-visible`, `loading`, `empty`.

### Benefit card

Card o columna para dispositivos, descargas, watch everywhere y perfiles infantiles. Estados: `default`, `hover`, `focus-visible`.

### FAQ disclosure

Preguntas expandibles con icono, contenido y cierre. Estados: `collapsed`, `expanded`, `focus-visible`, `loading`.

### Footer navigation

FAQ, Help Center, Account, Ways to Watch, privacidad, términos, idioma y contacto. Estados: `default`, `hover`, `focus-visible`, `stacked-mobile`.

## Layout and spacing

- Header: ancho completo, padding lateral 24px desktop y 16px mobile.
- Hero: altura amplia con overlay y copy centrado; max-width aproximado de 950px para el bloque editorial.
- Email form: inline en desktop, apilado en mobile; gap de 8px.
- Secciones: padding vertical de 48px, divisores de 8px o superficies separadas cuando se requiere ritmo.
- Trending: rail horizontal con gap de 16px y cards que conservan relación de poster.
- FAQ: contenido con max-width de 900px; cada disclosure debe anunciar su estado.

## Responsive

| Rango | Comportamiento |
|---|---|
| 320–543px | Hero vertical, copy reducido, email y CTA apilados, trending desplazable y FAQ a una columna |
| 544–767px | Formulario flexible, benefits en dos columnas cuando cabe y footer parcialmente apilado |
| 768–1011px | Hero amplio, formulario inline y benefits en varias columnas |
| 1012–1279px | Contenedor editorial amplio, rail de posters y FAQ limitado |
| 1280px+ | Mayor aire exterior sin ampliar indefinidamente la lectura o el formulario |

Probar 320px, 768px y 1280px, además de teclado, zoom, reduced motion, alto contraste, validación de email y lector de pantalla.

## Do's and Don'ts

- Do: explicar precio, cancelación, prueba y acción del email antes de pedir datos.
- Do: mantener FAQ usable y beneficios comprensibles sin artwork.
- Do: comunicar estados de email con texto y foco, no solo color.
- Don't: copiar artwork, títulos, logo o tipografía de Netflix sin permiso.
- Don't: ocultar condiciones de renovación, precio o disponibilidad regional.
- Don't: usar un carousel que no pueda operarse por teclado o que bloquee el contenido.

## Provenance

- Fuente observada: [Netflix homepage](https://www.netflix.com/).
- Fecha de observación: 2026-08-02.
- Evidencia visible: selector de idioma, Sign In, propuesta de valor, precio/cancelación, email signup, Get Started, promo de plan, Trending Now, benefits, FAQ y footer.
- Límite: precio, títulos, idioma, campañas, arte y enlaces varían por país y fecha.

## Validation Contract

### PASSED

- El documento contiene contrato duro, contrato blando, componentes, estados, responsive y procedencia.
- `design-system.json` contiene tokens, breakpoints y componentes derivados del contrato.
- El preview muestra hero, formulario, trending, benefits, FAQ, tokens y validación sin reutilizar activos.
- Se contemplan accesibilidad de disclosure, validación de email, touch targets y reduced motion.

### WARNING

- El precio y el contenido observado son regionales y dinámicos.
- La experiencia real puede cambiar por campaña, cookies, sesión y dispositivo.
- Este no es un sistema oficial de Netflix ni una autorización para redistribuir sus activos.

### Criterios de aceptación

Una implementación pasa cuando mantiene la secuencia de adquisición, formulario accesible, señal editorial, beneficios, FAQ, footer y responsive behavior; todos los contenidos de marca deben sustituirse por recursos autorizados.
