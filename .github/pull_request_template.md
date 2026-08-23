## Summary of Changes
<!-- Provide a clear description of what this PR introduces or fixes -->

- 

## Core Web Vitals & Technical Quality Checklist
- [ ] **LCP / Image Optimization:** Explicit `width`/`height` specified; hero image has `fetchpriority="high"` and modern `.webp` format.
- [ ] **No CLS:** Layout shifts prevented through responsive aspect-ratio wrappers.
- [ ] **JavaScript:** Pure Vanilla JS only (`js/custom.js`), no jQuery or unnecessary frameworks.
- [ ] **Structured Data:** Valid Schema.org JSON-LD markup (`@graph` / `Person` / `BreadcrumbList`).
- [ ] **Accessibility (a11y):** Valid `aria-label` / `title` attributes on interactive elements and external links (`rel="noopener noreferrer"`).
- [ ] **Automated Test Run:** Local validation executed and passed (`./test.sh`).
