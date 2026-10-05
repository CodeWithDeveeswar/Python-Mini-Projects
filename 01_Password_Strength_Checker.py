# Password Strength Checker
# Check if a password is strong using at least 8 characters, one uppercase letter, one digit and one symbol.
# Concepts: CONDITIONALS • STRINGS • REGEX

import re

password = input("Enter password: ")

strong = (len(password) >= 8 and 
          re.search(r'[A-Z]', password) and 
          re.search(r'[0-9]', password) and
          re.search(r'[!@#$%^&]', password))

print("Strong 💪" if strong else "Weak 🤪")