import os

description = "Displays system battery, memory, processes, graphics, and startup info"

def run(cmd):
    print(f"\n[Running] {cmd}")
    os.system(cmd)

def main():
    print("\n[Battery]")
    run('powercfg /batteryreport /output "%TEMP%\\battery-report.html"')
    print("Battery report saved to: %TEMP%\\battery-report.html")

    print("\n[Memory Modules]")
    run('powershell "Get-CimInstance Win32_PhysicalMemory | Format-Table BankLabel, Capacity, Speed, Manufacturer"')

    print("\n[Active Processes]")
    run('powershell "Get-Process | Sort-Object CPU -Descending | Select-Object Name, CPU, ID | Format-Table -AutoSize"')

    print("\n[Graphics Pipeline]")
    run('powershell "Get-CimInstance Win32_VideoController | Format-Table Name, DriverVersion, VideoModeDescription, CurrentRefreshRate"')

    print("\n[Startup Programs]")
    run('powershell "Get-CimInstance Win32_StartupCommand | Format-Table Name, Command, Location"')