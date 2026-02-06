import subprocess
from pathlib import Path
import sys

ROOT = Path(__file__).parent
EMBEDDED_PY = ROOT / "src" / "python-3.14.2-embed-amd64" / "python.exe"
MAIN = ROOT / "main.py"

# Relaunch main.py using embedded Python
subprocess.run([str(EMBEDDED_PY), str(MAIN)])
sys.exit()