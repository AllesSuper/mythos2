from __future__ import annotations

from mythos.config import load_config, save_config
from mythos.registry import register


@register("seed", "Setzt RNG-Seed: seed <zahl> | seed clear")
def seed_cmd(args: list[str]) -> int:
    cfg = load_config()

    if not args:
        print(cfg.get("seed", ""))
        return 0

    if args[0].strip().lower() == "clear":
        cfg.pop("seed", None)
        save_config(cfg)
        print("✅ seed gelöscht")
        return 0

    s = args[0].strip()
    cfg["seed"] = s
    save_config(cfg)
    print(f"✅ seed gesetzt: {s}")
    return 0