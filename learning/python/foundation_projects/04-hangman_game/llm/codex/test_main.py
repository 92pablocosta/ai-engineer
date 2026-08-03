"""Tests for the Hangman game."""

import unittest

from main import ask_for_guess, play_round, word_is_complete, word_progress


def answers(*values: str):
    """Build a fake input function from a fixed sequence of answers."""
    iterator = iter(values)
    return lambda _prompt: next(iterator)


class HangmanTests(unittest.TestCase):
    def test_word_progress_reveals_guessed_letters(self) -> None:
        self.assertEqual(word_progress("python", {"p", "h"}), "p _ _ h _ _")

    def test_word_is_complete_ignores_duplicate_letters(self) -> None:
        self.assertTrue(word_is_complete("letter", {"l", "e", "t", "r"}))
        self.assertFalse(word_is_complete("letter", {"l", "e", "t"}))

    def test_guess_is_trimmed_and_normalized(self) -> None:
        self.assertEqual(ask_for_guess(set(), answers(" P "), lambda _text: None), "p")

    def test_invalid_and_repeated_guesses_are_rejected(self) -> None:
        messages: list[str] = []
        guess = ask_for_guess(
            {"a"},
            answers("", "ab", "4", "A", "b"),
            messages.append,
        )

        self.assertEqual(guess, "b")
        self.assertEqual(len(messages), 4)

    def test_winning_round(self) -> None:
        output: list[str] = []
        won = play_round("cat", answers("c", "a", "t"), output.append)

        self.assertTrue(won)
        self.assertIn("You won! The word was 'cat'.", output)

    def test_losing_round(self) -> None:
        output: list[str] = []
        won = play_round(
            "cat",
            answers("b", "d", "e", "f", "g", "h"),
            output.append,
        )

        self.assertFalse(won)
        self.assertIn("You lost. The word was 'cat'.", output)


if __name__ == "__main__":
    unittest.main()
