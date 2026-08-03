---
name: github-security-advisory-manager
description: Prepara security advisories con vulnerabilidad, versiones afectadas, severidad, CVE, mitigación y divulgación responsable. Úsala antes de publicar o actualizar un advisory.
---

# GitHub Security Advisory Manager

Construye el advisory a partir de evidencia confirmada. No publiques CVE, detalles explotables, créditos ni fechas sin revisar responsables y política de divulgación. Cualquier publicación o actualización requiere confirmación.

## Flujo

1. Define paquete, versiones afectadas, corregidas y ecosistema.
2. Documenta impacto, severidad, vector, mitigación y referencias.
3. Revisa créditos, timeline, destinatarios y estado de divulgación.
4. Prepara borrador, validación y plan de comunicación.
5. Valida:

```bash
python plugins/github-security-advisory-manager/scripts/validate_advisory.py --input advisory.md --json advisory-report.json
```
