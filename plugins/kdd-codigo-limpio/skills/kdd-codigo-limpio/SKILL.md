---
name: kdd-codigo-limpio
description: 'Verifica 30 heuristicas de Codigo Limpio (Clean Code, Robert Martin): comentarios, funciones (argumentos, muertas, de salida), heuristicas generales (duplicacion, numeros magicos, condicionales, encapsulado, separacion vertical), nombres, pruebas (rapidas, aisladas, con cobertura, con mutantes en los limites) y profundidad de cadena (Ley de Demeter). Usala cuando el usuario pida revisar o auditar codigo Python contra Clean Code.'
---

# KDD Código Limpio Checker

Extraído de "Código Limpio" (Clean Code, Robert C. Martin) con el método
[Knowledge-Driven Development](https://github.com/MauricioPerera/kdd-book) (kdd-book). De 66
heurísticas del catálogo del libro, 32 caen en pila A -y **31 de esas 32 tienen instrumento
real**: la única excepción es J1 ("evitar listas de importación extensas usando comodines"),
consejo de la era Java que Python invierte -el propio estilo del lenguaje **prohíbe** los
wildcard imports-, así que "cero imports con comodín" ya lo mide la regla `imports` de
`kdd-pep8` y agregar aquí una regla trivialmente siempre-verde no mediría nada nuevo.

## Flujo

1. **Encontrá el código Python relevante.** La mayoría de las reglas son por archivo; `limites`
   (mutación) además necesita que el proyecto tenga su propia suite de tests corriendo, porque
   muta el código y mira si esa suite atrapa al mutante.
2. **Corré las 30 reglas**:

   ```bash
   python scripts/checks.py --rule <regla> --max <N> <archivo.py> [...]
   python scripts/repo_checks.py --rule <regla> <archivo.py>
   python scripts/params_max.py --max 3 <archivo.py> [...]
   python scripts/chain_depth.py --max 1 <archivo.py> [...]
   python scripts/mutation_checks.py --rule limites --mutar <archivo.py> --proyecto <raiz>
   ```

   Cada regla de `checks.py` trae su propio `max` por defecto (ver `--list`); `params_max` y
   `chain_depth` exigen `--max` explícito -no hay un límite "correcto" universal para argumentos o
   profundidad de cadena, así que el proyecto lo declara-. Exit `0` (cumple), `1` (no cumple, con
   detalle) o `2` (no se pudo verificar).
3. **Reportá las 30 reglas siempre**, con `[PASSED]` / `[FAILED]` / `[NO VERIFICABLE]`.
4. **Para el resto del libro** (31 en pila B, 3 en pila C, y J1), consultá `scripts/knowledge.json`
   antes de responder. Cada nodo trae `pile`, `verification` y, si es `B`, un `why_not`. **No
   inventes una regla para lo que el nodo dice que requiere juicio -o que, como J1, ya está cubierta
   por otro plugin y no mide nada nuevo en Python.**

## Reglas medibles (pila A), agrupadas por capítulo de Clean Code

| Grupo | Reglas | Script | Qué miden |
|---|---|---|---|
| Comentarios | `c5` | checks.py | C5 código comentado |
| Funciones | `f2`, `f3`/`g15`, `f4`/`g9`, `f1` (`params_max.py`) | checks.py, params_max.py | F2 argumentos de salida; F3/G15 argumento indicador o selector; F4/G9 función muerta; F1 demasiados argumentos |
| Generales (G) | `g4`, `g5`, `g7`, `g8`, `g10`, `g12`, `g14`, `g23`, `g25`, `g28`, `g29`, `g33`, `g3`/`limites` (`mutation_checks.py`), `g36` (`chain_depth.py`) | checks.py, mutation_checks.py, chain_depth.py | Medidas de seguridad canceladas; duplicación; clase base que depende de su variante; exceso de información (superficie pública); separación vertical; desorden; envidia de características; polimorfismo antes que if/else; números mágicos; encapsular condicionales; evitar condicionales negativas; encapsular condiciones de límite; comportamiento incorrecto en los límites (mutación); evitar cadenas largas de accesos (Ley de Demeter) |
| Nombres (N) | `n5`, `n6` | checks.py | Nombres extensos para ámbitos extensos; evitar codificaciones en el nombre |
| Java (J) | `j2` | checks.py | J2 no heredar constantes |
| Tests (E/T) | `e1`, `e2`, `t1`, `t2`, `t9`, `aislamiento`, `t5`/`limites` (`mutation_checks.py`), `anatomia` | repo_checks.py, mutation_checks.py, checks.py | Generar/probar en un solo paso; pruebas suficientes (cobertura de línea); usar herramienta de cobertura; pruebas rápidas; pruebas aisladas entre sí; probar condiciones de límite (mutación); anatomía del test (sin aserción no prueba nada) |

## Límite declarado, sin excepciones

Todas las reglas de `checks.py`/`repo_checks.py`/`params_max.py`/`chain_depth.py` leen código vía
`ast`, sin ejecutar nada. `mutation_checks.py` es la excepción: sí ejecuta -corre la suite de
tests del proyecto contra una versión mutada del archivo objetivo (`--mutar`), y por eso necesita
`--proyecto` -sin la suite real no hay nada que "sobreviva" o no a la mutación-.

## Reporte

| Regla | Estado | Archivo:línea | Detalle |
|---|---|---|---|
| (una fila por cada una de las 30 reglas) | [PASSED]/[FAILED]/[NO VERIFICABLE] | ... | ... |

## Recursos incluidos

- `scripts/checks.py` (21 reglas citadas de 22 totales, compartido con otras fuentes del corpus),
  `scripts/repo_checks.py` (6 reglas citadas de 7), `scripts/params_max.py` (F1), `scripts/chain_depth.py`
  (G36) y `scripts/mutation_checks.py` (G3/T5, comparte la regla `limites`) -sin dependencias
  externas, extraídos y verificados en [kdd-book](https://github.com/MauricioPerera/kdd-book).
- `scripts/knowledge.json` -las 66 heurísticas del catálogo, triadas en pila A/B/C con su
  `why_not` cuando corresponde, incluyendo J1 documentada como pila A sin instrumento nuevo.
