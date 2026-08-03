"""Game rules for Hangman. Pure functions only: no input(), no print()."""

import random
from pathlib import Path

MAX_ATTEMPTS = 6


def load_categories(path: Path) -> dict[str, list[str]]:
    """Read lines like `animals: otter, giraffe` into {"animals": ["otter", ...]}."""
    categories: dict[str, list[str]] = {}

    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue

        name, _, words = line.partition(":")
        categories[name.strip()] = [word.strip().lower() for word in words.split(",") if word.strip()]

    return categories


def pick_word(words: list[str]) -> str:
    return random.choice(words)


def mask_word(secret: str, guessed: set[str]) -> str:
    """mask_word("python", {"p", "n"}) -> "p _ _ _ _ n"."""
    return " ".join(letter if letter in guessed else "_" for letter in secret)


def is_won(secret: str, guessed: set[str]) -> bool:
    """True when every letter of the secret has been guessed."""
    return set(secret) <= guessed


def validate_guess(guess: str, guessed: set[str]) -> str | None:
    """Return an error message, or None when the guess is acceptable."""
    if len(guess) != 1:
        return "Type exactly one letter."
    if not guess.isalpha():
        return "Letters only."
    if guess in guessed:
        return f"You already tried '{guess}'."
    return None
