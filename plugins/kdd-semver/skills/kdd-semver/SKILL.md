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

1. **Encontrá la version.** Un proyecto Python la declara como `__version__ = "..."` (en
   `__init__.py`, `setup.py`, o donde el usuario indique) o como `[project].version` en
   `pyproject.toml`. Si hay varias declaraciones en el proyecto, pedí cuál es la canónica en vez de
   asumir — el script lee *solo el archivo puntual que le pases*, nunca escanea el resto del
   directorio buscando otras.
2. **Corré el chequeo determinista** contra ese archivo puntual (`.py` o `pyproject.toml`):

   ```bash
   python scripts/semver_checks.py --rule formato <archivo>
   python scripts/semver_checks.py --rule prerelease <archivo>
   python scripts/semver_checks.py --rule build <archivo>
   ```

   Para auditar un proyecto entero (varios archivos, cada uno con su propia version) usá
   `--proyecto <directorio>` en vez de un archivo puntual; ahí sí escanea todo `.py` y
   `pyproject.toml` bajo ese directorio.

   Cada corrida devuelve exit `0` (cumple), `1` (no cumple, con archivo:línea:detalle) o `2` (no se
   pudo verificar — el archivo no declara ninguna version, `pyproject.toml` la declara `dynamic`, o
   no hay `tomllib` disponible en Python < 3.11; eso es correcto, no un error).
3. **Reportá las 3 reglas siempre**, aunque alguna no aplique a esa version en particular (por
   ejemplo `build` sobre una version sin `+...`: sale verde porque no hay nada que ese artículo le
   pida a esa version, no porque se haya verificado algo). Usá `[PASSED]` / `[FAILED]` /
   `[NO VERIFICABLE]`.
4. **Para el resto del spec** (los otros 8 artículos), consultá `scripts/knowledge.json` antes de
   responder cualquier pregunta sobre SemVer que no sea una de las 3 reglas. Cada nodo trae `pile`
   (`A`=medible, `B`=juicio real sin umbral, `C`=referencia), `title`, `description` y, si es `B`, un
   `why_not` que explica por qué no tiene una propiedad binaria. **No completes con tu propio
   conocimiento de SemVer lo que el nodo `B` dice que no es medible** — citá el `why_not` tal cual.

## Reglas medibles (pila A)

| Regla | Artículo del spec | Qué mide |
|---|---|---|
| `formato` | 2 | El *normal version* `X.Y.Z` (el prefijo, sin importar si trae sufijo `-pre`/`+build`) son tres enteros no negativos sin ceros iniciales |
| `prerelease` | 9 | Si hay sufijo `-...`: identificadores no vacíos, `[0-9A-Za-z-]`, sin cero inicial en los numéricos. Un `-` sin nada detrás es un identificador vacío: inválido |
| `build` | 10 | Si hay sufijo `+...`: identificadores no vacíos y de solo `[0-9A-Za-z-]` (a diferencia de pre-release, sí puede llevar ceros iniciales). Un `+` sin nada detrás es inválido por el mismo motivo |

`formato` **no** rechaza una version por tener un sufijo válido — `1.2.3-alpha+001` cumple `formato`
igual que `1.2.3`, porque el artículo 2 describe el prefijo, no la ausencia de sufijos. Eso lo miden
`prerelease` y `build` por separado, cada uno sobre su propio artículo.

## Límite declarado, sin excepciones

El script lee código Python vía `ast` y `pyproject.toml` vía `tomllib` (stdlib desde Python 3.11); no
ejecuta nada y no tiene un parser real de SemVer. Solo reconoce un literal de string: un `__version__`
asignado en Python, o `[project].version` en TOML. Una versión armada por concatenación, f-string, o
declarada `dynamic = ["version"]` en `pyproject.toml` (la resuelve el backend de build, no es un
literal) no la ve — no es un defecto a ajustar con más regex, es el límite de leer el dato en vez de
ejecutar el proyecto, y hay que decirlo así si el usuario pregunta por qué no detectó algo.

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
