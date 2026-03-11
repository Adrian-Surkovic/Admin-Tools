import os
import ctypes

description = "Backs up user files or creates a full system restore point."

# This will be set by your settings-service later.
# Valid options: "none", "restore_point", "file_backup", "both"
backup_mode = "none"

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def run(cmd):
    print(f"\n[Running] {cmd}")
    os.system(cmd)

def create_restore_point():
    print("Creating System Restore Point...")
    run('powershell -command "Checkpoint-Computer -Description \'SystemBackup Tool\' -RestorePointType \'MODIFY_SETTINGS\'"')

def backup_files():
    print("\nBacking up key folders...")

    run('xcopy "%USERPROFILE%\\Documents" "%SystemDrive%\\Backup\\Documents" /E /I /Y')
    run('xcopy "%USERPROFILE%\\Pictures" "%SystemDrive%\\Backup\\Pictures" /E /I /Y')
    run('xcopy "%USERPROFILE%\\Music" "%SystemDrive%\\Backup\\Music" /E /I /Y')
    run('xcopy "%USERPROFILE%\\Videos" "%SystemDrive%\\Backup\\Videos" /E /I /Y')

    print("\nBackup complete. Folders saved to %SystemDrive%\\Backup")

def main():
    if backup_mode == "none":
        print("Backup module loaded. No action selected.")
        print("Use settings to choose: file backup, restore point, or both.")
        return

    if backup_mode in ("restore_point", "both"):
        if not is_admin():
            print("Restore point creation requires administrator privileges.")
            print("Please run the terminal as admin or use the elevate service.")
            return
        create_restore_point()

    if backup_mode in ("file_backup", "both"):
        backup_files()