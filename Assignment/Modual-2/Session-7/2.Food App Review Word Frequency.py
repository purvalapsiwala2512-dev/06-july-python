import string

review = """Swiggy is super fast! The food delivery was on time, 
and the food quality was great. Swiggy never disappoints!"""

clean_review = review.lower().translate(str.maketrans("", "", string.punctuation))
words = clean_review.split()

word_counts = {}
for word in words:
    word_counts[word] = word_counts.get(word, 0) + 1

print("Word Frequency:", word_counts)