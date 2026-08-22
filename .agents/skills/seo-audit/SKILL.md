---
name: seo-audit
description: Audits SEO configuration, robots.txt, sitemap.xml, canonical tags, and structured data for Nomad.
---

# SEO Audit Skill

Use this skill to audit and ensure high-ranking SEO configuration across all pages.

## Audit Checklist

1. **Robots.txt & Sitemap:**
   - Verify `/robots.txt` exists in root and points to `https://www.moderatorin-katrin-neumann.de/sitemap.xml`.
   - Verify `/sitemap.xml` lists valid URLs (`/`, `/datenschutz.html`, `/impressum.html`).
   - Verify `<lastmod>` timestamps are recent.

2. **Metadata & Open Graph:**
   - Each HTML page must have unique `<title>`, `<meta name="description">`, `<link rel="canonical">`.
   - Open Graph tags (`og:title`, `og:description`, `og:image`, `og:url`) must match canonical data.
   - Twitter Card metadata (`twitter:card`, `twitter:title`, `twitter:description`, `twitter:image`) must be present.

3. **Structured Data:**
   - Index page must contain `application/ld+json` with `@type: Person` or `WebSite`.
   - Subpages must contain `application/ld+json` with `@type: BreadcrumbList`.
