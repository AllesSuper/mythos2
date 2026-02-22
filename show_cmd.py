from __future__ import annotations

from mythos.models import Quest
from mythos.registry import register
from mythos.storage import load_store


@register("show", "Zeigt Details zu einer Quest: show <id>")
def show_cmd(args: list[str]) -> int:
    if not args:
        print("Nutze: show <id>")
        return 2
    qid = args[0].strip()

    store = load_store()
    if qid not in store:
        print(f"Nicht gefunden: {qid}")
        return 2

    q = Quest.from_dict(store[qid])
    print(f"ID: {q.id}")
    print(f"Titel: {q.title}")
    print(f"Erstellt: {q.created_at}")
    print(f"Erledigt: {q.done_at or '-'}")
    print(f"Tags: {', '.join(q.tags) if q.tags else '-'}")
    print("")
    print(q.hook)
    print("")
    for i, s in enumerate(q.steps, start=1):
        print(f"{i}. {s}")
    return 0