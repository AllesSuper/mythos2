from __future__ import annotations

from dataclasses import dataclass
from typing import Callable


Handler = Callable[[list[str]], int]


@dataclass(frozen=True)
class Command:
    name: str
    help: str
    handler: Handler


_REGISTRY: dict[str, Command] = {}


def register(name: str, help: str) -> Callable[[Handler], Handler]:
    name = name.strip().lower()

    def deco(fn: Handler) -> Handler:
        _REGISTRY[name] = Command(name=name, help=help, handler=fn)
        return fn

    return deco


def get(name: str) -> Command | None:
    return _REGISTRY.get(name.strip().lower())


def all_commands() -> list[Command]:
    return [cmd for _, cmd in sorted(_REGISTRY.items(), key=lambda kv: kv[0])]