"""A clean, terminal-based Hangman game."""

import random
import string
from collections.abc import Callable


WORDS = (
    "algorithm",
    "computer",
    "developer",
    "function",
    "keyboard",
    "program",
    "python",
    "terminal",
    "variable",
)

MAX_WRONG_GUESSES = 6

HANGMAN_PICTURES = (
    """
     +---+
     |   |
         |
         |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
         |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
     |   |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =========
    """,
    r"""
     +---+
     |   |
     O   |
    /|\  |
         |
         |
    =========
    """,
    r"""
     +---+
     |   |
     O   |
    /|\  |
    /    |
         |
    =========
    """,
    r"""
     +---+
     |   |
     O   |
    /|\  |
    / \  |
         |
    =========
    """,
)

InputFunction = Callable[[str], str]
OutputFunction = Callable[[str], None]


def choose_word() -> str:
    """Return a random secret word."""
    return random.choice(WORDS)


def word_progress(secret_word: str, guessed_letters: set[str]) -> str:
    """Show guessed letters and hide the rest with underscores."""
    return " ".join(
        letter if letter in guessed_letters else "_" for letter in secret_word
    )


def word_is_complete(secret_word: str, guessed_letters: set[str]) -> bool:
    """Return whether every letter in the secret word has been guessed."""
    return set(secret_word) <= guessed_letters


def ask_for_guess(
    guessed_letters: set[str],
    input_fn: InputFunction = input,
    output_fn: OutputFunction = print,
) -> str:
    """Prompt until the player enters one new English letter."""
    while True:
        guess = input_fn("Guess a letter: ").strip().lower()

        if len(guess) != 1 or guess not in string.ascii_lowercase:
            output_fn("Please enter exactly one letter (a-z).")
        elif guess in guessed_letters:
            output_fn(f"You already guessed '{guess}'. Try another letter.")
        else:
            return guess


def show_game(
    secret_word: str,
    guessed_letters: set[str],
    wrong_guesses: int,
    output_fn: OutputFunction = print,
) -> None:
    """Display the current state of the round."""
    guessed = " ".join(sorted(guessed_letters)) or "none"
    remaining = MAX_WRONG_GUESSES - wrong_guesses

    output_fn(HANGMAN_PICTURES[wrong_guesses].strip("\n"))
    output_fn(f"\nWord:     {word_progress(secret_word, guessed_letters)}")
    output_fn(f"Guessed:  {guessed}")
    output_fn(f"Attempts: {remaining}\n")


def play_round(
    secret_word: str,
    input_fn: InputFunction = input,
    output_fn: OutputFunction = print,
) -> bool:
    """Play one round and return True when the player wins."""
    guessed_letters: set[str] = set()
    wrong_guesses = 0

    while wrong_guesses < MAX_WRONG_GUESSES and not word_is_complete(
        secret_word, guessed_letters
    ):
        show_game(secret_word, guessed_letters, wrong_guesses, output_fn)
        guess = ask_for_guess(guessed_letters, input_fn, output_fn)
        guessed_letters.add(guess)

        if guess not in secret_word:
            wrong_guesses += 1

    show_game(secret_word, guessed_letters, wrong_guesses, output_fn)

    if word_is_complete(secret_word, guessed_letters):
        output_fn(f"You won! The word was '{secret_word}'.")
        return True

    output_fn(f"You lost. The word was '{secret_word}'.")
    return False


def ask_to_play_again(input_fn: InputFunction = input) -> bool:
    """Ask whether another round should start."""
    while True:
        answer = input_fn("\nPlay again? [y/n]: ").strip().lower()
        if answer in {"y", "yes"}:
            return True
        if answer in {"n", "no"}:
            return False
        print("Please enter 'y' or 'n'.")


def main() -> None:
    """Run Hangman until the player chooses to stop."""
    print("Welcome to Hangman!")

    try:
        while True:
            play_round(choose_word())
            if not ask_to_play_again():
                break
    except (EOFError, KeyboardInterrupt):
        print()

    print("Thanks for playing!")


if __name__ == "__main__":
    main()
