---
name: echo-pace-logistics-erp-analysis
version: 1.0.0
description: Análisis reproducible del sistema visual de un dashboard ERP de logística React proporcionado como código; no es un sistema oficial de Echo Pace Logistics.
source: local:pasted-text.txt
colors: blue-700-to-blue-900-sidebar-white-surface-gray-neutral-status-colors
typography: tailwind-sans-system-ui-12-to-30px
rounded: 4px-controls-8px-actions-12px-cards
spacing: tailwind-4px-base-scale
components: sidebar-header-stat-card-chart-table-status-pill-search-form-quick-action
---

# Echo Pace Logistics ERP — Design System Analysis

## 1. Resumen de identidad visual

El sistema observado es un dashboard administrativo de logística con una jerarquía clara: navegación azul profunda a la izquierda, superficie de trabajo gris muy clara y módulos blancos elevados. La interfaz prioriza lectura rápida de métricas, operaciones de envíos, finanzas y facturación.

La identidad visual está **observada** en las clases Tailwind y componentes React proporcionados. El nombre “Echo Pace Logistics” y los datos de envíos, clientes, facturas y métricas son contenido de demostración incluido en la fuente; no deben interpretarse como datos reales.

## 2. Contrato duro: colores

Valores observados en clases Tailwind y configuraciones inline:

| Token | Valor | Uso observado |
| --- | --- | --- |
| `colors.brand.sidebarStart` | `#1d4ed8` | Inicio del gradiente de la barra lateral (`blue-700`). |
| `colors.brand.sidebarEnd` | `#1e3a8a` | Final del gradiente de la barra lateral (`blue-900`). |
| `colors.brand.action` | `#2563eb` | CTA principal, enlaces activos y barras de datos (`blue-600`). |
| `colors.brand.actionHover` | `#1d4ed8` | Hover de botones principales (`blue-700`). |
| `colors.brand.soft` | `#dbeafe` | Fondo suave para badges y métricas azules (`blue-100`). |
| `colors.surface.page` | `#f9fafb` | Fondo general del dashboard (`gray-50`). |
| `colors.surface.card` | `#ffffff` | Tarjetas, header, footer y formularios. |
| `colors.border.subtle` | `#f3f4f6` | Bordes de tarjetas y separadores (`gray-100`). |
| `colors.border.default` | `#d1d5db` | Inputs y controles (`gray-300`). |
| `colors.text.heading` | `#1f2937` | Títulos y valores principales (`gray-800`). |
| `colors.text.body` | `#4b5563` | Texto secundario (`gray-600`). |
| `colors.text.muted` | `#6b7280` | Metadatos, fechas y ayudas (`gray-500`). |
| `colors.status.success` | `#22c55e` | Crecimiento, entregado, ingresos y éxito (`green-500`). |
| `colors.status.warning` | `#eab308` | Pendiente, facturas por cobrar y advertencias (`yellow-500`). |
| `colors.status.danger` | `#ef4444` | Retrasos, gastos y estados vencidos (`red-500`). |
| `colors.status.info` | `#3b82f6` | En tránsito y datos informativos (`blue-500`). |
| `colors.status.purple` | `#a855f7` | Satisfacción y categorías administrativas (`purple-500`). |

La paleta de gráficos usa `#2563eb`, `#3b82f6`, `#60a5fa` y `#93c5fd`. Son valores observados en `COLORS` y deben reservarse para series relacionadas, no para texto normal.

## 3. Contrato duro: tipografía

- Familia: `ui-sans-serif, system-ui, sans-serif` por la pila por defecto de Tailwind; **observado por convención**, no por una fuente web explícita.
- Texto base: `16px` y line-height aproximado de `24px` por la escala Tailwind.
- Texto auxiliar: `12px`–`14px`, con `text-xs` y `text-sm`.
- Títulos de tarjeta: `18px`, peso `600` (`text-lg font-semibold`).
- Título de sección/header: `24px`, peso `700` (`text-2xl font-bold`).
- Métrica destacada: `24px`–`30px`, peso `700` (`text-2xl` y `text-3xl font-bold`).
- Etiquetas de tabla: `12px`, peso `500`, mayúsculas y tracking ampliado.

