# **Admin Tools – Modular, Script‑Driven Utilities for Windows**

Easily modifiable admin tools covering everything from system, rig, and network information to diagnostics and repair.

---

## **General Notes**
- **All C# code is AI‑generated.**
- **All BAT and Python scripts are hand‑written.**
- **Version 1 has been moved to https://github.com/Adrian-Surkovic/Admin-Tools-Original/tree/main** 
- **Version 2.0 will be removed Feb 14, 2026 due to being virtually impossible to make modular, the google drive link has already been removed.**


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

## **Important Note**
The **SystemBoost** command disables certain Windows Defender scheduled tasks to improve performance.  
This may reduce system protection.  
Use at your own risk — and seriously, don’t download malware.

---

## **Version 3.0.0 (Python Edition)**

Modding support will follow the same philosophy as the original version:  
**simple, modular, drop‑in commands with minimal setup.**

Version 3.0.0 will also introduce the ability to wrap around Command Prompt, PowerShell, or PowerShell 7 and hook directly into their commands.

Additionally, it will include services such as:
- Auto‑updates (disabled by default)
- The option to roll back updates if needed
- Permission elevation to ensure all commands run smoothly
- Clearscreen and other functions either from integration or hardcoding