# Reverse a String 

text = "Python"

# Method 1: Slicing
print(text[::-1])

# Method 2: reversed()
print("".join(reversed(text)))

# Method 3: Loop
rev = ""
for char in text:
    rev = char + rev
print(rev)