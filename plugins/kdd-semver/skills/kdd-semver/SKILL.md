---
name: kdd-semver
description: 'Verifica si un proyecto Python declara su version siguiendo Semantic Versioning 2.0.0: formato X.Y.Z, identificadores de pre-release y de build metadata. Usala cuando el usuario pida revisar, auditar o confirmar que una version cumple SemVer, o pregunte que dice el spec de SemVer sobre un caso puntual.'
---

# KDD SemVer Checker

Este skill no es un linter genérico de "buenas prácticas de versionado": es la salida directa de
extraer el spec de **Semantic Versioning 2.0.0** con el método [Knowledge-Driven Development](https://github.com/MauricioPerera/kdd-book)
(kdd-book). El spec tiene 11 artículos. Solo 3 tienen una propiedad concreta que un script puede
verificar sin ambigüedad; los otros 8 son juicio de versionado (cuándo bump mayor vs. menor) o
referencia (cómo se calcula la precedencia). El skill sabe distinguir cuáles son cuáles y nunca
inventa una regla para los 8 que no puede verificar.

## Flujo

1. **Encontrá la version.** Buscá `__version__ = "..."` en el código Python del proyecto (típicamente
   `__init__.py`, `setup.py`, `pyproject.toml` vía `version = "..."`, o donde el usuario indique). Si
   hay varias declaraciones, pedí cuál es la canónica en vez de asumir.
2. **Corré el chequeo determinista** contra el archivo que declara `__version__`:

   ```bash
   python scripts/semver_checks.py --rule formato <archivo.py>
   python scripts/semver_checks.py --rule prerelease <archivo.py>
   python scripts/semver_checks.py --rule build <archivo.py>
   ```

   Cada corrida devuelve exit `0` (cumple), `1` (no cumple, con archivo:línea:detalle) o `2` (no se
   pudo verificar — por ejemplo, si no hay ningún `__version__` de pre-release para medir esa regla en
   particular; eso es correcto, no un error).
3. **Reportá las 3 reglas siempre**, aunque alguna no aplique (exit 2 = "no verificable", no lo
   marques como fallo). Usá `[PASSED]` / `[FAILED]` / `[NO VERIFICABLE]`.
4. **Para el resto del spec** (los otros 8 artículos), consultá `scripts/knowledge.json` antes de
   responder cualquier pregunta sobre SemVer que no sea una de las 3 reglas. Cada nodo trae `pile`
   (`A`=medible, `B`=juicio real sin umbral, `C`=referencia), `title`, `description` y, si es `B`, un
   `why_not` que explica por qué no tiene una propiedad binaria. **No completes con tu propio
   conocimiento de SemVer lo que el nodo `B` dice que no es medible** — citá el `why_not` tal cual.

## Reglas medibles (pila A)

| Regla | Artículo del spec | Qué mide |
|---|---|---|
| `formato` | 2 | `X.Y.Z` con enteros no negativos, sin ceros iniciales, sin sufijo pre-release ni build |
| `prerelease` | 9 | Identificadores de pre-release no vacíos, `[0-9A-Za-z-]`, sin cero inicial en los numéricos |
| `build` | 10 | Identificadores de build metadata no vacíos y de solo `[0-9A-Za-z-]` (a diferencia de pre-release, sí puede llevar ceros iniciales) |

## Límite declarado, sin excepciones

El script lee código Python vía `ast`, no ejecuta nada y no tiene un parser real de SemVer: solo
reconoce un literal de string asignado a `__version__`. Una versión armada por concatenación, f-string
o calculada en tiempo de ejecución no la ve — no es un defecto a ajustar con más regex, es el límite
de leer código en vez de ejecutarlo, y hay que decirlo así si el usuario pregunta por qué no detectó
algo.

## Reporte

| Regla | Estado | Archivo:línea | Detalle |
|---|---|---|---|
| formato | [PASSED]/[FAILED]/[NO VERIFICABLE] | ... | ... |
| prerelease | ... | ... | ... |
| build | ... | ... | ... |

Si el usuario pregunta por un artículo fuera de estas 3 (por ejemplo "¿cuándo bump la mayor?"),
respondé citando el nodo correspondiente de `knowledge.json` y aclarando que es pila B o C — no una
regla que este skill pueda marcar en verde o rojo.

## Recursos incluidos

- `scripts/semver_checks.py` — instrumento sin dependencias externas, extraído y verificado (sabotaje
  de cada regla, atajos prohibidos reconstruidos a mano) en [kdd-book](https://github.com/MauricioPerera/kdd-book).
- `scripts/knowledge.json` — las 11 técnicas del spec, triadas en pila A/B/C con su `why_not` cuando
  corresponde.
