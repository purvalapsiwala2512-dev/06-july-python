text = input("Enter a string: ")

char_counts = {}
for char in text:
    char_counts[char] = char_counts.get(char, 0) + 1

print("Character Frequency:", char_counts)