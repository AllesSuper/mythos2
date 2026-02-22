from __future__ import annotations

from mythos.models import Quest
from mythos.registry import register
from mythos.storage import load_store


@register("find", "Suche in Titel/Hook/Tags: find <text>")
def find_cmd(args: list[str]) -> int:
    if not args:
        print("Nutze: find <text>")
        return 2
    needle = " ".join(args).strip().lower()

    store = load_store()
    quests = [Quest.from_dict(v) for v in store.values()]

    hits: list[Quest] = []
    for q in quests:
        blob = " ".join([q.title, q.hook, " ".join(q.tags)]).lower()
        if needle in blob:
            hits.append(q)

    if not hits:
        print("(Keine Treffer)")
        return 0

    hits.sort(key=lambda q: q.created_at)
    for q in hits:
        status = "✅" if q.done_at else "🗺️"
        print(f"{status} {q.id}  {q.title}")
    return 0