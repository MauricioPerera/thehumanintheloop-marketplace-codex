---
name: kdd-arquitectura-java
description: 'Verifica 8 reglas de arquitectura y codigo limpio: capas, excepciones, ISP, inversion de control/DI/Factory, AOP, convencion de nombres (COC), duplicacion (DRY) y polimorfismo antes que if/else. Usala cuando el usuario pida revisar o auditar arquitectura por capas, inyeccion de dependencias o principios SOLID en un proyecto Python.'
---

# KDD Arquitectura Java Solida Checker

Extraido de "Arquitectura Java solida" con el metodo [Knowledge-Driven
Development](https://github.com/MauricioPerera/kdd-book) (kdd-book). De 33 secciones, 15 caen en
pila A -el porcentaje contractable mas alto entre los libros de codigo del corpus-: los principios
de arquitectura resultan tan medibles como las heuristicas de código limpio porque son propiedades
del grafo de dependencias e instanciación, justo lo que un analisis estatico lee de forma nativa.
"Semantico" para un humano no implica "no medible" para un parser.

## Flujo

1. **Para las reglas de arquitectura** (`capas`, `excepciones`, `isp`, `instanciacion`, `aop`,
   `coc`), encontra la raiz del proyecto: estas reglas miden relaciones **entre modulos** -una
   capa, quien crea a quien-, y derivar la raiz del archivo que se esta tocando escanearia solo su
   propia capa, dando siempre verde.
2. **Corré las reglas**:

   ```bash
   python scripts/arch_checks.py --rule capas \
     --capa presentacion=vistas --capa negocio=servicios --capa persistencia=dao \
     --permite presentacion>negocio --permite negocio>persistencia <raiz>
   python scripts/arch_checks.py --rule excepciones <raiz>
   python scripts/arch_checks.py --rule isp <raiz>
   python scripts/arch_checks.py --rule instanciacion <raiz>
   python scripts/arch_checks.py --rule instanciacion --permite-crear factoria <raiz>
   python scripts/arch_checks.py --rule aop <raiz>
   python scripts/arch_checks.py --rule coc --esquema tabla.sql <raiz>
   python scripts/checks.py --rule g5 --max 0 <archivo.py> [...]
   python scripts/checks.py --rule g23 --max 2 <archivo.py> [...]
   ```

   `capas` exige que el proyecto **declare** sus capas y las relaciones permitidas con
   `--capa`/`--permite`: una regla de capas que el instrumento adivinara no seria una regla, seria
   una opinión. `coc` exige `--esquema` (el archivo con el esquema de la tabla). Ningún valor se
   adivina. Exit `0` (cumple), `1` (no cumple, con detalle) o `2` (no se pudo verificar).
3. **Reportá las 8 reglas siempre**, con `[PASSED]` / `[FAILED]` / `[NO VERIFICABLE]`.
4. **Para el resto del libro** (18 de las 33 secciones), consultá `scripts/knowledge.json` antes
   de responder. Cada nodo trae `pile` (`A`=medible, `B`=juicio real sin umbral, `C`=referencia) y,
   si es `B`, un `why_not`. **No inventes una regla para lo que el nodo dice que requiere juicio.**

## Reglas medibles (pila A)

| Regla | Script | Qué mide |
|---|---|---|
| `capas` | arch_checks.py | Nadie importa fuera de las capas y direcciones declaradas (cubre SRP, MVC, DAO, capa de servicio) |
| `excepciones` | arch_checks.py | Cero `except` mudos (`pass`) o excesivamente amplios (`except Exception`/`except:`) |
| `isp` | arch_checks.py | Nadie depende de una interfaz con métodos que no usa |
| `instanciacion` | arch_checks.py | Una clase de negocio no crea directamente a sus colaboradores -inversión de control/DI-; con `--permite-crear` se acepta que una fábrica declarada sí instancie |
| `aop` | arch_checks.py | Lo transversal (logging, transacciones, seguridad) vive fuera de las clases de negocio |
| `coc` | arch_checks.py | Los campos de la clase siguen la convención de nombres de la tabla declarada (`--esquema`) |
| `g5` | checks.py | G5 Duplicación: cero bloques de código repetidos |
| `g23` | checks.py | G23 Polimorfismo antes que `if`/`else`/`switch` sobre tipo |

## Límite declarado, sin excepciones

Las reglas de `arch_checks.py` leen el grafo de imports e instanciación vía `ast`: no ejecutan
nada, y una capa/relación no declarada explícitamente por el proyecto es `NO VERIFICABLE`, nunca
una suposición. `checks.py` es el mismo instrumento multi-regla usado por otras fuentes del
corpus (Clean Code); aquí solo se citan `g5` y `g23`, pero se incluye el archivo completo -son un
único módulo, no partes separables- documentado en `scripts/knowledge.json`.

## Reporte

| Regla | Estado | Archivo:línea | Detalle |
|---|---|---|---|
| capas | [PASSED]/[FAILED]/[NO VERIFICABLE] | ... | ... |
| excepciones | ... | ... | ... |
| isp | ... | ... | ... |
| instanciacion | ... | ... | ... |
| aop | ... | ... | ... |
| coc | ... | ... | ... |
| g5 | ... | ... | ... |
| g23 | ... | ... | ... |

## Recursos incluidos

- `scripts/arch_checks.py` (6 reglas) + `scripts/checks.py` (22 reglas, de las cuales esta fuente
  cita 2: `g5`, `g23`) -sin dependencias externas, extraídos y verificados en
  [kdd-book](https://github.com/MauricioPerera/kdd-book).
- `scripts/knowledge.json` -las 33 secciones del libro, triadas en pila A/B/C con su `why_not`
  cuando corresponde.
