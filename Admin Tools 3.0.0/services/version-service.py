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

    remote_path = "Admin%20Tools%203.0.0/json/version.lock.json"
    url = f"https://raw.githubusercontent.com/{owner}/{repo}/main/{remote_path}"

    try:
        with urllib.request.urlopen(url) as response:
            data = json.loads(response.read().decode())
            return data.get("version", "0.0.0")
    except Exception:
        return "0.0.0"


# Fetch latest version ONCE so all functions can use it
LATEST_VERSION = get_latest_version()


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

    repo_root = Path(__file__).resolve().parents[2]

    if not (repo_root / ".git").exists():
        print("This application is not a git repository. Update failed.")
        print(f"Checked here: {repo_root}")
        return

    if LATEST_VERSION == "0.0.0":
        print("Could not retrieve latest version from GitHub.")
        return

    if version_tuple(CURRENT_VERSION) >= version_tuple(LATEST_VERSION):
        print("Already up to date.")
        return

    print(f"New version available: {LATEST_VERSION}")
    print("Updating...")

    try:
        os.system(f'cd "{repo_root}" && git pull')
    except Exception:
        print("Git pull failed.")
        return

    try:
        version_path.write_text(json.dumps({"version": LATEST_VERSION}, indent=4))
    except Exception:
        print("Failed to update version.lock.json")
        return

    print("Update complete. Restarting application...")

    subprocess.Popen(["cmd.exe", "/c", "start", "", "pythonw", "start.pyw"], shell=True)
    os._exit(0)


# -----------------------------------------
# auto_update command
# -----------------------------------------


def auto_update(shell):

    auto_update_setting = shell.settings.get("auto_update", "off")

    if auto_update_setting != "on":
        return

    if version_tuple(CURRENT_VERSION) < version_tuple(LATEST_VERSION):
        print(f"Auto-update: updating from {CURRENT_VERSION} to {LATEST_VERSION}...")
        update(shell)
    else:
        print("Auto-update: already up to date.")

# Run auto-update automatically when the service loads
def _auto_update_bootstrap(shell):
    try:
        auto_update(shell)
    except Exception:
        pass