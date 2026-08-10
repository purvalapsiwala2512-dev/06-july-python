users = [('raj', 800), ('simran', 1500), ('veer', 1200), ('ananya', 950)]

k_badge_users = [username for username, followers in filter(lambda u: u[1] > 1000, users)]

print("Usernames eligible for 'K' badge:", k_badge_users)