#!/usr/bin/env bash
set -euo pipefail

# Activate venv and run auto_test.py
if [ -f ".venv/bin/activate" ]; then
  source .venv/bin/activate
else
  echo ".venv not found — create it with ./setup.sh" >&2
  exit 1
fi

python auto_test.py
