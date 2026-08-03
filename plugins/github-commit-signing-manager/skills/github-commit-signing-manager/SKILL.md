---
name: github-commit-signing-manager
description: Audita firmas verificadas, autores, claves y políticas de commits de GitHub. Úsala para evaluar cobertura de firma y preparar mejoras sin alterar claves ni configuración automáticamente.
---

# GitHub Commit Signing Manager

Revisa commits y estados de verificación con `gh`. No expongas material privado de claves; separa commits observados, cobertura incompleta y recomendaciones. Cambiar políticas o claves requiere aprobación explícita.

## Flujo

1. Define repositorio, ramas y ventana de commits.
2. Comprueba estados de firma, autoría, método y excepciones.
3. Detecta commits no verificados, cambios de identidad y cobertura insuficiente.
4. Propón política con owner, impacto, validación y rollback.
5. Valida:

```bash
python plugins/github-commit-signing-manager/scripts/validate_signing_audit.py --input signing.md --json signing-report.json
```
