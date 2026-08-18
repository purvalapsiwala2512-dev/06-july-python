ipl_scores = {
    "Mumbai Indians": {
        "Rohit Sharma": 68,
        "Suryakumar Yadav": 83,
        "Ishan Kishan": 31
    },
    "Royal Challengers Bengaluru": {
        "Virat Kohli": 92,
        "Faf du Plessis": 54,
        "Dinesh Karthik": 28
    }
}

team_name = "Royal Challengers Bengaluru"
player_name = "Virat Kohli"

runs = ipl_scores[team_name][player_name]
print(f"Runs scored by {player_name} ({team_name}): {runs}")