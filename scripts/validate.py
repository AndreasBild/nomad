#!/usr/bin/env python3
"""
Nomad Project - Comprehensive Validation & Health Check Suite
Validates XML, robots.txt, Schema.org JSON-LD, internal anchors, static assets, and HTTP 200 endpoints.
"""

import glob
import http.server
import json
import os
import re
import socketserver
import sys
import threading
import time
import urllib.request
import xml.etree.ElementTree as ET

WORKSPACE_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(WORKSPACE_ROOT)

def print_header(title):
    print(f"\n{'='*60}\n  {title}\n{'='*60}")

def validate_xml_and_robots():
    print_header("1. Validating Sitemap XML & robots.txt")
    
    # 1. sitemap.xml
    sitemap_path = os.path.join(WORKSPACE_ROOT, "sitemap.xml")
    assert os.path.isfile(sitemap_path), "sitemap.xml is missing!"
    tree = ET.parse(sitemap_path)
    root = tree.getroot()
    urls = root.findall("{http://www.sitemaps.org/schemas/sitemap/0.9}url")
    assert len(urls) > 0, "sitemap.xml contains no <url> entries!"
    print(f"✓ sitemap.xml is valid XML with {len(urls)} URL entries.")
    
    # 2. sitemap.xsl
    xsl_path = os.path.join(WORKSPACE_ROOT, "sitemap.xsl")
    assert os.path.isfile(xsl_path), "sitemap.xsl is missing!"
    ET.parse(xsl_path)
    print("✓ sitemap.xsl is valid XML/XSL.")
    
    # 3. robots.txt
    robots_path = os.path.join(WORKSPACE_ROOT, "robots.txt")
    assert os.path.isfile(robots_path), "robots.txt is missing!"
    with open(robots_path, "r", encoding="utf-8") as f:
        robots_txt = f.read()
    assert "Sitemap:" in robots_txt, "robots.txt must contain a Sitemap directive!"
    assert "User-agent:" in robots_txt, "robots.txt must contain User-agent!"
    print("✓ robots.txt is valid and contains standard directives.")

def validate_json_ld():
    print_header("2. Validating JSON-LD Structured Data")
    html_files = sorted(glob.glob("*.html"))
    total_blocks = 0
    for fpath in html_files:
        with open(fpath, "r", encoding="utf-8") as f:
            content = f.read()
        matches = re.findall(r'<script type="application/ld\+json">(.*?)</script>', content, re.DOTALL)
        for i, match in enumerate(matches):
            total_blocks += 1
            try:
                data = json.loads(match.strip())
                schema_type = data.get("@type") or ("@graph" if "@graph" in data else "Unknown")
                print(f"✓ {fpath} -> JSON-LD block {i+1} valid ({schema_type})")
            except Exception as e:
                raise AssertionError(f"Invalid JSON-LD in {fpath}: {e}")
    print(f"✓ Total of {total_blocks} JSON-LD blocks validated successfully.")

def validate_links_and_assets():
    print_header("3. Validating Static Assets & Internal Anchors")
    html_files = sorted(glob.glob("*.html"))
    
    # Collect all IDs from HTML files
    file_ids = {}
    for fpath in html_files:
        with open(fpath, "r", encoding="utf-8") as f:
            content = f.read()
        ids = set(re.findall(r'\bid=["\']([^"\']+)["\']', content))
        file_ids[fpath] = ids

    # Check internal links and anchors
    for fpath in html_files:
        with open(fpath, "r", encoding="utf-8") as f:
            content = f.read()
        
        # Check href links
        links = re.findall(r'href=["\']([^"\']+)["\']', content)
        for link in links:
            if link.startswith(("#", "http://", "https://", "mailto:", "tel:", "javascript:")):
                # Internal anchor on same page
                if link.startswith("#"):
                    anchor = link[1:]
                    assert anchor in file_ids[fpath], f"Broken internal anchor '{link}' in {fpath}"
                continue
            
            # Target file with optional anchor
            parts = link.split("#", 1)
            target_file = parts[0].lstrip("/")
            anchor = parts[1] if len(parts) > 1 else None
            
            if target_file and not target_file.endswith((".css", ".png", ".jpg", ".webp", ".ico", ".webmanifest")):
                assert os.path.isfile(target_file), f"Broken link '{link}' in {fpath}: file {target_file} not found"
                if anchor and target_file in file_ids:
                    assert anchor in file_ids[target_file], f"Broken anchor '{anchor}' in {link} from {fpath}"

        # Check image and media sources
        img_sources = re.findall(r'(?:src|srcset|href)=["\']([^"\']+\.(?:png|jpg|webp|ico|svg))["\']', content)
        for src in img_sources:
            clean_path = src.lstrip("/")
            assert os.path.isfile(clean_path), f"Referenced asset '{src}' in {fpath} does not exist on disk!"

    print("✓ All internal links, section anchors, and referenced image assets exist.")

class QuietHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        pass

class QuietServer(socketserver.TCPServer):
    allow_reuse_address = True
    def handle_error(self, request, client_address):
        pass

def validate_http_endpoints():
    print_header("4. Validating HTTP 200 Endpoints on Local Server")
    
    server = None
    port = 8000
    for test_port in [8000, 8080, 8888, 9000, 0]:
        try:
            server = QuietServer(("127.0.0.1", test_port), QuietHandler)
            port = server.server_address[1]
            break
        except OSError:
            continue

    assert server is not None, "Could not start local HTTP server on any port!"
    
    server_thread = threading.Thread(target=server.serve_forever, daemon=True)
    server_thread.start()
    time.sleep(0.5)

    try:
        urls = [
            f"http://127.0.0.1:{port}/",
            f"http://127.0.0.1:{port}/index.html",
            f"http://127.0.0.1:{port}/impressum.html",
            f"http://127.0.0.1:{port}/datenschutz.html",
            f"http://127.0.0.1:{port}/robots.txt",
            f"http://127.0.0.1:{port}/sitemap.xml",
            f"http://127.0.0.1:{port}/sitemap.xsl",
            f"http://127.0.0.1:{port}/site.webmanifest",
            f"http://127.0.0.1:{port}/sw.js",
            f"http://127.0.0.1:{port}/css/bootstrap.min.css",
            f"http://127.0.0.1:{port}/css/aos.css",
            f"http://127.0.0.1:{port}/css/templatemo-nomad-force.css",
            f"http://127.0.0.1:{port}/css/katrin.css",
            f"http://127.0.0.1:{port}/js/bootstrap.bundle.min.js",
            f"http://127.0.0.1:{port}/js/aos.js",
            f"http://127.0.0.1:{port}/js/custom.js",
            f"http://127.0.0.1:{port}/images/Katrin-Neumann-Moderatorin.webp",
            f"http://127.0.0.1:{port}/images/Katrin-Neumann-Moderatorin-768.webp",
            f"http://127.0.0.1:{port}/images/Katrin-Neumann-Moderatorin.jpg",
            f"http://127.0.0.1:{port}/llms.txt",
            f"http://127.0.0.1:{port}/llms-full.txt",
            f"http://127.0.0.1:{port}/favicon.ico",
            f"http://127.0.0.1:{port}/favicon-32x32.png",
            f"http://127.0.0.1:{port}/favicon-16x16.png",
            f"http://127.0.0.1:{port}/apple-touch-icon.png"
        ]

        for u in urls:
            req = urllib.request.Request(u, headers={'User-Agent': 'Nomad-Validation-Suite/1.0'})
            with urllib.request.urlopen(req) as resp:
                assert resp.status == 200, f"Endpoint {u} returned status {resp.status}"
                resp.read() # Consume full stream
                path_part = u.split(f":{port}")[1]
                print(f"✓ [HTTP 200] {path_part}")

        print(f"\n✓ All {len(urls)} endpoints verified successfully with HTTP 200!")
    finally:
        server.shutdown()
        server.server_close()

def main():
    try:
        validate_xml_and_robots()
        validate_json_ld()
        validate_links_and_assets()
        validate_http_endpoints()
        print("\n" + "="*60)
        print("  🎉 ALL TESTS PASSED! SITE BUILD IS BULLETPROOF. 🎉")
        print("="*60 + "\n")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Validation Failed: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
