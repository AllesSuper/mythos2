from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any


def now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


@dataclass
class Quest:
    id: str
    title: str
    hook: str
    steps: list[str]
    created_at: str = field(default_factory=now_iso)
    done_at: str | None = None
    tags: list[str] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        return {
            "id": self.id,
            "title": self.title,
            "hook": self.hook,
            "steps": self.steps,
            "created_at": self.created_at,
            "done_at": self.done_at,
            "tags": self.tags,
        }

    @staticmethod
    def from_dict(d: dict[str, Any]) -> "Quest":
        return Quest(
            id=str(d.get("id", "")),
            title=str(d.get("title", "")),
            hook=str(d.get("hook", "")),
            steps=list(d.get("steps", [])),
            created_at=str(d.get("created_at", "")),
            done_at=d.get("done_at", None),
            tags=list(d.get("tags", [])),
        )