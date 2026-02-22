from __future__ import annotations

import hashlib
from datetime import date

from mythos.registry import register


@register("daily", "Täglicher Prompt: daily")
def daily_cmd(args: list[str]) -> int:
    today = date.today().isoformat()
    seed = int(hashlib.sha256(today.encode("utf-8")).hexdigest(), 16)

    prompts = [
        "Welche Tür würdest du heute öffnen, wenn niemand zusieht?",
        "Was ist deine stärkste Waffe, wenn du keine hast?",
        "Welcher Ort in dir ist unerforscht?",
        "Welche Wahrheit würdest du leise notieren?",
        "Was würdest du einem jüngeren Helden raten?",
        "Worin bist du heute mutig, ohne laut zu sein?",
    ]

    p = prompts[seed % len(prompts)]
    print(f"📅 {today}")
    print(f"✨ Prompt: {p}")
    return 0