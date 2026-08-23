#!/usr/bin/env bash
# ==============================================================================
# Nomad Build & Validation Runner
# Executes all unit checks, JSON-LD schema audits, link & asset checks, and HTTP 200 tests.
# ==============================================================================
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

if command -v python3 >/dev/null 2>&1; then
    PYTHON_BIN="python3"
elif command -v python >/dev/null 2>&1; then
    PYTHON_BIN="python"
else
    echo "Error: Python 3 is required to run the test suite." >&2
    exit 1
fi

chmod +x scripts/validate.py
"$PYTHON_BIN" scripts/validate.py
