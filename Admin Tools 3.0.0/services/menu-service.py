description = "Provides the commands, services, and help menus" #<-- the description is here, make THIS display when i type "services"
# Or make it print menu-service     -

def commands(shell):
    print("\nAvailable commands:")

    print("\nBuilt-In Commands:")
    for cmd in sorted(shell.service_cmds):
        func = shell.service_cmds[cmd]

        # In the old system: svc_module = module containing the command
        # In the new system: we stored module description on the function
        desc = (
            getattr(func, "_service_description", None)
            or getattr(func, "__doc__", None)
            or "No description provided"
        )

        print(f"  {cmd:<20} - {desc}")

    print("\nModular Commands:")
    for cmd in sorted(shell.module_cmds):
        func = shell.module_cmds[cmd]

        # Same logic as above, but for module commands
        desc = (
            getattr(func, "_module_description", None)
            or getattr(func, "__doc__", None)
            or "No description provided"
        )

        print(f"  {cmd:<20} - {desc}")

    print()


def services(shell):
    print("\nAvailable services:\n")

    # In the old system: services were files
    # In the new system: services = service commands
    for cmd in sorted(shell.service_cmds):
        func = shell.service_cmds[cmd]

        desc = (
            getattr(func, "_service_description", None)
            or getattr(func, "__doc__", None)
            or "No description provided"
        )

        print(f"{cmd:<20} - {desc}")

    print()


def help(shell):
    print("""
=== Admin Tools Help ===
Show Commands: commands
Show Services: services
Show Help: help
""")