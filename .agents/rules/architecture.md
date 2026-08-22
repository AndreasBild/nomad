---
description: Architectural guidelines and technology stack constraints for the Nomad project
trigger: always_on
---

# Architecture & Code Rules

1. **No External Frameworks / Vanilla JavaScript Only:**
   - Do NOT introduce jQuery, React, Vue, or heavy dependencies.
   - All custom logic resides in `js/custom.js` written in pure modern Vanilla JavaScript (ES6+).
   - Use native Browser APIs (DOM API, `IntersectionObserver`, `fetch`, Bootstrap 5 JS components).

2. **Modular & Streamlined CSS:**
   - Base framework: Bootstrap 5 (`css/bootstrap.min.css`).
   - Theme styling: `css/templatemo-nomad-force.css`.
   - Custom tweaks: `css/katrin.css`. Do NOT duplicate Bootstrap classes or reset rules into `katrin.css`.
   - Ensure responsive design works across mobile (320px+), tablet (768px+), and desktop (1200px+).

3. **Asset Organization:**
   - All images in `/images/`.
   - All CSS in `/css/`.
   - All JS in `/js/`.
   - SEO and Crawler files (`robots.txt`, `sitemap.xml`, `sitemap.xsl`) strictly in the root directory.
