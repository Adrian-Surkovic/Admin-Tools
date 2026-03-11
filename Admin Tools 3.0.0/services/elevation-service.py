import ctypes
from pathlib import Path
import subprocess

description = "Allows the user to switch between base and elevated mode"


def elevate(shell):
    print("Requesting administrator privileges...")

    ROOT = Path(__file__).resolve().parents[1]
    EMBEDDED_PY = ROOT / "src" / "python-3.14.2-embed-amd64" / "python.exe"
    MAIN = ROOT / "main.py"

    # IMPORTANT: embedded Python requires the script path as a single quoted string
    params = f'"{MAIN}"'

    result = ctypes.windll.shell32.ShellExecuteW(
        None, "runas", str(EMBEDDED_PY), params, None, 1
    )

    if result <= 32:
        print("Elevation failed.")
        return

    # Hard exit so the elevated instance takes over
    raise SystemExit
