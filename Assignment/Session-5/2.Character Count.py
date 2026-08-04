user_bio = 'Music lover | Foodie | Traveller'
character_count = 0

for char in user_bio:
    if char != ' ':
        character_count = character_count + 1

print("Total characters (excluding spaces):", character_count)
print()