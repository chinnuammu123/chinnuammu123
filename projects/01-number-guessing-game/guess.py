"""Number Guessing Game - a first Python project.

The computer picks a secret number and you try to guess it.
After each guess it tells you if you are too high or too low.
"""
import random


def play(low=1, high=100):
    secret = random.randint(low, high)
    attempts = 0
    print(f"I'm thinking of a number between {low} and {high}.")

    while True:
        text = input("Your guess: ")
        if not text.strip().isdigit():
            print("Please type a whole number.")
            continue

        guess = int(text)
        attempts += 1

        if guess < secret:
            print("Too low! ⬇️")
        elif guess > secret:
            print("Too high! ⬆️")
        else:
            print(f"🎉 Correct! You got it in {attempts} tries.")
            return attempts


if __name__ == "__main__":
    play()
