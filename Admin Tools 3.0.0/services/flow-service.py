import os
import subprocess
from pathlib import Path

description = "Allows the user to control the flow of the terminal"

def echo(shell, arg=None):
    if arg is None:
        print()
    else:
        print(arg)

def pause(shell):
    os.system("pause")

def cls(shell):
    os.system("cls")

def restart(shell, arg=None):
    
    print("Restarting terminal...")
    # Launch the new instance
    subprocess.Popen(["cmd.exe", "/c", "start", "", "pythonw", "start.pyw"], shell=True)
    os._exit(0)