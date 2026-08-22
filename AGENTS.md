# Nomad Project - AI Agent & Jules Context Guide

This document defines the architecture, conventions, and workflows for AI agents (Antigravity, Jules, and other AI pair programmers) working on the **Nomad (Katrin Neumann)** repository.

---

## 📌 Project Overview

- **Owner/Brand:** Katrin Neumann – Freie Moderatorin, Journalistin & Medientrainerin (Berlin)
- **Domain:** [https://www.moderatorin-katrin-neumann.de](https://www.moderatorin-katrin-neumann.de)
- **Type:** Ultra-fast, responsive static web presence.

---

## 🛠️ Technology Stack & Constraints

1. **HTML5:** Semantic markup, valid schema, German language (`<html lang="de">`), valid metadata and Open Graph tags.
2. **CSS3:**
   - Framework: Bootstrap 5 (`css/bootstrap.min.css`)
   - Animation: AOS (`css/aos.css`)
   - Custom Theme: `css/templatemo-nomad-force.css`
   - Custom Overrides: `css/katrin.css` (keep minimal, no Bootstrap duplication).
3. **JavaScript:**
   - **Pure Vanilla JS only** (`js/custom.js`).
   - **NO jQuery** or legacy plugins (Magnific Popup, jQuery Sticky, Scrollspy plugin are prohibited).
   - Scripts loaded with `defer` at the bottom of the page:
     ```html
     <script src="js/bootstrap.bundle.min.js" defer></script>
     <script src="js/aos.js" defer></script>
     <script src="js/custom.js" defer></script>
     ```
4. **Structured Data:** JSON-LD (`Schema.org` `Person` on index, `BreadcrumbList` on subpages).

---

## 📂 Directory Structure

```
nomad/
├── index.html              # Main landing page (Hero, About, Moderation, Kontakt)
├── impressum.html          # Legal Notice (Impressum - § 18 Abs. 2 MStV)
├── datenschutz.html        # Privacy Policy (DSGVO / GDPR compliant)
├── robots.txt              # Search engine crawler directives (Root level)
├── sitemap.xml             # XML Sitemap with canonical URLs (Root level)
├── sitemap.xsl             # XSL stylesheet for human-readable sitemap
├── site.webmanifest        # PWA Web Manifest
├── css/
│   ├── bootstrap.min.css   # Bootstrap 5 Core CSS
│   ├── aos.css             # AOS animation styles
│   ├── templatemo-nomad-force.css  # Nomad Force theme styling
│   └── katrin.css          # Custom enhancements & overrides
├── js/
│   ├── bootstrap.bundle.min.js # Bootstrap 5 JS (Collapse, Navbar)
│   ├── aos.js              # AOS scroll animations
│   └── custom.js           # Vanilla JS interactive logic (menu collapse, smooth scroll)
├── images/
│   ├── Katrin-Neumann-Moderatorin.webp  # Hero Banner Image (1920x1083)
│   └── Instagram_logo.png               # Instagram icon (26x26)
├── .agents/                # Antigravity & Jules rules and skills
├── start-server.sh         # Local Python HTTP server launcher
├── ARCHITECTURE.md         # Detailed architectural documentation
└── README.md               # Quickstart and overview
```

---

## ⚡ Performance & Core Web Vitals Rules

1. **Images (LCP & CLS):**
   - Always specify explicit `width` and `height` attributes on `<img>` tags.
   - The hero banner in `index.html` must include `fetchpriority="high"` and `decoding="async"`.
   - Prefer modern web formats (`.webp`).
2. **Navigation Anchors:**
   - Section anchors must match navigation targets: `#hero`, `#about`, `#moderation`, `#kontakt`.
   - Smooth scrolling is handled via native CSS `scroll-behavior: smooth`, `scroll-padding-top: 80px`, and fallback in `js/custom.js`.
3. **Accessibility (a11y):**
   - All interactive elements and links must have descriptive `aria-label` or `title` attributes.
   - External links must include `target="_blank" rel="noopener noreferrer"`.
   - Avoid empty container tags (`<strong></strong>`, `<b></b>`).

---

## 🔄 Development & Local Testing Workflow

### 1. Starting Local Server
```bash
./start-server.sh
# Server starts at http://localhost:8000
```
In IntelliJ IDEA: Run configuration **"Start Dev Server"** is available in the top toolbar.

### 2. Automated Verification Script
Before pushing changes or creating a PR, verify all endpoints:
```bash
python3 -c "
import urllib.request
urls = [
    'http://localhost:8000/',
    'http://localhost:8000/index.html',
    'http://localhost:8000/impressum.html',
    'http://localhost:8000/datenschutz.html',
    'http://localhost:8000/robots.txt',
    'http://localhost:8000/sitemap.xml',
    'http://localhost:8000/css/katrin.css',
    'http://localhost:8000/js/custom.js'
]
for u in urls:
    urllib.request.urlopen(u)
print('All endpoints verified!')
"
```

### 3. Git Workflow
- Branch naming: `feature/<feature-name>`, `fix/<bug-description>`
- Commit messages: Imperative mood, clear bullet points describing non-obvious rationale.
