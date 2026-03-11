from pathlib import Path
import importlib.util
import json
import os
import ast
import inspect


os.system("title Admin Tools")

ROOT = Path(__file__).parent
TOOLS_DIR = ROOT / "modules"
SERVICES_DIR = ROOT / "services"


class Shell:
    def __init__(self):
        self.service_cmds = self.load_service_commands()

    # ------------------------------
    # Settings Loader
    # ------------------------------
    def load_settings(self):
        SETTINGS_PATH = Path(__file__).parent / "json" / "settings.json"
        if not SETTINGS_PATH.exists():
            return {}

        try:
            with open(SETTINGS_PATH, "r") as f:
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

        for dir_path in [SERVICES_DIR, TOOLS_DIR]:
            for py in dir_path.glob("*.py"):
                module = self.load_python_module(py)
                module_name = py.stem.lower()

                for name, func in module.__dict__.items():
                    if not callable(func):
                        continue

                    # Try to read the function source
                    try:
                        source = inspect.getsource(func)
                        tree = ast.parse(source)
                    except Exception:
                        continue

                    cmd_name = None
                    cmd_desc = None

                    # Look for assignments inside the function
                    for node in ast.walk(tree):
                        if isinstance(node, ast.Assign):
                            for target in node.targets:
                                if isinstance(target, ast.Name):

                                    if target.id == "cmd_name" and isinstance(node.value, ast.Constant) and isinstance(node.value.value, str):
                                        cmd_name = node.value.value

                                    if target.id == "cmd_description" and isinstance(node.value, ast.Constant) and isinstance(node.value.value, str):
                                        cmd_desc = node.value.value

                    # Skip functions without both metadata
                    if cmd_name is None or cmd_desc is None:
                        continue

                    # Normalize missing fields
                    if cmd_name is None:
                        cmd_name = name.lower()
                    if cmd_desc is None:
                        cmd_desc = "None"

                    # Attach metadata
                    func._service_name = cmd_name
                    func._service_description = cmd_desc
                    func._service_module = module_name

                    commands[cmd_name.lower()] = func

        return commands




    # ------------------------------
    # Command Execution
    # ------------------------------
    def execute(self, cmd):
        parts = cmd.split()
        head = parts[0].lower()

        # Service commands
        if head in self.service_cmds:
            func = self.service_cmds[head]
            module = getattr(func, "_service_module", "")
            if "-service" in module:
                func(self, *parts[1:])
            else:
                func(*parts[1:])
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