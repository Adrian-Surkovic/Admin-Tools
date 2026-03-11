from pathlib import Path
import os
import importlib.util
import json

os.system("title Admin Tools")

ROOT = Path(__file__).parent
TOOLS_DIR = ROOT / "modules"
SERVICES_DIR = ROOT / "services"

class Shell:
    def __init__(self):
        self.tools = self.list_tools()
        self.services = self.list_services()
        self.builtins = self.scan_service_builtins()

    # ------------------------------
    # Settings Loader
    # ------------------------------
    def load_settings(self):
        settings_path = ROOT / "settings.json"
        if not settings_path.exists():
            return {}
        try:
            with open(settings_path, "r") as f:
                return json.load(f)
        except Exception:
            print("Warning: settings.json is corrupted or unreadable.")
            return {}

    # ------------------------------
    # Settings Applier
    # ------------------------------
    def apply_settings(self):
        color = self.settings.get("default_color")
        if color:
            os.system(f"color {color}")

        title = self.settings.get("default_title")
        if title:
            os.system(f"title {title}")

    # ------------------------------
    # File scanning
    # ------------------------------
    def list_tools(self):
        return {py.stem.lower(): py for py in TOOLS_DIR.glob("*.py")}

    def list_services(self):
        return {py.stem.lower(): py for py in SERVICES_DIR.glob("*.py")}

    # ------------------------------
    # Unified description loader
    # ------------------------------
    def load_description(self, path):
        try:
            module = self.load_module(path)
            return getattr(module, "description", None)
        except Exception:
            return None

    # ------------------------------
    # Module loading
    # ------------------------------
    def load_module(self, path):
        spec = importlib.util.spec_from_file_location(path.stem, path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module

    def run_module(self, path):
        module = self.load_module(path)
        if hasattr(module, "main"):
            module.main()

    # ------------------------------
    # Built-in scanning
    # ------------------------------
    def scan_service_builtins(self):
        builtins = set()
        for name, path in self.services.items():
            module = self.load_module(path)
            for attr in dir(module):
                if not attr.startswith("_"):
                    if callable(getattr(module, attr)):
                        builtins.add(attr.lower())
        return builtins

    # ------------------------------
    # Built-in description parsing
    # ------------------------------
    def find_service_for_command(self, command):
        for name, path in self.services.items():
            module = self.load_module(path)
            if hasattr(module, command):
                return name, module
        return None, None
    # ------------------------------
    # Built-in execution
    # ------------------------------
    def run_builtin(self, cmd):
        parts = cmd.split(" ", 1)
        name = parts[0]
        arg = parts[1] if len(parts) > 1 else None

        # Find which service file contains this built-in
        for path in self.services.values():
            module = self.load_module(path)
            func = getattr(module, name, None)
            if callable(func):
                try:
                    if arg is not None:
                        func(self, arg)
                    else:
                        func(self)
                except TypeError:
                    print(f"Invalid usage of built-in: {cmd}")
                return

        print(f"Unknown built-in: {cmd}")

# ------------------------------
# Main loop
# ------------------------------
def main():
    shell = Shell()

    shell.settings = shell.load_settings()
    shell.apply_settings()

    print("Admin Tools Terminal")
    print("Type commands, services, or help — or 'exit' to quit.\n")

    while True:
        cmd = input("> ").strip()
        if not cmd:
            continue

        lower = cmd.lower()

        if lower == "exit":
            break

        # Built-ins from services
        if lower.split(" ")[0] in shell.builtins:
            shell.run_builtin(cmd)
            continue

        # Tools
        if lower in shell.tools:
            shell.run_module(shell.tools[lower])
            continue

        # Services (modules with main())
        if lower in shell.services:
            shell.run_module(shell.services[lower])
            continue

        print(f"Unknown command: {cmd}")

if __name__ == "__main__":
    main()