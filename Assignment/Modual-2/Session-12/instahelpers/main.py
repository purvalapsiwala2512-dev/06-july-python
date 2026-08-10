from instahelpers import format_likes

test_counts = [85, 999, 1200, 1500000, 2300000]

for count in test_counts:
    print(f"Likes: {count:<10} -> Formatted: {format_likes(count)}")