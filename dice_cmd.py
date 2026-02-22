from __future__ import annotations

import random
import re

from mythos.registry import register


@register("dice", "Würfel: dice 2d6+1 | dice d20 | dice 4d8-2")
def dice_cmd(args: list[str]) -> int:
    if not args:
        print("Nutze: dice <NdM(+/-)K>")
        return 2

    expr = args[0].strip().lower()
    m = re.fullmatch(r"(?:(\d*)d(\d+))(?:([+-])(\d+))?", expr)
    if not m:
        print("Ungültig. Beispiele: 2d6+1, d20, 4d8-2")
        return 2

    n_str, sides_str, op, k_str = m.groups()
    n = int(n_str) if n_str else 1
    sides = int(sides_str)
    k = int(k_str) if k_str else 0
    if n <= 0 or sides <= 1 or n > 200:
        print("Grenzen: n>0, sides>1, n<=200")
        return 2

    rolls = [random.randint(1, sides) for _ in range(n)]
    total = sum(rolls)
    if op == "+":
        total += k
    elif op == "-":
        total -= k

    print(f"🎲 {expr}  -> Rolls: {rolls}  Total: {total}")
    return 0