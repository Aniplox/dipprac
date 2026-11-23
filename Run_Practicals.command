#!/bin/bash
cd "$(dirname "$0")" || exit 1
if [ -x .venv/bin/python ]; then
    .venv/bin/python run.py
else
    python3 run.py
fi
status=$?
if [ "$status" -ne 0 ]; then
    echo "If packages are missing, run: bash setup.sh"
    read -r -p "Press Enter to close..."
fi
exit "$status"
