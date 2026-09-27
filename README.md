# Website Katrin Neumann (Moderatorin | Journalistin | Medientrainerin)

Offizielle Webpräsenz für Katrin Neumann: [www.moderatorin-katrin-neumann.de](https://www.moderatorin-katrin-neumann.de).

## 🚀 Lokaler Testserver

Zum lokalen Testen und Entwickeln steht ein einfaches Start-Skript bereit:

```bash
./start-server.sh
```

Alternativ direkt per Python:
```bash
python3 -m http.server 8000
```

Anschließend im Browser aufrufen:
👉 **[http://localhost:8000](http://localhost:8000)**

---

## ⚡ Durchgeführte Optimierungen

1. **Performance & Verschlankung (Zero jQuery / Pure Vanilla JS):**
   - Veraltete jQuery-Abhängigkeiten (`jquery.min.js`, `jquery.sticky.js`, `jquery.magnific-popup.min.js`, `scrollspy.min.js`, `magnific-popup.css`) vollständig entfernt (~120 KB Einsparung).
   - Menü-Collapse und Smooth-Scrolling modern und performant in nativem JavaScript implementiert (`js/custom.js`).
2. **SEO & Crawling:**
   - `robots.txt`, `sitemap.xml` und `sitemap.xsl` direkt im Web-Root abgelegt und mit kanonischen HTML-Pfaden harmonisiert.
3. **Core Web Vitals & a11y:**
   - Hero-Bannerbild mit `fetchpriority="high"`, `width="1920"` und `height="1083"` gegen Cumulative Layout Shifts (CLS) optimiert.
   - Separate Navigations-Anker (`#about`, `#moderation`, `#kontakt`) für präzise Sprungziele.
   - Syntax- und HTML-Fehler (fehlende Quotes, ungenutzte leere Tags) bereinigt.

---

## 🚢 Automatisches Deployment (webhoster.de)

Die Website wird bei jedem Push/Merge auf den `master`-Branch automatisch per GitHub Actions auf den Webspace bei webhoster.de übertragen (`.github/workflows/deploy.yml`).

### Erforderliche GitHub Secrets (unter `Settings > Secrets and variables > Actions`):
- `FTP_SERVER`: FTP-Serveradresse / Hostname (z. B. `ftp.moderatorin-katrin-neumann.de` oder Server-IP)
- `FTP_USERNAME`: FTP-Benutzername
- `FTP_PASSWORD`: FTP-Passwort
- `FTP_SERVER_DIR`: *(Optional)* Zielordner auf dem Webspace (Standard: `webpage/`)

