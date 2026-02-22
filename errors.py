class MythosError(Exception):
    """Basisfehler für kontrollierte CLI-Fehlermeldungen."""


class UserInputError(MythosError):
    """Fehler durch ungültige Nutzereingaben."""


class StorageError(MythosError):
    """Fehler beim Lesen/Schreiben der Daten."""