from __future__ import annotations

from mythos.registry import all_commands, register


@register("help", "Zeigt Hilfe und alle Befehle")
def help_cmd(args: list[str]) -> int:
    print("MYTHOS — Mythische Quests im Terminal\n")
    print("Aufruf:")
    print("  python mythos_cli.py <befehl> [argumente]\n")
    print("Befehle:")
    for c in all_commands():
        print(f"  {c.name:10} {c.help}")
    return 0