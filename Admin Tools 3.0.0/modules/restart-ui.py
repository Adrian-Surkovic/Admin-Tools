import os
import ctypes
import time

def run(cmd):
    print(f"\n[Running] {cmd}")
    os.system(cmd)


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def run(cmd):
    print(f"\n[Running] {cmd}")
    os.system(cmd)

def main():
    cmd_name = "ui-restart"
    cmd_description = "Restarts DWM and Explorer"
    if not is_admin():
        print("This module requires administrator privileges.")
        print("Please run the terminal as admin or use the elevate service.")
        return
    print("Restarting DWM...")
    run("Taskkill /f /im dwm.exe")
    time.sleep(3) #give DWM time to restart automatically
    print("Restarting explorer...")
    run("Taskkill /f /im explorer.exe")
    print("Starting explorer...")
    run("Start explorer.exe")
