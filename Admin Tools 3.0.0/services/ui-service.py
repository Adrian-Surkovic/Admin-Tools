import os

description = "Allows the user to customize the look of the terminal"

def color(shell, arg=None):
    cmd_name = "color"
    cmd_description = "changes the terminal color scheme using hex codes (e.g. 0A, 1F, A1)"
    if not arg:
        print("Usage: color <hex>")
        return
    os.system(f"color {arg}")

def title(shell, arg=None):
    cmd_name = "title"
    cmd_description = "changes the terminal title"
    if not arg:
        print("Usage: title <text>")
        return
    os.system(f"title {arg}")