@echo off

REM Run tests script for Windows

REM Activate virtual environment
call .venv\Scripts\activate

REM Run test scripts
for %%f in (tests\*.py) do (
    echo Running %%f
    python %%f
)

echo All tests completed.

pause