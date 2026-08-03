---
name: ollama-homepage-analysis
version: 1.0.0
description: Análisis externo y reproducible del homepage público de Ollama; no es un sistema oficial de Ollama.
source: https://ollama.com/
colors: documented-in-design-system-json
typography: utilitarian-developer-sans
rounded: 4px-controls-12px-cards
spacing: 4px-base-scale
components: developer-nav-hero-install-command-app-launcher-cloud-plan-privacy-footer
---

# Ollama Homepage — Design System Analysis

## Overview

Este documento analiza el homepage público de Ollama observado el 2 de agosto de 2026. La experiencia posiciona Ollama como una vía simple para construir con modelos abiertos, combina instalación por terminal, descarga, apps/agentes, ejecución local, cloud, plan Pro, privacidad y enlaces de docs/GitHub. Es un análisis externo, no una especificación oficial.

El sitio está orientado a desarrolladores y prioriza el primer comando ejecutable. Los comandos, modelos, precios, integraciones y claims pueden cambiar; no se redistribuyen logo, screenshots, fuentes ni textos completos.

## Contrato duro

- El lienzo usa `{colors.canvas}` y las superficies de código usan `{colors.codeSurface}`.
- El texto principal usa `{colors.ink}`; el texto auxiliar usa `{colors.muted}`.
- El CTA de instalación usa `{colors.brand}`; los bordes usan `{colors.border}`.
- El hero debe incluir una propuesta sobre modelos abiertos, un bloque de comando instalable y un CTA de descarga/get started.
- El bloque de terminal presenta comando, prompt, menú de apps/agentes y estados de disponibilidad.
- La narrativa distingue local/offline de cloud/scale y conecta ambas rutas con CTA.
- El plan Pro usa una card de precio, uso, frecuencia y acción de compra.
- El bloque de privacidad comunica ownership de datos, regiones cloud y operación offline.
- Controles usan radio 4px; cards y paneles hasta 12px; touch targets mínimos 44px.

## Soft contract

Las siguientes decisiones son `inferido` a partir de la composición observable:

- La interfaz busca reducir la distancia entre landing page y terminal (`inferido`).
- El comando curl funciona como prueba inmediata de valor y como elemento de identidad (`inferido`).
- “Start local. Scale with cloud.” presenta la arquitectura como una decisión gradual, no como una dicotomía (`inferido`).
- El lenguaje de privacidad responde a objeciones de seguridad y control de datos (`inferido`).
- Apps/agentes y modelos se comunican como un ecosistema que crece alrededor de una herramienta local (`inferido`).

## Colors

| Token | Valor | Uso |
|---|---|---|
| `colors.canvas` | `#FFFFFF` | Fondo principal |
| `colors.surface` | `#F5F5F3` | Secciones y cards |
| `colors.codeSurface` | `#111111` | Terminal y comandos |
| `colors.ink` | `#171717` | Texto principal |
| `colors.muted` | `#6B6B6B` | Copy auxiliar |
| `colors.brand` | `#1F8F5F` | CTA y estado activo |
| `colors.accent` | `#E36A32` | Acento secundario |
| `colors.border` | `#D8D8D3` | Bordes |
| `colors.success` | `#2E9B62` | Disponibilidad/confirmación |
| `colors.error` | `#C5443A` | Error |

Los colores son un snapshot analítico porque la fuente pública no expone aquí todos los valores computados. Medir contraste de CTA, terminal y metadata antes de producción.

## Typography

| Rol | Familia | Tamaño | Peso | Line-height |
|---|---|---:|---:|---:|
| Hero heading | Sans-serif de interfaz | 56px | 600 | 1.05 |
| Section heading | Sans-serif de interfaz | 32px | 600 | 1.2 |
| Card heading | Sans-serif interface | 20px | 600 | 1.3 |
| Body | Sans-serif interface | 16px | 400 | 1.5 |
| Terminal | ui-monospace, monospace | 14px | 400 | 1.5 |
| Metadata | Sans-serif interface | 13px | 500 | 1.4 |

