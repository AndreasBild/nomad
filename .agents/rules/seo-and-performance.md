---
description: Apply when modifying or auditing Core Web Vitals (LCP, CLS, INP), hero images, SEO meta tags, Open Graph/Twitter cards, sitemap.xml, robots.txt, llms.txt, or Schema.org JSON-LD structured data.
trigger: model_decision
---

# SEO, Performance & Core Web Vitals Rules

1. **Core Web Vitals:**
   - **LCP (Largest Contentful Paint):**
     - Desktop banner: `images/Katrin-Neumann-Moderatorin.webp` (1920x1083).
     - Mobile banner: `images/Katrin-Neumann-Moderatorin-768.webp` (768x433).
     - Set `fetchpriority="high"` and `decoding="async"` on LCP hero images; use `loading="lazy"` and `decoding="async"` on below-the-fold images. Load scripts with `defer`.
   - **CLS (Cumulative Layout Shift):** Always define explicit `width` and `height` attributes on images or CSS `aspect-ratio` containers.
   - **INP (Interaction to Next Paint):** Keep JavaScript minimal, event listeners passive, and avoid synchronous main-thread blocking.

2. **SEO & Metadata Integrity:**
   - Maintain canonical tags pointing to exact URLs (`https://www.moderatorin-katrin-neumann.de/...`).
   - Keep Open Graph (`og:*`) and Twitter Card (`twitter:*`) tags synchronized with page `<title>` and `<meta name="description">`.
   - Update `sitemap.xml` `<lastmod>` whenever page content or URLs change.

3. **Structured Data:**
   - Maintain valid Schema.org JSON-LD (`@graph` with `Person` on `index.html`, `BreadcrumbList` on legal subpages).
