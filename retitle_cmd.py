from __future__ import annotations

from mythos.models import Quest
from mythos.registry import register
from mythos.storage import load_store, save_store


@register("retitle", "Ändert Titel: retitle <id> <neuer titel>")
def retitle_cmd(args: list[str]) -> int:
    if len(args) < 2:
        print("Nutze: retitle <id> <neuer titel>")
        return 2
    qid = args[0].strip()
    new_title = " ".join(args[1:]).strip()

    store = load_store()
    if qid not in store:
        print(f"Nicht gefunden: {qid}")
        return 2

    q = Quest.from_dict(store[qid])
    q.title = new_title
    store[q.id] = q.to_dict()
    save_store(store)
    print(f"✏️ Titel aktualisiert: {q.id} — {q.title}")
    return 0