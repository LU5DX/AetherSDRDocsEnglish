/* AetherSDR landing-page parallax.

   Sets a CSS custom property --parallax-y on each parallax layer based
   on window scroll position. CSS composes that with whatever transforms
   the layer already has.

   Speed semantics: 0 = locked to viewport (no apparent motion),
   1 = scrolls with content (no parallax). Sweet spot is 0.2-0.7.

   Hooks into Material for MkDocs' `document$` observable when present,
   so the script re-initializes on every page navigation under the
   `navigation.instant` feature. Falls back to a normal IIFE on first
   load when document$ isn't ready.

   Respects prefers-reduced-motion.
*/

(function () {
  'use strict';

  function init() {
    if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
      return;
    }

    const layers = document.querySelectorAll('[data-parallax-speed]');
    if (!layers.length) return;

    let ticking = false;

    function update() {
      const scrollY = window.scrollY || window.pageYOffset || 0;
      layers.forEach(function (layer) {
        const speed = parseFloat(layer.dataset.parallaxSpeed) || 0.5;
        // Negative offset so layer drifts UP slower than page (parallax illusion).
        const offset = -scrollY * speed;
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

    update();
    // Remove any prior listener (in case of SPA re-init) before adding.
    window.removeEventListener('scroll', onScroll);
    window.addEventListener('scroll', onScroll, { passive: true });
    window.addEventListener('resize', onScroll, { passive: true });
  }

  // Material for MkDocs (with navigation.instant) exposes document$ — an
  // RxJS-like observable that emits on every page load. Subscribing makes
  // the parallax re-initialize after each instant-nav, otherwise the
  // listener attached on the first page would be the only one.
  if (typeof document$ !== 'undefined' && document$ && typeof document$.subscribe === 'function') {
    document$.subscribe(init);
  } else if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
