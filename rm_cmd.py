from __future__ import annotations

from mythos.registry import register
from mythos.storage import load_store, save_store


@register("rm", "Löscht eine Quest: rm <id>")
def rm_cmd(args: list[str]) -> int:
    if not args:
        print("Nutze: rm <id>")
        return 2
    qid = args[0].strip()

    store = load_store()
    if qid not in store:
        print(f"Nicht gefunden: {qid}")
        return 2

    deleted = store.pop(qid)
    save_store(store)
    title = str(deleted.get("title", ""))
    print(f"🗑️ Gelöscht: {qid} — {title}")
    return 0