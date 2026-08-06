# TheHumanInTheLoop Marketplace

Marketplace público de plugins, skills y Design System Analyses para Claude Code y Codex, creado por Mauricio Perera.

Catálogo actual: **83 plugins y 19 Design System Analyses**, distribuido en dos manifests compatibles y una [GitHub Page navegable](https://mauricioperera.github.io/thehumanintheloop-marketplace-codex/). También puedes conocer el proyecto en el [canal The Human in the Loop](https://www.youtube.com/@Rckflr).

## Plugins disponibles

- `Auditor SEO/GEO 2026` (`linter-seo-geo-2026`): validador de contenido para buscadores y motores generativos.
- `Marketplace Validator` (`marketplace-validator`): valida manifests y sincronización Claude Code/Codex.
- `AI Prompt Workflow` (`ai-prompt-workflow`): diseña prompts evaluables y reutilizables.
- `UX Accessibility Guide` (`ux-accessibility-guide`): audita UX y accesibilidad con evidencia.
- `Research Methods Guide` (`research-methods-guide`): estructura investigaciones con fuentes y evidencia trazable.
- `Plugin Authoring` (`plugin-authoring`): crea y valida plugins para este marketplace.
- `KDD Guide` (`kdd-guide`): explica y aplica Knowledge-Driven Development con OKF y CCDD.
- `Design System Auditor` (`design-system-auditor`): genera contratos `DESIGN.md`, tokens y validadores.
- `Design System Governance` (`design-system-governance`): mantiene contratos de diseño y detecta drift entre diseño, código y documentación.
- `Content Fact Checker` (`content-fact-checker`): exige fuentes, fechas y evidencia para afirmaciones.
- `Repo Quality Gate` (`repo-quality-gate`): revisa repositorios antes de commit, PR o release.
- `Technical Docs Linter` (`technical-docs-linter`): valida documentación, ejemplos, comandos y enlaces.
- `Accessibility Auditor` (`accessibility-auditor`): audita HTML, ARIA, formularios y teclado.
- `Privacy Risk Auditor` (`privacy-risk-auditor`): detecta PII, secretos y credenciales.
- `Release Readiness` (`release-readiness`): valida si el repositorio está listo para publicar.
- `Prompt Contract Linter` (`prompt-contract-linter`): valida prompts como contratos ejecutables.
- `Research Evidence Builder` (`research-evidence-builder`): construye matrices de evidencia.
- `Brand Voice Validator` (`brand-voice-validator`): valida tono y consistencia editorial.
- `API Contract Linter` (`api-contract-linter`): audita contratos OpenAPI y ejemplos.
- `Web Performance Auditor` (`web-performance-auditor`): audita carga y Core Web Vitals.
- `Dependency Risk Auditor` (`dependency-risk-auditor`): revisa dependencias y lockfiles.
- `Test Coverage Gate` (`test-coverage-gate`): valida evidencia de tests y cobertura.
- `CV Job Tailor` (`cv-job-tailor`): adapta CVs a ofertas laborales con trazabilidad y controles anti-fabricación.
- `Commercial Proposal Builder` (`commercial-proposal-builder`): redacta propuestas comerciales basadas en requerimientos con integridad de alcance y precios.
- `RFP Response Builder` (`rfp-response-builder`): responde RFPs y licitaciones con matriz de cumplimiento y evidencia.
- `GitHub Issue Manager` (`github-issue-manager`): gestiona Issues con `gh` CLI, triage y confirmación antes de mutar.
- `GitHub PR Manager` (`github-pr-manager`): prepara y revisa Pull Requests con checklist y evidencia.
- `GitHub Release Manager` (`github-release-manager`): prepara releases, tags y notas de versión con `gh` CLI.
- `GitHub Actions Manager` (`github-actions-manager`): inspecciona ejecuciones, jobs y logs de CI.
- `GitHub Security Suite` (`github-security-suite`): audita seguridad de GitHub: code/secret scanning, advisories, dependencias, Dependabot, reportes privados y secretos, con planes de remediación.
- `GitHub CI/CD Governance` (`github-cicd-governance`): audita la gobernanza de CI/CD en GitHub Actions: permisos, environments, checks, merge queue, runners, OIDC, variables y despliegues manuales.
- `GitHub Repository Governance` (`github-repo-governance`): audita y prepara configuración de repositorios GitHub: settings, CODEOWNERS, templates, labels, milestones, funding, Pages y rulesets de protección.
- `GitHub Collaboration & Activity` (`github-collab-activity`): resume actividad y colaboración en GitHub: Discussions, notificaciones, contribuidores, equipos, actividad temporal, tráfico y audit log administrativo.
- `GitHub Branch & Release Ops` (`github-branch-release-ops`): opera el ciclo de vida de ramas y despliegues en GitHub: ramas, firma de commits, despliegues, conflictos de merge y paquetes.
- `GitHub Org & Lifecycle` (`github-org-lifecycle`): audita configuración organizacional y ciclo de vida de repositorios en GitHub: settings de organización, archivado, migraciones, forks, webhooks, API y Projects.
- `GitHub Code Search` (`github-code-search`): busca código, commits y referencias reproducibles.
- `Mercado Pago Payment Manager` (`mercadopago-payment-manager`): prepara enlaces de pago con validadores de seguridad.
- `Supabase Self-hosted Observer` (`supabase-selfhosted-observer`): observa contenedores, healthchecks, versiones y recursos de Supabase por SSH.
- `Supabase Database Manager` (`supabase-database-manager`): diagnostica PostgreSQL y clasifica consultas antes de mutar.
- `Supabase Service Manager` (`supabase-service-manager`): opera servicios Docker Compose con rollback y confirmación.
- `Supabase Config Auditor` (`supabase-config-auditor`): audita configuración, puertos y variables sin revelar secretos.
- `Supabase Backup Manager` (`supabase-backup-manager`): planifica backups y restores con retención y verificación.
- `Supabase Upgrade Manager` (`supabase-upgrade-manager`): evalúa upgrades con compatibilidad, backup y rollback.
- `Supabase Policy Security Auditor` (`supabase-policy-security-auditor`): audita RLS, Storage, Auth/JWT y Edge Functions en modo lectura.
- `Docker VPS Observer` (`docker-vps-observer`): observa daemon, contenedores, salud, recursos y puertos Docker por SSH.
- `Docker Service Manager` (`docker-service-manager`): planifica cambios Docker Compose con confirmación y rollback.
- `Docker Image Manager` (`docker-image-manager`): audita imágenes, digests y espacio recuperable antes de limpiar.
- `Docker Storage Auditor` (`docker-storage-auditor`): audita volúmenes, redes, mounts y exposición sin leer secretos.
- `Docker Log Diagnostics` (`docker-log-diagnostics`): correlaciona logs, eventos y healthchecks para investigar incidentes.
- `VPS Backup Suite` (`vps-backup-suite`): planifica, monitorea y verifica backups de un VPS: jobs programados, planes de backup con restauración comprobable y verificación de integridad de restores, sin ejecutar cambios.
- `VPS Container Security Suite` (`vps-container-security-suite`): audita seguridad de contenedores Docker en un VPS: postura general, aislamiento de red, límites de recursos, procedencia de imágenes y CVE/SBOM, en modo lectura.
- `VPS Network Exposure Suite` (`vps-network-exposure-suite`): audita la superficie de red expuesta de un VPS: DNS y autenticación de correo (SPF, DKIM, DMARC), diagnóstico de conectividad, exposición de servicios y renovación de certificados TLS.
- `VPS Observability Suite` (`vps-observability-suite`): audita capacidad, métricas, logs y retención de un VPS: CPU, RAM, disco, sobredimensionamiento, healthchecks/alertas y crecimiento de logs, sin instalar agentes.
- `VPS Deployment Readiness Suite` (`vps-deployment-readiness-suite`): audita preparación de despliegues en un VPS: drift entre configuración declarada y estado activo, preparación de Docker Compose y mapa de dependencias y blast radius.
- `VPS Incident & Security Suite` (`vps-incident-security-suite`): audita seguridad de un VPS (firewall, SSH, fail2ban, actualizaciones) e investiga incidentes correlacionando procesos, conexiones, Docker, disco y memoria, sin aplicar cambios.
- `TLS Domain Manager` (`tls-domain-manager`): audita certificados, dominios, SNI y redirecciones HTTPS.
- `Firewall Policy Manager` (`firewall-policy-manager`): audita UFW, iptables y nftables sin modificar reglas.
- `System Update Planner` (`system-update-planner`): prepara actualizaciones de paquetes y kernel con rollback.
- `Cron Automation Auditor` (`cron-automation-auditor`): audita cron y systemd timers sin ejecutar tareas.
- `Secrets Exposure Auditor` (`secrets-exposure-auditor`): detecta indicios de secretos sin revelar valores.
- `Nginx Reverse Proxy Manager` (`nginx-reverse-proxy-manager`): audita hosts, upstreams, headers y rutas públicas.
- `Database Operations Manager` (`database-operations-manager`): diagnostica PostgreSQL, MySQL y Redis con guardas.
- `Supabase Migration Drift Auditor` (`supabase-migration-drift-auditor`): audita migraciones aplicadas vs archivos en disco vs catálogos PostgreSQL para detectar drift de schema en modo lectura.
- `Supabase pg_cron Auditor` (`supabase-pgcron-auditor`): audita jobs pg_cron de Supabase self-hosted en modo lectura listando cron.job y cron.job_run_details, detectando jobs fallidos, pausados, duplicados, frecuencias peligrosas y comandos que expongan secretos o muten fuera de alcance.
- `Terraform Plan Auditor` (`terraform-plan-auditor`): audita el output de `terraform plan` antes de aplicarlo: cambios destructivos, recursos con estado, permisos amplios y exposición pública, sin ejecutar apply, destroy ni modificar el state.
- `KDD TypeScript Checker` (`kdd-typescript`): verifica 17 reglas duras del Google TypeScript Style Guide: var/const/let, exports, imports, campos privados, const enum, wrapper types, comillas, triple igual y nombres con guion bajo, extraidas y verificadas con Knowledge-Driven Development.

## Categorías

El catálogo usa una taxonomía común en Claude Code, Codex y la GitHub Page:

- Content & Editorial — 7 plugins
- Design Systems — 2 plugins
- Marketplace & Quality — 7 plugins
- Developer Tools — 43 plugins
- Accessibility & UX — 3 plugins
- Security & Privacy — 17 plugins
- Research & Evidence — 2 plugins
- AI & Prompt Engineering — 2 plugins

Además, la categoría Design Systems contiene **17 análisis publicados**; se listan y enlazan en la sección [Design System Analyses publicados](#design-system-analyses-publicados).

La GitHub Page permite filtrar por categoría, buscar por nombre o capacidad, copiar instrucciones de instalación y abrir el código fuente de cada plugin.

## Estructura

- `.claude-plugin/marketplace.json`: catálogo compatible con Claude Code.
- `.agents/plugins/marketplace.json`: catálogo compatible con Codex.
- `plugins/`: un directorio por plugin.
- Cada plugin puede contener `.claude-plugin/plugin.json` y `.codex-plugin/plugin.json`; ambos reutilizan las mismas skills bajo `skills/`.
- `docs/analyses/`: resultados publicados de análisis visuales; cada entrada contiene `DESIGN.md`, `design-system.json`, `validation-report.json` y un preview navegable.
- `CONTRIBUTING.md`: flujo para proponer plugins y Design System Analyses.
- `CHANGELOG.md`: historial de capacidades publicadas.
- `SECURITY.md`: alcance y procedimiento para reportar vulnerabilidades.
- `CODE_OF_CONDUCT.md`: reglas de participación de la comunidad.
- `AGENTS.md`: instrucciones operativas para agentes de IA y colaboradores automatizados.
- `.github/CODEOWNERS` y `.github/dependabot.yml`: revisión y actualizaciones automáticas de CI.

## Design System Analyses

El marketplace publica resultados, no el plugin privado que los generó. Cada análisis debe incluir:

1. `DESIGN.md` como fuente de verdad con contrato duro, contrato blando y `Validation Contract`.
2. `design-system.json` derivado del `DESIGN.md`.
3. `validation-report.json` con estado, errores y advertencias.
4. `index.html` como preview navegable enlazado desde el catálogo.

Los análisis de terceros se presentan como análisis externos, no como sistemas oficiales de sus respectivas marcas.

## Añadir un plugin

1. Crear un directorio dentro de `plugins/`.
2. Añadir los manifiestos `.claude-plugin/plugin.json` y `.codex-plugin/plugin.json` cuando el plugin deba funcionar en ambas plataformas.
3. Añadir una entrada en `.claude-plugin/marketplace.json` y `.agents/plugins/marketplace.json`.
4. Mantener las skills compartidas en `skills/` y validar ambos formatos antes de publicar cambios.

Antes de publicar, comprueba que la entrada exista en ambos manifests, que la ruta `source` apunte al directorio correcto y que la ficha visible esté actualizada en `docs/catalog.json`. El workflow [Marketplace Validation](https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex/actions/workflows/marketplace-validation.yml) ejecuta estas comprobaciones automáticamente.

## Validación local

Desde la raíz del repositorio puedes ejecutar toda la suite con:

```powershell
python scripts/validate_all.py
```

Para ejecutar los controles por separado:

```powershell
python plugins/marketplace-validator/scripts/validate_marketplace.py .
python scripts/validate_catalog_metadata.py
python scripts/validate_analysis_metadata.py
python scripts/validate_llms_catalog.py
node --check docs/app.js
git diff --check
```

No publiques un plugin si la validación devuelve `[FAILED]` o si la ficha de catálogo no coincide con los manifests.

Los workflows usan `actions/checkout@v6` y optan por Node.js 24. Si utilizas runners autoalojados, mantenlos en una versión compatible con ese runtime.

## Migración de plugins GitHub consolidados

El 6 de agosto de 2026 se consolidaron 43 plugins `github-*` de superficie única (uno por endpoint de la API de GitHub) en 6 plugins multi-skill agrupados por dominio de proceso. Si tenías instalado o referenciado alguno de estos nombres, ya no existe en el marketplace: instala el plugin nuevo de la columna derecha, que incluye la misma skill sin cambios.

| Plugin anterior | Plugin nuevo |
|---|---|
| `github-action-permissions-manager` | `github-cicd-governance` (`GitHub CI/CD Governance`) |
| `github-activity-manager` | `github-collab-activity` (`GitHub Collaboration & Activity`) |
| `github-api-manager` | `github-org-lifecycle` (`GitHub Org & Lifecycle`) |
| `github-archive-manager` | `github-org-lifecycle` (`GitHub Org & Lifecycle`) |
| `github-audit-log-manager` | `github-collab-activity` (`GitHub Collaboration & Activity`) |
| `github-branch-manager` | `github-branch-release-ops` (`GitHub Branch & Release Ops`) |
| `github-checks-manager` | `github-cicd-governance` (`GitHub CI/CD Governance`) |
| `github-code-scanning-manager` | `github-security-suite` (`GitHub Security Suite`) |
| `github-codeowners-manager` | `github-repo-governance` (`GitHub Repository Governance`) |
| `github-commit-signing-manager` | `github-branch-release-ops` (`GitHub Branch & Release Ops`) |
| `github-contributor-manager` | `github-collab-activity` (`GitHub Collaboration & Activity`) |
| `github-dependabot-manager` | `github-security-suite` (`GitHub Security Suite`) |
| `github-dependency-review-manager` | `github-security-suite` (`GitHub Security Suite`) |
| `github-deployment-manager` | `github-branch-release-ops` (`GitHub Branch & Release Ops`) |
| `github-discussion-manager` | `github-collab-activity` (`GitHub Collaboration & Activity`) |
| `github-environment-manager` | `github-cicd-governance` (`GitHub CI/CD Governance`) |
| `github-fork-manager` | `github-org-lifecycle` (`GitHub Org & Lifecycle`) |
| `github-funding-manager` | `github-repo-governance` (`GitHub Repository Governance`) |
| `github-label-manager` | `github-repo-governance` (`GitHub Repository Governance`) |
| `github-merge-conflict-manager` | `github-branch-release-ops` (`GitHub Branch & Release Ops`) |
| `github-merge-queue-manager` | `github-cicd-governance` (`GitHub CI/CD Governance`) |
| `github-migration-manager` | `github-org-lifecycle` (`GitHub Org & Lifecycle`) |
| `github-milestone-manager` | `github-repo-governance` (`GitHub Repository Governance`) |
| `github-notifications-manager` | `github-collab-activity` (`GitHub Collaboration & Activity`) |
| `github-oidc-manager` | `github-cicd-governance` (`GitHub CI/CD Governance`) |
| `github-organization-settings-manager` | `github-org-lifecycle` (`GitHub Org & Lifecycle`) |
| `github-package-manager` | `github-branch-release-ops` (`GitHub Branch & Release Ops`) |
| `github-pages-manager` | `github-repo-governance` (`GitHub Repository Governance`) |
| `github-private-reporting-manager` | `github-security-suite` (`GitHub Security Suite`) |
| `github-project-manager` | `github-org-lifecycle` (`GitHub Org & Lifecycle`) |
| `github-repository-manager` | `github-repo-governance` (`GitHub Repository Governance`) |
| `github-ruleset-manager` | `github-repo-governance` (`GitHub Repository Governance`) |
| `github-runner-manager` | `github-cicd-governance` (`GitHub CI/CD Governance`) |
| `github-secret-manager` | `github-security-suite` (`GitHub Security Suite`) |
| `github-secret-scanning-manager` | `github-security-suite` (`GitHub Security Suite`) |
| `github-security-advisory-manager` | `github-security-suite` (`GitHub Security Suite`) |
| `github-security-manager` | `github-security-suite` (`GitHub Security Suite`) |
| `github-team-manager` | `github-collab-activity` (`GitHub Collaboration & Activity`) |
| `github-template-manager` | `github-repo-governance` (`GitHub Repository Governance`) |
| `github-traffic-manager` | `github-collab-activity` (`GitHub Collaboration & Activity`) |
| `github-variable-manager` | `github-cicd-governance` (`GitHub CI/CD Governance`) |
| `github-webhook-manager` | `github-org-lifecycle` (`GitHub Org & Lifecycle`) |
| `github-workflow-dispatch-manager` | `github-cicd-governance` (`GitHub CI/CD Governance`) |

## Migración de plugins VPS consolidados

El 6 de agosto de 2026 se consolidaron 21 plugins `vps-*` de superficie única en 6 plugins multi-skill agrupados por dominio de proceso (`vps-ssh-manager` queda standalone). Si tenías instalado o referenciado alguno de estos nombres, ya no existe en el marketplace: instala el plugin nuevo de la columna derecha, que incluye la misma skill sin cambios.

| Plugin anterior | Plugin nuevo |
|---|---|
| `vps-backup-job-monitor` | `vps-backup-suite` (`VPS Backup Suite`) |
| `vps-backup-manager` | `vps-backup-suite` (`VPS Backup Suite`) |
| `vps-backup-restore-verifier` | `vps-backup-suite` (`VPS Backup Suite`) |
| `vps-configuration-drift-auditor` | `vps-deployment-readiness-suite` (`VPS Deployment Readiness Suite`) |
| `vps-container-security-auditor` | `vps-container-security-suite` (`VPS Container Security Suite`) |
| `vps-cost-capacity-auditor` | `vps-observability-suite` (`VPS Observability Suite`) |
| `vps-dependency-topology-auditor` | `vps-deployment-readiness-suite` (`VPS Deployment Readiness Suite`) |
| `vps-deployment-readiness-auditor` | `vps-deployment-readiness-suite` (`VPS Deployment Readiness Suite`) |
| `vps-dns-email-auth-auditor` | `vps-network-exposure-suite` (`VPS Network Exposure Suite`) |
| `vps-docker-network-isolation-auditor` | `vps-container-security-suite` (`VPS Container Security Suite`) |
| `vps-docker-resource-limits-auditor` | `vps-container-security-suite` (`VPS Container Security Suite`) |
| `vps-image-provenance-auditor` | `vps-container-security-suite` (`VPS Container Security Suite`) |
| `vps-image-vulnerability-sbom-auditor` | `vps-container-security-suite` (`VPS Container Security Suite`) |
| `vps-incident-responder` | `vps-incident-security-suite` (`VPS Incident & Security Suite`) |
| `vps-log-retention-auditor` | `vps-observability-suite` (`VPS Observability Suite`) |
| `vps-network-diagnostics` | `vps-network-exposure-suite` (`VPS Network Exposure Suite`) |
| `vps-observability-auditor` | `vps-observability-suite` (`VPS Observability Suite`) |
| `vps-resource-monitor` | `vps-observability-suite` (`VPS Observability Suite`) |
| `vps-security-auditor` | `vps-incident-security-suite` (`VPS Incident & Security Suite`) |
| `vps-service-exposure-auditor` | `vps-network-exposure-suite` (`VPS Network Exposure Suite`) |
| `vps-tls-renewal-monitor` | `vps-network-exposure-suite` (`VPS Network Exposure Suite`) |

## Instalación

En Claude Code:

```text
claude plugin marketplace add MauricioPerera/thehumanintheloop-marketplace-codex
claude plugin install linter-seo-geo-2026@thehumanintheloop-marketplace-claude
```

En Claude Desktop, usa `+ → Plugins → Add plugin`; los comandos `/plugin` solo funcionan dentro de la interfaz interactiva de Claude Code.

En Codex, registra el marketplace desde Plugins y busca `linter-seo-geo-2026`, o usa el botón de instalación de la [GitHub Page](https://mauricioperera.github.io/thehumanintheloop-marketplace-codex/).

Para instalar otro plugin, reemplaza `linter-seo-geo-2026` por cualquiera de los nombres disponibles en la sección [Plugins disponibles](#plugins-disponibles). En la página, el botón **Pedir a Codex** prepara una conversación con el nombre exacto del plugin y **Claude** ofrece la instrucción equivalente para Claude Code.

Si ya habías agregado este marketplace antes, `claude plugin install` puede fallar con `Plugin "..." not found in marketplace` para un plugin agregado recientemente, porque Claude Code cachea el marketplace localmente y no lo refresca solo. Actualiza el caché primero:

```text
claude plugin marketplace update thehumanintheloop-marketplace-claude
```

## Design System Analyses publicados

Los análisis visuales se publican como resultados reutilizables, no como plugins generadores. Cada análisis incluye el contrato `DESIGN.md`, tokens estructurados, reporte de validación y un preview HTML integrado en el catálogo. Actualmente están disponibles desde la sección de diseños de la [GitHub Page](https://mauricioperera.github.io/thehumanintheloop-marketplace-codex/).

Análisis publicados:

- [KDD](https://mauricioperera.github.io/thehumanintheloop-marketplace-codex/analyses/kdd/) — Knowledge-Driven Development.
- [Mercado Libre México](https://mauricioperera.github.io/thehumanintheloop-marketplace-codex/analyses/mercadolibre/).
- [TheHumanInTheLoop Marketplace](https://mauricioperera.github.io/thehumanintheloop-marketplace-codex/analyses/marketplace/).
- [GitHub](https://mauricioperera.github.io/thehumanintheloop-marketplace-codex/analyses/github/).
- [Google](https://mauricioperera.github.io/thehumanintheloop-marketplace-codex/analyses/google/).
- [LinkedIn](https://mauricioperera.github.io/thehumanintheloop-marketplace-codex/analyses/linkedin/).
- [Crunchyroll](https://mauricioperera.github.io/thehumanintheloop-marketplace-codex/analyses/crunchyroll/).
- [Prime Video](https://mauricioperera.github.io/thehumanintheloop-marketplace-codex/analyses/primevideo/).
- [Netflix](https://mauricioperera.github.io/thehumanintheloop-marketplace-codex/analyses/netflix/).
- [OpenAI](https://mauricioperera.github.io/thehumanintheloop-marketplace-codex/analyses/openai/).
- [Google Antigravity](https://mauricioperera.github.io/thehumanintheloop-marketplace-codex/analyses/antigravity/).
- [Anthropic](https://mauricioperera.github.io/thehumanintheloop-marketplace-codex/analyses/anthropic/).
- [Claude](https://mauricioperera.github.io/thehumanintheloop-marketplace-codex/analyses/claude/).
- [Ollama](https://mauricioperera.github.io/thehumanintheloop-marketplace-codex/analyses/ollama/).
- [Qwen](https://mauricioperera.github.io/thehumanintheloop-marketplace-codex/analyses/qwen/).
- [ZCode](https://mauricioperera.github.io/thehumanintheloop-marketplace-codex/analyses/zcode/).
- [NotebookLM / Gemini Notebook](https://mauricioperera.github.io/thehumanintheloop-marketplace-codex/analyses/notebooklm/).

Cada preview enlaza su `DESIGN.md`, `design-system.json`, reporte de validación y fuente original. Las advertencias de procedencia, contenido dinámico o extracción limitada se mantienen en cada análisis.

Este repositorio se distribuye bajo la [licencia MIT](LICENSE). Los análisis de terceros y las marcas o activos de sus respectivos sitios conservan sus derechos y condiciones de uso.
