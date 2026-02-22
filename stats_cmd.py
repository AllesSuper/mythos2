from __future__ import annotations

from collections import Counter

from mythos.models import Quest
from mythos.registry import register
from mythos.storage import load_store


@register("stats", "Zeigt Statistiken")
def stats_cmd(args: list[str]) -> int:
    store = load_store()
    quests = [Quest.from_dict(v) for v in store.values()]

    total = len(quests)
    done = sum(1 for q in quests if q.done_at)
    open_ = total - done

    tags = Counter(t for q in quests for t in q.tags)

    print(f"Quests gesamt: {total}")
    print(f"Offen:        {open_}")
    print(f"Erledigt:     {done}")
    print("")
    print("Top-Tags:")
    if not tags:
        print("  -")
        return 0

    for tag, n in tags.most_common(10):
        print(f"  {tag}: {n}")
    return 0