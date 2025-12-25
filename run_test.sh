#!/bin/bash
# Test runner script for Linux/macOS

set -e

# Activate virtual environment
if [ ! -d ".venv" ]; then
    echo "Error: .venv directory not found. Please run setup.sh first."
    exit 1
fi

source .venv/bin/activate

echo "Running tests..."
python auto_test.py
