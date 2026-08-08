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
  name: 'github-code-search', displayName: 'GitHub Code Search', category: 'Developer Tools', icon: 'SEARCH', version: '0.1.0',
  description: 'Busca codigo, commits y referencias en GitHub con consultas reproducibles.',
  capabilities: ['Code Search', 'References', 'Commits'], url: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex/tree/main/plugins/github-code-search', marketplace: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex', codexUrl: 'codex://new', claudeMarketplace: 'thehumanintheloop-marketplace-claude'
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
}, {
  name: 'kdd-semver', displayName: 'KDD SemVer Checker', category: 'Developer Tools', icon: 'SV', version: '0.1.0',
  description: 'Verifica cumplimiento de Semantic Versioning 2.0.0 con un instrumento determinista extraido con Knowledge-Driven Development.',
  capabilities: ['SemVer', 'Versioning', 'KDD'], url: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex/tree/main/plugins/kdd-semver', marketplace: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex', codexUrl: 'codex://new', claudeMarketplace: 'thehumanintheloop-marketplace-claude'
}, {
  name: 'kdd-stripe', displayName: 'KDD Stripe API Checker', category: 'Security & Privacy', icon: 'ST', version: '0.1.0',
  description: 'Verifica claves de Stripe embebidas en el codigo e Idempotency-Key en peticiones GET/DELETE, extraido con Knowledge-Driven Development.',
  capabilities: ['Stripe', 'Security', 'KDD'], url: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex/tree/main/plugins/kdd-stripe', marketplace: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex', codexUrl: 'codex://new', claudeMarketplace: 'thehumanintheloop-marketplace-claude'
}, {
  name: 'kdd-rust-api', displayName: 'KDD Rust API Guidelines Checker', category: 'Developer Tools', icon: 'RS', version: '0.1.0',
  description: 'Verifica getters, Debug y ejemplos rustdoc de las Rust API Guidelines, extraido con Knowledge-Driven Development.',
  capabilities: ['Rust', 'API Guidelines', 'KDD'], url: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex/tree/main/plugins/kdd-rust-api', marketplace: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex', codexUrl: 'codex://new', claudeMarketplace: 'thehumanintheloop-marketplace-claude'
}, {
  name: 'kdd-effective-go', displayName: 'KDD Effective Go Checker', category: 'Developer Tools', icon: 'EG', version: '0.1.0',
  description: 'Verifica indentacion con tabs, parentesis en control y llaves de Effective Go, extraido con Knowledge-Driven Development.',
  capabilities: ['Go', 'Effective Go', 'KDD'], url: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex/tree/main/plugins/kdd-effective-go', marketplace: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex', codexUrl: 'codex://new', claudeMarketplace: 'thehumanintheloop-marketplace-claude'
}, {
  name: 'kdd-zen-of-python', displayName: 'KDD Zen of Python Reference', category: 'Developer Tools', icon: 'ZP', version: '0.1.0',
  description: 'Consulta honesta de los 19 aforismos del Zen de Python (0% instrumentado), extraido con Knowledge-Driven Development.',
  capabilities: ['Python', 'Zen of Python', 'KDD'], url: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex/tree/main/plugins/kdd-zen-of-python', marketplace: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex', codexUrl: 'codex://new', claudeMarketplace: 'thehumanintheloop-marketplace-claude'
}, {
  name: 'kdd-agile-manifesto', displayName: 'KDD Agile Manifesto Reference', category: 'Marketplace & Quality', icon: 'AM', version: '0.1.0',
  description: 'Consulta honesta de los 4 valores y 12 principios del Manifiesto Agil (0% instrumentado), extraido con Knowledge-Driven Development.',
  capabilities: ['Agile', 'Manifesto', 'KDD'], url: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex/tree/main/plugins/kdd-agile-manifesto', marketplace: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex', codexUrl: 'codex://new', claudeMarketplace: 'thehumanintheloop-marketplace-claude'
}, {
  name: 'kdd-tailwind', displayName: 'KDD Tailwind CSS Checker', category: 'Developer Tools', icon: 'TW', version: '0.1.0',
  description: 'Verifica 10 tecnicas de Tailwind CSS v4 (instalacion, conflictos de utilidades, mobile-first, theme), extraido con Knowledge-Driven Development.',
  capabilities: ['Tailwind', 'CSS', 'KDD'], url: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex/tree/main/plugins/kdd-tailwind', marketplace: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex', codexUrl: 'codex://new', claudeMarketplace: 'thehumanintheloop-marketplace-claude'
}, {
  name: 'kdd-wcag', displayName: 'KDD WCAG 2.2 Checker', category: 'Accessibility & UX', icon: 'A11', version: '0.1.0',
  description: 'Verifica 10 criterios de exito de WCAG 2.2 (idioma, contraste, area de toque, etiquetas), extraido con Knowledge-Driven Development.',
  capabilities: ['WCAG', 'Accessibility', 'KDD'], url: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex/tree/main/plugins/kdd-wcag', marketplace: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex', codexUrl: 'codex://new', claudeMarketplace: 'thehumanintheloop-marketplace-claude'
}, {
  name: 'kdd-doce-factores', displayName: 'KDD Twelve-Factor App Checker', category: 'Developer Tools', icon: '12F', version: '0.1.0',
  description: 'Verifica 10 tecnicas de The Twelve-Factor App: dependencias, config, servicios, puerto, paridad, daemonizacion, SIGTERM, logs, codebase y release ID.',
  capabilities: ['twelve-factor', '12factor', 'devops', 'kdd', 'validation'], url: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex/tree/main/plugins/kdd-doce-factores', marketplace: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex', codexUrl: 'codex://new', claudeMarketplace: 'thehumanintheloop-marketplace-claude'
}, {
  name: 'kdd-htmx', displayName: 'KDD htmx Checker', category: 'Developer Tools', icon: 'HX', version: '0.1.0',
  description: 'Verifica HTML, capturas HTTP y plantillas contra 6 tecnicas medibles de la documentacion de htmx: mejora progresiva, indicador, CSRF, Vary, CSP y escapado, extraidas con Knowledge-Driven Development.',
  capabilities: ['htmx', 'hypermedia', 'html', 'csp', 'csrf', 'kdd', 'validation'], url: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex/tree/main/plugins/kdd-htmx', marketplace: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex', codexUrl: 'codex://new', claudeMarketplace: 'thehumanintheloop-marketplace-claude'
}, {
  name: 'kdd-arquitectura-java', displayName: 'KDD Arquitectura Java Solida Checker', category: 'Developer Tools', icon: 'AJ', version: '0.1.0',
  description: 'Verifica 8 reglas de arquitectura y codigo limpio: capas, excepciones, ISP, DI/Factory, AOP, COC, duplicacion (G5) y polimorfismo antes que if/else (G23), extraidas con Knowledge-Driven Development.',
  capabilities: ['arquitectura', 'solid', 'capas', 'dependency-injection', 'kdd', 'validation'], url: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex/tree/main/plugins/kdd-arquitectura-java', marketplace: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex', codexUrl: 'codex://new', claudeMarketplace: 'thehumanintheloop-marketplace-claude'
}, {
  name: 'kdd-pep8', displayName: 'KDD PEP 8 Checker', category: 'Developer Tools', icon: 'P8', version: '0.1.0',
  description: 'Verifica 28 reglas de PEP 8: indentacion, longitud de linea, imports, comillas, comentarios, docstrings y convenciones de nombres, extraidas con Knowledge-Driven Development.',
  capabilities: ['pep8', 'python', 'style-guide', 'linting', 'kdd', 'validation'], url: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex/tree/main/plugins/kdd-pep8', marketplace: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex', codexUrl: 'codex://new', claudeMarketplace: 'thehumanintheloop-marketplace-claude'
}, {
  name: 'kdd-scrum-xp', displayName: 'KDD Scrum y XP Checker', category: 'Marketplace & Quality', icon: 'SX', version: '0.1.0',
  description: 'Verifica 12 tecnicas de Scrum y eXtreme Programming con instrumento real (cadencia, TDD, repo unico, Clean Code) y documenta 22 tecnicas mas que requieren tablero, calendario o CI reales, extraidas con Knowledge-Driven Development.',
  capabilities: ['scrum', 'extreme-programming', 'tdd', 'agile', 'kdd', 'validation'], url: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex/tree/main/plugins/kdd-scrum-xp', marketplace: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex', codexUrl: 'codex://new', claudeMarketplace: 'thehumanintheloop-marketplace-claude'
}, {
  name: 'kdd-codigo-limpio', displayName: 'KDD Codigo Limpio Checker', category: 'Developer Tools', icon: 'CL', version: '0.1.0',
  description: 'Verifica 30 heuristicas de Clean Code: comentarios, funciones, principios generales G, nombres, pruebas y profundidad de cadena, extraidas con Knowledge-Driven Development.',
  capabilities: ['clean-code', 'codigo-limpio', 'python', 'linting', 'kdd', 'validation'], url: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex/tree/main/plugins/kdd-codigo-limpio', marketplace: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex', codexUrl: 'codex://new', claudeMarketplace: 'thehumanintheloop-marketplace-claude'
}, {
  name: 'kdd-estilo-google', displayName: 'KDD Estilo Google Checker', category: 'Content & Editorial', icon: 'GS', version: '0.1.0',
  description: 'Verifica 42 reglas del Google developer documentation style guide: puntuacion, numeros/unidades/fechas, encabezados, codigo/CLI, voz/tiempo verbal y vocabulario declarado, extraidas con Knowledge-Driven Development.',
  capabilities: ['google-style', 'technical-writing', 'documentation', 'prosa', 'kdd', 'validation'], url: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex/tree/main/plugins/kdd-estilo-google', marketplace: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex', codexUrl: 'codex://new', claudeMarketplace: 'thehumanintheloop-marketplace-claude'
}, {
  name: 'vps-ssh-manager', displayName: 'VPS SSH Manager', category: 'Developer Tools', icon: 'SSH', version: '0.1.0',
  description: 'Conecta a VPS propios por SSH con preflight, verificación de host key y confirmación antes de cambios.',
  capabilities: ['SSH', 'VPS', 'Preflight', 'Remote diagnostics'], url: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex/tree/main/plugins/vps-ssh-manager', marketplace: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex', codexUrl: 'codex://new', claudeMarketplace: 'thehumanintheloop-marketplace-claude'
}, {
  name: 'supabase-selfhosted-observer', displayName: 'Supabase Self-hosted Observer', category: 'Developer Tools', icon: 'SVO', version: '0.1.0', description: 'Inspecciona salud, versiones, contenedores y recursos de Supabase self-hosted por SSH sin exponer secretos.', capabilities: ['Supabase', 'Docker', 'Observability', 'SSH'], url: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex/tree/main/plugins/supabase-selfhosted-observer', marketplace: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex', codexUrl: 'codex://new', claudeMarketplace: 'thehumanintheloop-marketplace-claude'
}, {
  name: 'supabase-database-manager', displayName: 'Supabase Database Manager', category: 'Developer Tools', icon: 'SDB', version: '0.1.0', description: 'Diagnostica y administra PostgreSQL de Supabase self-hosted por SSH con consultas seguras.', capabilities: ['Supabase', 'PostgreSQL', 'SQL', 'SSH'], url: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex/tree/main/plugins/supabase-database-manager', marketplace: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex', codexUrl: 'codex://new', claudeMarketplace: 'thehumanintheloop-marketplace-claude'
}, {
  name: 'supabase-service-manager', displayName: 'Supabase Service Manager', category: 'Developer Tools', icon: 'SSM', version: '0.1.0', description: 'Diagnostica y opera servicios Supabase en Docker Compose por SSH con rollback y confirmación.', capabilities: ['Supabase', 'Docker Compose', 'Services', 'Rollback'], url: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex/tree/main/plugins/supabase-service-manager', marketplace: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex', codexUrl: 'codex://new', claudeMarketplace: 'thehumanintheloop-marketplace-claude'
}, {
  name: 'supabase-config-auditor', displayName: 'Supabase Config Auditor', category: 'Security & Privacy', icon: 'SCA', version: '0.1.0', description: 'Audita configuración, variables, puertos y exposición de Supabase self-hosted sin revelar secretos.', capabilities: ['Supabase', 'Configuration', 'Secrets', 'Security'], url: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex/tree/main/plugins/supabase-config-auditor', marketplace: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex', codexUrl: 'codex://new', claudeMarketplace: 'thehumanintheloop-marketplace-claude'
}, {
  name: 'supabase-backup-manager', displayName: 'Supabase Backup Manager', category: 'Security & Privacy', icon: 'SBM', version: '0.1.0', description: 'Planifica y verifica backups y recuperaciones de PostgreSQL en Supabase self-hosted.', capabilities: ['Supabase', 'Backup', 'Restore', 'Recovery'], url: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex/tree/main/plugins/supabase-backup-manager', marketplace: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex', codexUrl: 'codex://new', claudeMarketplace: 'thehumanintheloop-marketplace-claude'
}, {
  name: 'supabase-upgrade-manager', displayName: 'Supabase Upgrade Manager', category: 'Developer Tools', icon: 'SUM', version: '0.1.0', description: 'Evalúa y prepara upgrades de Supabase self-hosted con compatibilidad, backup y rollback.', capabilities: ['Supabase', 'Upgrades', 'Compatibility', 'Rollback'], url: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex/tree/main/plugins/supabase-upgrade-manager', marketplace: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex', codexUrl: 'codex://new', claudeMarketplace: 'thehumanintheloop-marketplace-claude'
}, {
  name: 'docker-vps-observer', displayName: 'Docker VPS Observer', category: 'Developer Tools', icon: 'DVO', version: '0.1.0', description: 'Observa daemon, contenedores, healthchecks, recursos y puertos Docker por SSH sin mutaciones.', capabilities: ['Docker', 'SSH', 'Healthchecks', 'Resources'], url: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex/tree/main/plugins/docker-vps-observer', marketplace: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex', codexUrl: 'codex://new', claudeMarketplace: 'thehumanintheloop-marketplace-claude'
}, {
  name: 'docker-service-manager', displayName: 'Docker Service Manager', category: 'Developer Tools', icon: 'DSM', version: '0.1.0', description: 'Planifica cambios Docker Compose con preflight, confirmación, ventana y rollback.', capabilities: ['Docker Compose', 'SSH', 'Deployments', 'Rollback'], url: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex/tree/main/plugins/docker-service-manager', marketplace: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex', codexUrl: 'codex://new', claudeMarketplace: 'thehumanintheloop-marketplace-claude'
}, {
  name: 'docker-image-manager', displayName: 'Docker Image Manager', category: 'Developer Tools', icon: 'DIM', version: '0.1.0', description: 'Audita imágenes, digests y espacio recuperable con guardas contra limpieza destructiva.', capabilities: ['Docker Images', 'Disk Usage', 'Digests', 'Safe Cleanup'], url: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex/tree/main/plugins/docker-image-manager', marketplace: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex', codexUrl: 'codex://new', claudeMarketplace: 'thehumanintheloop-marketplace-claude'
}, {
  name: 'docker-storage-auditor', displayName: 'Docker Storage Auditor', category: 'Security & Privacy', icon: 'DSA', version: '0.1.0', description: 'Audita volúmenes, redes, mounts y exposición Docker sin leer secretos.', capabilities: ['Docker', 'Volumes', 'Networks', 'Exposure'], url: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex/tree/main/plugins/docker-storage-auditor', marketplace: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex', codexUrl: 'codex://new', claudeMarketplace: 'thehumanintheloop-marketplace-claude'
}, {
  name: 'docker-log-diagnostics', displayName: 'Docker Log Diagnostics', category: 'Developer Tools', icon: 'DLD', version: '0.1.0', description: 'Correlaciona logs acotados, eventos, reinicios y healthchecks para investigar incidentes.', capabilities: ['Docker Logs', 'Events', 'Healthchecks', 'Incident Response'], url: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex/tree/main/plugins/docker-log-diagnostics', marketplace: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex', codexUrl: 'codex://new', claudeMarketplace: 'thehumanintheloop-marketplace-claude'
}, {
  name: 'tls-domain-manager', displayName: 'TLS Domain Manager', category: 'Security & Privacy', icon: 'TDM', version: '0.1.0', description: 'Audita certificados, dominios, SNI y redirecciones HTTPS.', capabilities: ['TLS', 'Domains', 'Nginx', 'HTTPS'], url: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex/tree/main/plugins/tls-domain-manager', marketplace: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex', codexUrl: 'codex://new', claudeMarketplace: 'thehumanintheloop-marketplace-claude'
}, {
  name: 'firewall-policy-manager', displayName: 'Firewall Policy Manager', category: 'Security & Privacy', icon: 'FPM', version: '0.1.0', description: 'Audita UFW, iptables y nftables sin modificar reglas.', capabilities: ['Firewall', 'UFW', 'iptables', 'Hardening'], url: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex/tree/main/plugins/firewall-policy-manager', marketplace: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex', codexUrl: 'codex://new', claudeMarketplace: 'thehumanintheloop-marketplace-claude'
}, {
  name: 'system-update-planner', displayName: 'System Update Planner', category: 'Developer Tools', icon: 'SUP', version: '0.1.0', description: 'Prepara actualizaciones de paquetes y kernel con rollback.', capabilities: ['Updates', 'Kernel', 'Packages', 'Rollback'], url: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex/tree/main/plugins/system-update-planner', marketplace: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex', codexUrl: 'codex://new', claudeMarketplace: 'thehumanintheloop-marketplace-claude'
}, {
  name: 'cron-automation-auditor', displayName: 'Cron Automation Auditor', category: 'Developer Tools', icon: 'CAA', version: '0.1.0', description: 'Audita cron y systemd timers sin ejecutar tareas.', capabilities: ['Cron', 'Systemd Timers', 'Automation', 'Auditing'], url: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex/tree/main/plugins/cron-automation-auditor', marketplace: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex', codexUrl: 'codex://new', claudeMarketplace: 'thehumanintheloop-marketplace-claude'
}, {
  name: 'secrets-exposure-auditor', displayName: 'Secrets Exposure Auditor', category: 'Security & Privacy', icon: 'SEA', version: '0.1.0', description: 'Detecta indicios de secretos sin revelar valores.', capabilities: ['Secrets', 'Docker', 'Redaction', 'Security'], url: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex/tree/main/plugins/secrets-exposure-auditor', marketplace: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex', codexUrl: 'codex://new', claudeMarketplace: 'thehumanintheloop-marketplace-claude'
}, {
  name: 'nginx-reverse-proxy-manager', displayName: 'Nginx Reverse Proxy Manager', category: 'Developer Tools', icon: 'NRP', version: '0.1.0', description: 'Audita hosts, upstreams, headers y rutas públicas de Nginx.', capabilities: ['Nginx', 'Reverse Proxy', 'TLS', 'Routing'], url: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex/tree/main/plugins/nginx-reverse-proxy-manager', marketplace: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex', codexUrl: 'codex://new', claudeMarketplace: 'thehumanintheloop-marketplace-claude'
}, {
  name: 'database-operations-manager', displayName: 'Database Operations Manager', category: 'Developer Tools', icon: 'DBO', version: '0.1.0', description: 'Diagnostica PostgreSQL, MySQL y Redis con consultas seguras y confirmación.', capabilities: ['PostgreSQL', 'MySQL', 'Redis', 'Database Ops'], url: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex/tree/main/plugins/database-operations-manager', marketplace: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex', codexUrl: 'codex://new', claudeMarketplace: 'thehumanintheloop-marketplace-claude'
}, {
  name: 'supabase-policy-security-auditor', displayName: 'Supabase Policy Security Auditor', category: 'Security & Privacy', icon: 'SPSA', version: '0.1.0', description: 'Audita RLS, Storage, Auth/JWT y Edge Functions/Realtime de Supabase self-hosted en modo lectura sin revelar secretos.', capabilities: ['Supabase', 'RLS', 'Policies', 'Auth', 'JWT', 'Storage', 'Edge Functions'], url: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex/tree/main/plugins/supabase-policy-security-auditor', marketplace: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex', codexUrl: 'codex://new', claudeMarketplace: 'thehumanintheloop-marketplace-claude'
}, {
  name: 'supabase-migration-drift-auditor', displayName: 'Supabase Migration Drift Auditor', category: 'Security & Privacy', icon: 'SMDA', version: '0.1.0', description: 'Audita migraciones aplicadas, archivos en disco y catálogos PostgreSQL de Supabase self-hosted para detectar drift de schema sin aplicar ni revertir migraciones y sin leer datos de usuario ni secretos.', capabilities: ['Supabase', 'Migrations', 'Drift', 'Schema', 'Postgres', 'Read-only'], url: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex/tree/main/plugins/supabase-migration-drift-auditor', marketplace: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex', codexUrl: 'codex://new', claudeMarketplace: 'thehumanintheloop-marketplace-claude'
}, {
  name: 'supabase-pgcron-auditor', displayName: 'Supabase pg_cron Auditor', category: 'Developer Tools', icon: 'SPGCRA', version: '0.1.0', description: 'Audita jobs pg_cron de Supabase self-hosted en modo lectura listando cron.job y cron.job_run_details, detectando jobs fallidos, pausados, duplicados, frecuencias peligrosas y comandos que expongan secretos o muten fuera de alcance.', capabilities: ['Supabase', 'pg_cron', 'Cron', 'Read-only', 'Security'], url: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex/tree/main/plugins/supabase-pgcron-auditor', marketplace: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex', codexUrl: 'codex://new', claudeMarketplace: 'thehumanintheloop-marketplace-claude'
}, {
  name: 'agent-tools-runtime-poc', displayName: 'Agent Tools Runtime POC', category: 'Developer Tools', icon: 'ATR', version: '0.9.4', description: 'Runtime MCP instalable basado en just-bash para cargar adaptadores MCP, REST y CLI progresivamente desde skills, con catálogo estructurado, validadores, sesiones, preflight de CLIs, OAuth host-side y confirmación.', capabilities: ['just-bash', 'MCP', 'REST API', 'CLI', 'Adapter catalog', 'Preflight', 'OAuth', 'Validation'], url: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex/tree/main/plugins/agent-tools-runtime-poc', marketplace: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex', codexUrl: 'codex://new', claudeMarketplace: 'thehumanintheloop-marketplace-claude'
}, {
  name: 'plugin-authoring', displayName: 'Plugin Authoring', category: 'Marketplace & Quality', icon: 'PA', version: '0.1.0', description: 'Guía la creación de plugins, manifests, skills, entradas sincronizadas del marketplace y validaciones antes de publicar.', capabilities: ['Scaffolding', 'Manifests', 'Skills', 'Marketplace', 'Validation'], url: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex/tree/main/plugins/plugin-authoring', marketplace: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex', codexUrl: 'codex://new', claudeMarketplace: 'thehumanintheloop-marketplace-claude'
}, {
  name: 'kdd-guide', displayName: 'KDD Guide', category: 'Developer Tools', icon: 'KDD', version: '0.1.0', description: 'Explica y aplica Knowledge-Driven Development combinando OKF, CCDD, contratos deterministas y gates de validación.', capabilities: ['OKF', 'CCDD', 'Contracts', 'Validation', 'CI'], url: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex/tree/main/plugins/kdd-guide', marketplace: 'https://github.com/MauricioPerera/KDD', codexUrl: 'codex://new', claudeMarketplace: 'thehumanintheloop-marketplace-claude'
}, {
  name: 'ai-prompt-workflow', displayName: 'AI Prompt Workflow', category: 'AI & Prompt Engineering', icon: 'AI', version: '0.1.0', description: 'Diseña, revisa y mejora flujos de prompting con objetivos, contexto, restricciones y criterios de evaluación.', capabilities: ['Prompt design', 'Evaluation', 'Context', 'Guardrails'], url: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex/tree/main/plugins/ai-prompt-workflow', marketplace: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex', codexUrl: 'codex://new', claudeMarketplace: 'thehumanintheloop-marketplace-claude'
}, {
  name: 'ux-accessibility-guide', displayName: 'UX Accessibility Guide', category: 'Accessibility & UX', icon: 'UX', version: '0.1.0', description: 'Guía auditorías de accesibilidad y UX con evidencia, alcance explícito y pruebas manuales.', capabilities: ['UX review', 'Accessibility', 'Keyboard', 'Evidence'], url: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex/tree/main/plugins/ux-accessibility-guide', marketplace: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex', codexUrl: 'codex://new', claudeMarketplace: 'thehumanintheloop-marketplace-claude'
}, {
  name: 'research-methods-guide', displayName: 'Research Methods Guide', category: 'Research & Evidence', icon: 'RM', version: '0.1.0', description: 'Estructura investigaciones reproducibles con preguntas, fuentes, evidencia, incertidumbre y síntesis.', capabilities: ['Research', 'Sources', 'Evidence', 'Synthesis'], url: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex/tree/main/plugins/research-methods-guide', marketplace: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex', codexUrl: 'codex://new', claudeMarketplace: 'thehumanintheloop-marketplace-claude'
}, {
  name: 'design-system-governance', displayName: 'Design System Governance', category: 'Design Systems', icon: 'DSG', version: '0.1.0', description: 'Mantiene contratos de diseño y detecta drift entre tokens, componentes, documentación e implementación.', capabilities: ['Governance', 'Tokens', 'Components', 'Drift', 'Accessibility'], url: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex/tree/main/plugins/design-system-governance', marketplace: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex', codexUrl: 'codex://new', claudeMarketplace: 'thehumanintheloop-marketplace-claude'

}, {

  name: 'github-security-suite', displayName: 'GitHub Security Suite', category: 'Security & Privacy', icon: 'SEC', version: '0.2.0',
  description: 'Audita seguridad de GitHub: code/secret scanning, advisories, dependencias, Dependabot, reportes privados y secretos, con planes de remediación.',
  capabilities: ['Code scanning', 'Secret scanning', 'Advisories', 'Dependency review', 'Dependabot', 'Private reporting', 'Secrets'],
  url: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex/tree/main/plugins/github-security-suite', marketplace: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex', codexUrl: 'codex://new', claudeMarketplace: 'thehumanintheloop-marketplace-claude'

}, {

  name: 'github-cicd-governance', displayName: 'GitHub CI/CD Governance', category: 'Security & Privacy', icon: 'CID', version: '0.2.0',
  description: 'Audita la gobernanza de CI/CD en GitHub Actions: permisos, environments, checks, merge queue, runners, OIDC, variables y despliegues manuales.',
  capabilities: ['Action permissions', 'Environments', 'Checks', 'Merge queue', 'Runners', 'OIDC', 'Variables', 'Workflow dispatch'],
  url: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex/tree/main/plugins/github-cicd-governance', marketplace: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex', codexUrl: 'codex://new', claudeMarketplace: 'thehumanintheloop-marketplace-claude'

}, {

  name: 'github-repo-governance', displayName: 'GitHub Repository Governance', category: 'Developer Tools', icon: 'RGV', version: '0.2.0',
  description: 'Audita y prepara configuración de repositorios GitHub: settings, CODEOWNERS, templates, labels, milestones, funding, Pages y rulesets de protección.',
  capabilities: ['Repository settings', 'CODEOWNERS', 'Templates', 'Labels', 'Milestones', 'Funding', 'Pages', 'Rulesets'],
  url: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex/tree/main/plugins/github-repo-governance', marketplace: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex', codexUrl: 'codex://new', claudeMarketplace: 'thehumanintheloop-marketplace-claude'

}, {

  name: 'github-collab-activity', displayName: 'GitHub Collaboration & Activity', category: 'Developer Tools', icon: 'COL', version: '0.2.0',
  description: 'Resume actividad y colaboración en GitHub: Discussions, notificaciones, contribuidores, equipos, actividad temporal, tráfico y audit log administrativo.',
  capabilities: ['Discussions', 'Notifications', 'Contributors', 'Teams', 'Activity', 'Traffic', 'Audit log'],
  url: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex/tree/main/plugins/github-collab-activity', marketplace: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex', codexUrl: 'codex://new', claudeMarketplace: 'thehumanintheloop-marketplace-claude'

}, {

  name: 'github-branch-release-ops', displayName: 'GitHub Branch & Release Ops', category: 'Developer Tools', icon: 'BRO', version: '0.2.0',
  description: 'Opera el ciclo de vida de ramas y despliegues en GitHub: ramas, firma de commits, despliegues, conflictos de merge y paquetes.',
  capabilities: ['Branches', 'Commit signing', 'Deployments', 'Merge conflicts', 'Packages'],
  url: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex/tree/main/plugins/github-branch-release-ops', marketplace: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex', codexUrl: 'codex://new', claudeMarketplace: 'thehumanintheloop-marketplace-claude'

}, {

  name: 'github-org-lifecycle', displayName: 'GitHub Org & Lifecycle', category: 'Developer Tools', icon: 'ORG', version: '0.2.0',
  description: 'Audita configuración organizacional y ciclo de vida de repositorios en GitHub: settings de organización, archivado, migraciones, forks, webhooks, API y Projects.',
  capabilities: ['Organization settings', 'Archive', 'Migration', 'Forks', 'Webhooks', 'API queries', 'Projects'],
  url: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex/tree/main/plugins/github-org-lifecycle', marketplace: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex', codexUrl: 'codex://new', claudeMarketplace: 'thehumanintheloop-marketplace-claude'

}, {

  name: 'vps-backup-suite', displayName: 'VPS Backup Suite', category: 'Developer Tools', icon: 'BKP', version: '0.2.0',
  description: 'Planifica, monitorea y verifica backups de un VPS: jobs programados, planes de backup con restauración comprobable y verificación de integridad de restores, sin ejecutar cambios.',
  capabilities: ['Backup jobs', 'Backup planning', 'Restore verification'],
  url: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex/tree/main/plugins/vps-backup-suite', marketplace: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex', codexUrl: 'codex://new', claudeMarketplace: 'thehumanintheloop-marketplace-claude'

}, {

  name: 'vps-container-security-suite', displayName: 'VPS Container Security Suite', category: 'Security & Privacy', icon: 'CSE', version: '0.2.0',
  description: 'Audita seguridad de contenedores Docker en un VPS: postura general, aislamiento de red, límites de recursos, procedencia de imágenes y CVE/SBOM, en modo lectura.',
  capabilities: ['Container posture', 'Network isolation', 'Resource limits', 'Image provenance', 'CVE/SBOM'],
  url: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex/tree/main/plugins/vps-container-security-suite', marketplace: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex', codexUrl: 'codex://new', claudeMarketplace: 'thehumanintheloop-marketplace-claude'

}, {

  name: 'vps-network-exposure-suite', displayName: 'VPS Network Exposure Suite', category: 'Security & Privacy', icon: 'NET', version: '0.2.0',
  description: 'Audita la superficie de red expuesta de un VPS: DNS y autenticación de correo (SPF, DKIM, DMARC), diagnóstico de conectividad, exposición de servicios y renovación de certificados TLS.',
  capabilities: ['DNS/email auth', 'Network diagnostics', 'Service exposure', 'TLS renewal'],
  url: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex/tree/main/plugins/vps-network-exposure-suite', marketplace: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex', codexUrl: 'codex://new', claudeMarketplace: 'thehumanintheloop-marketplace-claude'

}, {

  name: 'vps-observability-suite', displayName: 'VPS Observability Suite', category: 'Developer Tools', icon: 'OBS', version: '0.2.0',
  description: 'Audita capacidad, métricas, logs y retención de un VPS: CPU, RAM, disco, sobredimensionamiento, healthchecks/alertas y crecimiento de logs, sin instalar agentes.',
  capabilities: ['Cost/capacity', 'Observability', 'Resource monitoring', 'Log retention'],
  url: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex/tree/main/plugins/vps-observability-suite', marketplace: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex', codexUrl: 'codex://new', claudeMarketplace: 'thehumanintheloop-marketplace-claude'

}, {

  name: 'vps-deployment-readiness-suite', displayName: 'VPS Deployment Readiness Suite', category: 'Developer Tools', icon: 'DEP', version: '0.2.0',
  description: 'Audita preparación de despliegues en un VPS: drift entre configuración declarada y estado activo, preparación de Docker Compose y mapa de dependencias y blast radius.',
  capabilities: ['Configuration drift', 'Deployment readiness', 'Dependency topology'],
  url: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex/tree/main/plugins/vps-deployment-readiness-suite', marketplace: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex', codexUrl: 'codex://new', claudeMarketplace: 'thehumanintheloop-marketplace-claude'

}, {

  name: 'vps-incident-security-suite', displayName: 'VPS Incident & Security Suite', category: 'Security & Privacy', icon: 'INC', version: '0.2.0',
  description: 'Audita seguridad de un VPS (firewall, SSH, fail2ban, actualizaciones) e investiga incidentes correlacionando procesos, conexiones, Docker, disco y memoria, sin aplicar cambios.',
  capabilities: ['Security audit', 'Incident investigation'],
  url: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex/tree/main/plugins/vps-incident-security-suite', marketplace: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex', codexUrl: 'codex://new', claudeMarketplace: 'thehumanintheloop-marketplace-claude'
}, {
  name: 'terraform-plan-auditor', displayName: 'Terraform Plan Auditor', category: 'Security & Privacy', icon: 'TFP', version: '0.1.0',
  description: 'Audita el output de `terraform plan` antes de aplicarlo: cambios destructivos, recursos con estado, permisos amplios y exposición pública, sin ejecutar apply, destroy ni modificar el state.',
  capabilities: ['Plan review', 'Destructive change detection', 'IAM risk', 'Public exposure', 'Drift-safe'],
  url: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex/tree/main/plugins/terraform-plan-auditor', marketplace: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex', codexUrl: 'codex://new', claudeMarketplace: 'thehumanintheloop-marketplace-claude'
}, {
  name: 'kdd-typescript', displayName: 'KDD TypeScript Checker', category: 'Developer Tools', icon: 'TS', version: '0.1.0',
  description: 'Verifica 17 reglas duras del Google TypeScript Style Guide: var/const/let, exports, imports, campos privados, const enum, wrapper types, comillas, triple igual y nombres con guion bajo, extraidas y verificadas con Knowledge-Driven Development.',
  capabilities: ['var/const', 'Exports', 'Imports', 'Comparisons', 'Naming'],
  url: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex/tree/main/plugins/kdd-typescript', marketplace: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex', codexUrl: 'codex://new', claudeMarketplace: 'thehumanintheloop-marketplace-claude'
}, {
  name: 'k8s-manifest-auditor', displayName: 'K8s Manifest Auditor', category: 'Security & Privacy', icon: 'K8S', version: '0.1.0',
  description: 'Audita manifiestos Kubernetes contra los Pod Security Standards oficiales (Baseline y Restricted): host namespaces, contenedores privilegiados, capabilities, hostPath, hostPort, privilege escalation, runAsNonRoot y seccomp, sin aplicar cambios al cluster.',
  capabilities: ['Host namespaces', 'Privileged containers', 'Capabilities', 'hostPath/hostPort', 'Privilege escalation', 'runAsNonRoot', 'Seccomp'],
  url: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex/tree/main/plugins/k8s-manifest-auditor', marketplace: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex', codexUrl: 'codex://new', claudeMarketplace: 'thehumanintheloop-marketplace-claude'
}, {
  name: 'kdd-dockerfile', displayName: 'KDD Dockerfile Checker', category: 'Developer Tools', icon: 'DFC', version: '0.1.0',
  description: 'Verifica 11 reglas duras de Dockerfile best practices: FROM sin pin, apt-get sin combinar ni limpiar, CMD/ENTRYPOINT en shell form, USER root, sudo instalado, WORKDIR relativo, ADD en vez de COPY, pipe sin pipefail y .dockerignore ausente, extraidas y verificadas con Knowledge-Driven Development.',
  capabilities: ['FROM pin', 'apt-get', 'CMD/ENTRYPOINT', 'USER', 'WORKDIR', 'ADD/COPY', 'pipefail'],
  url: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex/tree/main/plugins/kdd-dockerfile', marketplace: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex', codexUrl: 'codex://new', claudeMarketplace: 'thehumanintheloop-marketplace-claude'
}, {
  name: 'n8n-workflow-auditor', displayName: 'N8N Workflow Auditor', category: 'Security & Privacy', icon: 'N8N', version: '0.2.0',
  description: 'Audita workflows de n8n vía REST API en modo lectura: credenciales hardcodeadas, webhooks sin autenticación, nodos de alto riesgo, manejo de errores, reintentos y nodos huérfanos.',
  capabilities: ['n8n', 'Workflows', 'Seguridad', 'Robustez'],
  url: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex/tree/main/plugins/n8n-workflow-auditor', marketplace: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex', codexUrl: 'codex://new', claudeMarketplace: 'thehumanintheloop-marketplace-claude'
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
}, {
  name: 'Netflix Homepage', category: 'Design Systems', icon: 'NF', version: '1.0.0',
  description: 'Análisis externo del homepage público con adquisición, email signup, trending, beneficios, FAQ y responsive behavior.',
  capabilities: ['Streaming UI', 'Acquisition', 'Validation'],
  url: './analyses/netflix/index.html', preview: './analyses/netflix/index.html', source: 'https://www.netflix.com/', codexUrl: 'codex://new', designMdUrl: 'https://raw.githubusercontent.com/MauricioPerera/thehumanintheloop-marketplace-codex/main/docs/analyses/netflix/DESIGN.md', contractUrl: 'https://raw.githubusercontent.com/MauricioPerera/thehumanintheloop-marketplace-codex/main/docs/analyses/netflix/design-system.json'
}, {
  name: 'OpenAI Homepage', category: 'Design Systems', icon: 'OAI', version: '1.0.0',
  description: 'Análisis externo del homepage público con navegación por audiencias, prompt, contenido editorial y productos.',
  capabilities: ['Editorial UI', 'Prompt Entry', 'Validation'],
  url: './analyses/openai/index.html', preview: './analyses/openai/index.html', source: 'https://openai.com/', codexUrl: 'codex://new', designMdUrl: 'https://raw.githubusercontent.com/MauricioPerera/thehumanintheloop-marketplace-codex/main/docs/analyses/openai/DESIGN.md', contractUrl: 'https://raw.githubusercontent.com/MauricioPerera/thehumanintheloop-marketplace-codex/main/docs/analyses/openai/design-system.json'
}, {
  name: 'Google Antigravity', category: 'Design Systems', icon: 'AG', version: '1.0.0',
  description: 'Análisis externo de antigravity.google con producto agentic, CLI, SDK, IDE, casos de uso y descargas.',
  capabilities: ['Product UI', 'Agentic UX', 'Validation'],
  url: './analyses/antigravity/index.html', preview: './analyses/antigravity/index.html', source: 'https://antigravity.google/', codexUrl: 'codex://new', designMdUrl: 'https://raw.githubusercontent.com/MauricioPerera/thehumanintheloop-marketplace-codex/main/docs/analyses/antigravity/DESIGN.md', contractUrl: 'https://raw.githubusercontent.com/MauricioPerera/thehumanintheloop-marketplace-codex/main/docs/analyses/antigravity/design-system.json'
}, {
  name: 'Anthropic Homepage', category: 'Design Systems', icon: 'AN', version: '1.0.0',
  description: 'Análisis externo del homepage público con safety, research, productos, releases, políticas y navegación editorial.',
  capabilities: ['Editorial UI', 'Safety', 'Validation'],
  url: './analyses/anthropic/index.html', preview: './analyses/anthropic/index.html', source: 'https://www.anthropic.com/', codexUrl: 'codex://new', designMdUrl: 'https://raw.githubusercontent.com/MauricioPerera/thehumanintheloop-marketplace-codex/main/docs/analyses/anthropic/DESIGN.md', contractUrl: 'https://raw.githubusercontent.com/MauricioPerera/thehumanintheloop-marketplace-codex/main/docs/analyses/anthropic/design-system.json'
}, {
  name: 'Claude Homepage', category: 'Design Systems', icon: 'CL', version: '1.0.0',
  description: 'Análisis externo del producto Claude con autenticación, planes, beneficios, FAQ y navegación de ecosistema.',
  capabilities: ['Product UI', 'Pricing', 'Validation'],
  url: './analyses/claude/index.html', preview: './analyses/claude/index.html', source: 'https://claude.com/', codexUrl: 'codex://new', designMdUrl: 'https://raw.githubusercontent.com/MauricioPerera/thehumanintheloop-marketplace-codex/main/docs/analyses/claude/DESIGN.md', contractUrl: 'https://raw.githubusercontent.com/MauricioPerera/thehumanintheloop-marketplace-codex/main/docs/analyses/claude/design-system.json'
}, {
  name: 'Ollama Homepage', category: 'Design Systems', icon: 'OL', version: '1.0.0',
  description: 'Análisis externo del homepage público con open models, terminal, local/cloud, plan Pro y privacidad.',
  capabilities: ['Developer UI', 'Terminal UX', 'Validation'],
  url: './analyses/ollama/index.html', preview: './analyses/ollama/index.html', source: 'https://ollama.com/', codexUrl: 'codex://new', designMdUrl: 'https://raw.githubusercontent.com/MauricioPerera/thehumanintheloop-marketplace-codex/main/docs/analyses/ollama/DESIGN.md', contractUrl: 'https://raw.githubusercontent.com/MauricioPerera/thehumanintheloop-marketplace-codex/main/docs/analyses/ollama/design-system.json'
}, {
  name: 'Qwen Homepage', category: 'Design Systems', icon: 'QW', version: '1.0.0',
  description: 'Análisis externo del homepage público con Qwen Studio, API Platform, Download, modelos y features multimodales.',
  capabilities: ['AI Product UI', 'Model Cards', 'Validation'],
  url: './analyses/qwen/index.html', preview: './analyses/qwen/index.html', source: 'https://qwen.ai/', codexUrl: 'codex://new', designMdUrl: 'https://raw.githubusercontent.com/MauricioPerera/thehumanintheloop-marketplace-codex/main/docs/analyses/qwen/DESIGN.md', contractUrl: 'https://raw.githubusercontent.com/MauricioPerera/thehumanintheloop-marketplace-codex/main/docs/analyses/qwen/design-system.json'
}, {
  name: 'ZCode Homepage', category: 'Design Systems', icon: 'ZC', version: '1.0.0',
  description: 'Análisis externo de zcode.z.ai con agentic coding, workspace, task board, pricing, capabilities y downloads.',
  capabilities: ['Agentic UI', 'Developer UX', 'Validation'],
  url: './analyses/zcode/index.html', preview: './analyses/zcode/index.html', source: 'https://zcode.z.ai/en', codexUrl: 'codex://new', designMdUrl: 'https://raw.githubusercontent.com/MauricioPerera/thehumanintheloop-marketplace-codex/main/docs/analyses/zcode/DESIGN.md', contractUrl: 'https://raw.githubusercontent.com/MauricioPerera/thehumanintheloop-marketplace-codex/main/docs/analyses/zcode/design-system.json'
}, {
  name: 'NotebookLM Homepage', category: 'Design Systems', icon: 'NL', version: '1.0.0',
  description: 'Análisis externo de NotebookLM/Gemini Notebook con fuentes, citas, outputs multimodales y notebooks públicos.',
  capabilities: ['Research UI', 'Source Grounding', 'Validation'],
  url: './analyses/notebooklm/index.html', preview: './analyses/notebooklm/index.html', source: 'https://notebooklm.google/', codexUrl: 'codex://new', designMdUrl: 'https://raw.githubusercontent.com/MauricioPerera/thehumanintheloop-marketplace-codex/main/docs/analyses/notebooklm/DESIGN.md', contractUrl: 'https://raw.githubusercontent.com/MauricioPerera/thehumanintheloop-marketplace-codex/main/docs/analyses/notebooklm/design-system.json'
}, {
  name: 'Mihomo Gate Dashboard', category: 'Design Systems', icon: 'MG', version: '1.0.0',
  description: 'Análisis de un dashboard local oscuro con tokens índigo, navegación operativa, métricas, proxies, logs y responsive behavior.',
  capabilities: ['Dashboard UI', 'Dark Theme', 'Validation'],
  url: './analyses/mihomo-gate/index.html', preview: './analyses/mihomo-gate/index.html', source: 'local:pasted-text.txt', codexUrl: 'codex://new', designMdUrl: 'https://raw.githubusercontent.com/MauricioPerera/thehumanintheloop-marketplace-codex/main/docs/analyses/mihomo-gate/DESIGN.md', contractUrl: 'https://raw.githubusercontent.com/MauricioPerera/thehumanintheloop-marketplace-codex/main/docs/analyses/mihomo-gate/design-system.json'
}, {
  name: 'Echo Pace Logistics ERP', category: 'Design Systems', icon: 'EP', version: '1.0.0',
  description: 'Análisis de un dashboard ERP de logística con sidebar azul, métricas, gráficos, envíos, finanzas y facturación.',
  capabilities: ['ERP Dashboard', 'Logistics UI', 'Validation'],
  url: './analyses/echo-pace-logistics/index.html', preview: './analyses/echo-pace-logistics/index.html', source: 'local:pasted-text.txt', codexUrl: 'codex://new', designMdUrl: 'https://raw.githubusercontent.com/MauricioPerera/thehumanintheloop-marketplace-codex/main/docs/analyses/echo-pace-logistics/DESIGN.md', contractUrl: 'https://raw.githubusercontent.com/MauricioPerera/thehumanintheloop-marketplace-codex/main/docs/analyses/echo-pace-logistics/design-system.json'
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
  grid.innerHTML = visible.map(p => `<article class="plugin-card ${p.preview ? 'analysis-card' : ''}"><div class="card-top"><div class="plugin-icon" aria-hidden="true">${p.icon}</div><span class="badge">${p.preview ? 'Design System Analysis' : 'Plugin'} · ${p.category}</span></div><h3>${p.displayName || p.name}</h3><p>${p.description}</p>${p.preview ? `<div class="install-cta design-cta"><div class="design-platform-buttons"><button class="install-link" type="button" data-open-codex="${p.name}" data-open-type="design" data-codex-url="${p.codexUrl}" data-design-md="${p.designMdUrl}" data-contract="${p.contractUrl}" data-source="${p.source}">Abrir diseño en Codex</button><button class="install-link claude-link" type="button" data-open-claude-design="${p.name}" data-design-md="${p.designMdUrl}" data-contract="${p.contractUrl}" data-source="${p.source}">Abrir diseño en Claude</button></div><span class="install-status" role="status" aria-live="polite"></span></div><div class="card-footer"><span class="version">v${p.version} · ${p.capabilities.join(' · ')}</span><button class="card-link preview-link" type="button" data-preview="${p.preview}" data-title="${p.displayName || p.name}">Ver preview ↗</button></div>` : `<div class="platform-install-links"><button class="install-link claude-link" type="button" data-open-claude="${p.name}" data-claude-marketplace="${p.claudeMarketplace}">Copiar para Claude Code</button><button class="install-link" type="button" data-open-codex="${p.name}" data-codex-url="${p.codexUrl}">Abrir en Codex</button><span class="install-status" role="status" aria-live="polite"></span></div><div class="card-footer"><span class="version">v${p.version} · ${p.capabilities.join(' · ')}</span><span class="card-links"><a class="card-link" href="./plugins/${p.name}/">Enlace directo ↗</a><a class="card-link" href="${p.url}" target="_blank" rel="noreferrer">GitHub ↗</a></span></div>`}</article>`).join('');
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
