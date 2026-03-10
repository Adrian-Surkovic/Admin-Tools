import os

description = "Backs up your documents, pictures, music, and videos"

def run(cmd):
    print(f"\n[Running] {cmd}")
    os.system(cmd)

def main():
    print("Creating System Restore Point...")
    run('powershell -command "Checkpoint-Computer -Description \'SystemBackup Tool\' -RestorePointType \'MODIFY_SETTINGS\'"')

    print("\nBacking up key folders...")

    # Backup Documents
    run('xcopy "%USERPROFILE%\\Documents" "%SystemDrive%\\Backup\\Documents" /E /I /Y')

    # Backup Pictures
    run('xcopy "%USERPROFILE%\\Pictures" "%SystemDrive%\\Backup\\Pictures" /E /I /Y')

    # Backup Music
    run('xcopy "%USERPROFILE%\\Music" "%SystemDrive%\\Backup\\Music" /E /I /Y')

    # Backup Videos
    run('xcopy "%USERPROFILE%\\Videos" "%SystemDrive%\\Backup\\Videos" /E /I /Y')

    print("\nBackup complete. Folders saved to %SystemDrive%\\Backup")

