# Palindrome Checker

word = input("Enter a word: ").lower()

reversed_word = word[::-1]

if word == reversed_word:
    print(f"{word} is a Palindrome ✅")
else:
    print(f"{word} is Not a Palindrome ❌")