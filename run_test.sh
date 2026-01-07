#!/usr/bin/env bash
set -euo pipefail

# Activate virtual environment and run tests
if [ -d ".venv" ]; then
  . .venv/bin/activate
else
  echo "No virtualenv found. Run setup.sh first to create .venv/"
  exit 1
fi

# Run all test scripts in tests/ and log output
mkdir -p logs
python auto_test.py | tee logs/test_run.log
echo "Test logs written to logs/test_run.log"
