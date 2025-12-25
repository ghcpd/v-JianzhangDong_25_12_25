#!/usr/bin/env python3
import os
import sys
import subprocess
from pathlib import Path
from datetime import datetime

ROOT = Path(__file__).resolve().parent
VENV_DIR = ROOT / '.venv'
LOG_DIR = ROOT / 'logs'
LOG_DIR.mkdir(exist_ok=True)
LOG_FILE = LOG_DIR / 'test_run.log'
TESTS_DIR = ROOT / 'tests'

# Determine python executable inside .venv
if sys.platform == 'win32':
    venv_python = VENV_DIR / 'Scripts' / 'python.exe'
else:
    venv_python = VENV_DIR / 'bin' / 'python'

if not venv_python.exists():
    print('Virtual environment python not found at', venv_python)
    print('Ensure .venv/ exists and is created by setup.sh or similar.')
    sys.exit(1)

# Collect test scripts
test_files = sorted([p for p in TESTS_DIR.glob('*.py')])
if not test_files:
    print('No test files found in tests/')

with LOG_FILE.open('a', encoding='utf-8') as fh:
    header = f"\n=== Test run at {datetime.utcnow().isoformat()} UTC ===\n"
    fh.write(header)
    for test in test_files:
        fh.write(f"\n--- Running {test.name} ---\n")
        try:
            env = os.environ.copy()
            env['PYTHONPATH'] = str(ROOT)
            completed = subprocess.run([str(venv_python), str(test)], capture_output=True, text=True, timeout=300, env=env, cwd=str(ROOT))
            fh.write(completed.stdout or '')
            if completed.stderr:
                fh.write('\n[stderr]\n')
                fh.write(completed.stderr)
            fh.write(f"\nExit code: {completed.returncode}\n")
        except Exception as e:
            fh.write(f"Exception when running {test.name}: {e}\n")

    # Append environment info
    try:
        py_ver = subprocess.run([str(venv_python), '--version'], capture_output=True, text=True).stdout.strip()
        pip_ver = subprocess.run([str(venv_python), '-m', 'pip', '--version'], capture_output=True, text=True).stdout.strip()
    except Exception as e:
        py_ver = f"Error getting python version: {e}"
        pip_ver = f"Error getting pip version: {e}"

    env_info = f"\nEnvironment: .venv\nPath: {venv_python}\n{py_ver}\n{pip_ver}\n"
    fh.write('\n' + env_info)

# Append brief summary to README.md
readme = ROOT / 'README.md'
readme_content = readme.read_text(encoding='utf-8') if readme.exists() else ''
append_text = f"\n\nLast test run: {datetime.utcnow().isoformat()} UTC\nEnvironment: .venv\nPath: {venv_python}\n{py_ver}\n{pip_ver}\n"
readme.write_text(readme_content + append_text, encoding='utf-8')

print(f'Tests executed. Logs appended to {LOG_FILE}')
