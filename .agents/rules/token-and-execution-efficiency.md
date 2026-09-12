# Token Economics & Execution Efficiency Rule

## 1. Context Boundaries & Token Hygiene
- **Large Binary Files Invariant:** Never read binary media files, images, or large library bundles in full into LLM context:
  - Hero and teaser images: `images/*.webp`, `images/*.jpg`, `images/*.png`
  - Favicon and app icon assets: `favicon.ico`, `android-chrome-*.png`, `apple-touch-icon.png`
  - Minified vendor bundles: `css/bootstrap.min.css`, `js/bootstrap.bundle.min.js`, `css/aos.css`, `js/aos.js`
- **Targeted Inspection Protocol:**
  - Use `grep_search` to locate specific CSS selectors, DOM IDs, classes, or meta tags.
  - Use `view_file` strictly with bounded `StartLine` and `EndLine` slices (maximum 50–100 lines at a time).
  - Inspect custom styles (`css/katrin.css`) and custom scripts (`js/custom.js`, `sw.js`) rather than minified third-party libraries.
- **Surgical Diffing:** Always use targeted diff tools (`replace_file_content` or `multi_replace_file_content`) with minimal necessary context lines. Never rewrite entire HTML or CSS files unmodified.

## 2. Dynamic Model Tier Recommendation Protocol
To guarantee peak token efficiency and execution accuracy, agents dynamically evaluate incoming tasks and propose the appropriate model tier in implementation plans or initial scoping responses:

| Model Tier | Capability Profile | Typical Workflows in Nomad (HTML / Static Web) |
| :--- | :--- | :--- |
| **Tier 1: Fast / Medium**<br>*(Latest Flash / Medium in IDE)* | High throughput, sub-second latency, optimal token economy. | • Routine HTML content & text copy updates<br>• Section anchor adjustments and internal navigation links<br>• CSS styling adjustments in `css/katrin.css`<br>• Updating `<lastmod>` timestamps in `sitemap.xml`<br>• Open Graph, Twitter Card, and meta tag adjustments<br>• Inner-loop validation (`./test.sh --fast`)<br>• Minor bugfixes, formatting, and autonomous PR creation |
| **Tier 2: Deep Reasoning / Pro**<br>*(Latest Pro / Thinking in IDE)* | Multi-step reasoning, architectural synthesis, subtle edge-case detection. | • Major responsive layout redesigns (Bootstrap 5 flex/grid refactoring)<br>• Deep Core Web Vitals diagnostics (LCP banner preload, INP event listeners)<br>• Schema.org JSON-LD graph architecture (`@graph`, `Person`, `VideoObject`)<br>• Complex Service Worker offline caching strategy (`sw.js`)<br>• Accessibility (WCAG 2.1 AA) full structural audits across landmarks & tabindex |

*Implementation Plan Standard:* Every `implementation_plan.md` must include a `## 🎯 Recommended Execution Model` section declaring the recommended tier and rationale.

## 3. Dual-Loop Execution Strategy
Separate development into two distinct validation loops to minimize latency and token consumption:

### 3.1 Fast Inner Loop (Active Development & Iteration)
Do NOT start a local HTTP server or validate all 25 HTTP network endpoints for intermediate syntax and layout edits:
```bash
./test.sh --fast
```
*Validates Sitemap XML, `robots.txt`, Schema.org JSON-LD, internal anchors, referenced static assets, and HTML5 semantic standards in <50ms without server startup.*

### 3.2 Comprehensive Outer Gate (Pre-Commit / Pre-PR)
Execute only after inner-loop checks pass and task implementation is finalized:
```bash
./test.sh
```
*Executes the complete validation suite, spins up the local test server, and confirms HTTP 200 responses across all 25 production endpoints.*

## 4. Working Tree Hygiene & Unrelated Changes
- **Preserve Unrelated Work:** The workspace owner may have local overrides or uncommitted changes.
- **Never Run `git add .` Blindly:** Strictly stage only files directly modified for the agent's specific task using `git add <file1> <file2>`.
- Check `git status` before committing to ensure no stray temporary files or artifacts are staged.

## 5. Command Output & Log Truncation
- Avoid commands that generate unbounded terminal output into conversation context.
- Limit command outputs using `head`, `grep`, or targeted flags.
- Do not poll running tasks or background timers in tight loops. Rely on reactive wakeup.

## 6. Subagent Boundary Isolation
- **Delegate Heavy Diagnostics:** Offload verbose, exploratory, or repetitive tasks (e.g., extensive test/build runs, large raw log inspections, deep dependency analysis) to dedicated subagents.
- **Executive Memo Protocol:** Subagents must synthesize their findings and return concise, actionable executive memos (summary, root cause, verified fix) to the primary orchestrator rather than dumping raw command traces into the main conversation context.
- **Context Preservation:** Isolating noisy subagent trajectories preserves the main orchestrator's token budget and keeps reasoning focused on architectural decisions and user deliverables.

## 7. High-Signal Communication
- Eliminate conversational pleasantries, repetitive apologies, and boilerplate explanations.
- Always provide concise, actionable markdown with direct clickable `file://` links using the `file://` scheme.
