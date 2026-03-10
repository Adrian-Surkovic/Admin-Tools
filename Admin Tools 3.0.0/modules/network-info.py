import os

description = "Displays your networks info"


def run(cmd):
    print(f"\n[Running] {cmd}")
    os.system(cmd)


def main():
    print("[Open Ports & Connections]")
    run("netstat -ano")

    print("\n[IP & Adapter Info]")
    run("ipconfig /all")

    print("\n[Ping Test - Google DNS]")
    run("ping 8.8.8.8 -n 4")

    print("\n[Traceroute - Google DNS]")
    run("tracert 8.8.8.8")

    print("\n[DNS Lookup - Microsoft Domain]")
    run("nslookup www.microsoft.com")

    print("\n[Wi-Fi SSID (if applicable)]")
    run('netsh wlan show interfaces | findstr /R "^....SSID"')

    print("\n[Adapter List - Connected Only]")
    run(
        'powershell "Get-CimInstance Win32_NetworkAdapter | '
        "Where-Object { $_.NetConnectionStatus -eq 2 } | "
        'Format-Table Name, MACAddress"'
    )
