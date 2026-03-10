# from pathlib import Path
# import importlib.util

description = "Provides the commands, services, and help menus"

def commands(shell):
    print("\nAvailable commands:")

    print("\nBuilt-In Commands:")
    for name in shell.core_builtins:
        print(f"  {name:<20} - built-in command")

    for name in sorted(shell.dynamic_builtins):
        print(f"  {name:<20} - from services")

    print("\nModular Commands:")
    for name, path in shell.tools.items():
        desc = shell.load_description(path)
        print(f"  {name:<20} - {desc or 'No description provided'}")

    print()

def services(shell):
    print("\nAvailable services:")

    for name, path in shell.services.items():
        module = shell.load_module(path)
        desc = getattr(module, "description", "No description provided")
        print(f"  {name:<20} - {desc}")

    print()

def help(shell):
    print("""
=== Admin Tools Help === 
Show Commands: commands
Show Services: services 
Show Help: Help <-- This menu
""")

def load_description(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line.startswith("description"):
                    # Example: description = "text"
                    parts = line.split("=", 1)
                    if len(parts) == 2:
                        return parts[1].strip().strip('"').strip("'")
        return None
    except:
        return None