---
description: Architectural guidelines and technology stack constraints for the Nomad project
trigger: always_on
---

# Architecture & Code Rules

1. **No External Frameworks / Vanilla JavaScript Only:**
   - Strictly **NO jQuery**, React, Vue, or heavy dependencies.
   - All interactive logic resides in `js/custom.js` and `sw.js` written in modern Vanilla JavaScript (ES6+).
   - Leverage native Browser APIs (DOM API, `IntersectionObserver`, `fetch`, Bootstrap 5 JS components).

2. **Modular & Streamlined CSS Hierarchy:**
   - Base framework: Bootstrap 5 (`css/bootstrap.min.css`).
   - Scroll animations: AOS (`css/aos.css`).
   - Theme styling: `css/templatemo-nomad-force.css`.
   - Custom overrides: `css/katrin.css`. Do NOT duplicate Bootstrap classes or reset rules into `katrin.css`.
   - Ensure responsive layout across mobile (320px+), tablet (768px+), and desktop (1200px+).

3. **Asset Organization:**
   - Images in `/images/` (prefer modern `.webp`).
   - Stylesheets in `/css/`.
   - Scripts in `/js/`.
   - SEO and Crawler files (`robots.txt`, `sitemap.xml`, `sitemap.xsl`, `llms.txt`, `llms-full.txt`, `site.webmanifest`) strictly in the root directory.
