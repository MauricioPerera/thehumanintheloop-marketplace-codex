const plugins = [{
  name: 'linter-seo-geo-2026', displayName: 'Auditor SEO/GEO 2026', category: 'Content & Editorial', icon: '⌁', version: '0.1.0',
  description: 'Validador de contenido para buscadores y motores generativos con controles de prepublicación.',
  capabilities: ['SEO', 'GEO', 'Contenido'],
  url: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex/tree/main/plugins/linter-seo-geo-2026', marketplace: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex', codexUrl: 'codex://new', claudeMarketplace: 'thehumanintheloop-marketplace-claude'
}, {
  name: 'marketplace-validator', displayName: 'Marketplace Validator', category: 'Marketplace & Quality', icon: 'MV', version: '0.1.0',
  description: 'Valida manifests, rutas, sincronización y estructura dual Claude Code/Codex antes de publicar.',
  capabilities: ['Marketplace', 'Validation', 'Claude + Codex'], url: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex/tree/main/plugins/marketplace-validator', marketplace: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex', codexUrl: 'codex://new', claudeMarketplace: 'thehumanintheloop-marketplace-claude'
}, {
  name: 'design-system-auditor', displayName: 'Design System Auditor', category: 'Design Systems', icon: 'DS', version: '0.1.0',
  description: 'Genera DESIGN.md, tokens, componentes y validadores a partir de un sitio o proyecto.',
  capabilities: ['DESIGN.md', 'Tokens', 'Validation'], url: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex/tree/main/plugins/design-system-auditor', marketplace: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex', codexUrl: 'codex://new', claudeMarketplace: 'thehumanintheloop-marketplace-claude'
}, {
  name: 'content-fact-checker', displayName: 'Content Fact Checker', category: 'Content & Editorial', icon: 'FC', version: '0.1.0',
  description: 'Detecta afirmaciones verificables y exige fuentes, fechas y atribuciones antes de publicar.',
  capabilities: ['Facts', 'Sources', 'Evidence'], url: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex/tree/main/plugins/content-fact-checker', marketplace: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex', codexUrl: 'codex://new', claudeMarketplace: 'thehumanintheloop-marketplace-claude'
}, {
  name: 'cv-job-tailor', displayName: 'CV Job Tailor', category: 'Content & Editorial', icon: 'CV', version: '0.1.0',
  description: 'Adapta CVs a ofertas laborales con trazabilidad, controles anti-fabricación y validación ATS.',
  capabilities: ['CV', 'ATS', 'Traceability'], url: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex/tree/main/plugins/cv-job-tailor', marketplace: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex', codexUrl: 'codex://new', claudeMarketplace: 'thehumanintheloop-marketplace-claude'
}, {
  name: 'commercial-proposal-builder', displayName: 'Commercial Proposal Builder', category: 'Content & Editorial', icon: 'CP', version: '0.1.0',
  description: 'Redacta propuestas comerciales basadas en requerimientos con trazabilidad, control de alcance e integridad de precios.',
  capabilities: ['Requirements', 'Scope', 'Pricing'], url: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex/tree/main/plugins/commercial-proposal-builder', marketplace: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex', codexUrl: 'codex://new', claudeMarketplace: 'thehumanintheloop-marketplace-claude'
}, {
  name: 'rfp-response-builder', displayName: 'RFP Response Builder', category: 'Content & Editorial', icon: 'RFP', version: '0.1.0',
  description: 'Responde RFPs y licitaciones con matriz de cumplimiento, evidencia y control de compromisos.',
  capabilities: ['RFP', 'Compliance', 'Evidence'], url: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex/tree/main/plugins/rfp-response-builder', marketplace: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex', codexUrl: 'codex://new', claudeMarketplace: 'thehumanintheloop-marketplace-claude'
}, {
  name: 'github-issue-manager', displayName: 'GitHub Issue Manager', category: 'Developer Tools', icon: 'ISS', version: '0.1.0',
  description: 'Gestiona Issues con gh CLI, triage y confirmacion antes de acciones mutables.',
  capabilities: ['Issues', 'Triage', 'gh CLI'], url: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex/tree/main/plugins/github-issue-manager', marketplace: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex', codexUrl: 'codex://new', claudeMarketplace: 'thehumanintheloop-marketplace-claude'
}, {
  name: 'github-pr-manager', displayName: 'GitHub PR Manager', category: 'Developer Tools', icon: 'PR', version: '0.1.0',
  description: 'Prepara y revisa Pull Requests con gh CLI, checklist y evidencia de validacion.',
  capabilities: ['Pull Requests', 'Review', 'Checks'], url: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex/tree/main/plugins/github-pr-manager', marketplace: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex', codexUrl: 'codex://new', claudeMarketplace: 'thehumanintheloop-marketplace-claude'
}, {
  name: 'github-release-manager', displayName: 'GitHub Release Manager', category: 'Developer Tools', icon: 'REL', version: '0.1.0',
  description: 'Prepara releases, tags y notas de version con gh CLI y confirmacion antes de publicar.',
  capabilities: ['Releases', 'Tags', 'Changelog'], url: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex/tree/main/plugins/github-release-manager', marketplace: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex', codexUrl: 'codex://new', claudeMarketplace: 'thehumanintheloop-marketplace-claude'
}, {
  name: 'github-actions-manager', displayName: 'GitHub Actions Manager', category: 'Developer Tools', icon: 'CI', version: '0.1.0',
  description: 'Inspecciona ejecuciones, jobs y logs de GitHub Actions con evidencia.',
  capabilities: ['Actions', 'CI', 'Logs'], url: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex/tree/main/plugins/github-actions-manager', marketplace: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex', codexUrl: 'codex://new', claudeMarketplace: 'thehumanintheloop-marketplace-claude'
}, {
  name: 'github-project-manager', displayName: 'GitHub Project Manager', category: 'Developer Tools', icon: 'PROJ', version: '0.1.0',
  description: 'Organiza Projects, tareas y campos con planes de mutacion trazables.',
  capabilities: ['Projects', 'Planning', 'Tasks'], url: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex/tree/main/plugins/github-project-manager', marketplace: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex', codexUrl: 'codex://new', claudeMarketplace: 'thehumanintheloop-marketplace-claude'
}, {
  name: 'github-code-search', displayName: 'GitHub Code Search', category: 'Developer Tools', icon: 'SEARCH', version: '0.1.0',
  description: 'Busca codigo, commits y referencias en GitHub con consultas reproducibles.',
  capabilities: ['Code Search', 'References', 'Commits'], url: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex/tree/main/plugins/github-code-search', marketplace: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex', codexUrl: 'codex://new', claudeMarketplace: 'thehumanintheloop-marketplace-claude'
}, {
  name: 'github-security-manager', displayName: 'GitHub Security Manager', category: 'Security & Privacy', icon: 'SEC', version: '0.1.0',
  description: 'Audita alertas de seguridad y propone remediaciones trazables.',
  capabilities: ['Security', 'Scanning', 'Evidence'], url: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex/tree/main/plugins/github-security-manager', marketplace: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex', codexUrl: 'codex://new', claudeMarketplace: 'thehumanintheloop-marketplace-claude'
}, {
  name: 'github-dependabot-manager', displayName: 'GitHub Dependabot Manager', category: 'Security & Privacy', icon: 'DEP', version: '0.1.0',
  description: 'Revisa alertas Dependabot y propone actualizaciones seguras.',
  capabilities: ['Dependabot', 'Dependencies', 'Risk'], url: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex/tree/main/plugins/github-dependabot-manager', marketplace: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex', codexUrl: 'codex://new', claudeMarketplace: 'thehumanintheloop-marketplace-claude'
}, {
  name: 'github-notifications-manager', displayName: 'GitHub Notifications Manager', category: 'Developer Tools', icon: 'INBOX', version: '0.1.0',
  description: 'Resume y prioriza notificaciones de GitHub con enlaces y siguientes acciones.',
  capabilities: ['Notifications', 'Triage', 'Priority'], url: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex/tree/main/plugins/github-notifications-manager', marketplace: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex', codexUrl: 'codex://new', claudeMarketplace: 'thehumanintheloop-marketplace-claude'
}, {
  name: 'github-discussion-manager', displayName: 'GitHub Discussion Manager', category: 'Developer Tools', icon: 'DISC', version: '0.1.0',
  description: 'Resume y prepara respuestas trazables para GitHub Discussions.',
  capabilities: ['Discussions', 'Community', 'Moderation'], url: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex/tree/main/plugins/github-discussion-manager', marketplace: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex', codexUrl: 'codex://new', claudeMarketplace: 'thehumanintheloop-marketplace-claude'
}, {
  name: 'github-label-manager', displayName: 'GitHub Label Manager', category: 'Marketplace & Quality', icon: 'LAB', version: '0.1.0',
  description: 'Disena taxonomias y planes de labels con consistencia y preview.',
  capabilities: ['Labels', 'Taxonomy', 'Triage'], url: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex/tree/main/plugins/github-label-manager', marketplace: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex', codexUrl: 'codex://new', claudeMarketplace: 'thehumanintheloop-marketplace-claude'
}, {
  name: 'github-repository-manager', displayName: 'GitHub Repository Manager', category: 'Developer Tools', icon: 'REPO', version: '0.1.0',
  description: 'Inspecciona y configura repositorios con planes de cambio y confirmacion.',
  capabilities: ['Repositories', 'Settings', 'Administration'], url: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex/tree/main/plugins/github-repository-manager', marketplace: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex', codexUrl: 'codex://new', claudeMarketplace: 'thehumanintheloop-marketplace-claude'
}, {
  name: 'github-milestone-manager', displayName: 'GitHub Milestone Manager', category: 'Marketplace & Quality', icon: 'MILE', version: '0.1.0',
  description: 'Planifica milestones con objetivos medibles, fechas y Issues vinculados.',
  capabilities: ['Milestones', 'Planning', 'Progress'], url: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex/tree/main/plugins/github-milestone-manager', marketplace: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex', codexUrl: 'codex://new', claudeMarketplace: 'thehumanintheloop-marketplace-claude'
}, {
  name: 'github-branch-manager', displayName: 'GitHub Branch Manager', category: 'Developer Tools', icon: 'BR', version: '0.1.0',
  description: 'Inspecciona y prepara operaciones de ramas con guardas contra cambios destructivos.',
  capabilities: ['Branches', 'Git', 'Protection'], url: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex/tree/main/plugins/github-branch-manager', marketplace: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex', codexUrl: 'codex://new', claudeMarketplace: 'thehumanintheloop-marketplace-claude'
}, {
  name: 'github-template-manager', displayName: 'GitHub Template Manager', category: 'Developer Tools', icon: 'TPL', version: '0.1.0',
  description: 'Revisa y mantiene templates de Issues y Pull Requests con validadores.',
  capabilities: ['Templates', 'Issues', 'Pull Requests'], url: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex/tree/main/plugins/github-template-manager', marketplace: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex', codexUrl: 'codex://new', claudeMarketplace: 'thehumanintheloop-marketplace-claude'
}, {
  name: 'github-api-manager', displayName: 'GitHub API Manager', category: 'Developer Tools', icon: 'API+', version: '0.1.0',
  description: 'Ejecuta consultas seguras y reproducibles a GitHub API mediante gh CLI.',
  capabilities: ['REST API', 'GraphQL', 'Safe queries'], url: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex/tree/main/plugins/github-api-manager', marketplace: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex', codexUrl: 'codex://new', claudeMarketplace: 'thehumanintheloop-marketplace-claude'
}, {
  name: 'github-codeowners-manager', displayName: 'GitHub CODEOWNERS Manager', category: 'Developer Tools', icon: 'OWN', version: '0.1.0',
  description: 'Valida ownership y cobertura de rutas en CODEOWNERS.',
  capabilities: ['CODEOWNERS', 'Ownership', 'Coverage'], url: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex/tree/main/plugins/github-codeowners-manager', marketplace: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex', codexUrl: 'codex://new', claudeMarketplace: 'thehumanintheloop-marketplace-claude'
}, {
  name: 'github-contributor-manager', displayName: 'GitHub Contributor Manager', category: 'Developer Tools', icon: 'CON', version: '0.1.0',
  description: 'Analiza actividad de contribuyentes y propone reviewers con evidencia.',
  capabilities: ['Contributors', 'Ownership', 'Reviewers'], url: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex/tree/main/plugins/github-contributor-manager', marketplace: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex', codexUrl: 'codex://new', claudeMarketplace: 'thehumanintheloop-marketplace-claude'
}, {
  name: 'github-activity-manager', displayName: 'GitHub Activity Manager', category: 'Developer Tools', icon: 'ACT', version: '0.1.0',
  description: 'Resume actividad temporal del repositorio con evidencia y limites de alcance.',
  capabilities: ['Activity', 'Timeline', 'Evidence'], url: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex/tree/main/plugins/github-activity-manager', marketplace: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex', codexUrl: 'codex://new', claudeMarketplace: 'thehumanintheloop-marketplace-claude'
}, {
  name: 'github-traffic-manager', displayName: 'GitHub Traffic Manager', category: 'Developer Tools', icon: 'TRAF', version: '0.1.0',
  description: 'Analiza views, clones, referrers y rutas populares con limites claros.',
  capabilities: ['Traffic', 'Views', 'Clones'], url: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex/tree/main/plugins/github-traffic-manager', marketplace: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex', codexUrl: 'codex://new', claudeMarketplace: 'thehumanintheloop-marketplace-claude'
}, {
  name: 'github-webhook-manager', displayName: 'GitHub Webhook Manager', category: 'Security & Privacy', icon: 'HOOK', version: '0.1.0',
  description: 'Audita y prepara webhooks con eventos acotados y secretos redactados.',
  capabilities: ['Webhooks', 'Events', 'Security'], url: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex/tree/main/plugins/github-webhook-manager', marketplace: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex', codexUrl: 'codex://new', claudeMarketplace: 'thehumanintheloop-marketplace-claude'
}, {
  name: 'github-environment-manager', displayName: 'GitHub Environment Manager', category: 'Security & Privacy', icon: 'ENV', version: '0.1.0',
  description: 'Gestiona environments, reviewers y gates de despliegue con plan previo.',
  capabilities: ['Environments', 'Deployments', 'Protection'], url: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex/tree/main/plugins/github-environment-manager', marketplace: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex', codexUrl: 'codex://new', claudeMarketplace: 'thehumanintheloop-marketplace-claude'
}, {
  name: 'github-variable-manager', displayName: 'GitHub Variable Manager', category: 'Security & Privacy', icon: 'VAR', version: '0.1.0',
  description: 'Audita variables de Actions sin exponer secretos ni valores sensibles.',
  capabilities: ['Variables', 'Actions', 'Scopes'], url: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex/tree/main/plugins/github-variable-manager', marketplace: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex', codexUrl: 'codex://new', claudeMarketplace: 'thehumanintheloop-marketplace-claude'
}, {
  name: 'github-package-manager', displayName: 'GitHub Package Manager', category: 'Developer Tools', icon: 'PKG', version: '0.1.0',
  description: 'Revisa paquetes, versiones, visibilidad y planes de retencion.',
  capabilities: ['Packages', 'Versions', 'Retention'], url: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex/tree/main/plugins/github-package-manager', marketplace: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex', codexUrl: 'codex://new', claudeMarketplace: 'thehumanintheloop-marketplace-claude'
}, {
  name: 'github-secret-manager', displayName: 'GitHub Secret Manager', category: 'Security & Privacy', icon: 'SEC+', version: '0.1.0',
  description: 'Audita secretos por scope y referencias sin exponer valores.',
  capabilities: ['Secrets', 'Scopes', 'Rotation'], url: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex/tree/main/plugins/github-secret-manager', marketplace: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex', codexUrl: 'codex://new', claudeMarketplace: 'thehumanintheloop-marketplace-claude'
}, {
  name: 'github-ruleset-manager', displayName: 'GitHub Ruleset Manager', category: 'Security & Privacy', icon: 'RULE', version: '0.1.0',
  description: 'Diseña reglasets, bypass actors y checks requeridos.',
  capabilities: ['Rulesets', 'Branches', 'Governance'], url: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex/tree/main/plugins/github-ruleset-manager', marketplace: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex', codexUrl: 'codex://new', claudeMarketplace: 'thehumanintheloop-marketplace-claude'
}, {
  name: 'github-checks-manager', displayName: 'GitHub Checks Manager', category: 'Developer Tools', icon: 'CHK', version: '0.1.0',
  description: 'Analiza checks, annotations y resultados de CI con evidencia.',
  capabilities: ['Checks', 'CI', 'Annotations'], url: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex/tree/main/plugins/github-checks-manager', marketplace: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex', codexUrl: 'codex://new', claudeMarketplace: 'thehumanintheloop-marketplace-claude'
}, {
  name: 'github-audit-log-manager', displayName: 'GitHub Audit Log Manager', category: 'Security & Privacy', icon: 'AUD', version: '0.1.0',
  description: 'Analiza actividad administrativa con datos redactados.',
  capabilities: ['Audit Log', 'Activity', 'Evidence'], url: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex/tree/main/plugins/github-audit-log-manager', marketplace: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex', codexUrl: 'codex://new', claudeMarketplace: 'thehumanintheloop-marketplace-claude'
}, {
  name: 'github-runner-manager', displayName: 'GitHub Runner Manager', category: 'Security & Privacy', icon: 'RUN', version: '0.1.0',
  description: 'Audita runners, labels y aislamiento de Actions.',
  capabilities: ['Runners', 'Actions', 'Isolation'], url: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex/tree/main/plugins/github-runner-manager', marketplace: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex', codexUrl: 'codex://new', claudeMarketplace: 'thehumanintheloop-marketplace-claude'
}, {
  name: 'github-deployment-manager', displayName: 'GitHub Deployment Manager', category: 'Developer Tools', icon: 'DEPLOY', version: '0.1.0',
  description: 'Controla despliegues con evidencia y rollback.',
  capabilities: ['Deployments', 'Environments', 'Rollback'], url: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex/tree/main/plugins/github-deployment-manager', marketplace: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex', codexUrl: 'codex://new', claudeMarketplace: 'thehumanintheloop-marketplace-claude'
}, {
  name: 'github-team-manager', displayName: 'GitHub Team Manager', category: 'Security & Privacy', icon: 'TEAM', version: '0.1.0',
  description: 'Audita equipos, membresías y permisos.',
  capabilities: ['Teams', 'Permissions', 'Access'], url: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex/tree/main/plugins/github-team-manager', marketplace: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex', codexUrl: 'codex://new', claudeMarketplace: 'thehumanintheloop-marketplace-claude'
}, {
  name: 'github-merge-queue-manager', displayName: 'GitHub Merge Queue Manager', category: 'Developer Tools', icon: 'QUEUE', version: '0.1.0',
  description: 'Analiza colas de integración y checks.',
  capabilities: ['Merge Queue', 'Pull Requests', 'Integration'], url: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex/tree/main/plugins/github-merge-queue-manager', marketplace: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex', codexUrl: 'codex://new', claudeMarketplace: 'thehumanintheloop-marketplace-claude'
}, {
  name: 'github-fork-manager', displayName: 'GitHub Fork Manager', category: 'Developer Tools', icon: 'FORK', version: '0.1.0',
  description: 'Audita forks y políticas de redes de código.',
  capabilities: ['Forks', 'Networks', 'Governance'], url: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex/tree/main/plugins/github-fork-manager', marketplace: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex', codexUrl: 'codex://new', claudeMarketplace: 'thehumanintheloop-marketplace-claude'
}, {
  name: 'github-commit-signing-manager', displayName: 'GitHub Commit Signing Manager', category: 'Security & Privacy', icon: 'SIGN', version: '0.1.0',
  description: 'Audita firmas y verificación de commits.',
  capabilities: ['Signing', 'Commits', 'Verification'], url: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex/tree/main/plugins/github-commit-signing-manager', marketplace: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex', codexUrl: 'codex://new', claudeMarketplace: 'thehumanintheloop-marketplace-claude'
}, {
  name: 'github-migration-manager', displayName: 'GitHub Migration Manager', category: 'Developer Tools', icon: 'MIG', version: '0.1.0',
  description: 'Planifica migraciones con trazabilidad y rollback.',
  capabilities: ['Migration', 'Repositories', 'Rollback'], url: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex/tree/main/plugins/github-migration-manager', marketplace: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex', codexUrl: 'codex://new', claudeMarketplace: 'thehumanintheloop-marketplace-claude'
}, {
  name: 'github-archive-manager', displayName: 'GitHub Archive Manager', category: 'Developer Tools', icon: 'ARC', version: '0.1.0',
  description: 'Gestiona el ciclo de vida de repositorios.',
  capabilities: ['Archive', 'Lifecycle', 'Repositories'], url: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex/tree/main/plugins/github-archive-manager', marketplace: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex', codexUrl: 'codex://new', claudeMarketplace: 'thehumanintheloop-marketplace-claude'
}, {
  name: 'github-code-scanning-manager', displayName: 'GitHub Code Scanning Manager', category: 'Security & Privacy', icon: 'CODE', version: '0.1.0',
  description: 'Audita alertas de Code Scanning.',
  capabilities: ['Code Scanning', 'Alerts', 'Remediation'], url: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex/tree/main/plugins/github-code-scanning-manager', marketplace: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex', codexUrl: 'codex://new', claudeMarketplace: 'thehumanintheloop-marketplace-claude'
}, {
  name: 'github-secret-scanning-manager', displayName: 'GitHub Secret Scanning Manager', category: 'Security & Privacy', icon: 'SS', version: '0.1.0',
  description: 'Analiza alertas sin exponer secretos.',
  capabilities: ['Secret Scanning', 'Exposure', 'Revocation'], url: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex/tree/main/plugins/github-secret-scanning-manager', marketplace: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex', codexUrl: 'codex://new', claudeMarketplace: 'thehumanintheloop-marketplace-claude'
}, {
  name: 'github-security-advisory-manager', displayName: 'GitHub Security Advisory Manager', category: 'Security & Privacy', icon: 'ADV', version: '0.1.0',
  description: 'Gestiona advisories y divulgación responsable.',
  capabilities: ['Advisories', 'CVE', 'Disclosure'], url: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex/tree/main/plugins/github-security-advisory-manager', marketplace: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex', codexUrl: 'codex://new', claudeMarketplace: 'thehumanintheloop-marketplace-claude'
}, {
  name: 'github-dependency-review-manager', displayName: 'GitHub Dependency Review Manager', category: 'Security & Privacy', icon: 'DREV', version: '0.1.0',
  description: 'Revisa dependencias nuevas en Pull Requests.',
  capabilities: ['Dependencies', 'Pull Requests', 'Supply Chain'], url: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex/tree/main/plugins/github-dependency-review-manager', marketplace: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex', codexUrl: 'codex://new', claudeMarketplace: 'thehumanintheloop-marketplace-claude'
}, {
  name: 'github-private-reporting-manager', displayName: 'GitHub Private Reporting Manager', category: 'Security & Privacy', icon: 'PRIV', version: '0.1.0',
  description: 'Gestiona reportes privados de vulnerabilidades.',
  capabilities: ['Vulnerability Reports', 'Privacy', 'Disclosure'], url: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex/tree/main/plugins/github-private-reporting-manager', marketplace: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex', codexUrl: 'codex://new', claudeMarketplace: 'thehumanintheloop-marketplace-claude'
}, {
  name: 'github-organization-settings-manager', displayName: 'GitHub Organization Settings Manager', category: 'Security & Privacy', icon: 'ORG', version: '0.1.0',
  description: 'Audita políticas organizacionales.',
  capabilities: ['Organizations', 'Policies', 'Administration'], url: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex/tree/main/plugins/github-organization-settings-manager', marketplace: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex', codexUrl: 'codex://new', claudeMarketplace: 'thehumanintheloop-marketplace-claude'
}, {
  name: 'github-pages-manager', displayName: 'GitHub Pages Manager', category: 'Developer Tools', icon: 'PAGES', version: '0.1.0',
  description: 'Audita y prepara despliegues de GitHub Pages.',
  capabilities: ['Pages', 'Deployment', 'Publishing'], url: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex/tree/main/plugins/github-pages-manager', marketplace: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex', codexUrl: 'codex://new', claudeMarketplace: 'thehumanintheloop-marketplace-claude'
}, {
  name: 'github-funding-manager', displayName: 'GitHub Funding Manager', category: 'Developer Tools', icon: 'FUND', version: '0.1.0',
  description: 'Gestiona financiación y sponsorship.',
  capabilities: ['Funding', 'Sponsors', 'Repository'], url: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex/tree/main/plugins/github-funding-manager', marketplace: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex', codexUrl: 'codex://new', claudeMarketplace: 'thehumanintheloop-marketplace-claude'
}, {
  name: 'github-workflow-dispatch-manager', displayName: 'GitHub Workflow Dispatch Manager', category: 'Developer Tools', icon: 'DISP', version: '0.1.0',
  description: 'Prepara disparos manuales de workflows.',
  capabilities: ['Workflows', 'Dispatch', 'Inputs'], url: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex/tree/main/plugins/github-workflow-dispatch-manager', marketplace: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex', codexUrl: 'codex://new', claudeMarketplace: 'thehumanintheloop-marketplace-claude'
}, {
  name: 'github-oidc-manager', displayName: 'GitHub OIDC Manager', category: 'Security & Privacy', icon: 'OIDC', version: '0.1.0',
  description: 'Audita confianza OIDC de Actions.',
  capabilities: ['OIDC', 'Actions', 'Cloud Trust'], url: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex/tree/main/plugins/github-oidc-manager', marketplace: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex', codexUrl: 'codex://new', claudeMarketplace: 'thehumanintheloop-marketplace-claude'
}, {
  name: 'github-action-permissions-manager', displayName: 'GitHub Action Permissions Manager', category: 'Security & Privacy', icon: 'PERM', version: '0.1.0',
  description: 'Audita permisos de workflows y GITHUB_TOKEN.',
  capabilities: ['Actions', 'Permissions', 'GITHUB_TOKEN'], url: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex/tree/main/plugins/github-action-permissions-manager', marketplace: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex', codexUrl: 'codex://new', claudeMarketplace: 'thehumanintheloop-marketplace-claude'
}, {
  name: 'github-merge-conflict-manager', displayName: 'GitHub Merge Conflict Manager', category: 'Developer Tools', icon: 'CONF', version: '0.1.0',
  description: 'Diagnostica conflictos de Pull Requests.',
  capabilities: ['Conflicts', 'Pull Requests', 'Resolution'], url: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex/tree/main/plugins/github-merge-conflict-manager', marketplace: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex', codexUrl: 'codex://new', claudeMarketplace: 'thehumanintheloop-marketplace-claude'
}, {
  name: 'mercadopago-payment-manager', displayName: 'Mercado Pago Payment Manager', category: 'Developer Tools', icon: 'MP', version: '0.1.0',
  description: 'Prepara enlaces de pago con validadores de seguridad.',
  capabilities: ['Payments', 'Checkout', 'Validation'], url: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex/tree/main/plugins/mercadopago-payment-manager', marketplace: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex', codexUrl: 'codex://new', claudeMarketplace: 'thehumanintheloop-marketplace-claude'
}, {
  name: 'repo-quality-gate', displayName: 'Repo Quality Gate', category: 'Marketplace & Quality', icon: 'RQ', version: '0.1.0', description: 'Revisa repositorios antes de commit, PR, release o despliegue.', capabilities: ['Quality', 'CI', 'Release'], url: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex/tree/main/plugins/repo-quality-gate', marketplace: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex', codexUrl: 'codex://new', claudeMarketplace: 'thehumanintheloop-marketplace-claude'
}, {
  name: 'technical-docs-linter', displayName: 'Technical Docs Linter', category: 'Developer Tools', icon: 'TD', version: '0.1.0', description: 'Valida README, documentación API, ejemplos, comandos y enlaces.', capabilities: ['Docs', 'API', 'Examples'], url: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex/tree/main/plugins/technical-docs-linter', marketplace: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex', codexUrl: 'codex://new', claudeMarketplace: 'thehumanintheloop-marketplace-claude'
}, {
  name: 'accessibility-auditor', displayName: 'Accessibility Auditor', category: 'Accessibility & UX', icon: 'A11Y', version: '0.1.0', description: 'Audita HTML, ARIA, nombres accesibles, formularios y teclado.', capabilities: ['A11y', 'HTML', 'WCAG'], url: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex/tree/main/plugins/accessibility-auditor', marketplace: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex', codexUrl: 'codex://new', claudeMarketplace: 'thehumanintheloop-marketplace-claude'
}, {
  name: 'privacy-risk-auditor', displayName: 'Privacy Risk Auditor', category: 'Security & Privacy', icon: 'PR', version: '0.1.0', description: 'Detecta PII, secretos, credenciales y configuraciones de riesgo.', capabilities: ['Privacy', 'PII', 'Secrets'], url: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex/tree/main/plugins/privacy-risk-auditor', marketplace: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex', codexUrl: 'codex://new', claudeMarketplace: 'thehumanintheloop-marketplace-claude'
}, {
  name: 'release-readiness', displayName: 'Release Readiness', category: 'Marketplace & Quality', icon: 'RR', version: '0.1.0', description: 'Comprueba si un repositorio está listo para release o despliegue.', capabilities: ['Release', 'CI', 'Checklist'], url: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex/tree/main/plugins/release-readiness', marketplace: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex', codexUrl: 'codex://new', claudeMarketplace: 'thehumanintheloop-marketplace-claude'
}, {
  name: 'prompt-contract-linter', displayName: 'Prompt Contract Linter', category: 'AI & Prompt Engineering', icon: 'PC', version: '0.1.0', description: 'Valida objetivos, entradas, salidas, límites y criterios de aceptación.', capabilities: ['Prompts', 'Contracts', 'QA'], url: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex/tree/main/plugins/prompt-contract-linter', marketplace: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex', codexUrl: 'codex://new', claudeMarketplace: 'thehumanintheloop-marketplace-claude'
}, {
  name: 'research-evidence-builder', displayName: 'Research Evidence Builder', category: 'Research & Evidence', icon: 'RE', version: '0.1.0', description: 'Construye informes con fuentes, fechas, citas y matriz de evidencia.', capabilities: ['Research', 'Sources', 'Evidence'], url: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex/tree/main/plugins/research-evidence-builder', marketplace: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex', codexUrl: 'codex://new', claudeMarketplace: 'thehumanintheloop-marketplace-claude'
}, {
  name: 'brand-voice-validator', displayName: 'Brand Voice Validator', category: 'Content & Editorial', icon: 'BV', version: '0.1.0', description: 'Valida tono, vocabulario y claims contra una guía editorial.', capabilities: ['Brand', 'Voice', 'Editorial'], url: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex/tree/main/plugins/brand-voice-validator', marketplace: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex', codexUrl: 'codex://new', claudeMarketplace: 'thehumanintheloop-marketplace-claude'
}, {
  name: 'api-contract-linter', displayName: 'API Contract Linter', category: 'Developer Tools', icon: 'API', version: '0.1.0', description: 'Audita contratos OpenAPI, rutas, operaciones y respuestas.', capabilities: ['OpenAPI', 'Contracts', 'API'], url: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex/tree/main/plugins/api-contract-linter', marketplace: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex', codexUrl: 'codex://new', claudeMarketplace: 'thehumanintheloop-marketplace-claude'
}, {
  name: 'web-performance-auditor', displayName: 'Web Performance Auditor', category: 'Developer Tools', icon: 'WP', version: '0.1.0', description: 'Audita carga, recursos y Core Web Vitals con evidencia.', capabilities: ['Performance', 'LCP', 'CLS'], url: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex/tree/main/plugins/web-performance-auditor', marketplace: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex', codexUrl: 'codex://new', claudeMarketplace: 'thehumanintheloop-marketplace-claude'
}, {
  name: 'dependency-risk-auditor', displayName: 'Dependency Risk Auditor', category: 'Security & Privacy', icon: 'DR', version: '0.1.0', description: 'Revisa dependencias, lockfiles y riesgos de supply chain.', capabilities: ['Dependencies', 'Security', 'Supply Chain'], url: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex/tree/main/plugins/dependency-risk-auditor', marketplace: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex', codexUrl: 'codex://new', claudeMarketplace: 'thehumanintheloop-marketplace-claude'
}, {
  name: 'test-coverage-gate', displayName: 'Test Coverage Gate', category: 'Marketplace & Quality', icon: 'TC', version: '0.1.0', description: 'Valida evidencia de tests, reportes y cobertura antes de publicar.', capabilities: ['Tests', 'Coverage', 'Quality'], url: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex/tree/main/plugins/test-coverage-gate', marketplace: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex', codexUrl: 'codex://new', claudeMarketplace: 'thehumanintheloop-marketplace-claude'
}];
const analyses = [{
  name: 'KDD — Knowledge-Driven Development', category: 'Design Systems', icon: 'DS', version: '1.0.0',
  description: 'Análisis visual publicado con contrato duro/blando, tokens, componentes, responsive behavior y validadores.',
  capabilities: ['Tokens', 'Components', 'Validation'],
  url: './analyses/kdd/index.html', preview: './analyses/kdd/index.html', source: 'https://mauricioperera.github.io/KDD/', codexUrl: 'codex://new', designMdUrl: 'https://raw.githubusercontent.com/MauricioPerera/thehumanintheloop-marketplace-codex/main/docs/analyses/kdd/DESIGN.md', contractUrl: 'https://raw.githubusercontent.com/MauricioPerera/thehumanintheloop-marketplace-codex/main/docs/analyses/kdd/design-system.json'
}, {
  name: 'Mercado Libre México — Homepage', category: 'Design Systems', icon: 'ML', version: '1.0.0',
  description: 'Análisis externo del homepage público con tokens, búsqueda, cards, estados, responsive behavior y procedencia.',
  capabilities: ['Commerce UI', 'Responsive', 'Validation'],
  url: './analyses/mercadolibre/index.html', preview: './analyses/mercadolibre/index.html', source: 'https://www.mercadolibre.com.mx/', codexUrl: 'codex://new', designMdUrl: 'https://raw.githubusercontent.com/MauricioPerera/thehumanintheloop-marketplace-codex/main/docs/analyses/mercadolibre/DESIGN.md', contractUrl: 'https://raw.githubusercontent.com/MauricioPerera/thehumanintheloop-marketplace-codex/main/docs/analyses/mercadolibre/design-system.json'
}, {
  name: 'TheHumanInTheLoop Marketplace Codex', category: 'Design Systems', icon: 'THL', version: '1.0.0',
  description: 'Análisis del propio marketplace: identidad editorial, tokens, catálogo, instalación, previews y contrato de validación.',
  capabilities: ['Marketplace UI', 'Codex Flow', 'Validation'],
  url: './analyses/marketplace/index.html', preview: './analyses/marketplace/index.html', source: 'https://mauricioperera.github.io/thehumanintheloop-marketplace-codex/', codexUrl: 'codex://new', designMdUrl: 'https://raw.githubusercontent.com/MauricioPerera/thehumanintheloop-marketplace-codex/main/docs/analyses/marketplace/DESIGN.md', contractUrl: 'https://raw.githubusercontent.com/MauricioPerera/thehumanintheloop-marketplace-codex/main/docs/analyses/marketplace/design-system.json'
}, {
  name: 'GitHub Homepage', category: 'Design Systems', icon: 'GH', version: '1.0.0',
  description: 'Análisis externo del homepage público con tokens, navegación, CTAs, estados, responsive behavior y procedencia.',
  capabilities: ['Navigation UI', 'Responsive', 'Validation'],
  url: './analyses/github/index.html', preview: './analyses/github/index.html', source: 'https://github.com/', codexUrl: 'codex://new', designMdUrl: 'https://raw.githubusercontent.com/MauricioPerera/thehumanintheloop-marketplace-codex/main/docs/analyses/github/DESIGN.md', contractUrl: 'https://raw.githubusercontent.com/MauricioPerera/thehumanintheloop-marketplace-codex/main/docs/analyses/github/design-system.json'
}, {
  name: 'Google Homepage', category: 'Design Systems', icon: 'G', version: '1.0.0',
  description: 'Análisis externo del homepage público con búsqueda, tokens, estados, responsive behavior y procedencia.',
  capabilities: ['Search UI', 'Responsive', 'Validation'],
  url: './analyses/google/index.html', preview: './analyses/google/index.html', source: 'https://www.google.com/', codexUrl: 'codex://new', designMdUrl: 'https://raw.githubusercontent.com/MauricioPerera/thehumanintheloop-marketplace-codex/main/docs/analyses/google/DESIGN.md', contractUrl: 'https://raw.githubusercontent.com/MauricioPerera/thehumanintheloop-marketplace-codex/main/docs/analyses/google/design-system.json'
}, {
  name: 'LinkedIn Homepage', category: 'Design Systems', icon: 'in', version: '1.0.0',
  description: 'Análisis externo del homepage público con autenticación, contenido profesional, oportunidades y responsive behavior.',
  capabilities: ['Professional UI', 'Auth States', 'Validation'],
  url: './analyses/linkedin/index.html', preview: './analyses/linkedin/index.html', source: 'https://www.linkedin.com/', codexUrl: 'codex://new', designMdUrl: 'https://raw.githubusercontent.com/MauricioPerera/thehumanintheloop-marketplace-codex/main/docs/analyses/linkedin/DESIGN.md', contractUrl: 'https://raw.githubusercontent.com/MauricioPerera/thehumanintheloop-marketplace-codex/main/docs/analyses/linkedin/design-system.json'
}, {
  name: 'Crunchyroll Homepage', category: 'Design Systems', icon: 'CR', version: '1.0.0',
  description: 'Análisis externo del homepage público con streaming UI, hero, rails, planes Premium y responsive behavior.',
  capabilities: ['Streaming UI', 'Content Rails', 'Validation'],
  url: './analyses/crunchyroll/index.html', preview: './analyses/crunchyroll/index.html', source: 'https://www.crunchyroll.com/', codexUrl: 'codex://new', designMdUrl: 'https://raw.githubusercontent.com/MauricioPerera/thehumanintheloop-marketplace-codex/main/docs/analyses/crunchyroll/DESIGN.md', contractUrl: 'https://raw.githubusercontent.com/MauricioPerera/thehumanintheloop-marketplace-codex/main/docs/analyses/crunchyroll/design-system.json'
}, {
  name: 'Prime Video Homepage', category: 'Design Systems', icon: 'PV', version: '1.0.0',
  description: 'Análisis externo del homepage público con streaming UI, rankings, rails, suscripciones y responsive behavior.',
  capabilities: ['Streaming UI', 'Content Rails', 'Validation'],
  url: './analyses/primevideo/index.html', preview: './analyses/primevideo/index.html', source: 'https://www.primevideo.com/', codexUrl: 'codex://new', designMdUrl: 'https://raw.githubusercontent.com/MauricioPerera/thehumanintheloop-marketplace-codex/main/docs/analyses/primevideo/DESIGN.md', contractUrl: 'https://raw.githubusercontent.com/MauricioPerera/thehumanintheloop-marketplace-codex/main/docs/analyses/primevideo/design-system.json'
}];
const grid = document.querySelector('#plugin-grid');
const empty = document.querySelector('#empty-state');
const count = document.querySelector('#result-count');
const search = document.querySelector('#search');
let category = 'all';

