---
name: kdd-pep8
description: 'Verifica 28 reglas de PEP 8 (Style Guide for Python Code): indentacion, longitud de linea, imports, comillas, comentarios, docstrings y las 15 convenciones de nombres (funciones, clases, constantes, excepciones, modulos, etc). Usala cuando el usuario pida revisar o auditar estilo PEP 8 en codigo Python.'
---

# KDD PEP 8 Checker

Extraido de [PEP 8 — Style Guide for Python Code](https://peps.python.org/pep-0008/) con el
método [Knowledge-Driven Development](https://github.com/MauricioPerera/kdd-book) (kdd-book). De
42 secciones, 29 caen en pila A (69%) -el porcentaje contractable más alto del corpus-: un
estándar de estilo describe reglas de forma, y la forma es exactamente lo que un parser lee sin
ambigüedad.

## Flujo

1. **Encontrá el código Python relevante** para la regla (un archivo puntual; ninguna regla de
   esta fuente necesita el proyecto entero).
2. **Corré las 28 reglas** contra ese archivo:

   ```bash
   python scripts/pep8_checks.py --rule sangria <archivo.py> [...]
   python scripts/pep8_checks.py --rule operador <archivo.py> [...]
   python scripts/pep8_checks.py --rule blancos <archivo.py> [...]
   python scripts/pep8_checks.py --rule codificacion <archivo.py> [...]
   python scripts/pep8_checks.py --rule imports <archivo.py> [...]
   python scripts/pep8_checks.py --rule dunder <archivo.py> [...]
   python scripts/pep8_checks.py --rule comillas <archivo.py> [...]
   python scripts/pep8_checks.py --rule espacios <archivo.py> [...]
   python scripts/pep8_checks.py --rule operadores <archivo.py> [...]
   python scripts/pep8_checks.py --rule comafinal <archivo.py> [...]
   python scripts/pep8_checks.py --rule bloque <archivo.py> [...]
   python scripts/pep8_checks.py --rule enlinea <archivo.py> [...]
   python scripts/pep8_checks.py --rule docstring <archivo.py> [...]
   python scripts/pep8_checks.py --rule ambiguos <archivo.py> [...]
   python scripts/pep8_checks.py --rule ascii <archivo.py> [...]
   python scripts/pep8_checks.py --rule modulo <archivo.py> [...]
   python scripts/pep8_checks.py --rule clase <archivo.py> [...]
   python scripts/pep8_checks.py --rule tipovar <archivo.py> [...]
   python scripts/pep8_checks.py --rule excepcion <archivo.py> [...]
   python scripts/pep8_checks.py --rule global <archivo.py> [...]
   python scripts/pep8_checks.py --rule funcion <archivo.py> [...]
   python scripts/pep8_checks.py --rule primerarg <archivo.py> [...]
   python scripts/pep8_checks.py --rule metodo <archivo.py> [...]
   python scripts/pep8_checks.py --rule constante <archivo.py> [...]
   python scripts/pep8_checks.py --rule publica <archivo.py> [...]
   python scripts/pep8_checks.py --rule anotafuncion <archivo.py> [...]
   python scripts/pep8_checks.py --rule anotavariable <archivo.py> [...]
   python scripts/repo_checks.py --rule g24 --max-line 79 <archivo.py>
   ```

   `--impuesto` (en `pep8_checks.py`) declara nombres de método cuyo estilo lo impone un
   framework (p. ej. `setUp`), para no marcarlos como violación de `funcion`/`metodo`. Ningún
   valor se adivina. Exit `0` (cumple), `1` (no cumple, con detalle) o `2` (no se pudo verificar).
3. **Reportá las 28 reglas siempre**, con `[PASSED]` / `[FAILED]` / `[NO VERIFICABLE]`.
4. **Para el resto de PEP 8** (13 de las 42 secciones), consultá `scripts/knowledge.json` antes de
   responder. Cada nodo trae `pile` (`A`=medible, `B`=juicio real sin umbral, `C`=referencia) y,
   si es `B`, un `why_not`. **No inventes una regla para lo que el nodo dice que requiere juicio.**

## Reglas medibles (pila A), agrupadas

| Grupo | Reglas | Qué miden |
|---|---|---|
| Forma del código | `sangria`, `operador`, `blancos`, `codificacion`, `comafinal`, `espacios`, `operadores` | Indentación, corte de línea antes de operador binario, líneas en blanco, encoding declarado, coma final, espacios sobrantes/segun contexto |
| Longitud de línea | `g24` (repo_checks.py, `--max-line 79`) | Máximo de caracteres por línea |
| Imports | `imports`, `dunder` | Uno por línea sin comodines arriba del archivo; dunders de módulo antes de los imports |
| Comentarios y docs | `bloque`, `enlinea`, `docstring` | Comentarios de bloque empiezan con `# `, dos espacios antes de un comentario en línea, toda API pública tiene docstring |
| Comillas y anotaciones | `comillas`, `anotafuncion`, `anotavariable` | Usar la otra comilla en vez de escapar; espaciado de anotaciones de tipo |
| Superficie pública | `publica` | El módulo declara `__all__` |
| Nombres (15 reglas) | `ambiguos`, `ascii`, `modulo`, `clase`, `tipovar`, `excepcion`, `global`, `funcion`, `primerarg`, `metodo`, `constante` | Ninguna variable se llama `l`/`O`/`I`; identificadores ASCII; `snake_case`/`CapWords`/`UPPER_CASE` según el tipo de nombre; excepciones terminan en `Error`; primer argumento `self`/`cls` |

## Límite declarado, sin excepciones

Son heurísticas textuales/AST: no ejecutan el código. `--impuesto` existe porque un framework de
testing (p. ej. `unittest`) exige nombres de método (`setUp`) que PEP 8 marcaría como violación;
sin declararlo, el instrumento reportaría un falso positivo por seguir una convención ajena al
proyecto.

## Reporte

| Regla | Estado | Archivo:línea | Detalle |
|---|---|---|---|
| (una fila por cada una de las 28 reglas) | [PASSED]/[FAILED]/[NO VERIFICABLE] | ... | ... |

## Recursos incluidos

- `scripts/pep8_checks.py` (27 reglas) + `scripts/repo_checks.py` (7 reglas, de las cuales esta
  fuente cita 1: `g24`) -sin dependencias externas, extraídos y verificados en
  [kdd-book](https://github.com/MauricioPerera/kdd-book).
- `scripts/knowledge.json` -las 42 secciones de PEP 8, triadas en pila A/B/C con su `why_not`
  cuando corresponde.
