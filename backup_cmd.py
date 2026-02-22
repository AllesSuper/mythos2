from __future__ import annotations

from datetime import datetime
from pathlib import Path
import shutil

from mythos.registry import register
from mythos.storage import quests_path


@register("backup", "Backup quests.json: backup [zielordner]")
def backup_cmd(args: list[str]) -> int:
    src = quests_path()
    if not src.exists():
        print("(Noch keine quests.json vorhanden)")
        return 0

    target_dir = Path(args[0]).expanduser() if args else src.parent
    target_dir.mkdir(parents=True, exist_ok=True)

    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    dst = target_dir / f"quests_{stamp}.json"
    shutil.copy2(src, dst)
    print(f"🧷 Backup erstellt: {dst}")
    return 0