---
name: git-pr-workflow
description: >-
  Use this skill when executing the 6-stage development lifecycle, branching, staging files selectively,
  committing changes, pushing to origin, and opening a Pull Request via GitHub CLI (gh pr create).
---

# Git & PR Workflow Skill

## 6-Stage Development Lifecycle

1. **Analysis & Context:** Inspect target sections (`#hero`, `#about`, `#moderation`, `#kontakt`), CSS cascade in `css/katrin.css`, or metadata using `grep` and bounded `read_file` slices.
2. **Architecture & Design:** Ensure pure Vanilla JS (`js/custom.js`, `sw.js`) and Bootstrap 5 + `css/katrin.css` overrides.
3. **Branch Isolation:** Create a descriptive branch from `master` (`feature/<slug>`, `fix/<slug>`, or `chore/<slug>`):
   ```bash
   git checkout -b <branch-name>
   ```
4. **Implementation & Inner Loop:** Apply surgical `edit_file` changes, update `sitemap.xml` `<lastmod>` if pages change, and validate continuously:
   ```bash
   ./test.sh --fast
   ```
5. **Quality Gate (Outer Loop):** Run the full test suite and verify 0 errors across all 25 HTTP endpoints:
   ```bash
   ./test.sh
   ```
6. **Selective Staging, Commit & Automated PR:**
   ```bash
   git add <file1> <file2>
   git commit -m "<type>: <concise imperative summary>"
   git push -u origin <branch-name>
   ```
   Open the Pull Request via GitHub CLI following `.github/pull_request_template.md`:
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