function render() {
  const query = search.value.trim().toLowerCase();
  const catalog = [...plugins, ...analyses];
  const visible = catalog.filter(p => (category === 'all' || p.category === category) && `${p.name} ${p.displayName || ''} ${p.description} ${p.capabilities.join(' ')}`.toLowerCase().includes(query));
  count.textContent = visible.length;
  empty.hidden = visible.length !== 0;
  grid.innerHTML = visible.map(p => `<article class="plugin-card ${p.preview ? 'analysis-card' : ''}"><div class="card-top"><div class="plugin-icon" aria-hidden="true">${p.icon}</div><span class="badge">${p.preview ? 'Design System Analysis' : 'Plugin'} · ${p.category}</span></div><h3>${p.displayName || p.name}</h3><p>${p.description}</p>${p.preview ? `<div class="install-cta design-cta"><div class="design-platform-buttons"><button class="install-link" type="button" data-open-codex="${p.name}" data-open-type="design" data-codex-url="${p.codexUrl}" data-design-md="${p.designMdUrl}" data-contract="${p.contractUrl}" data-source="${p.source}">Abrir diseño en Codex</button><button class="install-link claude-link" type="button" data-open-claude-design="${p.name}" data-design-md="${p.designMdUrl}" data-contract="${p.contractUrl}" data-source="${p.source}">Abrir diseño en Claude</button></div><span class="install-status" role="status" aria-live="polite"></span></div><div class="card-footer"><span class="version">v${p.version} · ${p.capabilities.join(' · ')}</span><button class="card-link preview-link" type="button" data-preview="${p.preview}" data-title="${p.displayName || p.name}">Ver preview ↗</button></div>` : `<div class="platform-install-links"><button class="install-link claude-link" type="button" data-open-claude="${p.name}" data-claude-marketplace="${p.claudeMarketplace}">Copiar para Claude Code</button><button class="install-link" type="button" data-open-codex="${p.name}" data-codex-url="${p.codexUrl}">Abrir en Codex</button><span class="install-status" role="status" aria-live="polite"></span></div><div class="card-footer"><span class="version">v${p.version} · ${p.capabilities.join(' · ')}</span><a class="card-link" href="${p.url}" target="_blank" rel="noreferrer">GitHub ↗</a></div>`}</article>`).join('');
  document.querySelectorAll('[data-preview]').forEach(button => button.addEventListener('click', () => openPreview(button.dataset.preview, button.dataset.title)));
  document.querySelectorAll('[data-open-codex]').forEach(button => button.addEventListener('click', () => {
    const prompt = button.dataset.openType === 'design' ? buildDesignPrompt(button) : buildInstallPrompt(button.dataset.openCodex);
    const status = button.parentElement.querySelector('.install-status');
    const codexUrl = `${button.dataset.codexUrl}?prompt=${encodeURIComponent(prompt)}`;
    const codexWindow = window.open(codexUrl, '_blank', 'noopener,noreferrer');
    const copyPromise = navigator.clipboard?.writeText(prompt);
    if (!copyPromise) {
      button.textContent = 'Abrir Codex';
      status.textContent = 'No se pudo copiar automáticamente. Puedes copiar la solicitud desde el chat o intentarlo de nuevo.';
      return;
    }
    copyPromise.then(() => {
      button.textContent = 'Solicitud copiada';
      status.innerHTML = `${codexWindow ? 'Sesión preparada. ' : 'Codex fue bloqueado. '}Si la app no se abre, <a href="https://chatgpt.com/codex" target="_blank" rel="noreferrer">abre Codex web</a> y pega la solicitud.`;
    }).catch(() => {
      button.textContent = 'Abrir Codex';
      status.textContent = 'No se pudo copiar automáticamente. Puedes copiar la solicitud desde el chat o intentarlo de nuevo.';
    });
  }));
  document.querySelectorAll('[data-open-claude]').forEach(button => button.addEventListener('click', async () => {
    const prompt = buildClaudeInstallPrompt(button.dataset.openClaude, button.dataset.claudeMarketplace);
    const status = button.parentElement.querySelector('.install-status');
    try {
      await navigator.clipboard.writeText(prompt);
      button.textContent = 'Comandos copiados';
      status.textContent = 'Pégalos en Claude Code y confirma la instalación.';
    } catch {
      status.textContent = 'Copia manualmente los comandos de la sección de instalación.';
    }
  }));
  document.querySelectorAll('[data-open-claude-design]').forEach(button => button.addEventListener('click', async () => {
    const prompt = buildDesignPrompt(button);
    const status = button.parentElement.parentElement.querySelector('.install-status');
    const claudeWindow = window.open('https://claude.ai/new', '_blank', 'noopener,noreferrer');
    try {
      await navigator.clipboard.writeText(prompt);
      button.textContent = 'Instrucción copiada';
      status.textContent = `${claudeWindow ? 'Claude está abierto. ' : ''}Pega la instrucción para importar el diseño.`;
    } catch {
      status.textContent = 'No se pudo copiar automáticamente. Abre Claude y copia la instrucción manualmente.';
    }
  }));
}

