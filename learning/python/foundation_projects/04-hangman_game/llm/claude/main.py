"""Terminal Hangman. Run with: python3 main.py"""

import random
from pathlib import Path

MAX_ATTEMPTS = 6
WORDS_FILE = Path(__file__).parent / "words.txt"


def load_categories() -> dict[str, list[str]]:
    """Read lines like `animals: otter, giraffe` into {"animals": ["otter", ...]}."""
    categories: dict[str, list[str]] = {}

    for line in WORDS_FILE.read_text(encoding="utf-8").splitlines():
        name, colon, words = line.strip().partition(":")
        if colon and not name.startswith("#"):
            categories[name.strip()] = [w.strip().lower() for w in words.split(",") if w.strip()]

    return categories


def choose_category(categories: dict[str, list[str]]) -> str:
    names = sorted(categories)

    print("\nCategories:")
    for number, name in enumerate(names, start=1):
        print(f"  {number}. {name}")

    while True:
        answer = input("Pick a category number: ").strip()
        if answer.isdigit() and 1 <= int(answer) <= len(names):
            return names[int(answer) - 1]
        print(f"Type a number between 1 and {len(names)}.")


def play(secret: str) -> None:
    guessed: set[str] = set()
    attempts = MAX_ATTEMPTS

    while attempts and not set(secret) <= guessed:
        masked = " ".join(letter if letter in guessed else "_" for letter in secret)
        print(f"\n{masked}   ({attempts} attempts left)")
        if guessed:
            print(f"Tried: {' '.join(sorted(guessed))}")

        guess = input("Type a letter: ").strip().lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Type exactly one letter.")
        elif guess in guessed:
            print(f"You already tried '{guess}'.")
        else:
            guessed.add(guess)
            if guess in secret:
                print("Correct.")
            else:
                attempts -= 1
                print("Wrong.")

    result = "won" if set(secret) <= guessed else "lost"
    print(f"\nYou {result}. The word was '{secret}'.")


def main() -> None:
    categories = load_categories()
    words = categories[choose_category(categories)]
    play(random.choice(words))


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nBye.")
