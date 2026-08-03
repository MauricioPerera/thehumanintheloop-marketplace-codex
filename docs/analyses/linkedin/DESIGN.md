---
name: linkedin-homepage-analysis
version: 1.0.0
description: Análisis externo y reproducible del homepage público de LinkedIn; no es un sistema oficial de LinkedIn.
source: https://www.linkedin.com/
colors: documented-in-design-system-json
typography: system-ui-linkedin-sans-inference
rounded: 4px-controls-24px-pills
spacing: 4px-base-scale
components: utility-header-auth-card-content-sections-footer
---

# LinkedIn Homepage — Design System Analysis

## Overview

Este documento analiza el homepage público de LinkedIn observado el 2 de agosto de 2026. La página accesible sin sesión combina un acceso/registro prominente con navegación de contenido profesional, empleo, aprendizaje, soluciones de negocio y directorios. Es un análisis externo para auditoría y reconstrucción; no es una especificación oficial de LinkedIn.

La fuente puede mostrar consentimiento de cookies, variaciones regionales, experimentos y estados de autenticación. Por eso cada hallazgo se separa entre observado, inferido o no verificable, y no se incluyen logos, fotografías, textos completos ni otros activos protegidos.

## Contrato duro

- La acción primaria de registro usa `{colors.brand}` sobre fondo blanco; la acción de acceso usa `{colors.brand}` o una variante outline según el estado de la experiencia.
- El texto principal usa `{colors.ink}`; el texto auxiliar usa `{colors.muted}`.
- Las superficies de contenido alternan `{colors.canvas}` con `{colors.surface}` y pueden usar `{colors.warmSurface}` para secciones editoriales.
- Los bordes de cards y formularios usan `{colors.border}` y los estados de error usan `{colors.error}`.
- La familia de interfaz debe usar una sans-serif de sistema permitida; la familia exacta de marca es no verificable sin inspección autorizada de assets.
- Los controles usan radio 4px; chips, pills y estados redondeados usan 24px.
- Los botones y enlaces de navegación deben tener un objetivo táctil mínimo de 44px en mobile.
- El layout usa una columna central en mobile, tarjetas de contenido y grupos de enlaces en footer; la navegación secundaria se colapsa cuando no hay espacio.
- La jerarquía debe mantener una propuesta profesional clara: entrar o registrarse, explorar oportunidades y encontrar contenido útil.

## Soft contract

Las siguientes decisiones son `inferido` a partir de la estructura y copy visibles:

- La interfaz busca transmitir confianza profesional y orientación a oportunidades (`inferido`).
- El azul de marca comunica acción y pertenencia; el beige cálido introduce una capa editorial menos transaccional (`inferido`).
- Las categorías de contenido funcionan como puertas de entrada para distintos jobs-to-be-done (`inferido`).
- La presencia de login y cookie consent antes de explorar el contenido indica una estrategia de conversión y cumplimiento (`inferido`).
- El footer denso prioriza descubrimiento SEO y navegación por directorios (`inferido`).

## Colors

| Token | Valor | Uso |
|---|---|---|
| `colors.canvas` | `#FFFFFF` | Fondo principal |
| `colors.surface` | `#F3F2EF` | Paneles y bandas suaves |
| `colors.warmSurface` | `#E9E5DF` | Bloques editoriales |
| `colors.ink` | `#1D2226` | Texto principal |
| `colors.muted` | `#56687A` | Texto secundario |
| `colors.brand` | `#0A66C2` | CTA, enlaces y foco |
| `colors.border` | `#D0D9E3` | Bordes y divisores |
| `colors.hoverSurface` | `#EEF3F8` | Hover y selección suave |
| `colors.success` | `#057642` | Confirmación |
| `colors.error` | `#CC1016` | Error y validación |
| `colors.warning` | `#915907` | Advertencia |

Contraste de referencia: `colors.ink` sobre `colors.canvas` supera 12:1; `colors.muted` sobre `colors.canvas` supera 5:1; `colors.brand` sobre `colors.canvas` supera 4.5:1. Recalcular para cualquier tema, overlay o estado nuevo.

## Typography

| Rol | Familia | Tamaño | Peso | Line-height |
|---|---|---:|---:|---:|
| Hero heading | Sans de sistema | 40px | 400 | 1.2 |
| Section heading | Sans de sistema | 32px | 600 | 1.25 |
| Card heading | Sans de sistema | 20px | 600 | 1.3 |
| Body | Sans de sistema | 16px | 400 | 1.5 |
| Utility / label | Sans de sistema | 14px | 600 | 1.4 |
| Code / reference | ui-monospace, monospace | 13px | 400 | 1.45 |

