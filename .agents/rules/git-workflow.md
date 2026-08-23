---
description: Git branching, commit conventions, automated PR creation, and CI/CD validation protocol for AI agents (Antigravity & Jules)
trigger: always_on
---

# Git & Pull Request Automation Rules

1. **Dedicated Branching Protocol:**
   - Never commit or push directly to `master`.
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

4. **Automated Remote Push & PR Creation:**
   - After local verification and commit, push the branch to the remote repository:
     ```bash
     git push -u origin <branch-name>
     ```
   - Automatically initiate and open a Pull Request against `master`.
   - Populate the PR body following `.github/pull_request_template.md`:
     - Concise summary of changes.
     - Core Web Vitals & Technical Quality Checklist (verify all relevant checkboxes).
   - Let GitHub Actions CI (`.github/workflows/ci.yml`) run and validate the PR.
