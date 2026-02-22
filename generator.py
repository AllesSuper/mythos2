from __future__ import annotations

import random
import secrets


def new_id() -> str:
    return secrets.token_hex(4)


def generate() -> dict:
    patrons = ["Athene", "Hermes", "Hekate", "Odin", "Freya", "Anansi", "Ra", "Morrígan"]
    places = ["Nebelwald", "versunkene Bibliothek", "Basaltklippen", "Mondtempel", "Salzsteppe", "Glaswüste"]
    artifacts = ["Splitter der Wahrheit", "Faden des Schicksals", "Maske des Lachens", "Schlüssel ohne Schloss", "Sternenkarte"]
    obstacles = ["Rätselwächter", "vergessene Sprache", "Vertrag mit Schatten", "Spiegellabyrinth", "Zeitknick"]
    rewards = ["einen Namen, der Türen öffnet", "ein Lied, das Wunden schließt", "einen Funken Mut", "eine neue Sicht", "eine Freundschaft"]

    patron = random.choice(patrons)
    place = random.choice(places)
    artifact = random.choice(artifacts)
    obstacle = random.choice(obstacles)
    reward = random.choice(rewards)

    title = f"Die Prüfung von {patron}"
    hook = f"{patron} flüstert: In der {place} liegt der {artifact}. Doch ein {obstacle} steht im Weg."
    steps = [
        f"Finde einen Hinweis auf den Weg zur {place}.",
        f"Bezahle den Preis des {obstacle} (List, Mut oder ein Geheimnis).",
        f"Berühre den {artifact} und nimm {reward} mit zurück.",
    ]

    return {"id": new_id(), "title": title, "hook": hook, "steps": steps}