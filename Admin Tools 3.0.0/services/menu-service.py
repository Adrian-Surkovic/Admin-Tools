def commands(shell):
    cmd_name = "commands"
    cmd_description = "shows a list of commands and descriptions"

    print("\nAvailable commands:\n")
 
    modules = []
    built_ins = []

    for cmd in sorted(shell.service_cmds):
        func = shell.service_cmds[cmd]
        module = getattr(func, "_service_module", "unknown")
        desc = (
            getattr(func, "_service_description", None)
            or getattr(func, "cmd_description", None)
            or getattr(func, "__doc__", None)
            or "No description provided"
        )
        if "-service" in module:
            built_ins.append((cmd, desc))
        else:
            modules.append((cmd, desc))

    print("Modules:")
    for cmd, desc in modules:
        print(f"  {cmd:<20} - {desc}")

    print("\nBuilt-ins:")
    for cmd, desc in built_ins:
        print(f"  {cmd:<20} - {desc}")

    print()


def services(shell):
    cmd_name = "services"
    cmd_description = "shows a list of services and contained commands"

    print("\nAvailable services:\n")

    grouped = {}
    for cmd, func in shell.service_cmds.items():
        module = getattr(func, "_service_module", "unknown")
        if "-service" in module:
            grouped.setdefault(module, []).append(cmd)

    # for module, cmds in sorted(grouped.items()):
    #     print(f"[{module}]")
    #     for cmd in sorted(cmds):
    #         print(f"  {cmd}")
    #     print()
    for module, cmds in sorted(grouped.items()):
        cmd_list = ", ".join(sorted(cmds))
        print(f"{module} - {cmd_list}")


def help(shell):
    cmd_name = "help"
    cmd_description = "shows the help menu"

    print("""
=== Admin Tools Help ===
Show Commands: commands
Show Services: services
Show Help: help
""")

def cheese(shell):
    cmd_name = "cheese"
    cmd_description = "prints cheese"

    print("Cheese! 🧀")
