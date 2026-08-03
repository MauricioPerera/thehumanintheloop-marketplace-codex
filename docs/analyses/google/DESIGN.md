---
name: google-homepage-analysis
version: 1.0.0
description: Análisis externo y reproducible del homepage público de Google; no es un sistema oficial de Google.
source: https://www.google.com/
colors: documented-in-design-system-json
typography: google-sans-roboto-stack
rounded: 4px-buttons-24px-search
spacing: 4px-base-scale
components: utility-header-search-box-search-actions-footer
---

# Google Homepage — Design System Analysis

## Overview

Este documento analiza la interfaz observable del homepage público de Google el 2 de agosto de 2026. Es un análisis externo para auditoría y reconstrucción; no es una especificación oficial de Google y no redistribuye su logotipo, tipografías propietarias, imágenes ni textos protegidos.

La página concentra una tarea primaria: búsqueda. La jerarquía observable es deliberadamente mínima: enlaces utilitarios superiores, área central con marca y campo de búsqueda, acciones secundarias y footer con enlaces legales, de configuración y de producto.

## Contrato duro

- El lienzo base usa `{colors.canvas}` y el texto principal usa `{colors.ink}`.
- El texto auxiliar y los enlaces de navegación secundaria usan `{colors.muted}`.
- El foco y los enlaces de acción usan `{colors.accent}`.
- La búsqueda es un control horizontal de aproximadamente 46px de altura, con radio de 24px y borde `{colors.border}`.
- Los botones de acción secundaria usan superficie `{colors.buttonSurface}`, texto `{colors.ink}` y radio de 4px.
- La familia de texto de interfaz es `Roboto, Arial, sans-serif`; los títulos de marca deben tratarse como un activo no redistribuible.
- La escala base de espaciado es 4px; los gutters del viewport estrecho son 16px.
- La página conserva una sola tarea primaria y no debe añadir tarjetas, banners o navegación que compitan con la búsqueda.
- En viewport estrecho el header mantiene acciones utilitarias compactas y el campo de búsqueda ocupa el ancho disponible.

## Soft contract

Todas las siguientes decisiones son `inferido` a partir de la composición observada:

- La intención visual es neutral, rápida y de baja carga cognitiva (`inferido`).
- El espacio vacío alrededor del buscador funciona como jerarquía y no como contenido faltante (`inferido`).
- El footer agrupa controles legales y de configuración como navegación de baja prioridad (`inferido`).
- El botón secundario con gris muy claro reduce énfasis frente al campo de búsqueda (`inferido`).
- La ausencia de una navegación de categorías visible favorece el foco en la tarea primaria (`inferido`).

## Colors

| Token | Valor | Uso |
|---|---|---|
| `colors.canvas` | `#FFFFFF` | Fondo general |
| `colors.ink` | `#202124` | Texto y controles principales |
| `colors.muted` | `#5F6368` | Texto secundario y navegación |
| `colors.accent` | `#1A73E8` | Enlaces, foco y acciones |
| `colors.border` | `#DADCE0` | Borde de búsqueda y divisores |
| `colors.buttonSurface` | `#F8F9FA` | Fondo de botones secundarios |
| `colors.hoverSurface` | `#F1F3F4` | Hover de controles y superficies |
| `colors.error` | `#D93025` | Error de formulario |
| `colors.success` | `#188038` | Confirmación |

Contraste de referencia: `colors.ink` sobre `colors.canvas` es aproximadamente 16:1; `colors.muted` sobre `colors.canvas` es aproximadamente 6:1; `colors.accent` sobre `colors.canvas` es aproximadamente 4.5:1. El cálculo debe repetirse para temas o estados nuevos.

## Typography

| Rol | Familia | Tamaño | Peso | Line-height |
|---|---|---:|---:|---:|
| Utility link | Roboto, Arial, sans-serif | 13px | 400 | 1.4 |
| Search input | Roboto, Arial, sans-serif | 16px | 400 | 1.5 |
| Action button | Roboto, Arial, sans-serif | 14px | 500 | 1.4 |
| Footer link | Roboto, Arial, sans-serif | 14px | 400 | 1.4 |
| Code/reference | ui-monospace, monospace | 13px | 400 | 1.45 |

