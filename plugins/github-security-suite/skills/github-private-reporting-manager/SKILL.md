---
name: github-private-reporting-manager
description: Prepara reportes privados de vulnerabilidades con impacto, reproducción mínima, versiones afectadas, mitigación y divulgación responsable. Úsala sin incluir secretos ni detalles explotables innecesarios.
---

# GitHub Private Reporting Manager

Redacta el mínimo necesario para que un maintainer reproduzca y responda. No publiques la vulnerabilidad ni compartas secretos. Identifica contacto, severidad, versiones, mitigación, timeline y destinatarios; enviar el reporte requiere confirmación.

## Flujo

1. Confirma repositorio, canal privado y alcance.
2. Documenta impacto, pasos mínimos, versiones y evidencia segura.
3. Añade mitigación, contacto, deadline y divulgación prevista.
4. Revisa PII, secretos y detalles explotables antes de entregar.
5. Valida:

```bash
python plugins/github-private-reporting-manager/scripts/validate_private_report.py --input report.md --json report-check.json
```
