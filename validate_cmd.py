from __future__ import annotations

from mythos.models import Quest
from mythos.registry import register
from mythos.storage import load_store


@register("validate", "Prüft gespeicherte Quests auf Plausibilität")
def validate_cmd(args: list[str]) -> int:
    store = load_store()
    bad: list[str] = []

    for qid, raw in store.items():
        try:
            q = Quest.from_dict(raw)
            if not q.id or not q.title or not q.hook or not isinstance(q.steps, list) or len(q.steps) == 0:
                bad.append(str(qid))
        except Exception:
            bad.append(str(qid))

    if not bad:
        print("✅ Alles okay.")
        return 0

    print("⚠️ Auffällige IDs:")
    for x in bad:
        print(f"  {x}")
    return 1