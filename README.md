# Project Environment and Test Automation

## Overview ✅
This repository includes automated environment setup and test scripts produced by the dependency maintenance process. Generated files:

- `requirements_backup.txt` — Backup of the original requirements.
- `requirements.txt` — Updated, pinned dependencies compatible with Python 3.14.
- `report.json` — A concise report describing the packages that were updated and why.
- `Dockerfile` — Reproducible Docker build installing the pinned dependencies.
- `setup.sh` — Creates a fresh virtual environment at `.venv/` and installs dependencies (Linux/macOS).
- `run_test.sh` — Activates `.venv/` and runs `auto_test.py` (Linux/macOS).
- `run_test.bat` — Activates `.venv/` and runs `auto_test.py` (Windows).
- `auto_test.py` — Runs each test script in the `tests/` directory using the `.venv` Python and writes logs to `logs/test_run.log`. It also appends the environment name/path and Python/pip versions to this `README.md` after each run.
- `logs/` — Directory created at test time containing `test_run.log`.
- `.gitignore` — Ignores `.venv/`, `logs/`, and build artifacts.

---

## Setup (Linux/macOS) 🔧
1. Ensure system Python is 3.14.x (this project was validated on Python 3.14).  
2. Run:
   - `bash setup.sh`  (creates a fresh `.venv/` and installs pinned dependencies)

## Setup (Windows) ⚙️
1. Ensure Python 3.14 is available as `python`.  
2. Create a venv manually and install requirements:
   - `python -m venv .venv`
   - `.\.venv\Scripts\activate`
   - `python -m pip install --upgrade pip setuptools wheel`
   - `pip install -r requirements.txt`

## Running tests
- Linux/macOS: `bash run_test.sh`
- Windows: run `run_test.bat`

These scripts will execute `auto_test.py` which runs each `tests/*.py` script using the `.venv` Python and writes logs to `logs/test_run.log`.

## Using `auto_test.py` directly
- Make sure `.venv/` exists and contains a Python interpreter.  
- Run with the system Python (it will use the `.venv` interpreter to execute tests):
  - `python auto_test.py`

## Checking logs 📋
- After a run, open `logs/test_run.log` to see test outputs, exit codes, and environment information.

---

If you need me to run the tests and attach the logs here, say so and I will execute them and summarize the results. ✅


Last test run: 2025-12-25T07:59:28.687982 UTC
Environment: .venv
Path: D:\projects\v-JianzhangDong_25_12_25\oswe-mini-prime-new\v-JianzhangDong_25_12_25\.venv\Scripts\python.exe
Python 3.14.0
pip 25.3 from D:\projects\v-JianzhangDong_25_12_25\oswe-mini-prime-new\v-JianzhangDong_25_12_25\.venv\Lib\site-packages\pip (python 3.14)


Last test run: 2025-12-25T07:59:55.664398 UTC
Environment: .venv
Path: D:\projects\v-JianzhangDong_25_12_25\oswe-mini-prime-new\v-JianzhangDong_25_12_25\.venv\Scripts\python.exe
Python 3.14.0
pip 25.3 from D:\projects\v-JianzhangDong_25_12_25\oswe-mini-prime-new\v-JianzhangDong_25_12_25\.venv\Lib\site-packages\pip (python 3.14)
