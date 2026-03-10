import os
import ctypes

description = "Tweaks system settings to boost performance"

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

    print("Switching to High Performance mode...")
    run("powercfg /setactive SCHEME_MIN")

    print("\nSetting Processor Performance Boost Mode to Aggressive...")
    run("powercfg -setacvalueindex SCHEME_MIN SUB_PROCESSOR PERFBOOSTMODE 2")
    run("powercfg -setdcvalueindex SCHEME_MIN SUB_PROCESSOR PERFBOOSTMODE 2")

    print("\nApplying updated power settings...")
    run("powercfg /S SCHEME_MIN")

    print("\nDisabling Windows Defender scheduled tasks...")

    run('schtasks /Change /TN "\\Microsoft\\Windows\\Windows Defender\\Windows Defender Scheduled Scan" /Disable')
    run('schtasks /Change /TN "\\Microsoft\\Windows\\Windows Defender\\Windows Defender Verification" /Disable')
    run('schtasks /Change /TN "\\Microsoft\\Windows\\Windows Defender\\Windows Defender Cache Maintenance" /Disable')
    run('schtasks /Change /TN "\\Microsoft\\Windows\\Windows Defender\\Windows Defender Cleanup" /Disable')

    print("\nAll Defender tasks disabled and system fully optimized.")

