@echo off
REM Create venv if missing and run the auto test runner (Windows)
if not exist .venv ( 
  echo Creating .venv and installing dependencies...
  python -m venv .venv
  .venv\Scripts\python -m pip install --upgrade pip setuptools wheel
  .venv\Scripts\python -m pip install -r requirements.txt
)
.venv\Scripts\python auto_test.py
if %ERRORLEVEL% neq 0 (
  echo Some tests failed. See logs\test_run.log
) else (
  echo All tests passed. See logs\test_run.log
)
