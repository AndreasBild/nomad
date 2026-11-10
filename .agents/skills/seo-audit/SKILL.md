---
name: seo-audit
description: >-
  Use this skill when auditing or updating SEO metadata, robots.txt, sitemap.xml, llms.txt,
  canonical URLs, Open Graph / Twitter Card tags, or Schema.org JSON-LD structured data.
---

# SEO & Structured Data Audit Skill

## Audit Checklist

1. **Crawler & AI Discovery Files (Root Directory):**
   - `/robots.txt`: Must allow crawling and reference `Sitemap: https://www.moderatorin-katrin-neumann.de/sitemap.xml`.
   - `/sitemap.xml` & `/sitemap.xsl`: Must list all canonical URLs (`/`, `/impressum.html`, `/datenschutz.html`) with up-to-date `<lastmod>` ISO dates.
   - `/llms.txt` & `/llms-full.txt`: Keep synchronized when biography, moderation topics, or contact details change.

2. **HTML Head Metadata & Social Cards:**
   - Every page requires a unique `<title>`, `<meta name="description">`, `<link rel="canonical">`, `<meta name="date-created">`, and `<meta name="build-date">`.
   - Open Graph (`og:title`, `og:description`, `og:image`, `og:url`, `og:type`, `og:locale`) and Twitter Card (`twitter:card`, `twitter:title`, `twitter:description`, `twitter:image`) tags must stay aligned with canonical metadata.

3. **Schema.org JSON-LD (`<script type="application/ld+json">`):**
   - `index.html`: Valid `@graph` containing `Person`, `WebSite`, and `VideoObject` entities.
   - `impressum.html` & `datenschutz.html`: Valid `BreadcrumbList` schema.
   - Run `./test.sh --fast` after any edit to verify XML and JSON-LD parsing.
