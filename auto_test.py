import os
import subprocess
import sys

venv_path = '.venv'
python_exe = os.path.join(venv_path, 'Scripts', 'python.exe') if os.name == 'nt' else os.path.join(venv_path, 'bin', 'python')
log_file = 'logs/test_run.log'

env = dict(os.environ, PYTHONPATH=os.getcwd())

with open(log_file, 'w') as log:
    for test_file in os.listdir('tests'):
        if test_file.endswith('.py'):
            log.write(f"Running {test_file}\n")
            result = subprocess.run([python_exe, os.path.join('tests', test_file)], capture_output=True, text=True, env=env)
            log.write(result.stdout)
            if result.stderr:
                log.write(result.stderr)
            log.write("\n")

# Append environment info to README.md
with open('README.md', 'a') as readme:
    readme.write(f"\nEnvironment: {venv_path}\n")
    readme.write(f"Absolute Path: {os.getcwd()}\n")
    readme.write(f"Python Version: {sys.version}\n")
    try:
        import pip
        readme.write(f"Pip Version: {pip.__version__}\n")
    except ImportError:
        readme.write("Pip Version: Not available\n")