@echo off
REM Activate virtualenv and run tests on Windows
IF NOT EXIST ".venv\Scripts\activate.bat" (
  echo No virtual environment found. Run setup.sh (on WSL/mac) or create a venv manually.
  exit /b 1
)
call .venv\Scripts\activate.bat
IF NOT EXIST logs mkdir logs
python auto_test.py > logs\test_run.log 2>&1
echo Test logs written to logs\test_run.log
