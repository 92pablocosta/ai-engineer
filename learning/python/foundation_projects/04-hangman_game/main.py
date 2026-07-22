from rich import print
import random

words = [
    "pickle",
    "banana",
    "unicorn",
    "waffle",
    "noodle",
    "penguin",
    "taco",
    "squirrel",
    "popcorn",
    "marshmallow",
]

secret_word = random.choice(words)
hangman = list()
for _i in range(len(secret_word)):
    hangman.append('_')

print(hangman)

while True:
        
    guess = input("Type a letter: ")
    if guess == '0':
        break
    if guess in secret_word:
        for index, letter in enumerate(secret_word):
            if guess == letter:
                hangman[index] = guess

    print(" ".join(hangman))
