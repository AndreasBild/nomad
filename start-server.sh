#!/usr/bin/env bash

# Start a lightweight local HTTP server for Katrin Neumann's Website
PORT=${1:-8000}
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo "========================================================"
echo " Starting local development server for Katrin Neumann"
echo " Directory: ${DIR}"
echo " Local URL: http://localhost:${PORT}"
echo " Press Ctrl+C to stop the server"
echo "========================================================"

cd "${DIR}" || exit 1

if command -v python3 &> /dev/null; then
    python3 -m http.server "${PORT}"
elif command -v python &> /dev/null; then
    python -m SimpleHTTPServer "${PORT}"
elif command -v php &> /dev/null; then
    php -S "localhost:${PORT}"
else
    echo "Error: Neither python3, python nor php is installed."
    exit 1
fi
