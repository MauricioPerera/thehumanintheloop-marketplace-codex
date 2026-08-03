---
name: github-secret-scanning-manager
description: Analiza alertas de Secret Scanning sin revelar tokens, claves ni valores. Úsala para priorizar exposición, revocación, rotación y seguimiento seguro.
---

# GitHub Secret Scanning Manager

Los valores nunca se imprimen ni se copian a informes. Revisa proveedor, ubicación, estado, commit y owner; recomienda revocar o rotar mediante el canal oficial y solicita confirmación antes de mutar.

## Flujo

1. Define repositorio, alerta y alcance.
2. Registra solo metadatos redactados, proveedor, ubicación y estado.
3. Prioriza exposición, consumidores, revocación y rotación.
4. Documenta impacto, owner, verificación y comunicación.
5. Valida:

```bash
python plugins/github-secret-scanning-manager/scripts/validate_secret_scan_report.py --input secrets.md --json secrets-report.json
```
