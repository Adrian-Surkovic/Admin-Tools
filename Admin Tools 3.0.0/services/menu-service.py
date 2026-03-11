description = "Provides the commands, services, and help menus"

def commands(shell):
    print("\nAvailable commands:")

    print("\nBuilt-In Commands:")
    for cmd in sorted(shell.builtins):
        svc_name, svc_module = shell.find_service_for_command(cmd)
        desc = getattr(svc_module, "description", "No description provided")
        print(f"  {cmd:<20} - {desc}")

    print("\nModular Commands:")
    for name, path in shell.tools.items():
        desc = shell.load_description(path)
        print(f"  {name:<20} - {desc or 'No description provided'}")

    print()


def services(shell):
    print("\nAvailable services:\n")

    for name, path in shell.services.items():
        module = shell.load_module(path)

        # Collect commands belonging to this service
        cmds = []
        for cmd in shell.builtins:
            if hasattr(module, cmd):
                cmds.append(cmd)

        # Format EXACTLY how you requested:
        # ui-service           - color, title
        cmd_list = ", ".join(cmds) if cmds else "No commands"

        print(f"{name:<20} - {cmd_list}")

    print()


def help(shell):
    print("""
=== Admin Tools Help ===
Show Commands: commands
Show Services: services
Show Help: help
""")