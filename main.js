/* ===================================================
   Tolga Oto Boya — main.js
   =================================================== */

document.addEventListener('DOMContentLoaded', () => {

  /* ── 1. SCROLL PROGRESS BAR ── */
  const progressBar = document.getElementById('scroll-progress');
  window.addEventListener('scroll', () => {
    const scrolled = window.scrollY;
    const total = document.documentElement.scrollHeight - window.innerHeight;
    const pct = total > 0 ? (scrolled / total) * 100 : 0;
    if (progressBar) progressBar.style.width = pct + '%';
  }, { passive: true });

  /* ── 2. NAVBAR SCROLL EFFECT ── */
  const navbar = document.getElementById('navbar');
  window.addEventListener('scroll', () => {
    if (navbar) {
      navbar.classList.toggle('scrolled', window.scrollY > 60);
    }
  }, { passive: true });

  /* ── 3. MOBILE MENU ── */
  const hamburger = document.getElementById('hamburger');
  const mobileMenu = document.getElementById('mobileMenu');
  if (hamburger && mobileMenu) {
    hamburger.addEventListener('click', () => {
      mobileMenu.classList.toggle('open');
      const isOpen = mobileMenu.classList.contains('open');
      hamburger.setAttribute('aria-expanded', isOpen);
      // Animate hamburger lines
      const spans = hamburger.querySelectorAll('span');
      if (isOpen) {
        spans[0].style.transform = 'rotate(45deg) translate(5px, 5px)';
        spans[1].style.opacity = '0';
        spans[2].style.transform = 'rotate(-45deg) translate(5px, -5px)';
      } else {
        spans[0].style.transform = '';
        spans[1].style.opacity = '';
        spans[2].style.transform = '';
      }
    });

    // Close on link click
    mobileMenu.querySelectorAll('a').forEach(link => {
      link.addEventListener('click', () => {
        mobileMenu.classList.remove('open');
        hamburger.setAttribute('aria-expanded', 'false');
        const spans = hamburger.querySelectorAll('span');
        spans[0].style.transform = '';
        spans[1].style.opacity = '';
        spans[2].style.transform = '';
      });
    });
  }

  /* ── 4. SCROLL REVEAL (IntersectionObserver) ── */
  const revealObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
        revealObserver.unobserve(entry.target);
      }
    });
  }, { threshold: 0.07, rootMargin: '0px 0px -40px 0px' });

  document.querySelectorAll('.reveal').forEach(el => revealObserver.observe(el));

  /* ── 5. ANIMATED COUNTERS ── */
  function animateCounter(el, target, duration = 1800) {
    let start = 0;
    const step = (timestamp) => {
      if (!start) start = timestamp;
      const progress = Math.min((timestamp - start) / duration, 1);
      const eased = 1 - Math.pow(1 - progress, 3);
      el.textContent = Math.floor(eased * target);
      if (progress < 1) requestAnimationFrame(step);
      else el.textContent = target;
    };
    requestAnimationFrame(step);
  }

  const counterObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const el = entry.target;
        const target = parseInt(el.dataset.target, 10);
        const suffix = el.dataset.suffix || '';
        animateCounter(el, target);
        el.addEventListener('_done', () => { el.textContent = target + suffix; }, { once: true });
        // add suffix after animation
        setTimeout(() => {
          el.textContent = target + suffix;
        }, 1900);
        counterObserver.unobserve(el);
      }
    });
  }, { threshold: 0.5 });

  document.querySelectorAll('[data-target]').forEach(el => counterObserver.observe(el));

  /* ── 6. GALLERY FILTER ── */
  document.querySelectorAll('.filter-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');

      const filter = btn.dataset.filter;
      document.querySelectorAll('.gallery-item').forEach(item => {
        if (filter === 'all' || item.dataset.category === filter) {
          item.style.display = '';
          item.style.opacity = '0';
          item.style.transform = 'scale(0.94)';
          setTimeout(() => {
            item.style.opacity = '1';
            item.style.transform = 'scale(1)';
          }, 60);
        } else {
          item.style.display = 'none';
        }
      });
    });
  });

  /* ── 7. LIGHTBOX ── */
  const lightbox    = document.getElementById('lightbox');
  const lbImg       = document.getElementById('lightboxImg');
  const lbCaption   = document.getElementById('lightboxCaption');
  const lbClose     = document.getElementById('lbClose');
  const lbPrev      = document.getElementById('lbPrev');
  const lbNext      = document.getElementById('lbNext');

  const galleryItems = [...document.querySelectorAll('.gallery-item')];
  let currentIdx = 0;

  function getVisibleItems() {
    return galleryItems.filter(item => item.style.display !== 'none');
  }

  window.openLightbox = function(idx) {
    currentIdx = idx;
    const visible = getVisibleItems();
    if (!visible[idx]) return;
    const img = visible[idx].querySelector('img');
    if (!img) return;
    lbImg.src = img.src;
    lbCaption.textContent = img.alt;
    lightbox.classList.add('active');
    document.body.style.overflow = 'hidden';
  };

  function closeLightbox() {
    lightbox.classList.remove('active');
    document.body.style.overflow = '';
  }

  function showLightboxImg(idx) {
    const visible = getVisibleItems();
    const total = visible.length;
    if (total === 0) return;
    currentIdx = ((idx % total) + total) % total;
    const img = visible[currentIdx].querySelector('img');
    if (!img) return;
    lbImg.style.opacity = '0';
    setTimeout(() => {
      lbImg.src = img.src;
      lbCaption.textContent = img.alt;
      lbImg.style.opacity = '1';
    }, 180);
  }

  if (lbImg) lbImg.style.transition = 'opacity 0.18s ease';
  if (lbClose) lbClose.addEventListener('click', closeLightbox);
  if (lbPrev)  lbPrev.addEventListener('click',  () => showLightboxImg(currentIdx - 1));
  if (lbNext)  lbNext.addEventListener('click',  () => showLightboxImg(currentIdx + 1));

  lightbox?.addEventListener('click', (e) => {
    if (e.target === lightbox) closeLightbox();
  });

  document.addEventListener('keydown', (e) => {
    if (!lightbox?.classList.contains('active')) return;
    if (e.key === 'Escape')     closeLightbox();
    if (e.key === 'ArrowLeft')  showLightboxImg(currentIdx - 1);
    if (e.key === 'ArrowRight') showLightboxImg(currentIdx + 1);
  });

  // Touch swipe support for lightbox
  let touchStartX = 0;
  lightbox?.addEventListener('touchstart', e => { touchStartX = e.touches[0].clientX; }, { passive: true });
  lightbox?.addEventListener('touchend', e => {
    const dx = e.changedTouches[0].clientX - touchStartX;
    if (Math.abs(dx) > 50) dx < 0 ? showLightboxImg(currentIdx + 1) : showLightboxImg(currentIdx - 1);
  }, { passive: true });

  /* ── 8. SMOOTH ACTIVE NAV LINK ── */
  const sections = document.querySelectorAll('section[id]');
  const navLinks = document.querySelectorAll('.nav-link');

  const sectionObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const id = entry.target.id;
        navLinks.forEach(link => {
          link.classList.toggle('active-nav', link.getAttribute('href') === '#' + id);
        });
      }
    });
  }, { threshold: 0.4 });

  sections.forEach(s => sectionObserver.observe(s));

});
