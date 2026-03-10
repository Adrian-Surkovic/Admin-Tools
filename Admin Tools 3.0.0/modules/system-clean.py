import os
import ctypes

description = "Performs deep system cleanup: cache, temp files, DNS, ARP, Winsock, and Windows Update"

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

    print("\n[Microsoft Store Cache]")
    run("wsreset.exe")

    print("\nWaiting for Microsoft Store to open...")
    run("timeout /t 5 >nul")

    print("\nClosing Microsoft Store...")
    run("taskkill /F /IM WinStore.App.exe >nul 2>&1")

    print("\n[Windows Update Cache]")
    run("net stop wuauserv")
    run("net stop bits")
    run(r'del /f /s /q "%windir%\\SoftwareDistribution\\Download\\*.*"')

    print("\nRestarting Windows Update services...")
    run("net start wuauserv")
    run("net start bits")

    print("\n[DNS Cache]")
    run("ipconfig /flushdns")

    print("\n[ARP Cache]")
    run("arp -d")

    print("\n[Winsock Reset]")
    run("netsh winsock reset")

    print("\n[Cleaning Temp Files]")
    run(r'del /f /q "%TEMP%\\*"')
    run(r'del /f /q "%SystemRoot%\\Temp\\*"')

    print("\n[Windows Update Component Cleanup]")
    run("Dism /Online /Cleanup-Image /StartComponentCleanup")

    print("\nAll done! Reboot for best results.")