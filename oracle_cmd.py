from __future__ import annotations

import random

from mythos.registry import register


@register("oracle", "Orakel: oracle <frage...>")
def oracle_cmd(args: list[str]) -> int:
    q = " ".join(args).strip()
    if not q:
        print("Nutze: oracle <frage...>")
        return 2

    answers = ["Ja", "Nein", "Vielleicht", "Eher ja", "Eher nein", "Frag später", "Unklar"]
    twists = [
        "…aber nur, wenn du etwas loslässt.",
        "…doch ein Verbündeter zweifelt.",
        "…und die Zeit wird knapp.",
        "…aber der Preis ist ein Name.",
        "…und ein Zeichen erscheint im Regen.",
        "…doch die Karte lügt einmal.",
    ]

    a = random.choice(answers)
    t = random.choice(twists)
    print(f"🔮 Frage: {q}")
    print(f"Antwort: {a} — {t}")
    return 0