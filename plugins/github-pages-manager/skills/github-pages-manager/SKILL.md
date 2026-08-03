---
name: github-pages-manager
description: Audita fuente, rama, workflow, dominio y estado de GitHub Pages. Úsala para preparar despliegues, diagnosticar fallos y validar publicación sin mutar automáticamente.
---

# GitHub Pages Manager

Inspecciona Pages y workflows con `gh` en modo lectura. Revisa fuente, branch, artefacto, dominio, permisos y último despliegue. Publicar o cambiar configuración requiere previsualización, confirmación y rollback.

## Flujo

1. Define repositorio, URL, fuente y rama esperada.
2. Relaciona workflow, artefacto, commit, estado y error.
3. Verifica enlaces, dominio, headers y contenido publicado.
4. Propón despliegue con smoke tests, owner e impacto.
5. Valida:

```bash
python plugins/github-pages-manager/scripts/validate_pages_plan.py --input pages.md --json pages-report.json
```
