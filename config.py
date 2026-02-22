from __future__ import annotations

from pathlib import Path

from mythos.storage import mythos_dir, read_json, write_json_atomic


def config_path() -> Path:
    return mythos_dir() / "config.json"


def load_config() -> dict:
    cfg = read_json(config_path())
    if not isinstance(cfg, dict):
        return {}
    return cfg


def save_config(cfg: dict) -> None:
    write_json_atomic(config_path(), cfg)