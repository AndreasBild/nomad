---
description: Apply when creating git branches, staging files, committing changes, pushing to remote, or opening Pull Requests via GitHub CLI.
trigger: model_decision
---

# Git & Pull Request Rules

1. **Dedicated Branching & Staging (Hook-Enforced):**
   - Never commit or push directly to `master` (enforced by `.agents/hooks.json`).
   - Branch from latest `master` using `feature/<slug>`, `fix/<slug>`, or `chore/<slug>`.
   - Never run `git add .` or `git add -A`. Stage only modified task files (`git add <file1> <file2>`).

2. **Mandatory Pre-PR Validation:**
   - Run `./test.sh` and confirm 0 errors across all static checks and 25 HTTP endpoints before committing.

3. **Commit & PR Handoff:**
   - Use imperative conventional commits (`feat: ...`, `fix: ...`, `chore: ...`, `docs: ...`).
   - Follow the `git-pr-workflow` skill (`.agents/skills/git-pr-workflow/SKILL.md`) to push and open a structured PR via `gh pr create` matching `.github/pull_request_template.md`.
