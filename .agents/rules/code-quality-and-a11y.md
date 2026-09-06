---
description: Code quality, accessibility (a11y), and legal compliance guidelines for the Nomad project
trigger: always_on
---

# Code Quality, Accessibility & Legal Rules

1. **HTML5 Semantic Standards & Document Structure:**
   - Always declare modern HTML5 doctype (`<!doctype html>`) and German language specification (`<html lang="de">`).
   - Include required head elements on every page: `<meta charset="utf-8">`, `<meta name="viewport" content="width=device-width, initial-scale=1">`, `<title>`, `<meta name="description">`, and `<link rel="canonical">`.
   - Maintain a strict semantic landmark structure (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`).
   - Enforce exactly one `<h1>` per page as the top-level landmark; nest `<h2>` and `<h3>` logically without skipping heading levels.
   - All element `id` attributes must be unique across each HTML document (no duplicate IDs).
   - No inline JavaScript (`onclick=...`) or inline CSS `style` attributes; all behaviors live in `js/custom.js` and styles in `css/katrin.css`.

2. **Accessibility (WCAG 2.1 AA Conformance):**
   - Provide descriptive `alt` text on all `<img>` elements (empty `alt=""` only for purely decorative elements with `aria-hidden="true"`).
   - Provide `aria-label` or `title` on icon-only buttons and links.
   - Maintain clear, high-contrast focus visible styles (`:focus-visible`) for keyboard navigation.
   - Touch targets for interactive elements (links, buttons) must meet minimum 48x48px hit areas.
   - External links must include `target="_blank" rel="noopener noreferrer"`.

3. **Core Web Vitals & Image Asset Standards:**
   - Always specify explicit `width` and `height` attributes on all `<img>` tags to eliminate Cumulative Layout Shift (CLS).
   - LCP hero images must include `fetchpriority="high"` and `decoding="async"`.
   - Below-the-fold images must specify `loading="lazy"` and `decoding="async"`.

4. **Code Cleanliness:**
   - Avoid empty container tags (`<strong></strong>`, `<b></b>`, `<span></span>`, `<a></a>`).
   - Validate HTML quotes, attributes, self-closing conventions, and clean nesting.

5. **Legal Compliance (DSGVO / MStV):**
   - Keep `impressum.html` updated and compliant with § 18 Abs. 2 MStV.
   - Keep `datenschutz.html` strictly DSGVO / GDPR compliant with zero unauthorized third-party tracking.

