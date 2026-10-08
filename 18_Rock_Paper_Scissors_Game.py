# Rock Paper Scissors Game

import random

choices = ["rock", "paper", "scissors"]
user = input("Rock, Paper, or Scissors? ").lower()
comp = random.choice(choices)

print(f"Computer chose: {comp}")

if user == comp:
    print("It's a tie! 🤝")
elif (user == "rock" and comp == "scissors") or \
     (user == "paper" and comp == "rock") or \
     (user == "scissors" and comp == "paper"):
    print("You win! 🎉")
else:
    print("Computer wins! 🤖")