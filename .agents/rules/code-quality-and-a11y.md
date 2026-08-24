---
description: Code quality, accessibility (a11y), and legal compliance guidelines for the Nomad project
trigger: always_on
---

# Code Quality, Accessibility & Legal Rules

1. **Accessibility (WCAG 2.1 AA):**
   - Provide descriptive `alt`, `title`, and `aria-label` tags for assistive technology and screen readers.
   - Maintain strict semantic heading hierarchy (`<h1>` for main title, `<h2>` for sections, `<h3>` for cards/subsections).
   - Ensure focus visible indicators are styled and distinct for keyboard navigation.
   - External links must include `target="_blank" rel="noopener noreferrer"`.

2. **Code Cleanliness:**
   - Avoid empty container tags (`<strong></strong>`, `<b></b>`, `<span></span>`).
   - Keep markup semantic (use `<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`).
   - Validate HTML quotes, attributes, and formatting.

3. **Legal Compliance (DSGVO / MStV):**
   - Keep `impressum.html` updated and compliant with § 18 Abs. 2 MStV.
   - Keep `datenschutz.html` strictly DSGVO / GDPR compliant with zero unauthorized third-party tracking.
