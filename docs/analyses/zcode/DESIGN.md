---
name: zcode-homepage-analysis
version: 1.0.0
description: Análisis externo y reproducible del homepage público de ZCode; no es un sistema oficial de Z.ai.
source: https://zcode.z.ai/en
colors: documented-in-design-system-json
typography: dark-agentic-developer-sans
rounded: 8px-controls-16px-cards
spacing: 4px-base-scale
components: agent-nav-hero-workspace-task-board-pricing-card-capability-card-download-footer
---

# ZCode Homepage — Design System Analysis

## Overview

Este documento analiza `zcode.z.ai/en` observado el 2 de agosto de 2026. La página presenta ZCode como un harness de coding agentic optimizado para GLM-5.2, con hero, descarga, workspace/task board, multi-agent collaboration, planes GLM Coding, capacidades y descargas por plataforma. Es un análisis externo, no una especificación oficial de Z.ai.

El sitio expone datos de producto, precios, versiones y ejemplos de tareas que pueden cambiar. No se redistribuyen logo, screenshots, fuentes, nombres de clientes, código ni textos completos.

## Contrato duro

- La experiencia usa un lienzo oscuro con superficies de workspace y un acento de acción; los tokens están en `design-system.json`.
- La navegación debe exponer login, anuncio de release, Download, New Task, Open Workspace y Skills.
- El hero comunica agentic coding y ofrece Download, además de una acción para explorar capacidades.
- El workspace mock muestra Tasks, proyectos, subtareas, duración y estados de agente.
- Pricing separa Lite, Pro y Max con uso, precio, beneficios y CTA.
- Capabilities distinguen long-running tasks, bot control e integración profunda con GLM-5.2.
- Downloads distinguen macOS Apple Silicon/Intel, Windows x64/ARM64 y Linux beta.
- Controles usan radio 8px; cards 16px; chips 999px; touch targets mínimos 44px.

## Soft contract

Las siguientes decisiones son `inferido` a partir de la composición observable:

- La UI busca hacer visible el trabajo de agentes, no solo su resultado (`inferido`).
- Task board y timeline convierten autonomía en una secuencia auditable (`inferido`).
- Pricing junto a capacidades comunica que el producto es una herramienta profesional recurrente (`inferido`).
- El lenguaje “simple, fast, vibe-ready” reduce la fricción de entrada para distintos perfiles de desarrollador (`inferido`).
- Las plataformas y canales de bot muestran un producto que continúa fuera del editor (`inferido`).

## Colors

| Token | Valor | Uso |
|---|---|---|
| `colors.canvas` | `#0D0E12` | Fondo principal |
| `colors.surface` | `#171922` | Workspace y cards |
| `colors.surfaceRaised` | `#252838` | Hover y panel elevado |
| `colors.ink` | `#F7F8FA` | Texto principal |
| `colors.muted` | `#A4A8B5` | Metadata |
| `colors.brand` | `#7C6BFF` | CTA y selección |
| `colors.accent` | `#58C7D9` | Enlaces y foco |
| `colors.border` | `#363A4B` | Bordes y divisores |
| `colors.success` | `#65D391` | Estado completado |
| `colors.error` | `#F28B82` | Error |

Los valores cromáticos son un snapshot analítico y deben verificarse con CSS computado antes de producción. Medir contraste de brand/accent sobre cada superficie.

## Typography

| Rol | Familia | Tamaño | Peso | Line-height |
|---|---|---:|---:|---:|
| Hero heading | Sans-serif display | 56px | 600 | 1.05 |
| Section heading | Sans-serif display | 36px | 600 | 1.15 |
| Card heading | Sans-serif interface | 20px | 600 | 1.3 |
| Body | Sans-serif interface | 16px | 400 | 1.5 |
| Task / terminal | ui-monospace, monospace | 13px | 400 | 1.45 |
| Metadata | Sans-serif interface | 13px | 500 | 1.4 |

La familia exacta de ZCode no se afirma como verificada ni redistribuible. Una adaptación debe usar una fuente compatible con su licencia.

