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

def create_restore_point():
    cmd_name = "restore-point"
    cmd_description = "Create a system restore point"
    if not is_admin():
            print("Restore point creation requires administrator privileges.")
            print("Please run the terminal as admin or use the elevate service.")
            return
    print("Creating System Restore Point...")
    run('powershell -command "Checkpoint-Computer -Description \'SystemBackup Tool\' -RestorePointType \'MODIFY_SETTINGS\'"')

def backup_files():
    cmd_name = "backup-files"
    cmd_description = "Backup documents, pictures, music, and vidoes to a drive"
    print("\nBacking up key folders...")

    run('xcopy "%USERPROFILE%\\Documents" "%SystemDrive%\\Backup\\Documents" /E /I /Y')
    run('xcopy "%USERPROFILE%\\Pictures" "%SystemDrive%\\Backup\\Pictures" /E /I /Y')
    run('xcopy "%USERPROFILE%\\Music" "%SystemDrive%\\Backup\\Music" /E /I /Y')
    run('xcopy "%USERPROFILE%\\Videos" "%SystemDrive%\\Backup\\Videos" /E /I /Y')

    print("\nBackup complete. Folders saved to %SystemDrive%\\Backup")