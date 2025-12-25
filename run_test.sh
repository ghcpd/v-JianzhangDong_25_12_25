#!/bin/bash

# Run tests script for Linux/macOS

# Activate virtual environment
source .venv/bin/activate

# Run test scripts
for test_file in tests/*.py; do
    echo "Running $test_file"
    python "$test_file"
done

echo "All tests completed."