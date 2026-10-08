# Dice Rolling Simulator

import random

while True:
    roll = input("\nPress Enter to roll dice \
                 \n(Type 'q' to stop) 🎲: ")

    if roll.lower() == 'q':
        print("Game Over! 👋")
        break

    dice = random.randint(1, 6)

    print(f"You got: {dice} 🎲")

# Challenge: Simulate rolling two dice using the random module and a while loop.

"""
import random

while True:
    roll = input("\nPress Enter to roll two dice \
                 \n(Type 'q' to stop) 🎲: ")

    if roll.lower() == "q":
        print("Game Over! 👋")
        break

    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)

    print(f"Dice 1: {dice1} 🎲")
    print(f"Dice 2: {dice2} 🎲")
    print(f"Total: {dice1 + dice2}")
"""