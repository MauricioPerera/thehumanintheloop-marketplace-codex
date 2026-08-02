---
name: thehumanintheloop-marketplace-codex-analysis
version: 1.0.0
description: Design System Analysis del marketplace público TheHumanInTheLoop Marketplace Codex; análisis externo de su interfaz de catálogo.
source: https://mauricioperera.github.io/thehumanintheloop-marketplace-codex/
colors:
  ink: "#17211D"
  muted: "#65736D"
  cream: "#F5F5EF"
  paper: "#FFFFFF"
  primary: "#D7F36A"
  orange: "#FF704E"
  line: "#DCE2D9"
  orbit: "#47554F"
  softText: "#B7C4BD"
  oliveText: "#56621C"
typography:
  body: {fontFamily: "Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, Segoe UI, sans-serif", fontSize: "16px", fontWeight: 400, lineHeight: 1.5}
  eyebrow: {fontFamily: "Inter, ui-sans-serif, system-ui, sans-serif", fontSize: "11px", fontWeight: 800, lineHeight: 1.2, letterSpacing: "0.18em"}
  display: {fontFamily: "Inter, ui-sans-serif, system-ui, sans-serif", fontSize: "56px", fontWeight: 800, lineHeight: 0.94, letterSpacing: "-0.08em"}
  displayAccent: {fontFamily: "Georgia, Times New Roman, serif", fontSize: "56px", fontWeight: 400, lineHeight: 0.94, letterSpacing: "-0.07em"}
  heading: {fontFamily: "Inter, ui-sans-serif, system-ui, sans-serif", fontSize: "40px", fontWeight: 800, lineHeight: 0.98, letterSpacing: "-0.07em"}
  cardTitle: {fontFamily: "Inter, ui-sans-serif, system-ui, sans-serif", fontSize: "23px", fontWeight: 800, lineHeight: 1.1, letterSpacing: "-0.045em"}
  small: {fontFamily: "Inter, ui-sans-serif, system-ui, sans-serif", fontSize: "12px", fontWeight: 400, lineHeight: 1.5}
rounded: {pill: "999px", card: "8px", icon: "12px", control: "6px", circle: "999px"}
spacing: {xs: "7px", sm: "10px", md: "16px", lg: "18px", xl: "25px", section: "90px", contentMax: "1120px", heroTop: "100px"}
components:
  site-header: {backgroundColor: "{colors.ink}", textColor: "{colors.paper}", padding: "24px 0", height: "72px"}
  hero: {backgroundColor: "{colors.ink}", textColor: "{colors.cream}", height: "620px", padding: "100px 0 130px", typography: "{typography.display}"}
  primary-button: {backgroundColor: "{colors.primary}", textColor: "{colors.ink}", rounded: "{rounded.pill}", padding: "14px 19px", typography: "{typography.small}"}
  search-input: {backgroundColor: "{colors.paper}", textColor: "{colors.muted}", rounded: "{rounded.pill}", height: "44px", padding: "0 16px", typography: "{typography.body}"}
  plugin-card: {backgroundColor: "{colors.paper}", textColor: "{colors.ink}", rounded: "{rounded.card}", padding: "25px", height: "300px", typography: "{typography.cardTitle}"}
  install-panel: {backgroundColor: "{colors.primary}", textColor: "{colors.ink}", padding: "90px 0"}
  accent-label: {backgroundColor: "{colors.orange}", textColor: "{colors.ink}", typography: "{typography.eyebrow}"}
  hero-copy: {backgroundColor: "{colors.ink}", textColor: "{colors.softText}", typography: "{typography.body}"}
  install-copy: {backgroundColor: "{colors.primary}", textColor: "{colors.oliveText}", typography: "{typography.body}"}
  decorative-orbit: {backgroundColor: "{colors.orbit}", rounded: "{rounded.circle}"}
  divider: {backgroundColor: "{colors.line}", height: "1px"}
---

# TheHumanInTheLoop Marketplace Codex — Design System Analysis

## 1. Overview — Resumen de identidad visual

El marketplace observado el 2 de agosto de 2026 usa una interfaz editorial de catálogo: fondo crema, superficies blancas, hero oscuro, lima para activar y naranja para señalar intención o estado. La composición combina lenguaje de documentación con una voz humana y experimental. El resultado comunica selección curada y control antes de la instalación.

