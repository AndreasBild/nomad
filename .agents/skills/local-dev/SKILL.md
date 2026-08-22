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
   python3 -c "
   import urllib.request
   urls = [
       'http://localhost:8000/',
       'http://localhost:8000/index.html',
       'http://localhost:8000/impressum.html',
       'http://localhost:8000/datenschutz.html',
       'http://localhost:8000/robots.txt',
       'http://localhost:8000/sitemap.xml',
       'http://localhost:8000/sitemap.xsl',
       'http://localhost:8000/css/bootstrap.min.css',
       'http://localhost:8000/css/aos.css',
       'http://localhost:8000/css/templatemo-nomad-force.css',
       'http://localhost:8000/css/katrin.css',
       'http://localhost:8000/js/bootstrap.bundle.min.js',
       'http://localhost:8000/js/aos.js',
       'http://localhost:8000/js/custom.js',
       'http://localhost:8000/sw.js',
       'http://localhost:8000/images/Katrin-Neumann-Moderatorin.webp',
       'http://localhost:8000/images/Katrin-Neumann-Moderatorin-768.webp',
       'http://localhost:8000/images/Instagram_logo.png',
       'http://localhost:8000/llms.txt',
       'http://localhost:8000/llms-full.txt'
   ]
   for u in urls:
       resp = urllib.request.urlopen(u)
       assert resp.status == 200, f'Failed: {u}'
   print('All 20 assets & pages verified successfully with HTTP 200!')
   "
   ```
