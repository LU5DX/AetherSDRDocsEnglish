/* AetherSDR landing-page parallax — Material-inspired.

   Each layer has data-parallax-speed where:
     speed < 1  → layer drifts slower than scroll (background depth)
     speed = 1  → layer moves at scroll speed (no parallax)
     speed > 1  → layer moves faster than scroll (foreground escape)

   Math: when the page scrolls down by `scrollY`, an element in document
   flow naturally appears to shift up by scrollY (in viewport coords).
   We add a transform offset to make its apparent motion match the
   target speed:

     apparent_motion_up = scrollY * speed
     transform_offset_up = apparent_motion_up - natural_motion_up
                         = scrollY * speed - scrollY
                         = scrollY * (speed - 1)
     translateY = -transform_offset_up   (positive translateY shifts down)
                = scrollY * (1 - speed)

   So:
     speed 0.3 → translateY = +0.7 * scrollY → element shifts DOWN as you
                 scroll DOWN, partially cancelling natural scroll = slow drift
     speed 1.7 → translateY = -0.7 * scrollY → element shifts UP, on top
                 of natural scroll = fast escape upward

   Hooks into Material's `document$` observable so it survives instant
   navigation. Respects prefers-reduced-motion.
*/

(function () {
  'use strict';

  let attached = false;

  function update() {
    const scrollY = window.scrollY || window.pageYOffset || 0;

    // data-parallax-speed: for elements in document flow (e.g. inside the
    // hero). Formula: translateY = scrollY * (1 - speed)
    //   speed 0   → element appears stuck in viewport
    //   speed 1   → moves with scroll (no parallax)
    //   speed >1  → moves faster than scroll (rises out of view)
    document.querySelectorAll('[data-parallax-speed]').forEach(function (el) {
      const speed = parseFloat(el.dataset.parallaxSpeed);
      if (Number.isNaN(speed)) return;
      const offset = scrollY * (1 - speed);
      el.style.setProperty('--parallax-y', offset + 'px');
    });

    // data-parallax-drift: for FIXED-position elements that need to
    // slowly drift up out of the viewport as the page scrolls. Formula:
    // translateY = -scrollY * drift
    //   drift 0   → no movement
    //   drift 0.2 → drifts up at 20% of scroll = visible for ~5 viewports
    //   drift 0.5 → drifts up at half scroll speed = visible for ~2 viewports
    document.querySelectorAll('[data-parallax-drift]').forEach(function (el) {
      const drift = parseFloat(el.dataset.parallaxDrift);
      if (Number.isNaN(drift)) return;
      const offset = -scrollY * drift;
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
    if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
      console.log('[aether-parallax] prefers-reduced-motion — disabled');
      return;
    }
    const layers = document.querySelectorAll('[data-parallax-speed], [data-parallax-drift]');
    console.log('[aether-parallax] init —', layers.length, 'layer(s)');
    update();
    if (!attached) {
      window.addEventListener('scroll', onScroll, { passive: true });
      window.addEventListener('resize', onScroll, { passive: true });
      attached = true;
      console.log('[aether-parallax] scroll listener attached');
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