## 4. Botones y enlaces

- Botón principal: fondo `#2563eb`, texto blanco, padding vertical `8px`–`12px`, radio `8px`, hover `#1d4ed8` y transición de color.
- Acción secundaria: botón con borde punteado de `2px`, padding `16px`, radio `8px`; se usa en acciones rápidas.
- Enlace textual: `#2563eb`, con oscurecimiento a `#1e3a8a` en hover.
- Acción destructiva o de riesgo: rojo semántico, como “Report Issue” o gastos, sin reutilizar el azul de navegación.
- Los botones interactivos deben conservar foco visible mediante `focus:ring-2` y un color de anillo coherente con su estado.

## 5. Navegación y búsqueda

La sidebar tiene ancho observado de `256px` (`w-64`), gradiente vertical de `blue-700` a `blue-900`, logo de `40px`, y navegación agrupada con `16px` de padding horizontal. El elemento activo usa fondo `#2563eb`, texto blanco y radio `8px`; los elementos inactivos usan texto azul claro y hover azul oscuro.

El header de contenido es blanco, tiene borde inferior gris y distribuye el título de sección a la izquierda y búsqueda/notificaciones a la derecha. Los inputs de búsqueda usan icono a la izquierda, `8px` de radio y foco azul.

## 6. Tarjetas, contenedores y componentes

| Componente | Contrato observado | Estados relevantes |
| --- | --- | --- |
| Sidebar | `256px`, gradiente azul, navegación vertical, bloque de usuario inferior. | activo, hover, entrada, navegación móvil no verificable. |
| Header | Superficie blanca, borde inferior, título de `24px`, búsqueda y notificación. | default, focus de búsqueda. |
| Stat card | Blanco, `p-6` (`24px`), borde `gray-100`, sombra media, radio `12px`; icono circular `48px`. | default, hover con desplazamiento `-5px`, positivo, negativo. |
| Chart card | Blanco, `p-6`, título de `18px`, área de gráfico de `320px`. | default, tooltip, leyenda. |
| Tabla | Contenedor blanco, header `gray-50`, filas separadas y overflow horizontal. | hover de fila, status select, empty no verificable. |
| Status pill | Padding horizontal `8px`–`12px`, radio completo, texto `12px` semibold. | delivered, in-transit, pending, delayed, paid, overdue. |
| Formulario | Labels `14px` semibold, inputs con borde gris, padding horizontal `16px`, foco azul. | default, focus, required, loading, error no implementado. |
| Quick action | Botón ancho completo, icono grande, borde discontinuo y radio `8px`. | default, hover. |

## 7. Formularios y estados de interacción

El formulario “Create New Invoice” es controlado por React. Customer, amount y due date son campos requeridos. Durante el envío aparece un estado `loading`, se deshabilita el botón y se muestra un indicador giratorio. La confirmación se comunica mediante `alert()`.

El cambio de estado de un envío es inmediato en el `select` y usa estilos semánticos según `Delivered`, `In Transit`, `Pending` o `Delayed`. El efecto `whileHover` de Framer Motion desplaza las tarjetas y los elementos de navegación; el efecto de entrada del contenido cambia la opacidad de `0` a `1`.

## 8. Datos, tablas y métricas

El dashboard usa cuatro stat cards: Total Revenue, Active Shipments, Pending Invoices y On-Time Delivery. Las tablas presentan tracking, cliente, ruta, fechas, importes y acciones. Revenue utiliza un `BarChart`; Shipment Status Distribution utiliza un `PieChart`.

Los valores como `$86,450`, `24`, `12`, `94.2%`, clientes y números de tracking son **mock data observados**. El análisis no los convierte en claims ni métricas de negocio reales.

## 9. Espaciado y grid

- Base de espaciado: escala Tailwind de `4px`, con ejemplos `4px`, `8px`, `12px`, `16px`, `24px` y `32px`.
- Separación principal entre módulos: `24px` (`gap-6`, `space-y-6`).
- Padding de tarjetas: `24px` (`p-6`).
- Grid de métricas: una columna en móvil, dos en tablet y cuatro en desktop.
- Grid de gráficos: una columna hasta `lg`, dos columnas desde el breakpoint grande.
- Layout raíz: viewport completo (`h-screen`) con sidebar fija y contenido con overflow vertical independiente.