function buildInstallPrompt(pluginName) {
  return `Quiero instalar el plugin "${pluginName}" desde este marketplace:\nhttps://github.com/MauricioPerera/thehumanintheloop-marketplace-codex\n\nInstala únicamente ese plugin. Confirma el nombre exacto, indícame si necesitas autorización y dime cuándo esté listo para usarlo en un chat nuevo.`;
}

function buildClaudeInstallPrompt(pluginName, marketplaceName) {
  return `claude plugin marketplace add MauricioPerera/thehumanintheloop-marketplace-codex\nclaude plugin install ${pluginName}@${marketplaceName}`;
}

function buildDesignPrompt(button) {
  const designName = button.dataset.openCodex || button.dataset.openClaudeDesign;
  return `Quiero importar el Design System Analysis "${designName}" en mi proyecto actual.\n\nUsa DESIGN.md como contrato principal y design-system.json como contrato estructurado:\n- DESIGN.md: ${button.dataset.designMd}\n- design-system.json: ${button.dataset.contract}\n\nEl sitio analizado originalmente es: ${button.dataset.source}\n\nPrimero inspecciona el proyecto actual y explica dónde integrarás los tokens, componentes, estados, layout y responsive behavior. Después aplica el sistema de diseño respetando sus validadores y señala cualquier conflicto antes de modificar archivos. No copies contenido ni activos propietarios del sitio de referencia.`;
}

