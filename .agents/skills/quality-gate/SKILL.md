---
name: quality-gate
description: Executes the complete automated test and validation suite for Nomad, verifying XML schemas, JSON-LD data, asset health, and HTTP 200 endpoint responses.
---

# Quality Gate Skill

Use this skill to validate changes during active development (Fast Inner Loop) and before committing code or opening a Pull Request (Comprehensive Outer Gate).

## Dual-Loop Validation Steps

### 1. Fast Inner Loop (Active Development)
Run instantaneous (<50ms) static checks during editing:
```bash
./test.sh --fast
```
*Direct python execution:*
```bash
python3 scripts/validate.py --fast
```
Verifies:
- Sitemap XML & `robots.txt` validity.
- JSON-LD blocks (`Person`, `BreadcrumbList`) schema integrity.
- Internal links, section anchors, and referenced static assets.
- HTML5 standards: doctype, lang="de", meta tags, single `<h1>`, unique IDs, explicit image dimensions (`width`/`height`), `alt` tags, and external link security (`rel="noopener noreferrer"`).

### 2. Comprehensive Outer Gate (Pre-Commit / Pre-PR)
Run the full test suite before committing or opening a PR:
```bash
./test.sh
```
*Verifies all static checks above PLUS starts a local TCP server and validates live HTTP 200 responses across all 25 production endpoints.*

