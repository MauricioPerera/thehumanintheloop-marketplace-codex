---
name: github-oidc-manager
description: "Audita confianza OIDC de GitHub Actions: subjects, audiences, proveedores cloud, repositorios y workflows. Úsala para revisar federación sin exponer tokens ni cambiar trusts automáticamente."
---

# GitHub OIDC Manager

Inspecciona workflows y configuración cloud en modo lectura. Compara claims esperados con trusts configurados y redacta tokens, IDs sensibles y credenciales. Cambiar permisos cloud requiere confirmación del propietario.

## Flujo

1. Define repositorio, proveedor, audiencia y entorno.
2. Lista subjects, workflows, ramas, tags y repositorios autorizados.
3. Detecta comodines excesivos, audiencias incorrectas y trusts huérfanos.
4. Propón mínimo privilegio, owner, impacto, validación y rollback.
5. Valida:

```bash
python plugins/github-oidc-manager/scripts/validate_oidc_audit.py --input oidc.md --json oidc-report.json
```
