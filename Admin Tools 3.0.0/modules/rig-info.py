import os

description = "Displays your computers info"


def run(cmd):
    print(f"\n[Running] {cmd}")
    os.system(cmd)


def main():
    print("[CPU]")
    run(
        'powershell "Get-CimInstance Win32_Processor | Format-Table Name, MaxClockSpeed, NumberOfCores"'
    )

    print("\n[GPU]")
    run(
        'powershell "Get-CimInstance Win32_VideoController | Format-Table Name, DriverVersion"'
    )

    print("\n[RAM]")
    run(
        'powershell "Get-CimInstance Win32_PhysicalMemory | Select-Object Manufacturer, Capacity, Speed | Format-Table"'
    )

    print("\n[Installed RAM Total]")
    run('powershell "(Get-CimInstance Win32_ComputerSystem).TotalPhysicalMemory / 1GB"')

    print("\n[Motherboard]")
    run(
        'powershell "Get-CimInstance Win32_BaseBoard | Format-Table Manufacturer, Product, Version"'
    )

    print("\n[Storage]")
    run(
        'powershell "Get-CimInstance Win32_DiskDrive | Format-Table Model, Size, InterfaceType"'
    )

    print("\n[Monitor(s)]")
    run(
        'powershell "Get-CimInstance Win32_DesktopMonitor | Select Name, ScreenWidth, ScreenHeight | Format-Table"'
    )

    print("\n[Operating System]")
    run(
        'powershell "Get-CimInstance Win32_OperatingSystem | Format-Table Caption, Version, BuildNumber"'
    )

    print("\n[Network]")
    run(
        'powershell "Get-CimInstance Win32_NetworkAdapter | Where-Object { $_.NetConnectionStatus -eq 2 } | Format-Table Name, MACAddress"'
    )

    print("\n[Battery]")
    run(
        'powershell "Get-CimInstance Win32_Battery | Format-Table Name, EstimatedChargeRemaining, BatteryStatus"'
    )

    print("\n[BIOS]")
    run(
        'powershell "Get-CimInstance Win32_BIOS | Format-Table Manufacturer, Version, ReleaseDate"'
    )
