import string

def word_freq_filtered(text):
    stopwords = {'the', 'and', 'in', 'of', 'a', 'to', 'is'}
    
    clean_text = text.lower().translate(str.maketrans("", "", string.punctuation))
    words = clean_text.split()
    
    freq = {}
    for word in words:
        if word not in stopwords:
            freq[word] = freq.get(word, 0) + 1
    return freq

match_summary = 'Virat scored 100, Rohit scored 80, and Gill scored 50 in the IPL match'
print(word_freq_filtered(match_summary))