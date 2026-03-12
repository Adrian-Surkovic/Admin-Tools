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

def fix_audio():
    cmd_name = "fix-audio"
    cmd_description = "Restarts Windows Audio services to fix sound issues"

    if not is_admin():
        print("This module requires administrator privileges.")
        print("Please run the terminal as admin or use the elevate service.")
        return

    print("\nRestarting Windows Audio services...")

    run("net stop audiosrv /y")
    run("net stop AudioEndpointBuilder /y")

    print("\nWaiting 1 second to ensure smooth restart...")
    run("timeout /T 1 /NOBREAK > nul")

    run("net start audiosrv /y")
    run("net start AudioEndpointBuilder /y")

    print("\nAudio Restart Complete.")
    print("Script complete.")