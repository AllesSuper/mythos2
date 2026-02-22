from __future__ import annotations

import json
import os
from pathlib import Path

from mythos.errors import StorageError


def mythos_dir() -> Path:
    base = Path.home() / ".mythos"
    base.mkdir(parents=True, exist_ok=True)
    return base


def quests_path() -> Path:
    return mythos_dir() / "quests.json"


def read_json(path: Path) -> dict:
    if not path.exists():
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as e:
        raise StorageError(f"Konnte Datei nicht lesen: {path}") from e


def write_json_atomic(path: Path, data: dict) -> None:
    tmp = path.with_suffix(path.suffix + ".tmp")
    try:
        tmp.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
        os.replace(tmp, path)
    except Exception as e:
        raise StorageError(f"Konnte Datei nicht schreiben: {path}") from e
    finally:
        try:
            if tmp.exists():
                tmp.unlink()
        except Exception:
            pass


def load_store() -> dict:
    return read_json(quests_path())


def save_store(store: dict) -> None:
    write_json_atomic(quests_path(), store)