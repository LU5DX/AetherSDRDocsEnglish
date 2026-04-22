/* AetherSDR landing-page parallax.

   Sets a CSS custom property --parallax-y on each parallax layer based
   on window scroll position. CSS composes that with whatever transforms
   the layer already has.

   Speed semantics: 0 = no parallax (moves with page),
                    1 = stays fixed in viewport.
   Sweet spot is 0.3-0.7 for visible drift.

   Hooks into Material for MkDocs' `document$` observable when present,
   so the script re-initializes on every page navigation under the
   `navigation.instant` feature. Falls back to a normal IIFE on first
   load when document$ isn't ready.

   Respects prefers-reduced-motion.
*/

(function () {
  'use strict';

  let initialized = false;

  function init() {
    if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
      console.log('[aether-parallax] reduced motion preferred — skipping');
      return;
    }

    const layers = document.querySelectorAll('[data-parallax-speed]');
    console.log('[aether-parallax] init — found', layers.length, 'layer(s)');
    if (!layers.length) return;

    function update() {
      const scrollY = window.scrollY || window.pageYOffset || 0;
      layers.forEach(function (layer) {
        const speed = parseFloat(layer.dataset.parallaxSpeed) || 0.5;
        const offset = -scrollY * speed;
        layer.style.setProperty('--parallax-y', offset + 'px');
      });
    }

    let ticking = false;
    function onScroll() {
      if (!ticking) {
        window.requestAnimationFrame(function () {
          update();
          ticking = false;
        });
        ticking = true;
      }
    }

    update();
    if (!initialized) {
      window.addEventListener('scroll', onScroll, { passive: true });
      window.addEventListener('resize', onScroll, { passive: true });
      initialized = true;
      console.log('[aether-parallax] scroll listener attached');
    }
  }

  // Material for MkDocs (with navigation.instant) exposes document$ — an
  // observable that emits on every page load. Subscribing makes the
  // parallax re-pick up the layers after instant-nav swaps the page.
  if (typeof document$ !== 'undefined' && document$ && typeof document$.subscribe === 'function') {
    console.log('[aether-parallax] using Material document$ observable');
    document$.subscribe(init);
  } else if (document.readyState === 'loading') {
    console.log('[aether-parallax] waiting for DOMContentLoaded');
    document.addEventListener('DOMContentLoaded', init);
  } else {
    console.log('[aether-parallax] DOM already ready, init now');
    init();
  }
})();
