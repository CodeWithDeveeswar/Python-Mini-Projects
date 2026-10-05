# Number Guessing Game

import random

secret_num = random.randint(1, 50)
attempts = 0

while True:
    guess = int(input("Guess (1 - 50): "))
    attempts += 1

    if guess == secret_num:
        print(f"Correct! In {attempts} tries 🎉")
        break
    elif guess < secret_num:
        print("Too low")
    else:
        print("Too high")