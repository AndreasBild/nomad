---
name: quality-gate
description: Executes the complete automated test and validation suite for Nomad, verifying XML schemas, JSON-LD data, asset health, and HTTP 200 endpoint responses.
---

# Quality Gate Skill

Use this skill before committing code or opening a Pull Request to ensure 100% compliance with HTML, schema, asset, and endpoint health standards.

## Validation Steps

1. **Run Complete Validation Suite:**
   ```bash
   ./test.sh
   ```

2. **Direct Python Validator Execution:**
   ```bash
   python3 scripts/validate.py
   ```

3. **Check Output:**
   - Verify Sitemap XML & `robots.txt` are valid.
   - Verify all JSON-LD blocks (`Person`, `BreadcrumbList`) parse with valid schema.
   - Verify all internal anchors (`#hero`, `#about`, `#moderation`, `#kontakt`) and image assets exist.
   - Verify all 25 HTTP endpoints return status 200.
