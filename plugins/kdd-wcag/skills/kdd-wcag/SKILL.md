---
name: kdd-wcag
description: 'Verifica HTML contra 10 criterios de exito de WCAG 2.2: idioma declarado, contraste minimo, area de toque, etiquetas, autocomplete, alternativa a movimiento, control de autoplay, saltar bloques, y nombre/rol de componentes. Usala cuando el usuario pida revisar, auditar o confirmar accesibilidad de una pagina HTML.'
---

# KDD WCAG 2.2 Checker

Extraido de los 104 criterios de [WCAG 2.2](https://www.w3.org/TR/WCAG22/) con el método
[Knowledge-Driven Development](https://github.com/MauricioPerera/kdd-book) (kdd-book). Los criterios
de WCAG se llaman literalmente *"testable success criteria"* — están operacionalizados al máximo por
diseño, con umbrales numéricos explícitos (contraste 4.5:1, área de toque 24×24px). Aun así, solo 10
de los 104 (11,5%) terminan siendo instrumentables con este método: el resto pide juicio humano sobre
contenido (¿el texto alternativo describe bien la imagen?) que ningún regex puede confirmar.

**Verde en este skill significa "estos 10 mecanismos están", no "la página es accesible".** Quedan
94 criterios reales de WCAG fuera de esta pila A, y decirlo es parte del método.

## Flujo

1. **Encontrá el HTML relevante**: la página o el componente que el usuario quiera auditar.
2. **Corré los chequeos** relevantes:

   ```bash
   python scripts/a11y_checks.py --rule idioma <pagina.html>
   python scripts/a11y_checks.py --rule contraste --min 4.5 <pagina.html>
   python scripts/a11y_checks.py --rule toque --min 24 <pagina.html>
   python scripts/a11y_checks.py --rule etiqueta <pagina.html>
   python scripts/a11y_checks.py --rule autocomplete <pagina.html>
   python scripts/a11y_checks.py --rule movimiento <pagina.html>
   python scripts/a11y_checks.py --rule autoplay <pagina.html>
   python scripts/a11y_checks.py --rule saltar <pagina.html>
   python scripts/a11y_checks.py --rule nombrerol <pagina.html>
   python scripts/a11y_checks.py --rule etiquetaennombre <pagina.html>
   ```

   `contraste` y `toque` comparten `--min`: dos criterios de conformidad distintos usan el mismo
   mecanismo con un umbral diferente. Exit `0` (cumple), `1` (no cumple, con detalle) o `2` (no se
   pudo verificar — por ejemplo, `--min` faltante o con el valor equivocado).
3. **Reportá cada regla corrida** con `[PASSED]` / `[FAILED]` / `[NO VERIFICABLE]`.
4. **Para el resto de WCAG 2.2** (94 criterios restantes), consultá `scripts/knowledge.json`. Cada
   nodo trae `pile` (`A`=medible, `B`=juicio real sin umbral, `C`=conocimiento), `title`,
   `description` y, si es `B`, un `why_not`. **No inventes un umbral para un criterio que el nodo
   dice que requiere juicio humano sobre contenido.**

## Límite declarado, sin excepciones

`html_checks` construye su propio árbol a partir de `html.parser` (no un DOM completo). El nombre
accesible que compara `etiquetaennombre` es el texto visible del elemento, no el cálculo completo del
algoritmo de "Accessible Name and Description Computation" del W3C -una aproximación declarada, no el
algoritmo entero-.

## Reporte

| Regla | Estado | Archivo:línea | Detalle |
|---|---|---|---|
| (una fila por cada regla corrida) | [PASSED]/[FAILED]/[NO VERIFICABLE] | ... | ... |

## Recursos incluidos

- `scripts/a11y_checks.py` + `scripts/html_checks.py` (dependencia: `a11y_checks` reusa el árbol de
  `html_checks` en vez de construir otro) — extraídos y verificados (sabotaje de cada regla, atajos
  prohibidos reconstruidos a mano) en [kdd-book](https://github.com/MauricioPerera/kdd-book).
- `scripts/knowledge.json` — los 104 criterios de WCAG 2.2, triados en pila A/B/C con su `why_not`
  cuando corresponde.
