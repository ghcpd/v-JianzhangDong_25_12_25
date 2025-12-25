#!/usr/bin/env python
"""
Auto-test runner for the project.

This script:
1. Detects the virtual environment
2. Runs all test scripts in the tests/ directory
3. Logs all results to logs/test_run.log
4. Appends environment information to README.md
"""

import os
import sys
import subprocess
import glob
from pathlib import Path
from datetime import datetime


def get_python_info():
    """Get Python and pip version information."""
    python_version = f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"
    python_executable = sys.executable
    
    # Get pip version
    try:
        result = subprocess.run(
            [python_executable, "-m", "pip", "--version"],
            capture_output=True,
            text=True
        )
        pip_version = result.stdout.strip()
    except Exception as e:
        pip_version = f"Error getting pip version: {e}"
    
    return {
        "python_version": python_version,
        "python_executable": python_executable,
        "pip_version": pip_version
    }


def get_venv_info():
    """Get virtual environment information."""
    venv_path = os.path.abspath(".venv")
    if os.path.exists(venv_path):
        return {
            "venv_path": venv_path,
            "venv_exists": True,
            "venv_name": "venv"
        }
    return {
        "venv_path": "Not found",
        "venv_exists": False,
        "venv_name": "N/A"
    }


def ensure_logs_directory():
    """Create logs directory if it doesn't exist."""
    logs_dir = Path("logs")
    logs_dir.mkdir(exist_ok=True)
    return logs_dir


def run_test_file(test_file, log_file):
    """Run a single test file and log results."""
    test_name = os.path.basename(test_file)
    log_file.write(f"\n{'='*80}\n")
    log_file.write(f"Running: {test_name}\n")
    log_file.write(f"Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    log_file.write(f"{'='*80}\n")
    log_file.flush()
    
    try:
        # Set up environment with project root in PYTHONPATH
        env = os.environ.copy()
        project_root = os.path.abspath(".")
        pythonpath = env.get("PYTHONPATH", "")
        if pythonpath:
            env["PYTHONPATH"] = f"{project_root}{os.pathsep}{pythonpath}"
        else:
            env["PYTHONPATH"] = project_root
        
        result = subprocess.run(
            [sys.executable, test_file],
            capture_output=True,
            text=True,
            timeout=60,
            env=env
        )
        
        log_file.write("STDOUT:\n")
        log_file.write(result.stdout)
        log_file.write("\n")
        
        if result.stderr:
            log_file.write("STDERR:\n")
            log_file.write(result.stderr)
            log_file.write("\n")
        
        if result.returncode == 0:
            log_file.write(f"Status: PASSED\n")
            return True
        else:
            log_file.write(f"Status: FAILED (Exit code: {result.returncode})\n")
            return False
            
    except subprocess.TimeoutExpired:
        log_file.write("Status: TIMEOUT (exceeded 60 seconds)\n")
        return False
    except Exception as e:
        log_file.write(f"Status: ERROR - {str(e)}\n")
        return False


def main():
    """Main function to run all tests."""
    print("=" * 80)
    print("Auto Test Runner")
    print("=" * 80)
    
    # Get environment information
    py_info = get_python_info()
    venv_info = get_venv_info()
    
    print(f"\nPython Version: {py_info['python_version']}")
    print(f"Python Executable: {py_info['python_executable']}")
    print(f"Virtual Environment: {venv_info['venv_path']}")
    print(f"Pip Version: {py_info['pip_version'].split()[1] if 'pip' in py_info['pip_version'] else 'Unknown'}")
    
    # Ensure logs directory exists
    logs_dir = ensure_logs_directory()
    log_path = logs_dir / "test_run.log"
    
    # Open log file
    with open(log_path, "w") as log_file:
        # Write header
        log_file.write("=" * 80 + "\n")
        log_file.write("AUTO TEST RUN LOG\n")
        log_file.write("=" * 80 + "\n\n")
        log_file.write(f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        
        log_file.write("ENVIRONMENT INFORMATION:\n")
        log_file.write(f"  Python Version: {py_info['python_version']}\n")
        log_file.write(f"  Python Executable: {py_info['python_executable']}\n")
        log_file.write(f"  Virtual Environment: {venv_info['venv_path']}\n")
        log_file.write(f"  {py_info['pip_version']}\n\n")
        
        # Find and run all test files
        test_files = sorted(glob.glob("tests/case_*.py"))
        
        if not test_files:
            print("\nNo test files found in tests/ directory.")
            log_file.write("No test files found in tests/ directory.\n")
            return
        
        print(f"\nFound {len(test_files)} test file(s):")
        for test_file in test_files:
            print(f"  - {test_file}")
        
        # Run each test
        results = {}
        for test_file in test_files:
            test_name = os.path.basename(test_file)
            passed = run_test_file(test_file, log_file)
            results[test_name] = passed
        
        # Write summary
        log_file.write(f"\n{'='*80}\n")
        log_file.write("TEST SUMMARY\n")
        log_file.write(f"{'='*80}\n")
        
        passed_count = sum(1 for v in results.values() if v)
        failed_count = len(results) - passed_count
        
        log_file.write(f"Total Tests: {len(results)}\n")
        log_file.write(f"Passed: {passed_count}\n")
        log_file.write(f"Failed: {failed_count}\n")
        log_file.write(f"Success Rate: {(passed_count/len(results)*100):.1f}%\n\n")
        
        for test_name, passed in results.items():
            status = "PASSED" if passed else "FAILED"
            log_file.write(f"  {test_name}: {status}\n")
    
    # Print summary to console
    print(f"\n{'='*80}")
    print("TEST SUMMARY")
    print(f"{'='*80}")
    passed_count = sum(1 for v in results.values() if v)
    failed_count = len(results) - passed_count
    print(f"Total Tests: {len(results)}")
    print(f"Passed: {passed_count}")
    print(f"Failed: {failed_count}")
    if len(results) > 0:
        print(f"Success Rate: {(passed_count/len(results)*100):.1f}%")
    
    print(f"\nLog file saved to: {log_path.absolute()}")
    
    # Update README.md with environment information
    update_readme(py_info, venv_info)
    
    # Return appropriate exit code
    sys.exit(0 if failed_count == 0 else 1)


def update_readme(py_info, venv_info):
    """Update README.md with environment information."""
    readme_path = Path("README.md")
    
    env_section = f"""

## Environment Setup Information

**Last Updated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

### Python Environment
- **Python Version:** {py_info['python_version']}
- **Python Executable:** {py_info['python_executable']}
- **Virtual Environment Name:** {venv_info['venv_name']}
- **Virtual Environment Path:** {venv_info['venv_path']}
- **{py_info['pip_version']}**

### Execution
- Test results are logged to: `logs/test_run.log`
- Run auto_test.py to execute all tests and generate logs
"""
    
    if readme_path.exists():
        with open(readme_path, "r", encoding="utf-8") as f:
            content = f.read()
        
        # Remove old environment section if it exists
        if "## Environment Setup Information" in content:
            content = content.split("## Environment Setup Information")[0].rstrip()
        
        with open(readme_path, "w", encoding="utf-8") as f:
            f.write(content)
            f.write(env_section)
    
    print(f"✓ README.md updated with environment information")


if __name__ == "__main__":
    main()
