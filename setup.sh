#!/usr/bin/env bash
set -euo pipefail

# Create a fresh virtual environment in .venv
if [ -d ".venv" ]; then
  echo "Removing existing .venv/"
  rm -rf .venv
fi
python3 -m venv .venv
. .venv/bin/activate
python -m pip install --upgrade pip setuptools wheel
pip install --no-cache-dir -r requirements.txt

echo "Virtual environment created at $(pwd)/.venv"
