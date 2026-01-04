# Project Setup and Testing Guide

## Overview

This document provides complete instructions for setting up and testing this Python project. The project has been updated with the latest secure versions of all dependencies and includes automated testing scripts.

## Generated Files and Their Purpose

### Dependency Management
- **requirements.txt** - Updated dependencies with pinned versions (security patches applied)
- **requirements_backup.txt** - Backup of original requirements.txt before updates
- **report.json** - Detailed report of all dependency updates and security improvements

### Environment Setup
- **Dockerfile** - Docker configuration for containerized environment deployment
- **.venv/** - Virtual environment directory (created during setup)

### Test Execution
- **auto_test.py** - Automated test runner that:
  - Detects and uses the .venv/ environment
  - Runs all test scripts in tests/ directory
  - Logs all results to logs/test_run.log
  - Updates README.md with environment information
- **run_test.sh** - Linux/macOS test runner script
- **run_test.bat** - Windows test runner batch script
- **setup.sh** - Linux/macOS environment setup script

### Documentation and Logs
- **logs/test_run.log** - Complete test execution log (created after first test run)
- **.gitignore** - Updated to exclude .venv/ directory

---

## Step-by-Step Setup Instructions

### Prerequisites
- Python 3.14.0 or compatible version
- pip 25.3 or compatible version
- Git (for version control)

### Option 1: Setup on Windows (PowerShell)

```powershell
# 1. Create and activate virtual environment
python -m venv .venv
.venv\Scripts\Activate.ps1

# 2. Upgrade pip, setuptools, and wheel
python -m pip install --upgrade pip setuptools wheel

# 3. Install all dependencies
pip install -r requirements.txt

# 4. Run tests
python auto_test.py
```

### Option 2: Setup on Linux/macOS (Bash)

```bash
# 1. Create and activate virtual environment
python3 -m venv .venv
source .venv/bin/activate

# 2. Upgrade pip, setuptools, and wheel
pip install --upgrade pip setuptools wheel

# 3. Install all dependencies
pip install -r requirements.txt

# 4. Run tests (Option A: using script)
bash run_test.sh

# Or Option B: using auto_test.py directly
python auto_test.py
```

### Option 3: Docker Setup

```bash
# Build Docker image
docker build -t python-project .

# Run tests in container
docker run --rm python-project
```

---

## Running Test Scripts

### Using auto_test.py (Recommended)
The auto_test.py script is the primary test runner. It:
- Automatically detects your Python environment
- Runs all test files (case_1.py, case_2.py, case_3.py)
- Logs results with timestamps and detailed output
- Updates README.md with environment information

**Run with:**
```bash
python auto_test.py
```

### Using Platform-Specific Scripts

**Linux/macOS:**
```bash
bash run_test.sh
```

**Windows:**
```cmd
run_test.bat
```

These scripts will activate the virtual environment and call auto_test.py automatically.

### Manual Test Execution

To run individual test files:
```bash
python tests/case_1.py
python tests/case_2.py
python tests/case_3.py
```

---

## Checking Test Logs

After running tests, check the log file:

**Location:** `logs/test_run.log`

**View the log:**
```bash
# Windows PowerShell
Get-Content logs/test_run.log

# Linux/macOS
cat logs/test_run.log

# Real-time tail (Linux/macOS)
tail -f logs/test_run.log
```

The log file contains:
- Timestamp of test execution
- Environment information (Python version, venv path)
- Individual test output (STDOUT and STDERR)
- Test status (PASSED, FAILED, TIMEOUT, ERROR)
- Summary statistics (pass/fail rate)

---

## Dependency Updates Summary

All dependencies have been updated to the latest stable versions with security patches applied:

| Package | Original | Updated | Reason |
|---------|----------|---------|--------|
| numpy | 1.24.0 | 2.4.0 | Security updates, Python 3.14 support |
| pandas | 1.5.0 | 2.3.3 | EOL version, security vulnerabilities |
| matplotlib | 3.5.0 | 3.10.8 | Latest features and patches |
| requests | 2.25.0 | 2.32.5 | Known security vulnerabilities |
| pyyaml | 5.3.1 | 6.0.3 | YAML deserialization vulnerabilities |
| scipy | 1.9.0 | 1.16.3 | Compatibility with numpy 2.4.0 |
| regex | 2021.4.4 | 2025.11.3 | 4+ years old, major updates |
| tqdm | 4.32.0 | 4.67.1 | Outdated with missing features |
| lxml | 4.6.1 | 6.0.2 | XML security vulnerabilities |
| typing_extensions | 3.7.4 | 4.15.0 | Python 3.14 compatibility |

See `report.json` for detailed vulnerability information and justifications.

---

## Virtual Environment Management

### Activating the Environment

**Windows (PowerShell):**
```powershell
.venv\Scripts\Activate.ps1
```

**Windows (Command Prompt):**
```cmd
.venv\Scripts\activate.bat
```

**Linux/macOS:**
```bash
source .venv/bin/activate
```

### Deactivating the Environment
```bash
deactivate
```

### Removing and Recreating the Environment
```bash
# Remove existing environment
rm -r .venv  # Linux/macOS
rmdir /s .venv  # Windows (or use Remove-Item -Recurse in PowerShell)

# Recreate environment
python -m venv .venv
```

---

## Environment Information

### Current Setup Details
The `.venv/` directory contains a complete Python environment with all dependencies. This information is automatically updated after running auto_test.py:

- **Python Version:** (automatically detected and logged)
- **Virtual Environment Path:** (automatically detected and logged)
- **Pip Version:** (automatically detected and logged)

See the "Environment Setup Information" section at the bottom of this README for the latest environment details.

---

## Troubleshooting

### Virtual Environment Not Found
```
Error: .venv directory not found. Please run setup.sh/setup.bat first.
```
**Solution:** Run the setup script for your platform (see Step-by-Step Setup above)

### Module Import Errors
```
ModuleNotFoundError: No module named '...'
```
**Solution:** Ensure the virtual environment is activated and all dependencies are installed:
```bash
python -m pip install -r requirements.txt
```

### Permission Denied (Linux/macOS)
```
bash: run_test.sh: Permission denied
```
**Solution:** Make the script executable:
```bash
chmod +x run_test.sh setup.sh auto_test.py
```

### Python Version Mismatch
Ensure you're using Python 3.14 or compatible:
```bash
python --version
python3 --version
```

---

## Project Structure

```
.
├── app/                          # Application source code
│   ├── __init__.py
│   ├── data_loader.py
│   ├── text_processor.py
│   └── visualizer.py
├── tests/                        # Test files
│   ├── case_1.py
│   ├── case_2.py
│   └── case_3.py
├── logs/                         # Test logs (created after first run)
│   └── test_run.log
├── .venv/                        # Virtual environment (created during setup)
├── requirements.txt              # Updated dependencies
├── requirements_backup.txt       # Original dependencies
├── report.json                   # Dependency update details
├── auto_test.py                  # Main test runner
├── run_test.sh                   # Linux/macOS test runner
├── run_test.bat                  # Windows test runner
├── setup.sh                      # Linux/macOS setup script
├── Dockerfile                    # Docker configuration
├── .gitignore                    # Git ignore patterns
└── README.md                     # This file
```

---

## Security and Maintenance

### Why Dependencies Were Updated
1. **Security Vulnerabilities:** Multiple packages had known CVEs
2. **EOL Versions:** Some packages were no longer maintained
3. **Python 3.14 Support:** Ensure compatibility with latest Python
4. **Performance:** Latest versions include optimization improvements

### Keeping Dependencies Updated
Regularly check for updates:
```bash
pip list --outdated
pip install --upgrade -r requirements.txt
```

### Version Pinning
All dependencies are pinned to specific versions in requirements.txt. This ensures:
- Reproducible builds across systems
- No unexpected breaking changes
- Controlled upgrade cycles

---

## Additional Commands

### Install New Package
```bash
# Activate environment first
pip install package_name

# Update requirements.txt
pip freeze > requirements.txt
```

### View Installed Packages
```bash
pip list
pip show package_name
```

### Run with Absolute Paths
```bash
# On Windows
D:\path\to\.venv\Scripts\python.exe auto_test.py

# On Linux/macOS
/path/to/.venv/bin/python auto_test.py
```

---

## Git Configuration

The `.gitignore` file has been updated to exclude:
- `.venv/` - Virtual environment directory
- `logs/` - Test log files
- `__pycache__/` - Python cache
- `.pytest_cache/` - Pytest cache
- `*.pyc` - Compiled Python files

Ensure your changes to requirements.txt and other source files are committed:
```bash
git add requirements.txt report.json auto_test.py
git commit -m "Update dependencies and add automated testing"
```

---

## Support and Documentation

For more information:
- **Python Documentation:** https://docs.python.org/3.14/
- **Pip Documentation:** https://pip.pypa.io/
- **Virtual Environments:** https://docs.python.org/3.14/tutorial/venv.html

---

## Environment Setup Information

**Last Updated:** 2025-12-25 15:19:53

### Python Environment
- **Python Version:** 3.14.0
- **Python Executable:** D:\projects\v-JianzhangDong_25_12_25\Claude-haiku-4.5\v-JianzhangDong_25_12_25\.venv\Scripts\python.exe
- **Virtual Environment Name:** venv
- **Virtual Environment Path:** D:\projects\v-JianzhangDong_25_12_25\Claude-haiku-4.5\v-JianzhangDong_25_12_25\.venv
- **pip 25.3 from D:\projects\v-JianzhangDong_25_12_25\Claude-haiku-4.5\v-JianzhangDong_25_12_25\.venv\Lib\site-packages\pip (python 3.14)**

### Execution
- Test results are logged to: `logs/test_run.log`
- Run auto_test.py to execute all tests and generate logs
