---
name: github-code-scanning-manager
description: Audita alertas de Code Scanning, severidad, reglas, ubicaciones y remediaciones. Úsala para priorizar hallazgos sin cerrar alertas ni modificar workflows automáticamente.
---

# GitHub Code Scanning Manager

Consulta alertas con `gh` en modo lectura. Conserva regla, ubicación, severidad, estado y evidencia; distingue falso positivo de vulnerabilidad no confirmada. Cerrar alertas o editar análisis requiere confirmación explícita.

## Flujo

1. Define repositorio, rama, herramienta y ventana.
2. Agrupa alertas por severidad, regla, archivo y estado.
3. Identifica propietarios, impacto, duplicados y falsos positivos.
4. Propón remediación, validación y seguimiento.
5. Valida:

```bash
python plugins/github-security-suite/skills/github-code-scanning-manager/scripts/validate_code_scan_report.py --input scan.md --json scan-report.json
```
