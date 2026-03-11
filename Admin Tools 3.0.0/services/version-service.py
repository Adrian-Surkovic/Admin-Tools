import os
import subprocess
# #import settings from either settings.json, load_settings in main, or settings-service
# # "auto_update": "off" default
# auto_update = "off"


# def auto_update(shell):
#     #This command will run once automatically each time the program starts
#     current = "" #add code the grab the curent version 
#     #(maybe embed version="" in the metadata of start.pyw? or add version tag to git?)
#     latest = "" #add code to grab the latest version from github

#     if auto_update == "on":
#         if current != latest:
#             print("Updating...")
#         #add in code to git pull the latest version
#             subprocess.Popen(["cmd.exe", "/c", "start", "", "pythonw", "start.pyw"], shell=True)
#             os._exit(0)
#         elif current == latest:
#             print("Up to date")
#             return
#         else:
#             return

def version(shell):
    cmd_name = "version"
    cmd_description = "shows the version of the application"
    print("Admin Tools v3.0.0")

def update(shell):
    cmd_name = "update"
    cmd_description = "checks for updates and applies them"
    print("This feature is not implemented yet. Please check back later.")


# def rollback(shell):
#     cmd_name = "rollback"
#     cmd_description = "rolls back to the previous version"
#     print("This feature is not implemented yet. Please check back later.")w

# auto_update()