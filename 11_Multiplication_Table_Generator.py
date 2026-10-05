# Multiplication Table Generator

num = int(input("Enter a number: "))

for i in range(1, 21):
    print(f"{num} x {i} = {num * i}")

# Challenge: Generate a multiplication table without using a for loop.

num = int(input("\nEnter a number: "))

i = 1

while i <= 10:
    print(f"{num} x {i} = {num * i}")
    i += 1