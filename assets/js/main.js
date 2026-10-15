/* ProVision Infra – Kamera- & Videoüberwachung
   Hero-Video: Verhalten wie der Elementor-Video-Hintergrund der Liveseite
   (autoplay, stumm, einmalig, auch mobil, stoppt bei data-video-end Sekunden). */
(function () {
  var hero = document.querySelector('.hero');
  if (!hero) return;

  var video = hero.querySelector('.hero__video');
  var src = hero.getAttribute('data-video');
  var end = parseFloat(hero.getAttribute('data-video-end')) || 0;

  if (video && src) {
    video.muted = true;
    video.playsInline = true;
    video.autoplay = true;
    video.loop = false;

    video.addEventListener('loadeddata', function () {
      hero.classList.add('has-video');
      var p = video.play();
      if (p && p.catch) p.catch(function () { hero.classList.remove('has-video'); });
    });
    video.addEventListener('error', function () { hero.classList.remove('has-video'); });

    if (end > 0) {
      video.addEventListener('timeupdate', function () {
        if (video.currentTime >= end) { video.pause(); }
      });
    }
    video.addEventListener('ended', function () { video.pause(); });

    // Datei nur laden, wenn sie wirklich existiert – sonst bleibt die SVG-Szene sichtbar.
    fetch(src, { method: 'HEAD' }).then(function (r) {
      if (r.ok) { video.src = src; video.load(); }
    }).catch(function () { /* kein Video vorhanden: SVG-Szene bleibt */ });
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
