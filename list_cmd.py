from __future__ import annotations

from mythos.models import Quest
from mythos.registry import register
from mythos.storage import load_store


@register("list", "Listet Quests (offen/erledigt)")
def list_cmd(args: list[str]) -> int:
    mode = (args[0].strip().lower() if args else "open")
    if mode not in {"open", "done", "all"}:
        print("Nutze: list [open|done|all]")
        return 2

    store = load_store()
    quests = [Quest.from_dict(v) for v in store.values()]

    def want(q: Quest) -> bool:
        if mode == "all":
            return True
        if mode == "open":
            return q.done_at is None
        return q.done_at is not None

    rows = [q for q in quests if want(q)]
    rows.sort(key=lambda q: (q.done_at is not None, q.created_at), reverse=False)

    if not rows:
        print("(Keine Treffer)")
        return 0

    for q in rows:
        status = "✅" if q.done_at else "🗺️"
        print(f"{status} {q.id}  {q.title}")
    return 0