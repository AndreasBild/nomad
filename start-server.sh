#!/usr/bin/env bash
set -e

# Start a lightweight local HTTP server for Katrin Neumann's Website
PORT=${1:-8000}
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

cd "${DIR}" || exit 1

# Check if the port is already in use and stop existing server process(es)
if command -v lsof >/dev/null 2>&1; then
    OCCUPIED_PIDS=$(lsof -ti :"$PORT" 2>/dev/null || true)
    if [ -n "$OCCUPIED_PIDS" ]; then
        PID_LIST=$(echo "$OCCUPIED_PIDS" | tr '\n' ' ' | sed 's/ $//')
        echo "⚠️  Port ${PORT} is already in use (PID: ${PID_LIST})."
        echo "🛑 Stopping existing server process(es)..."
        kill $OCCUPIED_PIDS 2>/dev/null || true

        # Wait up to 3 seconds for the port to clear
        for _ in {1..30}; do
            if ! lsof -ti :"$PORT" >/dev/null 2>&1; then
                break
            fi
            sleep 0.1
        done

        # If still running, force terminate
        REMAINING_PIDS=$(lsof -ti :"$PORT" 2>/dev/null || true)
        if [ -n "$REMAINING_PIDS" ]; then
            echo "⚡ Force terminating PID: $(echo "$REMAINING_PIDS" | tr '\n' ' ')..."
            kill -9 $REMAINING_PIDS 2>/dev/null || true
            sleep 0.2
        fi
        echo "✓ Existing process stopped. Starting fresh server instance."
    fi
fi

echo "========================================================"
echo " Starting local development server for Katrin Neumann"
echo " Directory: ${DIR}"
echo " Local URL: http://localhost:${PORT}"
echo " Press Ctrl+C to stop the server"
echo "========================================================"

if command -v python3 &> /dev/null; then
    exec python3 -m http.server "${PORT}"
elif command -v python &> /dev/null; then
    exec python -m SimpleHTTPServer "${PORT}"
elif command -v php &> /dev/null; then
    exec php -S "localhost:${PORT}"
else
    echo "Error: Neither python3, python nor php is installed."
    exit 1
fi

