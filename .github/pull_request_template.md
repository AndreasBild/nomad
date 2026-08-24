## 📌 Pull Request Overview

<!-- Provide a concise description of the changes introduced and rationale -->

### 🎯 Type of Change
- [ ] 🚀 New Feature / Section
- [ ] 🐛 Bugfix / Layout Correction
- [ ] ⚡ Performance & Core Web Vitals Optimization
- [ ] 📝 Documentation & Agent Governance
- [ ] 🔧 Maintenance / CI/CD

---

## 📝 Summary of Changes
- 

---

## 🛡️ 6-Stage Quality Gate Checklist
- [ ] **Stage 1 (Context & Scope):** Change scope clearly mapped to semantic HTML, legal subpages, or assets.
- [ ] **Stage 2 (Architecture & Zero-Bloat):** Pure Vanilla JS only (`js/custom.js`), zero jQuery/legacy plugins. Styles isolated in `css/katrin.css`.
- [ ] **Stage 3 (Branch Isolation):** Isolated feature/fix branch created from latest `master`.
- [ ] **Stage 4 (Core Web Vitals & a11y):**
  - [ ] Explicit `width`/`height` on images; hero banner has `fetchpriority="high"`.
  - [ ] Valid Schema.org JSON-LD structured data (`@graph` / `Person` / `BreadcrumbList`).
  - [ ] WCAG AA a11y attributes (`aria-label`, `title`, `rel="noopener noreferrer"` on external links).
- [ ] **Stage 5 (Local Verification):** Full test suite passed (`./test.sh` - 0 errors across all 25 endpoints).
- [ ] **Stage 6 (CI & Deployment):** PR triggers `.github/workflows/ci.yml`; merge to `master` deploys to webhoster.de.
