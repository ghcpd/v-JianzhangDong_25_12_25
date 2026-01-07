#!/usr/bin/env bash
set -euo pipefail
printf "Creating a clean .venv/ and installing dependencies...\n"
if [ -d .venv ]; then
  rm -rf .venv
fi
python3 -m venv .venv
. .venv/bin/activate
python -m pip install --upgrade pip setuptools wheel
python -m pip install -r requirements.txt
printf "Setup complete. To run tests: ./run_test.sh\n"
