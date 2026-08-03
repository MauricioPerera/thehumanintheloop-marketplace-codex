---
name: kdd-tailwind
description: 'Verifica proyectos de Tailwind CSS v4 contra 10 tecnicas: instalacion del plugin, preprocesadores, @reference, utilidades removidas o en conflicto, modificador important, mobile-first, theme variables, namespace de color, y clases dinamicas. Usala cuando el usuario pida revisar, auditar o migrar un proyecto de Tailwind CSS.'
---

# KDD Tailwind CSS Checker

Extraido de una selección curada de 13 páginas de [tailwindcss.com/docs](https://tailwindcss.com/docs)
("Getting started" + "Core concepts") con el método [Knowledge-Driven Development](https://github.com/MauricioPerera/kdd-book)
(kdd-book). El sitio completo tiene ~210 páginas, y ~195 son referencia de clases CSS (`z-index`,
`flex-basis`...) sin técnica que prescribir — por eso el triaje no fue un volcado literal, sino una
selección a mano de las páginas que sí prescriben algo. El porcentaje que da esta fuente **no es
comparable** al de un volcado completo: mide la fracción contractable de la selección, no del sitio.

## Flujo

1. **Encontrá los archivos relevantes**: `vite.config.ts`/`package.json` (instalación,
   preprocesadores), HTML/JSX con clases de Tailwind (utilidades, mobile-first, clases dinámicas),
   CSS con `@theme`/`@apply`/`@variant` (theme variables, namespace de color, `@reference`).
2. **Corré los chequeos** relevantes para lo que el usuario quiera auditar:

   ```bash
   python scripts/tailwind_checks.py --rule instalacion <vite.config.ts>
   python scripts/tailwind_checks.py --rule preprocesadores <package.json>
   python scripts/tailwind_checks.py --rule referencia <archivo.css>
   python scripts/tailwind_checks.py --rule utilidades-removidas <archivo.html>
   python scripts/tailwind_checks.py --rule modificador-important <archivo.html>
   python scripts/tailwind_checks.py --rule utilidades-en-conflicto <archivo.html>
   python scripts/tailwind_checks.py --rule mobile-first <archivo.html>
   python scripts/tailwind_checks.py --rule theme-variables <archivo.css>
   python scripts/tailwind_checks.py --rule namespace-color <archivo.css>
   python scripts/tailwind_checks.py --rule clases-dinamicas <archivo.jsx>
   ```

   Exit `0` (cumple), `1` (no cumple, con archivo:línea:detalle) o `2` (no se pudo verificar).
3. **Reportá cada regla corrida** con `[PASSED]` / `[FAILED]` / `[NO VERIFICABLE]`.
4. **Para el resto de las 21 técnicas** identificadas en la selección curada, consultá
   `scripts/knowledge.json`. Cada nodo trae `pile` (`A`=medible, `B`=juicio real sin umbral,
   `C`=referencia), `title`, `description` y, si es `B`, un `why_not`.

## Reglas medibles (pila A)

| Regla | Qué mide |
|---|---|
| `instalacion` | El plugin oficial y el import de Tailwind están declarados en la config de Vite |
| `preprocesadores` | Cero dependencias de Sass/Less/Stylus junto con Tailwind v4 |
| `referencia` | Los `<style>` con `@apply`/`@variant` declaran `@reference` |
| `utilidades-removidas` | Cero apariciones de utilidades v3 removidas (no renombradas — esas siguen siendo válidas en v4 con otra escala) |
| `modificador-important` | El modificador `!` va al final de la clase, no antepuesto |
| `utilidades-en-conflicto` | Cero utilidades que fijan la misma propiedad CSS sobre el mismo elemento |
| `mobile-first` | La utilidad sin prefijo es para mobile, no el breakpoint chico |
| `theme-variables` | Los theme tokens se declaran con `@theme`, top-level |
| `namespace-color` | Los colores custom van bajo el namespace `--color-*` |
| `clases-dinamicas` | Cero nombres de clase construidos por concatenación en tiempo de ejecución |

## Límite declarado, sin excepciones

No hay parser real de HTML, JSX ni CSS: son expresiones regulares sobre el texto, igual que
`html_checks` antes de tener un árbol. El mapa utilidad→propiedad CSS que usan
`utilidades-en-conflicto` y `mobile-first` es deliberadamente chico —cubre solo las familias que las
propias páginas fuente usan de ejemplo (`display`, `position`, `text-align`...)—.

## Reporte

| Regla | Estado | Archivo:línea | Detalle |
|---|---|---|---|
| (una fila por cada regla corrida) | [PASSED]/[FAILED]/[NO VERIFICABLE] | ... | ... |

## Recursos incluidos

- `scripts/tailwind_checks.py` — instrumento sin dependencias externas, extraído y verificado
  (sabotaje de cada regla, atajos prohibidos reconstruidos a mano) en
  [kdd-book](https://github.com/MauricioPerera/kdd-book).
- `scripts/knowledge.json` — las 21 técnicas de la selección curada, triadas en pila A/B/C con su
  `why_not` cuando corresponde.
