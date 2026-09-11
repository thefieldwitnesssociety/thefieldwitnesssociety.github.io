(() => {
  const header = document.querySelector('.site-header');
  const button = document.querySelector('.menu-toggle');
  const nav = document.querySelector('#main-navigation');
  if (!header || !button || !nav) return;
  const compact = window.matchMedia('(max-width: 860px)');
  const setOpen = (open, focus = false) => {
    button.setAttribute('aria-expanded', String(open));
    button.setAttribute('aria-label', open ? 'Close navigation' : 'Open navigation');
    header.classList.toggle('nav-open', open);
    if (focus) button.focus();
  };
  header.dataset.enhanced = 'true';
  button.hidden = false;
  button.addEventListener('click', () => setOpen(button.getAttribute('aria-expanded') !== 'true'));
  header.addEventListener('keydown', event => {
    if (event.key === 'Escape' && button.getAttribute('aria-expanded') === 'true') setOpen(false, true);
  });
  document.addEventListener('click', event => {
    if (!header.contains(event.target)) setOpen(false);
  });
  nav.addEventListener('click', event => {
    if (event.target.closest('a')) setOpen(false);
  });
  compact.addEventListener('change', () => setOpen(false));
})();
