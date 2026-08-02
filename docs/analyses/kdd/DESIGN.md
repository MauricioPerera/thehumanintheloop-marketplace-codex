---
name: kdd-knowledge-driven-development
version: 1.0.0
description: Design System Analysis reproducible del sitio público de KDD — Knowledge-Driven Development.
source: https://mauricioperera.github.io/KDD/
colors:
  ink: "#1B2430"
  inkPanel: "#232E3D"
  inkLine: "#3A4557"
  inkText: "#E8E6DC"
  inkTextDim: "#ABB4C2"
  paper: "#EDEFE7"
  paperPanel: "#E3E6DA"
  paperLine: "#C4C8B8"
  paperText: "#1E2A2A"
  paperTextDim: "#57624F"
  seal: "#B58D3F"
  sealStrong: "#8F6E2E"
  verified: "#3F7A5C"
  flagged: "#A23B3B"
  terminal: "#141B24"
  terminalBar: "#1A2230"
  terminalLine: "#303D4F"
  familyAccentLight: "#6E520E"
  familyAccentDark: "#C79A3A"
typography:
  display:
    fontFamily: "Iowan Old Style, Palatino Linotype, Palatino, Book Antiqua, Georgia, serif"
    fontSize: "3rem"
    fontWeight: 400
    lineHeight: 1.15
  heading:
    fontFamily: "Iowan Old Style, Palatino Linotype, Palatino, Book Antiqua, Georgia, serif"
    fontSize: "2rem"
    fontWeight: 400
    lineHeight: 1.15
  body:
    fontFamily: "-apple-system, Segoe UI, Roboto, Helvetica, Arial, sans-serif"
    fontSize: "16.5px"
    fontWeight: 400
    lineHeight: 1.6
  monoLabel:
    fontFamily: "SF Mono, Cascadia Code, JetBrains Mono, Consolas, Liberation Mono, monospace"
    fontSize: ".72rem"
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: ".16em"
  stat:
    fontFamily: "SF Mono, Cascadia Code, JetBrains Mono, Consolas, Liberation Mono, monospace"
    fontSize: "2.1rem"
    fontWeight: 700
    lineHeight: 1.2
rounded:
  tab: "3px"
  card: "4px"
  terminal: "6px"
  familyNode: "7px"
  familyCore: "9px"
  circle: "999px"
  seal: "999px"
spacing:
  base: "1rem"
  sectionVertical: "4.5rem"
  heroVerticalTop: "5.5rem"
  heroVerticalBottom: "4.5rem"
  contentMeasure: "66ch"
  contentWide: "1100px"
  rail: "240px"
  cardPadding: "1.6rem"
  gridGap: "1.5rem"
  microGap: ".6rem"
components:
  primary-button:
    backgroundColor: "{colors.seal}"
    textColor: "{colors.ink}"
    rounded: "{rounded.tab}"
    padding: ".75em 1.3em"
    typography: "{typography.body}"
  ghost-button:
    backgroundColor: "transparent"
    textColor: "{colors.inkText}"
    rounded: "{rounded.tab}"
    padding: ".75em 1.3em"
  pillar-card:
    backgroundColor: "{colors.paperPanel}"
    textColor: "{colors.paperText}"
    rounded: "{rounded.card}"
    padding: "{spacing.cardPadding}"
---

# KDD — Knowledge-Driven Development

## Overview

Análisis estático del sitio publicado el 2 de agosto de 2026. El producto se presenta como una metodología para gobernar agentes de IA mediante contratos, compuertas deterministas y evidencia verificable. La interfaz comunica rigor técnico con una composición editorial: serif para tesis y títulos, sans para lectura y monospace para etiquetas, métricas y artefactos de terminal.

## Hard Contract

Valores observados en el CSS/HTML publicado: `#1B2430`, `#232E3D`, `#EDEFE7`, `#E3E6DA`, `#B58D3F`, `#3F7A5C` y `#A23B3B`; base tipográfica de `16.5px` con `line-height: 1.6`; rail ancho de `240px`; contenido ancho de `1100px`; tarjeta de `4px`; terminal de `6px`; pasos de `44px`; y breakpoints de `980`, `960`, `900`, `860`, `820`, `760`, `700` y `520px`. La tabla de tokens completa está en `design-system.json` y cada componente documentado abajo referencia esos valores.

## Soft Contract