function renderFilters() {
  const catalog = [...plugins, ...analyses];
  const categories = [...new Set(catalog.map(item => item.category))].sort();
  const labels = {
    'Content & Editorial': 'Contenido',
    'Design Systems': 'Design Systems',
    'Marketplace & Quality': 'Marketplace y calidad',
    'Developer Tools': 'Developer tools',
    'Accessibility & UX': 'Accesibilidad',
    'Security & Privacy': 'Seguridad y privacidad',
    'Research & Evidence': 'Investigación',
    'AI & Prompt Engineering': 'IA y prompts'
  };
  document.querySelector('.filters').innerHTML = ['all', ...categories].map(value => {
    const amount = value === 'all' ? catalog.length : catalog.filter(item => item.category === value).length;
    return `<button class="filter ${value === 'all' ? 'active' : ''}" data-category="${value}" aria-pressed="${value === 'all'}">${value === 'all' ? 'Todos' : (labels[value] || value)} <small>${amount}</small></button>`;
  }).join('');
  document.querySelectorAll('.filter').forEach(button => button.addEventListener('click', () => {
    document.querySelector('.filter.active').classList.remove('active');
    button.classList.add('active');
    document.querySelectorAll('.filter').forEach(item => item.setAttribute('aria-pressed', item === button ? 'true' : 'false'));
    category = button.dataset.category;
    render();
  }));
}

