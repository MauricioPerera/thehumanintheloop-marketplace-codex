---
name: github-runner-manager
description: Audita runners hospedados y self-hosted de GitHub Actions, sus labels, grupos, alcance, estado y controles de aislamiento. Úsala antes de registrar, retirar o cambiar runners.
---

# GitHub Runner Manager

Inspecciona runners y permisos sin ejecutar cambios. Trata un runner self-hosted como infraestructura sensible: revisa repositorios autorizados, labels, software, conectividad y separación de cargas antes de proponer mutaciones.

## Flujo

1. Define organización, repositorio, runner group y entorno objetivo.
2. Lista estado, labels, versión, último contacto, alcance y workflows consumidores.
3. Detecta runners offline, labels peligrosos, falta de aislamiento y permisos excesivos.
4. Prepara plan con impacto, owner, ventana de mantenimiento y rollback.
5. Valida el plan:

```bash
python plugins/github-runner-manager/scripts/validate_runner_plan.py --input runners.md --json runners-report.json
```

No registres ni elimines runners, ni cambies grupos, sin mostrar el cambio y recibir confirmación explícita.
