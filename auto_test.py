#!/usr/bin/env python3
"""Automatically run all test scripts in ./tests using the project's .venv Python.
Writes results to logs/test_run.log and appends environment info to README.md.
"""
import os
import sys
import subprocess
from datetime import datetime

ROOT = os.path.dirname(os.path.abspath(__file__))
VENV_PY = os.path.join(ROOT, ".venv", "Scripts", "python") if os.name == "nt" else os.path.join(ROOT, ".venv", "bin", "python")
if not os.path.exists(VENV_PY):
    # fallback to current interpreter but warn
    VENV_PY = sys.executable

LOG_DIR = os.path.join(ROOT, "logs")
LOG_FILE = os.path.join(LOG_DIR, "test_run.log")
os.makedirs(LOG_DIR, exist_ok=True)

test_files = sorted([os.path.join(ROOT, "tests", f) for f in os.listdir(os.path.join(ROOT, "tests")) if f.endswith('.py')])

results = []
# ensure tests can import project package(s)
env = os.environ.copy()
env.setdefault("PYTHONPATH", ROOT)
with open(LOG_FILE, "a", encoding="utf-8") as log:
    header = f"\n=== test run: {datetime.utcnow().isoformat()}Z (runner: {VENV_PY}) ===\n"
    log.write(header)
    for tf in test_files:
        log.write(f"\n--- RUNNING: {tf}\n")
        proc = subprocess.run([VENV_PY, tf], capture_output=True, text=True, env=env)
        log.write(proc.stdout or "")
        if proc.stderr:
            log.write("\n--- STDERR:\n")
            log.write(proc.stderr)
        status = "PASS" if proc.returncode == 0 else f"FAIL (code {proc.returncode})"
        log.write(f"\n--- RESULT: {status}\n")
        results.append((tf, proc.returncode))

# Append environment summary to README.md
try:
    py_ver = subprocess.run([VENV_PY, "--version"], capture_output=True, text=True).stdout.strip()
    pip_ver = subprocess.run([VENV_PY, "-m", "pip", "--version"], capture_output=True, text=True).stdout.strip()
except Exception:
    py_ver = sys.version.replace('\n',' ')
    pip_ver = "(pip not available)"

readme_path = os.path.join(ROOT, "README.md")
env_info = f"\nEnvironment: .venv\nPath: {os.path.abspath(VENV_PY)}\n{py_ver}\n{pip_ver}\n"
with open(readme_path, "a", encoding="utf-8") as r:
    r.write('\n')
    r.write(env_info)

# Exit non-zero if any test failed
failed = [r for r in results if r[1] != 0]
print(f"Ran {len(results)} test(s); failures: {len(failed)}. Detailed log: {LOG_FILE}")
if failed:
    sys.exit(1)
