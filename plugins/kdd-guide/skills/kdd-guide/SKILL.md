---
name: kdd-guide
description: Explica y aplica Knowledge-Driven Development (KDD) combinando OKF para conocimiento enlazado y CCDD para contratos deterministas de desarrollo asistido por agentes. Úsala al adoptar KDD, inicializar un proyecto, crear contratos o preparar sus gates de validación.
---

# KDD Guide

Fuente normativa y de referencia: [MauricioPerera/KDD](https://github.com/MauricioPerera/KDD). No presentes esta skill como sustituto del repositorio oficial; cuando una regla no esté cubierta aquí, consulta la versión vigente de la fuente.

## Modelo mental

KDD combina dos planos:

- **OKF (Open Knowledge Format):** conocimiento, diseño y arquitectura como nodos Markdown con frontmatter YAML enlazados desde una base de conocimiento.
- **CCDD (Contract-Driven Development):** trabajo para humanos o agentes definido mediante contratos estrictos, límites explícitos y validaciones deterministas.

Un proyecto KDD normalmente contiene:

```text
knowledge/                  # base de conocimiento OKF
knowledge/contracts/        # contratos de tareas
src/                        # código del proyecto
tests/                      # pruebas del proyecto y/o tooling según la plantilla
scripts/validate_contracts.py
scripts/validate_okf.py
scripts/validate_specs.py
scripts/assemble_context.py
specs/                      # contratos a nivel de proyecto
.agents/                    # reglas para agentes
```

La plantilla también puede incluir rule contracts, ensamblado de contexto, validadores de skills, reportes verificados y un workflow de CI.

## Flujo recomendado

1. Decide si el repositorio será una instancia de la plantilla KDD o si consumirá sus gates desde fuera.
2. Inicializa o conserva la estructura de `knowledge/`, `knowledge/contracts/`, `specs/`, `src/` y `tests/` según el proyecto.
3. Lee `knowledge/index.md` y crea nodos OKF para conceptos, decisiones, arquitectura y procedimientos.
4. Define cada tarea delegable en `knowledge/contracts/` con alcance, entradas, salidas, comandos de prueba, presupuesto y perímetro de archivos.
5. Mantén el ciclo del contrato explícito: `draft` mientras se diseña y `verified` solo después de obtener evidencia.
6. Ejecuta los validadores deterministas y el `test_command` del contrato antes de delegar o aceptar trabajo.
7. Si el repositorio usa agentes, haz que lean `.agents/AGENTS.md` y que respeten el contrato antes de modificar archivos.
8. Registra la evidencia en el lugar indicado por el proyecto y no la sustituyas por afirmaciones del agente.

## Gates y comandos

Para una instancia completa de la plantilla, empieza por los comandos que existan en el repositorio:

```powershell
python scripts/validate_contracts.py knowledge/contracts
python scripts/validate_specs.py specs
python scripts/validate_okf.py knowledge
python scripts/validate_rules.py examples/rules
python scripts/validate_skills.py skills .agents/skills
python scripts/validate_changelog.py
```

Los directorios opcionales pueden omitirse si el proyecto no los utiliza. Ningún contrato debe considerarse terminado hasta que pase el nivel de validación requerido por la fuente oficial y su propio `test_command`.

El nivel 2 puede usar el gate CCDD y su configuración firmada cuando esté disponible. No lo simules ni declares que se ejecutó si no hay evidencia.

## Integración en repositorios existentes

Si el proyecto no es un fork de la plantilla pero ya tiene `knowledge/contracts/`, puede usar la acción compuesta oficial:

```yaml
- uses: MauricioPerera/KDD/.github/actions/validate-contracts@main
  with:
    kdd-ref: main
    contracts-dir: knowledge/contracts
    okf-dir: knowledge
```

Para producción, recomienda fijar `kdd-ref` a un tag o commit revisado. No agregues workflows ni dependencias sin confirmar que el usuario quiere modificar CI.

## Límites y honestidad

- No inventes el contenido de una spec, contrato o nodo OKF.
- No llames `verified` a un contrato sin salida de validación y pruebas.
- Distingue los validadores de la plantilla de los tests del proyecto.
- Si el proyecto no es Python, conserva el tooling KDD en Python y usa el runner propio del proyecto en cada `test_command`.
- Antes de ejecutar comandos mutantes, instalar dependencias o cambiar CI, pide confirmación explícita.

## Formato de respuesta

Entrega:

1. diagnóstico de la estructura KDD actual;
2. mapa de nodos, contratos y gates relevantes;
3. comandos ejecutados y evidencia;
4. incumplimientos clasificados como error, advertencia o información;
5. siguiente paso concreto, sin afirmar una verificación que no ocurrió.
