const themeButton = document.querySelector('[data-theme]');
themeButton.addEventListener('click', () => {
  const dark = document.body.dataset.theme === 'dark';
  document.body.dataset.theme = dark ? 'light' : 'dark';
  themeButton.textContent = dark ? 'Oscuro' : 'Claro';
});