### Provenance and scope

- Fuente: https://mauricioperera.github.io/thehumanintheloop-marketplace-codex/
- Evidencia: `docs/index.html`, `docs/styles.css`, `docs/preview-modal.css` y `docs/app.js` del repositorio.
- Viewports documentados: desktop con contenedor de `1120px` y mobile mediante breakpoint de `700px`.
- Alcance: se analiza la interfaz del catálogo, el hero, las tarjetas, la sección de instalación, el preview embebido y el footer. El contenido del catálogo puede cambiar.
- Propiedad: este documento analiza el marketplace; sus tokens no deben interpretarse como licencia para reutilizar marca, textos o activos fuera del repositorio.

## 2. Contrato duro

Valores observados en CSS: `--ink #17211D`, `--cream #F5F5EF`, `--paper #FFFFFF`, `--lime #D7F36A`, `--orange #FF704E`, `--line #DCE2D9` y `--muted #65736D`. El contenido principal usa un máximo de `1120px`; las tarjetas usan `25px` de padding, `8px` de radio y `300px` de altura mínima. El hero tiene una altura mínima de `620px` y su contenido comienza después de `100px` de padding.

## 3. Contrato blando

Inferido: la interfaz quiere sentirse como un archivo curado, no como una tienda de extensiones masiva. El contraste entre tinta y lima crea una señal de acción clara; el naranja funciona como acento de atención y el serif solo aparece para introducir calidez dentro del display. Las superficies deben permanecer tranquilas, con bordes finos y sombras suaves. Evitar una UI saturada de badges, gradientes o efectos de producto genéricos.

## 4. Colors — Paleta de colores

| Token | Valor | Uso | Evidencia |
| --- | --- | --- | --- |
| `ink` | `#17211D` | Hero, texto principal, botones activos | `docs/styles.css :root`, `.hero`, `.filter.active` |
| `muted` | `#65736D` | Metadata, descripciones y texto secundario | `:root`, `.plugin-card p` |
| `cream` | `#F5F5EF` | Canvas general | `:root`, `body` |
| `paper` | `#FFFFFF` | Tarjetas, búsqueda y superficies | `:root`, `.plugin-card`, `.search` |
| `lime` | `#D7F36A` | CTA principal y panel de instalación | `:root`, `.primary-button`, `.install-section` |
| `orange` | `#FF704E` | Eyebrow, contador y CTA de copia | `:root`, `.eyebrow`, `.copy-button` |
| `line` | `#DCE2D9` | Bordes y divisores | `:root`, `.filter`, `.card-footer` |
| `orbit` | `#47554F` | Anillos decorativos del hero | `.hero-orbit` |
| `softText` | `#B7C4BD` | Texto sobre hero oscuro | `.hero-copy`, `.code-card` |
| `oliveText` | `#56621C` | Texto del panel lima | `.install-copy`, `.install-steps` |

Contraste observado: `#FFFFFF` sobre `#17211D` es aproximadamente `15.5:1`; `#17211D` sobre `#D7F36A` es aproximadamente `11.8:1`; `#65736D` sobre `#F5F5EF` es aproximadamente `4.5:1`. El uso de muted en texto pequeño debe revisarse si se modifica la paleta.

## 5. Typography — Escala tipográfica

La interfaz usa Inter o una sans de sistema para el cuerpo y Georgia/Times New Roman en el acento editorial del hero.

| Rol | Tamaño base | Peso | Line-height | Uso |
| --- | --- | --- | --- | --- |
| Body | `16px` | 400 | `1.5` | Texto general |
| Eyebrow | `11px` | 800 | `1.2` | Etiquetas de sección, tracking `0.18em` |
| Display | `56px` desktop | 800 | `0.94` | Título principal; se reduce en mobile |
| Display accent | `56px` desktop | 400 | `0.94` | Frase editorial serif |
| Heading | `40px` desktop | 800 | `0.98` | Títulos de sección |
| Card title | `23px` desktop | 800 | `1.1` | Nombre del recurso |
| Small | `12px` | 400 | `1.5` | Footer y metadata |

## 6. Navegación y búsqueda

El header es una barra oscura con marca textual, enlaces de navegación, botón de GitHub y altura visual aproximada de `72px` incluyendo padding. En mobile los enlaces no esenciales desaparecen y permanece el botón principal. La búsqueda se presenta como una cápsula blanca de `44px` de alto, con ícono, placeholder y ancho máximo de `430px`. Los filtros son controles pill con borde y estado activo invertido.

