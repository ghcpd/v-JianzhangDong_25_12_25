#!/usr/bin/env python3
"""
Run all test scripts in the `tests/` directory using the Python interpreter from `.venv/`.
Writes a detailed run log to `logs/test_run.log` and appends environment info to README.md.
"""
import os
import sys
import subprocess
from pathlib import Path
from datetime import datetime

ROOT = Path(__file__).resolve().parent
VENV = ROOT / '.venv'
LOG_DIR = ROOT / 'logs'
LOG_DIR.mkdir(exist_ok=True)
LOG_FILE = LOG_DIR / 'test_run.log'
TESTS_DIR = ROOT / 'tests'


def venv_python():
    if sys.platform.startswith('win'):
        candidate = VENV / 'Scripts' / 'python.exe'
    else:
        candidate = VENV / 'bin' / 'python'
    if not candidate.exists():
        raise FileNotFoundError(f"Virtualenv python not found at {candidate}. Create .venv using setup.sh or python -m venv .venv")
    return str(candidate)


def run_tests(python_exe):
    results = []
    for p in sorted(TESTS_DIR.glob('*.py')):
        start = datetime.utcnow().isoformat() + 'Z'
        env = os.environ.copy()
        # ensure tests can import the local `app` package
        env['PYTHONPATH'] = str(ROOT) + os.pathsep + env.get('PYTHONPATH', '')
        proc = subprocess.run([python_exe, str(p)], capture_output=True, text=True, env=env)
        end = datetime.utcnow().isoformat() + 'Z'
        results.append({
            'test': p.name,
            'returncode': proc.returncode,
            'stdout': proc.stdout,
            'stderr': proc.stderr,
            'start': start,
            'end': end,
        })
    return results


def write_log(py_exe, results):
    py_ver = subprocess.run([py_exe, '--version'], capture_output=True, text=True).stdout.strip()
    pip_ver = subprocess.run([py_exe, '-m', 'pip', '--version'], capture_output=True, text=True).stdout.strip()
    with LOG_FILE.open('a', encoding='utf-8') as f:
        f.write(f"=== Test run: {datetime.utcnow().isoformat()}Z ===\n")
        f.write(f"Environment: .venv\n")
        f.write(f"Project path: {ROOT}\n")
        f.write(f"Python: {py_ver}\n")
        f.write(f"Pip: {pip_ver}\n\n")
        for r in results:
            f.write(f"-- {r['test']} (exit {r['returncode']}) --\n")
            if r['stdout']:
                f.write(f"STDOUT:\n{r['stdout']}\n")
            if r['stderr']:
                f.write(f"STDERR:\n{r['stderr']}\n")
            f.write('\n')
        f.write('\n')


def append_readme(py_exe):
    readme = ROOT / 'README.md'
    py_ver = subprocess.run([py_exe, '--version'], capture_output=True, text=True).stdout.strip()
    pip_ver = subprocess.run([py_exe, '-m', 'pip', '--version'], capture_output=True, text=True).stdout.strip()
    entry = f"\nEnvironment: .venv | Path: {ROOT} | Python: {py_ver} | Pip: {pip_ver}\n"
    with readme.open('a', encoding='utf-8') as f:
        f.write(entry)


def main():
    try:
        py = venv_python()
    except FileNotFoundError as e:
        print(e, file=sys.stderr)
        sys.exit(2)

    results = run_tests(py)
    write_log(py, results)
    append_readme(py)

    # print concise summary for CLI
    failed = [r for r in results if r['returncode'] != 0]
    print(f"Ran {len(results)} test(s). Failed: {len(failed)}. Full log: {LOG_FILE}")
    sys.exit(1 if failed else 0)


if __name__ == '__main__':
    main()