const previewDialog = document.querySelector('#preview-dialog');
const previewFrame = document.querySelector('#preview-frame');
const previewTitle = document.querySelector('#preview-title');
function openPreview(url, title) {
  previewTitle.textContent = title;
  previewFrame.src = url;
  previewDialog.showModal();
}
document.querySelector('#close-preview').addEventListener('click', () => { previewFrame.src = 'about:blank'; previewDialog.close(); });
previewDialog.addEventListener('click', event => { if (event.target === previewDialog) { previewFrame.src = 'about:blank'; previewDialog.close(); } });
search.addEventListener('input', render);
document.querySelectorAll('[data-platform-command]').forEach(button => button.addEventListener('click', () => {
  document.querySelectorAll('[data-platform-command]').forEach(item => item.classList.remove('active'));
  button.classList.add('active');
  document.querySelector('#install-command').textContent = button.dataset.platformCommand === 'claude'
    ? `claude plugin marketplace add MauricioPerera/thehumanintheloop-marketplace-codex\nclaude plugin install linter-seo-geo-2026@thehumanintheloop-marketplace-claude`
    : `codex plugin marketplace add MauricioPerera/thehumanintheloop-marketplace-codex\ncodex plugin install linter-seo-geo-2026`;
}));
document.querySelector('#copy-command').addEventListener('click', async () => { const text = document.querySelector('#install-command').textContent; try { await navigator.clipboard.writeText(text); document.querySelector('#copy-status').textContent = 'Copiado'; } catch { document.querySelector('#copy-status').textContent = 'Selecciona y copia el comando'; } });
renderFilters();
render();