## Components

### Agent navigation

Login, release announcement, Download, New Task, Open Workspace y Skills. Estados: `default`, `hover`, `focus-visible`, `menu-open`, `compact`.

### Hero download CTA

Claim de agentic coding, Download y Explore use cases. Estados: `default`, `hover`, `focus-visible`, `loading`, `reduced-motion`.

### Workspace task board

Tasks, workspaces, subtasks, tiempos, agentes y estados de ejecución. Estados: `idle`, `running`, `completed`, `failed`, `paused`, `empty`.

### Pricing card

Lite, Pro y Max con uso, precio, beneficios y acción. Estados: `default`, `popular`, `selected`, `disabled`, `error`.

### Capability card

Long-running tasks, Bot control y GLM integration con visual y descripción. Estados: `default`, `hover`, `focus-visible`, `featured`.

### Download matrix

Instaladores por plataforma y arquitectura, incluyendo Linux beta. Estados: `default`, `hover`, `focus-visible`, `unavailable`.

## Layout and spacing

- Header: padding lateral 24px desktop y 16px mobile.
- Hero: copy de ancho limitado con CTA y visual de workspace separado.
- Task board: panel oscuro con filas de tareas y timeline; gap de 12px.
- Pricing: tres cards en desktop, una columna mobile; gap de 16px.
- Capabilities: grid de tres cards y footer agrupado por producto/recursos.
- Downloads: matriz por OS/arquitectura con labels visibles y estados beta explícitos.

## Responsive

| Rango | Comportamiento |
|---|---|
| 320–543px | Menú compacto, hero vertical, task board apilado y pricing en una columna |
| 544–767px | Grid flexible, capabilities de dos columnas si caben y CTAs adaptables |
| 768–1011px | Hero de dos zonas, workspace amplio y pricing adaptable |
| 1012–1279px | Pricing de tres columnas, capabilities densas y downloads agrupados |
| 1280px+ | Mayor aire exterior sin estirar indefinidamente el workspace |

Probar 320px, 768px y 1280px, además de teclado, zoom, reduced motion, estados de agente, descarga no disponible y foco en la task board.

## Do's and Don'ts

- Do: comunicar el estado de cada tarea con texto, duración y acción disponible.
- Do: distinguir pricing, plataforma, arquitectura y estado beta de forma explícita.
- Do: ofrecer Download además de una acción de exploración o demo.
- Don't: presentar precios, versiones GLM, tareas de ejemplo o disponibilidad como permanentes.
- Don't: copiar screenshots, logo, fuentes o código de ZCode sin autorización.
- Don't: usar animación para ocultar fallos o hacer incomprensible el estado del agente.

## Provenance

- Fuente observada: [ZCode](https://zcode.z.ai/en).
- Fecha de observación: 2026-08-02.
- Evidencia visible: ZCode 3.0, GLM-5.2, hero, Download, New Task, Open Workspace, Skills, tasks, workspace, pricing Lite/Pro/Max, capabilities y matrix de downloads.
- Límite: precios, versiones, tareas demo, modelos, enlaces y disponibilidad cambian por fecha, región y plataforma.

## Validation Contract

### PASSED

- El documento separa contrato duro, contrato blando, componentes, estados, responsive y procedencia.
- `design-system.json` contiene tokens, breakpoints y componentes derivados del contrato.
- El preview muestra hero, task board, pricing, capabilities, downloads, tokens y validación.
- Se contemplan estados de agente, arquitectura, beta, reduced motion y teclado.

### WARNING

- Los colores son snapshot analítico y requieren medición CSS computada.
- Precios, GLM versions, tareas, capacidades y downloads son dinámicos.
- Este no es un sistema oficial de Z.ai/ZCode ni una autorización para redistribuir activos.

### Criterios de aceptación

Una implementación pasa cuando conserva la visibilidad del trabajo agentic, task board, pricing, capacidades, descargas por plataforma, estados accesibles, tokens y responsive behavior.
