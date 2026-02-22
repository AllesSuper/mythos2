from __future__ import annotations

from mythos.config import load_config, save_config
from mythos.registry import register


@register("config", "Config lesen/schreiben: config [get <k>] | [set <k> <v>]")
def config_cmd(args: list[str]) -> int:
    cfg = load_config()

    if not args:
        if not cfg:
            print("(leer)")
            return 0
        for k in sorted(cfg.keys(), key=lambda s: s.lower()):
            print(f"{k}={cfg[k]}")
        return 0

    action = args[0].strip().lower()
    if action == "get":
        if len(args) < 2:
            print("Nutze: config get <key>")
            return 2
        k = args[1].strip()
        print(cfg.get(k, ""))
        return 0

    if action == "set":
        if len(args) < 3:
            print("Nutze: config set <key> <value>")
            return 2
        k = args[1].strip()
        v = " ".join(args[2:]).strip()
        cfg[k] = v
        save_config(cfg)
        print(f"✅ gesetzt: {k}={v}")
        return 0

    print("Nutze: config | config get <k> | config set <k> <v>")
    return 2