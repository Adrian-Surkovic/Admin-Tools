import subprocess
from pathlib import Path
import os
os.system("title Admin Tools")

ROOT = Path(__file__).parent
TOOLS_DIR = ROOT / "modules"
built_in = ('help', 'commands')

def list_tools():
    tools = {}
    for py in TOOLS_DIR.glob("*.py"):
        name = py.stem.lower()
        tools[name] = py
    return tools

def run_tool(tool_path):
    subprocess.run(str(tool_path), shell=True)

def main():
    tools = list_tools()

    print("Admin Tools Terminal")
    print(f"Type {built_in[0]} or {built_in[1]} to list commands or 'exit' to quit.\n")

    while True:
        cmd = input("> ").strip().lower()

        if cmd == "exit":
            break

        if cmd == "help" or cmd == "commands":
            print("\nAvailable commands:")
            print("\nBuilt In Commands:")
            for name in built_in:
                print(f"  {name}")
            print("\nModular Commands")
            for name in tools:
                print(f"  {name}")
            print()
            continue

        if cmd in tools:
            run_tool(tools[cmd])
            continue

        print(f"Unknown command: {cmd}")

if __name__ == "__main__":
    main()