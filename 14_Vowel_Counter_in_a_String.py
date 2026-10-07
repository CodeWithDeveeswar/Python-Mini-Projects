# Vowel Counter in a String 

text = input("Enter a sentence: ")

vowels = "aeiou"
count = 0

for char in text:
    if char in vowels:
        count += 1

print(f"Total Vowels: {count}")

# Challenge: Can you solve this in one line using sum() and list comprehension?

Text = input("Enter a sentence: ")

vowels = "aeiou"

print(f"Total Vowels: {sum(1 for char in Text if char in vowels)}")