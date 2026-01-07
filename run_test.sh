#!/usr/bin/env bash
set -euo pipefail
# Activate venv if present, otherwise create it
if [ ! -d .venv ]; then
  echo ".venv not found — creating and installing dependencies..."
  ./setup.sh
fi
. .venv/bin/activate
python auto_test.py
