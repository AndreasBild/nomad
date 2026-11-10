---
name: test-suite
description: >-
  Use this skill when validating code changes during development (Fast Inner Loop via ./test.sh --fast)
  or running the full pre-PR regression suite including live HTTP 200 endpoint checks (./test.sh).
---

# Test Suite Skill (Nomad)

## 1. Fast Inner Loop (Active Development)
Run instantaneous (<50ms) static checks without starting a local web server:
```bash
./test.sh --fast
```
*Direct Python invocation:* `python3 scripts/validate.py --fast`

**Coverage:**
- `sitemap.xml`, `sitemap.xsl`, and `robots.txt` XML/directive validity.
- JSON-LD `@graph` (`Person`) and `BreadcrumbList` schema parsing across all `*.html` files.
- Internal anchor integrity (`#id`), local file links, and referenced image/media existence on disk.
- HTML5 & WCAG AA standards: `<!doctype html>`, `lang="de"`, required `<head>` meta tags (`charset`, `viewport`, `title`, `description`, `canonical`, `date-created`, `build-date`), no empty tags, unique IDs, single `<h1>`, explicit `width`/`height` and `alt` on `<img>`, and `rel="noopener noreferrer"` on `target="_blank"`.

## 2. Comprehensive Outer Gate (Pre-Commit / Pre-PR)
Run the full regression suite including the live local HTTP server:
```bash
./test.sh
```
**Coverage:**
- Runs all static checks above.
- Spawns an ephemeral HTTP server on `127.0.0.1` and asserts live `HTTP 200` responses across all 25 production endpoints (HTML pages, CSS/JS bundles, hero WebP/JPG images, sitemaps, `llms.txt`, `llms-full.txt`, and icons).

## Troubleshooting Failures
- **Missing Asset / 404 Anchor:** Verify exact path casing in HTML vs. `/images/` or target `id="..."`.
- **JSON-LD Schema Error:** Validate JSON syntax inside `<script type="application/ld+json">`.
- **HTML5 Validation Error:** Ensure single `<h1>`, unique element IDs, and explicit `width`/`height` on every `<img>`.
