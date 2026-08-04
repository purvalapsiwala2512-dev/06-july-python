user_word = input("Enter a word (like a song name): ")

for char in user_word:
    c = char.lower()
    if c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u':
        print(char)