---
name: kdd-dockerfile
description: 'Verifica 11 reglas duras de Dockerfile best practices (docs.docker.com): FROM sin pin, apt-get update sin install ni limpieza, CMD/ENTRYPOINT en shell form, USER root, sudo instalado, WORKDIR relativo, ADD en vez de COPY, pipe sin pipefail, .dockerignore ausente. Usala cuando el usuario pida revisar o auditar un Dockerfile.'
---

# KDD Dockerfile Checker

Extraído de [Dockerfile best practices](https://docs.docker.com/build/building/best-practices/)
con el método [Knowledge-Driven Development](https://github.com/MauricioPerera/kdd-book)
(kdd-book). La guía tiene muchas más recomendaciones ("should", "consider") que exigen juzgar el
diseño del servicio — si conviene multi-stage, si un proceso puede correr sin privilegios, qué
labels agregar — y esas quedan en `scripts/knowledge.json` como pila B, nunca simuladas como
regla dura.

## Flujo

1. **Encontrá el `Dockerfile` puntual** (y su `.dockerignore` si existe en el mismo directorio;
   ninguna de las 11 reglas necesita más contexto que eso).
2. **Corré las 11 reglas** contra ese archivo:

   ```bash
   python scripts/dockerfile_checks.py --rule fromlatest <Dockerfile> [...]
   python scripts/dockerfile_checks.py --rule aptcombine <Dockerfile> [...]
   python scripts/dockerfile_checks.py --rule aptcleanup <Dockerfile> [...]
   python scripts/dockerfile_checks.py --rule execform <Dockerfile> [...]
   python scripts/dockerfile_checks.py --rule userroot <Dockerfile> [...]
   python scripts/dockerfile_checks.py --rule sudoinstall <Dockerfile> [...]
   python scripts/dockerfile_checks.py --rule workdirabs <Dockerfile> [...]
   python scripts/dockerfile_checks.py --rule cdinstead <Dockerfile> [...]
   python scripts/dockerfile_checks.py --rule addvscopy <Dockerfile> [...]
   python scripts/dockerfile_checks.py --rule pipefail <Dockerfile> [...]
   python scripts/dockerfile_checks.py --rule dockerignore <Dockerfile> [...]
   ```

   El script une las continuaciones de línea con `\` antes de analizar, igual que el parser real
   de Docker, así que un `RUN` de varias líneas se audita como una sola instrucción lógica. Exit
   `0` (cumple), `1` (no cumple, con línea y detalle), `2` (no se pudo verificar — el archivo no
   existe).
3. **Reportá las 11 reglas siempre**, con `[PASSED]` / `[FAILED]` / `[NO VERIFICABLE]`.
4. **Para el resto de la guía** (multi-stage, base image confiable, un proceso por contenedor,
   VOLUME para estado, labels), consultá `scripts/knowledge.json` antes de responder. Cada nodo
   trae `pile` (`A`=medible, `B`=juicio real sin umbral) y, si es `B`, un `why_not`. **No
   inventes una regla dura para lo que el nodo dice que requiere juicio** — repórtalo como
   observación cualitativa, no como `[FAILED]`.

## Reglas medibles (pila A), agrupadas

| Grupo | Reglas | Qué miden |
|---|---|---|
| Reproducibilidad | `fromlatest` | `FROM` sin tag o con `:latest` explícito |
| Capas de `apt-get` | `aptcombine`, `aptcleanup` | `update` sin `install` en el mismo `RUN`; `install` sin limpiar `/var/lib/apt/lists/*` |
| Arranque del contenedor | `execform` | `CMD`/`ENTRYPOINT` en shell form en vez de exec form |
| Privilegios | `userroot`, `sudoinstall` | `USER root` explícito; instalación o uso de `sudo` |
| Directorio de trabajo | `workdirabs`, `cdinstead` | `WORKDIR` con ruta relativa; `RUN cd ... &&` en vez de `WORKDIR` |
| Copia de archivos | `addvscopy` | `ADD` para un archivo/directorio local que no es URL ni archivo comprimido |
| Robustez del build | `pipefail` | `RUN` con pipe `|` sin `set -o pipefail` |
| Contexto de build | `dockerignore` | Ausencia de `.dockerignore` junto al Dockerfile |

## Límite declarado, sin excepciones

Heurísticas de texto sobre instrucciones Dockerfile, no un parser real del formato — tampoco
existe uno en la librería estándar de Python. `addvscopy` no reconoce todos los formatos de
archivo que Docker sabe extraer automáticamente, solo las extensiones más comunes (`.tar`,
`.tar.gz`, `.tgz`, `.tar.bz2`, `.tar.xz`, `.zip`); un caso fuera de esa lista puede marcarse como
falso positivo — revisá la línea antes de actuar.

## Reporte

| Regla | Estado | Archivo:línea | Detalle |
|---|---|---|---|
| (una fila por cada una de las 11 reglas) | [PASSED]/[FAILED]/[NO VERIFICABLE] | ... | ... |

## Recursos incluidos

- `scripts/dockerfile_checks.py` (11 reglas) — sin dependencias externas, extraídas y verificadas
  contra un Dockerfile con una violación de cada regla (11/11 `FAILED`) y un Dockerfile limpio
  (11/11 `PASSED`, cero falsos positivos).
- `scripts/knowledge.json` — las 20 reglas normativas identificadas en la fuente, triadas en pila
  A/B con su `why_not` cuando corresponde.
