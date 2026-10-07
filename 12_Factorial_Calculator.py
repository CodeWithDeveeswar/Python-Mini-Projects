# Factorial Calculator

# Method 1: Loop
def factorial_loop(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

# Method 2: Recursion
def factorial_recursion(n):
    if n <= 1:
        return 1
    return n * factorial_recursion(n - 1) 

print(factorial_loop(5))
print(factorial_recursion(5))