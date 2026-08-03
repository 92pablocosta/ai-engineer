def is_valid_guess(guess, guessed_letters):
    guess = guess.strip().lower()

    if len(guess) != 1:
        return False, "Digite apenas uma letra"
    pass