## 7. Components — Tarjetas, previews y acciones

Las tarjetas de recurso tienen superficie blanca, borde `1px`, radio `8px`, padding `25px` y una altura mínima de `300px`. El icono cuadrado de `44px` usa radio `12px` y lima. El badge de categoría es compacto, uppercase y pill. El hover eleva la tarjeta `4px` y añade una sombra suave.

Los plugins muestran una acción primaria de ancho completo para abrir Codex y una acción GitHub. Los Design System Analyses muestran “Abrir diseño en Codex” y “Ver preview”. Esta distinción es observada en `docs/app.js`; no mezclar preview y ejecución en una sola acción.

Estados requeridos: default, hover, focus-visible, active y disabled para controles; `WARNING` cuando una fuente no exponga un estado. La modal de preview usa un backdrop oscuro, shell de `18px` y un iframe de contenido.

## 8. Panel de instalación y código

La sección de instalación invierte el tono del hero: fondo lima, copy en olive y una tarjeta de código oscura con sombra desplazada de `12px`. Su layout es de dos columnas con gap de `70px` en desktop y una columna en mobile. La interacción de copiar debe mostrar un estado de confirmación y conservar un camino manual.

## 9. Espaciado y grid

El sistema usa una escala compacta de `7px`, `10px`, `16px`, `18px`, `25px`, con secciones de `90px`. El grid de recursos usa columnas adaptativas con mínimo de `300px` y gap de `18px`; el contenedor editorial tiene máximo de `1120px` y gutters de `24px` en desktop, `16px` en mobile.

## 10. Border radius y elevación

Los controles de acción son pills de `999px`; las tarjetas usan `8px`; los iconos usan `12px`; los filtros y la búsqueda también son pills. La elevación es expresiva solo en hover de tarjetas y en el bloque de código. No añadir sombras pesadas al canvas ni a cada control.

## 11. Responsive behavior y touch targets

El breakpoint observado es `700px`: el nav oculta enlaces secundarios, el hero pasa a una columna, toolbar y footer se apilan, el grid de instalación pasa a una columna y el radio visual del hero se desplaza fuera del viewport. Los botones pill tienen `9px 15px` o `14px 19px` de padding; validar que el área final de toque sea al menos `44px` cuando se reutilice en producción. El comportamiento exacto del iframe en pantallas muy estrechas es `WARNING` y debe probarse en runtime.

## 12. Do's and Don'ts

- Do conservar el contraste tinta/lima para acciones de alta prioridad.
- Do usar superficies blancas y bordes finos para que el catálogo se lea como archivo curado.
- Do mantener el serif como acento breve, no como tipografía de toda la interfaz.
- Do diferenciar preview, GitHub y apertura en Codex.
- Don't convertir cada metadata en un badge saturado.
- Don't reutilizar logos, nombres o activos de terceros sin verificar derechos.
- Don't ocultar estados de copia, focus o error.

## 13. Validation Contract

- `[PASSED] Source evidence`: HTML, CSS y JavaScript locales identificados y trazables.
- `[PASSED] Hard tokens`: colores, tipografía, radios, spacing y componentes referencian valores definidos en frontmatter.
- `[PASSED] Component references`: todas las referencias `{colors.*}`, `{rounded.*}` y `{typography.*}` resuelven.
- `[PASSED] Responsive contract`: desktop y mobile con breakpoint `700px` y cambios concretos documentados.
- `[PASSED] Provenance`: fecha, URL, límites y propiedad intelectual están registrados.
- `[WARNING] Runtime focus matrix`: la cobertura completa de focus-visible de todos los controles necesita prueba de teclado en browser.
- `[WARNING] Protocol dependency`: `codex://new` depende de que Codex Desktop esté instalado y registrado en el sistema.
- `[WARNING] Dynamic catalog`: la cantidad y naturaleza de los recursos cambiará con futuras publicaciones.

## 14. Extractability contract

Una IA debe leer este `DESIGN.md` antes de cambiar el marketplace. Usar `design-system.json` como proyección mecánica, preservar la separación entre hero, catálogo, instalación y preview, y actualizar el Validation Contract cuando se agreguen nuevos componentes, estados o breakpoints.
