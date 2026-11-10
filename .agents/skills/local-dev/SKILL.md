---
name: local-dev
description: >-
  Use this skill when starting the local development HTTP server (./start-server.sh)
  to preview the site in a browser or inspect live local pages.
---

# Local Dev Server Skill

## Steps

1. **Start the local HTTP server (default port 8000):**
   ```bash
   ./start-server.sh 8000
   ```
   *(Uses `python3 -m http.server` to serve the static root at `http://localhost:8000`.)*

2. **Browser Preview / Inspection:**
   - Once the server is running in background/daemon mode, delegate live UI or DevTools inspection of `http://localhost:8000` to the `browser` subagent.
   - For automated endpoint and HTML5 validation without manual preview, use the `test-suite` skill (`./test.sh --fast` or `./test.sh`).
