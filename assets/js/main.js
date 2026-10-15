/* ProVision Infra – Kamera- & Videoüberwachung
   Hero-Video: Verhalten wie der Elementor-Video-Hintergrund der Liveseite
   (autoplay, stumm, einmalig, auch mobil, stoppt bei data-video-end Sekunden). */
(function () {
  var hero = document.querySelector('.hero');
  if (!hero) return;

  var video = hero.querySelector('.hero__video');
  var end = parseFloat(hero.getAttribute('data-video-end')) || 0;

  if (video) {
    video.muted = true;
    video.playsInline = true;
    video.autoplay = true;
    video.loop = false;

    // Video vorhanden: sofort anzeigen (Poster bis zum ersten Frame), SVG-Szene nur bei Ladefehler.
    hero.classList.add('has-video');
    video.addEventListener('loadeddata', function () {
      var p = video.play();
      if (p && p.catch) p.catch(function () { /* Autoplay blockiert: Poster bleibt sichtbar */ });
    });
    // Bei mehreren <source> meldet der Browser den Fehler an der letzten Quelle.
    var sources = video.querySelectorAll('source');
    var fallback = function () { hero.classList.remove('has-video'); };
    video.addEventListener('error', fallback);
    if (sources.length) sources[sources.length - 1].addEventListener('error', fallback);

    if (end > 0) {
      video.addEventListener('timeupdate', function () {
        if (video.currentTime >= end) { video.pause(); }
      });
    }
    video.addEventListener('ended', function () { video.pause(); });

    video.load();
  }

  /* Mobile Navigation */
  var toggle = document.querySelector('.site-nav__toggle');
  var mobileNav = document.getElementById('mobile-nav');
  if (toggle && mobileNav) {
    toggle.addEventListener('click', function () {
      var open = mobileNav.hasAttribute('hidden');
      if (open) mobileNav.removeAttribute('hidden'); else mobileNav.setAttribute('hidden', '');
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
      toggle.setAttribute('aria-label', open ? 'Menü schließen' : 'Menü öffnen');
    });
    mobileNav.querySelectorAll('a').forEach(function (a) {
      a.addEventListener('click', function () { mobileNav.setAttribute('hidden', ''); toggle.setAttribute('aria-expanded', 'false'); });
    });
  }
})();
