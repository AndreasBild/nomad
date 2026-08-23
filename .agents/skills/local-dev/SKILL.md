---
name: local-dev
description: Starts the local development server and runs health and asset validation tests for Nomad.
---

# Local Dev & Testing Skill

Use this skill when you need to start the local web server, test changes, or verify endpoint accessibility.

## Steps

1. **Start the local server:**
   ```bash
   ./start-server.sh 8000
   ```
   Or in background with python:
   ```bash
   python3 -m http.server 8000
   ```

2. **Verify all endpoints and static assets:**
   ```bash
   ./test.sh
   ```
   Or run the validator directly:
   ```bash
   python3 scripts/validate.py
   ```

