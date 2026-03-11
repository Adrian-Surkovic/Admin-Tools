# **Admin Tools – Modular, Script‑Driven Utilities for Windows**
![Admin Tools Banner](image.png)

Easily modifiable admin tools covering everything from system, rig, and network information to diagnostics and repair.

---

## **Original Version**
- **Version 1 has been moved to https://github.com/Adrian-Surkovic/Admin-Tools-Original/tree/main** 


## **Usage & Licensing**
You may use, modify, and distribute this program for any purpose, **as long as you credit the original author**.

---

## **Requirements**
- **System:** Windows 10 or Windows 11  
- **Path Variables:** `ipconfig`, `sfc`, `chkdsk`  
- **Privileges:** Administrator rights required for most commands

---

## **Disclaimer**
I am not responsible for any misuse of this program in illegal or unethical contexts.

---

## **Important Notes**
The **system-boost** command disables certain Windows Defender scheduled tasks to improve performance.  
This may reduce system protection.  
Use at your own risk — and seriously, don’t download malware.

The **system-backup** command will not backup folders saved to Onedrive. This is a known non-issue as it means the things you are trying to backup are already saved. 

---

## **Version 3.0.0 (Python Edition)**

Modding support will follow the same philosophy as the original version:  
**simple, modular, drop‑in commands with minimal setup.**

Version 3.0.0 will also (eventually) introduce the ability to wrap around Command Prompt, PowerShell, or PowerShell 7 and hook directly into their commands.

Additionally, it will include services such as:
- Auto‑updates (disabled by default)
- The option to roll back updates if needed (once Git tags are implemented)
- Permission elevation to ensure all commands run smoothly
- Clearscreen and other functions either from integration or hardcoding

## **File Structure**
```
Admin Tools 3.0.0/
│
├── modules/          # Drop‑in commands (system, network, rig, etc.)
├── services/         # Core services (update, rollback, elevation)
├── src/              # Embedded runtimes (fallback)
│   ├── powershell7/
│   └── python-3.14.2-embed-amd64/
│
├── main.py           # Main entry point
├── start.pyw         # GUI/shortcut launcher
├── TODO.md           # Development notes
└── README.md
```
## **Basic Usage**
To run the program, double click the **start.pyw** bootstrapper, it will auto detect if python is present on your device and fallback to the embedded python if it isn't. 
To enter admin mode, run the **elevate** command. 
To modify or add modules, simply drop in or edit files py in the **/modules** folder. 
To modify or add services, simply drop in or edit py files in the **/services** folder.

## **Changing Settings**
To change settings, you must first run the **settings** command. This will enter a settings prompt where you can change settings. Type **options** for a list of settings.

## ** Custom Module / Service Template **
```py
imports
def function(shell):
    cmd_name=""
    cmd_description=""
```
# Notes: #
1. **Modules** are user facing commands whereas **Services** can directly affect the way the terminal works.
2. Multiple functions can be defined, only functions with **cmd_name** and **cmd_description** will be loaded.
3. if you put ```function()`` at the end of your module or service it will auto run.  