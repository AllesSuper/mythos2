from __future__ import annotations

import sys

import mythos.commands  # noqa: F401

from mythos.errors import MythosError
from mythos.registry import all_commands, get


def main(argv: list[str]) -> int:
    if len(argv) < 2:
        cmd = get("help")
        return cmd.handler([]) if cmd else 2

    cmd_name = argv[1].strip().lower()
    cmd = get(cmd_name)
    if not cmd:
        print(f"Unbekannter Befehl: {cmd_name}")
        print("Verfügbare Befehle:")
        for c in all_commands():
            print(f"  {c.name:10} {c.help}")
        return 2

    try:
        return cmd.handler(argv[2:])
    except MythosError as e:
        print(f"❌ Fehler: {e}")
        return 2


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))