---
name: pr-automation
description: Pushes feature/fix branch to remote origin and opens a structured Pull Request autonomously using GitHub CLI.
---

# Pull Request Automation Skill

Use this skill when local validation (Stage 5) passes and changes are ready to be proposed as a Pull Request (Stage 6).

## Execution Steps

1. **Verify Local Quality Gate:**
   ```bash
   ./test.sh
   ```

2. **Stage and Commit Changes:**
   ```bash
   git add <files>
   git commit -m "<type>(<scope>): <concise description>"
   ```

3. **Push Branch to Origin:**
   ```bash
   git push -u origin <branch-name>
   ```

4. **Create Pull Request via GitHub CLI:**
   ```bash
   gh pr create --base master --head <branch-name> --title "<title>" --body "## Summary of Changes
- <bullet point changes>

## Core Web Vitals & Technical Quality Checklist
- [x] **LCP / Image Optimization:** Verified via test suite.
- [x] **No CLS:** Responsive layout and dimension rules verified.
- [x] **JavaScript:** Pure Vanilla JS confirmed.
- [x] **Structured Data:** Valid JSON-LD Schema.org markup confirmed.
- [x] **Accessibility (a11y):** ARIA and external link attributes confirmed.
- [x] **Automated Test Run:** Local validation executed and passed (\`./test.sh\`)."
   ```
