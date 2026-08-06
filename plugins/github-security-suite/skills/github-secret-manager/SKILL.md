---
name: github-secret-manager
description: Audita secretos de GitHub a nivel de repositorio, organización y entorno sin leer ni exponer valores. Úsala para inventariar scopes, referencias, permisos, rotación y riesgos antes de aplicar cambios con gh CLI.
---

# GitHub Secret Manager

Analiza configuración y uso de secretos, no sus contenidos. Ejecuta primero consultas de solo lectura con `gh`, redacta valores sensibles y solicita confirmación explícita antes de crear, eliminar, renombrar o rotar secretos.

## Flujo

1. Identifica repositorio, organización, entorno y alcance solicitado.
2. Inspecciona nombres, referencias de workflows, scopes y permisos; nunca imprimas valores.
3. Separa hallazgos confirmados de inferencias y registra propietario, impacto y fecha.
4. Propón rotación o limpieza como plan revisable. No ejecutes mutaciones sin confirmación.
5. Valida el informe con:

```bash
python plugins/github-security-suite/skills/github-secret-manager/scripts/validate_secret_audit.py --input audit.md --json audit-report.json
```

## Seguridad

No incluyas tokens, contraseñas, claves API ni valores cifrados en salidas, logs o commits. Si aparece un valor, detén la exposición, redacta el resultado y recomienda revocación según el procedimiento del propietario.
