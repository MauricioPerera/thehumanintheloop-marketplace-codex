---
name: k8s-manifest-auditor
description: Audita manifiestos Kubernetes (Pod, Deployment, DaemonSet, etc.) contra los Pod Security Standards oficiales (Baseline y Restricted) sin aplicarlos ni modificar el cluster. Úsala para revisar YAML antes de un `kubectl apply` o dentro de un pipeline de CI.
---

# K8s Manifest Auditor

Audita un manifiesto YAML de Kubernetes contra los [Pod Security Standards](https://kubernetes.io/docs/concepts/security/pod-security-standards/) oficiales (perfiles Baseline y Restricted). Nunca ejecuta `kubectl apply`, `kubectl edit` ni ninguna operación contra un cluster real — solo lee el archivo que se le indique.

## Procedimiento

1. Confirma qué manifiesto auditar y contra qué perfil (`Baseline`, el mínimo, o `Restricted`, el más estricto — Restricted incluye todos los controles de Baseline más los suyos propios).
2. Corré las 11 reglas deterministas contra ese archivo:

   ```bash
   python plugins/k8s-manifest-auditor/skills/k8s-manifest-auditor/scripts/k8s_checks.py --rule hostnetwork <manifiesto.yaml> [...]
   python plugins/k8s-manifest-auditor/skills/k8s-manifest-auditor/scripts/k8s_checks.py --rule hostpid <manifiesto.yaml> [...]
   python plugins/k8s-manifest-auditor/skills/k8s-manifest-auditor/scripts/k8s_checks.py --rule hostipc <manifiesto.yaml> [...]
   python plugins/k8s-manifest-auditor/skills/k8s-manifest-auditor/scripts/k8s_checks.py --rule privileged <manifiesto.yaml> [...]
   python plugins/k8s-manifest-auditor/skills/k8s-manifest-auditor/scripts/k8s_checks.py --rule capsadd <manifiesto.yaml> [...]
   python plugins/k8s-manifest-auditor/skills/k8s-manifest-auditor/scripts/k8s_checks.py --rule hostpath <manifiesto.yaml> [...]
   python plugins/k8s-manifest-auditor/skills/k8s-manifest-auditor/scripts/k8s_checks.py --rule hostport <manifiesto.yaml> [...]
   python plugins/k8s-manifest-auditor/skills/k8s-manifest-auditor/scripts/k8s_checks.py --rule privesc <manifiesto.yaml> [...]
   python plugins/k8s-manifest-auditor/skills/k8s-manifest-auditor/scripts/k8s_checks.py --rule nonroot <manifiesto.yaml> [...]
   python plugins/k8s-manifest-auditor/skills/k8s-manifest-auditor/scripts/k8s_checks.py --rule seccomp <manifiesto.yaml> [...]
   python plugins/k8s-manifest-auditor/skills/k8s-manifest-auditor/scripts/k8s_checks.py --rule capsdropall <manifiesto.yaml> [...]
   ```

   Las primeras 7 (`hostnetwork`, `hostpid`, `hostipc`, `privileged`, `capsadd`, `hostpath`, `hostport`) son controles **Baseline**: el campo debe estar ausente o en su valor seguro. Las últimas 4 (`privesc`, `nonroot`, `seccomp`, `capsdropall`) son controles **Restricted**: el campo debe estar presente y en el valor exigido — auditalas solo si el usuario pidió el perfil Restricted, no como default silencioso sobre un manifiesto que solo apunta a Baseline.

   Exit `0` (cumple), `1` (no cumple, con línea y detalle), `2` (no se pudo verificar — el archivo no existe o no es `.yaml`/`.yml`).
3. **Reportá siempre las 7 de Baseline**; agregá las 4 de Restricted solo cuando el perfil objetivo lo pida. Usá `[PASSED]` / `[FAILED]` / `[NO VERIFICABLE]`.
4. Para hallazgos que no son controles de estos 11 (imagen sin tag fijo, ausencia de `resources.limits`, RBAC del ServiceAccount asociado, NetworkPolicy faltante), repórtalos como observación cualitativa aparte — no son parte de los Pod Security Standards y no tienen checker determinista acá.
5. No apliques ni sugieras aplicar el manifiesto. Cualquier remediación se entrega como diff propuesto con el campo exacto a cambiar, nunca como un `kubectl apply` ejecutado.

## Fuera de alcance, declarado

La tabla oficial tiene más controles que los 11 de arriba: HostProcess (solo Windows), AppArmor, SELinux, `procMount`, Sysctls, el host de Host Probes/Lifecycle Hooks, y Volume Types (Restricted). Cada uno exige leer una lista de valores permitidos más larga o contexto de plataforma que un heurístico de texto no puede aplicar con la misma confianza. No los simules como cubiertos.

## Límite declarado, sin excepciones

Python no trae un parser YAML en su librería estándar y este repositorio no suma dependencias externas por plugin: esto **no es un parser YAML real**, es un escaneo de texto sobre los nombres de campo exactos de la tabla oficial (únicos dentro de un manifiesto de Pod/Deployment y sin otro significado legítimo), más un extractor liviano de listas `add:`/`drop:` por indentación. No distingue manifiestos con múltiples documentos (`---`) recurso por recurso — reporta sobre el archivo completo. Por eso cada hit imprime la línea exacta para que la revises antes de actuar.

## Reporte

| Regla | Perfil | Estado | Archivo:línea | Detalle |
|---|---|---|---|---|
| (una fila por cada regla auditada) | Baseline/Restricted | [PASSED]/[FAILED]/[NO VERIFICABLE] | ... | ... |

## Recursos incluidos

- `scripts/k8s_checks.py` (11 reglas) — sin dependencias externas, extraídas de la tabla oficial de Pod Security Standards y verificadas contra manifiestos de prueba con una violación de cada regla (11/11 `FAILED`) y un manifiesto Restricted-compliant (11/11 `PASSED`).
