---
name: kdd-doce-factores
description: 'Verifica proyectos contra 10 tecnicas de The Twelve-Factor App: dependencias declaradas, config en el entorno, servicios como recursos adjuntos, port binding, paridad dev/prod, sin daemonizacion, manejo de SIGTERM, logs a stdout, codebase unico bajo control de version, y release ID. Usala cuando el usuario pida revisar o auditar la arquitectura de despliegue de una app.'
---

# KDD Twelve-Factor App Checker

Extraido de [The Twelve-Factor App](https://12factor.net) con el método [Knowledge-Driven
Development](https://github.com/MauricioPerera/kdd-book) (kdd-book). Es la fuente con el porcentaje
contractable más alto del corpus (62,5%, o 10 de 12 sobre los factores solos, sin el preámbulo): un
manifiesto es prescripción pura, sin una línea de relleno, y eso predice que quede por encima de los
libros de código.

## Flujo

1. **Encontrá el punto de entrada del proyecto** (el script/módulo principal) y, si corresponde, el
   manifiesto de dependencias y los archivos de despliegue.
2. **Corré los chequeos** relevantes:

   ```bash
   python scripts/entorno_checks.py --rule dependencias --manifiesto requirements.txt <entrada.py>
   python scripts/entorno_checks.py --rule config <entrada.py>
   python scripts/entorno_checks.py --rule servicios <entrada.py>
   python scripts/entorno_checks.py --rule puerto <entrada.py>
   python scripts/entorno_checks.py --rule paridad --despliegue dev=a.yml --despliegue prod=b.yml <entrada.py>
   python scripts/entorno_checks.py --rule daemonizar <entrada.py>
   python scripts/entorno_checks.py --rule sigterm <entrada.py>
   python scripts/entorno_checks.py --rule logs <entrada.py>
   python scripts/git_checks.py --rule codebase <repo>
   python scripts/git_checks.py --rule releaseid <repo>
   ```

   `dependencias` y `paridad` necesitan que se declare explícitamente cuál archivo es el manifiesto o
   los despliegues -pedirlo, no adivinarlo, porque el formato depende del gestor de paquetes del
   proyecto-. Exit `0` (cumple), `1` (no cumple, con detalle) o `2` (no se pudo verificar).
3. **Reportá cada regla corrida** con `[PASSED]` / `[FAILED]` / `[NO VERIFICABLE]`.
4. **Para el resto de los 16 ítems** (el preámbulo y las 2 técnicas de proceso/juicio), consultá
   `scripts/knowledge.json`. Cada nodo trae `pile` (`A`=medible, `B`=juicio real sin umbral,
   `C`=conocimiento) y, si es `B`, un `why_not`.

## Reglas medibles (pila A)

| Regla | Factor | Qué mide |
|---|---|---|
| `dependencias` | Dependencies | Todo import de terceros está en el manifiesto declarado |
| `config` | Config | Cero constantes de configuración y credenciales en el código |
| `servicios` | Backing services | Cero locators de servicio (URLs de conexión) escritos en el código |
| `puerto` | Port binding | La app abre su propio puerto |
| `paridad` | Dev/prod parity | Los despliegues declarados usan la misma versión de cada servicio |
| `daemonizar` | Disposability | Cero daemonización y cero archivos PID |
| `sigterm` | Disposability | El proceso instala un manejador de SIGTERM |
| `logs` | Logs | Cero handlers de logging que escriban a archivo |
| `codebase` | Codebase | Un solo repositorio por aplicación, bajo control de versiones |
| `releaseid` | Build, release, run | Todo release tiene un identificador propio |

## Límite declarado, sin excepciones

Las reglas que buscan un marcador léxico -una credencial, un locator- encuentran lo que se escribe
con las palabras de la convención declarada; una clave asignada a una variable llamada `x` no la ve
nadie. Eso no se arregla afinando la expresión regular: es el límite de leer el código en vez de
ejecutarlo.

## Reporte

| Regla | Estado | Archivo:línea | Detalle |
|---|---|---|---|
| (una fila por cada regla corrida) | [PASSED]/[FAILED]/[NO VERIFICABLE] | ... | ... |

## Recursos incluidos

- `scripts/entorno_checks.py` (8 reglas) + `scripts/git_checks.py` (2 de sus 5 reglas se usan acá;
  las otras 3 son técnicas legítimas sin forma de ejercicio, documentadas en `knowledge.json`) —
  extraídos y verificados en [kdd-book](https://github.com/MauricioPerera/kdd-book).
- `scripts/knowledge.json` — los 16 ítems de la fuente, triados en pila A/B/C con su `why_not`
  cuando corresponde.
