# Random Password Generator

import random
import string

# Character pool
chars = string.ascii_letters + string.digits + \
    string.punctuation

# Length of password
length = int(input("Password Length: "))

# Generate random password
password = "".join(random.choices(chars, k=length))

print(f"Generated Password: {password}")