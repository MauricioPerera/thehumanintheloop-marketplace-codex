---
name: kdd-scrum-xp
description: 'Verifica 12 tecnicas de Scrum y eXtreme Programming con instrumento real: cadencia de entregas, unificacion de repositorio, orden del ciclo TDD, y 8 heuristicas de Clean Code (metodos extensos, codigo duplicado, cobertura, aislamiento de tests). Documenta ademas 22 tecnicas del mismo libro que kdd-book triό como pila A pero que este instrumento no puede medir sin acceso a un tablero, calendario o pipeline de CI reales -usala igual para consultar ese mapa antes de inventar una regla de tablero o de ceremonias.'
---

# KDD Scrum y XP Checker

Extraído de "Scrum y eXtreme Programming para Programadores" (Bahit) con el método
[Knowledge-Driven Development](https://github.com/MauricioPerera/kdd-book) (kdd-book). De 153
secciones, 39 caen en pila A -pero **solo 17 de esos 39 nodos (12 reglas distintas) tienen un
instrumento de texto real**; los otros 22 son pila A en la propia clasificación de kdd-book
(miden algo concreto, con umbral) pero requieren leer un tablero Kanban, un calendario de
ceremonias o un pipeline de CI -evidencia que vive fuera del código y que este plugin no tiene
forma de leer sin integrarse a esas herramientas-. Este plugin porta los 12 con instrumento y
documenta los 22 sin él, en vez de inventarles una heurística de texto que no mediría lo mismo.

## Flujo

1. **Corré las 12 reglas con instrumento real**:

   ```bash
   python scripts/git_checks.py --rule cadencia <repo>
   python scripts/git_checks.py --rule tddorden <repo>
   python scripts/git_checks.py --rule repounico <repo>
   python scripts/repo_checks.py --rule e2 <archivo.py>
   python scripts/repo_checks.py --rule g24 --max-line 79 <archivo.py>
   python scripts/repo_checks.py --rule t9 --max-seconds 5 <archivo.py>
   python scripts/repo_checks.py --rule aislamiento <archivo.py>
   python scripts/checks.py --rule anatomia --max 0 <archivo.py> [...]
   python scripts/checks.py --rule g12 --max 0 <archivo.py> [...]
   python scripts/checks.py --rule exprops --max 3 <archivo.py> [...]
   python scripts/checks.py --rule metlineas --max 15 <archivo.py> [...]
   python scripts/checks.py --rule g5 --max 0 <archivo.py> [...]
   ```

   Exit `0` (cumple), `1` (no cumple, con detalle) o `2` (no se pudo verificar).
2. **Reportá esas 12 reglas siempre**, con `[PASSED]` / `[FAILED]` / `[NO VERIFICABLE]`.
3. **Para las 22 técnicas sin instrumento** (ver tabla abajo) y para el resto del libro (78
   secciones en pila C, 36 en pila B), consultá `scripts/knowledge.json` antes de responder. Cada
   nodo trae `pile`, `verification` (`instrumented`/`proxy`/`none`) y, si es `B`, un `why_not`.
   **No inventes una regla de tablero, calendario o CI para lo que el nodo dice que necesita esa
   evidencia externa.**

## Reglas medibles con instrumento (pila A, 12 reglas)

| Regla | Script | Qué mide |
|---|---|---|
| `cadencia` | git_checks.py | Hueco máximo entre entregas (cubre "entregas cortas", Principio #3 y Práctica #7) |
| `tddorden` | git_checks.py | El test entra antes que el código en el historial (ciclo TDD: rojo, verde, refactor) |
| `repounico` | git_checks.py | El código vive unificado en un único repositorio |
| `e2` | repo_checks.py | E2 Probar en un solo paso (cubre "Testing" y los 4 pasos del ciclo TDD) |
| `g24` | repo_checks.py | G24 Seguir las convenciones estándar declaradas (código estándar/coding standards) |
| `t9` | repo_checks.py | T9 Las pruebas deben ser rápidas |
| `aislamiento` | repo_checks.py | Pruebas unitarias independientes entre sí |
| `anatomia` | checks.py | Anatomía del test: sin aserción no prueba nada |
| `g12` | checks.py | G12 Desorden (variables de uso temporal mal implementadas) |
| `exprops` | checks.py | Expresiones extensas: operadores por expresión |
| `metlineas` | checks.py | Métodos extensos: líneas por función |
| `g5` | checks.py | G5 Duplicación (código duplicado, con o sin herencia compartida) |

## Las 22 técnicas sin instrumento (pila A en kdd-book, sin script aquí)

| Grupo | Cuántas | Ejemplos | Por qué no hay script |
|---|---|---|---|
| Tablero Kanban/Scrum | 12 | Backlog ordenado, formato del ítem, priorización, estimación, criterios de aceptación, sprint backlog, historias con tareas, columnas del proceso, WIP | Requiere leer el estado de un tablero real (Jira, Trello, GitHub Projects); sin integrarse a esa API no hay nada que un script sobre el código pueda parsear |
| Calendario de ceremonias | 4 | Planificación, reunión diaria, revisión, retrospectiva ocurridas en el momento que corresponde | Requiere un calendario o bitácora de reuniones; el historial de git mide cadencia de *entregas*, no de *ceremonias* |
| Build/CI | 1 | Incremento de funcionalidad entregado como build | Requiere un pipeline de build real, no solo el código fuente |
| CI y test_command declarados | 5 | CI corrida por commit con exit 0; test_command de integración/aceptación/funcional/sistema | El comando de test lo declara cada proyecto (no hay un nombre fijo que un instrumento pueda invocar); es "correr lo que el proyecto declare y mirar el exit code", no una propiedad del código fuente en sí |

## Límite declarado, sin excepciones

Las 12 reglas con instrumento leen código y `git log`: ninguna ejecuta el proyecto ni asume una
integración externa. Documentar las 22 sin instrumento en vez de forzarles una regla de texto es
la misma disciplina que ya se aplicó en `kdd-zen-of-python` y `kdd-agile-manifesto`: un 0%
instrumentable en una porción de la fuente es un resultado correcto, no una falla del triaje.

## Reporte

| Regla | Estado | Archivo/Repo | Detalle |
|---|---|---|---|
| (una fila por cada una de las 12 reglas con instrumento) | [PASSED]/[FAILED]/[NO VERIFICABLE] | ... | ... |

## Recursos incluidos

- `scripts/git_checks.py` (5 reglas, 3 citadas: `cadencia`, `tddorden`, `repounico`) +
  `scripts/repo_checks.py` (7 reglas, 4 citadas: `e2`, `g24`, `t9`, `aislamiento`) +
  `scripts/checks.py` (22 reglas, 5 citadas: `anatomia`, `g12`, `exprops`, `metlineas`, `g5`) -sin
  dependencias externas, compartidos con otras fuentes del corpus y extraídos y verificados en
  [kdd-book](https://github.com/MauricioPerera/kdd-book).
- `scripts/knowledge.json` -las 153 secciones del libro, triadas en pila A/B/C, con
  `verification` (`instrumented`/`proxy`/`none`) y `why_not` cuando corresponde.