La interfaz debe sentirse como una especificación editorial verificable: sobria, técnica y deliberadamente anti-promocional. La serif expresa tesis; la monospace expresa evidencia; el oro indica sello o autoridad; el verde y el rojo expresan resultado. Esta intención es una inferencia basada en la repetición de esos patrones en el hero, los exhibits, el terminal, las métricas y el grafo de familia; no es una afirmación oficial de marca.

### Provenance

- Fuente primaria: https://mauricioperera.github.io/KDD/
- Repositorio enlazado por el sitio: https://github.com/MauricioPerera/KDD
- Método: inspección visual de la página publicada y lectura de HTML/CSS inline.
- Estado de procedencia: tokens y componentes marcados aquí como observados provienen del CSS publicado; la intención de marca es una inferencia basada en jerarquía, copy y patrones repetidos.
- Alcance: página única; no se inventan pantallas internas ni flujos de aplicación no presentes en la fuente.

## Visual language

La composición alterna una superficie clara tipo papel con un hero oscuro y bloques de terminal. El color dorado funciona como sello, índice y acento de autoridad; verde y rojo codifican estados verificado/alerta. La densidad visual se mantiene baja: líneas de 1px, paneles planos, bordes pequeños y sombra reservada al terminal y a los nodos interactivos.

## Colors

### Light paper surfaces

| Token | Valor | Uso observado |
| --- | --- | --- |
| `paper` | `#EDEFE7` | Fondo principal de secciones |
| `paperPanel` | `#E3E6DA` | Tarjetas, tabs y nodos |
| `paperLine` | `#C4C8B8` | Divisores y bordes |
| `paperText` | `#1E2A2A` | Texto principal |
| `paperTextDim` | `#57624F` | Texto secundario |

### Dark hero and terminal

| Token | Valor | Uso observado |
| --- | --- | --- |
| `ink` | `#1B2430` | Fondo del hero |
| `inkPanel` | `#232E3D` | Paneles oscuros |
| `inkLine` | `#3A4557` | Líneas y controles oscuros |
| `inkText` | `#E8E6DC` | Texto primario en oscuro |
| `inkTextDim` | `#ABB4C2` | Texto secundario en oscuro |
| `terminal` | `#141B24` | Consola demostrativa |
| `terminalBar` | `#1A2230` | Barra de consola |
| `terminalLine` | `#303D4F` | Borde de consola |

### Semantic accents

| Token | Valor | Uso observado |
| --- | --- | --- |
| `seal` | `#B58D3F` | Acento principal, sello, CTA |
| `sealStrong` | `#8F6E2E` | Acento en papel |
| `verified` | `#3F7A5C` | Estado positivo |
| `flagged` | `#A23B3B` | Estado negativo |
| `familyAccentLight` | `#6E520E` | Identificador de familia en claro |
| `familyAccentDark` | `#C79A3A` | Identificador de familia en oscuro |

## Typography

The base size is `16.5px` with `line-height: 1.6`. Headings use `Iowan Old Style`, `Palatino Linotype`, `Palatino`, `Book Antiqua`, `Georgia`, serif. Body copy uses the system sans stack. Labels, indices, metrics and terminal content use the system monospace stack.

| Role | Size | Weight | Line-height | Tracking |
| --- | --- | --- | --- | --- |
| Hero title | `clamp(2.1rem, 4vw, 3rem)` | 400 | `1.15` | normal |
| Section heading | `clamp(1.5rem, 2.6vw, 2rem)` | 400 | inherited/observed | normal |
| Body | `16.5px` | 400 | `1.6` | normal |
| Eyebrow/index | `.72rem` | 400 | inferred from line box | `.16em`, uppercase |
| Stat value | `2.1rem` | 700 | inferred from block | tabular numerals |
| Terminal | `.82rem` | not explicitly set | `1.7` | monospace |

## Components

### Navigation rail and mobile bar

On wide screens the layout reserves a `240px` vertical rail. It contains an editorial mark and eight indexed links (`A` through `H`). At narrower widths the rail becomes a compact mobile bar with a hamburger control, language toggle and collapsible navigation panel. The skip link is present for keyboard users.

### Buttons

The primary and ghost buttons share `.75em 1.3em` padding, `font-size: .92rem`, `font-weight: 600`, a `3px` radius and inline-flex alignment. Primary uses the seal color; ghost is transparent and is used for secondary repository actions. Hover introduces a short transform/shadow transition; focus-visible is part of the validation contract even where the source CSS does not expose a separate token.

