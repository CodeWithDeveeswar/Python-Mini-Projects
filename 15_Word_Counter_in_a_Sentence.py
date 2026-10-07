# Word Counter in a Sentence

# 1. Get user input
sentence = input("Type the sentence: ")

# 2. Split words and count length
words = sentence.split()
word_count = len(words)

# 3. Print output
print(f"Total Words: {word_count} 📝")

# Challenge: Count words without using split()

Sentence = input("Type the sentence: ")

total_words = 0
in_word = False

for char in Sentence:
    if char != " " and not in_word:
        total_words += 1
        in_word = True
    elif char == " ":
        in_word = False

print(f"Total Words: {total_words} 📝")

