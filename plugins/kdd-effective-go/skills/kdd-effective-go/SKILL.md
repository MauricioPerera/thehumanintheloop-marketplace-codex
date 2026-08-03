---
name: kdd-effective-go
description: 'Verifica codigo Go contra 3 convenciones de Effective Go: indentacion con tabs, cero parentesis en if/for/switch, y llave de apertura en la misma linea que el if/for/switch/func. Usala cuando el usuario pida revisar, auditar o confirmar que codigo Go sigue Effective Go.'
---

# KDD Effective Go Checker

Extraido de [Effective Go](https://go.dev/doc/effective_go) con el método [Knowledge-Driven
Development](https://github.com/MauricioPerera/kdd-book) (kdd-book) — la primera fuente de kdd-book
sobre **prosa narrativa corrida**, no un checklist ni un spec numerado: 15 secciones y más de 30
subsecciones sin ítems que enumerar. De las 45 técnicas identificadas, solo 3 tienen una propiedad
concreta que un script puede verificar por texto.

Varias convenciones de Effective Go quedan fuera de esta pila A por un motivo distinto al habitual
("no hay umbral" o "requiere juicio"): `gofmt`, el formateador oficial del lenguaje, ya las hace
cumplir automáticamente, así que no hay nada que el código pueda violar de forma persistente sin que
la propia herramienta lo corrija.

## Flujo

1. **Encontrá el código Go relevante**: el archivo o los archivos que el usuario quiera auditar.
2. **Corré los 3 chequeos**:

   ```bash
   python scripts/effective_go_checks.py --rule indentation-tabs <archivo.go>
   python scripts/effective_go_checks.py --rule no-paren-control <archivo.go>
   python scripts/effective_go_checks.py --rule brace-next-line <archivo.go>
   ```

   Exit `0` (cumple), `1` (no cumple, con archivo:línea:detalle) o `2` (no se pudo verificar — no
   hay archivos `.go` que leer).
3. **Reportá las 3 reglas siempre**, con `[PASSED]` / `[FAILED]` / `[NO VERIFICABLE]`.
4. **Para el resto del documento** (las 42 técnicas restantes, en Formatting, Commentary, Names,
   Semicolons, Control Structures, Functions, Data, Initialization, Methods, Interfaces and other
   types, The blank identifier, Embedding, Concurrency, Errors), consultá `scripts/knowledge.json`
   antes de responder. Cada nodo trae `pile` (`A`=medible, `B`=juicio real sin umbral,
   `C`=conocimiento o garantizado por `gofmt`), `title`, `description` y, si es `B`, un `why_not`.
   **No inventes una regla de texto para lo que el nodo dice que requiere análisis semántico o de
   flujo de datos.**

## Reglas medibles (pila A)

| Regla | Qué mide |
|---|---|
| `indentation-tabs` | La sangría de bloques de código usa tabulaciones, no espacios |
| `no-paren-control` | Las condiciones de `if`/`for`/`switch` no llevan paréntesis alrededor |
| `brace-next-line` | La llave de apertura de un bloque va en la misma línea que `if`/`for`/`switch`/`func`, no en la siguiente |

## Límite declarado, sin excepciones

No hay parser de Go real: son expresiones regulares sobre el texto, igual que `rust_api_checks`.
Ningún compilador ni `gofmt` real corre detrás — el instrumento lee la forma del código, no lo
formatea ni lo valida semánticamente.

## Reporte

| Regla | Estado | Archivo:línea | Detalle |
|---|---|---|---|
| indentation-tabs | [PASSED]/[FAILED]/[NO VERIFICABLE] | ... | ... |
| no-paren-control | ... | ... | ... |
| brace-next-line | ... | ... | ... |

## Recursos incluidos

- `scripts/effective_go_checks.py` — instrumento sin dependencias externas, extraído y verificado
  (sabotaje de cada regla, atajos prohibidos reconstruidos a mano) en
  [kdd-book](https://github.com/MauricioPerera/kdd-book).
- `scripts/knowledge.json` — las 45 técnicas identificadas en Effective Go, triadas en pila A/B/C
  con su `why_not` cuando corresponde.
