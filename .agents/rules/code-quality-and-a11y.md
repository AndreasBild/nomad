---
description: Apply when creating, editing, or auditing HTML markup, CSS styles, DOM landmarks, WCAG 2.1 AA accessibility, images, or legal compliance pages (impressum.html, datenschutz.html).
trigger: model_decision
---

# Code Quality, Accessibility & Legal Rules

1. **HTML5 Semantic Standards & Document Structure:**
   - Declare modern HTML5 doctype (`<!doctype html>`) and German language specification (`<html lang="de">`).
   - Include required `<head>` elements on every page: `<meta charset="utf-8">`, `<meta name="viewport" content="width=device-width, initial-scale=1">`, `<title>`, `<meta name="description">`, `<link rel="canonical">`, `<meta name="date-created">`, and `<meta name="build-date">`.
   - Maintain a strict semantic landmark structure (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`).
   - Enforce exactly one `<h1>` per page; nest `<h2>` and `<h3>` logically without skipping heading levels.
   - All element `id` attributes must be unique across each HTML document.
   - No inline JavaScript (`onclick=...`) or inline CSS `style` attributes; all behaviors live in `js/custom.js` and styles in `css/katrin.css`.

2. **Accessibility (WCAG 2.1 AA Conformance):**
   - Provide descriptive `alt` text on all `<img>` elements (empty `alt=""` only for decorative elements with `aria-hidden="true"`).
   - Provide `aria-label` or `title` on icon-only buttons and links.
   - Maintain high-contrast `:focus-visible` styles for keyboard navigation and minimum 48x48px touch targets.
   - External links must include `target="_blank" rel="noopener noreferrer"`.

3. **Image Asset Standards & Code Cleanliness:**
   - Always specify explicit `width` and `height` attributes on all `<img>` tags to eliminate Cumulative Layout Shift (CLS).
   - Avoid empty container tags (`<strong></strong>`, `<b></b>`, `<span></span>`, `<a></a>`).

4. **Legal Compliance (DSGVO / MStV):**
   - Keep `impressum.html` compliant with § 18 Abs. 2 MStV and `datenschutz.html` strictly DSGVO compliant with zero unauthorized third-party tracking.
