import os
import subprocess
from pathlib import Path

def echo(shell, arg=None):
    if arg is None:
        print()
    else:
        print(arg)

def pause(shell):
    cmd_name = "pause"
    cmd_description = "pauses the terminal"
    os.system("pause")



def cls(shell):
    cmd_name = "cls"
    cmd_description = "clears the screen"
    os.system("cls")

def restart(shell, arg=None):
    cmd_name = "restart"
    cmd_description = "restarts the terminal"
    print("Restarting terminal...")
    # Launch the new instance
    subprocess.Popen(["cmd.exe", "/c", "start", "", "pythonw", "start.pyw"], shell=True)
    os._exit(0)