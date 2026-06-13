import sys
import os
import site


def print_venv_info() -> None:
    print(f"""MATRIX STATUS: Welcome to the construct

Current Python: {sys.executable}
Virtual Environment: {os.path.basename(sys.prefix)}
Environment Path: {sys.prefix}

SUCCESS: You're in an isolated environment!
Safe to install packages without affecting
the global system.
Package installation path:
{site.getsitepackages()[0]}
""", end='')


def print_no_venv_warning() -> None:
    print(f"""MATRIX STATUS: You’re still plugged in

Current Python: {sys.executable}
Virtual Environment: None detected

WARNING: You're in the global environment!
The machines can see everything you install.

To enter the construct, run:
python -m venv matrix_env
source matrix_env/bin/activate # On Unix
matrix_env\\Scripts\\activate # On Windows

Then run this program again.
""", end='')


if __name__ == "__main__":

    if sys.prefix != sys.base_prefix:
        print_venv_info()
    else:
        print_no_venv_warning()
