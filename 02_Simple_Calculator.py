# Simple Calculator
# Perform basic arithmetic operations using input handling and if-elif.
# Concepts: INPUT • CONDITIONALS • ARITHMETIC • F-STRINGS

num1 = float(input("First number: "))
num2 = float(input("Second number: "))
op = input("Operator (+ - * /): ")

if op == "+":
    result = num1 + num2
elif op == "-":
    result = num1 - num2
elif op == "*":
    result = num1 * num2
elif op == "/":
    result = num1 / num2

print(f"Result: {result}")