# Fibonacci Series Generator

n = int(input("How many terms: "))

a, b = 0, 1

for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b

# Challenge: Generate the Fibonacci series using a recursive function

num = int(input("\nHow many terms: "))

def fibonacci(num):
    if num <= 1:
        return num
    return fibonacci(num - 1) + fibonacci(num - 2)

for i in range(num):
    print(fibonacci(i), end=" ")