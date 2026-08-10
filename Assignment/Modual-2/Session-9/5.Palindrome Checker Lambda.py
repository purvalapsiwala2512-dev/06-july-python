is_palindrome = lambda text: text == text[::-1]

test_words = ['madam', 'python', 'noon']

for word in test_words:
    print(f"'{word}': {is_palindrome(word)}")