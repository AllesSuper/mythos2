from __future__ import annotations

import sys


def main(argv: list[str]) -> int:
    if len(argv) < 2:
        print("MYTHOS: Nutze 'python mythos_cli.py help'")
        return 2

    cmd = argv[1].strip().lower()
    if cmd in {"help", "-h", "--help"}:
        print("MYTHOS (noch minimal)")
        print("Bald verfügbar: new, list, show, done, export, oracle, dice ...")
        return 0

    print(f"Unbekannter Befehl: {cmd}")
    print("Nutze: python mythos_cli.py help")
    return 2


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))