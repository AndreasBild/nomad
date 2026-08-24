---
description: Git branching protocol, commit conventions, automated PR creation via gh CLI, and CI/CD validation protocol
trigger: always_on
---

# Git & Pull Request Automation Rules

1. **Dedicated Branching Protocol:**
   - **Never commit directly to `master`.**
   - Always create and switch to a descriptive branch from latest `master` before making changes:
     - `feature/<short-description>`: New features, content additions, or major styling changes.
     - `fix/<short-description>`: Bugfixes, layout corrections, broken links.
     - `chore/<short-description>`: Refactoring, dependency updates, CI/CD, or documentation tweaks.

2. **Pre-PR Quality Gate (Mandatory Validation):**
   - Before committing or creating a PR, always run the full validation suite locally:
     ```bash
     ./test.sh
     ```
   - Ensure all HTML validations, XML sitemaps, JSON-LD schemas, asset links, and Core Web Vitals checks pass with 0 errors.

3. **Commit Standards:**
   - Use clear, imperative commit messages: `feat: ...`, `fix: ...`, `chore: ...`, `docs: ...`.
   - Provide concise bullet points detailing non-obvious rationale and verified changes.

4. **Autonomous Remote Push & PR Creation:**
   - Push branch to remote:
     ```bash
     git push -u origin <branch-name>
     ```
   - Create Pull Request autonomously using GitHub CLI:
     ```bash
     gh pr create --base master --head <branch-name> --title "<title>" --body "<body>"
     ```
   - Populate the PR body following `.github/pull_request_template.md`.
   - Automated CI (`.github/workflows/ci.yml`) runs on PR; merge triggers automated production deployment (`.github/workflows/deploy.yml`).
