from __future__ import annotations

from mythos.generator import generate
from mythos.models import Quest
from mythos.registry import register
from mythos.storage import load_store, save_store


@register("new", "Erzeugt eine neue Quest und speichert sie")
def new_cmd(args: list[str]) -> int:
    store = load_store()
    data = generate()
    q = Quest.from_dict(data)
    store[q.id] = q.to_dict()
    save_store(store)

    print(f"✅ Neue Quest erstellt: {q.id}")
    print(q.title)
    print(q.hook)
    for i, s in enumerate(q.steps, start=1):
        print(f"  {i}. {s}")
    return 0