La familia exacta de Ollama no se afirma como verificada ni redistribuible. Una adaptación debe usar una fuente con licencia compatible.

## Components

### Developer navigation

Navegación con producto, Download, Blog, Docs, GitHub, Discord y cuenta. Estados: `default`, `hover`, `focus-visible`, `menu-open`, `compact`.

### Hero install command

Propuesta de valor, comando curl, copy de terminal y Download/Get started. Estados: `default`, `copied`, `error`, `focus-visible`, `loading`.

### App launcher terminal

Menú para Run a model, Claude Code, Codex, OpenClaw y More. Estados: `idle`, `selected`, `unavailable`, `loading`, `error`.

### Local/cloud split

Sección que explica local, cloud, hardware, parallel requests y web information. Estados: `default`, `hover`, `focus-visible`, `expanded`.

### Pro plan card

Card con uso mensual, precio, periodo y Get Pro. Estados: `default`, `recommended`, `selected`, `disabled`, `error`.

### Privacy statement

Bloque de datos no entrenados, regiones cloud y offline. Estados: `default`, `expanded`, `focus-visible`.

## Layout and spacing

- Header: padding lateral 24px desktop y 16px mobile.
- Hero: copy centrado con comando de ancho limitado y CTAs próximos.
- Terminal: superficie oscura, padding 20px, radio 12px y tipografía monoespaciada.
- Local/cloud: grid de dos zonas desktop, una columna mobile.
- Plan: card con precio destacado y lista de beneficios separada por 8px.
- Footer: grupos de docs, comunidad, contacto y legal con gap de 24px.

## Responsive

| Rango | Comportamiento |
|---|---|
| 320–543px | Header compacto, hero vertical, comando con wrapping y cards apiladas |
| 544–767px | Terminal flexible, local/cloud en una o dos columnas y CTAs adaptables |
| 768–1011px | Hero de dos zonas, app launcher amplio y plan grid adaptable |
| 1012–1279px | Contenedor amplio, local/cloud en columnas y footer agrupado |
| 1280px+ | Mayor aire exterior sin ampliar indefinidamente el bloque de comando |

Probar 320px, 768px y 1280px, además de teclado, copiado de comandos, reduced motion, zoom y estados de red/offline.

## Do's and Don'ts

- Do: hacer el comando copiable, legible y acompañado de una alternativa Download.
- Do: diferenciar local/offline, cloud y Pro con texto, estados y condiciones.
- Do: anunciar si una app o integración no está instalada/disponible.
- Don't: ejecutar comandos automáticamente desde una landing page.
- Don't: presentar claims de privacidad, regiones, precio o disponibilidad como inmutables.
- Don't: copiar logo, screenshots o fuentes de Ollama sin autorización.

## Provenance

- Fuente observada: [Ollama homepage](https://ollama.com/).
- Fecha de observación: 2026-08-02.
- Evidencia visible: hero de open models, comando curl, download, apps/agentes, local/cloud, plan Pro, privacidad, Blog, Docs, GitHub, Discord y Terms.
- Límite: modelos, integraciones, precios, claims y disponibilidad cambian con el producto.

## Validation Contract

### PASSED

- El documento separa contrato duro, contrato blando, componentes, estados, responsive y procedencia.
- `design-system.json` contiene tokens, breakpoints y componentes derivados del contrato.
- El preview muestra comando, terminal, local/cloud, plan, privacidad, tokens y validación.
- Se contemplan copiado de comandos, disponibilidad, offline, teclado y reduced motion.

### WARNING

- Los colores son snapshot analítico y requieren medición CSS computada.
- Precios, modelos, integraciones y claims pueden cambiar rápidamente.
- Este no es un sistema oficial de Ollama ni una autorización para redistribuir activos.

### Criterios de aceptación

Una implementación pasa cuando conserva el primer comando ejecutable, la separación local/cloud, estados de terminal, plan transparente, privacidad y responsive behavior; ningún comando debe ejecutarse sin una acción explícita del usuario.
