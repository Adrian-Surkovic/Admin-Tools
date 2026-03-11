import os

def run(cmd):
    print(f"\n[Running] {cmd}")
    os.system(cmd)

def main():
    cmd_name = "system-info"
    cmd_description = "Displays system battery, memory, processes, graphics, and startup info"
    print("\n[Battery]")
    run('powercfg /batteryreport /output "%TEMP%\\battery-report.html"')
    print("Battery report saved to: %TEMP%\\battery-report.html")

    print("\n[Memory Modules]")
    run('powershell "Get-CimInstance Win32_PhysicalMemory | Format-Table BankLabel, Capacity, Speed, Manufacturer"')

    print("\n[Active Processes]")
    choice = input("Open Task Manager? (y/n): ").strip().lower()

    match choice:
        case "y":
            run('start taskmgr')
        case "n":
            print("Skipping Processes.")
        case _:
            print("Invalid input. Skipping.")
    
    print("\n[Graphics Pipeline]")
    run('powershell "Get-CimInstance Win32_VideoController | Format-Table Name, DriverVersion, VideoModeDescription, CurrentRefreshRate"')

    print("\n[Startup Programs]")
    choice = input("Open Startup Apps? (y/n): ").strip().lower()

    match choice:
        case "y":
            run('start ms-settings:startupapps')
        case "n":
            print("Skipping Startup Apps.")
        case _:
            print("Invalid input. Skipping.")
