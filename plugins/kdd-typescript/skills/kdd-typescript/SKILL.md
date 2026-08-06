---
name: kdd-typescript
description: 'Verifica 17 reglas duras del Google TypeScript Style Guide sobre un archivo .ts puntual: var/const/let, exports, imports, campos privados, const enum, wrapper types, comillas, triple igual, nombres con guion bajo, y mas. Usala cuando el usuario pida revisar o auditar estilo TypeScript segun la guia de Google.'
---

# KDD TypeScript Checker

Extraído de [Google TypeScript Style Guide](https://google.github.io/styleguide/tsguide.html) con
el método [Knowledge-Driven Development](https://github.com/MauricioPerera/kdd-book) (kdd-book).
De sus reglas normativas, 17 son prohibiciones duras ("must not", "never", "do not", "always") y
verificables sin ambigüedad sobre texto; el resto exige juicio real (si un `any` puntual estaba
justificado, si una función debió ser arrow, si una aserción no-nula tenía alternativa) y queda
documentado en `scripts/knowledge.json` como pila B, nunca simulado como pila A.

**Límite declarado desde el inicio:** son heurísticas de texto (regex y conteo de llaves), no un
parser real de TypeScript — Python no trae uno en su librería estándar y este repositorio no suma
dependencias externas por plugin. Un `#` dentro de un string o un `with(` dentro de un comentario
pueden producir un falso positivo puntual; por eso cada hit imprime archivo:línea para que lo
revises antes de actuar, igual que el resto de la familia KDD.

## Flujo

1. **Encontrá el archivo `.ts` puntual** para la regla (nunca escanea un proyecto entero; ninguna
   de las 17 reglas lo necesita).
2. **Corré las 17 reglas** contra ese archivo:

   ```bash
   python scripts/typescript_checks.py --rule sinvar <archivo.ts> [...]
   python scripts/typescript_checks.py --rule exportdefault <archivo.ts> [...]
   python scripts/typescript_checks.py --rule exportmutable <archivo.ts> [...]
   python scripts/typescript_checks.py --rule require <archivo.ts> [...]
   python scripts/typescript_checks.py --rule namespace <archivo.ts> [...]
   python scripts/typescript_checks.py --rule arrayctor <archivo.ts> [...]
   python scripts/typescript_checks.py --rule objectctor <archivo.ts> [...]
   python scripts/typescript_checks.py --rule clasepuntocoma <archivo.ts> [...]
   python scripts/typescript_checks.py --rule campoprivado <archivo.ts> [...]
   python scripts/typescript_checks.py --rule constenum <archivo.ts> [...]
   python scripts/typescript_checks.py --rule wrapper <archivo.ts> [...]
   python scripts/typescript_checks.py --rule debugger <archivo.ts> [...]
   python scripts/typescript_checks.py --rule with <archivo.ts> [...]
   python scripts/typescript_checks.py --rule tsignore <archivo.ts> [...]
   python scripts/typescript_checks.py --rule tripleigual <archivo.ts> [...]
   python scripts/typescript_checks.py --rule comillas <archivo.ts> [...]
   python scripts/typescript_checks.py --rule guionbajo <archivo.ts> [...]
   ```

   Exit `0` (cumple), `1` (no cumple, con `file:line` y detalle por hit), `2` (no se pudo
   verificar — el archivo no existe o no es `.ts`).
3. **Reportá las 17 reglas siempre**, con `[PASSED]` / `[FAILED]` / `[NO VERIFICABLE]`.
4. **Para el resto de la guía** (funciones vs. arrow, `any`, aserciones no-nulas, acrónimos,
   `interface` vs `type`, `readonly`, `for...in`, ASI, `eval`, modificar prototypes nativos),
   consultá `scripts/knowledge.json` antes de responder. Cada nodo trae `pile` (`A`=medible,
   `B`=juicio real sin umbral) y, si es `B`, un `why_not`. **No inventes una regla dura para lo
   que el nodo dice que requiere juicio** — repórtalo como observación cualitativa, no como
   `[FAILED]`.

## Reglas medibles (pila A), agrupadas

| Grupo | Reglas | Qué miden |
|---|---|---|
| Declaraciones | `sinvar` | `var` prohibido, solo `const`/`let` |
| Exports e imports | `exportdefault`, `exportmutable`, `require`, `namespace` | Sin `export default`, sin `export let/var`, sin `require()`, sin `namespace`/`module` |
| Constructores prohibidos | `arrayctor`, `objectctor`, `wrapper` | Sin `new Array()`, `new Object()`, `new String/Number/Boolean()` |
| Clases | `clasepuntocoma`, `campoprivado` | Sin `;` tras el cierre de clase, sin campos privados nativos `#foo` |
| Tipos | `constenum` | Sin `const enum` |
| Features prohibidas | `debugger`, `with`, `tsignore` | Sin `debugger;`, sin `with(...)`, sin `@ts-ignore` |
| Comparación y literales | `tripleigual`, `comillas` | `===`/`!==` en vez de `==`/`!=` (excepto contra `null`/`undefined`); comillas simples salvo para evitar escapar una simple |
| Nombres | `guionbajo` | Ningún identificador con `_` de prefijo o sufijo |

## Límite declarado, sin excepciones

Heurísticas de texto: no parsean TypeScript de verdad. `tripleigual` y `comillas` excluyen los
casos documentados en la propia guía (comparación contra `null`/`undefined`; comillas dobles para
no escapar una simple) para no marcar falsos positivos sobre excepciones explícitas de la fuente.

## Reporte

| Regla | Estado | Archivo:línea | Detalle |
|---|---|---|---|
| (una fila por cada una de las 17 reglas) | [PASSED]/[FAILED]/[NO VERIFICABLE] | ... | ... |

## Recursos incluidos

- `scripts/typescript_checks.py` (17 reglas) — sin dependencias externas, extraídas y verificadas
  contra archivos `.ts` de prueba con violaciones y sin ellas antes de publicarse.
- `scripts/knowledge.json` — las 28 reglas normativas identificadas en la fuente, triadas en pila
  A/B con su `why_not` cuando corresponde.
