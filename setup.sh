#!/bin/bash
set -e
cd "$(dirname "$0")"
if ! command -v python3 >/dev/null 2>&1; then
    echo "Install Python 3.11–3.13 from https://www.python.org/downloads/macos/ first."
    exit 1
fi
# Reuse installed scientific packages when available, so setup can work offline.
python3 -m venv --system-site-packages .venv
if ! .venv/bin/python -c 'import numpy, scipy, matplotlib, skimage, PIL' >/dev/null 2>&1; then
    .venv/bin/python -m pip install -r requirements.txt
fi
echo "Ready. Run: .venv/bin/python run.py"
