from __future__ import annotations

from mythos.models import Quest, now_iso
from mythos.registry import register
from mythos.storage import load_store, save_store


@register("done", "Markiert Quest als erledigt: done <id>")
def done_cmd(args: list[str]) -> int:
    if not args:
        print("Nutze: done <id>")
        return 2
    qid = args[0].strip()

    store = load_store()
    if qid not in store:
        print(f"Nicht gefunden: {qid}")
        return 2

    q = Quest.from_dict(store[qid])
    if q.done_at:
        print("Schon erledigt ✅")
        return 0

    q.done_at = now_iso()
    store[q.id] = q.to_dict()
    save_store(store)
    print(f"✅ Erledigt: {q.id} — {q.title}")
    return 0