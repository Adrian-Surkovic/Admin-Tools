import os
import subprocess
import json
import urllib.request
from pathlib import Path

# -----------------------------------------
# Load CURRENT version from version.lock.json
# -----------------------------------------

version_path = Path(__file__).parent.parent / "json" / "version.lock.json"

try:
    data = json.loads(version_path.read_text())
    CURRENT_VERSION = data.get("version", "0.0.0")
except Exception:
    CURRENT_VERSION = "0.0.0"


# -----------------------------------------
# Fetch latest version.lock.json from GitHub
# -----------------------------------------

def get_latest_version():
    owner = "Adrian-Surkovic"
    repo = "Admin-Tools"

    url = f"https://raw.githubusercontent.com/{owner}/{repo}/main/json/version.lock.json"

    try:
        with urllib.request.urlopen(url) as response:
            data = json.loads(response.read().decode())
            return data.get("version", "0.0.0")
    except Exception:
        return "0.0.0"


# -----------------------------------------
# Compare semantic versions
# -----------------------------------------

def version_tuple(v):
    return tuple(map(int, v.split(".")))


# -----------------------------------------
# version command
# -----------------------------------------

def version(shell):
    cmd_name = "version"
    cmd_description = "shows the version of the application"
    print(f"Admin Tools {CURRENT_VERSION}")


# -----------------------------------------
# update command
# -----------------------------------------

def update(shell):
    cmd_name = "update"
    cmd_description = "checks for updates and applies them"

    print("Attempting to update...")

    # Detect repo root based on this file's location
    repo_root = Path(__file__).resolve().parents[2]

    # Check for .git folder in the repo root
    if not (repo_root / ".git").exists():
        print("This application is not a git repository. Update failed.")
        print(f"Checked here: {repo_root}")
        return

    latest = get_latest_version()

    if latest == "0.0.0":
        print("Could not retrieve latest version from GitHub.")
        return

    if version_tuple(CURRENT_VERSION) >= version_tuple(latest):
        print("Already up to date.")
        return

    print(f"New version available: {latest}")
    print("Updating...")

    try:
        os.system(f'cd "{repo_root}" && git pull')
    except Exception:
        print("Git pull failed.")
        return

    try:
        version_path.write_text(json.dumps({"version": latest}, indent=4))
    except Exception:
        print("Failed to update version.lock.json")
        return

    print("Update complete. Restarting application...")

    subprocess.Popen(
        ["cmd.exe", "/c", "start", "", "pythonw", "start.pyw"],
        shell=True
    )
    os._exit(0)


# def auto_update(shell):
#     cmd_name = "auto_update"
#     cmd_description = "checks and applies updates automatically"
#     auto_update_setting = shell.settings.get("auto_update", "off")
#     if auto_update == "on":
#         if current != latest:
#             print("Updating...")
#         #add in code to git pull the latest version
#             subprocess.Popen(["cmd.exe", "/c", "start", "", "pythonw", "start.pyw"], shell=True)
#             os._exit(0)
#         elif current == latest:
#             print("Up to date")
#            return
#         else:
#            return
# auto_update()
