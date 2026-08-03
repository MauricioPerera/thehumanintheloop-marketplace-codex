---
name: kdd-estilo-google
description: 'Verifica 42 reglas del Google developer documentation style guide: puntuacion, numeros/unidades/fechas, encabezados y estructura, bloques de codigo y sintaxis CLI, voz/tiempo verbal, y vocabulario declarado por el proyecto (lista de palabras, jerga, lenguaje inclusivo, nombres de producto, tipos de aviso). Usala cuando el usuario pida revisar o auditar documentacion tecnica contra el estilo de Google.'
---

# KDD Estilo Google Checker

Extraído de la [Google developer documentation style guide](https://developers.google.com/style)
con el método [Knowledge-Driven Development](https://github.com/MauricioPerera/kdd-book)
(kdd-book). De 80 secciones, 42 caen en pila A: es una guía de estilo de prosa técnica, y casi
todas sus reglas son de forma -puntuación, mayúsculas, tiempo verbal-, verificable por texto sin
necesitar entender el contenido.

## Flujo

1. **Encontrá el documento** (Markdown o texto plano) a auditar.
2. **Corré las 42 reglas**:

   ```bash
   python scripts/prosa_checks.py --rule coma-serial <documento.md> [...]
   python scripts/prosa_checks.py --rule bloques-codigo --ancho-codigo 80 <documento.md>
   python scripts/prosa_checks.py --rule lista-palabras --lista terminos.json <documento.md>
   python scripts/prosa_checks.py --rule inclusivo --inclusivo no-inclusivo.json <documento.md>
   python scripts/prosa_checks.py --rule jerga --jerga jerga-dominio.json <documento.md>
   python scripts/prosa_checks.py --rule nombres-producto --productos productos.json <documento.md>
   python scripts/prosa_checks.py --rule posesivo-producto --productos productos.json <documento.md>
   python scripts/prosa_checks.py --rule avisos-tipo --avisos tipos-aviso.json <documento.md>
   ```

   **5 reglas exigen que el proyecto declare su propio vocabulario en JSON** -la guía dice "evitá
   la jerga fuera de tu lista" o "usá lenguaje inclusivo" pero no puede decir CUÁL es la lista de
   cada proyecto; adivinarla inventaría la convención-:
   - `lista-palabras` → `--lista {termino: alternativa}`
   - `inclusivo` → `--inclusivo` (términos no inclusivos a evitar)
   - `jerga` → `--jerga` (jerga del dominio del proyecto)
   - `nombres-producto` / `posesivo-producto` → `--productos` (grafía declarada de cada producto)
   - `avisos-tipo` → `--avisos` (tipos de aviso declarados, p. ej. Note/Warning/Important)

   Sin el JSON correspondiente, esas 5 reglas son `NO VERIFICABLE`, no un verde barato. Las otras
   37 no necesitan configuración. Exit `0` (cumple), `1` (no cumple, con detalle) o `2` (no se pudo
   verificar).
3. **Reportá las 42 reglas siempre**, con `[PASSED]` / `[FAILED]` / `[NO VERIFICABLE]`.
4. **Para el resto de la guía** (38 de las 80 secciones), consultá `scripts/knowledge.json` antes
   de responder. Cada nodo trae `pile` (`A`=medible, `B`=juicio real sin umbral, `C`=referencia) y,
   si es `B`, un `why_not`. **No inventes una regla para lo que el nodo dice que requiere juicio.**

## Reglas medibles (pila A), agrupadas

| Grupo | Reglas | Qué miden |
|---|---|---|
| Puntuación | `coma-serial`, `comillas-puntuacion`, `mayuscula-dos-puntos`, `punto-final`, `puntos-suspensivos`, `raya`, `parentesis-anidados`, `plural-parentesis`, `and-or` | Coma serial en enumeraciones; puntuación dentro de comillas; mayúscula tras dos puntos si sigue oración completa; un espacio tras el punto; carácter de elipsis en vez de tres puntos; raya larga sin espacios; sin paréntesis anidados; plurales con "(s)"; "and/or" y la barra como "o" |
| Números, unidades, fechas | `numeros-chicos`, `unidades`, `fechas`, `telefonos`, `dominios` | Del uno al nueve con letra; espacio entre número y unidad; sin ordinales en fechas; rango reservado para teléfonos y dominios de ejemplo |
| Encabezados y estructura | `encabezados-caja`, `encabezados-unicos`, `anclas`, `tablas-encabezado`, `items-lista` | Encabezados en minúscula de oración; únicos y sin punto final; el ancla de enlace existe; toda tabla tiene fila de encabezado; mayúscula inicial y puntuación coherente en listas |
| Código y CLI | `bloques-codigo`, `marcadores`, `sintaxis-cli`, `nombres-archivo`, `html-en-markdown`, `notacion-matematica` | Largo de línea y sin elisiones en muestras de código; placeholders en minúsculas con guiones; corchetes (no "(optional)") en sintaxis de línea de comandos; nombres de archivo en minúsculas con guiones; sin HTML crudo en Markdown; un solo estilo de notación matemática |
| Voz y tiempo verbal | `primera-persona`, `tiempo-futuro`, `tiempo-relativo`, `procedimientos`, `minimizadores`, `verbos-interaccion`, `texto-enlace` | Segunda persona en instrucciones (no primera persona); tiempo presente evitando futuro; sin marcas de tiempo relativas ("actualmente", "próximamente"); cada paso de un procedimiento empieza con un verbo; sin adjetivos que minimizan el esfuerzo ("simplemente", "solo"); verbos de interacción desaconsejados con elementos de UI; texto de enlace descriptivo |
| Vocabulario declarado por el proyecto | `lista-palabras`, `inclusivo`, `jerga`, `nombres-producto`, `posesivo-producto`, `avisos-tipo` | Ver arriba: requieren `--lista`/`--inclusivo`/`--jerga`/`--productos`/`--avisos` |
| Otras | `abreviaturas-latinas`, `alt-texto`, `notas-pie`, `pronombres-genero` | Sin abreviaturas latinas (e.g., i.e., etc.); toda imagen tiene texto alternativo; la guía desaconseja las notas al pie; pronombres de género |

## Límite declarado, sin excepciones

Es un instrumento de texto: no renderiza el Markdown ni ejecuta nada. Las 5 reglas de vocabulario
declarado son `NO VERIFICABLE` sin su JSON correspondiente a propósito -inventar una lista de
jerga o de lenguaje no inclusivo sería imponer la convención de otro proyecto.

## Reporte

| Regla | Estado | Archivo:línea | Detalle |
|---|---|---|---|
| (una fila por cada una de las 42 reglas) | [PASSED]/[FAILED]/[NO VERIFICABLE] | ... | ... |

## Recursos incluidos

- `scripts/prosa_checks.py` -instrumento sin dependencias externas, extraído y verificado (18
  pruebas, 72 subtests) en [kdd-book](https://github.com/MauricioPerera/kdd-book).
- `scripts/knowledge.json` -las 80 secciones de la guía, triadas en pila A/B/C con su `why_not`
  cuando corresponde.
