---
name: github-audit-log-manager
description: Analiza el audit log de GitHub con filtros temporales, actores, acciones y repositorios. Úsala para investigaciones administrativas y reportes de seguridad con evidencia y datos sensibles redactados.
---

# GitHub Audit Log Manager

Consulta eventos administrativos en modo lectura con `gh` o `gh api`. Define siempre organización, ventana temporal, actores y acciones; no presentes datos sensibles sin redactar. Las conclusiones deben distinguir eventos observados de hipótesis.

## Flujo

1. Captura el alcance, zona horaria y motivo de la investigación.
2. Filtra eventos por actor, acción, repositorio, IP o recurso solo cuando sea necesario.
3. Conserva identificadores, timestamps y URLs como evidencia; minimiza PII.
4. Resume anomalías, impacto, owner y siguiente paso sin ejecutar remediaciones automáticamente.
5. Valida el informe:

```bash
python plugins/github-collab-activity/skills/github-audit-log-manager/scripts/validate_audit_log_report.py --input audit.md --json audit-report.json
```
