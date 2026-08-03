---
name: kdd-rust-api
description: 'Verifica codigo Rust contra 3 tecnicas de las Rust API Guidelines: getters por valor sin prefijo get_, tipos publicos con #[derive(Debug)], y ejemplos rustdoc que usan ? en vez de unwrap()/try!. Usala cuando el usuario pida revisar, auditar o confirmar que un crate sigue las Rust API Guidelines.'
---

# KDD Rust API Guidelines Checker

Extraido del [Rust API Guidelines Checklist](https://rust-lang.github.io/api-guidelines/checklist.html)
(54 items en 11 categorías) con el método [Knowledge-Driven Development](https://github.com/MauricioPerera/kdd-book)
(kdd-book). Solo 3 de esos 54 items tienen una propiedad verificable por texto sin un compilador de
por medio; los otros 51 piden entender semántica de Rust -si un trait object es object-safe, si un
tipo es realmente un smart pointer- que ningún regex puede confirmar de verdad. El triaje fue
deliberadamente conservador: preferir un porcentaje bajo y honesto (3 de 54) a inflar la pila
medible con heurísticas débiles.

## Flujo

1. **Encontrá el código Rust relevante**: funciones públicas con receptor `&self` (para getters),
   `pub struct`/`pub enum` (para Debug), o comentarios de documentación con bloques de ejemplo
   ` ```rust ` (para los ejemplos rustdoc).
2. **Corré los 3 chequeos** contra el archivo `.rs`:

   ```bash
   python scripts/rust_api_checks.py --rule getter <archivo.rs>
   python scripts/rust_api_checks.py --rule common-traits <archivo.rs>
   python scripts/rust_api_checks.py --rule question-mark <archivo.rs>
   ```

   Exit `0` (cumple), `1` (no cumple, con archivo:línea:detalle) o `2` (no se pudo verificar — no
   hay archivos `.rs` que leer).
3. **Reportá las 3 reglas siempre**, con `[PASSED]` / `[FAILED]` / `[NO VERIFICABLE]`.
4. **Para el resto del checklist** (los otros 51 items en las 11 categorías: Naming,
   Interoperability, Macros, Documentation, Predictability, Flexibility, Type Safety, Dependability,
   Debuggability, Future Proofing, Necessities), consultá `scripts/knowledge.json` antes de
   responder. Cada nodo trae `pile` (`A`=medible, `B`=juicio real sin umbral, `C`=conocimiento),
   `title`, `description` y, si es `B`, un `why_not`. **No inventes una regla de texto para lo que el
   nodo dice que necesita un compilador o juicio de diseño.**

## Reglas medibles (pila A)

| Regla | Qué mide | Límite declarado |
|---|---|---|
| `getter` | Un getter con prefijo `get_` que devuelve por valor (no por referencia) debería renombrarse sin el prefijo | Solo reconoce `fn get_<nombre>(&self, ...) -> T` textualmente; no distingue si `T` es realmente "por valor" en el sentido semántico completo de Rust |
| `common-traits` | Un `pub struct`/`pub enum` sin `#[derive(...Debug...)]` en los atributos contiguos inmediatos | Solo mira derives contiguos arriba de la declaración; un `impl Debug for X` manual en otro lugar del archivo no lo detecta |
| `question-mark` | Un ejemplo rustdoc (` ```rust ` dentro de `///`) que usa `.unwrap()` o `try!()` en vez de `?` | Solo mira dentro de bloques de código marcados como ejemplo; no analiza el resto del archivo |

## Límite declarado, sin excepciones

No hay parser de Rust real: son expresiones regulares sobre el texto, igual que `tailwind_checks`
antes de tener un árbol. Ningún compilador valida los hallazgos — el instrumento lee la forma del
código, no su semántica.

## Reporte

| Regla | Estado | Archivo:línea | Detalle |
|---|---|---|---|
| getter | [PASSED]/[FAILED]/[NO VERIFICABLE] | ... | ... |
| common-traits | ... | ... | ... |
| question-mark | ... | ... | ... |

## Recursos incluidos

- `scripts/rust_api_checks.py` — instrumento sin dependencias externas, extraído y verificado
  (sabotaje de cada regla, atajos prohibidos reconstruidos a mano) en
  [kdd-book](https://github.com/MauricioPerera/kdd-book).
- `scripts/knowledge.json` — los 54 items del checklist, triados en pila A/B/C con su `why_not`
  cuando corresponde.
