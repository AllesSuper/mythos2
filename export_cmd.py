from __future__ import annotations

from pathlib import Path

from mythos.models import Quest
from mythos.registry import register
from mythos.storage import load_store


@register("export", "Exportiert Quest als Markdown: export <id> [pfad.md]")
def export_cmd(args: list[str]) -> int:
    if not args:
        print("Nutze: export <id> [pfad.md]")
        return 2

    qid = args[0].strip()
    out = Path(args[1]).expanduser() if len(args) >= 2 else Path(f"{qid}.md")

    store = load_store()
    if qid not in store:
        print(f"Nicht gefunden: {qid}")
        return 2

    q = Quest.from_dict(store[qid])

    lines = []
    lines.append(f"# {q.title}")
    lines.append("")
    lines.append(f"- ID: `{q.id}`")
    lines.append(f"- Erstellt: {q.created_at}")
    lines.append(f"- Erledigt: {q.done_at or '-'}")
    lines.append(f"- Tags: {', '.join(q.tags) if q.tags else '-'}")
    lines.append("")
    lines.append("## Hook")
    lines.append("")
    lines.append(q.hook)
    lines.append("")
    lines.append("## Schritte")
    lines.append("")
    for i, s in enumerate(q.steps, start=1):
        lines.append(f"{i}. {s}")
    lines.append("")

    out.write_text("\n".join(lines), encoding="utf-8")
    print(f"📄 Exportiert: {out}")
    return 0