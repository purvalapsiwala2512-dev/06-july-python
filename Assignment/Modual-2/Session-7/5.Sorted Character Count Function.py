def char_count_dict(text):
    freq = {}
    for char in text:
        freq[char] = freq.get(char, 0) + 1
    return freq

sample_text = "programming"
counts = char_count_dict(sample_text)

sorted_counts = {char: counts[char] for char in sorted(counts.keys())}

print("Sorted Character Frequency:", sorted_counts)