La familia exacta de LinkedIn Sans no se afirma como disponible. Una implementación independiente debe sustituirla por una familia con licencia compatible.

## Components

### Utility header and auth actions

Header con identidad, enlaces a Top Content, People, Learning, Jobs y Games, más Join now y Sign in. Estados: `default`, `hover`, `focus-visible`, `compact`, `cookie-consent`.

### Authentication card

Card o zona de registro con campos, acción de continuar y enlaces legales. Estados: `empty`, `focus`, `invalid`, `loading`, `disabled`, `success`.

### Content category links

Listas de categorías para contenido profesional, empleos, software y aprendizaje. Estados: `default`, `hover`, `focus-visible`, `expanded`, `collapsed`.

### Opportunity CTA

Bloques para publicar un empleo, activar Open to Work, conectar con personas y comenzar. Estados: `default`, `hover`, `pressed`, `focus-visible`.

### Footer directory

Footer con grupos General, Browse LinkedIn, Business Solutions, Directories y políticas. Estados: `default`, `hover`, `focus-visible`, `stacked-mobile`.

## Layout and spacing

- Header: ancho completo, padding lateral 24px en desktop y 16px en mobile.
- Hero/auth: grid de dos zonas en desktop; se apila en mobile.
- Cards: padding interno 24px, borde de 1px y radio 8px cuando la tarjeta es contenedora.
- Listas: separación vertical 8px entre enlaces; grupos mayores separados por 24px.
- Secciones: padding vertical de 48px; hero puede usar 64px en desktop.
- CTA: min-height 44px, padding horizontal 16px y gap de 8px entre acciones.

## Responsive

| Rango | Comportamiento |
|---|---|
| 320–543px | Header compacto, auth y hero a una columna, listas que envuelven y footer apilado |
| 544–767px | Cards y categorías en grilla flexible; CTA ocupa ancho disponible cuando corresponde |
| 768–1011px | Grid de dos zonas, navegación regular y footer parcialmente agrupado |
| 1012–1279px | Contenedor amplio, hero con copy y auth separados, listas de categorías en columnas |
| 1280px+ | Mantener ancho de lectura limitado; aumentar aire exterior sin estirar el contenido |

Probar 320px, 768px y 1280px, además de teclado, zoom, alto contraste, orientación y `prefers-reduced-motion`. Los enlaces y botones no deben depender únicamente de hover.

## Do's and Don'ts

- Do: hacer evidente si la persona va a iniciar sesión, registrarse o explorar como visitante.
- Do: conservar una jerarquía profesional y proporcionar foco visible en cada enlace.
- Do: distinguir estados de consentimiento y autenticación de los estados de contenido.
- Don't: reutilizar fotos, logotipos, iconos o textos de LinkedIn sin licencia.
- Don't: ocultar términos legales, privacidad o controles de cookies.
- Don't: crear listas de enlaces inaccesibles o confiar solo en color para comunicar estado.

## Provenance

- Fuente observada: [LinkedIn homepage](https://www.linkedin.com/).
- Fecha de observación: 2026-08-02.
- Evidencia visible: consentimiento de cookies, Login/Sign Up, navegación Top Content/People/Learning/Jobs/Games, registro, contenido profesional, empleo, software, aprendizaje, soluciones y footer de directorios.
- Límite crítico: el sitio puede variar con sesión, locale, experimentos, consentimiento y disponibilidad de contenido.

## Validation Contract

### PASSED

- El documento separa contrato duro, contrato blando y validación.
- Los tokens de color, spacing, radios y breakpoints están presentes en `design-system.json`.
- Cada componente tiene estados y el preview expone la procedencia y los artefactos.
- El contrato contempla auth, consentimiento, responsive y touch targets.

### WARNING

- El análisis no representa el sistema oficial de LinkedIn.
- La familia tipográfica exacta, valores computados y estados autenticados no son verificables desde el acceso público observado.
- Debe hacerse revisión legal antes de redistribuir cualquier adaptación visual o activo.

### Criterios de aceptación

Una implementación pasa cuando mantiene la jerarquía de acceso/registro, contenido profesional, oportunidades, categorías, estados accesibles, tokens y comportamiento responsive; las decisiones no observables deben quedar marcadas como inferidas.
