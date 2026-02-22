from __future__ import annotations

from mythos.models import Quest
from mythos.registry import register
from mythos.storage import load_store, save_store


@register("tag", "Tags verwalten: tag <id> [add|rm|ls] [tag]")
def tag_cmd(args: list[str]) -> int:
    if len(args) < 1:
        print("Nutze: tag <id> [add|rm|ls] [tag]")
        return 2

    qid = args[0].strip()
    action = (args[1].strip().lower() if len(args) >= 2 else "ls")

    store = load_store()
    if qid not in store:
        print(f"Nicht gefunden: {qid}")
        return 2

    q = Quest.from_dict(store[qid])

    if action == "ls":
        print(", ".join(q.tags) if q.tags else "-")
        return 0

    if len(args) < 3:
        print("Nutze: tag <id> add <tag>  |  tag <id> rm <tag>")
        return 2
    tag = " ".join(args[2:]).strip()

    tags = {t.strip() for t in q.tags if t.strip()}
    if action == "add":
        tags.add(tag)
    elif action in {"rm", "remove", "del"}:
        tags.discard(tag)
    else:
        print("Aktion muss sein: add | rm | ls")
        return 2

    q.tags = sorted(tags, key=lambda s: s.lower())
    store[q.id] = q.to_dict()
    save_store(store)
    print(f"🏷️ Tags: {', '.join(q.tags) if q.tags else '-'}")
    return 0