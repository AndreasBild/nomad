---
description: SEO, Core Web Vitals, and Accessibility rules for the Nomad project
trigger: always_on
---

# SEO, Performance & Accessibility Rules

1. **Core Web Vitals:**
   - **LCP (Largest Contentful Paint):** Preload or set `fetchpriority="high"` on hero images. Avoid render-blocking scripts (use `defer`).
   - **CLS (Cumulative Layout Shift):** Always define explicit `width` and `height` on images or aspect-ratio wrappers.
   - **INP / FID:** Keep JS minimal, avoiding synchronous heavy execution during load.

2. **SEO & Metadata Integrity:**
   - Maintain canonical tags pointing to exact URLs (`https://www.moderatorin-katrin-neumann.de/...`).
   - Keep Open Graph and Twitter Card tags in sync with page title and description.
   - When new pages are added or URLs are updated, update `sitemap.xml` with `<lastmod>` timestamp.

3. **Accessibility (a11y):**
   - Provide descriptive `alt`, `title`, and `aria-label` tags for screen readers.
   - Maintain semantic heading hierarchy (`<h1>` for page title, `<h2>` for sections, `<h3>` for subsections).
   - Ensure focus visible rings are present for keyboard navigation.