### Hero

The hero uses a two-column grid capped at `1100px`, with a `3rem` gap. It contains an eyebrow, large serif thesis, supporting lead, two CTAs and a terminal-like proof panel. At `980px` the grid stacks to one column.

### Pillar cards

The “Two pillars” section uses two equal columns with `1.5rem` gap. Each pillar is a flat panel with `#E3E6DA` background, `#C4C8B8` border, `4px` radius and `1.6rem` padding. At `700px` it becomes a single column.

### Contract flow

The flow is a row of five numbered circular steps, each `44px`, connected by a line. At `820px` it changes to a vertical, left-aligned list and hides the connector line. This is a structural responsive change, not only a size reduction.

### Terminal evidence panel

The terminal panel is the strongest elevated component: `#141B24` surface, `#303D4F` border, `6px` radius and `0 30px 60px -20px rgba(0,0,0,.55)` shadow. Its top bar has three `9px` circular controls and its content uses monospace at `.82rem` with `1.7` line-height. The adjacent annotations use a `2px` gold left border.

### Stat blocks

The numbers section renders five metrics in a five-column grid with `1.4rem` gap and `2.1rem` monospace values. At `900px` the layout becomes two columns. The copy explicitly frames the metrics as checked into the repository, so they are treated as content evidence rather than decorative counters.

### Boundary columns

The “Can be sealed / Stays out” comparison uses two equal columns, `1.6rem` gap and `1.5rem` padding. Lists use semantic green check and red dash markers. At `760px` the columns stack.

### Domain tabs and family nodes

The domains section uses four columns with `.9rem` gap, reducing to two at `900px` and one at `520px`. Tabs have a `3px` gold top border and `2px` radius. The family graph uses auto-fit nodes with a `220px` minimum, `7px` radius, `3px` left border and a hover lift of `2px` with `0 6px 18px rgba(0,0,0,.10)`.

## Responsive behavior

Observed breakpoints from CSS: `980px` hero stack; `960px` wide rail/layout switch; `900px` stats and domains reduction; `860px` terminal annotation stack; `820px` contract-flow stack; `760px` boundary stack; `700px` pillar stack; `520px` domain single column. The site also supports `prefers-color-scheme`, an explicit `data-theme` override and `prefers-reduced-motion`.

## Content and interaction contract

The page must preserve the narrative sequence: problem → pillars → file flow → terminal proof → numbers → boundary → domains → family. Internal anchors are semantic and indexed rather than generic. External CTAs point to GitHub, releases and Product Hunt. Every external image declaration observed has descriptive `alt` text. No form controls or transactional states were observed; do not invent them in derivatives.

## Validation Contract

- [PASS] Exactly one primary page title is present: `The verdict comes from a machine. Not from the model.`
- [PASS] Eight navigable exhibit sections are present: `problem`, `pillars`, `flow`, `terminal`, `numbers`, `boundary`, `domains`, `family`.
- [PASS] Core color tokens, typography stacks, radius values, layout widths and breakpoints are backed by the published CSS.
- [PASS] Responsive rules cover wide, tablet and mobile transformations, including rail collapse and flow reorientation.
- [PASS] Keyboard affordances are represented by a skip link and visible button/link focus contract.
- [PASS] The Product Hunt image has descriptive alt text.
- [WARN] Computed contrast ratios require runtime sampling for every theme/state; source-level token pairs are documented, but this report does not claim full WCAG certification.
- [WARN] Hover/focus behavior is partially inferred from CSS selectors; interactive runtime state coverage is not equivalent to a full browser test matrix.
- [PASS] No unverified product capabilities are added to the analysis; repository claims remain tied to the copy displayed on the source page.

## Extractability contract

An agent consuming this document should use `design-system.json` as the token source of truth, preserve semantic token names, and flag any component that introduces a new color, radius, spacing value or breakpoint without provenance. A derivative implementation must keep the eight-section information architecture, the terminal evidence treatment, the gold/green/red semantic mapping and the responsive transformations unless the change is explicitly justified.

## IP and reuse note

This is an analysis of a published site, not a transfer of its source code or brand assets. Reuse of the extracted values or visual language should be reviewed against the original repository license, trademarks and any third-party assets before commercial redistribution.
