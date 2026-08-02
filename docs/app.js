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
  grid.innerHTML = visible.map(p => `<article class="plugin-card ${p.preview ? 'analysis-card' : ''}"><div class="card-top"><div class="plugin-icon" aria-hidden="true">${p.icon}</div><span class="badge">${p.category}</span></div><h3>${p.displayName || p.name}</h3><p>${p.description}</p>${p.preview ? `<div class="install-cta design-cta"><div class="design-platform-buttons"><button class="install-link" type="button" data-open-codex="${p.name}" data-open-type="design" data-codex-url="${p.codexUrl}" data-design-md="${p.designMdUrl}" data-contract="${p.contractUrl}" data-source="${p.source}">Abrir diseño en Codex</button><button class="install-link claude-link" type="button" data-open-claude-design="${p.name}" data-design-md="${p.designMdUrl}" data-contract="${p.contractUrl}" data-source="${p.source}">Abrir diseño en Claude</button></div><span class="install-status" role="status" aria-live="polite"></span></div><div class="card-footer"><span class="version">v${p.version} · ${p.capabilities.join(' · ')}</span><button class="card-link preview-link" type="button" data-preview="${p.preview}" data-title="${p.displayName || p.name}">Ver preview ↗</button></div>` : `<div class="platform-install-links"><button class="install-link claude-link" type="button" data-open-claude="${p.name}" data-claude-marketplace="${p.claudeMarketplace}">Copiar para Claude Code</button><button class="install-link" type="button" data-open-codex="${p.name}" data-codex-url="${p.codexUrl}">Abrir en Codex</button><span class="install-status" role="status" aria-live="polite"></span></div><div class="card-footer"><span class="version">v${p.version} · ${p.capabilities.join(' · ')}</span><a class="card-link" href="${p.url}" target="_blank" rel="noreferrer">GitHub ↗</a></div>`}</article>`).join('');
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
document.querySelectorAll('.filter').forEach(button => button.addEventListener('click', () => { document.querySelector('.filter.active').classList.remove('active'); button.classList.add('active'); category = button.dataset.category; render(); }));
document.querySelectorAll('[data-platform-command]').forEach(button => button.addEventListener('click', () => {
  document.querySelectorAll('[data-platform-command]').forEach(item => item.classList.remove('active'));
  button.classList.add('active');
  document.querySelector('#install-command').textContent = button.dataset.platformCommand === 'claude'
    ? `claude plugin marketplace add MauricioPerera/thehumanintheloop-marketplace-codex\nclaude plugin install linter-seo-geo-2026@thehumanintheloop-marketplace-claude`
    : `codex plugin marketplace add MauricioPerera/thehumanintheloop-marketplace-codex\ncodex plugin install linter-seo-geo-2026`;
}));
document.querySelector('#copy-command').addEventListener('click', async () => { const text = document.querySelector('#install-command').textContent; try { await navigator.clipboard.writeText(text); document.querySelector('#copy-status').textContent = 'Copiado'; } catch { document.querySelector('#copy-status').textContent = 'Selecciona y copia el comando'; } });
render();
