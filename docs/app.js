const plugins = [{
  name: 'linter-seo-geo-2026', category: 'Productivity', icon: '⌁', version: '0.1.0',
  description: 'Analizador estático de artículos para SEO híbrido y GEO con validadores de prepublicación.',
  capabilities: ['SEO', 'GEO', 'Contenido'],
  url: 'https://github.com/MauricioPerera/thehumanintheloop-marketplace-codex/tree/main/plugins/linter-seo-geo-2026'
}];
const grid = document.querySelector('#plugin-grid');
const empty = document.querySelector('#empty-state');
const count = document.querySelector('#result-count');
const search = document.querySelector('#search');
let category = 'all';

function render() {
  const query = search.value.trim().toLowerCase();
  const visible = plugins.filter(p => (category === 'all' || p.category === category) && `${p.name} ${p.description} ${p.capabilities.join(' ')}`.toLowerCase().includes(query));
  count.textContent = visible.length;
  empty.hidden = visible.length !== 0;
  grid.innerHTML = visible.map(p => `<article class="plugin-card"><div class="card-top"><div class="plugin-icon" aria-hidden="true">${p.icon}</div><span class="badge">${p.category}</span></div><h3>${p.name}</h3><p>${p.description}</p><div class="card-footer"><span class="version">v${p.version} · ${p.capabilities.join(' · ')}</span><a class="card-link" href="${p.url}" target="_blank" rel="noreferrer">Ver plugin ↗</a></div></article>`).join('');
}
search.addEventListener('input', render);
document.querySelectorAll('.filter').forEach(button => button.addEventListener('click', () => { document.querySelector('.filter.active').classList.remove('active'); button.classList.add('active'); category = button.dataset.category; render(); }));
document.querySelector('#copy-command').addEventListener('click', async () => { const text = document.querySelector('.code-card code').textContent; try { await navigator.clipboard.writeText(text); document.querySelector('#copy-status').textContent = 'Copiado'; } catch { document.querySelector('#copy-status').textContent = 'Selecciona y copia el comando'; } });
render();
