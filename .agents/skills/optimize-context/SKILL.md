---
name: optimize-context
description: >-
  Use this skill when auditing repository agent instructions, checking rule triggers and token budgets,
  verifying .agents/hooks.json guardrails, or syncing ignore files (.antigravityignore, .geminiignore, .agentignore).
---

# Optimize Context Skill

## Audit Checklist & Procedures

### 1. Root Kernel Budget Audit
- Verify root `AGENTS.md` and `GEMINI.md` remain under **35 lines** (~400 tokens):
  ```bash
  wc -l AGENTS.md GEMINI.md
  ```
- Keep only Role/Identity, Core Invariants, Dual-Loop summary, Model Tier protocol, and Progressive Skill Router in `AGENTS.md`.

### 2. Rule Trigger & Duplication Audit (`.agents/rules/*.md`)
- Every rule file in `.agents/rules/` **must** include valid YAML frontmatter (`description` and `trigger`).
- Use `trigger: always_on` **only** for universal stack constraints (`architecture.md`).
- Use `trigger: model_decision` with specific trigger descriptions for domain rules (`code-quality-and-a11y.md`, `seo-and-performance.md`, `git-workflow.md`) so they load via progressive disclosure only when relevant.

### 3. Skill Deduplication & Frontmatter Audit (`.agents/skills/*/SKILL.md`)
- Ensure every skill has a distinct responsibility and a third-person `description` (`Use this skill when...`).
- Verify the Progressive Skill Router table in `AGENTS.md` matches the exact set of directories in `.agents/skills/`.

### 4. Deterministic Hook Guardrails (`.agents/hooks.json`)
- Prefer zero-token deterministic enforcement in `.agents/hooks.json` (`PreToolUse` on `run_command` via `.agents/hooks/pre_command.py`) over repetitive prompt warnings for:
  - Blocking blind staging (`git add .`, `git add -A`, `git add --all`).
  - Blocking direct commits or pushes to `master`.

### 5. Context & Ignore File Parity
- Verify `.antigravityignore`, `.geminiignore`, and `.agentignore` are identical in excluding binary media and minified vendor bundles:
  - `images/*.webp`, `images/*.jpg`, `images/*.png`, `*.png`, `*.ico`, `*.zip`, `*.tar.gz`, `*.iso`
  - `css/bootstrap.min.css`, `js/bootstrap.bundle.min.js`, `css/aos.css`, `js/aos.js`
