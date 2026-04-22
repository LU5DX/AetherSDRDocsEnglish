/* AetherSDR landing-page parallax.

   For each element with data-parallax-speed, set --parallax-y based on
   window scroll position. CSS composes that into the element's transform
   so it drifts at a different rate than the page itself.

   Speed semantics (negative shifts up, positive shifts down):
     0   → moves with the page (no parallax effect)
     0.5 → drifts up half as much as the page scrolls = subtle depth
     1   → counters scroll completely = appears stuck in viewport

   Hooks into Material's `document$` observable so it survives instant
   navigation. Respects prefers-reduced-motion.
*/

(function () {
  'use strict';

  let attached = false;

  function update() {
    const scrollY = window.scrollY || window.pageYOffset || 0;
    document.querySelectorAll('[data-parallax-speed]').forEach(function (el) {
      const speed = parseFloat(el.dataset.parallaxSpeed) || 0;
      const offset = -scrollY * speed;
      el.style.setProperty('--parallax-y', offset + 'px');
    });
  }

  let ticking = false;
  function onScroll() {
    if (ticking) return;
    window.requestAnimationFrame(function () { update(); ticking = false; });
    ticking = true;
  }

  function init() {
    if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
    update();
    if (!attached) {
      window.addEventListener('scroll', onScroll, { passive: true });
      window.addEventListener('resize', onScroll, { passive: true });
      attached = true;
    }
  }

  if (typeof document$ !== 'undefined' && document$ && typeof document$.subscribe === 'function') {
    document$.subscribe(init);
  } else if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
