from __future__ import annotations

import random
import secrets

from mythos.config import load_config


def new_id() -> str:
    return secrets.token_hex(4)


def _pool(theme: str) -> dict[str, list[str]]:
    if theme == "scifi":
        return {
            "patrons": ["Archiv-KI ATHENA", "Kurator HERMES", "Hex-Module HEKATE", "Navigator ODIN"],
            "places": ["Orbitruine", "Datenkathedrale", "Asteroidengarten", "Wurmloch-Mausoleum", "Salzmond"],
            "artifacts": ["Quanten-Schlüssel", "Schimmer-Chip", "Sternenkarte v2", "Masken-Protokoll", "Faden-Algorithmus"],
            "obstacles": ["Firewall-Wächter", "Zeitparadoxon", "Spiegel-Simulation", "Schuldvertrag", "vergessener Codec"],
            "rewards": ["Admin-Rechte", "ein neues Muster", "einen Mut-Boost", "eine geheime Route", "einen Verbündeten-Drone"],
        }
    # default: myth
    return {
        "patrons": ["Athene", "Hermes", "Hekate", "Odin", "Freya", "Anansi", "Ra", "Morrígan"],
        "places": ["Nebelwald", "versunkene Bibliothek", "Basaltklippen", "Mondtempel", "Salzsteppe", "Glaswüste"],
        "artifacts": ["Splitter der Wahrheit", "Faden des Schicksals", "Maske des Lachens", "Schlüssel ohne Schloss", "Sternenkarte"],
        "obstacles": ["Rätselwächter", "vergessene Sprache", "Vertrag mit Schatten", "Spiegellabyrinth", "Zeitknick"],
        "rewards": ["einen Namen, der Türen öffnet", "ein Lied, das Wunden schließt", "einen Funken Mut", "eine neue Sicht", "eine Freundschaft"],
    }


def generate() -> dict:
    cfg = load_config()
    theme = str(cfg.get("theme", "myth")).strip().lower()
    p = _pool(theme)

    patron = random.choice(p["patrons"])
    place = random.choice(p["places"])
    artifact = random.choice(p["artifacts"])
    obstacle = random.choice(p["obstacles"])
    reward = random.choice(p["rewards"])

    title = f"Die Prüfung von {patron}"
    hook = f"{patron} flüstert: In der {place} liegt der {artifact}. Doch ein {obstacle} steht im Weg."
    steps = [
        f"Finde einen Hinweis auf den Weg zur {place}.",
        f"Bezahle den Preis des {obstacle} (List, Mut oder ein Geheimnis).",
        f"Berühre den {artifact} und nimm {reward} mit zurück.",
    ]

    return {"id": new_id(), "title": title, "hook": hook, "steps": steps}