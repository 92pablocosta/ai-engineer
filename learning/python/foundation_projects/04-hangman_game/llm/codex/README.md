# 4. Hangman Game

## Objective

Create a terminal Hangman game where the program picks a secret word and the player guesses letters.

## Minimum Features

- Pick a random word from a list or file.
- Track guessed letters and remaining attempts.
- Display the word progress (`_ y t _ o n`) after each guess.
- Reject invalid input (more than one character, repeated guesses).
- End the game with a win/loss message.

## Concepts Practiced

- Functions, loops, conditions, lists, `try`/`except`, the `random` module

## Extra Challenge

Load the word list from a `.txt` file and pick a category before each round.

## Run the Game

Python 3.9 or newer is recommended. No third-party packages are needed.

```bash
python3 main.py
```

Enter one letter at a time. The game shows the letters you have tried and how
many incorrect guesses remain. At the end of a round, choose whether to play
again.

## Run the Tests

```bash
python3 -m unittest -v
```

## Project Structure

- `main.py` contains the game and its terminal entry point.
- `test_main.py` covers progress display, validation, wins, and losses.
