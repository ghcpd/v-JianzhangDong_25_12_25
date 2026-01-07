#!/usr/bin/env bash
set -euo pipefail

echo "Creating a fresh virtual environment at .venv/"
rm -rf .venv
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip setuptools wheel
pip install -r requirements.txt

echo "Virtual environment ready. To activate: source .venv/bin/activate"
