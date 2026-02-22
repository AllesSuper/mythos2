from __future__ import annotations

from pathlib import Path

from mythos.models import Quest
from mythos.registry import register
from mythos.storage import load_store, read_json, save_store


@register("import", "Importiert quests: import <datei.json>")
def import_cmd(args: list[str]) -> int:
    if not args:
        print("Nutze: import <datei.json>")
        return 2

    path = Path(args[0]).expanduser()
    if not path.exists():
        print(f"Nicht gefunden: {path}")
        return 2

    incoming = read_json(path)
    if not isinstance(incoming, dict):
        print("Ungültiges Format (erwarte dict).")
        return 2

    store = load_store()
    added = 0
    for k, v in incoming.items():
        try:
            q = Quest.from_dict(v)
            if not q.id:
                q.id = str(k)
            if q.id and q.id not in store:
                store[q.id] = q.to_dict()
                added += 1
        except Exception:
            continue

    save_store(store)
    print(f"📥 Import fertig. Neu hinzugefügt: {added}")
    return 0