## 10. Border radius

- `4px`: controles pequeños derivados de `rounded` cuando se usa sin modificador.
- `8px`: botones, inputs, navegación activa, quick actions y elementos de interacción.
- `12px`: tarjetas y superficies destacadas (`rounded-xl`).
- `9999px`: pills de estado y avatar circular (`rounded-full`).

## 11. Elevación y profundidad

Las tarjetas usan `shadow-md`, equivalente aproximado a una sombra media de Tailwind; la fuente no incluye el valor CSS computado. El gradiente azul de la sidebar crea la principal separación visual. Los bordes `gray-100` mantienen una división sutil sobre el fondo `gray-50`.

## 12. Responsive behavior y touch targets

La fuente declara grids responsivos (`grid-cols-1`, `md:grid-cols-2`, `lg:grid-cols-4`), paddings y flex directions (`md:flex-row`). En tablas se usa `overflow-x-auto`, por lo que el comportamiento móvil es desplazamiento horizontal localizado, no una reestructuración de columnas. No hay breakpoint explícito para colapsar la sidebar.

- Desktop: sidebar `256px`, cuatro métricas, gráficos en dos columnas.
- Tablet: dos métricas por fila y formularios/acciones en dos columnas cuando aplica.
- Móvil: una métrica por fila, tablas desplazables, header y formularios apilados.
- Touch target: botones de navegación con al menos `48px` de alto aproximado (`py-3` más line-height); otros tamaños exactos no son verificables sin CSS computado.

## 13. Contrato blando

- **Intención (inferido):** transmitir control operativo y confiabilidad mediante azul, métricas destacadas y estados de color inmediatos.
- **Jerarquía:** primero salud del negocio, después visualización, luego detalle tabular y acciones.
- **Regla de uso:** emplear azul para navegación y acciones; reservar verde, amarillo y rojo para semántica de estado.
- **Voz:** etiquetas breves y orientadas a tarea; evitar lenguaje promocional dentro de vistas administrativas.
- **Anti-patrones:** no usar rojo como decoración, no esconder estados solo en color, no mezclar múltiples gradientes en tarjetas y no convertir los datos mock en cifras reales.
- **Accesibilidad (inferido):** complementar cada estado cromático con texto visible; conservar foco y nombres accesibles para iconos/acciones.

## 14. Provenance and limitations

- Fuente: archivo local `pasted-text.txt`, código React proporcionado por el usuario.
- Fecha de análisis: 2026-08-04.
- Evidencia: JSX, clases Tailwind, valores inline, constantes de Recharts y transiciones de Framer Motion.
- No se inspeccionó un bundle compilado, CSS computado, viewport real ni estados de error/empty.
- No se reutilizan logos, imágenes ni activos externos en el preview.
- El resultado es un análisis técnico independiente; no es el sistema oficial de Echo Pace Logistics.

## 15. Validation Contract

| Regla | Estado | Valor detectado | Evidencia / corrección |
| --- | --- | --- | --- |
| Frontmatter completo | `[PASSED]` | 9 campos requeridos | Todos los campos del esquema están presentes. |
| Tokens de color | `[PASSED]` | 17 roles + 4 colores de chart | Valores derivados de clases Tailwind e inline styles. |
| Referencias de componentes | `[PASSED]` | 8 componentes | Cada componente se documenta y se proyecta en JSON. |
| Tipografía y dimensiones | `[PASSED]` | Escala 12–30px | Valores mapeados desde clases Tailwind observadas. |
| Responsive | `[PASSED]` | mobile/tablet/desktop | Grid y flex responsive documentados; sidebar móvil queda no verificable. |
| Estados | `[WARNING]` | loading, hover, status; error/empty parcial | Implementar mensajes inline de error y estados vacíos si el producto deja de ser demo. |
| Contraste | `[WARNING]` | No calculable completamente sin CSS computado | Verificar ratios de texto, azul sobre blanco y badges en implementación real. |
| Procedencia | `[WARNING]` | Fuente local con mock data | Confirmar licencia y reemplazar datos ficticios antes de uso productivo. |
