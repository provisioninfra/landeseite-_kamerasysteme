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

  /* Jahr im Footer */
  var jahr = document.getElementById('jahr');
  if (jahr) jahr.textContent = String(new Date().getFullYear());

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
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && !mobileNav.hasAttribute('hidden')) {
        mobileNav.setAttribute('hidden', ''); toggle.setAttribute('aria-expanded', 'false'); toggle.focus();
      }
    });
    mobileNav.querySelectorAll('a').forEach(function (a) {
      a.addEventListener('click', function () { mobileNav.setAttribute('hidden', ''); toggle.setAttribute('aria-expanded', 'false'); });
    });
  }

  /* Ablauf: Lottie-Timeline an den Scroll binden (wie Elementor bind_to_scroll, Viewport 0–100 %).
     Bibliothek und Animationsdaten werden erst geladen, wenn die Sektion in die Nähe kommt. */
  var lottieBox = document.querySelector('.ablauf__lottie');
  var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var loadScript = function (src, cb) {
    var el = document.createElement('script');
    el.src = src; el.async = true;
    el.onload = function () { cb(null); };
    el.onerror = function () { cb(new Error('Laden fehlgeschlagen: ' + src)); };
    document.head.appendChild(el);
  };
  var initLottie = function () {
    if (!window.lottie || !window.ABLAUF_TIMELINE) { lottieBox.classList.add('is-failed'); return; }
    var anim;
    try {
      anim = window.lottie.loadAnimation({
        container: lottieBox, renderer: 'svg', loop: false, autoplay: false,
        animationData: window.ABLAUF_TIMELINE,
        rendererSettings: { preserveAspectRatio: 'xMidYMid meet' }
      });
    } catch (e) { lottieBox.classList.add('is-failed'); return; }
    var ticking = false;
    var update = function () {
      ticking = false;
      var r = lottieBox.getBoundingClientRect();
      var vh = window.innerHeight || document.documentElement.clientHeight;
      var p = (vh - r.top) / (vh + r.height);      // 0 = Element erscheint unten, 1 = Element verlässt oben
      p = Math.max(0, Math.min(1, p));
      var total = anim.totalFrames || 0;
      if (total) anim.goToAndStop(Math.round(p * (total - 1)), true);
    };
    var onScroll = function () { if (!ticking) { ticking = true; window.requestAnimationFrame(update); } };
    anim.addEventListener('data_failed', function () { lottieBox.classList.add('is-failed'); });
    anim.addEventListener('DOMLoaded', function () {
      if (reduce) { anim.goToAndStop(anim.totalFrames - 1, true); return; }
      update();
      window.addEventListener('scroll', onScroll, { passive: true });
      window.addEventListener('resize', onScroll);
    });
  };
  if (lottieBox && getComputedStyle(lottieBox).display !== 'none') {
    var started = false;
    var startLottie = function () {
      if (started) return; started = true;
      loadScript(lottieBox.getAttribute('data-lottie-lib'), function (err) {
        if (err) { lottieBox.classList.add('is-failed'); return; }
        loadScript(lottieBox.getAttribute('data-lottie-data'), function (err2) {
          if (err2) { lottieBox.classList.add('is-failed'); return; }
          initLottie();
        });
      });
    };
    if ('IntersectionObserver' in window) {
      var lio = new IntersectionObserver(function (entries) {
        if (entries.some(function (e) { return e.isIntersecting; })) { lio.disconnect(); startLottie(); }
      }, { rootMargin: '800px 0px' });
      lio.observe(lottieBox);
    } else { startLottie(); }
  }

  /* Ablauf: Einblendung der Texte (fadeInDown / fadeInUp) */
  var reveals = document.querySelectorAll('.reveal');
  if (reveals.length) {
    if (reduce || !('IntersectionObserver' in window)) {
      reveals.forEach(function (el) { el.classList.add('is-visible'); });
    } else {
      var io = new IntersectionObserver(function (entries) {
        entries.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add('is-visible'); io.unobserve(e.target); } });
      }, { threshold: 0.2 });
      reveals.forEach(function (el) { io.observe(el); });
    }
  }

  /* Ablauf mobil: Linie füllt sich beim Scrollen, Kreise werden gelb */
  var timeline = document.querySelector('.timeline');
  if (timeline) {
    var items = timeline.querySelectorAll('.timeline__item');
    var tTick = false;
    var tUpdate = function () {
      tTick = false;
      var r = timeline.getBoundingClientRect();
      var vh = window.innerHeight || document.documentElement.clientHeight;
      var line = vh * 0.6;                           // Füllstand: Punkt bei 60 % der Bildschirmhöhe
      var h = Math.max(0, Math.min(r.height, line - r.top));
      timeline.style.setProperty('--tl-fill', h + 'px');
      items.forEach(function (it) {
        var d = it.querySelector('.timeline__dot').getBoundingClientRect();
        it.classList.toggle('is-active', d.top + d.height / 2 <= line);
      });
    };
    var tScroll = function () { if (!tTick) { tTick = true; window.requestAnimationFrame(tUpdate); } };
    if (reduce) {
      timeline.style.setProperty('--tl-fill', '100%');
      items.forEach(function (it) { it.classList.add('is-active'); });
    } else {
      tUpdate();
      window.addEventListener('scroll', tScroll, { passive: true });
      window.addEventListener('resize', tScroll);
    }
  }
})();
