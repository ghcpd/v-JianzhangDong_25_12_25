@echo off
REM Activate .venv and run auto_test.py (Windows)
IF NOT EXIST .venv\Scripts\activate.bat (
  echo .venv not found — create it with setup.bat or python -m venv .venv
  exit /b 1
)

call .venv\Scripts\activate.bat
python auto_test.py
