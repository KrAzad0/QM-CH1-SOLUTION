(() => {
  'use strict';

  const root = document.documentElement;
  const toggle = document.getElementById('theme-toggle');
  const cards = [...document.querySelectorAll('.problem-card')];
  const buttons = [...document.querySelectorAll('.filter')];
  const search = document.getElementById('problem-search');
  const empty = document.getElementById('no-results');
  const visibleCount = document.getElementById('visible-count');
  const progress = document.getElementById('reading-progress');
  let activeGroup = 'all';

  try {
    const stored = localStorage.getItem('qm-ch1-theme');
    if (stored === 'light' || stored === 'dark') {
      root.dataset.theme = stored;
    } else if (window.matchMedia?.('(prefers-color-scheme: dark)').matches) {
      root.dataset.theme = 'dark';
    }
  } catch (_) {
    // Preference storage may be unavailable in private browsing mode.
  }

  function setTheme(next) {
    root.dataset.theme = next;
    toggle.setAttribute('aria-label', next === 'light' ? 'Switch to dark theme' : 'Switch to light theme');
    toggle.title = next === 'light' ? 'Switch to dark theme' : 'Switch to light theme';
    try { localStorage.setItem('qm-ch1-theme', next); } catch (_) {}
  }

  setTheme(root.dataset.theme === 'dark' ? 'dark' : 'light');
  toggle.addEventListener('click', () => setTheme(root.dataset.theme === 'light' ? 'dark' : 'light'));

  function filterCards() {
    const term = search.value.trim().toLocaleLowerCase();
    let visible = 0;
    for (const card of cards) {
      const byGroup = activeGroup === 'all' || card.dataset.group === activeGroup;
      const number = Number(card.querySelector('.problem-number').textContent.trim().split(' ')[0]);
      const combined = (card.dataset.terms + ' ' + card.textContent + ' 1.' + number).toLocaleLowerCase();
      const matches = !term || combined.includes(term);
      const show = byGroup && matches;
      card.hidden = !show;
      if (show) visible++;
    }
    empty.hidden = visible > 0;
    visibleCount.textContent = 'Showing ' + visible + ' of ' + cards.length + ' problems';
  }

  search.addEventListener('input', filterCards);
  for (const button of buttons) {
    button.addEventListener('click', () => {
      activeGroup = button.dataset.filter;
      for (const other of buttons) {
        const selected = other === button;
        other.classList.toggle('is-active', selected);
        other.setAttribute('aria-pressed', String(selected));
      }
      filterCards();
    });
  }

  let ticking = false;
  const updateScroll = () => {
    const full = document.documentElement.scrollHeight - window.innerHeight;
    progress.style.width = (full > 0 ? 100 * window.scrollY / full : 100).toFixed(2) + '%';
    ticking = false;
  };
  window.addEventListener('scroll', () => {
    if (!ticking) {
      window.requestAnimationFrame(updateScroll);
      ticking = true;
    }
  }, { passive: true });
  window.addEventListener('resize', updateScroll, { passive: true });
  updateScroll();
  filterCards();
})();
