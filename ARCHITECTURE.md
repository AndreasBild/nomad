# Architecture Documentation - Nomad (Katrin Neumann)

This document provides a comprehensive technical overview of the architecture, asset pipeline, styling conventions, and tooling for the **Katrin Neumann Web Application**.

---

## 1. System Overview & Principles

```
                    +--------------------------------+
                    |           Client /             |
                    |     Web Browser / Mobile       |
                    +---------------+----------------+
                                    |
                    +---------------+----------------+
                    |        Static Web Host         |
                    |  (HTTPS, CDN / Web Server)     |
                    +---------------+----------------+
                                    |
          +-------------------------+-------------------------+
          |                         |                         |
+---------v---------+     +---------v---------+     +---------v---------+
|    index.html     |     |  impressum.html   |     | datenschutz.html  |
|  (Landing Page)   |     |  (Legal Notice)   |     | (Privacy Policy)  |
+---------+---------+     +---------+---------+     +---------+---------+
          |                         |                         |
          +-------------------------+-------------------------+
                                    |
          +-------------------------+-------------------------+
          |                         |                         |
+---------v---------+     +---------v---------+     +---------v---------+
|     CSS Layer     |     | JavaScript Layer  |     |   SEO / Config    |
| - bootstrap.min   |     | - bootstrap.bundle|     | - robots.txt      |
| - aos.css         |     | - aos.js          |     | - sitemap.xml     |
| - nomad-force.css |     | - custom.js (ES6) |     | - sitemap.xsl     |
| - katrin.css      |     |                   |     | - webmanifest     |
+-------------------+     +-------------------+     +-------------------+
```

### Core Architecture Principles
1. **Zero Runtime Overhead:** No dynamic server rendering or bloated client frameworks. Standard HTML5 static pages deliver instantaneous response times and maximum reliability.
2. **Modern JavaScript (ES6+):** Pure Vanilla JS architecture without jQuery or obsolete libraries.
3. **Core Web Vitals First:** Optimized LCP (Largest Contentful Paint), zero CLS (Cumulative Layout Shift) with fixed image dimensions, and instant interactivity.

---

## 2. Page & Component Layout

### `index.html` (Single-Page Landing Structure)
- **Hero Section (`#hero`):** Full-bleed banner image (`Katrin-Neumann-Moderatorin.webp`) with zoom/fade animations and title overlay.
- **Navigation Bar (`.navbar`):** Sticky Bootstrap 5 navigation with auto-collapsing mobile menu and smooth offset scrolling.
- **About Section (`#about`):** Split two-column grid introducing background and competencies.
- **Moderation Section (`#moderation`):** Details about news/magazine moderation, panel discussions, and events.
- **Contact Section (`#kontakt`):** Direct email link and Instagram social profile integration.
- **Footer (`.site-footer`):** Copyright notices and links to legal pages.

### `impressum.html` & `datenschutz.html`
- Standalone subpages styled with identical typography and navigation header/footer for seamless user navigation.
- Fully compliant with DSGVO / GDPR and § 18 Abs. 2 MStV regulations.

---

## 3. Asset & Styling Hierarchy

CSS is loaded in strict order to avoid specificity conflicts:
1. `css/bootstrap.min.css`: Base grid, utilities, container, and responsive flexbox rules.
2. `css/aos.css`: Keyframe animations for scroll-triggered reveals.
3. `css/templatemo-nomad-force.css`: Typography, brand colors, navbar aesthetics, and custom hero overlay.
4. `css/katrin.css`: Project-specific refinements (smooth scroll offsets, responsive banner ratio, accessibility focus rings).

---

## 4. Search Engine Optimization (SEO) & Structured Data

- **Robots & Crawling:** `robots.txt` at the root instructs search bots to index the site and references `sitemap.xml`.
- **Sitemap:** XML sitemap includes exact canonical paths, priority weights, and change frequencies.
- **Structured Data:**
  - `index.html`: `Schema.org/Person` defining name, jobTitle, url, image, social links, and description.
  - Subpages: `Schema.org/BreadcrumbList` for clear navigational breadcrumbs in search results.

---

## 5. Developer & IDE Integration (IntelliJ IDEA & Antigravity / Jules)

- **IntelliJ IDEA Run Configuration:** `.idea/runConfigurations/Start_Dev_Server.xml` enables 1-click startup in the IDE.
- **Antigravity Governance & 6-Stage Lifecycle:** `AGENTS.md`, `.agents/rules/`, and `.agents/skills/` enforce the formal 6-stage development lifecycle (Analysis -> Architecture -> Branch Isolation -> Standards Implementation -> Local Quality Gate -> Autonomous PR Creation).
- **Automated Pull Request Workflow:** Autonomous PR creation via GitHub CLI (`gh pr create`) against `master`, triggering CI quality checks prior to automated FTP deployment.
- **Local Dev Server:** Shell script `./start-server.sh` works out-of-the-box on macOS and Linux without external dependencies.


