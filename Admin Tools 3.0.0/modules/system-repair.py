import os
import ctypes

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def run(cmd):
    print(f"\n[Running] {cmd}")
    os.system(cmd)

def main():
    cmd_name = "system-repair"
    cmd_description = "Repairs system files, system image, and disk using SFC, DISM, and CHKDSK"
    if not is_admin():
        print("This module requires administrator privileges.")
        print("Please run the terminal as admin or use the elevate service.")
        return

    print("\n[Repairing system files — SFC /scannow]")
    run("sfc /scannow")

    print("\n[Repairing system image — DISM /RestoreHealth]")
    run("DISM /Online /Cleanup-Image /RestoreHealth")

    print("\n[Repairing disk — CHKDSK /f /r (restart required)]")
    run('echo Y | chkdsk C: /f /r')