Google Sans y el wordmark deben considerarse referencias visuales no redistribuibles. Una implementación independiente debe usar una fuente permitida por su propia licencia.

## Components

### Utility header

Fila superior con enlaces de producto y soporte, acceso a imágenes, entrada de sesión y un control de aplicaciones. Estados: `default`, `hover`, `focus-visible`, `compact`.

### Search box

Control principal con affordances para texto, búsqueda por voz e imagen. Estados: `empty`, `typing`, `focus`, `submitted`, `error`, `disabled`. Los iconos deben tener nombres accesibles y nunca ser la única forma de comunicar el estado.

### Search actions

Grupo de botones secundarios para ejecutar la búsqueda y una acción alternativa. Estados: `default`, `hover`, `active`, `focus-visible`, `disabled`.

### Footer navigation

Dos grupos de enlaces de baja prioridad: enlaces utilitarios y configuración. Estados: `default`, `hover`, `focus-visible`; en mobile deben envolver o apilarse sin overflow.

## Layout and spacing

- Contenedor de header: ancho completo, padding lateral 16px y padding vertical 12px.
- Zona principal: layout vertical centrado; el buscador limita su ancho a 584px en desktop.
- Campo de búsqueda: min-height 46px, padding horizontal 16px y separación de iconos de 12px.
- Grupo de botones: separación de 8px, margen superior de 18px.
- Footer: superficie `{colors.buttonSurface}`, borde superior `{colors.border}`, enlaces agrupados con separación de 24px.
- Touch target recomendado: al menos 44px para iconos y acciones en mobile.

## Responsive

| Rango | Comportamiento |
|---|---|
| 320–543px | Header compacto, buscador a 100% menos 32px, botones con wrapping y footer apilable |
| 544–767px | Buscador centrado con ancho flexible; enlaces mantienen una línea si hay espacio |
| 768–1279px | Layout desktop, buscador hasta 584px y footer horizontal |
| 1280px+ | Mantener la misma columna de tarea; el espacio adicional no debe ampliar indefinidamente el control |

El análisis debe probar 320px, 768px y 1280px, además de zoom del navegador, contraste alto, teclado y `prefers-reduced-motion`.

## Do's and Don'ts

- Do: conservar una acción primaria clara, labels accesibles y foco visible.
- Do: usar tokens semánticos y medir contraste después de cambiar un estado.
- Don't: copiar el logotipo, el wordmark, iconos o tipografías de Google sin permiso o licencia.
- Don't: convertir el espacio vacío en una galería de contenido que compita con la búsqueda.
- Don't: depender solo del color para comunicar error, foco o éxito.

## Provenance

- Fuente observada: [Google homepage](https://www.google.com/).
- Fecha de observación: 2026-08-02.
- Evidencia visible: enlaces de Images, Sign in, campo de entrada, acciones de búsqueda, Privacy, Terms, Settings, Feedback, Help, Advertising, Business y About.
- Límites: el contenido puede variar por país, idioma, sesión, experimento, dispositivo y disponibilidad de servicios.

## Validation Contract

### PASSED

- `DESIGN.md` contiene contrato duro, contrato blando, procedencia y validación.
- `design-system.json` deriva sus valores de este documento y no contiene referencias rotas.
- El preview muestra tokens, tipografía, componentes, estados, responsive behavior y enlaces a la fuente.
- Los contrastes de referencia y touch targets están documentados como criterios medibles.

### WARNING

- El análisis no representa el sistema oficial de Google.
- Las marcas, iconos, textos, experimentos y estilos pueden cambiar por región o fecha.
- El reporte no sustituye revisión legal, accesibilidad completa ni pruebas con lectores de pantalla.

### Criterios de aceptación

Una implementación pasa cuando conserva la primacía de la búsqueda, tokens, radios, estados accesibles, límites de layout y comportamiento responsive; cualquier diferencia debe registrarse como decisión propia.
