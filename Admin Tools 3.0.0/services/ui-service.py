import os

description = "Allows the user to customize the look of the terminal"

def color(shell, arg=None):
    if not arg:
        print("Usage: color <hex>")
        return
    os.system(f"color {arg}")

def title(shell, arg=None):
    if not arg:
        print("Usage: title <text>")
        return
    os.system(f"title {arg}")