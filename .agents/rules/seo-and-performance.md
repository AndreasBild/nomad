---
description: Performance optimization, Core Web Vitals, and SEO guidelines for the Nomad project
trigger: always_on
---

# SEO, Performance & Core Web Vitals Rules

1. **Core Web Vitals:**
   - **LCP (Largest Contentful Paint):**
     - Desktop banner: `images/Katrin-Neumann-Moderatorin.webp` (1920x1083).
     - Mobile banner: `images/Katrin-Neumann-Moderatorin-768.webp` (768x433).
     - Preload or set `fetchpriority="high"` and `decoding="async"` on hero banner images. Avoid render-blocking scripts (load with `defer`).
   - **CLS (Cumulative Layout Shift):** Always define explicit `width` and `height` attributes on images or use CSS aspect-ratio wrappers.
   - **INP / FID:** Keep JavaScript minimal, event listeners passive, and avoid synchronous heavy execution during load.

2. **SEO & Metadata Integrity:**
   - Maintain canonical tags pointing to exact URLs (`https://www.moderatorin-katrin-neumann.de/...`).
   - Keep Open Graph and Twitter Card tags in sync with page title and description.
   - When new pages are added or URLs are updated, update `sitemap.xml` with current `<lastmod>` timestamp.

3. **Structured Data:**
   - Maintain valid Schema.org JSON-LD (`Person` graph on `index.html`, `BreadcrumbList` on legal pages).
