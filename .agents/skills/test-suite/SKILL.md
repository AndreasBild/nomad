---
name: test-suite
description: Executes the Nomad test suite, running static validations and full HTTP 200 endpoint checks.
---

# Test Suite Skill (Nomad)

Use this skill to execute tests during development (Fast Inner Loop) and before opening PRs (Comprehensive Outer Gate).

## Runner Commands

### 1. Fast Inner Loop (Active Development)
Run instantaneous (<50ms) static checks without starting a local web server:
```bash
./test.sh --fast
```
*Direct Python invocation:*
```bash
python3 scripts/validate.py --fast
```
**Coverage:**
- Sitemap XML structure & `robots.txt` directives.
- JSON-LD `@graph` (`Person`) and `BreadcrumbList` schema parsing.
- Internal anchor integrity, local links, and referenced image asset existence.
- HTML5 standards: doctype, `lang="de"`, meta tags, unique IDs, single `<h1>`, explicit `width`/`height` on images, WCAG AA `alt` attributes, and external link `rel="noopener noreferrer"`.

### 2. Comprehensive Outer Gate (Pre-Commit / Pre-PR)
Run full regression suite including the live local HTTP server:
```bash
./test.sh
```
**Coverage:**
- Runs all static checks above.
- Spawns a background HTTP server on port 8000.
- Asserts live HTTP 200 responses across all 25 production endpoints.

## Troubleshooting Failures
- **Missing Asset / 404 Anchor:** Check path casing in HTML vs. filesystem under `/images/` or `/css/`.
- **JSON-LD Schema Error:** Validate JSON syntax inside `<script type="application/ld+json">`.
- **HTML5 Validation Error:** Ensure single `<h1>`, unique element IDs, and explicit `width`/`height` on every `<img>`.
