---
name: kdd-stripe
description: 'Audita codigo Python que llama a la API de Stripe contra dos prohibiciones sin condicional de docs.stripe.com/api: claves secretas o restringidas embebidas en el codigo, y el header Idempotency-Key en peticiones GET o DELETE. Usala cuando el usuario pida revisar, auditar o confirmar seguridad/buenas practicas al integrar la API de Stripe.'
---

# KDD Stripe API Checker

Extraido de la seccion "Using the API" de docs.stripe.com/api con el metodo [Knowledge-Driven
Development](https://github.com/MauricioPerera/kdd-book) (kdd-book). De sus 7 paginas conceptuales,
solo 2 tienen una prohibicion **sin condicional** en el propio texto -las unicas dos con una
propiedad concreta que un script puede verificar-. Las otras 5 son referencia (forma del objeto
error, parametros de paginacion, como cada SDK fija version) o una capacidad opcional sin
correcto/incorrecto (expandir campos relacionados).

## Flujo

1. **Encontrá el codigo relevante**: donde el proyecto define claves de Stripe, o donde hace
   llamadas HTTP (`requests.get/post/delete`, o el SDK de Stripe) a la API.
2. **Corré los 2 chequeos** contra ese archivo:

   ```bash
   python scripts/stripe_checks.py --rule claves-en-codigo <archivo.py>
   python scripts/stripe_checks.py --rule idempotencia-en-lectura <archivo.py>
   ```

   Exit `0` (cumple), `1` (no cumple, con archivo:línea:detalle) o `2` (no se pudo verificar — el
   proyecto no tiene archivos `.py` que leer).
3. **Reportá las 2 reglas siempre**, con `[PASSED]` / `[FAILED]` / `[NO VERIFICABLE]`.
4. **Para el resto de "Using the API"** (Errors, Pagination, Expanding responses, Versioning,
   Request IDs), consultá `scripts/knowledge.json` antes de responder. Cada nodo trae `pile`
   (`A`=medible, `B`=capacidad opcional sin umbral, `C`=referencia), `title`, `description` y, si es
   `B`, un `why_not`. **No inventes una regla de "buena practica" para lo que el nodo dice que no es
   medible.**

## Reglas medibles (pila A)

| Regla | Qué mide | Por qué es sin-condicional |
|---|---|---|
| `claves-en-codigo` | Cero claves secretas (`sk_`) o restringidas (`rk_`) de Stripe escritas como literal en el código | "Don't embed secret or restricted API keys in source code" — sin condición. Las claves publicables (`pk_`) están pensadas para vivir en el cliente y **no** cuentan como violación |
| `idempotencia-en-lectura` | Cero headers `Idempotency-Key` en peticiones GET o DELETE | "Don't send idempotency keys in GET and DELETE requests because it has no effect" — sin condición. Usar la clave al crear/actualizar (POST) es una recomendación condicional del propio texto, no una prohibición, y por eso no entra en esta regla |

## Límite declarado, sin excepciones

El script lee código Python vía `ast`, no ejecuta nada. Reconoce una clave por su **forma**
(`sk_`/`rk_` + modo + cuerpo alfanumérico), no por el nombre de la variable — así la ve tanto en una
asignación como en un argumento inline. Una clave armada por concatenación en tiempo de ejecución no
la ve — no es un string literal. Para idempotencia, solo reconoce un `headers={...}` escrito inline
en la llamada; un header puesto en una variable intermedia no lo ve.

## Reporte

| Regla | Estado | Archivo:línea | Detalle |
|---|---|---|---|
| claves-en-codigo | [PASSED]/[FAILED]/[NO VERIFICABLE] | ... | ... |
| idempotencia-en-lectura | ... | ... | ... |

## Recursos incluidos

- `scripts/stripe_checks.py` — instrumento sin dependencias externas, extraído y verificado
  (sabotaje de cada regla, atajos prohibidos reconstruidos a mano) en
  [kdd-book](https://github.com/MauricioPerera/kdd-book).
- `scripts/knowledge.json` — las 7 técnicas de "Using the API", triadas en pila A/B/C con su
  `why_not` cuando corresponde.
