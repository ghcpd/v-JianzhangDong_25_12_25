# Dependency maintenance — generated files overview

This repository has been updated to ensure secure, compatible dependencies and to provide reproducible test/run scripts.

## What I changed / added ✅

- `requirements_backup.txt` — original requirements (backup).
- `requirements.txt` — **updated and pinned** to versions that were installed successfully on Python 3.14.
- `report.json` — simplified report of dependency updates and reasons.
- `.venv/` — a clean virtual environment (not checked into git).
- `auto_test.py` — runs all `tests/*.py` using the `.venv` Python and writes `logs/test_run.log`.
- `logs/test_run.log` — test execution output (created when tests are run).
- `Dockerfile` / `setup.sh` / `run_test.sh` / `run_test.bat` — environment replication & test helpers.
- `.gitignore` — updated to exclude `.venv/` and logs.

## How to reproduce (Linux/macOS)

1. git clone ... && cd repo
2. ./setup.sh
3. ./run_test.sh

## How to run on Windows

1. Open PowerShell in the repo root
2. .\run_test.bat

## Using `auto_test.py`

- `auto_test.py` will use `.venv`'s Python to execute every `*.py` in `tests/` and append environment info to `README.md`.
- Logs are written to `logs/test_run.log`.

## Checking logs

- See `logs/test_run.log` for stdout/stderr and pass/fail status for each test.

## Docker

- Build: docker build -t repo-test .
- Run: docker run --rm repo-test



Environment: .venv
Path: D:\projects\v-JianzhangDong_25_12_25\oswe-mini-m23a1s255\v-JianzhangDong_25_12_25\.venv\Scripts\python.exe
Python 3.14.0
pip 25.3 from D:\projects\v-JianzhangDong_25_12_25\oswe-mini-m23a1s255\v-JianzhangDong_25_12_25\.venv\Lib\site-packages\pip (python 3.14)


Environment: .venv
Path: D:\projects\v-JianzhangDong_25_12_25\oswe-mini-m23a1s255\v-JianzhangDong_25_12_25\.venv\Scripts\python.exe
Python 3.14.0
pip 25.3 from D:\projects\v-JianzhangDong_25_12_25\oswe-mini-m23a1s255\v-JianzhangDong_25_12_25\.venv\Lib\site-packages\pip (python 3.14)
