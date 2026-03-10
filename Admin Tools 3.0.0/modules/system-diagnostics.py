import os
import ctypes

description = "Runs SFC, DISM, CHKDSK and clears CBS logs for system integrity checks"

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def run(cmd):
    print(f"\n[Running] {cmd}")
    os.system(cmd)

def main():
    if not is_admin():
        print("This module requires administrator privileges.")
        print("Please run the terminal as admin or use the elevate service.")
        return

    print("\n[Clearing previous CBS log entries]")
    run(r'del /f /q "%windir%\\Logs\\CBS\\CBS.log" >nul 2>&1')

    print("\n[Checking system files — SFC Verify Only]")
    run("sfc /verifyonly")

    print("\n[Checking system image — DISM ScanHealth]")
    run("DISM /Online /Cleanup-Image /ScanHealth")

    print("\n[Scanning disk status — CHKDSK C:]")
    run("chkdsk C:")