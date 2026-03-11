from pathlib import Path
import importlib.util
import json
import os

os.system("title Admin Tools")

ROOT = Path(__file__).parent
TOOLS_DIR = ROOT / "modules"
SERVICES_DIR = ROOT / "services"


class Shell:
    def __init__(self):
        self.service_cmds = self.load_service_commands()
        self.module_cmds = self.load_module_commands()

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
    # Module Loader
    # ------------------------------
    def load_python_module(self, path: Path):
        """Load a Python file as a module."""
        spec = importlib.util.spec_from_file_location(path.stem, path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module

    # ------------------------------
    # Service Command Loader
    # ------------------------------
    def load_service_commands(self):
        commands = {}

        for py in SERVICES_DIR.glob("*.py"):
            module = self.load_python_module(py)
            module_desc = getattr(module, "description", None)

            for name in dir(module):
                if name.startswith("_"):
                    continue

                func = getattr(module, name)
                if not callable(func):
                    continue

                # Attach module-level description if function has none
                if not hasattr(func, "_service_description") and module_desc:
                    func._service_description = module_desc

                commands[name.lower()] = func

        return commands

    # ------------------------------
    # Modular Command Loader
    # ------------------------------
    def load_module_commands(self):
        modules = {}

        for py in TOOLS_DIR.glob("*.py"):
            module = self.load_python_module(py)
            module_name = py.stem.lower()

            module_desc = getattr(module, "description", None)
            subcommands = {}

            for name, func in module.__dict__.items():
                if name.startswith("_") or not callable(func):
                    continue

                # Attach module-level description if function has none
                if not hasattr(func, "_module_description") and module_desc:
                    func._module_description = module_desc

                subcommands[name.lower()] = func

            modules[module_name] = subcommands

        return modules

    # ------------------------------
    # Command Execution
    # ------------------------------
    def execute(self, cmd):
        parts = cmd.split()
        head = parts[0].lower()

        # 1. Service commands
        if head in self.service_cmds:
            func = self.service_cmds[head]
            func(self, *parts[1:])
            return

        # 2. Module namespace
        if head in self.module_cmds:
            module = self.module_cmds[head]

            if len(parts) == 1:
                print(f"Module '{head}' commands:")
                for sub in module:
                    print(f"  {head} {sub}")
                return

            sub = parts[1].lower()
            if sub in module:
                func = module[sub]
                func(self, *parts[2:])
                return

            print(f"Unknown subcommand: {head} {sub}")
            return

        print(f"Unknown command: {cmd}")


# ------------------------------
# Main Loop
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
        if cmd.lower() == "exit":
            break

        try:
            shell.execute(cmd)
        except Exception as e:
            print("\n--- ERROR ---")
            print(e)
            os.system("pause")


if __name__ == "__main__":
    main()