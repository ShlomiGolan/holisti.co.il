document.addEventListener('DOMContentLoaded', () => {
  const toggle = document.querySelector('.nav-toggle');
  const links = document.querySelector('.nav-links');
  if (toggle && links) {
    toggle.addEventListener('click', () => {
      const open = links.classList.toggle('open');
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
    links.querySelectorAll('a').forEach(a => {
      a.addEventListener('click', () => links.classList.remove('open'));
    });
  }

  // Accessibility widget: text size steps + stop-animations toggle
  const a11yToggle = document.getElementById('a11yToggle');
  const a11yPanel = document.getElementById('a11yPanel');
  const a11yTextInc = document.getElementById('a11yTextInc');
  const a11yTextDec = document.getElementById('a11yTextDec');
  const a11yTextReset = document.getElementById('a11yTextReset');
  const a11yMotion = document.getElementById('a11yMotion');
  const TEXT_CLASSES = ['a11y-text-1', 'a11y-text-2', 'a11y-text-3'];

  function applyTextStep(step) {
    document.documentElement.classList.remove(...TEXT_CLASSES);
    if (step > 0) document.documentElement.classList.add(TEXT_CLASSES[step - 1]);
    localStorage.setItem('a11yTextStep', String(step));
  }

  function applyMotion(off) {
    document.documentElement.classList.toggle('a11y-no-motion', off);
    if (a11yMotion) a11yMotion.setAttribute('aria-pressed', off ? 'true' : 'false');
    localStorage.setItem('a11yNoMotion', off ? '1' : '0');
  }

  let currentStep = Math.min(Math.max(parseInt(localStorage.getItem('a11yTextStep') || '0', 10) || 0, 0), TEXT_CLASSES.length);
  applyTextStep(currentStep);
  applyMotion(localStorage.getItem('a11yNoMotion') === '1');

  if (a11yToggle && a11yPanel) {
    a11yToggle.addEventListener('click', (e) => {
      e.stopPropagation();
      const open = a11yPanel.classList.toggle('open');
      a11yToggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
    document.addEventListener('click', (e) => {
      if (a11yPanel.classList.contains('open') && !a11yPanel.contains(e.target) && !a11yToggle.contains(e.target)) {
        a11yPanel.classList.remove('open');
        a11yToggle.setAttribute('aria-expanded', 'false');
      }
    });
  }
  if (a11yTextInc) a11yTextInc.addEventListener('click', () => {
    currentStep = Math.min(currentStep + 1, TEXT_CLASSES.length);
    applyTextStep(currentStep);
  });
  if (a11yTextDec) a11yTextDec.addEventListener('click', () => {
    currentStep = Math.max(currentStep - 1, 0);
    applyTextStep(currentStep);
  });
  if (a11yTextReset) a11yTextReset.addEventListener('click', () => {
    currentStep = 0;
    applyTextStep(currentStep);
  });
  if (a11yMotion) a11yMotion.addEventListener('click', () => {
    applyMotion(!document.documentElement.classList.contains('a11y-no-motion'));
  });
});
