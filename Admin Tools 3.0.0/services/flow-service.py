import os

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