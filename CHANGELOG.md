# Changelog

## Unreleased

- Tabla de migración para los 43 plugins `github-*` consolidados en 6 plugins multi-skill: ver [`README.md#migración-de-plugins-github-consolidados`](README.md#migración-de-plugins-github-consolidados).
- Consolidacion de 43 plugins `github-*` de superficie unica en 6 plugins multi-skill (misma cobertura, menos entradas instalables).
- `github-security-suite` (GitHub Security Suite): consolida 8 plugins GitHub anteriores en un plugin multi-skill (github-security-manager, github-code-scanning-manager, github-secret-scanning-manager, github-security-advisory-manager, github-dependency-review-manager, github-dependabot-manager, github-private-reporting-manager, github-secret-manager).
- `github-cicd-governance` (GitHub CI/CD Governance): consolida 8 plugins GitHub anteriores en un plugin multi-skill (github-action-permissions-manager, github-checks-manager, github-environment-manager, github-merge-queue-manager, github-oidc-manager, github-runner-manager, github-variable-manager, github-workflow-dispatch-manager).
- `github-repo-governance` (GitHub Repository Governance): consolida 8 plugins GitHub anteriores en un plugin multi-skill (github-repository-manager, github-codeowners-manager, github-template-manager, github-label-manager, github-milestone-manager, github-funding-manager, github-pages-manager, github-ruleset-manager).
- `github-collab-activity` (GitHub Collaboration & Activity): consolida 7 plugins GitHub anteriores en un plugin multi-skill (github-discussion-manager, github-notifications-manager, github-contributor-manager, github-team-manager, github-activity-manager, github-traffic-manager, github-audit-log-manager).
- `github-branch-release-ops` (GitHub Branch & Release Ops): consolida 5 plugins GitHub anteriores en un plugin multi-skill (github-branch-manager, github-commit-signing-manager, github-deployment-manager, github-merge-conflict-manager, github-package-manager).
- `github-org-lifecycle` (GitHub Org & Lifecycle): consolida 7 plugins GitHub anteriores en un plugin multi-skill (github-organization-settings-manager, github-archive-manager, github-migration-manager, github-fork-manager, github-webhook-manager, github-api-manager, github-project-manager).

- Documentación de contribución para plugins y Design System Analyses.
- Validación automática de metadata SEO, JSON-LD y sitemap para previews.
- `cv-job-tailor`: adaptación de CVs a ofertas con trazabilidad y validadores anti-fabricación.
- `commercial-proposal-builder`: propuestas comerciales basadas en requerimientos con control de alcance, precios y supuestos.
- `rfp-response-builder`: respuestas de RFP y licitaciones con matriz de cumplimiento, evidencia y pendientes.
- `github-issue-manager`: gestión de Issues con `gh` CLI y confirmación antes de acciones mutables.
- `github-pr-manager`: preparación y revisión de Pull Requests con checklist y evidencia.
- `github-release-manager`: preparación de releases, tags y notas de versión con `gh` CLI.
- `github-actions-manager`: diagnóstico de workflows, ejecuciones y logs de GitHub Actions.
- `github-project-manager`: organización de Projects y tareas con plan de mutaciones trazable.
- `github-code-search`: búsqueda reproducible de código, commits, Issues y Pull Requests.
- `github-security-manager`: auditoría de alertas de seguridad y planes de remediación.
- `github-dependabot-manager`: revisión de alertas y actualizaciones Dependabot.
- `github-notifications-manager`: digest y triage de notificaciones de GitHub.
- `github-discussion-manager`: gestión de Discussions con respuestas trazables.
- `github-label-manager`: taxonomía y mantenimiento de labels con plan previo.
- `github-repository-manager`: inspección y configuración de repositorios con confirmación.
- `github-milestone-manager`: planificación de hitos con objetivos, fechas y trazabilidad.
- `github-branch-manager`: gestión segura de ramas y operaciones remotas.
- `github-template-manager`: validación y mantenimiento de templates de Issues y PRs.
- `github-api-manager`: consultas GitHub API con controles GET-first y evidencia estructurada.
- `github-codeowners-manager`: validación de CODEOWNERS, ownership y cobertura.
- `github-contributor-manager`: análisis de contribuciones y planes de reviewers.
- `github-activity-manager`: reportes temporales de actividad con evidencia y límites.
- `github-traffic-manager`: análisis de tráfico de repositorios con retención y agregación explícitas.
- `github-webhook-manager`: planes y auditoría de webhooks con secretos redactados.
- `github-environment-manager`: auditoría y planes de environments y gates de despliegue.
- `github-variable-manager`: auditoría de variables sin lectura de valores secretos.
- `github-package-manager`: revisión de paquetes, versiones y planes de retención.
- `github-secret-manager`: auditoría de secretos con valores redactados y planes de rotación.
- `github-ruleset-manager`: auditoría y diseño de reglasets con bypass, checks y rollback.
- `github-checks-manager`: análisis de checks, annotations y resultados de CI con evidencia.
- `github-audit-log-manager`: análisis de actividad administrativa con filtros y datos redactados.
- `github-runner-manager`: auditoría de runners, labels, alcance y aislamiento.
- `github-deployment-manager`: análisis operativo de despliegues y planes de rollback.
- `github-team-manager`: auditoría de equipos, membresías y permisos efectivos.
- `github-merge-queue-manager`: diagnóstico de merge queues, checks y cuellos de botella.
- `github-fork-manager`: auditoría de forks, sincronización y políticas de visibilidad.
- `github-commit-signing-manager`: auditoría de firmas, estados verificados y cobertura.
- `github-migration-manager`: planes de migración con inventario, validación y rollback.
- `github-archive-manager`: evaluación de archivado, retención y recuperación.
- `github-code-scanning-manager`: auditoría de alertas, severidad, reglas y remediación.
- `github-secret-scanning-manager`: análisis seguro de alertas con valores siempre redactados.
- `github-security-advisory-manager`: borradores de advisories con mitigación y divulgación responsable.
- `github-dependency-review-manager`: revisión de dependencias nuevas, licencias y supply chain.
- `github-private-reporting-manager`: reportes privados con evidencia mínima y segura.
- `github-organization-settings-manager`: auditoría de políticas globales y permisos de organización.
- `github-pages-manager`: auditoría de fuentes, dominios y despliegues de GitHub Pages.
- `github-funding-manager`: revisión de FUNDING.yml, sponsors y enlaces públicos.
- `github-workflow-dispatch-manager`: preparación segura de ejecuciones manuales con inputs.
- `github-oidc-manager`: auditoría de subjects, audiences y trust de proveedores cloud.
- `github-action-permissions-manager`: revisión de scopes y mínimo privilegio de GITHUB_TOKEN.
- `github-merge-conflict-manager`: diagnóstico de conflictos y planes de resolución revisables.
- `mercadopago-payment-manager`: contrato y validador para enlaces Checkout Preference con confirmación previa.

## 2026-08-02

- Marketplace dual para Claude Code y Codex.
- Catálogo público con 16 plugins y ocho categorías.
- GitHub Page navegable con búsqueda, filtros, instalación y previews embebidos.
- Publicación de análisis KDD, Mercado Libre y TheHumanInTheLoop Marketplace.
- Licencia MIT.
