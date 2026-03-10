from pathlib import Path
import os
import importlib.util

os.system("title Admin Tools")

ROOT = Path(__file__).parent
TOOLS_DIR = ROOT / "modules"
SERVICES_DIR = ROOT / "services"

class Shell:
    def __init__(self):
        self.tools = self.list_tools()
        self.services = self.list_services()
        self.core_builtins = {"commands", "services", "help"}
        self.dynamic_builtins = self.scan_service_builtins()

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

    print("Admin Tools Terminal")
    print("Type commands, services, or help — or 'exit' to quit.\n")

    while True:
        cmd = input("> ").strip()
        if not cmd:
            continue

        lower = cmd.lower()

        if lower == "exit":
            break

        # Built-in commands (commands/services/help)
        if lower in shell.core_builtins:
            shell.run_builtin(lower)
            continue

        # Dynamic built-ins from services
        if lower.split(" ")[0] in shell.dynamic_builtins:
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