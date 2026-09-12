---
name: optimize-context
description: Self-auditing routine to detect rule bloat, audit context token budgets, and adapt to new model releases.
---

# Optimize Context Skill

Use this skill to audit repository agent instructions, prevent context bloat, and maintain token economy.

## Audit Checklist & Procedures

### 1. Root Kernel Budget Audit
- Verify root `AGENTS.md` and `GEMINI.md` remain under **35 lines** (~400 tokens).
- Command:
  ```bash
  wc -l AGENTS.md GEMINI.md
  ```
- The Kernel must hold **only**:
  - System Identity & Role
  - Non-negotiable Core Invariants (branch protection, zero stubs, context boundaries)
  - Dual-Loop Execution summary
  - Dynamic Model Tier protocol
  - Progressive Skill Router table
- Any operational or procedural guidance must be relocated to `.agents/rules/` or `.agents/skills/`.

### 2. Rule Bloat & Duplication Detection
- Inspect `.agents/rules/` files. Each rule should be focused on a single concern (`architecture`, `code-quality`, `git-workflow`, `seo`, `token-efficiency`).
- Eliminate:
  - Repetitive explanations of standard language/framework features (e.g., how CSS specificity works).
  - Conversational filler or duplicate instructions across multiple rule files.
  - Stale rules superseded by automated validation in `scripts/validate.py`.

### 3. Context & Ignore Hygiene
- Check ignore files (`.antigravityignore`, `.geminiignore`, `.agentignore`) to ensure binary assets and large vendor files are never indexed:
  ```
  images/*.webp
  images/*.jpg
  images/*.png
  css/bootstrap.min.css
  js/bootstrap.bundle.min.js
  css/aos.css
  js/aos.js
  ```
- Ensure commands run by agents avoid dumping massive terminal outputs (use `head`, `grep`, or subagents).

### 4. Subagent Boundary Isolation Check
- When executing heavy diagnostics (multi-step tests, large log parsing, extensive audits), confirm work is delegated to a subagent that returns an executive memo rather than consuming the main conversation context.

### 5. Model Release Adaptation
- As faster and more capable models (e.g. Gemini 3.8 / Flash / Pro) become standard, review whether instructions can be simplified:
  - Remove over-defensive prompting when newer models handle constraints natively.
  - Adjust the Dynamic Model Tier table in `AGENTS.md` if newer model identifiers or cost/capability tiers become available.
