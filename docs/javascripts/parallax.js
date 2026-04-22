/* AetherSDR landing-page parallax.
   Sets a CSS custom property --parallax-y on each layer so CSS can
   compose it with whatever centering transforms it already has.
   Respects prefers-reduced-motion. ~30 lines, no dependencies. */

(function () {
  'use strict';

  const reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (reduced) return;

  const layers = document.querySelectorAll('[data-parallax-speed]');
  if (!layers.length) return;

  let ticking = false;

  function update() {
    const scrollY = window.scrollY || window.pageYOffset || 0;
    layers.forEach(function (layer) {
      const speed = parseFloat(layer.dataset.parallaxSpeed) || 0.5;
      const offset = scrollY * speed;
      layer.style.setProperty('--parallax-y', offset + 'px');
    });
    ticking = false;
  }

  function onScroll() {
    if (!ticking) {
      window.requestAnimationFrame(update);
      ticking = true;
    }
  }

  // Initial paint + scroll listener
  update();
  window.addEventListener('scroll', onScroll, { passive: true });
  window.addEventListener('resize', onScroll, { passive: true });
})();
