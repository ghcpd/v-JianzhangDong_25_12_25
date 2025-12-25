@echo off
REM Test runner script for Windows

if not exist ".venv" (
    echo Error: .venv directory not found. Please run setup.bat first.
    exit /b 1
)

call .venv\Scripts\activate.bat

echo Running tests...
python auto_test.py
pause
