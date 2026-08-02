(function(){
  const root=document.documentElement;
  const toggle=document.querySelector('[data-theme-toggle]');
  const saved=localStorage.getItem('kdd-dsa-theme');
  if(saved){root.dataset.theme=saved;toggle.textContent=saved==='dark'?'Light':'Dark';}
  toggle.addEventListener('click',function(){
    const next=root.dataset.theme==='dark'?'light':'dark';
    if(next==='light') delete root.dataset.theme; else root.dataset.theme=next;
    localStorage.setItem('kdd-dsa-theme',next); toggle.textContent=next==='dark'?'Light':'Dark';
  });
})();
