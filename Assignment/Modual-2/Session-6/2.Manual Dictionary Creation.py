usernames = ["alex_vlogs", "tech_insider", "foodie_delight", "code_master"]
follower_counts = [12500, 89000, 3400, 52000]

instagram_followers = {}

for i in range(len(usernames)):
    instagram_followers[usernames[i]] = follower_counts[i]

print("Instagram Followers Dict:", instagram_followers)