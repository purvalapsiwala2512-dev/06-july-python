def format_follower_count(number):
    if number >= 1_000_000:
        return f"{number / 1_000_000:.1f}M"
    elif number >= 1_000:
        return f"{number / 1_000:.1f}K"
    else:
        return str(number)

print(f"--- Task 2 ---")
print(f"1500 becomes: {format_follower_count(1500)}")
print(f"1200000 becomes: {format_follower_count(1200000)}")
print(f"850 becomes: {format_follower_count(850)}\n")