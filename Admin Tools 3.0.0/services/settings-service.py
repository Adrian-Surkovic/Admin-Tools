import json
import os
import sys
import subprocess
from pathlib import Path

description = "Edit persistent terminal settings"

SETTINGS_PATH = Path(__file__).parent.parent / "settings.json"


def settings(shell, arg=None):
    cmd_name = "settings"
    cmd_description = "opens the settings editor for terminal customization"
    # Load settings with empty-file handling
    try:
        raw = SETTINGS_PATH.read_text(encoding="utf-8").strip()
        if raw == "":
            data = {}
        else:
            data = json.loads(raw)
    except Exception:
        print("Warning: settings.json is corrupted or unreadable.")
        data = {}

    print("\n--- Settings Editor ---")
    print(json.dumps(data, indent=4))
    print("\nType 'options' for a list of settings.")
    print("Type 'save' or 'exit' to finish.\n")

    while True:
        cmd = input("Setting> ").strip()

        # Exit or save
        if cmd in ("exit", "save"):
            break

        # Show available settings
        if cmd == "options":
            print("\nEditable settings:")
            print("  color <value>   - Set default terminal color (e.g., 0A, 1F, A1)")
            print("  title <text>    - Set default terminal title")
            print("  save / exit     - Save and restart\n")
            continue

        # Parse commands like: color 0A
        parts = cmd.split(" ", 1)
        if len(parts) != 2:
            print("Invalid command. Type 'options' for help.")
            continue

        key, value = parts[0].lower(), parts[1].strip()

        if key == "color":
            data["default_color"] = value
            print(f"Set default_color = {value}")
        elif key == "title":
            data["default_title"] = value
            print(f"Set default_title = {value}")
        else:
            print("Unknown setting. Type 'options' for help.")

    # Save settings
    with open(SETTINGS_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

    print("\nSettings saved. Restarting terminal...")

    # Relaunch the program in a new console window
    subprocess.Popen(
        ["cmd.exe", "/c", "start", "", "pythonw", "start.pyw"],
        shell=True
    )
    os._exit(0)