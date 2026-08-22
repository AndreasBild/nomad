/**
 * Nomad Force - Katrin Neumann Custom Scripts (Vanilla JS)
 */
document.addEventListener('DOMContentLoaded', () => {
    'use strict';

    // 1. Initialize AOS Animations if loaded
    if (typeof AOS !== 'undefined') {
        AOS.init({
            duration: 800,
            easing: 'ease-in-out',
            once: true,
            offset: 50
        });
    }

    // 2. Auto-collapse mobile navbar when clicking nav links
    const navbarCollapse = document.getElementById('navbarNav');
    const navLinks = document.querySelectorAll('.navbar-nav .nav-link');

    navLinks.forEach((link) => {
        link.addEventListener('click', () => {
            if (navbarCollapse && navbarCollapse.classList.contains('show')) {
                if (typeof bootstrap !== 'undefined' && bootstrap.Collapse) {
                    const bsCollapse = bootstrap.Collapse.getInstance(navbarCollapse) || new bootstrap.Collapse(navbarCollapse);
                    bsCollapse.hide();
                } else {
                    navbarCollapse.classList.remove('show');
                }
            }
        });
    });

    // 3. Smooth scrolling for internal anchor links with navbar offset
    const internalLinks = document.querySelectorAll('a[href^="#"]');
    const navbar = document.querySelector('.navbar');

    internalLinks.forEach((link) => {
        link.addEventListener('click', (event) => {
            const hash = link.getAttribute('href');
            if (hash && hash !== '#') {
                const target = document.querySelector(hash);
                if (target) {
                    event.preventDefault();
                    const navHeight = navbar ? navbar.offsetHeight : 70;
                    const elementPosition = target.getBoundingClientRect().top;
                    const offsetPosition = elementPosition + window.pageYOffset - (navHeight - 5);

                    window.scrollTo({
                        top: offsetPosition,
                        behavior: 'smooth'
                    });

                    // Update URL hash without abrupt jumping
                    if (history.pushState) {
                        history.pushState(null, null, hash);
                    } else {
                        location.hash = hash;
                    }
                }
            }
        });
    });
});
