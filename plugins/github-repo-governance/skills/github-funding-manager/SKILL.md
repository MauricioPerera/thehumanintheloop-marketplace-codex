---
name: github-funding-manager
description: Audita FUNDING.yml, enlaces de sponsor y documentación de financiación del repositorio. Úsala para mantener información pública consistente sin procesar pagos ni exponer credenciales.
---

# GitHub Funding Manager

Revisa configuración pública y enlaces; nunca maneja pagos, claves ni datos financieros. Presenta cambios de FUNDING.yml o README como diff y solicita confirmación antes de escribir.

## Flujo

1. Define repositorio, proveedores y enlaces autorizados.
2. Comprueba FUNDING.yml, README, sitio y consistencia de nombres.
3. Detecta enlaces rotos, proveedores no autorizados y afirmaciones ambiguas.
4. Propón corrección con owner, validación y evidencia.
5. Valida:

```bash
python plugins/github-funding-manager/scripts/validate_funding_audit.py --input funding.md --json funding-report.json
```
